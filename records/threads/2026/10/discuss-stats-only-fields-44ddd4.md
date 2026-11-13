---
id: thread/t-44ddd498b576dea4
type: thread
title: Stats-only fields
date: '2026-10-22'
url: https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr
kind: discuss
status: consensus
messages: 6
sources:
- devlist:t4nm0blbo33y5fnkcok6lrmdc4k4toxr
refs:
- gh:apache/iceberg#18405
- gh:apache/iceberg#16972
links:
- rel: discussed
  to: initiative/v4-content-stats
  confidence: extracted
  source: devlist:t4nm0blbo33y5fnkcok6lrmdc4k4toxr
- rel: discussed
  to: initiative/collations
  confidence: extracted
  source: devlist:t4nm0blbo33y5fnkcok6lrmdc4k4toxr
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Stats-only fields

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Stats-only fields](https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr) · **Started:** 2026-10-22 by [[person/rdblue|Ryan Blue]] · **Messages:** 6 (last 2026-10-28) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rdblue announced that the V4 spec change for what was previously called non-materialized columns is about ready in PR #18405, now named 'stats-only fields', and said he chose not to unify them with expression-generated materialized columns because that would add an unneeded indirection. pvary suggested modelling them as schema fields with a 'generated' block and a 'stats-only' strategy. rdblue replied that stats-only fields are not part of the table schema and should not be displayed in it, that their types are derived and can change with schema changes, and that nesting them in the schema would need composition rules; pvary accepted this. laskoviymishka supported the change, noted collation support (#16972) could use it, and asked whether readers should be required to ignore stats for expressions they cannot evaluate. rdblue preferred a new type with standardized metadata for collations and leaving unbindable expressions to implementations, and said he would start a vote.

**Why it matters:** V4 statistics can cover derived values through stats-only fields that live outside the table schema, so schema consumers do not need to filter them out.

## Outcome

No objections remained; rdblue said most PR comments were addressed and that he would start a vote thread. ([message](https://lists.apache.org/thread/ygsww828k5z5fj5otz2hpcjcmqwhmz60), `devlist:ygsww828k5z5fj5otz2hpcjcmqwhmz60`)

## Positions

- **[[person/rdblue|Ryan Blue]]:** Stats-only fields should stay separate from the schema and from generated columns, because they are not table data, have derived types and would complicate schema composition. ([message](https://lists.apache.org/thread/30v5gm09rhfpqk5wtjkt4psx21xzymvm))
- **[[person/pvary|Peter Vary]]:** Suggested expressing stats-only fields as generated schema fields with a stats-only strategy, then agreed with the proposal because they should not be displayed as part of the table schema. ([message](https://lists.apache.org/thread/1zd0wwwx5jfs1z3z7l8y70rk9yfbsj5k))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Supports the change and asks that the unsupported-type rule also cover expressions, so readers ignore stats for expression values they cannot evaluate, which would serve collations. ([message](https://lists.apache.org/thread/h2zmgk8f9b1mcx80dshslztfkg6x8573))
- **[[person/rdblue|Ryan Blue]]:** Collations should use a new type with standardized metadata rather than an expression, and whether to ignore unbindable expressions should be left to implementations. ([message](https://lists.apache.org/thread/ygsww828k5z5fj5otz2hpcjcmqwhmz60))

References: [iceberg#18405](https://github.com/apache/iceberg/issues/18405), [iceberg#16972](https://github.com/apache/iceberg/issues/16972)
<!-- kb:generated:end -->

## Notes
