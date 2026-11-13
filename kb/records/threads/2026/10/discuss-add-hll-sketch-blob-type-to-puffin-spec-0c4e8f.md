---
id: thread/t-0c4e8f7ab63cfb6d
type: thread
title: Adding an HLL sketch blob type to the Puffin spec
date: '2026-10-21'
url: https://lists.apache.org/thread/vlcv3ft4mw0d3nzvgr6xg34p3zrq1xb7
kind: discuss
status: open
messages: 6
sources:
- devlist:vlcv3ft4mw0d3nzvgr6xg34p3zrq1xb7
refs:
- gh:apache/iceberg#18513
- gh:apache/iceberg#18516
- gh:trinodb/trino#31173
links:
- rel: started_by
  to: person/ebyhr
  confidence: observed
updated: '2026-11-13'
---

# Adding an HLL sketch blob type to the Puffin spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Add HLL sketch blob type to Puffin spec](https://lists.apache.org/thread/vlcv3ft4mw0d3nzvgr6xg34p3zrq1xb7) · **Started:** 2026-10-21 by [[person/ebyhr|Yuya Ebihara]] · **Messages:** 6 (last 2026-10-27) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Yuya Ebihara opened a PR (#18513) to add a standard HyperLogLog blob type, apache-datasketches-hll-v1, to the Puffin spec. Puffin currently defines only apache-datasketches-theta-v1 for NDV statistics, and Theta sketch computation causes a 10-20% slowdown on inserts in Trino. Trino is considering an HLL option, which without a standard type would have to be stored as an engine-specific blob that other engines cannot read. The new blob would hold a serialized compact Apache DataSketches HLL sketch built with the default seed from values in Iceberg's single-value serialization, with an optional ndv property as for Theta. Four replies were +1; Junwang Zhao (zhjwpku) added that HLL uses less memory and is faster for simple distinct counts. Raghvendra Yadav agreed with the motivation and asked what a reader should do when a table has both Theta and HLL blobs, since they cannot be unioned, and whether the blob metadata should record lgK. Those questions were not answered in the thread.

**Why it matters:** Without a standard HLL blob type, engines that avoid Theta sketches would write statistics other engines cannot read.

## Outcome

No decision. Replies supported the proposal; questions about mixing Theta and HLL blobs and recording lgK were left unanswered.

## Positions

- **Yuya Ebihara:** Puffin should define a standard apache-datasketches-hll-v1 blob type so engines that prefer HLL can write NDV sketches that other engines can read. ([message](https://lists.apache.org/thread/vlcv3ft4mw0d3nzvgr6xg34p3zrq1xb7))
- **[[person/zhjwpku|Junwang Zhao]]:** HLL should be supported because it uses less memory and is faster for simple distinct counts. ([message](https://lists.apache.org/thread/gs6m32hhn75nzfr7yczkq7n5138dpjkr))
- **Raghvendra Yadav:** The spec should say how readers handle tables that mix Theta and HLL blobs, which cannot be merged, and should consider recording lgK in the blob metadata. ([message](https://lists.apache.org/thread/g703rcys0gdokpwp0m5f4n70wjv07gxp))

References: [iceberg#18513](https://github.com/apache/iceberg/issues/18513), [iceberg#18516](https://github.com/apache/iceberg/issues/18516), [trino#31173](https://github.com/trinodb/trino/issues/31173)
<!-- kb:generated:end -->

## Notes
