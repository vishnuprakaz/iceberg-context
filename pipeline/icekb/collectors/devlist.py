"""Collect the dev mailing list from the Apache PonyMail archive, one mbox per month."""
from __future__ import annotations

import datetime as dt
import email
import email.header
import email.utils
import hashlib
import json
import mailbox
import re
import tempfile
from pathlib import Path

import yaml

from icekb import state
from icekb.identity import Identity
from icekb.util import clean_text, extract_refs, http_get, sha, strip_emails, upsert

_REPLY_PREFIX = re.compile(r"^((re|fwd?|aw)\s*:\s*)+", re.I)
_REPO_HINTS = (("rust", "apache/iceberg-rust"), ("pyiceberg", "apache/iceberg-python"), ("python", "apache/iceberg-python"),
               ("iceberg-go", "apache/iceberg-go"), ("[go]", "apache/iceberg-go"), ("c++", "apache/iceberg-cpp"),
               ("cpp", "apache/iceberg-cpp"))


def _decode(value) -> str:
    if value is None:
        return ""
    try:
        return str(email.header.make_header(email.header.decode_header(str(value))))
    except Exception:
        return str(value)


def _body(msg) -> str:
    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", "replace")
            return ""
        return msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", "replace")
    except Exception:
        return ""


def own_text(body: str) -> str:
    """Keep what the sender wrote: drop quoted lines, 'On … wrote:' headers and the signature."""
    out = []
    for line in body.replace("\r\n", "\n").split("\n"):
        if line.startswith(">"):
            continue
        if line.strip() == "--" or line.startswith("-----Original Message"):
            break
        if re.match(r"^(On .{5,200} wrote:|Le .{5,200} a écrit\s*:|Am .{5,200} schrieb.*:)\s*$", line.strip()):
            continue
        out.append(line)
    return "\n".join(out)


def classify(subject: str) -> str:
    """Thread kind from the subject line. Prefixes are matched literally and case-insensitively."""
    s = _REPLY_PREFIX.sub("", subject.strip()).lower()
    tags = set(re.findall(r"\[([a-z ]+)\]", s))
    if "result" in tags:
        return "result"
    if "vote" in tags:
        return "release-vote" if re.search(r"\brelease\b|\brc\s?\d", s) else "vote"
    if "announce" in tags or s.startswith("announce"):
        return "announce"
    if tags & {"discuss", "discussion", "proposal"}:
        return "release-planning" if re.search(r"\brelease\b", s) else "discuss"
    if re.search(r"new (committer|pmc member)", s):
        return "roster"
    if re.search(r"\bsync\b|\bmeetup\b|\bsummit\b", s):
        return "community"
    return "other"


def parse_mbox(raw: bytes, identity: Identity, permalinks: dict[str, str]) -> list[dict]:
    with tempfile.NamedTemporaryFile(suffix=".mbox") as tmp:
        tmp.write(raw)
        tmp.flush()
        records = []
        for msg in mailbox.mbox(tmp.name):
            mid = (msg.get("Message-ID") or "").strip()
            try:
                when = email.utils.parsedate_to_datetime(msg.get("Date")).astimezone(dt.timezone.utc)
            except Exception:
                continue
            if not mid:
                continue
            name, addr = email.utils.parseaddr(_decode(msg.get("From")))
            name = name or addr.split("@")[0]
            subject = " ".join(_decode(msg.get("Subject")).split())
            refs = (msg.get("References") or "").split()
            parent = (msg.get("In-Reply-To") or "").strip()
            # Message-IDs look like email addresses, so they are never stored: records are keyed by the
            # archive's own id, and threads by a short hash of the root Message-ID.
            thread = "t-" + hashlib.sha1((refs[0] if refs else parent or mid).encode()).hexdigest()[:16]
            text = clean_text(own_text(_body(msg)), limit=6000)
            lowered = subject.lower()
            repo = next((r for hint, r in _REPO_HINTS if hint in lowered), "apache/iceberg")
            link = permalinks.get(mid)
            key = link or "h-" + hashlib.sha1(mid.encode()).hexdigest()[:20]
            records.append({
                "id": f"devlist:{key}",
                "source": "devlist",
                "type": "email",
                "date": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "url": f"https://lists.apache.org/thread/{link}" if link else
                       "https://lists.apache.org/list.html?dev@iceberg.apache.org",
                "people": [identity.person(name)],
                "title": strip_emails(subject),
                "body": text,
                "refs": extract_refs(subject + "\n" + text, repo),
                "hash": sha(subject + text),
                "meta": {"thread": thread, "kind": classify(subject), "reply": bool(refs or parent),
                         "subject": strip_emails(_REPLY_PREFIX.sub("", subject).strip())},
            })
        return records


def _months(start: str, end: str) -> list[str]:
    y, m = int(start[:4]), int(start[5:7])
    out = []
    while f"{y:04d}-{m:02d}" <= end:
        out.append(f"{y:04d}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def collect(root: Path, *, backfill: bool = False, months: list[str] | None = None, mbox_dir: Path | None = None) -> dict:
    mbox_dir = Path(mbox_dir) if mbox_dir else None
    if isinstance(months, str):
        months = months.split(",")
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())["devlist"]
    api, lst, dom = cfg["api"], cfg["list"], cfg["domain"]
    st = state.load(root, "devlist")
    today = dt.datetime.now(dt.timezone.utc)
    this_month = today.strftime("%Y-%m")
    if months is None:
        if backfill or st.get("status") == "never":
            months = _months(cfg["history_start"], this_month)
        else:
            prev = (today.replace(day=1) - dt.timedelta(days=1)).strftime("%Y-%m")
            months = [prev, this_month] if today.day <= 7 else [this_month]
    identity = Identity(root)
    totals = {"new": 0, "changed": 0}
    for month in months:
        stats = json.loads(http_get(f"{api}/stats.lua?list={lst}&domain={dom}&d={month}"))
        permalinks = {e["message-id"]: e["mid"] for e in stats.get("emails", []) if e.get("message-id")}
        local = mbox_dir / f"{month}.mbox" if mbox_dir else None
        if local and local.exists() and month != this_month:
            raw = local.read_bytes()
        else:
            raw = http_get(f"{api}/mbox.lua?list={lst}@{dom}&date={month}", timeout=300)
            if local and month != this_month:
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(raw)
        counts = upsert(root, "devlist", parse_mbox(raw, identity, permalinks))
        totals = {k: totals[k] + counts[k] for k in totals}
    identity.save_unresolved("devlist")
    state.save(root, "devlist", ok=True, counts={"last_new": totals["new"], "last_changed": totals["changed"]},
               cursor=this_month)
    return totals
