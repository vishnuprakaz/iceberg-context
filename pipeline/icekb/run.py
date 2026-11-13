"""Run collectors. A failing collector is recorded in its state file and does not stop the others."""
from __future__ import annotations

import importlib
import traceback
from pathlib import Path

from icekb import state

DAILY = ("devlist", "git", "asf", "github")


def collect(root: Path, source: str, *, backfill: bool = False, option: dict | None = None) -> int:
    sources = DAILY if source == "daily" else (source,)
    failures = 0
    for name in sources:
        module = importlib.import_module(f"icekb.collectors.{name}")
        kwargs = dict(option or {})
        if backfill:
            kwargs["backfill"] = True
        try:
            counts = module.collect(root, **kwargs)
            print(f"{name}: ok {counts}")
        except Exception as exc:  # isolate collectors from each other
            failures += 1
            traceback.print_exc()
            state.save(root, name, ok=False, error=f"{type(exc).__name__}: {exc}")
            print(f"{name}: FAILED {exc}")
    return 1 if failures == len(sources) else 0
