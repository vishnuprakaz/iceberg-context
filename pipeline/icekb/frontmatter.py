"""Read and write Markdown pages with YAML frontmatter and generated blocks."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

GEN_START = "<!-- kb:generated:start -->"
GEN_END = "<!-- kb:generated:end -->"
_FM = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
_GEN = re.compile(re.escape(GEN_START) + r".*?" + re.escape(GEN_END), re.S)


@dataclass
class Page:
    path: Path
    meta: dict
    body: str


def parse(text: str) -> tuple[dict, str]:
    m = _FM.match(text)
    if not m:
        return {}, text
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("frontmatter must be a mapping")
    return meta, m.group(2)


def load(path: Path) -> Page:
    meta, body = parse(path.read_text(encoding="utf-8"))
    return Page(path, meta, body)


def dump(meta: dict, body: str) -> str:
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000).rstrip()
    return f"---\n{fm}\n---\n{body if body.startswith(chr(10)) else chr(10) + body}"


def set_generated(body: str, generated: str) -> str:
    """Replace the generated block, or add one above the human notes. Text outside the markers is kept."""
    block = f"{GEN_START}\n{generated.strip()}\n{GEN_END}"
    if _GEN.search(body):
        return _GEN.sub(lambda _m: block, body, count=1)
    if "## Notes" in body:
        head, _, tail = body.partition("## Notes")
        return f"{head.rstrip()}\n\n{block}\n\n## Notes{tail}"
    return f"{body.rstrip()}\n\n{block}\n\n## Notes\n"


def markers_ok(body: str) -> bool:
    s, e = body.count(GEN_START), body.count(GEN_END)
    if s != e or s > 1:
        return False
    return s == 0 or body.index(GEN_START) < body.index(GEN_END)
