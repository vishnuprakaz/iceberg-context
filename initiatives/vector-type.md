---
id: initiative/vector-type
type: initiative
title: Vector type
status: design
updated: '2026-11-13'
sources:
- meeting/community/2026-07-15
- meeting/community/2026-08-05
- meeting/community/2026-10-07
- meeting/file-vector-type/2026-10-08
- meeting/file-vector-type/2026-10-22
- meeting/community/2026-10-28
- thread/t-709611fe90159e57
- meeting/file-vector-type/2026-11-05
links:
- rel: championed_by
  to: person/yyanyy
  confidence: extracted
  source: meeting/community/2026-10-07
- rel: handled_by
  to: group/file-vector-type
  confidence: extracted
  source: meeting/file-vector-type/2026-10-08
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: meeting/file-vector-type/2026-10-22
- rel: tracked_in
  to: gh:apache/iceberg#18416
  confidence: inferred
  source: meeting/file-vector-type/2026-10-22
---

# Vector type

<!-- kb:generated:start -->
## What it is

A proposed vector data type for V4 tables, aimed at AI/ML embeddings: a one-dimensional, fixed-size sequence of numbers with no null, NaN or infinity elements ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)). The design largely relies on Parquet's new vector-equivalent definition and keeps index and function questions separate ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).

## Current state

- Agreed in the working group: target the AI/ML use case; keep the spec simple, with no complicated stats and no predefined metadata such as a distance algorithm; do not bundle characteristics such as a distance function or normalization into the type; start with int, long, float and double element types; sparse vectors are out of scope for now ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- Agreed in the working group: serialize the type as `vector(float, 256)`, and allow only null for initial-default and write-default, accepting that a required vector column cannot be added later ([File and Vector Type Sync, 2026-10-22](../records/meetings/file-vector-type/2026/2026-10-22.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- Deferred: whether vector is a primitive type or a separate category. The question came from a review comment on [#18416](https://github.com/apache/iceberg/pull/18416) (inferred to be the vector type spec pull request), and implementation experience is meant to inform it ([File and Vector Type Sync, 2026-10-22](../records/meetings/file-vector-type/2026/2026-10-22.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- Open: narrow element types such as int8 and float16. Options discussed are new types, annotations, vector-only support, or leaving the width to the physical representation; no decision is recorded ([File and Vector Type Sync, 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- Open: whether vector can stay unsupported for ORC for now; Avro would use an array annotated with a logical type ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- At the community sync's V4 progress report the vector type was described as being in limbo ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- A proposal to ship AI embedding functions in the connectors alongside the FILE and VECTOR work drew replies that leaned against it; no decision ([thread, 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md); [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).

## Timeline

- 2026-07-15: The vector type proposal is listed at the community sync with a design document ([Community Sync, 2026-07-15](../records/meetings/community/2026/2026-07-15.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-05: The proposal document is listed again; no outcome recorded ([Community Sync, 2026-08-05](../records/meetings/community/2026/2026-08-05.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-07: A vector type discussion is announced for the next file and vector type sync ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-08: The sync records consensus on scope, element types and keeping the spec simple ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- 2026-10-22: The sync settles serialization as `vector(float, 256)` and null-only defaults, and defers the type category ([File and Vector Type Sync, 2026-10-22](../records/meetings/file-vector-type/2026/2026-10-22.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- 2026-10-28: V4 progress report at the community sync: vector type is in limbo ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-02: Thread on AI functions for FILE and VECTOR types ([thread, 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md); [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).
- 2026-11-05: float16 test results are presented; no decision on narrow element types ([File and Vector Type Sync, 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).

## Where help is needed

- Everyone was asked to take part in the Parquet community discussion on NaN and infinity handling ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- An action item without an owner: talk with the Avro community about representing vectors ([File and Vector Type Sync, 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
- The group's open questions on narrow element types: at which level they should be supported, and whether the exact element width is needed at planning time ([File and Vector Type Sync, 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).
<!-- kb:generated:end -->

## Notes
