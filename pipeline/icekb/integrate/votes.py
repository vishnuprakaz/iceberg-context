"""Tally dev-list votes from the raw messages, with binding status taken from the ASF roster.

Binding votes in Apache Iceberg are those of PMC members (including for the Rust, Go, C++, Python and other
sub-project releases, which share the one PMC). A voter's status is decided from the roster as of the vote date:

- binding:      the sender resolves to a GitHub login whose ASF roster entry is PMC since on or before that date;
- non-binding:  the sender resolves to a login that was not on the PMC then;
- unverified:   the sender could not be resolved to a login, so only what they declared ("(binding)") is known.

The tally is compared with the counts stated in the [RESULT] email when one exists, so a wrong parse shows up as a
mismatch instead of a silently wrong number. Output: kb/index/votes.jsonl, read by `kb votes`.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from collections import defaultdict
from pathlib import Path

from icekb.identity import Identity
from icekb.util import iter_raw

VOTE_KINDS = {"vote", "release-vote"}

_QUOTE_START = [
    re.compile(r"^\s*On [^\n]{5,300}\n?[^\n]{0,200}wrote:\s*$", re.M),
    re.compile(r"^\s*\*?\*?From:\*?\*?\s", re.M),
    re.compile(r"^-{3,}\s*Original Message", re.M | re.I),
    re.compile(r"^_{5,}\s*$", re.M),
    re.compile(r"^\s*>", re.M),
    re.compile(r"^\s*(Le|Am) [^\n]{5,200}(a écrit|schrieb)", re.M),
]
_VALUE = r"(\+1|\+0|-0|-1|0)(?=[\s(,!:;]|\.(?!\d)|$)"
_LINE_VOTE = re.compile(r"^\s*(?:\[\s*[xX]\s*\]\s*)?(?:(?:my|i)\s+(?:own\s+)?vote(?:\s+is)?\s*:?\s*|vote\s*:\s*)?" + _VALUE, re.I)
_INLINE_VOTE = re.compile(r"(?<![\w.+-])" + r"(\+1|\+0|-0|-1)(?![\d.])")
_IN_THREAD_RESULT = re.compile(r"^\s*(the )?(vote|this) (passes|passed|has passed|fails|failed)|^\s*(closing|i'?m closing) (the|this) vote",
                               re.I | re.M)
_DECLARED_NB = re.compile(r"non[\s-]?binding|not binding|nb\b", re.I)
_DECLARED_B = re.compile(r"\bbinding\b", re.I)


def own_part(body: str) -> str:
    """The sender's own words: everything before the first quoted-reply marker."""
    cut = len(body)
    for pat in _QUOTE_START:
        m = pat.search(body)
        if m:
            cut = min(cut, m.start())
    return body[:cut]


def parse_vote(body: str, opener: bool = False) -> tuple[str, str | None] | None:
    """Return (value, declared) for a message, where value is '+1', '0' or '-1' and declared is
    'binding', 'non-binding' or None. Template lines such as '[ ] +1 Release this' are ignored."""
    text = own_part(body)
    lines = [ln for ln in text.splitlines() if not re.match(r"^\s*\[\s*\]", ln)]
    hit = None
    for ln in lines:
        m = _LINE_VOTE.match(ln)
        if m:
            hit = (m.group(1), ln)
            break
    if hit is None and not opener:
        head = "\n".join(lines)[:400]
        m = _INLINE_VOTE.search(head)
        if m:
            line = head[head.rfind("\n", 0, m.start()) + 1: head.find("\n", m.end()) if "\n" in head[m.end():] else None]
            hit = (m.group(1), line)
    if hit is None:
        return None
    raw, line = hit
    value = {"+1": "+1", "-1": "-1"}.get(raw, "0")
    declared = "non-binding" if _DECLARED_NB.search(line) else "binding" if _DECLARED_B.search(line) else None
    return value, declared


def subject_key(subject: str) -> str:
    """A vote and its separately posted result share a subject once tags and 'Re:' are removed."""
    s = re.sub(r"\[[^\]]*\]|^\s*((re|fwd?|aw)\s*:\s*)+", " ", subject.lower())
    return " ".join(re.sub(r"[^a-z0-9. ]+", " ", s).split())


def result_status(text: str) -> str:
    text = text.lower()
    if re.search(r"\b(passes|passed)\b|vote is successful|vote succeeded|has been accepted|is accepted", text) and not re.search(
            r"\b(not|n't) pass", text):
        return "passed"
    if re.search(r"vote (has )?(fails|failed)|did not pass|not enough|\bcancel", text):
        return "failed"
    return "result-posted"


def stated_counts(text: str) -> dict:
    """Counts of +1 votes stated in a [RESULT] email, when the email states them."""
    t = own_part(text)
    low = t.lower()
    out: dict[str, int] = {}
    num = r"(?<![+\-\d.])(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)"
    words = {w: i + 1 for i, w in enumerate("one two three four five six seven eight nine ten eleven twelve".split())}

    def as_int(s: str) -> int:
        return int(s) if s.isdigit() else words[s]

    for key, pats in (
        ("binding", [rf"{num}\s*\+1\s*\(?binding", rf"{num}\s*binding\s*\+1", rf"{num}\s*binding\s*(?:votes?|\+1s?)",
                     rf"binding\s*(?:votes?)?\s*[:(]\s*{num}\b", rf"\+1\s*\(?binding\)?\s*(?:votes?)?\s*[:(]\s*{num}\b"]),
        ("non-binding", [rf"{num}\s*\+1\s*\(?non[\s-]?binding", rf"{num}\s*non[\s-]?binding\s*(?:\+1|votes?)",
                         rf"non[\s-]?binding\s*(?:votes?)?\s*[:(]\s*{num}\b", rf"\+1\s*\(?non[\s-]?binding\)?\s*(?:votes?)?\s*[:(]\s*{num}\b"]),
    ):
        for p in pats:
            m = re.search(p, low)
            if m:
                out[key] = as_int(m.group(1))
                break
    if "binding" not in out:
        listed = _listed(t)
        out.update(listed)
    return out


def _listed(text: str) -> dict:
    """Count names listed under 'Binding:' and 'Non-binding:' headings."""
    out, current = {}, None
    for ln in text.splitlines():
        s = ln.strip().strip("*").strip()
        head = re.match(r"^(\+1\s*)?\(?(non[\s-]?binding|binding)\)?(\s*\+1)?(\s*votes?)?\s*(\(\d+\))?\s*:?\s*$", s, re.I)
        if head:
            current = "non-binding" if head.group(2).lower().startswith("non") else "binding"
            out.setdefault(current, 0)
            continue
        if current is None:
            continue
        if not s:
            if out[current]:
                current = None
            continue
        if re.match(r"^(\+0|0|-1|-0|thanks|vote thread|i'?ll|regards|best)", s, re.I):
            current = None
            continue
        out[current] += 1
    return {k: v for k, v in out.items() if v}


def _deadline(opened: str, body: str) -> str:
    m = re.search(r"(\d{2,3})\s*(?:\+\s*)?hours", body.lower())
    hours = int(m.group(1)) if m and 24 <= int(m.group(1)) <= 240 else 72
    start = dt.datetime.strptime(opened, "%Y-%m-%dT%H:%M:%SZ")
    return (start + dt.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")


def pmc_roster(root: Path) -> dict[str, str]:
    """GitHub login -> date the person joined the PMC (only resolved PMC members)."""
    out = {}
    for r in iter_raw(root, "asf"):
        meta = r.get("meta") or {}
        login = (r.get("people") or [""])[0]
        if meta.get("role") == "pmc" and login and not login.startswith("asf:"):
            out[login] = meta.get("pmc_since") or "1970-01-01"
    return out


def _status(person: str, date: str, pmc: dict[str, str]) -> str:
    if person.startswith("name:") or person.startswith("asf:") or not person:
        return "unverified"
    since = pmc.get(person)
    return "binding" if since and since <= date[:10] else "non-binding"


def build(root: Path) -> list[dict]:
    mails = [r for r in iter_raw(root, "devlist") if r.get("type") == "email"]
    pmc = pmc_roster(root)
    identity = Identity(root)
    for m in mails:  # names that were unknown when the message was collected may be known now
        people = m.get("people") or []
        if people and people[0].startswith("name:"):
            m["people"] = [identity.resolve(people[0][5:]) or people[0]] + people[1:]
    threads: dict[str, list[dict]] = defaultdict(list)
    results: dict[str, list[dict]] = defaultdict(list)
    for m in mails:
        kind = m["meta"].get("kind")
        if kind in VOTE_KINDS:
            threads[m["meta"]["thread"]].append(m)
        elif kind == "result":
            results[subject_key(m["meta"].get("subject") or m["title"])].append(m)

    # Group threads that are one vote split in two (same subject, started within 14 days of each other).
    groups: dict[str, list[list[dict]]] = defaultdict(list)
    for msgs in sorted(threads.values(), key=lambda ms: min(x["date"] for x in ms)):
        msgs.sort(key=lambda x: x["date"])
        key = subject_key(msgs[0]["meta"].get("subject") or msgs[0]["title"])
        bucket = groups[key]
        if bucket and msgs[0]["date"][:10] <= _plus_days(bucket[-1][0]["date"], 14):
            bucket[-1].extend(msgs)
        else:
            bucket.append(list(msgs))

    rows = []
    for key, runs in groups.items():
        for i, msgs in enumerate(runs):
            msgs.sort(key=lambda x: x["date"])
            first = next((x for x in msgs if not x["meta"].get("reply")), msgs[0])
            nxt = runs[i + 1][0]["date"] if i + 1 < len(runs) else "9999"
            rows.append(_vote_row(key, first, msgs, results.get(key, []), nxt, pmc))
    rows.sort(key=lambda r: r["opened"], reverse=True)
    # A release candidate with no result that is followed by a later candidate for the same release was superseded.
    newest: dict[str, dict] = {}
    for r in rows:  # newest first
        if r["kind"] != "release-vote":
            continue
        base = re.sub(r"\brc\s*\d+\b", "", subject_key(r["subject"])).strip()
        if base in newest and not r.get("result"):
            r["superseded_by"] = newest[base]["id"]
        newest.setdefault(base, r)
    return rows


def _plus_days(ts: str, days: int) -> str:
    return (dt.date.fromisoformat(ts[:10]) + dt.timedelta(days=days)).isoformat()


def _vote_row(key: str, first: dict, msgs: list[dict], result_mails: list[dict], until: str, pmc: dict) -> dict:
    res = next((r for r in sorted(result_mails, key=lambda r: r["date"])
                if first["date"] <= r["date"] < until and not r["title"].lower().startswith("re:")), None)
    res = res or next((m for m in msgs if m["meta"].get("kind") == "result"), None)
    res = res or next((m for m in reversed(msgs) if m is not first and _IN_THREAD_RESULT.search(own_part(m.get("body") or ""))),
                      None)
    latest: dict[str, dict] = {}
    for m in msgs + ([res] if res is not None and res not in msgs else []):
        is_result = m is res
        if m["meta"].get("kind") not in VOTE_KINDS and not is_result:
            continue
        person = (m.get("people") or [""])[0]
        if not person or (is_result and person in latest):
            continue
        # In a result message only an explicit line such as "My vote is +1 (binding)" counts.
        parsed = parse_vote(m.get("body") or "", opener=m is first or is_result)
        if not parsed:
            continue
        value, declared = parsed
        latest[person] = {"who": person, "value": value, "declared": declared,
                          "status": _status(person, m["date"], pmc), "date": m["date"], "source": m["id"]}
    votes = sorted(latest.values(), key=lambda v: v["date"])
    tally = {s: {"+1": 0, "0": 0, "-1": 0} for s in ("binding", "non-binding", "unverified")}
    for v in votes:
        tally[v["status"]][v["value"]] += 1
    row = {
        "id": f"vote:{first['meta']['thread']}",
        "subject": re.sub(r"^\s*((re|fwd?)\s*:\s*)+", "", first["meta"].get("subject") or first["title"], flags=re.I),
        "kind": first["meta"].get("kind"),
        "opened": first["date"],
        "opener": (first.get("people") or [""])[0],
        "url": first["url"],
        "source": first["id"],
        "deadline": _deadline(first["date"], first.get("body") or ""),
        "messages": len(msgs),
        "votes": votes,
        "tally": tally,
    }
    if res:
        stated = stated_counts(res.get("body") or "")
        row["result"] = {"status": result_status(own_part(res.get("body") or "")), "date": res["date"], "url": res["url"],
                         "source": res["id"], "by": (res.get("people") or [""])[0], "stated": stated}
        if "binding" in stated:
            counted = tally["binding"]["+1"]
            declared = sum(1 for v in votes if v["status"] == "unverified" and v["value"] == "+1" and v["declared"] == "binding")
            if counted == stated["binding"]:
                row["check"] = "match"
            elif declared and counted + declared == stated["binding"]:
                row["check"] = f"match if the {declared} unverified voter(s) who declared binding are counted"
            else:
                row["check"] = f"result email states {stated['binding']} binding +1, counted {counted}" + (
                    f" ({tally['unverified']['+1']} unverified)" if tally["unverified"]["+1"] else "")
    return row


def render(rows: list[dict]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows)
