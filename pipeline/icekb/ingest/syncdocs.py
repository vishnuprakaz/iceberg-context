"""Split a working group's running notes document into one record per meeting.

Input is the Markdown text export of the Google Doc (Drive connector `read_file_content`), saved to a file.
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import yaml

from icekb import state
from icekb.dates import find_date
from icekb.identity import Identity
from icekb.util import clean_text, extract_refs, sha, upsert

_TAB = re.compile(r"^# (.+?)\s{2,}$")
_LEAD = re.compile(r"^[#\s*_>\\-]*")
_LANG = (("pyiceberg", "apache/iceberg-python"), ("python", "apache/iceberg-python"), ("rust", "apache/iceberg-rust"),
         ("c++", "apache/iceberg-cpp"), ("cpp", "apache/iceberg-cpp"), ("golang", "apache/iceberg-go"), ("go", "apache/iceberg-go"),
         ("java", "apache/iceberg"))
_AGENDA_NAME = re.compile(r"\\?\[([A-Z][A-Za-z .'’-]{1,40}?)\\?\]")
_AI = re.compile(r"AI[ -]generated|Gemini notes|Granola|notes by gemini", re.I)


def tab_region(text: str, tab: str | None) -> str:
    """Keep only the named tab. The export marks each tab with a '# Title' line ending in two spaces."""
    if not tab:
        return text
    lines = text.split("\n")
    start = next((i for i, ln in enumerate(lines) if _TAB.match(ln) and _TAB.match(ln).group(1).strip().lower() == tab.lower()), None)
    if start is None:
        start = next((i for i, ln in enumerate(lines) if ln.strip().lower() == f"# {tab.lower()}"), None)
    if start is None:
        return text
    end = next((i for i in range(start + 1, len(lines)) if _TAB.match(lines[i])), len(lines))
    return "\n".join(lines[start + 1:end])


def heading_date(line: str) -> tuple[dt.date, str] | None:
    """A meeting heading is a short line that starts with a date, optionally followed by links or a remark."""
    if len(line) > 260:
        return None
    stripped = _LEAD.sub("", line)
    found = find_date(stripped[:40])
    if not found or found[1] > 2:
        return None
    rest = stripped[found[2]:].strip(" *_")
    plain = re.sub(r"\(?\\?\[[^\]]*\]\([^)]*\)[,\s]*\)?|<[^>]+>", "", rest).strip(" ()[]\\,:–-")
    if len(plain) > 60:
        return None
    return found[0], rest


def split_meetings(text: str) -> list[tuple[dt.date, str, str]]:
    sections, current = [], None
    for line in text.split("\n"):
        head = heading_date(line)
        if head:
            current = [head[0], head[1], []]
            sections.append(current)
        elif _TAB.match(line):
            current = None
        elif current is not None:
            current[2].append(line)
    return [(d, rest, "\n".join(body)) for d, rest, body in sections]


def refs_by_language(body: str) -> list[str]:
    """Bare '#12345' refers to the repository of the Java / Python / Rust / Go / C++ subsection it sits under.

    A subsection is a short label line; it covers the more-indented lines below it and ends at the next line
    indented the same or less.
    """
    default, repo, label_indent, refs = "apache/iceberg", "apache/iceberg", None, []
    for line in body.split("\n"):
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        label = re.sub(r"[^a-z+ ]", "", _LEAD.sub("", line).lower()).strip()
        target = None
        if 0 < len(label) < 30:
            target = next((t for word, t in _LANG if label == word or label.split(" ")[0] == word), None)
        if target:
            repo, label_indent = target, indent
        elif label_indent is not None and indent <= label_indent:
            repo, label_indent = default, None
        refs += extract_refs(line, repo)
    return list(dict.fromkeys(refs))


def ingest(root: Path, group: str, file: Path, modified: str | None = None) -> dict:
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    info = next(g for g in cfg["groups"] if g["slug"] == group)
    text = tab_region(Path(file).read_text(encoding="utf-8", errors="replace"), info.get("tab"))
    text = re.sub(r"\\([\[\]#!_*().~<>+-])", r"\1", text)  # the export escapes Markdown punctuation
    identity = Identity(root)
    today = dt.datetime.now(dt.timezone.utc).date()
    records = []
    for date, rest, body in split_meetings(text):
        cleaned = clean_text(body, limit=24000)
        heading = clean_text(rest)
        status = "cancelled" if re.search(r"cancel|no meeting|skipped", heading + cleaned[:200], re.I) else \
                 "upcoming" if date > today else "link-only" if len(re.sub(r"<[^>]+>|\(http[^)]*\)", "", cleaned)) < 150 else "held"
        refs = refs_by_language(heading + "\n" + body)
        names = {n.strip() for n in _AGENDA_NAME.findall(body)}
        for thanked in re.findall(r"\(Thanks,? ([^()!]{2,90}?)!?\)", body):
            names |= {n.strip() for n in re.split(r",| and | & ", thanked) if n.strip()}
        people = sorted({login for login in (identity.resolve(n) for n in names) if login})
        records.append({
            "id": f"meet:{group}:{date.isoformat()}",
            "source": "syncdocs",
            "type": "meeting-notes",
            "date": f"{date.isoformat()}T00:00:00Z",
            "url": f"https://docs.google.com/document/d/{info['doc']}",
            "people": people,
            "title": f"{info['name']} notes, {date.isoformat()}" + (" (cancelled)" if status == "cancelled" else ""),
            "body": (heading + "\n\n" if heading else "") + cleaned,
            "refs": refs,
            "hash": sha(heading + cleaned),
            "ai_generated": bool(_AI.search(heading + cleaned)),
            "meta": {"group": group, "status": status, "recordings": [r[3:] for r in refs if r.startswith("yt:")],
                     "names_seen": sorted(names)[:40]},
        })
    counts = upsert(root, f"syncdocs/{group}", records, by="year")
    identity.save_unresolved(f"syncdocs:{group}")
    st = state.load(root, "syncdocs")
    cursor = dict(st.get("cursor") or {})
    cursor[group] = {"modified": modified, "meetings": len(records), "latest": max((r["date"][:10] for r in records), default=None)}
    state.save(root, "syncdocs", ok=True, cursor=cursor,
               counts={"groups": len(cursor), "meetings": sum(c["meetings"] for c in cursor.values())})
    return {"meetings": len(records), **counts}
