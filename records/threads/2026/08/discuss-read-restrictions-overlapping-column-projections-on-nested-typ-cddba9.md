---
id: thread/t-cddba95ff30a75d7
type: thread
title: 'Read Restrictions: overlapping column projections on nested types'
date: '2026-08-04'
url: https://lists.apache.org/thread/zh25o2msbjw3skd577qzsyrcorobcthz
kind: discuss
status: no-conclusion
messages: 7
sources:
- devlist:zh25o2msbjw3skd577qzsyrcorobcthz
refs:
- gh:apache/iceberg#13879
links:
- rel: started_by
  to: person/singhpk234
  confidence: observed
updated: '2026-11-13'
---

# Read Restrictions: overlapping column projections on nested types

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Read Restrictions: overlapping column projections on nested types](https://lists.apache.org/thread/zh25o2msbjw3skd577qzsyrcorobcthz) · **Started:** 2026-08-04 by [[person/singhpk234|Prashant Singh]] · **Messages:** 7 (last 2026-08-07) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Prashant (singhpk234) raised the last open item on the Read Restrictions spec PR (#13879) before a vote: what a client should do when a catalog returns one column projection on a nested container (struct, list or map) and another on a field beneath it. Option A, the current PR text, forbids the overlap and requires a reader to fail the query; option B defines a precedence such as outer-most wins. Prashant, Sung, Steven (stevenzwu) and Nevin Zheng favoured A, citing diverging behaviour across BigQuery, Redshift and other systems and arguing the rule can be relaxed later. Dan Weeks disagreed that relaxing a MUST NOT is backward compatible, since older validating clients would break, and wanted an application order defined now, along with a reference implementation. Steven suggested a later relaxation could use MAY wording. The thread ends without agreement.

**Why it matters:** This is the last open item before the Read Restrictions REST spec change goes to a vote.

## Outcome

Four participants favoured forbidding overlapping nested projections with fail-closed readers; Dan Weeks objected on backward-compatibility grounds and asked for precedence to be defined now. No resolution is stated in the thread.

## Positions

- **[[person/singhpk234|Prashant Singh]]:** Forbid overlapping projections on a nested container and its nested fields and fail closed, because no industry semantics exist to borrow and forbidding can be relaxed later while precedence cannot. ([message](https://lists.apache.org/thread/zh25o2msbjw3skd577qzsyrcorobcthz))
- **[[person/sungwy|Sung Yun]]:** Supports option A for the initial release, with RFC 2119 wording, leaving conflict resolution to the policy engine. ([message](https://lists.apache.org/thread/ntvydm2d08hylmm49qsqs5rmm8for5g0))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Relaxing the prohibition later is not behaviourally backward compatible for clients, so the order in which nested restrictions apply should be defined now. ([message](https://lists.apache.org/thread/r61278kmpywytmbffovlmn120jko9tto))
- **[[person/stevenzwu|Steven Wu]]:** Agrees clients must fail on conflicting nested policies; a future relaxation could say readers may fail or may apply a precedence rule, so older clients that fail stay compliant. ([message](https://lists.apache.org/thread/52yxgdqfcmow0zcx3nt2nz9n2vhr3nnq))
- **Nevin Zheng:** Prefers the strict contract (catalog must not send overlaps, reader fails closed) but is comfortable with another coherent contract if it is specified and implemented well. ([message](https://lists.apache.org/thread/70gpyd7fox899cdrl5zf1qcyttj8qyb2))

References: [iceberg#13879](https://github.com/apache/iceberg/issues/13879)
<!-- kb:generated:end -->

## Notes
