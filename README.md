# Iceberg Context

**A synced, source-cited knowledge base about the Apache Iceberg project and community, packaged as a Claude Code skill, so
contributors and their coding agents know what is happening, why the code is the way it is, and who to talk to.**

[![CI](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml/badge.svg)](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

> Unofficial and community-maintained. Not affiliated with or endorsed by the Apache Software Foundation.
> Apache Iceberg is a trademark of the ASF.

> **Status: first full build, November 2026.** The mailing list (since 2018), git history, the spec, meeting notes and the
> calendar are synced; pull-request history is filling in over several days; recording transcripts are limited (see
> [Known limits](#known-limits)). `kb status` always shows what is actually synced.

## The problem

What you need to know to contribute to Iceberg is spread over the dev mailing list, GitHub reviews, git history, a dozen
working-group notes documents, a calendar and hundreds of hours of recorded meetings. None of it is linked together, and a coding
agent sees only the code.

## What this gives you

Ask why a file is the way it is, and get its history tied to the votes and discussions behind it:

```console
$ kb context core/src/main/java/org/apache/iceberg/SnapshotProducer.java
== core/src/main/java/org/apache/iceberg/SnapshotProducer.java
  active authors in this directory since 2025-11-13: @anoopj (33), @nastra (32), @gaborkaszab (26), …
  latest changes:
    2026-10-07  Core: ensure snapshot timestamp is monotonically increasing for V4 tables (#16293)
        ↳ email 2026-10-07  [VOTE] Require monotonically increasing snapshot timestamps in v4  [devlist:…]
        ↳ email 2026-05-12  Re: [DISCUSS] row timestamp proposal  [devlist:…]
```

Ask what the community decided, and get the meeting with the moment it was said:

```console
$ kb search "derived columns index spec" --type meeting --limit 1
meeting/index/2026-11-09  [meeting]
  Index Support Sync, 2026-11-09
  … ## [Derived] [columns] in the [index] schema Peter asked whether [derived] [columns], needed …
```

Every answer points back to its source: a mailing-list thread, a pull request, a section of meeting notes or a video timestamp.

## Quick start

**In a Claude Code cloud session:** add `vishnuprakaz/iceberg-context` to the session or to your environment's repository list.
The `iceberg-context` skill loads on its own. Ask Claude something like "what is the community working on in v4?".

**On your own machine:**

```bash
git clone --depth 1 https://github.com/vishnuprakaz/iceberg-context
```

```bash
python3 iceberg-context/.claude/skills/iceberg-context/scripts/kb status
```

To make the skill available in every Claude Code project, copy it to your user skills and tell it where the clone is:

```bash
cp -r iceberg-context/.claude/skills/iceberg-context ~/.claude/skills/
```

```bash
export ICEBERG_CONTEXT_ROOT="$PWD/iceberg-context"
```

`kb` needs Python 3.10 or newer and nothing else. To update, run `git pull` in the clone. To remove it, delete the clone and
`~/.claude/skills/iceberg-context`.

## Commands

| Command | What it answers |
|---|---|
| `kb status` | How fresh each source is, whether a sync failed, how much the knowledge base holds |
| `kb search <words>` | Full-text search over pages and source records |
| `kb source <id>` | The exact text and link behind a result |
| `kb why <path>` | History of a file: commits, pull requests, and the threads and meetings that discussed them |
| `kb context <paths>` | What to know before editing: active authors, reviewers, open pull requests, recent decisions |
| `kb initiative <name>` | Status and timeline of an effort such as `v4-metadata-tree` or `materialized-views` |
| `kb group <name>` / `kb person <login>` | A working group or a contributor's public project activity |
| `kb who-to-ask <path or topic>` | Who writes and reviews an area, and which group handles it |
| `kb whats-new --since 7d` | Votes, results, discussions, meetings and spec changes since a date |
| `kb upcoming` | Community meetings in the coming days |
| `kb opportunities` | Ranked places to contribute |

## How it works

```
collect  →  normalize  →  link  →  process (AI)  →  integrate  →  validate  →  commit
```

- **Daily**, a GitHub Action collects the dev mailing list, pull requests and reviews, git history, the spec and the ASF roster.
- **Weekly**, a scheduled Claude session collects meeting notes, the calendar and recording transcripts, then summarizes what is
  new, updates the pages for people, working groups, initiatives and modules, and writes a briefing.
- Pages are Markdown with typed links in their headers, so the repository is a graph you can read on GitHub or open in Obsidian.

Details: [build plan](docs/build-plan.md), [design](docs/knowledge-base-plan.md), [source research](research/2026-11-13/).

## Repository map

| Path | Contents |
|---|---|
| `.claude/skills/iceberg-context/` | The skill and the `kb` script |
| `people/` `groups/` `initiatives/` `modules/` `releases/` | One page per entity |
| `records/` | One page per meeting and mailing-list thread |
| `data/raw/` | Cleaned source text. `data/sources.yaml` lists every source |
| `pipeline/icekb/` | Collectors, validators and the index builder |
| `notes/` | Human notes; the pipeline never writes here |
| `research/` | How each source was studied |

## Known limits

- **Recording transcripts.** YouTube answers requests from cloud servers with a bot check, so the collector cannot fetch
  captions from GitHub Actions or a cloud session. Three meetings have transcripts; the rest are summarized from their notes.
  Captions fetched on a personal machine can be added with `icekb ingest transcript`.
- **Pull requests and reviews.** GitHub's token limits mean full history arrives over several days of scheduled runs. Until
  then `kb why` shows commits and discussions but not every review.
- **AI summaries.** Meeting and thread pages are written by an AI model and checked mechanically (sources must exist, quotes
  must match the transcript). They can still be wrong; each page links its sources.
- **Thread splitting.** A few long mailing-list threads are stored as two parts when a mail client truncated the reply chain.
- **Names.** People are matched to GitHub logins through `people/aliases.yaml`, which is partly unverified. Unmatched names
  appear as plain names.
- **Scope.** Java and PyIceberg in depth; Rust, Go and C++ through the mailing list and meeting notes only. Slack is not collected.

## Roadmap

- [x] Foundation, schemas, validators, CI
- [x] Collectors: mailing list, git history and spec, ASF roster, GitHub (in Actions), meeting notes, calendar
- [x] Pages for people, working groups, modules, releases; AI summaries of six months of meetings and threads
- [x] Initiative pages, overview, opportunities, weekly briefing
- [ ] Weekly scheduled sync running unattended for two consecutive weeks
- [ ] Transcripts for all recordings
- [ ] Website with a graph view

## Development

```bash
uv sync
```

```bash
uv run pytest && uv run ruff check . && uv run python -m icekb validate
```

## People and privacy

Only public project activity is recorded: roles, reviews, votes, proposals, talks. No email addresses and no personal details.
To ask for a correction or removal, see [PRIVACY.md](PRIVACY.md).

## Contributing, security, licence

- [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- Code: [Apache-2.0](LICENSE). Knowledge-base pages: [CC BY 4.0](LICENSE-CONTENT.md). Source attribution: [NOTICE](NOTICE).
