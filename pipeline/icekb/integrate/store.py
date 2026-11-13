"""Load collected records into memory and write generated pages without disturbing human text."""
from __future__ import annotations

import datetime as dt
from collections import defaultdict
from pathlib import Path

import yaml

from icekb import frontmatter
from icekb.util import iter_raw


class Data:
    """All raw records, grouped by type, plus a few indexes used by the page generators."""

    def __init__(self, root: Path):
        self.root = root
        self.cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
        self.aliases = (yaml.safe_load((root / "people" / "aliases.yaml").read_text()) or {}).get("people") or {}
        self.by_type: dict[str, list[dict]] = defaultdict(list)
        self.by_id: dict[str, dict] = {}
        for rec in iter_raw(root, ""):
            self.by_type[rec["type"]].append(rec)
            self.by_id[rec["id"]] = rec
        for recs in self.by_type.values():
            recs.sort(key=lambda r: r["date"])
        self.today = dt.datetime.now(dt.timezone.utc).date()
        self.threads: dict[str, list[dict]] = defaultdict(list)
        for mail in self.by_type["email"]:
            self.threads[mail["meta"]["thread"]].append(mail)

    def since(self, days: int) -> str:
        return (self.today - dt.timedelta(days=days)).isoformat()

    def name(self, login: str) -> str:
        names = (self.aliases.get(login) or {}).get("names") or []
        return names[0] if names else login


def link(target: str, label: str | None = None) -> str:
    """An Obsidian-style wiki link that also reads fine as plain text."""
    return f"[[{target}|{label}]]" if label else f"[[{target}]]"


def write_page(root: Path, rel_path: str, meta: dict, heading: str, generated: str, today: str) -> bool:
    """Create or update a page. Only the frontmatter and the generated block change; `updated` moves only on real changes."""
    path = root / rel_path
    if path.exists():
        page = frontmatter.load(path)
        body = frontmatter.set_generated(page.body, generated)
        old = {k: v for k, v in page.meta.items() if k != "updated"}
        if old == meta and body == page.body:
            return False
        meta = {**meta, "updated": today}
    else:
        body = frontmatter.set_generated(f"# {heading}\n", generated)
        meta = {**meta, "updated": today}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter.dump(meta, body), encoding="utf-8")
    return True
