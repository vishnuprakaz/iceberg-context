---
name: iceberg-context
description: Answers questions about the Apache Iceberg project and community from a synced, source-cited knowledge base (dev mailing list, pull requests and reviews, git history, spec, working-group notes and recordings, calendar, ASF roster), for contributors, committers and PMC members. Use before changing code in apache/iceberg or apache/iceberg-python, and when the user asks "why is this code like this", "what did the community decide", "what is the status of" a proposal such as v4 or materialized views, "who reviews" an area, "what happened on the dev list this week", "where can I contribute", "open votes", "is the vote passing", "binding votes", "review queue", "PRs waiting for review", "release readiness", "board report", "did we already decide" or "unowned action items". Do not use for how to use Iceberg as a product (SQL, configuration, tuning); answer those from the Iceberg documentation.
license: Apache-2.0
compatibility: Claude Code or any agent with a shell, Python 3.10+ and git. The knowledge base is data in the skill repository; when the skill is installed without it, the script downloads a copy on first use (about 80 MB, network access to github.com) and refreshes it every 12 hours. No Python packages needed.
metadata:
  author: Iceberg Context contributors
  version: 0.1.0
  repository: https://github.com/vishnuprakaz/iceberg-context
  category: open-source-contribution
---

# Iceberg Context

A knowledge base about Apache Iceberg (Java) and PyIceberg, synced from the dev mailing list, GitHub, git history, working-group
meeting notes, the community calendar, YouTube recordings and the ASF roster. Query it with the `kb` script in this skill:

```bash
python3 SKILL_DIR/scripts/kb status
```

`SKILL_DIR` is the directory that contains this file. In the examples below, `kb` stands for `python3 SKILL_DIR/scripts/kb`. The script finds
the knowledge base on its own: inside the skill's repository when it is installed as a plugin or attached to the session,
otherwise in a copy it downloads on first use and refreshes every 12 hours. `kb update` fetches the latest now. Set
`ICEBERG_CONTEXT_ROOT` to use a specific checkout, or `ICEBERG_CONTEXT_OFFLINE=1` to stop all network use.

It is unofficial and not affiliated with the Apache Software Foundation.

## Workflow

1. **Start of a session:** run `kb status`. It shows how fresh each source is and whether a sync failed. If a source you rely
   on is stale, say so.
2. **Before changing Iceberg code:** run `kb context PATHS` for the files you will touch, and `kb why PATH` for the history
   of the ones that matter. Check the open pull requests it lists so you do not duplicate work. Read the upstream `AGENTS.md`
   and `CONTRIBUTING.md` in the repository you are editing.
3. **Questions about the project, people, decisions or history:** start with the specific command (`initiative`, `group`,
   `person`, `who-to-ask`, `whats-new`, `upcoming`, `opportunities`); otherwise `kb search WORDS`. Then run `kb source ID`
   on what you plan to use and read it before you state what it says.
4. **Cite everything.** Give the link that `kb source` prints, or the page path, for each claim. If you found no source, say
   that plainly. Do not fill the gap from memory.
5. **Say how you know.** Links are labeled `observed` (straight from data), `extracted` (taken by an AI model from a cited
   source) or `inferred` (an AI judgment, such as who is speaking in a recording). Meeting and thread summaries are AI-written;
   transcripts are machine captions without speaker names. Pass that on when it matters.
6. **Maintainer and PMC questions** (votes, review queue, releases, board report, decisions, loose ends): use the commands
   in the next section and read `references/maintainers.md` first.
7. **Asked to sync or update the knowledge base:** use the `iceberg-context-sync` skill.

## Commands

| Command | Use it for |
|---|---|
| `kb status` | Freshness of each source, failures, size of the knowledge base |
| `kb update` | Fetch the latest knowledge base now |
| `kb search WORDS [--type T] [--since 30d] [--limit N]` | Full-text search over pages and records. Put a phrase in double quotes. Types: `initiative`, `group`, `person`, `module`, `meeting`, `thread`, `email`, `pr`, `issue`, `comment`, `meeting-notes`, `transcript`, `spec-section`, `doc` |
| `kb source ID [--grep text] [--chars N]` | The text and link behind any id. `--grep` shows only the matching passages |
| `kb why PATH [--limit N]` | History of a file or directory: commits, their pull requests, and the list threads and meetings that discussed them. A file name alone works (`SnapshotProducer.java`). With `--symbol NAME --checkout CLONE` it adds `git log -L` for one function |
| `kb context PATHS` | Before editing: active authors and reviewers, open pull requests on the same files, latest changes and what was said about them |
| `kb initiative NAME` | An effort such as `v4-metadata-tree` or `materialized-views`: what it is, current state, timeline, where help is needed |
| `kb group NAME` | A working group: cadence, notes document, recent and upcoming meetings |
| `kb person LOGIN` | Public roles and project activity of a contributor |
| `kb who-to-ask PATH_OR_TOPIC` | Who writes and reviews a path, or which group and people handle a topic |
| `kb whats-new [--since 7d] [--area text]` | Votes, results, announcements, discussions, meetings and spec changes since a date |
| `kb upcoming [--days 14]` | Community meetings ahead, with the group page and last notes |
| `kb opportunities [--area python] [--level starter]` | Ranked places to contribute |
| `kb show ID_OR_NAME` | Print any page |

Paths are relative to the upstream repository root (`core/src/main/java/…`, `pyiceberg/table/…`).

## Maintainer and PMC tasks

| Command | Use it for |
|---|---|
| `kb votes [--open] [--match WORDS] [--since 30d]` | Votes with binding, non-binding and unverified tallies, deadline, result, and a check against the result email |
| `kb review-queue [--path DIR] [--stale 14]` | Open pull requests by whose turn it is, first-time contributors with no review, time to first review per area |
| `kb release VERSION [--repo python]` | Release votes and candidates, release manager, milestone pull requests, release discussions |
| `kb board-report [--quarter 2026Q4]` | A draft of the quarterly ASF board report with counts from the archives |
| `kb decisions TOPIC` | Past votes and decisions on a topic, newest first |
| `kb loose-ends [--since 60d]` | Unowned action items, discussions with no conclusion, dev@ threads with no reply |

Details, how binding is decided and worked examples: `references/maintainers.md`. Rules for these answers:

- Never suggest, rank or compare people as candidates for committer or PMC membership, and never guess what was said on
  private lists. Those discussions are private by ASF policy.
- Report health numbers in aggregate (per area or period), never as a list of slow or inactive people.
- Give counts with their uncertainty, for example "5 binding +1 (1 voter unverified)", and pass on any mismatch with the
  result email.
- The dev@ thread is the record. Link to it for every vote, result and decision.

## Examples

**Example 1: the reason behind code**
User says: "Why does SnapshotProducer check that snapshot timestamps increase?"
Actions:
1. `kb why SnapshotProducer.java` lists the commits and pull requests that touched the file, with the list threads and meetings that mention each pull request.
2. `kb source ID` on the vote thread and the pull request it shows.
Result: an answer that names the pull request, the dev-list vote and what was decided, each with its link.

**Example 2: status of a proposal**
User says: "Where are materialized views at, and who should I talk to about helping?"
Actions:
1. `kb initiative materialized-views` for the current state, timeline and "where help is needed".
2. `kb group materialized-views` and `kb upcoming` for the working group and its next meeting.
Result: the state with dates and sources, the people driving it, and when the group next meets.

**Example 3: before a change**
User says: "I'm going to change how the Flink sink commits. Anything I should know?"
Actions:
1. `kb context flink/v2.1/flink/src/main/java/org/apache/iceberg/flink/sink/` for active authors, reviewers and open pull requests on those files.
2. `kb search "flink sink commit" --since 6m` for recent discussion.
Result: who reviews the area, pull requests that overlap, and recent decisions to respect.

**Example 4: finding work**
User says: "I know Python. What could I pick up?"
Actions: `kb opportunities --area python`, then `kb source` or the linked pages for the one the user likes.
Result: a short list with level, evidence, who to talk to and a first step.

More command options and query patterns: `references/commands.md`. How Iceberg makes decisions: `references/process.md`.
Terms: `references/glossary.md`.

## Troubleshooting

**`kb: could not download the knowledge base`**
Cause: no network access to github.com, or git is missing. Fix: clone the repository where there is access and set
`ICEBERG_CONTEXT_ROOT=/path/to/iceberg-context`.

**Answers look out of date**
Run `kb update`, then `kb status`. A downloaded copy refreshes itself every 12 hours; a checkout needs `git pull`.

**The first command after an update takes several seconds**
Cause: the search index is rebuilt when the data changes. It is cached in `~/.cache/iceberg-context/`; later commands are fast.

**`no results`**
Search requires every word, then falls back to any word. Use fewer or more specific words, drop `--type`, or put an exact
phrase in double quotes. Mailing-list history goes back to 2018; summaries cover roughly the last six months.

**`no history found for PATH`**
Paths are relative to the upstream repository root. A bare file name (`SnapshotProducer.java`) or a directory (`core/`) also works.

**A pull request shows "details not synced yet", or reviewers are missing**
Pull-request history is collected in bounded batches. Run `kb status`: the `github` line says whether the backfill is complete.

**`kb status` shows a source as `failed` or days old**
Tell the user which source is stale and when it last succeeded, and treat answers that depend on it as possibly out of date.
`youtube` is often behind: recordings cannot always be fetched from cloud machines.

**`SyntaxError` or `unsupported operand type(s) for |`**
Cause: Python older than 3.10. Fix: run the script with a newer `python3`.

## What is in the repository

- `kb/state-of-iceberg.md`: current overview. `kb/opportunities.md`: where to contribute. `kb/briefings/weekly/`: what changed each week.
- `kb/people/`, `kb/groups/`, `kb/initiatives/`, `kb/modules/`, `kb/releases/`: one page per entity, linked to each other.
- `kb/records/`: one page per meeting and per mailing-list thread.
- `data/raw/`: cleaned source text, one JSON line per email, pull request, meeting section or transcript.
- `research/`: how each source was studied. `references/process.md` in this skill: how Iceberg makes decisions.

## Rules about people

Describe public project activity only: roles, reviews, votes, proposals, talks. Do not add personal details or guesses about
motives. The people described can read this repository.
