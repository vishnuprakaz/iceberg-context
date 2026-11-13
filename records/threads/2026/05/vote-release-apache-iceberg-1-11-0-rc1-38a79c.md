---
id: thread/t-38a79cd7862dfb2b
type: thread
title: Release Apache Iceberg 1.11.0 RC1
date: '2026-05-13'
url: https://lists.apache.org/thread/oxdht2fxkg4l7mh60lfts09g12hx4lh8
kind: release-vote
status: withdrawn
messages: 4
sources:
- devlist:oxdht2fxkg4l7mh60lfts09g12hx4lh8
refs:
- gh:apache/iceberg#16303
- gh:apache/iceberg#16295
links:
- rel: started_by
  to: person/aihuaxu
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg 1.11.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.11.0 RC1](https://lists.apache.org/thread/oxdht2fxkg4l7mh60lfts09g12hx4lh8) · **Started:** 2026-05-13 by [[person/aihuaxu|Aihua Xu]] · **Messages:** 4 (last 2026-05-13) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This is a short exchange on the 1.11.0 RC1 vote thread; the first message from aihuaxu has no body in the collected data. kevinjqliu pointed out on a final check that a backport, PR 16303, had been opened that day. huaxingao noted that the original change, PR 16295, had been merged to main only. aihuaxu replied that although a new release candidate had been created the night before, it does not include the backport in PR 16303, which also seems to be needed for the previous Spark release. He said he would wait for the backport to merge and create a new release candidate later that day. No votes or result are recorded in these messages.

**Why it matters:** The 1.11.0 release needed another candidate to pick up a late backport.

## Outcome

The release manager said he would wait for backport PR 16303 to merge and create a new release candidate; no vote result is recorded. ([message](https://lists.apache.org/thread/bowjj9wwgdm9dw3myoxd29rtvqfloogl), `devlist:bowjj9wwgdm9dw3myoxd29rtvqfloogl`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** Flagged a late backport, PR 16303, on his final check of the release candidate. ([message](https://lists.apache.org/thread/d5c6jq39mstk0wtz0z7mljpnrnbjmkrf))
- **[[person/huaxingao|Huaxin Gao]]:** The original PR 16295 was merged to main only. ([message](https://lists.apache.org/thread/9rxlv9ol6g10nod93js142knltfn677x))
- **[[person/aihuaxu|Aihua Xu]]:** The new release candidate lacks the backport, which is also needed for the previous Spark version, so a further candidate will be created once it merges. ([message](https://lists.apache.org/thread/bowjj9wwgdm9dw3myoxd29rtvqfloogl))

References: [iceberg#16303](https://github.com/apache/iceberg/issues/16303), [iceberg#16295](https://github.com/apache/iceberg/issues/16295)
<!-- kb:generated:end -->

## Notes
