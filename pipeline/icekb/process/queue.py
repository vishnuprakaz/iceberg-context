"""Find meetings and threads that need (re-)extraction and write one input bundle per item under .work/queue/."""
from __future__ import annotations

import datetime as dt
import json
import re
from collections import defaultdict
from pathlib import Path

from icekb.integrate.store import Data
from icekb.util import sha

THREAD_KINDS = {"vote", "result", "discuss", "release-planning", "roster", "release-vote"}


def _extract_state(root: Path, rel: str) -> str | None:
    path = root / "data" / "extract" / rel
    return json.loads(path.read_text()).get("_input_hash") if path.exists() else None


def meeting_units(data: Data) -> dict[tuple[str, str], dict]:
    """Pair each notes section with its recording: by the video link in the notes, else same group within one day."""
    videos = [v for v in data.by_type["transcript"] if v["meta"].get("group")]
    by_id = {v["meta"]["video"]: v for v in videos}
    units, used = {}, set()
    for n in data.by_type["meeting-notes"]:
        if n["meta"]["status"] in ("cancelled", "upcoming"):
            continue
        group, date = n["meta"]["group"], n["date"][:10]
        video = next((by_id[v] for v in n["meta"].get("recordings", []) if v in by_id), None)
        if video is None:
            day = dt.date.fromisoformat(date)
            video = next((v for v in videos if v["meta"]["group"] == group and v["id"] not in used
                          and abs((dt.date.fromisoformat(v["date"][:10]) - day).days) <= 1), None)
        if video:
            used.add(video["id"])
        units[(group, date)] = {"notes": n, "video": video}
    for v in videos:
        if v["id"] not in used:
            units.setdefault((v["meta"]["group"], v["date"][:10]), {"notes": None, "video": v})
    return units


def queue_meetings(data: Data, since: str, transcripts_since: str, force: bool = False) -> list[dict]:
    out_dir = data.root / ".work" / "queue" / "meetings"
    out_dir.mkdir(parents=True, exist_ok=True)
    items = []
    for (group, date), unit in sorted(meeting_units(data).items()):
        if date < since or date > data.today.isoformat():
            continue
        notes, video = unit["notes"], unit["video"]
        thin = not notes or len(notes["body"]) < 500
        use_video = video is not None and (date >= transcripts_since or thin)
        if not notes and not use_video:
            continue
        input_hash = sha((notes or {}).get("hash", "") + (video["hash"] if use_video else ""))
        rel = f"meetings/{group}/{date}.json"
        if not force and _extract_state(data.root, rel) == input_hash:
            continue
        name = next(g["name"] for g in data.cfg["groups"] if g["slug"] == group)
        parts = [f"# Extraction input: {name}, {date}", "", f"- extraction id: `meeting/{group}/{date}`",
                 f"- write the result to: `data/extract/{rel}`", f"- `_input_hash`: `{input_hash}`",
                 "- sources: " + ", ".join(f"`{s['id']}`" for s in (notes, video if use_video else None) if s), ""]
        if notes:
            parts += [f"## Notes document section (`{notes['id']}`)" + (" — contains AI-generated notes" if notes.get("ai_generated") else ""),
                      "", notes["body"], ""]
            if notes["refs"]:
                parts += ["References found in the notes: " + ", ".join(notes["refs"][:60]), ""]
        if use_video:
            parts += [f"## Recording transcript (`{video['id']}`, {video['url']})", "",
                      "Auto-generated captions: no speaker names, and project terms are sometimes misheard. "
                      "Timestamps in [h:mm:ss] mark paragraph starts.", "", video["body"], ""]
        elif video:
            parts += [f"(A recording exists, `{video['id']}`, but its transcript is not part of this input.)", ""]
        path = out_dir / f"{group}__{date}.md"
        path.write_text("\n".join(parts), encoding="utf-8")
        items.append({"id": f"meeting/{group}/{date}", "group": group, "date": date, "input": str(path.relative_to(data.root)),
                      "output": f"data/extract/{rel}", "chars": sum(len(p) for p in parts), "has_transcript": use_video})
    return items


def queue_threads(data: Data, since: str, min_messages: int = 4, force: bool = False) -> list[dict]:
    out_dir = data.root / ".work" / "queue" / "threads"
    out_dir.mkdir(parents=True, exist_ok=True)
    by_thread = defaultdict(list)
    for mail in data.by_type["email"]:
        by_thread[mail["meta"]["thread"]].append(mail)
    items = []
    for tid, mails in sorted(by_thread.items()):
        last = max(m["date"] for m in mails)
        kinds = {m["meta"]["kind"] for m in mails}
        if last[:10] < since or len(mails) < min_messages or not (kinds & THREAD_KINDS):
            continue
        input_hash = sha("".join(m["hash"] for m in mails))
        rel = f"threads/{tid}.json"
        if not force and _extract_state(data.root, rel) == input_hash:
            continue
        subject = mails[0]["meta"]["subject"]
        parts = [f"# Extraction input: dev-list thread “{subject}”", "", f"- extraction id: `thread/{tid}`",
                 f"- write the result to: `data/extract/{rel}`", f"- `_input_hash`: `{input_hash}`",
                 f"- messages: {len(mails)}, from {mails[0]['date'][:10]} to {last[:10]}", ""]
        for m in mails:
            who = m["people"][0]
            parts += [f"## `{m['id']}` · {m['date'][:16]} · {who.removeprefix('name:')}", "", m["body"][:3500], ""]
        slug = re.sub(r"[^a-z0-9]+", "-", subject.lower()).strip("-")[:60]
        path = out_dir / f"{tid}.md"
        path.write_text("\n".join(parts), encoding="utf-8")
        items.append({"id": f"thread/{tid}", "subject": subject, "slug": slug, "input": str(path.relative_to(data.root)),
                      "output": f"data/extract/{rel}", "chars": sum(len(p) for p in parts), "messages": len(mails)})
    return items
