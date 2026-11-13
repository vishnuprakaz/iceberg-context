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

1. **Start of a session:** run `kb status`. It shows how fresh each source is and whether a sync failed. If a source you rely
   on is stale, say so.
2. **Before changing Iceberg code:** run `kb context <paths>` for the files you will touch, and `kb why <path>` for the history
   of the ones that matter. Check the open pull requests it lists so you do not duplicate work. Read the upstream `AGENTS.md`
   and `CONTRIBUTING.md` in the repository you are editing.
3. **Questions about the project, people, decisions or history:** start with the specific command (`initiative`, `group`,
   `person`, `who-to-ask`, `whats-new`, `upcoming`, `opportunities`); otherwise `kb search <words>`. Then run `kb source <id>`
   on what you plan to use and read it before you state what it says.
4. **Cite everything.** Give the link that `kb source` prints, or the page path, for each claim. If you found no source, say
   that plainly. Do not fill the gap from memory.
5. **Say how you know.** Links are labeled `observed` (straight from data), `extracted` (taken by an AI model from a cited
   source) or `inferred` (an AI judgment, such as who is speaking in a recording). Meeting and thread summaries are AI-written;
   transcripts are machine captions without speaker names. Pass that on when it matters.
6. **Asked to sync or update the knowledge base:** use the `iceberg-context-sync` skill.

## Commands

| Command | Use it for |
|---|---|
| `kb status` | Freshness of each source, failures, size of the knowledge base |
| `kb search <words> [--type T] [--since 30d] [--limit N]` | Full-text search over pages and records. Put a phrase in double quotes. Types: `initiative`, `group`, `person`, `module`, `meeting`, `thread`, `email`, `pr`, `issue`, `comment`, `meeting-notes`, `transcript`, `spec-section`, `doc` |
| `kb source <id> [--grep text] [--chars N]` | The text and link behind any id. `--grep` shows only the matching passages |
| `kb why <path> [--limit N]` | History of a file or directory: commits, their pull requests, and the list threads and meetings that discussed them. A file name alone works (`SnapshotProducer.java`). With `--symbol <name> --checkout <clone>` it adds `git log -L` for one function |
| `kb context <paths…>` | Before editing: active authors and reviewers, open pull requests on the same files, latest changes and what was said about them |
| `kb initiative <name>` | An effort such as `v4-metadata-tree` or `materialized-views`: what it is, current state, timeline, where help is needed |
| `kb group <name>` | A working group: cadence, notes document, recent and upcoming meetings |
| `kb person <login>` | Public roles and project activity of a contributor |
| `kb who-to-ask <path or topic>` | Who writes and reviews a path, or which group and people handle a topic |
| `kb whats-new [--since 7d] [--area text]` | Votes, results, announcements, discussions, meetings and spec changes since a date |
| `kb upcoming [--days 14]` | Community meetings ahead, with the group page and last notes |
| `kb opportunities [--area python] [--level starter]` | Ranked places to contribute |
| `kb show <id or name>` | Print any page |

Paths are relative to the upstream repository root (`core/src/main/java/…`, `pyiceberg/table/…`).

### Typical questions

- "Why does this code do X?" → `kb why <file>`, then `kb source` on the pull request and thread ids it lists.
- "What is the status of materialized views?" → `kb initiative materialized-views`.
- "Who should review my Flink change?" → `kb who-to-ask flink/` or `kb context <files>`.
- "What happened this week?" → the latest file in `briefings/weekly/`, or `kb whats-new --since 7d`.
- "Where can a newcomer help with PyIceberg?" → `kb opportunities --area python --level starter`.
- "What does the spec say about snapshot timestamps?" → `kb search snapshot timestamp --type spec-section`.

## What is in the repository

- `state-of-iceberg.md`: current overview. `opportunities.md`: where to contribute. `briefings/weekly/`: what changed each week.
- `people/`, `groups/`, `initiatives/`, `modules/`, `releases/`: one page per entity, linked to each other.
- `records/`: one page per meeting and per mailing-list thread.
- `data/raw/`: cleaned source text, one JSON line per email, pull request, meeting section or transcript.
- `research/`: how each source was studied. `reference/process.md` in this skill: how Iceberg makes decisions.

## Rules about people

Describe public project activity only: roles, reviews, votes, proposals, talks. Do not add personal details or guesses about
motives. The people described can read this repository.
