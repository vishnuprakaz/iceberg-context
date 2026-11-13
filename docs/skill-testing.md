# Testing the skills

Follows the three kinds of test in Anthropic's guide to building skills: triggering, function, and comparison with no skill.

## 1. Triggering

Run these in a fresh Claude Code session that has this repository attached, without naming the skill. Record whether the
`iceberg-context` skill loads on its own.

Should trigger:

1. Why does `SnapshotProducer` validate that snapshot timestamps increase?
2. What's the history behind `pyiceberg/table/update/snapshot.py`?
3. What is the Iceberg community working on for v4 right now?
4. Where are materialized views at? Did the spec vote happen?
5. Who usually reviews Flink changes in Iceberg?
6. I'm about to change the REST catalog client's auth handling. Anything I should know first?
7. What happened on the Iceberg dev list this week?
8. When is the next catalog sync and what's on the agenda?
9. I know Python and want to start contributing to Iceberg. What could I pick up?
10. Has anyone already proposed a vector type for Iceberg?
11. Who is the release manager for Iceberg 1.13?
12. What did the index working group decide about derived columns?

Should not trigger:

1. How do I create a partitioned Iceberg table in Spark SQL?
2. What does `write.target-file-size-bytes` do?
3. Write a Python function that merges two sorted lists.
4. Explain how Parquet row groups work.
5. Fix the failing unit test in this repository. (No link to Iceberg history or community.)

Should trigger `iceberg-context-sync` instead: "sync the knowledge base now", "run the weekly sync", "write this week's briefing".

Target: the skill loads for at least 11 of the 12 positive cases and none of the negative ones. If it under-triggers, add the
missing phrasing to the `description` in `SKILL.md`; if it over-triggers, sharpen the "Do not use for" sentence.

## 2. Function

Automated, in CI (`uv run pytest`):

- `tests/test_kb.py`: `status`, `search`, `source` and index rebuilding against a small fixture knowledge base.
- `tests/test_skills.py`: the guide's structural checklist (names, frontmatter, description length and triggers, no angle
  brackets, linked references exist, `kb` uses only the standard library).
- `tests/test_collectors.py`, `tests/test_ingest.py`, `tests/test_pipeline.py`: the data the commands read.

Manual, against the real data, after each weekly sync:

| Check | Command | Passes when |
|---|---|---|
| Freshness | `kb status` | Every source except `youtube` shows `ok` and less than 8 days old |
| Code to discussion | `kb why core/src/main/java/org/apache/iceberg/SnapshotProducer.java` | Lists pull requests with reviewers and at least one linked thread or meeting |
| Initiative | `kb initiative v4-metadata-tree` | Shows the October 2026 baseline vote with a working link |
| Proof | `kb source ID` for an id from the output above | Prints text that supports the claim, and a URL that opens |
| People | `kb who-to-ask flink/` | Names authors and reviewers with counts |
| Upcoming | `kb upcoming` | Lists meetings in the next 14 days |
| Opportunities | `kb opportunities --area python --level starter` | Returns at least one entry with evidence links |

## 3. Comparison

Ask the same question with and without the skill, and compare. Suggested question: "What is the status of materialized views
in Iceberg and who should I talk to about helping?"

| | Without the skill | With the skill |
|---|---|---|
| Sources cited | | |
| Tool calls | | |
| Names a working group and its next meeting | | |
| Anything stated that the sources do not support | | |

Record results here after each change to `SKILL.md`.

| Date | Skill version | Triggering (positive / negative) | Function | Notes |
|---|---|---|---|---|
| 2026-11-13 | 0.1.0 | not yet run in a fresh session | automated tests pass; manual checks pass except `youtube` freshness | First build |
