---
id: initiative/v4-relative-paths
type: initiative
title: V4 relative paths
status: implementing
updated: '2026-11-13'
sources:
- thread/t-01f21da0dbe27e4f
- meeting/community/2026-05-13
- thread/t-214dc89c07f6f226
- thread/t-fa11fb73f2aa07a0
- meeting/community/2026-06-03
- thread/t-4fdcd748e0704aa5
- meeting/community/2026-08-26
- meeting/catalog/2026-10-14
links:
- rel: championed_by
  to: person/danielcweeks
  confidence: extracted
  source: thread/t-214dc89c07f6f226
- rel: championed_by
  to: person/talatuyarer
  confidence: extracted
  source: thread/t-01f21da0dbe27e4f
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-214dc89c07f6f226
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/community/2026-08-26
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
- rel: tracked_in
  to: gh:apache/iceberg#15630
  confidence: extracted
  source: thread/t-214dc89c07f6f226
- rel: tracked_in
  to: gh:apache/iceberg#13141
  confidence: extracted
  source: thread/t-01f21da0dbe27e4f
---

# V4 relative paths

<!-- kb:generated:start -->
## What it is

A V4 table spec change that lets the paths stored in table metadata be relative to the table location instead of absolute ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)). Supporters called it useful for disaster recovery ([thread, 2026-05-19](../records/threads/2026/05/vote-spec-addition-of-relative-paths-to-v4-214dc8.md); [dev list](https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n)). Keeping several locations for the same files under one table is explicitly a non-goal, and absolute paths remain available ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).

## Current state

- The vote to add relative paths to the v4 spec, as defined in [#15630](https://github.com/apache/iceberg/pull/15630), passed with 7 binding and 12 non-binding +1 votes; the vote confirms the direction and changes can still happen until the v4 spec is finalized ([thread, 2026-05-19](../records/threads/2026/05/vote-spec-addition-of-relative-paths-to-v4-214dc8.md); [dev list](https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n)).
- The relative paths spec change is listed as merged ([Community Sync, 2026-06-03](../records/meetings/community/2026/2026-06-03.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- The design joins the table location and the relative path on the '/' separator ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- Java work listed as merged: v4 location relativization utilities and an optional v4 table metadata location ([Community Sync, 2026-06-03](../records/meetings/community/2026/2026-06-03.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and relative path resolution in the V4 manifest reader ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- With relative paths, changing a table's location breaks reads and cleanup of files written under the old location; relocating data is treated as the responsibility of the catalog or implementation ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- REST catalog: a table-location field in load, commit and unregister responses was proposed to allow relative paths; participants converged on in-place model changes plus a v2 loadTable endpoint for V4 tables, with [#17642](https://github.com/apache/iceberg/pull/17642) open for feedback and a rest-v4-changes branch collecting the changes ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)). At the catalog sync it was said that the pull request adding the new endpoint already covers relative paths ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- RewriteTablePaths, its issues with V4 and its deprecation were listed for discussion at the community sync; no outcome is recorded ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Timeline

- 2025-05-27: Proposal thread for relative path support in the table spec starts (issue [#13141](https://github.com/apache/iceberg/pull/13141) and a design document) ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- 2025-07: A dedicated sync is held ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- 2026-01: A meeting reaches general agreement on the approach ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- 2026-05: The design changes to joining the table location and relative path on the '/' separator, ahead of a vote ([thread, 2025-05-27](../records/threads/2025/05/discuss-proposal-for-relative-path-support-in-table-spec-01f21d.md); [dev list](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2)).
- 2026-05-13: The spec pull request [#15630](https://github.com/apache/iceberg/pull/15630) is listed for discussion at the community sync ([Community Sync, 2026-05-13](../records/meetings/community/2026/2026-05-13.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-05-19: Vote on adding relative paths to the v4 spec starts; it is later closed as passed with 7 binding and 12 non-binding +1 votes ([thread, 2026-05-19](../records/threads/2026/05/vote-spec-addition-of-relative-paths-to-v4-214dc8.md); [dev list](https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n)). Further +1 replies to the same vote are in a second record ([thread, 2026-05-20](../records/threads/2026/05/vote-spec-addition-of-relative-paths-to-v4-fa11fb.md); [dev list](https://lists.apache.org/thread/wtntmmsmnxscfb8w1hr4slvmt2r8ghn5)).
- 2026-06-03: The spec change and the v4 location relativization utilities are listed as merged ([Community Sync, 2026-06-03](../records/meetings/community/2026/2026-06-03.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-13: Thread on the initial REST catalog changes for V4 starts, including table-location in responses ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
- 2026-08-26: Relative path resolution in the V4 manifest reader is listed as merged ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-14: Catalog sync: the V2 load table pull request is said to already cover relative paths ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).

## Where help is needed

- The REST catalog change for V4, which carries the table-location field, is open for feedback in [#17642](https://github.com/apache/iceberg/pull/17642) ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
<!-- kb:generated:end -->

## Notes
