---
id: thread/t-709611fe90159e57
type: thread
title: AI Functions for FILE/VECTOR types
date: '2026-11-02'
url: https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b
kind: discuss
status: open
messages: 4
sources:
- devlist:zv614sbcz0doshl4xpddpcj3oolfgo3b
refs: []
links:
- rel: started_by
  to: person/rambleraptor
  confidence: observed
updated: '2026-11-13'
---

# AI Functions for FILE/VECTOR types

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] AI Functions for FILE/VECTOR types](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b) · **Started:** 2026-11-02 by [[person/rambleraptor|Alex Stephen]] · **Messages:** 4 (last 2026-11-09) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alex Stephen proposed adding a generative AI function and an AI embedding function to the Iceberg Spark and Flink connectors, as part of the work on the FILE and VECTOR types, so users have vendor-agnostic functions for multimodal data and embeddings; a proposal document is linked. Russell Spitzer said he did not understand the goal and was hesitant, since each engine's API would likely have engine-specific parts beyond function names and arguments. Stephen clarified that he wants to learn whether the community is interested in shipping SQL functions in the Iceberg codebase, either built into the connectors or as default UDFs under the UDF spec. Szehon Ho preferred not to standardize AI functions and to use the existing function and UDF mechanisms. The thread stops there.

**Why it matters:** It tests whether Iceberg should ship or standardize SQL functions beyond partition transforms, and the first replies leaned against it.

## Outcome

Two replies questioned or opposed the proposal and the proposer acknowledged it may not fit the project; no decision was reached.

## Positions

- **[[person/rambleraptor|Alex Stephen]]:** Add a generative AI function and an AI embedding function to the Iceberg Spark and Flink connectors as vendor-agnostic functions for multimodal data. ([message](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The goal and use case are unclear, because each engine's API would likely contain engine-specific elements beyond function names and arguments. ([message](https://lists.apache.org/thread/j7sggw14p560mgnhp8tm31h2ypl5phn8))
- **[[person/rambleraptor|Alex Stephen]]:** The question is whether the community wants SQL functions shipped in the Iceberg codebase, either built into the connectors or as default UDFs that engines implement under the UDF spec. ([message](https://lists.apache.org/thread/4kr518oookg35bnpds5skxv0y1srjy8r))
- **[[person/szehon-ho|Szehon Ho]]:** AI functions should not be standardized in the Iceberg expression spec, which is deliberately small; existing function and UDF mechanisms should be used unless there is a clear Iceberg-specific need. ([message](https://lists.apache.org/thread/pvgqm0r4m1yy43do8k4sflzryoobgwmr))
<!-- kb:generated:end -->

## Notes
