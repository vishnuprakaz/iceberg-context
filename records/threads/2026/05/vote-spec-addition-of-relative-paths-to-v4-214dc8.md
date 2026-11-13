---
id: thread/t-214dc89c07f6f226
type: thread
title: 'Vote: add relative paths to the v4 spec'
date: '2026-05-19'
url: https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n
kind: vote
status: passed
messages: 13
sources:
- devlist:dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n
refs:
- gh:apache/iceberg#15630
links:
- rel: started_by
  to: person/danielcweeks
  confidence: observed
updated: '2026-11-13'
---

# Vote: add relative paths to the v4 spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Spec: Addition of Relative Paths to v4](https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n) · **Started:** 2026-05-19 by [[person/danielcweeks|Daniel C. Weeks]] · **Messages:** 13 (last 2026-05-22) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Daniel Weeks started a vote to add relative paths to the v4 table spec as defined in PR #15630. He stated that the vote confirms the agreed direction for relative paths in v4 and that changes can still happen until the v4 spec is finalized. The vote ran for 72 hours. All replies were +1 votes; Anoop Johnson said the proposal is very useful for disaster recovery use cases, and one voter left a minor comment on the PR. Daniel Weeks closed the vote as passed with 7 binding and 12 non-binding +1 votes and no +0 or -1 votes, and said he would merge the PR so the implementation could be iterated on.

**Why it matters:** Relative paths are now part of the v4 spec direction, so v4 implementations need to resolve paths against the table location.

## Outcome

Passed with 7 binding and 12 non-binding +1 votes, and no +0 or -1 votes. The PR was to be merged. ([message](https://lists.apache.org/thread/g9t1mcb7qzbrb3wh64mfg07txg54roro), `devlist:g9t1mcb7qzbrb3wh64mfg07txg54roro`)

## Positions

- **[[person/danielcweeks|Daniel C. Weeks]]:** Add relative paths to the v4 spec; the vote confirms the direction while details can still change until v4 is finalized. ([message](https://lists.apache.org/thread/dqlgo3rmz1tnshx0bgk2cv4qm1h06k2n))
- **[[person/anoopj|Anoop Johnson]]:** Supports the change as very useful for disaster recovery use cases. ([message](https://lists.apache.org/thread/ykt65mov2zfql52jqlwyjmn8txs54j21))

References: [iceberg#15630](https://github.com/apache/iceberg/issues/15630)
<!-- kb:generated:end -->

## Notes
