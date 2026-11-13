"""Generate people, group, module, repository and release pages from observed data. No AI involved."""
from __future__ import annotations

import re
from collections import Counter, defaultdict

from icekb.integrate.store import Data, link, write_page

WINDOW_DAYS = 365
JAVA_MODULES = {"api", "core", "data", "parquet", "orc", "arrow", "spark", "flink", "kafka-connect", "aws", "gcp", "azure",
                "hive-metastore", "mr", "nessie", "open-api", "format", "docs", "site", "bigquery", "snowflake", "delta-lake"}
MODULE_NOTES = {
    "api": "Public interfaces and types. Strongest stability guarantees; breaking changes are almost never accepted.",
    "core": "Engine-agnostic implementation of the table spec: metadata, snapshots, manifests, commits, REST client.",
    "format": "The specifications. Any change here needs a vote on the dev list.",
    "open-api": "REST catalog OpenAPI specification. Spec changes need a vote on the dev list.",
    "spark": "Spark integration, one copy of the source tree per supported Spark version.",
    "flink": "Flink integration: sources, sinks, table maintenance.",
    "data": "Generic readers, writers and delete handling shared by engines.",
}
_RELEASE = re.compile(r"\[ANNOUNCE\]\s*(?:Release\s+)?Apache\s+(Iceberg(?:\s+(?:Rust|Python|Go|C\+\+|Cpp|Terraform Provider))?|PyIceberg)\s*"
                      r"(?:Release\s+|version\s+)?v?(\d+\.\d+\.\d+)", re.I)
_PRODUCT = {"iceberg": "iceberg", "pyiceberg": "iceberg-python", "iceberg python": "iceberg-python", "iceberg rust": "iceberg-rust",
            "iceberg go": "iceberg-go", "iceberg c++": "iceberg-cpp", "iceberg cpp": "iceberg-cpp",
            "iceberg terraform provider": "terraform-provider-iceberg"}


def module_of(repo: str, path: str) -> str | None:
    parts = path.split("/")
    if repo == "apache/iceberg":
        if parts[0] in JAVA_MODULES:
            return f"iceberg/{parts[0]}"
        if parts[0] in (".github", "gradle", "dev", "baseline.gradle", "build.gradle", "settings.gradle", "gradle.properties"):
            return "iceberg/build"
        return None
    if parts[0] == "pyiceberg" and len(parts) > 1:
        return f"iceberg-python/{parts[1].removesuffix('.py')}" if parts[1] in PY_MODULES or parts[1].removesuffix(".py") in PY_MODULES else None
    if parts[0] in ("mkdocs",):
        return "iceberg-python/docs"
    return None


PY_MODULES = {"table", "catalog", "io", "expressions", "avro", "cli", "utils", "schema", "manifest", "transforms", "types", "partitioning"}


def commit_modules(commit: dict) -> set[str]:
    repo = commit["meta"]["repo"]
    return {m for m in (module_of(repo, f) for f in commit["meta"].get("files", [])) if m}


def is_person(p: str) -> bool:
    return not p.startswith(("name:", "asf:")) and "[bot]" not in p


def build(data: Data) -> dict:
    root, today = data.root, data.today.isoformat()
    recent = data.since(WINDOW_DAYS)
    counts = Counter()

    # ---------------------------------------------------------------- activity indexes
    commits_by_person, modules_by_person = defaultdict(list), defaultdict(Counter)
    module_authors_all, module_authors_recent, module_commits = defaultdict(Counter), defaultdict(Counter), defaultdict(list)
    for c in data.by_type["commit"]:
        mods = commit_modules(c)
        for m in mods:
            module_commits[m].append(c)
        for p in filter(is_person, c["people"]):
            for m in mods:
                module_authors_all[m][p] += 1
            if c["date"] >= recent:
                commits_by_person[p].append(c)
                for m in mods:
                    modules_by_person[p][m] += 1
                    module_authors_recent[m][p] += 1
    mails_by_person, started_by_person = Counter(), defaultdict(list)
    for mail in data.by_type["email"]:
        if mail["date"] < recent:
            continue
        for p in filter(is_person, mail["people"]):
            mails_by_person[p] += 1
            if not mail["meta"]["reply"]:
                started_by_person[p].append(mail)
    credited, group_people = defaultdict(Counter), defaultdict(Counter)
    for notes in data.by_type["meeting-notes"]:
        if notes["date"] >= recent:
            for p in notes["people"]:
                credited[p][notes["meta"]["group"]] += 1
                group_people[notes["meta"]["group"]][p] += 1
    reviews_by_person, module_reviewers = Counter(), defaultdict(Counter)
    for pr in data.by_type["pr"]:
        if pr["date"] < data.since(183):
            continue
        mods = {m for m in (module_of(pr["meta"]["repo"], f) for f in pr["meta"].get("files", [])) if m}
        for by in {r["by"] for r in pr["meta"].get("reviews", []) if r.get("by") and r["by"] not in pr["people"]}:
            reviews_by_person[by] += 1
            for m in mods:
                module_reviewers[m][by] += 1
    roster = {r["people"][0]: r["meta"] for r in data.by_type["roster"] if is_person(r["people"][0])}

    # ---------------------------------------------------------------- releases (from [ANNOUNCE] threads)
    releases, rm_of = {}, defaultdict(list)
    for mail in data.by_type["email"]:
        m = _RELEASE.search(mail["title"])
        if not m or mail["meta"]["reply"]:
            continue
        repo = _PRODUCT.get(" ".join(m.group(1).lower().split()))
        if not repo:
            continue
        version = m.group(2)
        releases.setdefault((repo, version), mail)
    release_pages = {f"release/{repo}-{version}": (repo, version, mail) for (repo, version), mail in releases.items()}

    # ---------------------------------------------------------------- modules
    module_ids = {}
    for mod, commits in sorted(module_commits.items()):
        if len(commits) < 25:
            continue
        repo_short, name = mod.split("/")
        repo = f"apache/{repo_short}"
        pid = f"module/{mod}"
        module_ids[mod] = pid
        recent_commits = [c for c in commits if c["date"] >= recent]
        owners = [p for p, _ in module_authors_all[mod].most_common(6)]
        lines = [MODULE_NOTES.get(name, "") if repo_short == "iceberg" else "",
                 f"**Path:** `{name}/` in [{repo}](https://github.com/{repo}) · **Commits:** {len(commits)} in total, "
                 f"{len(recent_commits)} in the last 12 months.", "",
                 "## Who works here", "",
                 "Long-term authors (all time): " + ", ".join(f"{link('person/' + p, data.name(p))} ({n})" for p, n in module_authors_all[mod].most_common(6)),
                 "", "Most active authors (last 12 months): " + (", ".join(
                     f"{link('person/' + p, data.name(p))} ({n})" for p, n in module_authors_recent[mod].most_common(8)) or "none")]
        if module_reviewers[mod]:
            lines += ["", "Most active reviewers (last 6 months): " + ", ".join(
                f"{link('person/' + p, data.name(p))} ({n})" for p, n in module_reviewers[mod].most_common(8))]
        else:
            lines += ["", "Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`."]
        lines += ["", "## Latest changes", ""] + [f"- {c['date'][:10]} {c['title']} ([commit]({c['url']}))" for c in reversed(commits[-8:])]
        meta = {"id": pid, "type": "module", "title": f"{repo_short}: {name}", "repo": repo, "path": name,
                "commits_total": len(commits), "commits_12m": len(recent_commits), "owners": owners,
                "links": [{"rel": "part_of", "to": f"repo/{repo_short}", "confidence": "observed"}]}
        counts["modules"] += write_page(root, f"modules/{repo_short}/{name}.md", meta, meta["title"], "\n".join(x for x in lines if x is not None), today)

    # ---------------------------------------------------------------- people
    score = Counter()
    for p in set(commits_by_person) | set(mails_by_person) | set(credited) | set(reviews_by_person):
        score[p] = len(commits_by_person[p]) * 2 + mails_by_person[p] + sum(credited[p].values()) * 2 + reviews_by_person[p]
    selected = set(roster) | {p for p, s in score.items() if s >= 12 and p in data.aliases}
    selected |= {p for (_, _, mail) in release_pages.values() for p in mail["people"] if is_person(p)}
    group_slugs = {g["slug"] for g in data.cfg["groups"]}
    for (repo, version, mail) in release_pages.values():
        for p in mail["people"]:
            rm_of[p].append((repo, version, mail["date"][:10]))
    for login in sorted(selected, key=str.lower):
        info = data.aliases.get(login) or {}
        role = roster.get(login)
        links, lines = [], []
        if role:
            label = "PMC chair" if role.get("chair") else "PMC member" if role["role"] == "pmc" else "Committer"
            since = f" since {role['pmc_since']}" if role.get("pmc_since") else ""
            lines.append(f"**Role:** {label} of Apache Iceberg{since} ([ASF roster](https://projects.apache.org/committee.html?iceberg)).")
            links.append({"rel": "has_role", "to": "repo/iceberg", "note": label, "confidence": "observed",
                          **({"since": role["pmc_since"]} if role.get("pmc_since") else {})})
        if rm_of[login]:
            recent_rm = sorted(rm_of[login], key=lambda x: x[2], reverse=True)[:6]
            lines.append("**Release manager for:** " + ", ".join(f"{link(f'release/{r}-{v}', f'{r} {v}')} ({d})" for r, v, d in recent_rm) + ".")
            links += [{"rel": "release_manager", "to": f"release/{r}-{v}", "confidence": "observed"} for r, v, _ in recent_rm]
        lines += ["", "## Activity in the last 12 months", "", "Counted from public records; see `kb person " + login + "` for live numbers.", ""]
        nc = len(commits_by_person[login])
        if nc:
            areas = ", ".join(f"{link('module/' + m, m)} ({n})" for m, n in modules_by_person[login].most_common(6) if m in module_ids)
            lines.append(f"- **Merged commits:** {nc}" + (f". Areas: {areas}" if areas else ""))
            links += [{"rel": "contributes", "to": module_ids[m], "n": n, "window": "12m", "confidence": "observed"}
                      for m, n in modules_by_person[login].most_common(6) if m in module_ids and n >= 2]
        if reviews_by_person[login]:
            lines.append(f"- **Pull requests reviewed (6 months):** {reviews_by_person[login]}")
        if mails_by_person[login]:
            started = started_by_person[login]
            kinds = Counter(m["meta"]["kind"] for m in started)
            detail = ", ".join(f"{n} {k}" for k, n in kinds.most_common() if k in ("vote", "discuss", "release-vote", "announce", "result"))
            lines.append(f"- **Dev list:** {mails_by_person[login]} messages, {len(started)} threads started" + (f" ({detail})" if detail else ""))
        if credited[login]:
            groups = ", ".join(f"{link('group/' + g, g)} ({n})" for g, n in credited[login].most_common() if g in group_slugs)
            lines.append(f"- **Named in meeting notes:** {groups}")
            links += [{"rel": "participates", "to": f"group/{g}", "n": n, "window": "12m", "confidence": "observed"}
                      for g, n in credited[login].most_common() if g in group_slugs and n >= 2]
        started = [m for m in started_by_person[login] if m["meta"]["kind"] in ("vote", "discuss", "release-vote", "result", "announce")][-6:]
        if started:
            lines += ["", "## Recent threads started", ""] + [f"- {m['date'][:10]} [{m['title']}]({m['url']}) `{m['id']}`" for m in reversed(started)]
        latest = commits_by_person[login][-6:]
        if latest:
            lines += ["", "## Recent merged changes", ""] + [f"- {c['date'][:10]} {c['title']} ([commit]({c['url']}))" for c in reversed(latest)]
        meta = {"id": f"person/{login}", "type": "person", "title": data.name(login), "login": login,
                "github": f"https://github.com/{login}", "links": links}
        if info.get("asf_id"):
            meta["asf_id"] = info["asf_id"]
        if role:
            meta["roles"] = ["pmc-chair" if role.get("chair") else role["role"]]
        counts["people"] += write_page(root, f"people/{login}.md", meta, meta["title"], "\n".join(lines), today)

    # ---------------------------------------------------------------- repositories
    for repo in data.cfg["repos"]:
        short = repo["name"].split("/")[1]
        rels = sorted(((v, m) for (r, v, m) in release_pages.values() if r == short), key=lambda x: x[1]["date"], reverse=True)
        lines = [f"**Repository:** [{repo['name']}](https://github.com/{repo['name']}) · **Coverage here:** "
                 + ("full (commits, pull requests, issues, reviews)" if repo.get("depth") == "full" else "releases and mentions only"), ""]
        mods = sorted(m for m in module_ids if m.startswith(short + "/"))
        if mods:
            lines += ["## Modules", ""] + [f"- {link('module/' + m, m.split('/')[1])}" for m in mods] + [""]
        if rels:
            lines += ["## Releases announced on the dev list", ""] + [
                f"- {m['date'][:10]} {link(f'release/{short}-{v}', v)}, announced by {link('person/' + m['people'][0], data.name(m['people'][0])) if is_person(m['people'][0]) else m['people'][0][5:]}"
                for v, m in rels[:12]]
        meta = {"id": f"repo/{short}", "type": "repo", "title": repo["name"], "depth": repo.get("depth", "light"), "links": []}
        counts["repos"] += write_page(root, f"repos/{short}.md", meta, repo["name"], "\n".join(lines), today)

    # ---------------------------------------------------------------- releases
    for pid, (repo, version, mail) in sorted(release_pages.items()):
        votes = [m for m in data.by_type["email"] if not m["meta"]["reply"] and m["meta"]["kind"] in ("release-vote", "result")
                 and version in m["title"] and (repo == "iceberg") == (not re.search(r"rust|python|pyiceberg|\bgo\b|c\+\+|cpp|terraform", m["title"], re.I))]
        rm = mail["people"][0]
        lines = [f"**Announced:** {mail['date'][:10]} by {link('person/' + rm, data.name(rm)) if is_person(rm) and rm in selected else rm.removeprefix('name:')} "
                 f"([announcement]({mail['url']}), `{mail['id']}`)", ""]
        if votes:
            lines += ["## Vote threads", ""] + [f"- {m['date'][:10]} [{m['title']}]({m['url']}) `{m['id']}`" for m in votes[-8:]]
        links = [{"rel": "release_of", "to": f"repo/{repo}", "confidence": "observed"}]
        meta = {"id": pid, "type": "release", "title": f"{repo} {version}", "repo": f"apache/{repo}", "version": version,
                "date": mail["date"][:10], "sources": [mail["id"]], "links": links}
        counts["releases"] += write_page(root, f"releases/{repo}-{version}.md", meta, meta["title"], "\n".join(lines), today)

    # ---------------------------------------------------------------- working groups
    upcoming = defaultdict(list)
    for ev in data.by_type["event"]:
        if ev["date"][:10] >= today and ev["meta"].get("group"):
            upcoming[ev["meta"]["group"]].append(ev)
    notes_by_group, videos_by_group = defaultdict(list), defaultdict(list)
    for n in data.by_type["meeting-notes"]:
        notes_by_group[n["meta"]["group"]].append(n)
    for v in data.by_type["transcript"]:
        if v["meta"].get("group"):
            videos_by_group[v["meta"]["group"]].append(v)
    for g in data.cfg["groups"]:
        slug = g["slug"]
        notes, videos = notes_by_group[slug], videos_by_group[slug]
        held = [n for n in notes if n["meta"]["status"] in ("held", "link-only")]
        last = max([n["date"][:10] for n in held] + [v["date"][:10] for v in videos], default=None)
        active = bool(upcoming[slug]) or (last or "") >= data.since(75)
        lines = [f"**Cadence:** {g.get('cadence', 'unknown')} · **Status:** {'active' if active else 'quiet'}"
                 + (f" · **Last meeting on record:** {last}" if last else ""), ""]
        if g.get("doc"):
            lines.append(f"**Notes document:** https://docs.google.com/document/d/{g['doc']}" + (f" (tab “{g['tab']}”)" if g.get("tab") else ""))
        if g.get("playlist"):
            lines.append(f"**Recordings:** playlist “{g['playlist']}” on the Apache Iceberg YouTube channel")
        if upcoming[slug]:
            lines += ["", "## Upcoming", ""] + [f"- {e['date'][:16].replace('T', ' ')} UTC: {e['title']}" for e in upcoming[slug][:4]]
        if group_people[slug]:
            lines += ["", "## People named most often in the notes (last 12 months)", "",
                      ", ".join(f"{link('person/' + p, data.name(p))} ({n})" for p, n in group_people[slug].most_common(12) if p in selected)]
        rows = sorted({n["date"][:10] for n in notes} | {v["date"][:10] for v in videos}, reverse=True)[:12]
        if rows:
            lines += ["", "## Recent meetings", "", "| Date | Notes | Recording | Summary |", "|---|---|---|---|"]
            for d in rows:
                n = next((x for x in notes if x["date"][:10] == d), None)
                v = next((x for x in videos if x["date"][:10] == d), None)
                page = root / "records" / "meetings" / slug / d[:4] / f"{d}.md"
                lines.append(f"| {d} | " + (f"`{n['id']}` ({n['meta']['status']})" if n else "") + " | "
                             + (f"[video]({v['url']}) `{v['id']}`" if v else "") + " | "
                             + (link(f"meeting/{slug}/{d}", "summary") if page.exists() else "") + " |")
        links = [{"rel": "participates_in", "to": f"person/{p}", "n": n, "window": "12m", "confidence": "observed"}
                 for p, n in group_people[slug].most_common(8) if p in selected and n >= 2]
        meta = {"id": f"group/{slug}", "type": "group", "title": g["name"], "cadence": g.get("cadence", "unknown"),
                "status": "active" if active else "quiet", "links": []}
        if g.get("doc"):
            meta["notes_doc"] = f"https://docs.google.com/document/d/{g['doc']}"
        del links
        counts["groups"] += write_page(root, f"groups/{slug}.md", meta, g["name"], "\n".join(lines), today)

    # ---------------------------------------------------------------- maps
    maps = root / "maps"
    maps.mkdir(exist_ok=True)
    out = ["# Module ownership", "", f"Generated {today} from git history. Counts are merged commits touching the module.", "",
           "| Module | Commits (12m / all) | Long-term authors | Most active authors, last 12 months | Most active reviewers, last 6 months |", "|---|---|---|---|---|"]
    for mod in sorted(module_ids):
        out.append(f"| {link('module/' + mod, mod)} | {sum(module_authors_recent[mod].values())} / {len(module_commits[mod])} | "
                   + ", ".join(f"@{p}" for p, _ in module_authors_all[mod].most_common(4)) + " | "
                   + ", ".join(f"@{p} ({n})" for p, n in module_authors_recent[mod].most_common(5)) + " | "
                   + (", ".join(f"@{p} ({n})" for p, n in module_reviewers[mod].most_common(5)) or "not synced yet") + " |")
    text = "\n".join(out) + "\n"
    if not (maps / "ownership.md").exists() or (maps / "ownership.md").read_text().split("\n", 3)[3:] != text.split("\n", 3)[3:]:
        (maps / "ownership.md").write_text(text)
    return dict(counts) | {"people_total": len(selected), "modules_total": len(module_ids), "releases_total": len(release_pages)}
