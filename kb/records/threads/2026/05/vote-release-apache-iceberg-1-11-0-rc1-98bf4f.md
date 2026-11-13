---
id: thread/t-98bf4fbbbb6c143a
type: thread
title: Vote on releasing Apache Iceberg 1.11.0 RC1
date: '2026-05-11'
url: https://lists.apache.org/thread/j83qwbv8vplqcx7b298toxmbrbckvprf
kind: release-vote
status: no-conclusion
messages: 7
sources:
- devlist:j83qwbv8vplqcx7b298toxmbrbckvprf
refs:
- gh:apache/iceberg#16283
- gh:apache/iceberg#16284
- gh:apache/iceberg#16263
- gh:apache/iceberg#16258
- gh:apache/iceberg#15470
- gh:apache/iceberg#16306
- gh:apache/iceberg#16307
- gh:apache/iceberg#16308
- gh:apache/iceberg#16311
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:j83qwbv8vplqcx7b298toxmbrbckvprf
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:j83qwbv8vplqcx7b298toxmbrbckvprf
- rel: started_by
  to: person/ajayky-os
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg 1.11.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.11.0 RC1](https://lists.apache.org/thread/j83qwbv8vplqcx7b298toxmbrbckvprf) · **Started:** 2026-05-11 by [[person/ajayky-os|Ajay Yadav]] · **Messages:** 7 (last 2026-05-13) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

These messages from the 1.11.0 RC1 vote thread cover fixes wanted before the next candidate. Ajay (ajayky-os) reported a performance regression in Spark queries on cloud storage: SerializableFileIOWithSize drops the file length, causing extra metadata calls, with a fix in a PR. Kevin Liu said the issues raised in the thread (first row ID, analyticscore, SerializableFileIOWithSize) were resolved and the 1.11.0 milestone complete, and proposed backporting several PRs to Spark 3.4 since 1.11 is its last release. Release manager Aihua (aihuaxu) wanted to cut the next candidate without waiting. Manu (manuzhang) argued for the backports, and Huaxin (huaxingao) asked to include a rewriteTablePath correctness fix. Kevin Liu opened four backport PRs; three were merged and the last awaited CI.

**Why it matters:** It shows which fixes and Spark 3.4 backports were pulled into 1.11.0, the last release to support Spark 3.4.

## Outcome

These messages do not state a result for the RC1 vote. The reported blockers were fixed, three of four Spark 3.4 backport PRs were merged and the fourth awaited CI, with a further release candidate planned.

## Positions

- **[[person/ajayky-os|Ajay Yadav]]:** The SerializableFileIOWithSize regression, which drops file length and causes excess metadata calls on cloud storage, should be fixed in 1.11.0. ([message](https://lists.apache.org/thread/j83qwbv8vplqcx7b298toxmbrbckvprf))
- **[[person/kevinjqliu|Kevin Liu]]:** The reported blockers are resolved; as an optional step, PRs missing from Spark 3.4 should be backported because this is the last release supporting it. ([message](https://lists.apache.org/thread/lcss3p2jg5qmf15hdnwww3tv0b9dfj8c))
- **[[person/aihuaxu|Aihua Xu]]:** The backports are not blocking and Spark 3.4 is deprecated, so the next RC should be cut now and the backports added only if another RC is needed. ([message](https://lists.apache.org/thread/6glvdyfnchbol0wrs13r0p5x27oorfdt))
- **[[person/huaxingao|Huaxin Gao]]:** The fix for stale file_size_in_bytes of rewritten position delete files in rewriteTablePath is a correctness issue that should go into 1.11. ([message](https://lists.apache.org/thread/2y1f7tf4qwv50trn459w7nbvbzgy17wq))
- **[[person/manuzhang|Manu Zhang]]:** Since Spark 3.4 is dropped after 1.11.0, the backports should go in so it is not left in a broken state. ([message](https://lists.apache.org/thread/g32677sb5tx9x4gkvphbko3owkvz0ybj))

References: [iceberg#16283](https://github.com/apache/iceberg/issues/16283), [iceberg#16284](https://github.com/apache/iceberg/issues/16284), [iceberg#16263](https://github.com/apache/iceberg/issues/16263), [iceberg#16258](https://github.com/apache/iceberg/issues/16258), [iceberg#15470](https://github.com/apache/iceberg/issues/15470), [iceberg#16306](https://github.com/apache/iceberg/issues/16306), [iceberg#16307](https://github.com/apache/iceberg/issues/16307), [iceberg#16308](https://github.com/apache/iceberg/issues/16308), [iceberg#16311](https://github.com/apache/iceberg/issues/16311)
<!-- kb:generated:end -->

## Notes
