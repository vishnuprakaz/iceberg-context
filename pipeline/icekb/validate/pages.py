"""Validate knowledge-base pages: schema, unique ids, link targets, generated-block markers."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from icekb import frontmatter
from icekb.paths import page_files

# Link targets outside the page graph: raw records and external items.
EXTERNAL_PREFIXES = ("gh:", "devlist:", "commit:", "meet:", "yt:", "doc:", "spec:", "asf:", "cal:", "http://", "https://")


def check(root: Path) -> list[str]:
    validator = Draft202012Validator(json.loads((root / "schema" / "page.json").read_text()))
    problems: list[str] = []
    pages = []
    for path in page_files(root):
        rel = path.relative_to(root)
        try:
            page = frontmatter.load(path)
        except Exception as exc:  # malformed YAML
            problems.append(f"{rel}: cannot read frontmatter: {exc}")
            continue
        if not page.meta:
            problems.append(f"{rel}: missing frontmatter")
            continue
        for err in sorted(validator.iter_errors(page.meta), key=lambda e: list(e.path)):
            where = "/".join(str(p) for p in err.path) or "(top level)"
            problems.append(f"{rel}: {where}: {err.message[:160]}")
        if not frontmatter.markers_ok(page.body):
            problems.append(f"{rel}: generated-block markers are unbalanced or duplicated")
        pages.append((rel, page))

    ids: dict[str, Path] = {}
    for rel, page in pages:
        pid = page.meta.get("id")
        if pid in ids:
            problems.append(f"{rel}: duplicate id {pid!r} (also in {ids[pid]})")
        elif pid:
            ids[pid] = rel
    for rel, page in pages:
        for link in page.meta.get("links") or []:
            to = link.get("to", "") if isinstance(link, dict) else ""
            if to and not to.startswith(EXTERNAL_PREFIXES) and to not in ids:
                problems.append(f"{rel}: link target {to!r} does not exist")
    return problems
