"""Collect commit history (the code map) and specification text from upstream git repositories."""
from __future__ import annotations

import datetime as dt
import re
import subprocess
from pathlib import Path

import yaml

from icekb import state
from icekb.identity import Identity
from icekb.util import clean_text, extract_refs, sha, upsert, write_jsonl

_PR = re.compile(r"\(#(\d+)\)\s*$")
MAX_FILES = 150
# Text that defines the rules the code implements, split into sections and indexed.
SPEC_FILES = {
    "apache/iceberg": ["format/spec.md", "format/view-spec.md", "format/puffin-spec.md", "format/udf-spec.md",
                       "format/expressions-spec.md", "format/gcm-stream-spec.md", "open-api/rest-catalog-open-api.yaml",
                       "site/docs/contribute.md", "site/docs/how-to-release.md", "AGENTS.md"],
    "apache/iceberg-python": ["mkdocs/docs/contributing.md", "mkdocs/docs/how-to-release.md", "AGENTS.md"],
}


def git(repo_dir: Path, *args: str, check: bool = True) -> str:
    res = subprocess.run(["git", "-C", str(repo_dir), *args], capture_output=True, text=True, errors="replace")
    if check and res.returncode != 0:
        raise RuntimeError(f"git {' '.join(args[:3])} failed: {res.stderr.strip()[:300]}")
    return res.stdout


def ensure_clone(repos_dir: Path, name: str, branch: str) -> Path:
    path = repos_dir / name.split("/")[1]
    if (path / ".git").exists() or (path / "HEAD").exists():
        git(path, "fetch", "--quiet", "--filter=blob:none", "origin", branch)
    else:
        repos_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--quiet", "--filter=blob:none", "--no-checkout", "--single-branch", "--branch", branch,
                        f"https://github.com/{name}", str(path)], check=True)
    return path


def parse_log(text: str, repo: str, identity: Identity) -> list[dict]:
    records = []
    for chunk in text.split("\x1e")[1:]:
        header, _, rest = chunk.partition("\n")
        commit, date, author, subject = header.split("\x1f", 3)
        files = [f for f in rest.split("\n") if f.strip()]
        pr = _PR.search(subject)
        refs = [f"gh:{repo}#{pr.group(1)}"] if pr else []
        refs += [r for r in extract_refs(subject, repo) if r not in refs]
        utc = dt.datetime.fromisoformat(date).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        records.append({
            "id": f"commit:{repo}@{commit[:12]}",
            "source": "git",
            "type": "commit",
            "date": utc,
            "url": f"https://github.com/{repo}/commit/{commit}",
            "people": [identity.person(author)],
            "title": subject,
            "refs": refs,
            "hash": sha(commit),
            "meta": {"repo": repo, "pr": int(pr.group(1)) if pr else None, "files": files[:MAX_FILES], "n_files": len(files)},
        })
    return records


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:80]


def split_markdown(text: str) -> list[tuple[str, str]]:
    """Split on headings up to level 3; return (heading path, section text)."""
    sections, trail, buf, title = [], {}, [], "(preamble)"
    in_code = False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
        m = None if in_code else re.match(r"^(#{1,3})\s+(.*\S)", line)
        if m:
            if "".join(buf).strip():
                sections.append((title, "\n".join(buf)))
            level = len(m.group(1))
            trail = {k: v for k, v in trail.items() if k < level}
            trail[level] = re.sub(r"[`*]", "", m.group(2))
            title, buf = " > ".join(trail[k] for k in sorted(trail)), []
        else:
            buf.append(line)
    if "".join(buf).strip():
        sections.append((title, "\n".join(buf)))
    return sections


def split_openapi(text: str) -> list[tuple[str, str]]:
    """Split the REST catalog OpenAPI file into one section per path and one per schema."""
    sections, title, buf, area = [], "(header)", [], ""
    for line in text.split("\n"):
        top = re.match(r"^(\w[\w-]*):", line)
        if top:
            area = top.group(1)
        key = re.match(r"^  (/\S*):", line) if area == "paths" else None
        if key is None and area == "components":
            sch = re.match(r"^    ([A-Z]\w+):", line)
            key = sch
        if key:
            if "".join(buf).strip():
                sections.append((title, "\n".join(buf)))
            title, buf = key.group(1), [line]
        else:
            buf.append(line)
    if "".join(buf).strip():
        sections.append((title, "\n".join(buf)))
    return sections


def collect_spec(repo_dir: Path, repo: str, branch: str) -> list[dict]:
    records = []
    for path in SPEC_FILES.get(repo, []):
        text = git(repo_dir, "show", f"origin/{branch}:{path}", check=False)
        if not text:
            continue
        date = git(repo_dir, "log", "-1", "--format=%cI", f"origin/{branch}", "--", path).strip()[:10] or "1970-01-01"
        parts = split_openapi(text) if path.endswith(".yaml") else split_markdown(text)
        seen: dict[str, int] = {}
        for title, body in parts:
            slug = _slug(title.split(" > ")[-1]) or "section"
            seen[slug] = seen.get(slug, 0) + 1
            anchor = slug if seen[slug] == 1 else f"{slug}-{seen[slug] - 1}"
            body = clean_text(body, limit=12000)
            if len(body) < 40:
                continue
            records.append({
                "id": f"spec:{repo}:{path}#{anchor}",
                "source": "spec",
                "type": "spec-section",
                "date": f"{date}T00:00:00Z",
                "url": f"https://github.com/{repo}/blob/{branch}/{path}" + ("" if path.endswith(".yaml") else f"#{anchor}"),
                "title": f"{path}: {title}",
                "body": body,
                "refs": extract_refs(body, None),
                "hash": sha(body),
                "meta": {"repo": repo, "file": path},
            })
    return records


def collect(root: Path, *, backfill: bool = False, repos_dir: str | None = None) -> dict:
    cfg = yaml.safe_load((root / "data" / "sources.yaml").read_text())
    work = Path(repos_dir) if repos_dir else root / ".work" / "repos"
    identity = Identity(root)
    st = state.load(root, "git")
    cursor = dict(st.get("cursor") or {})
    totals = {"new": 0, "changed": 0, "spec_sections": 0}
    for repo in cfg["repos"]:
        if repo.get("depth") != "full":
            continue
        name, branch = repo["name"], repo.get("default_branch", "main")
        repo_dir = ensure_clone(work, name, branch)
        head = git(repo_dir, "rev-parse", f"origin/{branch}").strip()
        last = None if backfill else cursor.get(name)
        if last != head:
            rng = f"{last}..origin/{branch}" if last else f"origin/{branch}"
            log = git(repo_dir, "log", "--no-renames", "--name-only", "--format=%x1e%H%x1f%aI%x1f%an%x1f%s", rng)
            counts = upsert(root, f"git/{name.split('/')[1]}", parse_log(log, name, identity), by="year")
            totals["new"] += counts["new"]
            totals["changed"] += counts["changed"]
        spec = collect_spec(repo_dir, name, branch)
        write_jsonl(root / "data" / "raw" / "spec" / f"{name.split('/')[1]}.jsonl", sorted(spec, key=lambda r: r["id"]))
        totals["spec_sections"] += len(spec)
        cursor[name] = head
    identity.save_unresolved("git")
    state.save(root, "git", ok=True, counts={"last_new": totals["new"], "spec_sections": totals["spec_sections"]}, cursor=cursor)
    state.save(root, "spec", ok=True, counts={"sections": totals["spec_sections"]})
    return totals
