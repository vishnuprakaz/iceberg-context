---
id: initiative/kafka-connect
type: initiative
title: Kafka Connect sink
status: discussion
updated: '2026-11-13'
sources:
- meeting/variant/2026-06-04
- meeting/variant/2026-08-06
- meeting/variant/2026-09-03
- thread/t-34ed4df6d3f60b91
- meeting/community/2026-10-28
links:
- rel: championed_by
  to: person/laskoviymishka
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: touches
  to: module/iceberg/kafka-connect
  confidence: extracted
  source: thread/t-34ed4df6d3f60b91
- rel: tracked_in
  to: gh:apache/iceberg#18003
  confidence: extracted
  source: thread/t-34ed4df6d3f60b91
---

# Kafka Connect sink

<!-- kb:generated:start -->
## What it is

The Kafka Connect sink is the connector in the Iceberg Java repository that writes records from Kafka into Iceberg tables. The mainline sink is append-only today ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)). The main open topic is whether it should gain a change-data-capture (upsert and delete) mode now that V4 forbids new equality deletes ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)) ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Current state

- A proposal on the dev list adds opt-in CDC writes that never commit equality deletes: the coordinator resolves each commit's equality deletes against the base snapshot, writes deletion vectors, and commits data files and deletion vectors together; it would require v3 or later. The thread is open with no decision; the work is in [#18003](https://github.com/apache/iceberg/pull/18003) ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- Reviewers asked first whether the community wants CDC in the sink at all, since append plus MERGE in another engine works, and asked for performance testing before any merge. A reported benchmark gives under 0.4 s per conversion with increasing IDs and 2 to 42 s with random UUID keys on a 10,000-file table ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- At the community sync the position voiced was not to add anything that produces new equality deletes and to explore upserts through a primary key index that yields positions for deletion vectors. Whether the mainline sink can already opt in to equality deletes was disputed and is to be checked ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- The Kafka Connect runtime LICENSE and NOTICE were fixed ([#18019](https://github.com/apache/iceberg/pull/18019)), which may let the artifact ship with the next release ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Kafka Connect shredding support for variant was listed among the merges for 1.12 ([Variant Community Sync, 2026-09-03](../records/meetings/variant/2026/2026-09-03.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).

## Timeline

- 2026-06-04: The variant sync lists Kafka Connect shredded write among open work ([Variant Community Sync, 2026-06-04](../records/meetings/variant/2026/2026-06-04.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- 2026-08-06: Reviving an older Kafka Connect shredding pull request is listed as active variant work ([Variant Community Sync, 2026-08-06](../records/meetings/variant/2026/2026-08-06.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- 2026-09-03: Kafka Connect shredding support is listed among recent merges for 1.12 ([Variant Community Sync, 2026-09-03](../records/meetings/variant/2026/2026-09-03.md); [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- 2026-10-26: Dev list discussion starts on CDC writes in the sink without equality deletes ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- 2026-10-28: Community sync discusses CDC through Kafka Connect once equality deletes are deprecated in V4; no decision. The LICENSE and NOTICE fix ([#18019](https://github.com/apache/iceberg/pull/18019)) is reported as merged ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-13: The latest message in the CDC thread summarizes the proposal and benchmark; no decision yet ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).

## Where help is needed

- The CDC thread asks for input on two questions: whether a sink that never commits equality deletes addresses the original objection to CDC in the sink, and whether the Kafka Connect and Flink approaches should converge for v4 ([thread, 2026-10-26](../records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [dev list](https://lists.apache.org/thread/gmkj55oc0k1k72gobsylgfc9ngk9lyxn)).
- Reviews were requested on the follow-up pull request covering the Hive distribution licensing for Kafka Connect ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
<!-- kb:generated:end -->

## Notes
