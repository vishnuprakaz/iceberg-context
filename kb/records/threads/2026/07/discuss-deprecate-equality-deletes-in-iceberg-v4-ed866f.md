---
id: thread/t-ed866fa82546916e
type: thread
title: Deprecate equality deletes in Iceberg V4
date: '2026-07-20'
url: https://lists.apache.org/thread/r6dv9wry0c52ypsm6g9twko1ctvdrdtc
kind: discuss
status: open
messages: 5
sources:
- devlist:r6dv9wry0c52ypsm6g9twko1ctvdrdtc
refs: []
links:
- rel: discussed
  to: initiative/v4-equality-deletes
  confidence: extracted
  source: devlist:r6dv9wry0c52ypsm6g9twko1ctvdrdtc
- rel: started_by
  to: person/xndai
  confidence: observed
updated: '2026-11-13'
---

# Deprecate equality deletes in Iceberg V4

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Deprecate Equality Deletes in Iceberg V4](https://lists.apache.org/thread/r6dv9wry0c52ypsm6g9twko1ctvdrdtc) · **Started:** 2026-07-20 by [[person/xndai|Xiening Dai]] · **Messages:** 5 (last 2026-07-23) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This part of the discussion on Huaxin Gao's proposal to stop writing equality deletes in V4 opens with Xiening's (xndai) concern that it moves the cost of fast updates and deletes from readers to writers, and that keeping an index current is expensive and could hurt V4 adoption. Huaxin replied that resolving positions once, at write time or in background conversion, replaces a join on every read; that the Flink ConvertEqualityDeletes work already maintains a persistent RocksDB primary-key index incrementally; and that streaming upsert workloads can stay on V3 until their engine can emit deletion vectors. zhjwpku asked why readers could not use such an index and how it would be kept in object storage. Ryan Blue strongly supported disallowing equality deletes in V4, said Kafka Connect is not a blocker, and said existing equality deletes can remain supported on upgrade, with two-phase planning used whenever delete manifests exist.

**Why it matters:** Streaming upsert writers that rely on equality deletes would need to produce deletion vectors, or stay on V3, if this proposal is adopted.

## Outcome

These messages end with Ryan Blue's support for the proposal and no stated decision; the questions from zhjwpku about the index are not answered here.

## Positions

- **[[person/xndai|Xiening Dai]]:** Forbidding equality deletes shifts the burden from reader to writer, and without a good alternative or tooling for fast updates it could become a V4 adoption problem. ([message](https://lists.apache.org/thread/r6dv9wry0c52ypsm6g9twko1ctvdrdtc))
- **[[person/huaxingao|Huaxin Gao]]:** Resolving delete positions once is cheaper than re-joining equality deletes on every read, background conversion and a key-lookup index make it practical, and affected workloads can stay on V3 until they can write deletion vectors. ([message](https://lists.apache.org/thread/zqhwkgly7h4c8gnqcf6xfmpvsd8513ww))
- **[[person/zhjwpku|Junwang Zhao]]:** Asks why a reader could not use a key-to-position index to resolve equality deletes at read time, and whether the RocksDB index stays local to one engine rather than shared in the table. ([message](https://lists.apache.org/thread/t7qhrtwyhjxjondt2moq3jgwp4gqhx01))
- **[[person/rdblue|Ryan Blue]]:** Strongly supports deprecating equality deletes and disallowing new ones in V4, making delete resolution a writer responsibility; Kafka Connect is not a blocker. ([message](https://lists.apache.org/thread/s91dd7s7c2ob7ks81cnk82qhbojw5ytp))
- **[[person/rdblue|Ryan Blue]]:** Existing equality deletes can still be supported after upgrade; V4 planning should run two-phase planning only when delete manifests are present. ([message](https://lists.apache.org/thread/tkllcmnfsmhhwfrcofm0c0200mchz51f))
<!-- kb:generated:end -->

## Notes
