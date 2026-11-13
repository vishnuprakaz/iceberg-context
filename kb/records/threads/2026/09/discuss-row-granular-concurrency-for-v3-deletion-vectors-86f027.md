---
id: thread/t-86f027bbab8fd9e0
type: thread
title: Row-granular concurrency for V3 deletion vectors
date: '2026-09-08'
url: https://lists.apache.org/thread/7w74dtgd0mjd0hl4gnvqkc33l31hxznw
kind: discuss
status: open
messages: 5
sources:
- devlist:7w74dtgd0mjd0hl4gnvqkc33l31hxznw
refs:
- gh:apache/iceberg#18020
- gh:apache/iceberg#17754
- gh:apache/iceberg#14613
- gh:apache/iceberg#15006
- gh:trinodb/trino#30860
links: []
updated: '2026-11-13'
---

# Row-granular concurrency for V3 deletion vectors

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Row-granular concurrency for V3 deletion vectors](https://lists.apache.org/thread/7w74dtgd0mjd0hl4gnvqkc33l31hxznw) · **Started:** 2026-09-08 by EJ Song · **Messages:** 5 (last 2026-10-13) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

EJ Song proposed making concurrent UPDATE and MERGE on V3 tables fail less often. Today validateAddedDVs fails a commit when a concurrent operation added a deletion vector for the same data file, even if the deleted positions do not overlap, and that ValidationException is not retried, so the whole operation is recomputed. The proposal refines the check to position granularity: if the newly deleted positions are disjoint, union the two DVs and proceed; otherwise fail as today. The design is in issue #18020. Xiening Dai (xndai) supported the idea and favored retrying the commit. Huaxin Gao supported it, suggested gating it under a table property because it adds driver-side I/O during commit, preferred doing the union in the validation path, and listed prior art. Song agreed on the validation path and argued the bitmap tier needs no property, only a later tier that reads data files. In October Song reported that the first step, merging concurrent DVs for pure delete commits (#17754), is reviewed and needs a second committer.

**Why it matters:** If adopted, concurrent row-level operations that touch different rows of the same data file would no longer force one of them to be recomputed.

## Outcome

The direction was supported by the two repliers. PR #17754 for pure delete commits awaits a second committer review; the position-overlap check for UPDATE and MERGE is the next step and its design is open for feedback in issue #18020. ([message](https://lists.apache.org/thread/qms426sxl3r1hjdm0jzm5wwqbkhdx01o), `devlist:qms426sxl3r1hjdm0jzm5wwqbkhdx01o`)

## Positions

- **EJ Song:** validateAddedDVs should compare deleted positions and union disjoint concurrent DVs instead of failing at file granularity. ([message](https://lists.apache.org/thread/7w74dtgd0mjd0hl4gnvqkc33l31hxznw))
- **[[person/xndai|Xiening Dai]]:** Finer-grained conflict resolution is a good idea, and the commit should be retried until it succeeds or hits a conflict that cannot be resolved. ([message](https://lists.apache.org/thread/zv97474lxrznp1mw7mqcvyn8bq7d8rsd))
- **[[person/huaxingao|Huaxin Gao]]:** The change is worth doing, should be gated under a table property because of the added commit-time I/O, and the union belongs in the validation path rather than a retry loop. ([message](https://lists.apache.org/thread/yn0c0495s6tqrx3ns0g39gon5n5vyco9))
- **EJ Song:** The union should happen in the validation path, and a table property is only needed for a later tier that reads data files, since the bitmap check reads nothing for commits on disjoint files. ([message](https://lists.apache.org/thread/xgh1tysy4tghld966619v30419nzcc1z))

References: [iceberg#18020](https://github.com/apache/iceberg/issues/18020), [iceberg#17754](https://github.com/apache/iceberg/issues/17754), [iceberg#14613](https://github.com/apache/iceberg/issues/14613), [iceberg#15006](https://github.com/apache/iceberg/issues/15006), [trino#30860](https://github.com/trinodb/trino/issues/30860)
<!-- kb:generated:end -->

## Notes
