"""Checks on data/aliases.yaml that protect vote counts and attributions.

- A display name listed under two logins is an error: the resolver ignores such names, so one of the entries is wrong.
- For each ASF committer or PMC member, the alias entry must list the name the ASF roster gives for them, so that a
  dev-list message signed with that name resolves to the right login.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import yaml

from icekb.identity import _key
from icekb.util import iter_raw


def check(root: Path) -> list[str]:
    people = (yaml.safe_load((root / "data" / "aliases.yaml").read_text(encoding="utf-8")) or {}).get("people") or {}
    problems = []
    owners: dict[str, set[str]] = defaultdict(set)
    for login, info in people.items():
        for name in info.get("names") or []:
            owners[_key(name)].add(login)
    for name, logins in sorted(owners.items()):
        if len(logins) > 1:
            problems.append(f"aliases.yaml: the name {name!r} is listed under {', '.join(sorted(logins))}")
    for r in iter_raw(root, "asf"):
        meta = r.get("meta") or {}
        login, name = (r.get("people") or [""])[0], meta.get("name")
        if not name or login.startswith("asf:"):
            continue
        names = {_key(n) for n in (people.get(login) or {}).get("names") or []}
        if _key(name) not in names:
            problems.append(f"aliases.yaml: {login} (ASF id {meta.get('asf_id')}) does not list the ASF roster name {name!r}")
    return problems
