# Iceberg Context

**A skill that gives your coding agent the full picture of Apache Iceberg: what the community is doing right now, and why the
code is the way it is, with a source for every answer.**

[![CI](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml/badge.svg)](https://github.com/vishnuprakaz/iceberg-context/actions/workflows/ci.yml)
[![Code: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)

> Unofficial and community-maintained. Not affiliated with or endorsed by the Apache Software Foundation.
> Apache Iceberg is a trademark of the ASF.

## Why

An agent working on Iceberg sees the code and nothing else. The reasons behind the code, the decisions in progress and the people
who make them are spread over the dev mailing list, pull-request reviews, a dozen working-group notes documents and hundreds of
hours of recorded meetings.

Iceberg Context keeps all of that synced in one place, linked to the codebase, and hands it to your agent as a skill.

## What your agent gains

| It can answer | Example |
|---|---|
| **Why is this code like this?** | From a file to its commits, the pull requests, and the vote or meeting where the change was decided |
| **What should I know before I change it?** | Who is working on those files, who reviews them, which open pull requests overlap |
| **What is the community working on?** | The state and timeline of each effort: v4 metadata, materialized views, variant, REST catalog changes and more |
| **What happened this week?** | Votes, results, design discussions, releases and meetings, in a weekly briefing |
| **Who should I talk to?** | Active authors and reviewers for any path or topic, and the working group that handles it |
| **Where can I contribute?** | A ranked list of openings with the evidence, the people to ask and a first step |

Every answer links to its source: a mailing-list message, a pull request, a section of meeting notes or a moment in a recording.

```console
$ kb context core/src/main/java/org/apache/iceberg/SnapshotProducer.java
  active authors in this directory since 2025-11-13: @anoopj (33), @nastra (32), @gaborkaszab (26), …
  latest changes:
    2026-10-07  Core: ensure snapshot timestamp is monotonically increasing for V4 tables (#16293)
        ↳ email 2026-10-07  [VOTE] Require monotonically increasing snapshot timestamps in v4
        ↳ email 2026-05-12  Re: [DISCUSS] row timestamp proposal
```

## Get started

**Claude Code in the cloud:** add `vishnuprakaz/iceberg-context` to your session or environment. The skill loads on its own.
Then ask, for example, "what is the status of materialized views, and who should I talk to about helping?"

**On your machine:**

```bash
git clone --depth 1 https://github.com/vishnuprakaz/iceberg-context
```

```bash
python3 iceberg-context/.claude/skills/iceberg-context/scripts/kb status
```

It needs Python 3.10 or newer and nothing else. To use the skill in every project, copy
`.claude/skills/iceberg-context` to `~/.claude/skills/` and set `ICEBERG_CONTEXT_ROOT` to the clone. Update with `git pull`.

## Read it yourself

You do not need an agent. Start here:

- [State of Iceberg](kb/state-of-iceberg.md): the current overview
- [Weekly briefings](kb/briefings/weekly/): what changed each week
- [Opportunities](kb/opportunities.md): where to contribute
- [Initiatives](kb/initiatives/), [working groups](kb/groups/), [meeting and thread summaries](kb/records/)

## Kept in sync

The mailing list, GitHub and git history are collected every six hours; meeting notes, the calendar and recordings once a week,
when new meetings and threads are summarized and the pages updated. `kb status` shows how fresh each source is.

Current coverage and known limits are in [docs/status.md](docs/status.md).

## Learn more

| | |
|---|---|
| [docs/status.md](docs/status.md) | What is synced, what is not, known limits |
| [docs/pipeline.md](docs/pipeline.md) | How the data is collected and processed |
| [docs/skill-testing.md](docs/skill-testing.md) | How the skill is tested |
| [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) | How to add notes, fix a page or add a source |
| [PRIVACY.md](PRIVACY.md) | What is recorded about people, and how to ask for a correction |

Only public project activity is recorded. Summaries of meetings and threads are written by an AI model, checked against their
sources, and always link to them.

Code: [Apache-2.0](LICENSE). Knowledge-base pages: [CC BY 4.0](LICENSE-CONTENT.md). Sources: [NOTICE](NOTICE).
Security: [.github/SECURITY.md](.github/SECURITY.md).
