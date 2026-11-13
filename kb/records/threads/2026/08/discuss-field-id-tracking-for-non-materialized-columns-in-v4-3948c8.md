---
id: thread/t-3948c81a19bd7c87
type: thread
title: Field ID tracking for non-materialized columns in v4
date: '2026-08-31'
url: https://lists.apache.org/thread/4h53r1nvvgxqymfvx7vcyhqgh1fk8180
kind: discuss
status: open
messages: 10
sources:
- devlist:4h53r1nvvgxqymfvx7vcyhqgh1fk8180
refs:
- gh:apache/iceberg#16961
- gh:apache/iceberg#17893
- doc:1u93kyIrTc8bt9VSTB4O0GM9S7zuXekqixJR6Id2FZC4
links:
- rel: discussed
  to: initiative/v4-content-stats
  confidence: extracted
  source: devlist:4h53r1nvvgxqymfvx7vcyhqgh1fk8180
- rel: discussed
  to: initiative/secondary-indexes
  confidence: extracted
  source: devlist:4h53r1nvvgxqymfvx7vcyhqgh1fk8180
- rel: discussed
  to: initiative/collations
  confidence: extracted
  source: devlist:4h53r1nvvgxqymfvx7vcyhqgh1fk8180
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Field ID tracking for non-materialized columns in v4

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Field ID tracking for non-materialized columns in v4](https://lists.apache.org/thread/4h53r1nvvgxqymfvx7vcyhqgh1fk8180) · **Started:** 2026-08-31 by [[person/rdblue|Ryan Blue]] · **Messages:** 10 (last 2026-10-15) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Ryan Blue proposed how v4 assigns table field IDs to values that are not written into the table, so their stats can be tracked: one table of non-materialized fields, with entry types for partition output values, collation bounds and expression results, instead of a table of all expressions. Gianluca Graziadei asked about expressions such as Hilbert curves whose meaning depends on the data distribution; Blue answered that the stored expression must completely describe a transformation of a single row, with any parameters embedded, and Graziadei agreed. Péter Váry noted that an explicit data type removes some schema evolution flexibility, asked for ID-based field references and suggested a dedicated identity type; Blue would require the data type only where it cannot be derived, agreed on ID-based references and saw no value in an identity case. Russell Spitzer asked to define an output for sort orders and how these fields are versioned. In October Váry asked whether derived virtual columns could handle this instead. No decision is recorded in the thread.

**Why it matters:** The choice determines how stats for partition outputs, collation bounds and index expressions are addressed in v4 metadata.

## Outcome

No decision is recorded. Repliers supported the direction, and the last message raises derived virtual columns as an alternative without a reply.

## Positions

- **[[person/rdblue|Ryan Blue]]:** Non-materialized values should get field IDs from a single table of non-materialized fields with typed entries (partition value, collation bounds, expression value), leaving existing structures alone. ([message](https://lists.apache.org/thread/4h53r1nvvgxqymfvx7vcyhqgh1fk8180))
- **[[person/GGraziadei|Gianluca Graziadei]]:** Expressions whose values depend on the data distribution need different handling from row-deterministic ones, possibly with a persisted distribution. ([message](https://lists.apache.org/thread/12bsyhd2g7z3sf86l6j681god6jvyrf1))
- **[[person/pvary|Peter Vary]]:** Expressions should reference fields by ID, an explicit data type trades away some schema evolution flexibility, and a compact identity-value type may be worth adding for indexes. ([message](https://lists.apache.org/thread/pn74s66ovj8hg6csv1n9cr34zt450q02))
- **[[person/rdblue|Ryan Blue]]:** The data type is required only when it cannot be derived, references are bound or ID-based, an identity special case has little value, and expressions with hidden inputs need not be designed for. ([message](https://lists.apache.org/thread/4ktckw5qlxsllhnk7vzbfbopdcslqx4c))
- **[[person/RussellSpitzer|Russell Spitzer]]:** An output for sort orders should be defined as well, and it should be clear whether these expressions are versioned over time alongside the schema ID. ([message](https://lists.apache.org/thread/gkhmlpbqj7oqq1ptgcbbr5bh59bsdz86))
- **[[person/GGraziadei|Gianluca Graziadei]]:** The spec should state that an expression is a deterministic function of the referenced fields with fitted parameters as literals, and that entries are immutable so a changed expression gets a new field ID. ([message](https://lists.apache.org/thread/6krz0g0h3hc2v3w5x8wgbhbx1sg8gr9j))
- **[[person/pvary|Peter Vary]]:** Non-materialized columns could instead be handled as derived virtual columns, as described in a separate document. ([message](https://lists.apache.org/thread/sq52zcsmc7ls7gzv6o10r9r5m4kobvx4))

References: [iceberg#16961](https://github.com/apache/iceberg/issues/16961), [iceberg#17893](https://github.com/apache/iceberg/issues/17893), [doc](https://docs.google.com/document/d/1u93kyIrTc8bt9VSTB4O0GM9S7zuXekqixJR6Id2FZC4)
<!-- kb:generated:end -->

## Notes
