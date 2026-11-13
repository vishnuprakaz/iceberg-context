---
id: initiative/v4-row-lineage-timestamps
type: initiative
title: V4 row timestamps and monotonic snapshot timestamps
status: vote
updated: '2026-11-13'
sources:
- meeting/v4-metadata/2026-06-01
- meeting/v4-metadata/2026-09-21
- thread/t-94521177da7f4309
- meeting/column-updates/2026-10-20
- meeting/community/2026-10-28
- thread/t-447ec59251977712
links:
- rel: championed_by
  to: person/stevenzwu
  confidence: extracted
  source: thread/t-447ec59251977712
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-09-21
- rel: handled_by
  to: group/column-updates
  confidence: extracted
  source: meeting/column-updates/2026-10-20
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-447ec59251977712
- rel: tracked_in
  to: gh:apache/iceberg#18526
  confidence: extracted
  source: thread/t-447ec59251977712
- rel: tracked_in
  to: gh:apache/iceberg#16294
  confidence: extracted
  source: thread/t-94521177da7f4309
---

# V4 row timestamps and monotonic snapshot timestamps

<!-- kb:generated:start -->
## What it is

Two linked changes to the V4 table spec. The first requires every new snapshot in a V4 table to have a timestamp strictly greater than its parent's on the same branch, so that snapshot timestamps follow snapshot order ([thread 2026-10-07](../records/threads/2026/10/vote-require-monotonically-increasing-snapshot-timestamps-in-v4-945211.md), [dev list](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm)). The second builds on it and adds a reserved `_last_updated_time` metadata column to row lineage, which records the timestamp of the snapshot that last updated a row ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).

## Current state

- Decided: V4 requires monotonically increasing snapshot timestamps per branch; root snapshots are unconstrained and v1 to v3 behaviour is unchanged. The vote passed with 9 binding and 11 non-binding +1 votes, on spec pull request [#16294](https://github.com/apache/iceberg/pull/16294) with reference implementation [#16293](https://github.com/apache/iceberg/pull/16293) ([thread 2026-10-07](../records/threads/2026/10/vote-require-monotonically-increasing-snapshot-timestamps-in-v4-945211.md), [dev list](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm)).
- In vote, no result recorded: `_last_updated_time` (a `timestamptz` column) and an optional `snapshot_timestamp` tracking field in V4 manifests, in spec pull request [#18526](https://github.com/apache/iceberg/pull/18526). The thread shows five binding and seven non-binding +1 votes and no -1, but no result message; the last message, from Ryan Blue, says the change is close but needs more editing before it is ready ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).
- Open: Dan Weeks voted +1 but said the column type should be `timestamp` rather than `timestamptz`, which he did not consider blocking ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).
- Open: a voter asked the community to consider extending `timestamp-ms` to nanosecond precision to allow more transaction throughput ([thread 2026-10-07](../records/threads/2026/10/vote-require-monotonically-increasing-snapshot-timestamps-in-v4-945211.md), [dev list](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm)).
- Decided in the V4 metadata sync: root manifest entries inherit only the update time from snapshot metadata, not the snapshot ID, sequence number or other fields ([V4 metadata sync 2026-09-21](../records/meetings/v4-metadata/2026/2026-09-21.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).

## Timeline

- 2026-06-01: row lineage for column files was an agenda item at the V4 metadata sync; no outcome is recorded ([V4 metadata sync 2026-06-01](../records/meetings/v4-metadata/2026/2026-06-01.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- 2026-09-21: the V4 metadata sync recorded that root manifest entries inherit only the update time from the snapshot ([V4 metadata sync 2026-09-21](../records/meetings/v4-metadata/2026/2026-09-21.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- 2026-10-07: Steven Wu called the vote on monotonically increasing snapshot timestamps in V4 ([thread 2026-10-07](../records/threads/2026/10/vote-require-monotonically-increasing-snapshot-timestamps-in-v4-945211.md), [dev list](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm)).
- 2026-10-12: the vote passed with 9 binding and 11 non-binding +1 votes; the spec pull request [#16294](https://github.com/apache/iceberg/pull/16294) was to be merged ([result](https://lists.apache.org/thread/4fp65bnrh7k6x98yl2wgl931301jg25o), `devlist:4fp65bnrh7k6x98yl2wgl931301jg25o`; [thread 2026-10-07](../records/threads/2026/10/vote-require-monotonically-increasing-snapshot-timestamps-in-v4-945211.md), [dev list](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm)).
- 2026-10-20: row timestamp was listed as a topic at the column updates sync, with no detail recorded ([column updates sync 2026-10-20](../records/meetings/column-updates/2026/2026-10-20.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- 2026-10-28: at the community sync's V4 progress report, Steven Wu was said to have the row timestamp spec pull request and to plan the vote that week ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-30: Steven Wu called a 72-hour vote on `_last_updated_time` ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).
- 2026-11-03: last message in the vote thread; no result had been announced ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).

## Where help is needed

- The `_last_updated_time` spec pull request [#18526](https://github.com/apache/iceberg/pull/18526) was described in the vote thread as needing more editing before it is ready, and the `timestamp` versus `timestamptz` question was raised there ([thread 2026-10-30](../records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md), [dev list](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv)).
<!-- kb:generated:end -->

## Notes
