---
id: thread/t-1bfe2cedf06f8797
type: thread
title: 'V4: improved column statistics'
date: '2025-06-02'
url: https://lists.apache.org/thread/81vqxtw6tlvszon1tzymjbjbmo0hjy0n
kind: discuss
status: open
messages: 29
sources:
- devlist:81vqxtw6tlvszon1tzymjbjbmo0hjy0n
refs:
- gh:apache/iceberg#13933
- gh:apache/iceberg#14234
- doc:1uvbrwwAJW2TgsnoaIcwAFpjbhHkBUL5wY_24nKgtt9I
- doc:1s9_o_Y8js4kHVCYI2OeL0Yh3Ey0qfkuE7Mm-z-QoEfo
- doc:1ZK5g8_bA1Y9SQ4UA5jAREX9iNX56xLWA5vAuKpQC4L8
links:
- rel: started_by
  to: person/nastra
  confidence: observed
updated: '2026-11-13'
---

# V4: improved column statistics

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] v4 - Improved column statistics](https://lists.apache.org/thread/81vqxtw6tlvszon1tzymjbjbmo0hjy0n) · **Started:** 2025-06-02 by [[person/nastra|Eduard Tudenhoefner]] · **Messages:** 29 (last 2026-05-13) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Eduard Tudenhöfner proposed replacing the map-based column statistics in manifests with a typed, per-field stats structure so that individual stats can be projected, original types are kept, and new stats (for example for geo and variant) can be added. Replies supported the goal. Discussion centred on how stats field IDs are derived (10000 + 200 * field ID), whether that leaves enough ID space, how to handle reserved columns, whether stats for sort orders or expressions should be covered, and whether engine-specific custom stats should be allowed. After two community meetings the proposal was updated: stats renamed to content stats, IDs defined for the table and reserved ID spaces, custom stats not supported with expressions preferred, column_size removed and avg/max value size added. Eduard said the design could go to a vote; the last message points to the spec changes in PR #14234 for review.

**Why it matters:** This is the design thread behind the V4 content stats structure and its field ID assignment, which every implementation reading V4 manifests will need to follow.

## Outcome

No vote was held in this thread. The proposal was updated after two meetings and the spec changes are under review in PR #14234.

## Positions

- **Eduard Tudenhöfner:** Column stats should move from field-id maps to a projectable, typed, extensible per-field structure. ([message](https://lists.apache.org/thread/81vqxtw6tlvszon1tzymjbjbmo0hjy0n))
- **[[person/rdblue|Ryan Blue]]:** Avro manifests also benefit because unprojected stats fields can be skipped, and the ID scheme leaves room for more than 10.7 million table field IDs; stats for expressions should be a later proposal. ([message](https://lists.apache.org/thread/2f5p6r5vh4ocjswfthjfg4k0mkdwsb5j))
- **[[person/pvary|Peter Vary]]:** The 10000 + 200 * field ID scheme is too limiting and leaves no way to store non-standard stats; metadata describing the stats present would use less ID space. ([message](https://lists.apache.org/thread/1hrc8ophzkymv6m1md46l31fbjg71nl0))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Space should be reserved for stats on the sort order transform applied to a file, to allow pruning and compaction optimizations. ([message](https://lists.apache.org/thread/fy2dpyzg6w9glz4pn2qwr39o94j3mgn7))
- **[[person/danielcweeks|Daniel C. Weeks]]:** The stats ID space should have an upper bound with ranges for sort orders and expressions, and custom stats should not be supported; expressions are a better way to customize. ([message](https://lists.apache.org/thread/9s6h9lq9yzzq9gpryqr2v36jg5so7lt5))
- **Micah Kornfield:** Keep the V4 scheme as simple as possible and revise later if needed; implementations wanting custom stats could use the top of the reserved offset range. ([message](https://lists.apache.org/thread/2464p6c9nos9h4rj8lct0ldc1txk95yn))

References: [iceberg#13933](https://github.com/apache/iceberg/issues/13933), [iceberg#14234](https://github.com/apache/iceberg/issues/14234), [doc](https://docs.google.com/document/d/1uvbrwwAJW2TgsnoaIcwAFpjbhHkBUL5wY_24nKgtt9I), [doc](https://docs.google.com/document/d/1s9_o_Y8js4kHVCYI2OeL0Yh3Ey0qfkuE7Mm-z-QoEfo), [doc](https://docs.google.com/document/d/1ZK5g8_bA1Y9SQ4UA5jAREX9iNX56xLWA5vAuKpQC4L8)
<!-- kb:generated:end -->

## Notes
