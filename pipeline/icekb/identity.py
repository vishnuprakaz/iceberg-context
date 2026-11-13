"""Resolve the many names a person appears under to one GitHub login. Never guesses."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import yaml


def _key(name: str) -> str:
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def normalize_display(name: str) -> str:
    """Clean a mailing-list display name: drop 'via dev', quotes, '(company)', and flip 'Last, First'."""
    name = re.sub(r"\s+via\s+\S+$", "", name.strip().strip("\"'"), flags=re.I)
    name = re.sub(r"\s*[(\[].*?[)\]]\s*$", "", name).strip().strip("\"'")
    if "," in name and name.count(",") == 1:
        last, first = (p.strip() for p in name.split(","))
        if first and last:
            name = f"{first} {last}"
    return " ".join(name.split())


class Identity:
    def __init__(self, root: Path):
        self.root = root
        data = yaml.safe_load((root / "data" / "aliases.yaml").read_text(encoding="utf-8")) or {}
        self.people: dict[str, dict] = data.get("people") or {}
        self.by_name: dict[str, str] = {}
        self.by_login = {login.lower(): login for login in self.people}
        self.by_asf: dict[str, str] = {}
        ambiguous: set[str] = set()
        for login, info in self.people.items():
            if info.get("asf_id"):
                self.by_asf[info["asf_id"].lower()] = login
            for name in info.get("names") or []:
                k = _key(name)
                if k in self.by_name and self.by_name[k] != login:
                    ambiguous.add(k)
                self.by_name[k] = login
        for k in ambiguous:
            del self.by_name[k]
        self.unresolved: dict[str, int] = {}

    def resolve(self, name: str) -> str | None:
        clean = normalize_display(name)
        if "@" in clean:  # an address used as a display name: keep only the part before the @
            clean = clean.split("@")[0]
        if not clean or clean.isdigit():
            return None
        hit = self.by_login.get(clean.lower()) or self.by_name.get(_key(clean)) or self._garbled(clean)
        if hit is None:
            self.unresolved[clean] = self.unresolved.get(clean, 0) + 1
        return hit

    def _garbled(self, name: str) -> str | None:
        """A name whose accented letter was lost in transit ('Tudenh\ufffd\ufffdfner'): match it only when exactly one
        known name fits with one or two letters in each damaged spot."""
        if "\ufffd" not in name:
            return None
        parts = [_key(p) for p in re.split("\ufffd+", name)]
        pattern = re.compile(".{1,2}".join(re.escape(p) for p in parts) + "$")
        hits = {login for k, login in self.by_name.items() if pattern.match(k)}
        return hits.pop() if len(hits) == 1 else None

    def person(self, name: str) -> str:
        """A stable people[] entry: the login when known, otherwise 'name:<Display Name>'."""
        login = self.resolve(name)
        clean = normalize_display(name).split("@")[0]
        return login or f"name:{clean}"

    def save_unresolved(self, source: str) -> None:
        path = self.root / "data" / "state" / "unresolved-people.json"
        data = json.loads(path.read_text()) if path.exists() else {}
        data[source] = dict(sorted(self.unresolved.items(), key=lambda kv: (-kv[1], kv[0]))[:300])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
