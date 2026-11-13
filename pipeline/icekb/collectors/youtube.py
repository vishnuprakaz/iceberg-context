"""Collect transcripts of community recordings from YouTube's auto-generated captions."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import yaml

from icekb import state
from icekb.dates import find_date
from icekb.ingest.calendar import match_group
from icekb.util import clean_text, extract_refs, sha, upsert


def _ytdlp() -> list[str]:
    exe = shutil.which("yt-dlp")
    return [exe] if exe else ["uvx", "--from", "yt-dlp[default]", "yt-dlp"]


def list_videos(channel: str) -> list[dict]:
    res = subprocess.run(_ytdlp() + ["--flat-playlist", "-J", f"https://www.youtube.com/{channel}/videos"],
                         capture_output=True, text=True, timeout=600)
    if res.returncode != 0:
        raise RuntimeError(f"yt-dlp listing failed: {res.stderr.strip()[-300:]}")
    return [{"id": e["id"], "title": e.get("title") or ""} for e in json.loads(res.stdout).get("entries", []) if e.get("id")]


def paragraphs(json3: dict) -> list[tuple[int, str]]:
    """Group caption events into paragraphs, breaking at speaker changes ('>>') and about every 90 seconds."""
    paras, cur, start = [], [], 0
    for ev in json3.get("events", []):
        text = "".join(s.get("utf8", "") for s in ev.get("segs") or []).replace("\n", " ")
        if not text.strip():
            continue
        ms = ev.get("tStartMs", 0)
        for i, piece in enumerate(re.split(r"\s*>>\s*", text)):
            if i > 0 and cur:
                paras.append((start, " ".join(cur)))
                cur = []
            if not cur:
                start = ms
            if piece.strip():
                cur.append(piece.strip())
        if cur and ms - start > 90000 and cur[-1].endswith((".", "?", "!")):
            paras.append((start, " ".join(cur)))
            cur = []
    if cur:
        paras.append((start, " ".join(cur)))
    return [(ms, re.sub(r"\s+", " ", t)) for ms, t in paras]


def stamp(ms: int) -> str:
    s = ms // 1000
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}"


def build_record(info: dict, json3: dict, groups: list[dict]) -> dict:
    vid, title = info["id"], " ".join((info.get("title") or "").split())
    upload = info.get("upload_date") or "19700101"
    upload_iso = f"{upload[:4]}-{upload[4:6]}-{upload[6:]}"
    found = find_date(title)
    held = found[0].isoformat() if found and found[0].isoformat() <= upload_iso else upload_iso
    group = match_group(title, groups)
    paras = paragraphs(json3)
    body = "\n\n".join(f"[{stamp(ms)}] {text}" for ms, text in paras)
    desc = clean_text(info.get("description") or "", limit=1500)
    meta = {"group": group, "video": vid, "kind": "sync" if group else "talk", "upload_date": upload_iso,
            "duration_s": info.get("duration"), "words": len(body.split()), "caption_track": "en-orig (auto-generated)",
            "description": desc}
    return {
        "id": f"yt:{vid}",
        "source": "youtube",
        "type": "transcript",
        "date": f"{held}T00:00:00Z",
        "url": f"https://www.youtube.com/watch?v={vid}",
        "title": title,
        "body": clean_text(body),
        "refs": extract_refs(desc, None),
        "hash": sha(body),
        "ai_generated": True,  # machine captions: no speaker names, some misheard terms
        "meta": {k: v for k, v in meta.items() if v not in (None, "")},
    }


def fetch(vid: str, track: str, tmp: Path) -> tuple[dict, dict]:
    """Fetch metadata and captions for one video. YouTube sometimes answers cloud addresses with a bot check;
    that is reported as a failure and retried on a later run, not worked around."""
    out = tmp / vid
    res = subprocess.run(_ytdlp() + ["--skip-download", "--write-auto-subs", "--sub-langs", track, "--sub-format", "json3",
                                     "--write-info-json", "--no-warnings", "-o", str(out), f"https://www.youtube.com/watch?v={vid}"],
                         capture_output=True, text=True, timeout=300)
    info_path, subs_path = Path(f"{out}.info.json"), Path(f"{out}.{track}.json3")
    if not info_path.exists() or not subs_path.exists():
        raise RuntimeError((res.stderr.strip() or "no captions available")[-200:])
    return json.loads(info_path.read_text()), json.loads(subs_path.read_text())


def collect(root: Path, *, max_videos: str | int = 25, pause: str | float = 3, **_ignored) -> dict:
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    yt = cfg["youtube"]
    st = state.load(root, "youtube")
    cursor = dict(st.get("cursor") or {})
    done, failed = dict(cursor.get("done") or {}), dict(cursor.get("failed") or {})
    listing = list_videos(yt["channel"])
    pending = [v for v in listing if v["id"] not in done]
    # New videos first; ones that failed before go to the back of the queue but are always retried.
    todo = sorted(pending, key=lambda v: failed.get(v["id"], {}).get("tries", 0))[: int(max_videos)]
    totals = {"new": 0, "changed": 0}
    fetched = failed_now = 0

    def save(batch: list[dict]) -> None:
        counts = upsert(root, "youtube", batch)
        totals["new"] += counts["new"]
        totals["changed"] += counts["changed"]
        remaining = sum(1 for v in listing if v["id"] not in done)
        state.save(root, "youtube", ok=True, cursor={"done": done, "failed": failed},
                   counts={"videos_listed": len(listing), "transcripts": len(done), "remaining": remaining, "failing": len(failed)})

    batch: list[dict] = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, video in enumerate(todo):
            if i:
                time.sleep(float(pause))
            try:
                info, subs = fetch(video["id"], yt["caption_track"], Path(tmp))
                rec = build_record(info, subs, cfg["groups"])
                batch.append(rec)
                done[video["id"]] = rec["date"][:10]
                failed.pop(video["id"], None)
                fetched += 1
            except Exception as exc:  # leave it for the next run; never mark a failed video as done
                entry = failed.get(video["id"], {"tries": 0})
                failed[video["id"]] = {"tries": entry["tries"] + 1, "error": str(exc)[:160], "title": video["title"][:80]}
                failed_now += 1
            if len(batch) >= 10:  # save progress as we go, so an interrupted run keeps what it fetched
                save(batch)
                batch = []
    save(batch)
    return {"fetched": fetched, "failed_now": failed_now, "remaining": sum(1 for v in listing if v["id"] not in done), **totals}


def ingest_files(root: Path, info_file: Path, captions_file: Path) -> dict:
    """Store a transcript from files fetched elsewhere (for example on a machine YouTube does not challenge)."""
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    rec = build_record(json.loads(Path(info_file).read_text()), json.loads(Path(captions_file).read_text()), cfg["groups"])
    counts = upsert(root, "youtube", [rec])
    st = state.load(root, "youtube")
    cursor = dict(st.get("cursor") or {})
    done, failed = dict(cursor.get("done") or {}), dict(cursor.get("failed") or {})
    done[rec["meta"]["video"]] = rec["date"][:10]
    failed.pop(rec["meta"]["video"], None)
    state.save(root, "youtube", ok=True, cursor={"done": done, "failed": failed}, counts={"transcripts": len(done), "failing": len(failed)})
    return {"id": rec["id"], "group": rec["meta"].get("group"), "date": rec["date"][:10], **counts}
