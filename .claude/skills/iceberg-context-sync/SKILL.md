---
name: iceberg-context-sync
description: Maintainer runbook for the weekly sync of the Iceberg Context knowledge base. Use it when asked to "sync now", "run the weekly sync" or "update the knowledge base", and in the scheduled weekly session. Collects meeting notes, the calendar and recording transcripts, summarizes what is new, updates the pages and writes the weekly briefing.
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
python3 .claude/skills/iceberg-context/scripts/kb status
```

## 1. Collect (agent: `kb-collector`)

Start one `kb-collector` agent and wait for it. It fetches the notes documents, the calendar and new recordings, and reports
what changed. It needs the Google Drive and Google Calendar connectors; if they are missing it reports that and does the rest.

## 2. Summarize what is new

```bash
uv run python -m icekb queue meetings --since <14 days ago>
uv run python -m icekb queue threads --since <14 days ago>
```

Each command prints the items that need extraction and writes an input bundle per item under `.work/queue/`. Start
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
update `initiatives/`, `state-of-iceberg.md` and `opportunities.md` from the new records.

## 4. Verify (agent: `kb-verifier`)

Start one `kb-verifier` agent. It did not write the pages, and it gets no summary from you: only the list of files changed in
this run (`git status --short`). Apply the fixes it reports, or remove the claim it could not confirm.

## 5. Brief (agent: `kb-briefer`)

Start one `kb-briefer` agent to write `briefings/weekly/<ISO year>-W<week>.md`.

## 6. Check, commit, push

```bash
uv run python -m icekb index && uv run python -m icekb validate && uv run pytest -q
git add -A && git commit -m "sync(kb): <ISO year>-W<week>"
git pull --rebase origin main && git push origin HEAD:main
```

Commit messages carry no AI attribution lines (see `CLAUDE.md`). If the push to `main` is refused, push to `sync/weekly`
and say so in the summary.

## 7. Summarize

End with a short summary: what was collected, how many meetings and threads were summarized, pages changed, anything that
failed or is stale, and the three most important things that happened in the community this week.
