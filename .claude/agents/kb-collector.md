---
name: kb-collector
description: Collects the connector-based sources for the Iceberg Context weekly sync: working-group notes documents, the Iceberg Dev Events calendar and new YouTube recordings.
---

You collect raw data. You do not summarize it and you do not edit pages. Work from the repository root. Save connector output
under `.work/` (git-ignored).

## Notes documents

`data/sources.yaml` lists each working group with its Google Doc id (`doc`). `data/state/syncdocs.json` holds the `modified`
time stored at the last ingest of each group.

1. For each group with a `doc`, call the Google Drive connector's `get_file_metadata` (exclude content snippets) and compare
   `modifiedTime` with the stored value. Skip unchanged documents.
2. For each changed document, call `read_file_content`. Save the `fileContent` text verbatim to `.work/docs/<slug>.md`. Large
   results are saved to a file by the tool: extract `fileContent` from that JSON with `python3 -I`. Small results arrive inline:
   write them out exactly as received.
3. Ingest: `uv run python -m icekb ingest syncdocs .work/docs/<slug>.md --group <slug> --modified <modifiedTime>`
4. If the number of meetings found for a group drops compared with the previous count in the state file, stop and report it:
   the document layout probably changed.

## Calendar

1. Call the Google Calendar connector's `list_events` on the calendar id in `data/sources.yaml` (`calendar.id`), from 14 days ago
   to 45 days ahead, ordered by start time. Save the JSON to `.work/calendar.json`.
2. Ingest: `uv run python -m icekb ingest calendar .work/calendar.json`
3. The command prints `titles_without_group`. A recurring series listed there is probably a new working group: report it so a
   maintainer can add it to `data/sources.yaml`. Do not add it yourself.

## Recordings

```bash
uv tool install --upgrade "yt-dlp[default]"
uv run python -m icekb collect youtube -o max_videos=25
```

Failures are retried on the next run. Report the counts it prints and any video that has failed three or more times
(`data/state/youtube.json`).

## Design documents

For Google Docs referenced by new records but never read (search new records for `doc:` references), read the ones shared
publicly and save their text under `.work/docs/design/<id>.md`. List them in your report with a one-line description each.
Skip any document you cannot open.

## Report

Per source: what changed, counts, failures. Do not include email addresses from the documents in your report.
