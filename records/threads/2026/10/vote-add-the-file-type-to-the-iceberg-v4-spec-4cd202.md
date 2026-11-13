---
id: thread/t-4cd20220f5ceef8a
type: thread
title: Vote on adding the File type to the Iceberg v4 spec
date: '2026-10-12'
url: https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49
kind: vote
status: passed
messages: 22
sources:
- devlist:7ctclwomk8yqcclzj82z0htlqk2xjf49
- devlist:6b63cbcsf0l69z9hs6v9nc1gp4y96tlp
refs:
- gh:apache/iceberg#17918
links:
- rel: started_by
  to: person/talatuyarer
  confidence: observed
updated: '2026-11-13'
---

# Vote on adding the File type to the Iceberg v4 spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add the File type to the Iceberg v4 spec](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49) · **Started:** 2026-10-12 by [[person/talatuyarer|Talat UYARER]] · **Messages:** 22 (last 2026-10-19) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Talat Uyarer, on behalf of the FILE type working group, started a vote on adding a `file` data type to the v4 table spec through PR #17918. A file value is a range of bytes stored inline or as a reference to an external file, following the Parquet FILE logical type. It has six fixed implicit sub-fields (uri, offset, size, content_type, checksum, inline) whose field IDs are offsets +1 to +6 from the file field's ID. Relative URIs resolve against the table location, and each sub-field gets its own stats. File values have no equality, ordering or hashing, cannot be identifier fields or partition or sort sources, must default to null, and cannot be promoted from a struct. Mappings are given for Parquet, Avro and ORC, and the type is valid only in v4. Every reply in this part of the thread was a +1; no result message appears here.

**Why it matters:** If adopted, v4 tables gain a first-class type for referencing or embedding unstructured files, with rules implementations in every language must follow.

## Outcome

No result is announced in these messages. Votes cast here were all +1: four marked binding, sixteen marked non-binding and one unmarked.

**Result posted in a separate thread on 2026-10-19:** [[RESULT][VOTE] Add the File type to the Iceberg v4 spec](https://lists.apache.org/thread/6b63cbcsf0l69z9hs6v9nc1gp4y96tlp) (`devlist:6b63cbcsf0l69z9hs6v9nc1gp4y96tlp`). Outcome read from that message: passed.

## Positions

- **[[person/talatuyarer|Talat UYARER]]:** Proposes adding the `file` type to the v4 spec as defined in PR #17918. ([message](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49))

References: [iceberg#17918](https://github.com/apache/iceberg/issues/17918)
<!-- kb:generated:end -->

## Notes
