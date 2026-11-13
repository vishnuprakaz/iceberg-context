"""Validate AI extractions against their sources and render them as record pages.

An extraction is rejected when it fails its schema, cites a record that does not exist, or quotes
words that are not in the transcript near the stated timestamp.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

from icekb.integrate.store import Data, link, write_page


def _words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']{3,}", text.lower()))


def _seconds(stamp: str) -> int:
    h, m, s = (int(x) for x in stamp.split(":"))
    return h * 3600 + m * 60 + s


def check_quote(quote: dict, transcript: str) -> str | None:
    """The quoted words must appear in the transcript within about three minutes of the timestamp."""
    target = _seconds(quote["at"])
    window = []
    for para in transcript.split("\n\n"):
        m = re.match(r"\[(\d+:\d{2}:\d{2})\]", para)
        if m and abs(_seconds(m.group(1)) - target) <= 200:
            window.append(para)
    if not window:
        return f"no transcript text near {quote['at']}"
    have, want = _words(" ".join(window)), _words(quote["text"])
    if want and len(want & have) / len(want) < 0.7:
        return f"quote at {quote['at']} does not match the transcript there"
    return None


def person_label(data: Data, who: str) -> str:
    return link(f"person/{who}", data.name(who)) if (data.root / "people" / f"{who}.md").exists() else who


def ref_label(ref: str) -> str:
    if ref.startswith("gh:"):
        repo, num = ref[3:].split("#")
        return f"[{repo.split('/')[1]}#{num}](https://github.com/{repo}/issues/{num})"
    if ref.startswith("doc:"):
        return f"[doc](https://docs.google.com/document/d/{ref[4:]})"
    if ref.startswith("list:"):
        return f"[thread](https://lists.apache.org/thread/{ref[5:]})"
    if ref.startswith("yt:"):
        return f"[video](https://www.youtube.com/watch?v={ref[3:]})"
    return f"`{ref}`"


def initiative_links(data: Data, slugs: list[str], source: str) -> list[dict]:
    return [{"rel": "discussed", "to": f"initiative/{s}", "confidence": "extracted", "source": source}
            for s in dict.fromkeys(slugs) if (data.root / "initiatives" / f"{s}.md").exists()]


def apply_meeting(data: Data, ex: dict, validator, today: str) -> list[str]:
    errors = [f"{'/'.join(map(str, e.path))}: {e.message[:140]}" for e in validator.iter_errors({k: v for k, v in ex.items() if k != "_input_hash"})]
    if errors:
        return errors
    _, group, date = ex["id"].split("/")
    missing = [s for s in ex["sources"] if s not in data.by_id]
    if missing:
        return [f"unknown source(s): {missing}"]
    notes = next((data.by_id[s] for s in ex["sources"] if s.startswith("meet:")), None)
    video = next((data.by_id[s] for s in ex["sources"] if s.startswith("yt:")), None)
    for topic in ex["topics"]:
        for quote in topic.get("quotes", []):
            problem = "quote given but no transcript source" if not video else check_quote(quote, video["body"])
            if problem:
                errors.append(f"topic {topic['title']!r}: {problem}")
    if errors:
        return errors
    name = next(g["name"] for g in data.cfg["groups"] if g["slug"] == group)
    basis = "notes and recording transcript" if notes and video else "recording transcript only" if video else "notes only"
    lines = [f"**Group:** {link('group/' + group, name)} · **Date:** {date} · **Based on:** {basis}", ""]
    if notes:
        lines.append(f"**Notes:** {notes['url']} (`{notes['id']}`)" + (" — the notes include AI-generated text" if notes.get("ai_generated") else ""))
    if video:
        lines.append(f"**Recording:** {video['url']} (`{video['id']}`, auto-generated captions without speaker names)")
    lines += ["", "> Summary written by an AI model from the sources above. Check the source before relying on a detail.", "",
              "## Summary", "", ex["summary"], ""]
    slugs = []
    for topic in ex["topics"]:
        slugs += topic.get("initiatives", [])
        lines += [f"## {topic['title']}", "", topic["summary"], ""]
        if topic.get("decisions"):
            lines += ["**Decisions:**"] + [f"- {d}" for d in topic["decisions"]] + [""]
        if topic.get("open_questions"):
            lines += ["**Open questions:**"] + [f"- {q}" for q in topic["open_questions"]] + [""]
        for quote in topic.get("quotes", []):
            at = _seconds(quote["at"])
            speaker = f" ({quote['speaker']}, speaker inferred)" if quote.get("speaker") else ""
            lines += [f"> “{quote['text']}”{speaker} [{quote['at']}]({video['url']}&t={at}s)", ""]
        if topic.get("refs"):
            lines += ["References: " + ", ".join(ref_label(r) for r in topic["refs"][:25]), ""]
    if ex.get("action_items"):
        lines += ["## Action items", ""] + [f"- {(person_label(data, a['who']) + ': ') if a.get('who') else ''}{a['what']}" for a in ex["action_items"]] + [""]
    if ex.get("participants"):
        named = [f"{person_label(data, p['who'])}{' (inferred from the transcript)' if p['basis'] == 'transcript' else ''}" for p in ex["participants"]]
        lines += ["## People named", "", ", ".join(named), ""]
    links = [{"rel": "of", "to": f"group/{group}", "confidence": "observed"}] + initiative_links(data, slugs, ex["sources"][0])
    for p in ex.get("participants", []):
        if (data.root / "people" / f"{p['who']}.md").exists():
            links.append({"rel": "named", "to": f"person/{p['who']}", "source": ex["sources"][0],
                          "confidence": "extracted" if p["basis"] == "notes" else "inferred"})
    refs = list(dict.fromkeys(r for t in ex["topics"] for r in t.get("refs", [])))
    meta = {"id": ex["id"], "type": "meeting", "title": f"{name}, {date}", "date": date, "group": group, "status": "summarized",
            "sources": ex["sources"], "refs": refs, "links": links}
    write_page(data.root, f"records/meetings/{group}/{date[:4]}/{date}.md", meta, meta["title"], "\n".join(lines), today)
    return []


def apply_thread(data: Data, ex: dict, validator, today: str) -> list[str]:
    errors = [f"{'/'.join(map(str, e.path))}: {e.message[:140]}" for e in validator.iter_errors({k: v for k, v in ex.items() if k != "_input_hash"})]
    if errors:
        return errors
    tid = ex["id"].split("/")[1]
    mails = data.threads.get(tid) or []
    known = {m["id"] for m in mails}
    cited = set(ex["sources"]) | {p["source"] for p in ex.get("positions", [])} | ({ex["outcome"]["source"]} if ex["outcome"].get("source") else set())
    bad = sorted(cited - known)
    if not mails or bad:
        return [f"cites message(s) that are not in this thread: {bad[:5]}" if mails else "unknown thread"]
    first, last = mails[0], mails[-1]
    subject = first["meta"]["subject"]
    starter = first["people"][0]
    lines = [f"**Thread:** [{subject}]({first['url']}) · **Started:** {first['date'][:10]} by "
             f"{person_label(data, starter) if not starter.startswith('name:') else starter[5:]} · **Messages:** {len(mails)} "
             f"(last {last['date'][:10]}) · **Outcome:** {ex['outcome']['status']}", "",
             "> Summary written by an AI model from the messages. Check the thread before relying on a detail.", "",
             "## Summary", "", ex["summary"], ""]
    if ex.get("why_it_matters"):
        lines += ["**Why it matters:** " + ex["why_it_matters"], ""]
    if ex["outcome"].get("note"):
        src = ex["outcome"].get("source")
        lines += ["## Outcome", "", ex["outcome"]["note"] + (f" ([message]({data.by_id[src]['url']}), `{src}`)" if src else ""), ""]
    if ex.get("positions"):
        lines += ["## Positions", ""]
        for p in ex["positions"]:
            who = p["who"]
            lines.append(f"- **{person_label(data, who)}:** {p['stance']} ([message]({data.by_id[p['source']]['url']}))")
        lines.append("")
    if ex.get("refs"):
        lines += ["References: " + ", ".join(ref_label(r) for r in ex["refs"][:25]), ""]
    links = initiative_links(data, ex.get("initiatives", []), first["id"])
    if not starter.startswith("name:") and (data.root / "people" / f"{starter}.md").exists():
        links.append({"rel": "started_by", "to": f"person/{starter}", "confidence": "observed"})
    slug = re.sub(r"[^a-z0-9]+", "-", subject.lower()).strip("-")[:70] or tid
    meta = {"id": ex["id"], "type": "thread", "title": ex["title"], "date": first["date"][:10], "url": first["url"],
            "kind": first["meta"]["kind"], "status": ex["outcome"]["status"], "messages": len(mails),
            "sources": [first["id"]], "refs": ex.get("refs", []), "links": links}
    write_page(data.root, f"records/threads/{first['date'][:4]}/{first['date'][5:7]}/{slug}-{tid[2:8]}.md", meta, ex["title"], "\n".join(lines), today)
    return []


def apply_all(root: Path) -> dict:
    data = Data(root)
    today = data.today.isoformat()
    validators = {k: Draft202012Validator(json.loads((root / "schema" / f"extract-{k}.json").read_text())) for k in ("meeting", "thread")}
    result = {"meetings": 0, "threads": 0, "rejected": {}}
    for path in sorted((root / "data" / "extract").rglob("*.json")):
        try:
            ex = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            result["rejected"][str(path.relative_to(root))] = [f"not valid JSON: {exc}"]
            continue
        kind = "meeting" if "meetings" in path.parts else "thread"
        errors = (apply_meeting if kind == "meeting" else apply_thread)(data, ex, validators[kind], today)
        if errors:
            result["rejected"][str(path.relative_to(root))] = errors[:6]
        else:
            result[kind + "s"] += 1
    return result
