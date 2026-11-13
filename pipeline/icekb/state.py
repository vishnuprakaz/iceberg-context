"""Per-source sync state in data/state/<source>.json."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def path(root: Path, source: str) -> Path:
    return root / "data" / "state" / f"{source}.json"


def load(root: Path, source: str) -> dict:
    p = path(root, source)
    if p.exists():
        return json.loads(p.read_text())
    return {"source": source, "status": "never"}


def save(root: Path, source: str, *, ok: bool, counts: dict | None = None, cursor=None, error: str = "") -> dict:
    st = load(root, source)
    st["last_run"] = now()
    st["status"] = "ok" if ok else "failed"
    if ok:
        st["last_success"] = st["last_run"]
        st.pop("error", None)
        if cursor is not None:
            st["cursor"] = cursor
    else:
        st["error"] = error[:500]
    if counts:
        st["counts"] = {**st.get("counts", {}), **counts}
    p = path(root, source)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(st, indent=2, sort_keys=True) + "\n")
    return st
