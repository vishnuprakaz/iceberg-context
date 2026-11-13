---
id: thread/t-bacc923f0d0a8d51
type: thread
title: Vote on clarifying the day partition transform result type as date in the spec
date: '2026-06-11'
url: https://lists.apache.org/thread/gz432tvboxvno2v7g3l17c8tbtxckxrb
kind: vote
status: open
messages: 8
sources:
- devlist:gz432tvboxvno2v7g3l17c8tbtxckxrb
refs:
- gh:apache/iceberg#16446
- gh:apache/iceberg#16414
- gh:apache/iceberg-go#1176
- list:wnhvdmwc3b1dxc2ogk7po682pky12cps
links:
- rel: started_by
  to: person/laskoviymishka
  confidence: observed
updated: '2026-11-13'
---

# Vote on clarifying the day partition transform result type as date in the spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Clarify day partition transform result type as date in the spec](https://lists.apache.org/thread/gz432tvboxvno2v7g3l17c8tbtxckxrb) · **Started:** 2026-06-11 by [[person/laskoviymishka|Andrei Tserakhau]] · **Messages:** 8 (last 2026-06-11) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Andrei Tserakhau called a vote on the spec clarification in PR #16446. It changes the `day` partition transform's result type in the transform table from `int` to `date`, matching what Java, PyIceberg, Rust and C++ already write in manifests (the Avro `date` logical type), and adds a note that readers must also accept plain `int` values, read as days since 1970-01-01. He described it as a clarification with no behavioral change: the physical 4-byte day count is unchanged and no existing manifests are affected. The ambiguity had come up repeatedly, most recently as an interop failure in iceberg-go. A vote was held because changes under `format/` require one. All eight votes on the first day were +1. Russell Spitzer added that a vote was not really needed and that the PR mainly needs more committer approvals. No result message appears in the thread.

**Why it matters:** Implementations get an unambiguous rule for the day transform: write `date`, and accept `int` when reading.

## Outcome

No result is announced in the thread. Votes cast were all +1: five binding and three non-binding, including the proposer's.

## Positions

- **[[person/laskoviymishka|Andrei Tserakhau]]:** The spec should state `date` as the result type of the `day` transform and require readers to also accept plain `int`, documenting what implementations already do. ([message](https://lists.apache.org/thread/gz432tvboxvno2v7g3l17c8tbtxckxrb))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Votes +1 (binding) and considers a vote unnecessary since this is existing behavior; the PR needs more committer approvals. ([message](https://lists.apache.org/thread/3p9gxcv2p2z8bc6r4991fjvsnp5gtr7f))

References: [iceberg#16446](https://github.com/apache/iceberg/issues/16446), [iceberg#16414](https://github.com/apache/iceberg/issues/16414), [iceberg-go#1176](https://github.com/apache/iceberg-go/issues/1176), [thread](https://lists.apache.org/thread/wnhvdmwc3b1dxc2ogk7po682pky12cps)
<!-- kb:generated:end -->

## Notes
