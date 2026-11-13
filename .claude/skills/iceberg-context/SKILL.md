---
name: iceberg-context
description: Context on the Apache Iceberg project and community for anyone working on apache/iceberg or apache/iceberg-python. Use it before changing Iceberg code, and to answer questions about why code is the way it is, what the community is working on or has decided (dev list, votes, working-group syncs), who owns or reviews an area, or where to contribute. Answers come from a synced knowledge base and cite their sources.
---

# Iceberg Context

A knowledge base about Apache Iceberg (Java) and PyIceberg, synced from the dev mailing list, GitHub, git history, working-group
meeting notes, the community calendar, YouTube recordings and the ASF roster. Query it with the `kb` script in this skill:

```bash
KB=<this skill's directory>/scripts/kb      # Python 3.10+, standard library only
$KB status
```

It is unofficial and not affiliated with the Apache Software Foundation.

## Workflow

1. **Start of a session:** run `kb status`. It shows how fresh each source is and whether a sync failed. If a source is stale,
   say so when you rely on it.
2. **Any question about the project, people, decisions or history:** run `kb search <words>`, then `kb source <id>` on the
   results you plan to use. Read the source before you state what it says.
3. **Cite everything.** Give the link that `kb source` prints for each claim. If you could not find a source, say that plainly
   instead of answering from memory.
4. **Say how you know.** Links in the knowledge base are labeled `observed` (straight from data), `extracted` (taken by an AI
   model from a cited source) or `inferred` (an AI judgment). Pass that label on when it is not `observed`.
5. **Before changing Iceberg code:** read the upstream `AGENTS.md` and `CONTRIBUTING.md` in the repository you are editing, and
   search the knowledge base for the files, classes and feature names involved.

## Commands

| Command | Use it for |
|---|---|
| `kb status` | Freshness of each source, failures, size of the knowledge base |
| `kb search <words> [--type T] [--limit N]` | Full-text search over pages and raw records. Put a phrase in double quotes. |
| `kb source <id> [--grep text] [--chars N]` | The text and link behind an id. `--grep` shows only matching passages. |

More commands (`why`, `context`, `initiative`, `person`, `who-to-ask`, `whats-new`, `upcoming`, `opportunities`) are being added;
`kb --help` lists what is available in this checkout.

## What is in the repository

- `state-of-iceberg.md`: current overview. `opportunities.md`: where to contribute. `briefings/weekly/`: what changed each week.
- `people/`, `groups/`, `initiatives/`, `modules/`, `releases/`: one page per entity, linked to each other.
- `records/`: one page per meeting and per mailing-list thread.
- `data/raw/`: cleaned source text, one JSON line per email, pull request, meeting section or transcript.
- `research/`: how each source was studied. `reference/process.md` in this skill: how Iceberg makes decisions.

## Rules about people

Describe public project activity only: roles, reviews, votes, proposals, talks. Do not add personal details or guesses about
motives. The people described can read this repository.
