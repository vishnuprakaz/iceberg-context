"""Repository layout: where things live."""
from __future__ import annotations

import os
from pathlib import Path

PAGE_DIRS = ("people", "groups", "initiatives", "modules", "repos", "releases", "records")
# Free text that is indexed for search but has no frontmatter contract.
DOC_DIRS = ("docs", "research", "notes", "briefings", "maps")
DOC_FILES = ("state-of-iceberg.md", "opportunities.md", "README.md")


def repo_root() -> Path:
    env = os.environ.get("ICEBERG_CONTEXT_ROOT")
    if env:
        return Path(env).resolve()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "schema" / "page.json").exists():
            return parent
    raise RuntimeError("cannot locate the iceberg-context repository root")


def page_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for d in PAGE_DIRS:
        base = root / d
        if base.is_dir():
            out += [p for p in sorted(base.rglob("*.md")) if p.name != "README.md"]
    return out
