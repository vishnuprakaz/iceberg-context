---
id: initiative/v4-metadata-tree
type: initiative
title: V4 adaptive metadata tree and single-file commits
status: implementing
updated: '2026-11-13'
sources:
- thread/t-9da84e6ec274a52c
- meeting/v4-metadata/2026-05-18
- thread/t-ec167869ed1e0e08
- meeting/v4-metadata/2026-06-15
- thread/t-6b556fb65dd1775f
- meeting/column-updates/2026-07-28
- meeting/v4-metadata/2026-08-10
- meeting/column-updates/2026-08-11
- thread/t-5c70639b9c0f57ff
- thread/t-bd70f40d4eb1876d
- meeting/v4-metadata/2026-08-24
- meeting/v4-metadata/2026-09-21
- meeting/v4-metadata/2026-10-05
- thread/t-31c8012d43fc214e
- meeting/community/2026-10-28
links:
- rel: championed_by
  to: person/amogh-jahagirdar
  confidence: extracted
  source: thread/t-31c8012d43fc214e
- rel: championed_by
  to: person/stevenzwu
  confidence: extracted
  source: meeting/v4-metadata/2026-06-15
- rel: championed_by
  to: person/rdblue
  confidence: extracted
  source: thread/t-9da84e6ec274a52c
- rel: championed_by
  to: person/anoopj
  confidence: extracted
  source: meeting/v4-metadata/2026-08-10
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-06-15
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-31c8012d43fc214e
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/v4-metadata/2026-06-15
- rel: tracked_in
  to: gh:apache/iceberg#16025
  confidence: extracted
  source: thread/t-31c8012d43fc214e
---

# V4 adaptive metadata tree and single-file commits

<!-- kb:generated:start -->
## What it is

Format version 4 replaces the manifest list with a root manifest at the top of an "adaptive metadata tree" (AMT): a snapshot points at a root manifest, which points at leaf data and delete manifests ([v4-metadata sync 2026-06-15](../records/meetings/v4-metadata/2026/2026-06-15.md)). The root manifest can carry manifest deletion vectors, and later direct data-file entries, so that small changes do not require rewriting leaf manifests ([v4-metadata sync 2026-06-15](../records/meetings/v4-metadata/2026/2026-06-15.md); [thread summary](../records/threads/2026/04/discuss-compact-bitmap-format-9da84e.md), [dev list](https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f)). Entries in the tree are "tracked files" that can also carry deletion vectors and column files ([thread summary](../records/threads/2026/05/discuss-column-update-metadata-representation-ec1678.md), [dev list](https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg)).

## Current state

- The baseline AMT spec pull request [#16025](https://github.com/apache/iceberg/pull/16025) was voted on as a vote to merge, not a vote for adoption; encryption, column file requirements and dropping the partition tuple are left to follow-up changes ([thread summary](../records/threads/2026/10/vote-merge-baseline-v4-amt-spec-pr-into-main-repo-31c801.md), [dev list](https://lists.apache.org/thread/qch7jjnwb8pm49lt3h7lqfxj82hlg8ps)).
- The 28 October community sync lists the AMT entry structures ([#16025](https://github.com/apache/iceberg/pull/16025)), the file planner ([#17541](https://github.com/apache/iceberg/pull/17541)), write-direction wrappers ([#16936](https://github.com/apache/iceberg/pull/16936)), a mutable bitmap ([#18544](https://github.com/apache/iceberg/pull/18544)) and dropping `equality_ids` from the V4 TrackedFile ([#18427](https://github.com/apache/iceberg/pull/18427)) as merged ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- New or rewritten V4 manifests must be Parquet; upgraded tables can keep their existing Avro manifests ([thread summary](../records/threads/2026/08/discuss-should-v4-manifests-be-parquet-only-5c7063.md), [dev list](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y)).
- Upgrades stay cheap: V4 readers handle older manifests, and moving metadata to the V4 structures is an implementation choice that needs no spec work ([thread summary](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky); [column-updates sync 2026-07-28](../records/meetings/column-updates/2026/2026-07-28.md)).
- The partition tuple is to be removed in V4 and replaced by `content_stats`; it is kept temporarily so parameterized tests do not break ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)).
- Root manifest entries inherit only the update time from the snapshot ([v4-metadata sync 2026-09-21](../records/meetings/v4-metadata/2026/2026-09-21.md)).
- Open: whether `dv_snapshot_id` and `column_file_snapshot_id` are consolidated into one `modified_snapshot_id` ([v4-metadata sync 2026-10-05](../records/meetings/v4-metadata/2026/2026-10-05.md)); which format manifest deletion vectors use, Mumbling or Roaring ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md); the Mumbling draft spec in [#16518](https://github.com/apache/iceberg/pull/16518) is for coordination only, [thread summary](../records/threads/2026/04/discuss-compact-bitmap-format-9da84e.md), [dev list](https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f)); whether data files still need `spec_id` ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)); whether `fileSizeInBytes` is persisted for the root manifest ([v4-metadata sync 2026-09-21](../records/meetings/v4-metadata/2026/2026-09-21.md)); and the shape of a V4 `UpdateFiles` write interface ([v4-metadata sync 2026-08-24](../records/meetings/v4-metadata/2026/2026-08-24.md)).

## Timeline

- 2026-04-20: Ryan Blue proposes the compact "Mumbling" bitmap format for manifest deletion vectors in the root manifest ([thread summary](../records/threads/2026/04/discuss-compact-bitmap-format-9da84e.md), [dev list](https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f)).
- 2026-05-18: The sync concludes that a DV or column update change marks the old entry REPLACED and the changed entry MODIFIED, and that the two need not be in the same manifest ([v4-metadata sync 2026-05-18](../records/meetings/v4-metadata/2026/2026-05-18.md)).
- 2026-06-15: Steven Wu presents implementation milestone 1: a fixed two-level tree with copy-on-write leaf rewrites, aiming at parity with V3 commit and scan paths ([v4-metadata sync 2026-06-15](../records/meetings/v4-metadata/2026/2026-06-15.md)).
- 2026-07-20: Thread on reading small Parquet manifests in one request; agreed to do eager reads in the Parquet file reader, not in the manifest reader or FileIO ([thread summary](../records/threads/2026/07/discuss-integrate-eagerinputfile-into-the-manifest-reader-6b556f.md), [dev list](https://lists.apache.org/thread/qhn00762nrxl1zmb817wqqq5tzlqolbq)).
- 2026-07-28: Consensus on gradual, on-demand V3 to V4 migration: V4 tables reference legacy manifests and entries are promoted to V4 when modified ([column-updates sync 2026-07-28](../records/meetings/column-updates/2026/2026-07-28.md)).
- 2026-08-10: Decision to remove the partition tuple in V4 and replace it with `content_stats` ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)).
- 2026-08-11: The column updates sync decides V4 manifests are Parquet-only, subject to dev list feedback; the dev list thread starts the same day and ends in consensus ([column-updates sync 2026-08-11](../records/meetings/column-updates/2026/2026-08-11.md); [thread summary](../records/threads/2026/08/discuss-should-v4-manifests-be-parquet-only-5c7063.md), [dev list](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y)).
- 2026-08-12: Thread on V3 to V4 upgrade expectations ends in consensus that upgrades stay cheap ([thread summary](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky)).
- 2026-09-21: Root manifest entries inherit only the update time from the snapshot ([v4-metadata sync 2026-09-21](../records/meetings/v4-metadata/2026/2026-09-21.md)).
- 2026-10-09: Amogh Jahagirdar opens the vote to merge the baseline AMT spec pull request [#16025](https://github.com/apache/iceberg/pull/16025); it passed with 18 +1 votes, 9 of them binding ([thread summary](../records/threads/2026/10/vote-merge-baseline-v4-amt-spec-pr-into-main-repo-31c801.md), [dev list](https://lists.apache.org/thread/qch7jjnwb8pm49lt3h7lqfxj82hlg8ps)).
- 2026-10-28: The community sync lists the AMT entry structures and further V4 core work as merged ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Where help is needed

- Open design questions the group has put on the sync agenda without a recorded answer: consolidating the two snapshot ID fields ([v4-metadata sync 2026-10-05](../records/meetings/v4-metadata/2026/2026-10-05.md)) and whether the new `UpdateFiles` interface should also cover `OverwriteFiles` ([v4-metadata sync 2026-08-24](../records/meetings/v4-metadata/2026/2026-08-24.md)).
<!-- kb:generated:end -->

## Notes
