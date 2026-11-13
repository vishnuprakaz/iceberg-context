---
id: thread/t-e3df87d32bc07907
type: thread
title: 'Vote: deprecate equality deletes in Iceberg V4 (forbid new writes)'
date: '2026-08-13'
url: https://lists.apache.org/thread/5x8ovvz3ppf4krqs543sqjcy3dqdhthm
kind: vote
status: passed
messages: 28
sources:
- devlist:5x8ovvz3ppf4krqs543sqjcy3dqdhthm
refs:
- list:ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
links:
- rel: started_by
  to: person/huaxingao
  confidence: observed
updated: '2026-11-13'
---

# Vote: deprecate equality deletes in Iceberg V4 (forbid new writes)

<!-- kb:generated:start -->
**Thread:** [[VOTE] Deprecate equality deletes in Iceberg V4 (forbid new writes)](https://lists.apache.org/thread/5x8ovvz3ppf4krqs543sqjcy3dqdhthm) · **Started:** 2026-08-13 by [[person/huaxingao|Huaxin Gao]] · **Messages:** 28 (last 2026-08-18) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

huaxingao called a vote on the V4 table spec following the earlier discussion thread. The proposal has three parts: writing new equality deletes is forbidden for V4 tables, since V4 metadata will not define them as an allowed entry type; reading equality deletes stays supported in the reference implementation for V2/V3 tables and for deletes carried into upgraded V4 tables; and upgrading a V2/V3 table to V4 is metadata-only, with conversion to deletion vectors left as a separate, optional maintenance action. The rationale given is the cost equality deletes impose on every read and the features they block, such as CDC, row lineage and incremental index and materialized view maintenance. manuzhang asked whether the upgrade needs a manifest rewrite; huaxingao answered that the V4 root manifest references existing V2/V3 manifests as they are. The vote passed with no +0 or -1 votes.

**Why it matters:** V4 writers may not produce equality deletes, so engines that rely on them, such as streaming upserts, need a deletion-vector based path for V4 tables.

## Outcome

The vote passed with 7 binding +1 votes and 17 non-binding +1 votes, and no 0 or -1 votes. ([message](https://lists.apache.org/thread/y4ggjzfh8s9n80w16j857og3800xd3lv), `devlist:y4ggjzfh8s9n80w16j857og3800xd3lv`)

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** Forbid new equality deletes in V4 while keeping reads and a metadata-only upgrade; carried-over deletes are applied on read until they age off or are converted to deletion vectors. ([message](https://lists.apache.org/thread/nycwjpozbdo89k55277q7rqjw98k6b42))
- **[[person/manuzhang|Manu Zhang]]:** Asked whether upgrading a V2/V3 table to V4 requires a manifest rewrite and how it would be handled. ([message](https://lists.apache.org/thread/j8qsr6dwt6m1zlrrx67fycrdnynbhlhl))
- **[[person/GGraziadei|Gianluca Graziadei]]:** Supports the change because equality deletes shift an unbounded cost onto every reader, and the metadata-only upgrade decouples V4 adoption from delete file migration. ([message](https://lists.apache.org/thread/fpx3smwo90gr8jnkh4b4q666b4gphscj))

References: [thread](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)
<!-- kb:generated:end -->

## Notes
