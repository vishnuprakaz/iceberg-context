---
id: thread/t-26347b0fcdb11b56
type: thread
title: 'Spec ambiguity: Avro schema for day partition transform fields in manifests'
date: '2026-05-20'
url: https://lists.apache.org/thread/o3oycdqw4sm1sqt54hfrj8c2hwxc0yww
kind: discuss
status: consensus
messages: 8
sources:
- devlist:o3oycdqw4sm1sqt54hfrj8c2hwxc0yww
refs:
- gh:apache/iceberg#16446
- gh:apache/iceberg#5980
- gh:apache/iceberg-go#915
- gh:apache/iceberg-go#1176
links:
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:o3oycdqw4sm1sqt54hfrj8c2hwxc0yww
- rel: started_by
  to: person/Fokko
  confidence: observed
updated: '2026-11-13'
---

# Spec ambiguity: Avro schema for day partition transform fields in manifests

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Spec ambiguity: Avro schema for `day` partition transform fields in manifests](https://lists.apache.org/thread/o3oycdqw4sm1sqt54hfrj8c2hwxc0yww) · **Started:** 2026-05-20 by [[person/Fokko|Fokko Driesprong]] · **Messages:** 8 (last 2026-06-11) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread settles which type the `day` partition transform produces in manifests. Fokko noted the spec line had been changed a few times and suggested reverting the spec change. Kevin Liu laid out the current state: Java, Python and Rust write the result as an Iceberg date (Avro int with the date logical type) and can read either form, while Go writes a plain int and can only read a plain int. He supported changing the spec back to date. Ryan (rdblue) added that the Avro spec requires readers to ignore logical types they do not support, so reading either form follows from Avro. Andrei Tserakhau updated the spec PR to make the result type date with a note on the history; Gang Wu (wgtmac) confirmed iceberg-cpp also writes date.

**Why it matters:** Implementations should write day partition values as date in manifests, and iceberg-go changes its writer and reader to match.

## Outcome

Participants agreed that the day transform result type is date, with reading of plain-int manifests following from the Avro spec. The spec PR apache/iceberg#16446 was updated accordingly and was still unmerged at the last message. ([message](https://lists.apache.org/thread/c7nyxzkshl4d4bvjdjcgqpdr703y5617), `devlist:c7nyxzkshl4d4bvjdjcgqpdr703y5617`)

## Positions

- **[[person/Fokko|Fokko Driesprong]]:** The spec text was changed several times, and the spec change should perhaps be reverted. ([message](https://lists.apache.org/thread/o3oycdqw4sm1sqt54hfrj8c2hwxc0yww))
- **[[person/kevinjqliu|Kevin Liu]]:** Change the spec back to date to match what Java, Python and Rust write, and have readers accept both int and date; changing all implementations to match the current spec would be much work for little value. ([message](https://lists.apache.org/thread/vv80hjdlo5b3o5fnffv89lr15wl2t5zt))
- **[[person/rdblue|Ryan Blue]]:** The Avro spec requires readers that do not support a logical type annotation to ignore it, so reading either date or int correctly is inherited from Avro. ([message](https://lists.apache.org/thread/scnz8cvf4jf5r85qnvcsqqj2yhoxg4hd))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** The spec PR now makes the day result type date and adds a note on the history; iceberg-go will align its writer and reader once the spec change lands. ([message](https://lists.apache.org/thread/c7nyxzkshl4d4bvjdjcgqpdr703y5617))
- **[[person/kevinjqliu|Kevin Liu]]:** No vote should be needed because this is a clarification and not a change. ([message](https://lists.apache.org/thread/g6p56rsnndq64zvbm5w7xz7v6wz9y5rv))
- **[[person/wgtmac|Gang Wu]]:** iceberg-cpp also produces a date type for the day transform and is fine with the consensus. ([message](https://lists.apache.org/thread/y4xq9lyrd8jdxrjo0klfbwvbslog8zl0))

References: [iceberg#16446](https://github.com/apache/iceberg/issues/16446), [iceberg#5980](https://github.com/apache/iceberg/issues/5980), [iceberg-go#915](https://github.com/apache/iceberg-go/issues/915), [iceberg-go#1176](https://github.com/apache/iceberg-go/issues/1176)
<!-- kb:generated:end -->

## Notes
