"""Shared helpers: HTTP, JSONL storage, text cleaning, reference extraction."""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from collections.abc import Iterable, Iterator
from pathlib import Path

USER_AGENT = "iceberg-context-sync/0.1"
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
_GH_URL = re.compile(r"github\.com/(apache/[\w.-]+)/(?:pull|issues)/(\d+)")
_GH_SHORT = re.compile(r"\b(apache/[\w.-]+)#(\d+)")
_BARE = re.compile(r"(?<![\w/&#])#(\d{4,5})\b")
_GDOC = re.compile(r"docs\.google\.com/document/d/([\w-]{20,})")
_YT = re.compile(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]{11})")
_LIST = re.compile(r"lists\.apache\.org/thread/([a-z0-9]{20,})")


def http_get(url: str, *, headers: dict | None = None, timeout: int = 120, retries: int = 4) -> bytes:
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (400, 401, 404, 410, 422):
                raise
            last = exc
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed: {last}")


def sha(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:20]


def strip_emails(text: str) -> str:
    return EMAIL.sub("[email removed]", text)


def clean_text(text: str, limit: int | None = None) -> str:
    text = strip_emails(text.replace("\r\n", "\n").replace("\r", "\n").replace("\x00", ""))
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if limit and len(text) > limit:
        text = text[:limit].rstrip() + " […]"
    return text


def extract_refs(text: str, default_repo: str | None = "apache/iceberg") -> list[str]:
    """Find references to pull requests, issues, documents, videos and list threads in free text."""
    refs: list[str] = []
    for repo, num in _GH_URL.findall(text) + _GH_SHORT.findall(text):
        refs.append(f"gh:{repo}#{num}")
    if default_repo:
        refs += [f"gh:{default_repo}#{n}" for n in _BARE.findall(text)]
    refs += [f"doc:{d}" for d in _GDOC.findall(text)]
    refs += [f"yt:{v}" for v in _YT.findall(text)]
    refs += [f"list:{t}" for t in _LIST.findall(text)]
    return list(dict.fromkeys(refs))


def read_jsonl(path: Path) -> Iterator[dict]:
    if not path.exists():
        return
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                yield json.loads(line)


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def upsert(root: Path, source_dir: str, records: Iterable[dict], *, by: str = "month") -> dict:
    """Merge records into data/raw/<source_dir>/YYYY/MM.jsonl (or YYYY.jsonl), keyed by id.

    Returns counts of new and changed records. Files stay sorted by (date, id) so diffs are stable.
    """
    buckets: dict[Path, list[dict]] = {}
    for rec in records:
        date = rec["date"]
        rel = f"{date[:4]}/{date[5:7]}.jsonl" if by == "month" else f"{date[:4]}.jsonl"
        buckets.setdefault(root / "data" / "raw" / source_dir / rel, []).append(rec)
    new = changed = 0
    for path, recs in buckets.items():
        existing = {r["id"]: r for r in read_jsonl(path)}
        for rec in recs:
            old = existing.get(rec["id"])
            if old is None:
                new += 1
            elif old.get("hash") != rec.get("hash"):
                changed += 1
            existing[rec["id"]] = rec
        write_jsonl(path, sorted(existing.values(), key=lambda r: (r["date"], r["id"])))
    return {"new": new, "changed": changed}


def iter_raw(root: Path, source_dir: str) -> Iterator[dict]:
    base = root / "data" / "raw" / source_dir if source_dir else root / "data" / "raw"
    if base.is_dir():
        for path in sorted(base.rglob("*.jsonl")):
            yield from read_jsonl(path)


def http_json(url: str, *, method: str = "GET", payload: dict | None = None, headers: dict | None = None,
              timeout: int = 60, retries: int = 3) -> tuple[object, dict]:
    """JSON request returning (body, response headers). Retries on network errors and 5xx/secondary limits."""
    data = json.dumps(payload).encode() if payload is not None else None
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, method=method, headers={
            "User-Agent": USER_AGENT, "Accept": "application/vnd.github+json", **(headers or {})})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read() or b"null"), dict(resp.headers)
        except urllib.error.HTTPError as exc:
            body = exc.read()[:300].decode("utf-8", "replace")
            if exc.code in (401, 404, 422) or (exc.code == 403 and "rate limit" in body.lower()):
                raise RuntimeError(f"HTTP {exc.code} for {url.split('?')[0]}: {body}") from exc
            last = RuntimeError(f"HTTP {exc.code}: {body}")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"{method} {url.split('?')[0]} failed: {last}")
