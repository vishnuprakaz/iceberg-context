---
id: initiative/v4-content-stats
type: initiative
title: V4 statistics redesign
status: implementing
updated: '2026-11-13'
sources:
- thread/t-1bfe2cedf06f8797
- thread/t-28612214cb0c85f1
- meeting/community/2026-06-03
- meeting/v4-metadata/2026-06-29
- meeting/v4-metadata/2026-07-13
- meeting/v4-metadata/2026-08-10
- meeting/column-updates/2026-08-11
- meeting/v4-metadata/2026-08-24
- meeting/community/2026-08-26
- thread/t-3948c81a19bd7c87
- thread/t-72545de0b328100f
- thread/t-1dfccee77a1376e9
- meeting/v4-metadata/2026-10-19
- thread/t-44ddd498b576dea4
- thread/t-db8ec8a6f20fbd0d
- meeting/index/2026-10-26
- meeting/community/2026-10-28
- thread/t-7d24fa0351cadc2c
links:
- rel: championed_by
  to: person/nastra
  confidence: extracted
  source: thread/t-28612214cb0c85f1
- rel: championed_by
  to: person/anoopj
  confidence: extracted
  source: thread/t-db8ec8a6f20fbd0d
- rel: championed_by
  to: person/rdblue
  confidence: extracted
  source: thread/t-7d24fa0351cadc2c
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-10-19
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-28612214cb0c85f1
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/community/2026-08-26
- rel: tracked_in
  to: gh:apache/iceberg#14234
  confidence: extracted
  source: thread/t-28612214cb0c85f1
---

# V4 statistics redesign

<!-- kb:generated:start -->
## What it is

V4 replaces the map-based column statistics in manifests with a typed, per-field structure called content stats, so that single stats can be projected, original types are kept and new kinds of stats can be added ([thread summary](../records/threads/2025/06/discuss-v4-improved-column-statistics-1bfe2c.md), [dev list](https://lists.apache.org/thread/81vqxtw6tlvszon1tzymjbjbmo0hjy0n)). Related V4 changes build on it: a file-level flag saying whether stats are tight, and "stats-only fields" that give field IDs to values not stored in the table, such as partition values and expression results, so their stats can be tracked ([thread summary](../records/threads/2026/10/vote-spec-replace-per-column-tight-bounds-with-file-level-tight-stats--db8ec8.md), [dev list](https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl); [thread summary](../records/threads/2026/10/vote-add-stats-only-fields-for-v4-7d24fa.md), [dev list](https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t)).

## Current state

- The content stats representation is in the V4 spec: the vote on [#14234](https://github.com/apache/iceberg/pull/14234) passed, framed as acknowledging the direction, with changes still possible until the whole V4 spec is finalized ([thread summary](../records/threads/2026/05/vote-spec-addition-of-content-stats-representation-to-v4-286122.md), [dev list](https://lists.apache.org/thread/v3bq8snhtdwmj20v4s6kv5byg18cv84t)); the 3 June community sync lists it as merged ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md)).
- Stats-only fields ([#18405](https://github.com/apache/iceberg/pull/18405)): the vote passed with 15 +1 votes ([thread summary](../records/threads/2026/10/vote-add-stats-only-fields-for-v4-7d24fa.md), [dev list](https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t)).
- File-level `tight_stats` replacing per-column `tight_bounds` ([#18585](https://github.com/apache/iceberg/pull/18585)): a vote was called on 22 October; the thread shows 13 +1 votes and no result message ([thread summary](../records/threads/2026/10/vote-spec-replace-per-column-tight-bounds-with-file-level-tight-stats--db8ec8.md), [dev list](https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl)).
- `avg_value_size_in_bytes` is being changed to `total_bytes` ([#18308](https://github.com/apache/iceberg/pull/18308)); nobody objected, and for the Java API the favoured option is adding `totalBytes` with `avgValueSize` derived from it ([thread summary](../records/threads/2026/09/discuss-changing-avg-value-size-in-bytes-to-total-bytes-in-content-sta-72545d.md), [dev list](https://lists.apache.org/thread/8f91nk08cq2pxtsdpf1o34ktthn7jcwk)).
- In V4 the partition tuple is to be replaced by content stats: source column values for monotonic transforms, the expression for non-monotonic ones such as bucketing ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)).
- When manifests are rewritten, the stats read schema is built from the table's current metrics config ([column-updates sync 2026-08-11](../records/meetings/column-updates/2026/2026-08-11.md)).
- Open: manifest aggregation rules for `tight_stats` and its final name ([v4-metadata sync 2026-10-19](../records/meetings/v4-metadata/2026/2026-10-19.md)); whether to version the metrics config with a metrics-config-id ([v4-metadata sync 2026-08-24](../records/meetings/v4-metadata/2026/2026-08-24.md)); an exact flag for null and NaN counts, on the agenda with no outcome ([v4-metadata sync 2026-06-29](../records/meetings/v4-metadata/2026/2026-06-29.md)); partial updates of `content_stats` for column files ([v4-metadata sync 2026-07-13](../records/meetings/v4-metadata/2026/2026-07-13.md)).
- The collations proposal ([#16972](https://github.com/apache/iceberg/pull/16972)) is built on stats-only fields ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)), and the index spec is considering allowing them too ([index sync 2026-10-26](../records/meetings/index/2026/2026-10-26.md)).

## Timeline

- 2025-06-02: Eduard Tudenhöfner opens the design thread on improved column statistics for V4; after two community meetings the proposal is renamed content stats ([thread summary](../records/threads/2025/06/discuss-v4-improved-column-statistics-1bfe2c.md), [dev list](https://lists.apache.org/thread/81vqxtw6tlvszon1tzymjbjbmo0hjy0n)).
- 2026-05-15: Vote on adding the content stats representation to the V4 spec ([#14234](https://github.com/apache/iceberg/pull/14234)) opens; it passed with 5 binding and 2 non-binding +1 votes ([thread summary](../records/threads/2026/05/vote-spec-addition-of-content-stats-representation-to-v4-286122.md), [dev list](https://lists.apache.org/thread/v3bq8snhtdwmj20v4s6kv5byg18cv84t)).
- 2026-06-03: The community sync lists the content stats spec change as merged ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md)).
- 2026-08-10: Decision to replace the partition tuple with content stats in V4 ([v4-metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)).
- 2026-08-26: A content stats evaluator is listed among merged Java work ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md)).
- 2026-08-31: Ryan Blue proposes field ID tracking for non-materialized columns, the start of what became stats-only fields ([thread summary](../records/threads/2026/08/discuss-field-id-tracking-for-non-materialized-columns-in-v4-3948c8.md), [dev list](https://lists.apache.org/thread/4h53r1nvvgxqymfvx7vcyhqgh1fk8180)).
- 2026-09-29: Thread on storing `total_bytes` instead of the average value size ends without objection ([thread summary](../records/threads/2026/09/discuss-changing-avg-value-size-in-bytes-to-total-bytes-in-content-sta-72545d.md), [dev list](https://lists.apache.org/thread/8f91nk08cq2pxtsdpf1o34ktthn7jcwk)).
- 2026-10-05: Anoop Johnson's stats tightness thread reaches consensus on a file-level flag ([thread summary](../records/threads/2026/10/discuss-iceberg-v4-stats-tightness-1dfcce.md), [dev list](https://lists.apache.org/thread/tv7bvqctdfh5qng1sx5rp8r4r00nsv60)).
- 2026-10-19: The V4 metadata sync reaches consensus on `tight_stats`, naming still to be decided ([v4-metadata sync 2026-10-19](../records/meetings/v4-metadata/2026/2026-10-19.md)).
- 2026-10-22: Discussion thread on stats-only fields ends without remaining objections ([thread summary](../records/threads/2026/10/discuss-stats-only-fields-44ddd4.md), [dev list](https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr)); vote on file-level `tight_stats` opens ([thread summary](../records/threads/2026/10/vote-spec-replace-per-column-tight-bounds-with-file-level-tight-stats--db8ec8.md), [dev list](https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl)).
- 2026-10-28: Vote on stats-only fields ([#18405](https://github.com/apache/iceberg/pull/18405)) opens; it passed with 15 +1 votes ([thread summary](../records/threads/2026/10/vote-add-stats-only-fields-for-v4-7d24fa.md), [dev list](https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t)).
<!-- kb:generated:end -->

## Notes
