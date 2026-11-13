---
id: initiative/v4-equality-deletes
type: initiative
title: Deprecating equality deletes in V4
status: accepted
updated: '2026-11-13'
sources:
- thread/t-a938dd33b7b841d9
- thread/t-e3df87d32bc07907
- thread/t-44dd42ceee95da54
- meeting/community/2026-10-07
- meeting/community/2026-10-28
- thread/t-ce325e60255c54b1
- meeting/column-updates/2026-09-08
- thread/t-34ed4df6d3f60b91
- meeting/v4-metadata/2026-07-13
- thread/t-ed866fa82546916e
- thread/t-90d2a9cd80ec9ab2
- meeting/v4-metadata/2026-07-27
- meeting/v4-metadata/2026-08-10
links:
- rel: championed_by
  to: person/huaxingao
  source: thread/t-e3df87d32bc07907
  confidence: extracted
- rel: championed_by
  to: person/mxm
  source: thread/t-ce325e60255c54b1
  confidence: extracted
- rel: handled_by
  to: group/v4-metadata
  confidence: inferred
  source: meeting/v4-metadata/2026-07-27
- rel: touches
  to: module/iceberg/format
  source: thread/t-44dd42ceee95da54
  confidence: extracted
- rel: touches
  to: module/iceberg/flink
  source: thread/t-ce325e60255c54b1
  confidence: extracted
- rel: touches
  to: module/iceberg/kafka-connect
  source: thread/t-34ed4df6d3f60b91
  confidence: extracted
- rel: tracked_in
  to: gh:apache/iceberg#17783
  source: thread/t-44dd42ceee95da54
  confidence: extracted
---

# Deprecating equality deletes in V4

<!-- kb:generated:start -->
## What it is

Equality deletes mark rows as deleted by column values instead of by position. They are cheap to write but costly on every read, and they block change data capture, row lineage and incremental maintenance of materialized views and indexes ([thread summary](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-a938dd.md), [dev list](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)). In format version 4, writers may no longer produce new equality deletes; existing ones from v2 and v3 tables stay readable, and writers that need row-level deletes use deletion vectors ([thread summary](../records/threads/2026/08/vote-deprecate-equality-deletes-in-iceberg-v4-forbid-new-writes-e3df87.md), [dev list](https://lists.apache.org/thread/5x8ovvz3ppf4krqs543sqjcy3dqdhthm)).

## Current state

- Decided by vote: writing new equality deletes is forbidden for V4 tables, reading them stays supported for V2/V3 tables and for deletes carried into upgraded V4 tables, and upgrading to V4 is metadata-only with conversion to deletion vectors as an optional maintenance action. The vote passed with 7 binding and 17 non-binding +1 votes ([thread summary](../records/threads/2026/08/vote-deprecate-equality-deletes-in-iceberg-v4-forbid-new-writes-e3df87.md), [dev list](https://lists.apache.org/thread/5x8ovvz3ppf4krqs543sqjcy3dqdhthm)).
- Spec wording: the vote on [apache/iceberg#17783](https://github.com/apache/iceberg/pull/17783) passed with 4 binding and 5 non-binding +1 votes; a follow-up pull request was announced for restructuring how the delete sections present deletion vectors and the legacy representations ([thread summary](../records/threads/2026/09/vote-spec-forbid-writing-new-equality-deletes-in-v4-17783-44dd42.md), [dev list](https://lists.apache.org/thread/2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1)). The spec change is listed as merged in the 2026-10-07 community sync highlights ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- Java: dropping equality_ids from the V4 TrackedFile ([apache/iceberg#18427](https://github.com/apache/iceberg/pull/18427)) is listed as merged ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Flink has a conversion path: the ConvertEqualityDeletes table maintenance task converts equality deletes to deletion vectors using a primary-key index kept in Flink state, runs standalone or with IcebergSink, and requires V3 tables. Incremental re-indexing after external commits was deferred ([thread summary](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md), [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
- Column updates do not support equality deletes: existing equality deletes on a file must be converted to deletion vectors before a column update is applied ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)).
- Open: Kafka Connect. A proposal adds CDC writes to the sink that never commit equality deletes, by resolving them to deletion vectors in the coordinator; no decision yet ([thread summary](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md), [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)). At the 2026-10-28 sync the position voiced was not to add anything that produces new equality deletes and to explore upserts through a primary key index instead ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Timeline

- 2026-04-02: Discussion of Maximilian Michels' Flink equality-delete-to-deletion-vector conversion ([apache/iceberg#15996](https://github.com/apache/iceberg/pull/15996)); in July he reports the work merged and feature complete ([thread summary](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md), [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
- 2026-07-13: The V4 metadata sync asks whether the need for partition_spec_id goes away once equality deletes go away ([V4 metadata sync 2026-07-13](../records/meetings/v4-metadata/2026/2026-07-13.md)).
- 2026-07-14: Huaxin Gao restarts the deprecation discussion for V4 and moves from "deprecated but permitted" to forbidding equality delete writes in V4 tables ([thread summary](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-a938dd.md), [dev list](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)).
- 2026-07-20: Concerns about moving cost from readers to writers are raised; Ryan Blue supports disallowing equality deletes in V4 ([thread summary](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-ed866f.md), [dev list](https://lists.apache.org/thread/r6dv9wry0c52ypsm6g9twko1ctvdrdtc)).
- 2026-07-23: Respondents support forbidding new writes while keeping existing equality deletes readable after upgrade; several say a complete replacement is not needed before V4 is ratified as long as a path exists ([thread summary](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-90d2a9.md), [dev list](https://lists.apache.org/thread/9rvgx11ly1j3p570rg1rldsg1h10bzcx)).
- 2026-07-27: Implications of prohibiting equality delete writes are on the V4 metadata sync agenda; no outcome recorded ([V4 metadata sync 2026-07-27](../records/meetings/v4-metadata/2026/2026-07-27.md)).
- 2026-08-10: The V4 metadata sync decides to remove the partition tuple in V4 and replace it with content_stats; equality delete matching on upgraded tables was one of the decision points ([V4 metadata sync 2026-08-10](../records/meetings/v4-metadata/2026/2026-08-10.md)).
- 2026-08-13: Vote to forbid new equality delete writes in V4 is called and passes ([thread summary](../records/threads/2026/08/vote-deprecate-equality-deletes-in-iceberg-v4-forbid-new-writes-e3df87.md), [dev list](https://lists.apache.org/thread/5x8ovvz3ppf4krqs543sqjcy3dqdhthm)).
- 2026-09-23: Spec vote on #17783 is called and passes ([thread summary](../records/threads/2026/09/vote-spec-forbid-writing-new-equality-deletes-in-v4-17783-44dd42.md), [dev list](https://lists.apache.org/thread/2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1)).
- 2026-10-07: The spec change forbidding new equality deletes in v4 is listed as merged ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- 2026-10-26: Proposal for Kafka Connect CDC writes without committing equality deletes ([thread summary](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md), [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- 2026-10-28: Community sync discusses CDC through Kafka Connect after the deprecation; #18427 listed as merged ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Where help is needed

- The Kafka Connect CDC thread is waiting for replies: does a sink that never commits equality deletes address the original objection, and should the Kafka Connect and Flink approaches converge for V4 ([thread summary](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md), [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)). Péter Váry asked for performance testing before merging ([thread summary](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md), [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- Open questions from the 2026-10-28 sync: whether the mainline Kafka Connect sink can currently opt in to equality deletes, and whether it can support upserts with primary key indexes and deletion vectors ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Defaults in Flink, Spark and Kafka Connect need a follow-up pass for V4 deprecations, as noted at the same sync ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Flink: incremental re-indexing after external commits in ConvertEqualityDeletes was left as a follow-up ([thread summary](../records/threads/2026/04/discuss-flink-equality-delete-to-dv-conversion-ce325e.md), [dev list](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz)).
<!-- kb:generated:end -->

## Notes
