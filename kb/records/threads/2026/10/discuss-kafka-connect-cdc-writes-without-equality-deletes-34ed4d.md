---
id: thread/t-34ed4df6d3f60b91
type: thread
title: Kafka Connect CDC writes without equality deletes
date: '2026-10-26'
url: https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn
kind: discuss
status: open
messages: 5
sources:
- devlist:gmkj55oc0k1k72gobsylgfc9ngk9lyxn
refs:
- gh:apache/iceberg#18003
- gh:apache/iceberg#14797
- gh:apache/iceberg#10842
- gh:apache/iceberg#17783
- gh:apache/iceberg#15996
- gh:apache/iceberg#17142
- gh:apache/iceberg#16961
- list:96dhf3sj5pc4ql0l8yk8sxgtr78bchrd
- list:wfd3s65dpyzto8g8poffcg1tcqpgk5k7
links:
- rel: discussed
  to: initiative/kafka-connect
  confidence: extracted
  source: devlist:gmkj55oc0k1k72gobsylgfc9ngk9lyxn
- rel: discussed
  to: initiative/v4-equality-deletes
  confidence: extracted
  source: devlist:gmkj55oc0k1k72gobsylgfc9ngk9lyxn
updated: '2026-11-13'
---

# Kafka Connect CDC writes without equality deletes

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Kafka Connect CDC writes without equality deletes](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn) · **Started:** 2026-10-26 by koodin 9 · **Messages:** 5 (last 2026-11-13) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

koodin 9 proposed adding CDC (upsert and delete) writes to the Kafka Connect sink without ever committing equality deletes: the coordinator resolves each commit's equality deletes against the base snapshot with a stateless scan, writes deletion vectors, and commits data files and DVs in one RowDelta. CDC would require v3 or later and the write side pays the conversion cost. Andrei Tserakhau (laskoviymishka) considered the design right but asked first whether the community wants CDC in the sink at all, since append plus MERGE in another engine works, and asked for input from those who made the original decision. koodin 9 answered that issue #10842 intended to restore delta writer support once equality delete concerns were addressed, and that CDC would be opt-in. Péter Váry asked for performance testing before merging and raised concurrent commit starvation. A later summary reports a benchmark: under 0.4 s with increasing IDs, 2 to 42 s with random UUID keys on a 10,000-file table. The thread is waiting for further replies.

**Why it matters:** The outcome decides whether the mainline Kafka Connect sink, which is append-only today, gains an upsert and delete mode.

## Outcome

No decision yet. The last message summarizes the proposal and the benchmark and asks whether a sink that never commits equality deletes addresses the original objection, and whether the Kafka Connect and Flink approaches should converge for v4. ([message](https://lists.apache.org/thread/tgnnqdjwwfw71ogwcf3qbptjctd1zg4w), `devlist:tgnnqdjwwfw71ogwcf3qbptjctd1zg4w`)

## Positions

- **koodin 9:** The sink's coordinator should convert equality deletes into deletion vectors before the commit, without state, so the table never receives an equality delete. ([message](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** The design is right if CDC in the sink is wanted at all; append-only plus MERGE in another engine scales and keeps row IDs, but v3 DVs and the v4 ban on new equality deletes make it reasonable to reopen the earlier decision. ([message](https://lists.apache.org/thread/9ykl9n70mhzkvz21dwrmoollkz7k0p7h))
- **koodin 9:** CDC should be opt-in with append-only as the default, and append plus MERGE stays the better fit for tables that track rows by row ID or where conversion cannot keep up with the commit interval. ([message](https://lists.apache.org/thread/x95nkfkd6n1v1j4tyfr0ykz3qhbwrypm))
- **[[person/pvary|Peter Vary]]:** Equality delete resolution should be performance tested before any code is merged, since it is likely slow without an index, and concurrent commits such as compaction may be starved. ([message](https://lists.apache.org/thread/nnxk6z57h8csloj3s16r37sswsoync0l))

References: [iceberg#18003](https://github.com/apache/iceberg/issues/18003), [iceberg#14797](https://github.com/apache/iceberg/issues/14797), [iceberg#10842](https://github.com/apache/iceberg/issues/10842), [iceberg#17783](https://github.com/apache/iceberg/issues/17783), [iceberg#15996](https://github.com/apache/iceberg/issues/15996), [iceberg#17142](https://github.com/apache/iceberg/issues/17142), [iceberg#16961](https://github.com/apache/iceberg/issues/16961), [thread](https://lists.apache.org/thread/96dhf3sj5pc4ql0l8yk8sxgtr78bchrd), [thread](https://lists.apache.org/thread/wfd3s65dpyzto8g8poffcg1tcqpgk5k7)
<!-- kb:generated:end -->

## Notes
