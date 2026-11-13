---
id: thread/t-9b4ac94de3e00827
type: thread
title: 'Iceberg Variant: tracking document and sync proposal'
date: '2026-04-19'
url: https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l
kind: discuss
status: informational
messages: 12
sources:
- devlist:f8l27lr55nlrdg4qwno29r796d4v2p8l
refs:
- gh:apache/iceberg#10392
- doc:1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s
links:
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Iceberg Variant: tracking document and sync proposal

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg Variant - Tracking Document & Sync Proposal](https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l) · **Started:** 2026-04-19 by [[person/nssalian|Neelesh Salian]] · **Messages:** 12 (last 2026-11-05) · **Outcome:** informational

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Neelesh Salian shared a community tracking document for Variant work across Iceberg, Spark, Parquet and Flink, with an overview, a tracker of open issues and PRs, and a benchmarks tab. He summarized three independent benchmarks as showing variant reads 1.1 to 1.7 times faster than JSON strings but 15 to 17 times slower than typed columns, and proposed a monthly Variant sync. Steve Loughran welcomed the tracker and asked about cross-implementation interoperability testing, handling of invalid data, duplicate keys and sorted fields. The sync was set up for the first Thursday of each month starting May 7, 2026, and notes and recordings were posted to the thread for the May through September meetings. In November Neelesh updated the document with next milestones and cancelled the December call, with the sync resuming in January 2027.

**Why it matters:** The tracking document and monthly sync are the places to follow and coordinate Variant work across Iceberg, Parquet and Spark.

## Outcome

A monthly Variant sync was set up on the first Thursday of each month from May 7, 2026, with notes kept in the tracking document; the December 2026 call was cancelled. ([message](https://lists.apache.org/thread/812zf11xfoh78cp60xlrrzsnp25dno7w), `devlist:812zf11xfoh78cp60xlrrzsnp25dno7w`)

## Positions

- **[[person/nssalian|Neelesh Salian]]:** Variant work spans several projects and needs a single tracking document and its own monthly sync. ([message](https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l))
- **[[person/steveloughran|Steve Loughran]]:** Supports the cross-project tracker and asks whether variant implementations have been cross-tested, including consistent handling of invalid data. ([message](https://lists.apache.org/thread/j2g224gstxk77npgjldtn8g1ff4m30j6))
- **[[person/steveloughran|Steve Loughran]]:** Wants status from the Rust, Go and C++ implementations and raises sorted fields, duplicate keys and malformed shredded files as cases to test. ([message](https://lists.apache.org/thread/5yptv4w53nonlxrondovjl9dj8nmnytc))

References: [iceberg#10392](https://github.com/apache/iceberg/issues/10392), [doc](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)
<!-- kb:generated:end -->

## Notes
