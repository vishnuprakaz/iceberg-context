"""Build index/nodes.jsonl and index/edges.jsonl from page frontmatter.

The `kb` script in the skill reads these files, so it needs no YAML parser.
"""
from __future__ import annotations

import json
from pathlib import Path

from icekb import frontmatter
from icekb.paths import page_files


def build(root: Path) -> tuple[list[dict], list[dict]]:
    nodes, edges = [], []
    for path in page_files(root):
        page = frontmatter.load(path)
        meta = page.meta
        if not meta.get("id"):
            continue
        node = {k: v for k, v in meta.items() if k != "links"}
        node["path"] = path.relative_to(root).as_posix()
        nodes.append(node)
        for link in meta.get("links") or []:
            edges.append({"src": meta["id"], **link})
    nodes.sort(key=lambda n: n["id"])
    edges.sort(key=lambda e: (e["src"], e["rel"], e["to"]))
    return nodes, edges


def _render(rows: list[dict]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True, default=str) + "\n" for r in rows)


def write(root: Path, check_only: bool = False) -> bool:
    """Write the index. With check_only, return False if the files on disk are stale."""
    nodes, edges = build(root)
    out = root / "index"
    wanted = {"nodes.jsonl": _render(nodes), "edges.jsonl": _render(edges)}
    fresh = all((out / n).exists() and (out / n).read_text(encoding="utf-8") == t for n, t in wanted.items())
    if check_only or fresh:
        return fresh
    out.mkdir(exist_ok=True)
    for name, text in wanted.items():
        (out / name).write_text(text, encoding="utf-8")
    return True
