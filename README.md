# Iceberg Context

**A synced, source-cited knowledge base about the Apache Iceberg project and community, packaged as a Claude Code skill, so
contributors and their coding agents know what is happening, why the code is the way it is, and who to talk to.**

[![CI](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml/badge.svg)](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

> Unofficial and community-maintained. Not affiliated with or endorsed by the Apache Software Foundation.
> Apache Iceberg is a trademark of the ASF.

> **Status: early build.** The foundation, the skill and the source research are in place. The collectors that fill the
> knowledge base are being built next; see [Roadmap](#roadmap). `kb status` always shows what is actually synced.

## The problem

What you need to know to contribute to Iceberg is spread over the dev mailing list, GitHub reviews, git history, a dozen
working-group notes documents, a calendar and hundreds of hours of recorded meetings. None of it is linked together, and a coding
agent sees only the code.

## What this gives you

```console
$ kb search "monotonically increasing snapshot timestamps" --limit 1
(nothing matched every word; showing matches for any of them)

file:research/2026-11-13/dev-mailing-list.md  [doc]
  dev@iceberg.apache.org: source research (2026-11-13)
  … | 10-07 | [VOTE] [Monotonic] [snapshot] [timestamps] in v4 | 22 | Steven Wu | Passed | …

1 result(s). Show one with: kb source <id>
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

Planned: `why` (history behind a file), `context` (what to know before editing), `initiative`, `person`, `who-to-ask`,
`whats-new`, `upcoming`, `opportunities`.

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

## Roadmap

- [x] Phase 0: foundation, schemas, validators, CI, first `kb` commands
- [ ] Phase 1: daily collectors (dev list, GitHub, git, spec, roster) and the code map
- [ ] Phase 2: seed pages for people, working groups, initiatives and modules
- [ ] Phase 3: meeting notes, calendar and transcript collectors; AI summaries
- [ ] Phase 4: six months of history
- [ ] Phase 5: weekly schedule, full command set

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
