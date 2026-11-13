---
name: iceberg-context-sync
description: Maintainer runbook that refreshes the Iceberg Context knowledge base. Use when the user says "sync now", "run the weekly sync", "update the knowledge base", "refresh iceberg context" or "write this week's briefing", and in the scheduled weekly session. Collects working-group meeting notes, the community calendar and recording transcripts, summarizes new meetings and mailing-list threads, updates the pages, verifies them and writes the weekly briefing. Not for answering questions about Iceberg; use the iceberg-context skill for that.
license: Apache-2.0
compatibility: Claude Code with subagents, run from a checkout of the iceberg-context repository with push access. Needs uv, git and network access, and the Google Drive and Google Calendar connectors for meeting notes and the calendar.
metadata:
  author: Iceberg Context contributors
  version: 0.1.0
  repository: https://github.com/vishnuprakaz/iceberg-context
---

# Weekly sync runbook

Run from the root of the `iceberg-context` repository. The daily GitHub Action already collects the dev list, GitHub activity,
git history, the spec and the ASF roster; this runbook covers what needs Claude connectors and judgment.

Work through the steps in order. If a step fails, record it in the final summary and carry on: a partial sync is better than none.
Never mark something as synced when it failed.

## 0. Prepare

```bash
git pull --rebase origin main
uv sync
python3 skills/iceberg-context/scripts/kb status
```

## 1. Collect (agent: `kb-collector`)

Start one `kb-collector` agent and wait for it. It fetches the notes documents, the calendar and new recordings, and reports
what changed. It needs the Google Drive and Google Calendar connectors; if they are missing it reports that and does the rest.

## 2. Summarize what is new

```bash
uv run python -m icekb queue meetings --since DATE
uv run python -m icekb queue threads --since DATE
```

`DATE` is the day 14 days before today, as `YYYY-MM-DD`. Each command prints the items that need extraction and writes an input bundle per item under `.work/queue/`. Start
`kb-meeting-extractor` agents (at most 3 meetings with transcripts per agent) and `kb-thread-extractor` agents (about 20 threads
per agent) in parallel, giving each its list of bundle paths. Then:

```bash
uv run python -m icekb apply
```

Every extraction must be accepted. Send rejected ones back to an extractor with the reason, or delete the JSON file if it cannot
be fixed, and say so in the summary.

## 3. Integrate (agent: `kb-integrator`)

```bash
uv run python -m icekb integrate
```

This regenerates the people, group, module, repository and release pages from data. Then start one `kb-integrator` agent to
update `kb/initiatives/`, `kb/state-of-iceberg.md` and `kb/opportunities.md` from the new records.

## 4. Verify (agent: `kb-verifier`)

Start one `kb-verifier` agent. It did not write the pages, and it gets no summary from you: only the list of files changed in
this run (`git status --short`). Apply the fixes it reports, or remove the claim it could not confirm.

## 5. Brief (agent: `kb-briefer`)

Start one `kb-briefer` agent to write `kb/briefings/weekly/YYYY-Www.md` (ISO year and week, for example `2026-W46.md`).

## 6. Check, commit, push

```bash
uv run python -m icekb index && uv run python -m icekb validate && uv run pytest -q
git add -A && git commit -m "sync(kb): YYYY-Www"
git pull --rebase origin main && git push origin HEAD:main
```

Commit messages carry no AI attribution lines (see `CLAUDE.md`). If the push to `main` is refused, push to `sync/weekly`
and say so in the summary.

## 7. Summarize

End with a short summary: what was collected, how many meetings and threads were summarized, pages changed, anything that
failed or is stale, and the three most important things that happened in the community this week.

## Troubleshooting

**Google Drive or Calendar tools are not available**
Cause: the session has no connector (scheduled sessions only have the connectors attached to the scheduled task). Do steps 2
to 7 with what the daily Action collected, and report that notes and calendar were skipped.

**`Sign in to confirm you're not a bot` from the recordings collector**
Cause: YouTube challenges cloud addresses. The collector records the failure and retries next run. Do not try other clients or
cookies. Captions fetched on a personal machine can be added with
`uv run python -m icekb ingest transcript VIDEO.info.json --captions VIDEO.en-orig.json3`.

**`icekb apply` rejects an extraction**
"unknown source" or "not in this thread": the extraction cites an id that is not in its input bundle; correct the id.
"quote … does not match the transcript": the words or the timestamp are wrong; copy the passage exactly or remove the quote.

**The meeting count for a notes document drops**
Cause: the document layout changed (headings, tabs). Stop ingesting that group, keep the old records, and report it. Fix the
parser in `pipeline/icekb/ingest/syncdocs.py` with a test before re-ingesting.

**`git push` is refused**
Push to `sync/weekly` instead and say so in the summary. Never force-push `main`.

**`icekb validate` reports a privacy problem**
An email address reached a file. Find where it came from and remove it at the source (the cleaning step), not only in the page.
