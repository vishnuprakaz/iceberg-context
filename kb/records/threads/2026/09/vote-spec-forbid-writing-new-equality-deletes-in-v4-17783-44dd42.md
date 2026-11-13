---
id: thread/t-44dd42ceee95da54
type: thread
title: 'Spec vote: forbid writing new equality deletes in v4'
date: '2026-09-23'
url: https://lists.apache.org/thread/2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1
kind: vote
status: passed
messages: 11
sources:
- devlist:2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1
refs:
- gh:apache/iceberg#17783
links:
- rel: discussed
  to: initiative/v4-equality-deletes
  confidence: extracted
  source: devlist:2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1
- rel: started_by
  to: person/huaxingao
  confidence: observed
updated: '2026-11-13'
---

# Spec vote: forbid writing new equality deletes in v4

<!-- kb:generated:start -->
**Thread:** [[VOTE][SPEC] Forbid writing new equality deletes in v4 (#17783)](https://lists.apache.org/thread/2pgfvf8v5ob221q5t2xwzjo4xvw5ltz1) · **Started:** 2026-09-23 by [[person/huaxingao|Huaxin Gao]] · **Messages:** 11 (last 2026-09-29) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Huaxin Gao called a spec vote on PR #17783, the wording that implements the direction voted on in July: v4 writers must not write new equality deletes, readers still apply existing ones from v2 and v3, and upgrade stays metadata-only. Russell Spitzer and Yufei Gu said a second vote may not be needed since the concept was already voted on, but both voted +1. Xuanwo and Steven Wu noted that the wording covers reading existing equality deletes after a metadata-only upgrade. Ryan Blue voted +1, saying the text will be iterated on and the main purpose is to affirm the decision to no longer allow equality deletes. Anoop Johnson said this simplifies the v4 design. Huaxin announced that the vote passed and that the PR will be merged, with a follow-up PR for Ryan's suggestions on restructuring how the delete sections present deletion vectors and the legacy representations.

**Why it matters:** The v4 spec now forbids writers from producing new equality deletes, so engines that write them must switch to deletion vectors for v4 tables.

## Outcome

The vote passed with 4 binding +1 votes and 5 non-binding +1 votes, and no 0 or -1 votes. Huaxin Gao will merge #17783 and follow up with a separate PR for wording suggestions. ([message](https://lists.apache.org/thread/onbpbh3tmtorpd9zw6y6563k3krrxoly), `devlist:onbpbh3tmtorpd9zw6y6563k3krrxoly`)

## Positions

- **[[person/RussellSpitzer|Russell Spitzer]]:** +1, though another vote on the PR may be unnecessary since the concept was already voted on and the PR can be reviewed normally. ([message](https://lists.apache.org/thread/lo69zrtdncblzn3t62hgk8n24jtkomn0))
- **[[person/rdblue|Ryan Blue]]:** +1 binding; the wording will keep being refined, and the purpose of the vote is to affirm that equality deletes are no longer allowed. ([message](https://lists.apache.org/thread/5x7dd6ok0znwvnkckp1rkvdqrdll6hpt))

References: [iceberg#17783](https://github.com/apache/iceberg/issues/17783)
<!-- kb:generated:end -->

## Notes
