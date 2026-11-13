---
id: thread/t-3aecd28f8883bc90
type: thread
title: Cross-implementation conformance testing for Iceberg
date: '2026-06-29'
url: https://lists.apache.org/thread/h21x5r8bfrv3zg700y9py84plrfmtmsr
kind: discuss
status: open
messages: 4
sources:
- devlist:h21x5r8bfrv3zg700y9py84plrfmtmsr
refs:
- list:964630c6q0jovs579x1jzb1t0o19jgjg
- gh:sungwy/iceberg-testing#1
- gh:apache/iceberg#16414
- gh:apache/iceberg-go#880
links:
- rel: started_by
  to: person/sungwy
  confidence: observed
updated: '2026-11-13'
---

# Cross-implementation conformance testing for Iceberg

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Cross-implementation conformance testing for Iceberg](https://lists.apache.org/thread/h21x5r8bfrv3zg700y9py84plrfmtmsr) · **Started:** 2026-06-29 by [[person/sungwy|Sung Yun]] · **Messages:** 4 (last 2026-06-30) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Replies to Neelesh Salian's write-up on conformance testing across Iceberg implementations. Sung (sungwy) said his own parallel proposal is substantially the same, differing on repository layout and integration plan, and asked to merge the two documents and bring one proposal back for lazy consensus; he wants contribution guides, a submodule-based integration with each implementation pinning the fixture repository, and a CI integration plan folded in. Tanmay Rauth backed comparing decoded values and suggested fixtures structured as input, golden file and expected value so they serve read and write tests. Andrei Tserakhau agreed and refined the rule: normalize representation where the spec leaves it open, but keep the physical type where the spec pins one. Neelesh Salian reported that he, Sung, Andrei and Amogh are preparing a joint proposal and supported a community sync.

**Why it matters:** A single shared-fixture conformance proposal is being prepared, which would change how each implementation tests spec behavior in CI.

## Outcome

The authors of the two proposals are merging them offline and plan to share one proposal and hold a community sync; nothing was decided in these messages.

## Positions

- **[[person/sungwy|Sung Yun]]:** The two proposals are substantially the same and should be converged into one, including contribution guides, submodule-based pinning of the fixture repository and per-implementation CI integration. ([message](https://lists.apache.org/thread/h21x5r8bfrv3zg700y9py84plrfmtmsr))
- **[[person/tanmayrauth|Tanmay Rauth]]:** Comparing decoded values is right, and fixtures should be structured as input, golden file and expected value from the start so the same fixture covers reads and writes. ([message](https://lists.apache.org/thread/69xxw3j3xfwk8h03gsd4vjhrhdxptb1l))
- **[[person/nssalian|Neelesh Salian]]:** The proposers are working offline on a single proposal to share with the group, and a community sync is worthwhile. ([message](https://lists.apache.org/thread/skk2hfx6mh9o898l0jhwyroxvh02tm5c))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Comparison must be spec-semantic: normalize where the spec leaves representation open, as for the day transform, but keep the physical type where the spec pins it, as for equality_ids; fixtures will be bidirectional from v1. ([message](https://lists.apache.org/thread/5psp1347y4cjmstwjg0q65ldxjnycmy8))

References: [thread](https://lists.apache.org/thread/964630c6q0jovs579x1jzb1t0o19jgjg), [iceberg-testing#1](https://github.com/sungwy/iceberg-testing/issues/1), [iceberg#16414](https://github.com/apache/iceberg/issues/16414), [iceberg-go#880](https://github.com/apache/iceberg-go/issues/880)
<!-- kb:generated:end -->

## Notes
