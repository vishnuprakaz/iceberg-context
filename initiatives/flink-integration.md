---
id: initiative/flink-integration
type: initiative
title: Flink integration and table maintenance
status: implementing
updated: '2026-11-13'
sources:
- thread/t-ce325e60255c54b1
- thread/t-95092e2c0cd7ae07
- meeting/community/2026-06-03
- meeting/variant/2026-06-04
- thread/t-a938dd33b7b841d9
- meeting/community/2026-07-15
- meeting/spark/2026-08-18
- meeting/community/2026-08-26
- thread/t-1d3c20c5c64f7fcb
- meeting/community/2026-10-07
- meeting/community/2026-10-28
- meeting/materialized-views/2026-11-12
links:
- rel: championed_by
  to: person/mxm
  confidence: extracted
  source: thread/t-ce325e60255c54b1
- rel: championed_by
  to: person/pvary
  confidence: extracted
  source: thread/t-1d3c20c5c64f7fcb
- rel: championed_by
  to: person/stevenzwu
  confidence: extracted
  source: thread/t-95092e2c0cd7ae07
- rel: touches
  to: module/iceberg/flink
  confidence: extracted
  source: thread/t-ce325e60255c54b1
- rel: tracked_in
  to: gh:apache/iceberg#15996
  confidence: extracted
  source: thread/t-ce325e60255c54b1
---

# Flink integration and table maintenance

<!-- kb:generated:start -->
## What it is

The Flink connector in the Iceberg Java repository: its sinks, its table maintenance tasks, and the set of Flink versions each Iceberg release supports. Recent work centres on converting equality deletes into deletion vectors inside Flink ([thread, 2026-04-02](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md); [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)) and on the Flink version matrix ([thread, 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md); [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)).

## Current state

- Equality delete conversion: the ConvertEqualityDeletes table maintenance task is merged and reported feature complete. It resolves equality deletes against a primary-key index kept in Flink state, commits data files plus deletion vectors, runs standalone or integrated with IcebergSink, and requires V3 tables. Incremental re-indexing after external commits was deferred ([thread, 2026-04-02](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md); [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
- That task is cited as evidence in the proposal to forbid equality delete writes in V4, which would require Flink and other streaming writers to emit deletion vectors before adopting V4 ([thread, 2026-07-14](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-a938dd.md); [dev list](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)). The spec change forbidding new equality deletes in v4 is listed as merged ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and it was noted that defaults in Flink, Spark and Kafka Connect need a follow-up pass for V4 deprecations ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Versions: Iceberg 1.11.0 shipped Flink 1.20, 2.0 and 2.1. For 1.12.0 the thread settled on 1.20, 2.1, 2.2 and 2.3 after [#17849](https://github.com/apache/iceberg/pull/17849) was merged, so that Flink 2.1 users can upgrade Iceberg without changing Flink version ([thread, 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md); [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)). Removal of Flink 2.1 support is listed among later Java merges ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- A shared source folder for Flink 2.x versions was floated and deferred until after 1.12.0 ([thread, 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md); [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)).
- Variant: the Flink shredded write ([#15596](https://github.com/apache/iceberg/pull/15596)) merged on 2026-05-22 for 1.12 ([Variant Community Sync, 2026-06-04](../records/meetings/variant/2026/2026-06-04.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)); variant support for Flink Avro readers and writers ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and Variant in the DynamicIcebergSink ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) are listed as merged.
- Materialized views: a Flink implementation is in progress and waits for Iceberg core changes to merge first ([Materialized View Sync, 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md); [notes](https://docs.google.com/document/d/1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A)).
- CI: a pull request selecting the Flink pull request matrix by the version that changed ([#16947](https://github.com/apache/iceberg/pull/16947)) was listed at the Spark sync ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Timeline

- 2026-04-02: Thread on converting equality deletes to deletion vectors in Flink continues with [#15996](https://github.com/apache/iceberg/pull/15996) ([thread, 2026-04-02](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md); [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
- 2026-05-22: Flink shredded variant write ([#15596](https://github.com/apache/iceberg/pull/15596)) merged ([Variant Community Sync, 2026-06-04](../records/meetings/variant/2026/2026-06-04.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- 2026-05-26: Thread on Flink version support after Iceberg 1.11.0 starts; it ends without resolving the upgrade-path concern ([thread, 2026-05-26](../records/threads/2026/05/discuss-flink-version-support-after-iceberg-1-11-0-95092e.md); [dev list](https://lists.apache.org/thread/kd183vz2v2y69v4kwbz5wbjfxvx3gf1f)).
- 2026-06-03: Flink UUID support and shredded variant writes are listed as merged ([Community Sync, 2026-06-03](../records/meetings/community/2026/2026-06-03.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07: The equality delete conversion work is reported merged and feature complete ([thread, 2026-04-02](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md); [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
- 2026-07-14: Thread on deprecating equality deletes in V4 starts and cites the Flink conversion task ([thread, 2026-07-14](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-a938dd.md); [dev list](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)).
- 2026-07-15: A Flink equality delete conversion API is listed among Java merges ([Community Sync, 2026-07-15](../records/meetings/community/2026/2026-07-15.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-27: Thread on Flink version support in 1.12.0 starts; it ends with 1.20, 2.1, 2.2 and 2.3 for the release ([thread, 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md); [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)).
- 2026-10-07: Variant in the Flink DynamicIcebergSink and removal of Flink 2.1 support are listed as merged ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-12: Materialized views sync: the Flink implementation is blocked until core changes merge ([Materialized View Sync, 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md); [notes](https://docs.google.com/document/d/1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A)).

## Where help is needed

- An action item without an owner asks to push the Iceberg core pull request reviews for materialized views forward, since the Flink implementation is blocked on them ([Materialized View Sync, 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md); [notes](https://docs.google.com/document/d/1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A)).
- Incremental re-indexing after external commits is a deferred follow-up of the equality delete conversion task ([thread, 2026-04-02](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md); [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
<!-- kb:generated:end -->

## Notes
