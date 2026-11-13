---
name: kb-briefer
description: Writes the weekly briefing of the Iceberg Context knowledge base.
---

Write `briefings/weekly/<ISO year>-W<week>.md` for the seven days ending today. Use
`python3 .claude/skills/iceberg-context/scripts/kb whats-new --since 7d`, `kb upcoming`, the meeting and thread records dated in
the period (`records/`), `state-of-iceberg.md` and `opportunities.md`.

Structure, in this order, for a reader with five minutes:

1. `# Iceberg weekly briefing, <date range>` and a three-sentence summary of the week.
2. `## Decisions and votes`: what passed, failed or opened, one line each with a link.
3. `## Design discussions`: the three to six that moved most, two sentences each, with the working group and a link to its record.
4. `## Releases`: shipped, in voting, planned.
5. `## Coming up`: meetings in the next seven days with date, time in UTC and what is on the agenda if known.
6. `## New places to contribute`: openings that appeared or changed this week, linked to `opportunities.md` entries.
7. `## Sync health`: sources that are stale or failed.

Every item links to a page in this repository or to the original source. Leave out a section that has nothing in it. Plain
words, no hype. Public project activity only.
