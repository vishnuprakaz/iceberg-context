---
id: thread/t-9704aed6923e08fc
type: thread
title: Vote on adding table constraints to the v4 table spec
date: '2026-10-22'
url: https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r
kind: vote
status: passed
messages: 11
sources:
- devlist:cv1ks4gcvqpy3jmm8x00hxxyjz776d8r
refs:
- gh:apache/iceberg#17822
links:
- rel: discussed
  to: initiative/constraints
  confidence: extracted
  source: devlist:cv1ks4gcvqpy3jmm8x00hxxyjz776d8r
- rel: started_by
  to: person/huaxingao
  confidence: observed
updated: '2026-11-13'
---

# Vote on adding table constraints to the v4 table spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add table constraints to the v4 table spec](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r) · **Started:** 2026-10-22 by [[person/huaxingao|Huaxin Gao]] · **Messages:** 11 (last 2026-10-27) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Huaxin started a vote on adding table constraints to the Iceberg v4 table spec through PR #17822. The change adds three constraint types: `check`, `unique` and `primary-key`. Definitions are stored in table metadata with an `enforced` flag that controls whether writers must verify the rows they add or modify. Each snapshot records the status of every constraint in `constraint-statuses` as `validated`, `valid`, `invalid` or `unvalidated`. A `primary-key` constraint replaces identifier field IDs in v4; on upgrade, identifier fields become a primary-key constraint that is not enforced. Voters left minor wording comments. Ryan Blue voted +1 while noting small issues, including type promotion for fields referenced by a check constraint, and Huaxin said the comments were addressed in the PR. The vote passed, with the PR to be merged the following day.

**Why it matters:** The v4 spec gains check, unique and primary-key constraints, and primary-key constraints replace identifier field IDs in v4 tables.

## Outcome

Passed with 8 +1 votes, 5 of them binding, and no -1 or +0 votes. ([message](https://lists.apache.org/thread/k1zo93v0zq8f783hnswt1n29g5clzqyd), `devlist:k1zo93v0zq8f783hnswt1n29g5clzqyd`)

## Positions

- **[[person/rdblue|Ryan Blue]]:** Votes +1 overall; some edits for clarity and minor issues, such as type promotion of fields referenced by a check constraint, should be fixed but should not prevent the vote from passing. ([message](https://lists.apache.org/thread/j4yy5jpvyy0tvxtfyth1ofh842m3vp5y))
- **[[person/huaxingao|Huaxin Gao]]:** Addressed the review comments in the PR, including allowing type promotion for fields referenced by a check constraint. ([message](https://lists.apache.org/thread/7hoj4k2stvsg6gjywbcdyyqfdkv4tnjc))

References: [iceberg#17822](https://github.com/apache/iceberg/issues/17822)
<!-- kb:generated:end -->

## Notes
