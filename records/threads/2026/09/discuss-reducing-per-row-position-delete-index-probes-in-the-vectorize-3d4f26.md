---
id: thread/t-3d4f26de01d84b04
type: thread
title: Reducing per-row position delete index probes in the vectorized read path
date: '2026-09-10'
url: https://lists.apache.org/thread/5v8j1zj2l8ntygph47r0k61xyskxc5o1
kind: discuss
status: open
messages: 5
sources:
- devlist:5v8j1zj2l8ntygph47r0k61xyskxc5o1
refs:
- gh:apache/iceberg#18027
- gh:apache/iceberg#18026
links:
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:5v8j1zj2l8ntygph47r0k61xyskxc5o1
- rel: started_by
  to: person/simpleqt
  confidence: observed
updated: '2026-11-13'
---

# Reducing per-row position delete index probes in the vectorized read path

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Reducing per-row position delete index probes in the vectorized read path](https://lists.apache.org/thread/5v8j1zj2l8ntygph47r0k61xyskxc5o1) · **Started:** 2026-09-10 by [[person/simpleqt|陈志谦]] · **Messages:** 5 (last 2026-09-12) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

simpleqt proposed PR #18027 (issue #18026) to cut the cost of Spark's vectorized reader calling PositionDeleteIndex.isDeleted once per row, although a batch covers a contiguous ascending range of positions. The change adds a default method forEachInRange(posStart, length, consumer) to PositionDeleteIndex, whose default is the existing per-position loop, and overrides it in BitmapPositionDeleteIndex; ColumnarBatchUtil uses it only when the scan has no equality deletes. Reported results are 2.6x to 9.3x less delete-check CPU and 13 to 19 percent end to end on narrow integer projections, with no measurable gain at ten or more columns. The author asked mainly whether adding another default method to the interface is acceptable. Peter (pvary) suggested a batch iterator like RoaringBatchIterator; the author benchmarked it and found it slightly slower than the PR's approach, and kept the current design while offering to explore a persistent iterator.

**Why it matters:** The PR adds a method to the core PositionDeleteIndex interface, so it needs maintainer agreement on the API shape before it can land.

## Outcome

No decision on the interface addition is recorded; the author kept forEachInRange after benchmarking the suggested batch iterator and offered to investigate a persistent-iterator variant.

## Positions

- **[[person/simpleqt|陈志谦]]:** Add a forEachInRange default method to PositionDeleteIndex so a batch's position range is resolved once, keeping the per-row loop as the default for other implementations. ([message](https://lists.apache.org/thread/5v8j1zj2l8ntygph47r0k61xyskxc5o1))
- **[[person/pvary|Peter Vary]]:** Consider something like a PositionBatchIterator backed by RoaringBatchIterator instead. ([message](https://lists.apache.org/thread/n4j0z773lh7y4mobjx3hl1pjvsjsz601))
- **[[person/simpleqt|陈志谦]]:** A BatchIterator measured slightly slower than forEachInRange in JMH and would add a new API and lifecycle, so the PR keeps the default-method approach. ([message](https://lists.apache.org/thread/hk1h60k1moyozllpkyk264oq8x33o7xs))

References: [iceberg#18027](https://github.com/apache/iceberg/issues/18027), [iceberg#18026](https://github.com/apache/iceberg/issues/18026)
<!-- kb:generated:end -->

## Notes
