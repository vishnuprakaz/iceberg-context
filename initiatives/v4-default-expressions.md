---
id: initiative/v4-default-expressions
type: initiative
title: V4 default value expressions
status: vote
updated: '2026-11-13'
sources:
- meeting/community/2026-10-07
- meeting/file-vector-type/2026-10-22
- meeting/community/2026-10-28
- thread/t-33958badf295b701
links:
- rel: championed_by
  to: person/danielcweeks
  confidence: extracted
  source: thread/t-33958badf295b701
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-33958badf295b701
- rel: tracked_in
  to: gh:apache/iceberg#16777
  confidence: extracted
  source: thread/t-33958badf295b701
---

# V4 default value expressions

<!-- kb:generated:start -->
## What it is

Today a column's `write-default` is a literal value. This V4 change lets `write-default` hold an expression, as defined by the expressions spec, so that writers evaluate it when a value is not supplied ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob)).

## Current state

- A vote on the spec pull request [#16777](https://github.com/apache/iceberg/pull/16777) opened on 2 November. The thread shows only +1 votes; on 6 November the caller said he would add his own +1 and close the vote in a separate result thread, and that result is not on record here ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob)).
- The ballot text in the vote message is worded as adding stats-only fields, although the subject and description are about default value expressions ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob)).
- Before the vote, the 28 October community sync noted that the spec was thought to be ready but depends on expression spec primitives landing first ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- For vector columns, the file and vector type sync decided to allow only null as `initial-default` and `write-default` ([file-vector-type sync 2026-10-22](../records/meetings/file-vector-type/2026/2026-10-22.md)).

## Timeline

- 2026-10-07: The community sync lists default values with DDL in Spark among merged Java work ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- 2026-10-28: V4 progress report: the default value expressions spec is thought ready, pending expression spec primitives; Amogh Jahagirdar is to check with Daniel Weeks whether it is ready for a vote ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- 2026-11-02: Daniel Weeks starts the vote on default value expressions for V4 ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob)).
<!-- kb:generated:end -->

## Notes
