---
id: thread/t-8a1d2c357afe958e
type: thread
title: Variant shredding policy across Iceberg implementations
date: '2026-06-04'
url: https://lists.apache.org/thread/ztrygfd46607pns9t2d4hs0x95595cb2
kind: discuss
status: open
messages: 4
sources:
- devlist:ztrygfd46607pns9t2d4hs0x95595cb2
refs:
- doc:1OaB45mg9JJ_JRg-ipuvyh4AtOmaGmdWMsy_mJKiu5xs
- doc:1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s
links:
- rel: discussed
  to: initiative/variant
  confidence: extracted
  source: devlist:ztrygfd46607pns9t2d4hs0x95595cb2
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Variant shredding policy across Iceberg implementations

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Variant Shredding Policy Across Iceberg Implementations](https://lists.apache.org/thread/ztrygfd46607pns9t2d4hs0x95595cb2) · **Started:** 2026-06-04 by [[person/nssalian|Neelesh Salian]] · **Messages:** 4 (last 2026-07-25) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Neelesh Salian proposed a shared policy for variant shredding, since shredding writers exist in iceberg-java, arrow-go and arrow-rs and are landing in iceberg-go, iceberg-rust and later PyIceberg, with no agreement yet on whether to shred, how the layout is declared and how it is expressed so that implementations produce compatible output. The planned steps were community review, a vote, adjustments in the Java implementation, and then the other implementations aligning. After the Variant sync, he reported that the proposal should instead focus on agreeing on the best inference algorithm for shredding, backed by data and testing. On July 25th he shared an update: he benchmarked a set of inference strategies, the proposal now contains the resulting inference algorithm, and the tunable thresholds move from constants to table properties. He asked for further review; no vote has been started in the thread.

**Why it matters:** The outcome would decide how every Iceberg writer chooses which variant fields to shred, which affects cross-implementation consistency.

## Outcome

The updated proposal with a benchmarked inference algorithm is out for review; no vote has been called.

## Positions

- **[[person/nssalian|Neelesh Salian]]:** Implementations need one shared shredding policy; after feedback it centres on a benchmarked inference algorithm with thresholds exposed as table properties. ([message](https://lists.apache.org/thread/8rbkjzs59ycq442o1v4bpkzftwkr62ol))

References: [doc](https://docs.google.com/document/d/1OaB45mg9JJ_JRg-ipuvyh4AtOmaGmdWMsy_mJKiu5xs), [doc](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)
<!-- kb:generated:end -->

## Notes
