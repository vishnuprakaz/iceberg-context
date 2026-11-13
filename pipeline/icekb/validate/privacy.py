"""Privacy lint: no email addresses in committed text."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
# Public list and role addresses, and no-reply addresses, are not personal data.
ALLOWED = re.compile(
    r"^(?:(?:dev|issues|commits|ci-jobs|private|security)@iceberg\.apache\.org"
    r"|[\w.+-]*@users\.noreply\.github\.com|noreply@[\w.-]+|git@github\.com"
    r"|[\w.+-]+@(?:example\.(?:com|org)|group\.calendar\.google\.com|group\.v\.calendar\.google\.com))$",
    re.I,
)
SKIP_SUFFIX = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".sqlite", ".lock"}
SKIP_FILES = {"LICENSE", "uv.lock"}


def tracked_files(root: Path) -> list[Path]:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-co", "--exclude-standard"],
            capture_output=True, text=True, check=True,
        ).stdout
        return [root / line for line in out.splitlines() if line]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]


def find_emails(text: str) -> list[str]:
    return [m for m in EMAIL.findall(text) if not ALLOWED.match(m)]


def check(root: Path) -> list[str]:
    problems = []
    for path in tracked_files(root):
        if path.suffix.lower() in SKIP_SUFFIX or path.name in SKIP_FILES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        hits = find_emails(text)
        if hits:
            shown = ", ".join(h[:3] + "…" for h in sorted(set(hits))[:3])
            problems.append(f"{path.relative_to(root)}: {len(hits)} email address(es) ({shown})")
    return problems
