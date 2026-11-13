---
id: thread/t-cbe85b13658ba33b
type: thread
title: Release Apache Iceberg C++ 0.3.0
date: '2026-05-26'
url: https://lists.apache.org/thread/3vdtx3m4xbcw5htj246yhjt6wrc5rjo8
kind: release-planning
status: consensus
messages: 9
sources:
- devlist:3vdtx3m4xbcw5htj246yhjt6wrc5rjo8
refs:
- gh:apache/iceberg-cpp#523
links:
- rel: discussed
  to: initiative/iceberg-cpp
  confidence: extracted
  source: devlist:3vdtx3m4xbcw5htj246yhjt6wrc5rjo8
- rel: started_by
  to: person/zhjwpku
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg C++ 0.3.0

<!-- kb:generated:start -->
**Thread:** [[DISCUSS][C++] Release Apache Iceberg C++ 0.3.0](https://lists.apache.org/thread/3vdtx3m4xbcw5htj246yhjt6wrc5rjo8) · **Started:** 2026-05-26 by [[person/zhjwpku|Junwang Zhao]] · **Messages:** 9 (last 2026-06-04) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zhjwpku proposed releasing Apache Iceberg C++ 0.3.0 without waiting for every item on the roadmap issue, since 114 commits had landed since 0.2.0 in January 2026. Completed work includes REST catalog authentication (no-op, basic, initial OAuth2), snapshot management and expire-snapshots cleanup, incremental append and changelog scans, data and delete file writers with merge-on-read reading, S3 and streaming FileIO, nanosecond timestamp types, Puffin basics, and writer metrics. Guotao Yu asked for a one to two week delay so that merging update support, including overwrite, could land; wgtmac agreed overwrite should be included and zhjwpku agreed to extend the window. On June 3 zhjwpku reported the feature was merged, volunteered as release manager, planned to send the vote by the end of that week, and asked committers for help with parts of the process since he lacks commit rights.

**Why it matters:** Defines the scope of iceberg-cpp 0.3.0, including overwrite support added before the release was cut.

## Outcome

The release waited for overwrite support, which merged; zhjwpku volunteered as release manager and planned to start the 0.3.0 vote by the end of the week of June 3. ([message](https://lists.apache.org/thread/22t5j4wgfghqzgm6ds5xk5fwmt2rogph), `devlist:22t5j4wgfghqzgm6ds5xk5fwmt2rogph`)

## Positions

- **[[person/zhjwpku|Junwang Zhao]]:** Release 0.3.0 now with the substantial completed work rather than waiting for every roadmap item, and carry the remainder to the next release. ([message](https://lists.apache.org/thread/3vdtx3m4xbcw5htj246yhjt6wrc5rjo8))
- **Guotao Yu:** Delay the release by one to two weeks so overwrite support can land and round out the write story. ([message](https://lists.apache.org/thread/fpk1o87p6ysbtc720x7v3mmnn0844m8m))
- **[[person/wgtmac|Gang Wu]]:** At least overwrite support should be included in 0.3.0. ([message](https://lists.apache.org/thread/7h8fkw2kl20995vg3osv6l18ollnntkq))

References: [iceberg-cpp#523](https://github.com/apache/iceberg-cpp/issues/523)
<!-- kb:generated:end -->

## Notes
