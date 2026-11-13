---
id: thread/t-85a04b03334ef096
type: thread
title: Move iceberg-datafusion to Apache DataFusion
date: '2026-09-09'
url: https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s
kind: vote
status: passed
messages: 19
sources:
- devlist:ytb9x7x8ff3b7031kcrc05nzjtmh091s
refs:
- gh:apache/datafusion-iceberg#1
- list:pk4yqd4llr85lmq3gskbfl9v31sfqpp9
- list:6k5lws31c61y1lx2s34pxo4lmc7334lr
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:ytb9x7x8ff3b7031kcrc05nzjtmh091s
- rel: started_by
  to: person/kevinjqliu
  confidence: observed
updated: '2026-11-13'
---

# Move iceberg-datafusion to Apache DataFusion

<!-- kb:generated:start -->
**Thread:** [[VOTE] Move iceberg-datafusion to Apache DataFusion](https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s) · **Started:** 2026-09-09 by [[person/kevinjqliu|Kevin Liu]] · **Messages:** 19 (last 2026-09-14) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

kevinjqliu started the Iceberg-side vote to move the iceberg-datafusion integration from apache/iceberg-rust to apache/datafusion-iceberg under the Apache DataFusion project, following an earlier discussion thread. He argued the move makes it easier for contributors familiar with DataFusion to maintain and improve the integration while keeping it under Apache governance. A PR porting the code and its history had been prepared, and a corresponding vote was running on the DataFusion dev list; the migration would proceed if both communities approved. Xuanwo added that the move gives DataFusion contributors a natural place to maintain the integration. No objections were raised and the vote passed.

**Why it matters:** The DataFusion integration for Iceberg leaves the iceberg-rust repository, so contributions to it will go to apache/datafusion-iceberg.

## Outcome

Passed with 17 +1 votes (5 binding, 12 non-binding) and no +0 or -1 votes. The migration goes ahead if the DataFusion community's parallel vote also approves. ([message](https://lists.apache.org/thread/f21t4f8t8mx6pjjb9ojnszsbln0z5hr6), `devlist:f21t4f8t8mx6pjjb9ojnszsbln0z5hr6`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** Moving the integration to Apache DataFusion makes it easier for DataFusion contributors to maintain and improve it while keeping it under Apache governance. ([message](https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s))
- **[[person/Xuanwo|Hao Ding]]:** Supports the move because it gives DataFusion contributors a natural place to maintain the integration. ([message](https://lists.apache.org/thread/8r9xk97c7ychy5tfms0gcqsvm8tfmr4t))

References: [datafusion-iceberg#1](https://github.com/apache/datafusion-iceberg/issues/1), [thread](https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9), [thread](https://lists.apache.org/thread/6k5lws31c61y1lx2s34pxo4lmc7334lr)
<!-- kb:generated:end -->

## Notes
