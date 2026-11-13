"""Validators run in CI and before every sync commit."""
from __future__ import annotations

from pathlib import Path

from icekb.validate import pages, privacy


def run_all(root: Path) -> dict[str, list[str]]:
    return {"pages": pages.check(root), "privacy": privacy.check(root)}
