"""Turn events from the public Iceberg Dev Events calendar into records.

Input is the JSON returned by the Calendar connector's `list_events`, saved to a file. Only public event
details are kept; creator and attendee fields are dropped.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
from pathlib import Path

import yaml

from icekb import state
from icekb.util import clean_text, extract_refs, sha, upsert


def match_group(title: str, groups: list[dict]) -> str | None:
    low = title.lower()
    best = None
    for g in groups:
        if any(x in low for x in g.get("exclude_match", [])):
            continue
        for frag in g.get("title_match", []):
            if frag in low and (best is None or len(frag) > best[0]):
                best = (len(frag), g["slug"])
    return best[1] if best else None


def ingest(root: Path, file: Path) -> dict:
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    data = json.loads(Path(file).read_text())
    records = []
    for ev in data.get("events", []):
        start = (ev.get("start") or {}).get("dateTime") or (ev.get("start") or {}).get("date")
        if not start or ev.get("status") == "cancelled":
            continue
        when = dt.datetime.fromisoformat(start)
        if when.tzinfo is None:
            when = when.replace(tzinfo=dt.timezone.utc)
        utc = when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        desc = html.unescape(re.sub(r"<br\s*/?>|</p>|</li>", "\n", ev.get("description") or ""))
        refs = extract_refs(desc, None)
        desc = clean_text(re.sub(r"<[^>]+>", "", desc), limit=1500)
        title = ev.get("summary") or "(untitled)"
        group = match_group(title, cfg["groups"])
        meta = {"group": group, "event_id": ev["id"], "series": ev.get("recurringEventId"), "join": ev.get("conferenceUrl")}
        doc = next((r[4:] for r in refs if r.startswith("doc:")), None)
        if doc:
            meta["notes_doc"] = f"https://docs.google.com/document/d/{doc}"
        records.append({
            "id": f"cal:{ev['id']}",
            "source": "calendar",
            "type": "event",
            "date": utc,
            "url": ev.get("htmlLink") or "https://iceberg.apache.org/community/",
            "title": title,
            "body": desc,
            "refs": refs,
            "hash": sha(title + utc + desc),
            "meta": {k: v for k, v in meta.items() if v},
        })
    counts = upsert(root, "calendar", records)
    unmatched = sorted({r["title"] for r in records if not r["meta"].get("group")})
    state.save(root, "calendar", ok=True, counts={"events": len(records), "last_new": counts["new"]},
               cursor={"through": max((r["date"] for r in records), default=None), "titles_without_group": unmatched})
    return {"events": len(records), **counts, "titles_without_group": unmatched}
