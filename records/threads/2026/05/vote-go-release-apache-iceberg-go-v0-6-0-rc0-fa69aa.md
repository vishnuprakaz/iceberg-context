---
id: thread/t-fa69aa12d0302acd
type: thread
title: 'Vote: release Apache Iceberg Go v0.6.0 RC0'
date: '2026-05-18'
url: https://lists.apache.org/thread/yvf1ywkwwdw3f28b7xskqt2y0hsmtv2l
kind: release-vote
status: withdrawn
messages: 10
sources:
- devlist:yvf1ywkwwdw3f28b7xskqt2y0hsmtv2l
refs:
- gh:apache/iceberg-go#932
- gh:apache/iceberg-go#1102
links:
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Vote: release Apache Iceberg Go v0.6.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE][Go] Release Apache Iceberg Go v0.6.0 RC0](https://lists.apache.org/thread/yvf1ywkwwdw3f28b7xskqt2y0hsmtv2l) · **Started:** 2026-05-18 by [[person/zeroshade|Matthew Topol]] · **Messages:** 10 (last 2026-05-21) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zeroshade proposed release candidate RC0 of Apache Iceberg Go v0.6.0, based on commit 53fa29cc, and asked for verification and votes. Several +1 votes followed with verification details. nssalian voted +1 but suggested another RC could include Variant non-shredding support from iceberg-go PR #932. kevinjqliu first hit a verification failure that turned out to be a test failing because he was logged in to the az CLI, then voted +1 binding. Tobias voted -1 (non-binding) because a commit made iceberg-go write a deprecated manifest field (distinct_counts) that PyIceberg rejects when reading, a regression in compatibility; iceberg-go PR #1102 would fix it. zeroshade agreed that PyIceberg compatibility must not break and said he would merge the fix and cut a new RC, so this candidate was not released.

**Why it matters:** A release candidate was dropped because manifests written by iceberg-go could no longer be read by PyIceberg, showing cross-implementation compatibility is treated as release-blocking.

## Outcome

The release manager said he would merge the PyIceberg compatibility fix and cut a new RC. Before that the thread had 1 binding +1, 4 non-binding +1 and 1 non-binding -1. ([message](https://lists.apache.org/thread/37qrc24fr5l0dolr11yqpny3qf8l2oln), `devlist:37qrc24fr5l0dolr11yqpny3qf8l2oln`)

## Positions

- **[[person/nssalian|Neelesh Salian]]:** The RC is good to go, though cutting another RC with Variant non-shredding support would be preferable if PR #932 merges soon. ([message](https://lists.apache.org/thread/99ckwlm11fbzsfobq08m247nb9hhf50m))
- **Tobias:** Do not release: a commit made iceberg-go write a deprecated field that PyIceberg rejects, breaking compatibility that existed before. ([message](https://lists.apache.org/thread/jt617254r2bs1hl5vb8yvxflkt7jrt6w))
- **[[person/zeroshade|Matthew Topol]]:** PyIceberg compatibility must not be broken, so the fix will be merged and a new RC cut. ([message](https://lists.apache.org/thread/37qrc24fr5l0dolr11yqpny3qf8l2oln))

References: [iceberg-go#932](https://github.com/apache/iceberg-go/issues/932), [iceberg-go#1102](https://github.com/apache/iceberg-go/issues/1102)
<!-- kb:generated:end -->

## Notes
