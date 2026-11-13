"""Collect the public ASF roster for the Iceberg project: PMC members and committers."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from icekb import state
from icekb.identity import Identity
from icekb.util import http_get, sha, write_jsonl


def collect(root: Path, **_ignored) -> dict:
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())["asf"]
    project = cfg["project"]
    committee = json.loads(http_get(cfg["committee_info"]))["committees"][project]
    ldap = json.loads(http_get(cfg["ldap_projects"]))["projects"][project]
    names = {k: v.get("name") for k, v in json.loads(http_get(cfg["ldap_people"]))["people"].items()} if cfg.get(
        "ldap_people") else {}
    identity = Identity(root)
    chair = next(iter((committee.get("chair") or {}).keys()), None)
    pmc = committee.get("roster") or {}
    members = set(ldap.get("members") or []) | set(ldap.get("owners") or []) | set(pmc)
    rows = []
    for asf_id in sorted(members):
        info = pmc.get(asf_id) or {}
        name = info.get("name") or names.get(asf_id)
        role = "pmc" if asf_id in pmc else "committer"
        rows.append({
            "id": f"asf:{project}:{asf_id}",
            "source": "asf",
            "type": "roster",
            "date": f"{info.get('date') or '1970-01-01'}T00:00:00Z",
            "url": f"https://projects.apache.org/committee.html?{project}",
            "people": [identity.by_asf.get(asf_id.lower()) or f"asf:{asf_id}"],
            "title": f"{name or asf_id}: {'PMC chair' if asf_id == chair else role.upper() if role == 'pmc' else role}",
            "hash": sha(f"{asf_id}{role}{info.get('date')}{asf_id == chair}{name}"),
            "meta": {"asf_id": asf_id, "role": role, "chair": asf_id == chair, "name": name,
                     "pmc_since": info.get("date")},
        })
    write_jsonl(root / "data" / "raw" / "asf" / "roster.jsonl", rows)
    counts = {"pmc": len(pmc), "committers_total": len(members)}
    state.save(root, "asf", ok=True, counts=counts)
    return counts
