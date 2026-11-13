---
id: thread/t-ce325e60255c54b1
type: thread
title: 'Flink: equality delete to DV conversion'
date: '2026-04-02'
url: https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz
kind: discuss
status: informational
messages: 5
sources:
- devlist:d5wr7567ccfd86kf64n7snovnjhvtlqz
refs:
- gh:apache/iceberg#15996
links: []
updated: '2026-11-13'
---

# Flink: equality delete to DV conversion

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Flink: Equality delete to DV conversion](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz) · **Started:** 2026-04-02 by Márton Balassi · **Messages:** 5 (last 2026-07-15) · **Outcome:** informational

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

These messages continue a proposal by mxm to convert equality deletes into deletion vectors in Flink. Márton Balassi supported it as a step toward removing the need for equality deletes. mxm opened PR 15996: the converter monitors a staging branch where the writer commits equality deletes, builds a sharded primary-key index in Flink state backed by RocksDB, resolves the deletes against it and commits data files plus DVs to the main branch. stevenzwu agreed it moves closer to removing equality deletes and can test whether the index scales for streaming CDC and upsert writes; mxm confirmed the solution currently requires V3 tables. In July mxm reported that the work, split into six commits, was merged and feature complete: ConvertEqualityDeletes is a table maintenance task, runs standalone or integrated with IcebergSink, and supports a staging branch or same-branch conversion, the IcebergSink default. Incremental re-indexing after external commits was deferred.

**Why it matters:** Flink can now convert equality deletes into deletion vectors, which is the main evidence used for forbidding equality deletes in V4.

## Outcome

mxm reported that all six commits split from PR 15996 were merged and the ConvertEqualityDeletes maintenance task is feature complete and integrated with IcebergSink; incremental re-indexing after external commits is a deferred follow-up. ([message](https://lists.apache.org/thread/ktd6jqhhfxrj2o6y99dkv7qwkdlnp58t), `devlist:ktd6jqhhfxrj2o6y99dkv7qwkdlnp58t`)

## Positions

- **Márton Balassi:** Supports the proposal; removing reliance on equality deletes in the Flink write path improves read efficiency and makes Flink upserts viable. ([message](https://lists.apache.org/thread/d5wr7567ccfd86kf64n7snovnjhvtlqz))
- **[[person/mxm|Maximilian Michels]]:** The converter runs in line with the writer, resolving staged equality deletes into DVs via a RocksDB-backed primary-key index; row lineage and staging branch lifecycle remain gaps. ([message](https://lists.apache.org/thread/qj3gp8rfymn96x3fkjyfjyg4296rkplv))
- **[[person/stevenzwu|Steven Wu]]:** The proposal gets closer to removing equality deletes and can verify whether an index scales for streaming CDC and upsert writes; asked if it is limited to V3 tables. ([message](https://lists.apache.org/thread/4dmot2lfkr46l45yvfbjd57hjxsovqkn))
- **[[person/mxm|Maximilian Michels]]:** The current solution requires V3 tables; V2 support would be possible with storage and lookup efficiency tradeoffs. ([message](https://lists.apache.org/thread/fd01c188mxpl31kql7t3bdo3yd63dm1q))

References: [iceberg#15996](https://github.com/apache/iceberg/issues/15996)
<!-- kb:generated:end -->

## Notes
