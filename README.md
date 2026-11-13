# Iceberg Context Skill

**The full context of Apache Iceberg for your coding agent: why the code is the way it is, what the community is deciding right
now, who reviews what, and where to contribute. Every answer comes with its source.**

[![CI](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml/badge.svg)](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-agentskills.io-6b4fbb.svg)](https://agentskills.io)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

An [Agent Skill](https://agentskills.io), also packaged as a Claude Code plugin. It ships with a knowledge base that is synced
from the Iceberg dev mailing list, pull requests and reviews, git history, the spec, working-group meeting notes and recordings,
and the community calendar, all linked to the codebase.

> Unofficial and community-maintained. Not affiliated with or endorsed by the Apache Software Foundation.
> Apache Iceberg is a trademark of the ASF.

## Contents

- [Why this skill](#why-this-skill)
- [What your agent can do with it](#what-your-agent-can-do-with-it)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Usage examples](#usage-examples)
- [What is inside](#what-is-inside)
- [Staying up to date](#staying-up-to-date)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing) · [License](#license)

## Why this skill

An agent working on Iceberg sees the code and nothing else. The reasons behind the code, the decisions in progress and the people
who make them are spread over a mailing list, thousands of pull-request reviews, a dozen working-group notes documents and
hundreds of hours of recorded meetings.

This skill keeps all of that in one place, in sync with the codebase, and teaches your agent to use it and to cite it.

## What your agent can do with it

- **Explain why code is the way it is.** From a file to its commits, the pull requests, and the vote or meeting where the change was decided.
- **Check before it edits.** Who is changing those files, who reviews them, which open pull requests overlap.
- **Track the community.** The state and timeline of 35 efforts: v4 metadata, materialized views, variant, REST catalog changes and more.
- **Brief you on the week.** Votes, results, design discussions, releases and upcoming meetings.
- **Point you to people.** Active authors and reviewers for any path or topic, and the working group that handles it.
- **Find you work.** A ranked list of places to contribute, with evidence, who to ask and a first step.
- **Help maintainers and the PMC.** Vote tallies split into binding and non-binding and checked against the result email, the
  review queue by whose turn it is, release status, a board-report draft, past decisions and loose ends.
- **Prove it.** Each answer links to a mailing-list message, a pull request, a notes section or a moment in a recording.

## Installation

Requirements: Python 3.10 or newer and git. No packages to install.

### Option 1: Claude Code plugin (recommended)

On Claude Code 2.1.275 or later, one step:

```
/plugin install iceberg-context --marketplace vishnuprakaz/iceberg-context
```

On earlier versions, two steps:

```
/plugin marketplace add vishnuprakaz/iceberg-context
```

```
/plugin install iceberg-context@iceberg-context
```

This installs both skills and the sync agents, together with the knowledge base. Update with `/plugin marketplace update iceberg-context`.

### Option 2: `skills` CLI (Claude Code, Cursor, Codex, Gemini CLI and other agents)

```bash
npx skills add vishnuprakaz/iceberg-context --skill iceberg-context --global
```

Leave out `--global` to install for the current project only. The skill folder is installed on its own; on first use it
downloads the knowledge base (about 80 MB) and then refreshes it every 12 hours.

### Option 3: Claude Code on the web

Add `vishnuprakaz/iceberg-context` to your session or to your environment's repository list. The skill loads automatically.

### Option 4: Manual

```bash
git clone --depth 1 https://github.com/vishnuprakaz/iceberg-context
```

```bash
cp -r iceberg-context/skills/iceberg-context ~/.claude/skills/
```

For other agents, copy `skills/iceberg-context/` into the skill directory your agent documents.

### Verify

```bash
python3 ~/.claude/skills/iceberg-context/scripts/kb status
```

You should see a table of sources with their last sync time. Then ask your agent: *"What is the Iceberg community working on for v4?"*

## Quick start

Just ask. The skill loads when a question is about Iceberg's code history, community or contribution, for example:

- "Why does `SnapshotProducer` check that snapshot timestamps increase?"
- "I'm about to change the Flink sink commit path. Anything I should know first?"
- "Where are materialized views at, and who should I talk to about helping?"
- "What happened on the Iceberg dev list this week?"
- "I know Python. What could I pick up in PyIceberg?"
- "Which votes are open, and do they have enough binding +1s?" (maintainers)
- "What has been waiting longest for a committer review in Spark?" (maintainers)

## Usage examples

The skill works through one command, `kb`, which your agent runs for you. You can run it yourself too.

**History behind a file**

```console
$ kb why SnapshotProducer.java --limit 1
2026-11-13  API, Core: Add Snapshot.rootManifestLocation() (#17523)
    by @stevenzwu   https://github.com/apache/iceberg/commit/58cf9d8bba9f…
    PR gh:apache/iceberg#17523: reviewed by @amogh-jahagirdar, @anoopj, @gaborkaszab, @nastra, @rdblue; merged by @stevenzwu; 51 comments
    ↳ meeting-notes 2026-08-18  Spark Community Sync notes, 2026-08-18  [meet:spark:2026-08-18]
```

**Before a change**

```console
$ kb context core/src/main/java/org/apache/iceberg/SnapshotProducer.java
  active authors in this directory since 2025-11-13: @anoopj (33), @nastra (32), @gaborkaszab (26), …
  latest changes:
    2026-10-07  Core: ensure snapshot timestamp is monotonically increasing for V4 tables (#16293)
        ↳ email 2026-10-07  [VOTE] Require monotonically increasing snapshot timestamps in v4
```

**Who to ask**

```console
$ kb who-to-ask flink/
  authors of merged changes: @mxm (58), @Guosmilesmile (34), @talatuyarer (24), …
  reviewers: @pvary (83), @mxm (44), @huaxingao (41), …
```

**For maintainers: a vote**

```console
$ kb votes --match default value expressions
[VOTE] Default Value Expressions for v4  [vote:t-33958badf295b701]
  opened 2026-11-02 by @danielcweeks; 20 messages; https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob
  result: passed on 2026-11-06 by @danielcweeks  [devlist:h5jnk7l2op325x545hfnrpbo3qmh2ovo]
  binding +1 11, 0 0, -1 0  |  non-binding +1 7, 0 0, -1 0  |  unverified +1 1, 0 0, -1 0
  check against the result email: match
```

All commands: `status`, `update`, `search`, `source`, `why`, `context`, `initiative`, `group`, `person`, `who-to-ask`,
`whats-new`, `upcoming`, `opportunities`, and for maintainers `votes`, `review-queue`, `release`, `board-report`, `decisions`,
`loose-ends`. See the [command reference](skills/iceberg-context/references/commands.md).

Prefer reading? Start with the [state of Iceberg](kb/state-of-iceberg.md), the [weekly briefings](kb/briefings/weekly/) and the
[opportunities list](kb/opportunities.md).

## What is inside

| Skill | What it does |
|---|---|
| [`iceberg-context`](skills/iceberg-context/SKILL.md) | Answers questions about Iceberg's code history, community and contribution paths from the knowledge base |
| [`iceberg-context-sync`](skills/iceberg-context-sync/SKILL.md) | Maintainer runbook: refreshes the knowledge base and writes the weekly briefing |

```
iceberg-context/
├── .claude-plugin/          plugin and marketplace manifests
├── skills/
│   ├── iceberg-context/     the skill: SKILL.md, scripts/kb, references/
│   └── iceberg-context-sync/
├── agents/                  agents used by the weekly sync
├── kb/                      the knowledge base: overview, briefings, initiatives, groups, people, modules, records
├── data/                    cleaned source records and sync state
├── pipeline/                collectors and processing
└── docs/                    status, pipeline reference, testing
```

## Staying up to date

The knowledge base is refreshed in this repository every six hours (mailing list, GitHub, git history) and weekly (meeting
notes, calendar, recordings, summaries and the briefing).

- Installed with the `skills` CLI: the skill refreshes its copy every 12 hours. `kb update` fetches now.
- Installed as a plugin: `/plugin marketplace update iceberg-context`.
- Cloned: `git pull`.

`kb status` shows how fresh each source is. Coverage and known limits are in [docs/status.md](docs/status.md).

## Troubleshooting

| Problem | Fix |
|---|---|
| `kb: could not download the knowledge base` | No access to github.com or no git. Clone the repository elsewhere and set `ICEBERG_CONTEXT_ROOT` to it |
| The first command after an update is slow | The search index is being rebuilt; later commands are fast |
| `no results` | Use fewer or more specific words, or put an exact phrase in double quotes |
| Answers look out of date | Run `kb update`, then `kb status` |
| `SyntaxError` on start | Python is older than 3.10 |
| The skill does not load | Check that `SKILL.md` is at `~/.claude/skills/iceberg-context/SKILL.md`, then restart your agent |

More in the skill's own [troubleshooting section](skills/iceberg-context/SKILL.md#troubleshooting).

## What is an Agent Skill?

[Agent Skills](https://agentskills.io) are folders of instructions, scripts and resources that an agent discovers and loads only
when a task needs them. This one follows the open specification, so it works in Claude Code and in other agents that support skills.

## Contributing

Corrections, notes and new sources are welcome: see [CONTRIBUTING](.github/CONTRIBUTING.md). Only public project activity is
recorded about people; see [PRIVACY](PRIVACY.md) to ask for a correction. Summaries of meetings and threads are written by an AI
model, checked against their sources, and always link to them. Security: [SECURITY](.github/SECURITY.md).

## License

Code: [Apache-2.0](LICENSE). Knowledge-base pages: [CC BY 4.0](LICENSE-CONTENT.md). Sources and trademarks: [NOTICE](NOTICE).
