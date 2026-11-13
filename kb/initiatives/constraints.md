---
id: initiative/constraints
type: initiative
title: Table constraints
status: accepted
updated: '2026-11-13'
sources:
- meeting/community/2026-05-13
- meeting/constraints/2026-06-04
- meeting/constraints/2026-06-18
- thread/t-003a5548469ee105
- meeting/file-vector-type/2026-10-08
- meeting/file-vector-type/2026-10-22
- thread/t-9704aed6923e08fc
links:
- rel: championed_by
  to: person/huaxingao
  confidence: extracted
  source: thread/t-9704aed6923e08fc
- rel: handled_by
  to: group/constraints
  confidence: extracted
  source: meeting/constraints/2026-06-04
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-9704aed6923e08fc
- rel: tracked_in
  to: gh:apache/iceberg#17822
  confidence: extracted
  source: thread/t-9704aed6923e08fc
---

# Table constraints

<!-- kb:generated:start -->
## What it is

Table constraints add `check`, `unique` and `primary-key` constraints to the V4 table spec ([thread summary](../records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md), [dev list](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r)). Definitions live in table metadata with an `enforced` flag that says whether writers must verify the rows they add or change, and each snapshot records the status of every constraint ([thread summary](../records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md), [dev list](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r)). In V4 a `primary-key` constraint replaces identifier field IDs; on upgrade, identifier fields become a primary-key constraint that is not enforced ([thread summary](../records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md), [dev list](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r)).

## Current state

- The vote on adding constraints to the V4 spec through [#17822](https://github.com/apache/iceberg/pull/17822) passed with 8 +1 votes, 5 of them binding ([thread summary](../records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md), [dev list](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r)); the pull request was merged on 2026-10-28 ([#17822](https://github.com/apache/iceberg/pull/17822)).
- No record yet covers implementation work in any language (inferred from the absence of such records).
- A proposal for first-class primary-key tables (write, compaction and changelog semantics for CDC) was pointed to the constraints proposal; its author sees it as complementary, and nothing was decided ([thread summary](../records/threads/2026/06/discuss-first-class-primary-key-tables-in-apache-iceberg-003a55.md), [dev list](https://lists.apache.org/thread/o7tzt04by73l0hpjd58t2wgvl4ct9lrc)).
- The vector type discussion plans to use check constraints to enforce properties such as normalized vectors ([file-vector-type sync 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md)), and noted that check constraints may need to revisit how defaults that violate a constraint are handled ([file-vector-type sync 2026-10-22](../records/meetings/file-vector-type/2026/2026-10-22.md)).

## Timeline

- 2026-05-13: Huaxin Gao brings the constraint support proposal to the community sync ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md)).
- 2026-06-04 and 2026-06-18: Constraints syncs are held; the notes contain only links to recordings ([constraints sync 2026-06-04](../records/meetings/constraints/2026/2026-06-04.md); [constraints sync 2026-06-18](../records/meetings/constraints/2026/2026-06-18.md)).
- 2026-06-20: Thread on first-class primary key tables is redirected to the constraints proposal ([thread summary](../records/threads/2026/06/discuss-first-class-primary-key-tables-in-apache-iceberg-003a55.md), [dev list](https://lists.apache.org/thread/o7tzt04by73l0hpjd58t2wgvl4ct9lrc)).
- 2026-10-22: Vote on adding table constraints to the V4 spec opens; it passed ([thread summary](../records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md), [dev list](https://lists.apache.org/thread/cv1ks4gcvqpy3jmm8x00hxxyjz776d8r)).
- 2026-10-28: The constraints spec pull request is merged ([#17822](https://github.com/apache/iceberg/pull/17822)).
<!-- kb:generated:end -->

## Notes
