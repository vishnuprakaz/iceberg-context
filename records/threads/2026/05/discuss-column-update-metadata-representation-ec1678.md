---
id: thread/t-ec167869ed1e0e08
type: thread
title: Column update metadata representation
date: '2026-05-20'
url: https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg
kind: discuss
status: consensus
messages: 8
sources:
- devlist:7jryw9dfvc02s411twn4o7s5gjrybfxg
refs:
- gh:apache/iceberg#16285
- doc:1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs
- doc:160-FizR6zOASMb86NycfgCm7cZbh6HK7FLcUW8_Xp-0
- list:jbh1gbrso5h6l4by9rh9poy2cjjtb8j0
- yt:exC7RCDYtk4
links:
- rel: started_by
  to: person/gaborkaszab
  confidence: observed
updated: '2026-11-13'
---

# Column update metadata representation

<!-- kb:generated:start -->
**Thread:** [[Discuss] Column Update metadata representation](https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg) · **Started:** 2026-05-20 by [[person/gaborkaszab|Gabor Kaszab]] · **Messages:** 8 (last 2026-07-24) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Gábor Kaszab opened a discussion on how column files are represented in V4 manifest metadata. The agreed starting point was a ColumnFile struct with field_ids, location and file_size_in_bytes; the open part was tracking information such as sequence numbers and per-column-file status. Steven Wu objected to repurposing file_sequence_number and proposed a separate latest_column_file_sequence_number in the tracking struct. Later updates dropped per-column-file status in favour of change detection through REPLACED and MODIFIED entries of the TrackedFile, and a V4 AMT sync decided to bump the TrackedFile data sequence number instead of adding a new sequence number field. Whether the base file should itself be listed as a column file was debated across several syncs. The final message reports the conclusion to keep the base file separate from column files, and an extended ColumnFile struct with format_version, file_format, key_metadata and split_offsets. The metadata PR was still awaiting review.

**Why it matters:** It settles the manifest-level structs that V4 column update implementations build on, including that a TrackedFile stays a physical base file with column files on top.

## Outcome

The column update sync concluded to keep the base file separate from column files and extended the ColumnFile struct with format_version, file_format, key_metadata and split_offsets. The metadata PR (#16285) was still open for review. ([message](https://lists.apache.org/thread/dn6fpsn9o63d25kk6lgdq97cpcqv4l9s), `devlist:dn6fpsn9o63d25kk6lgdq97cpcqv4l9s`)

## Positions

- **Gábor Kaszab:** Proposed per-column-file status values (EXISTING, ADDED, DELETED, REPLACED) and argued a column-file-level sequence number is not needed for _last_updated_sequence_number. ([message](https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg))
- **[[person/stevenzwu|Steven Wu]]:** Do not change the semantics of file_sequence_number; add a latest_column_file_sequence_number field in the tracking struct instead. ([message](https://lists.apache.org/thread/ls3zkx9z95cb817831rqj9rkqzmwlyjn))
- **Gábor Kaszab:** After talking with Amogh, per-column-file status, sequence numbers and snapshot IDs are unnecessary; changes are detected by matching REPLACED and MODIFIED TrackedFile entries. ([message](https://lists.apache.org/thread/mc5yy979n3goh7jcxy3y041101zo935l))
- **Gábor Kaszab:** Leans toward keeping base file fields on TrackedFile rather than moving them into the column file list, to match the base file plus column files mental model. ([message](https://lists.apache.org/thread/008ocyp4k8jklqn8w0lt8pmh6y8m0pv2))

References: [iceberg#16285](https://github.com/apache/iceberg/issues/16285), [doc](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs), [doc](https://docs.google.com/document/d/160-FizR6zOASMb86NycfgCm7cZbh6HK7FLcUW8_Xp-0), [thread](https://lists.apache.org/thread/jbh1gbrso5h6l4by9rh9poy2cjjtb8j0), [video](https://www.youtube.com/watch?v=exC7RCDYtk4)
<!-- kb:generated:end -->

## Notes
