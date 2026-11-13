---
id: thread/t-0fffc650114a3f55
type: thread
title: Replace nullable with type arrays in the REST catalog OpenAPI spec
date: '2026-10-21'
url: https://lists.apache.org/thread/6y4txojozlrhoslkkygcp3lkdyv2sktf
kind: discuss
status: consensus
messages: 4
sources:
- devlist:6y4txojozlrhoslkkygcp3lkdyv2sktf
refs:
- gh:apache/iceberg#18428
links: []
updated: '2026-11-13'
---

# Replace nullable with type arrays in the REST catalog OpenAPI spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSSION] Replace nullable with type arrays in rest catalog openapi spec](https://lists.apache.org/thread/6y4txojozlrhoslkkygcp3lkdyv2sktf) · **Started:** 2026-10-21 by MonkeyCanCode · **Messages:** 4 (last 2026-10-22) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

MonkeyCanCode reported that, while upgrading the OpenAPI spec version from 3.0.x to 3.1.x for Apache Polaris, he noticed that the OpenAPI spec used by Iceberg is not valid 3.1.x. According to the OpenAPI upgrade guide, the nullable keyword should be replaced with type arrays when moving from 3.0.x to 3.1.x. He opened PR #18428 to make that change in the REST catalog OpenAPI spec and asked for review. Alex Dutra replied that the proposed changes make sense and that he had approved the PR. pvary thanked the author for the fix, and flyrain added a +1 on the fix. Nobody raised objections, and the thread does not say whether the PR was merged.

**Why it matters:** Projects that generate code or validate against the REST catalog OpenAPI file with 3.1 tooling depend on the spec being valid 3.1.

## Outcome

All three replies supported the fix and one approved PR #18428; the thread does not state that it was merged.

## Positions

- **MonkeyCanCode:** The Iceberg REST OpenAPI spec is invalid as 3.1.x because it uses nullable, which should be replaced with type arrays. ([message](https://lists.apache.org/thread/6y4txojozlrhoslkkygcp3lkdyv2sktf))
- **Alex Dutra:** The proposed changes make sense; he approved the PR. ([message](https://lists.apache.org/thread/jm0w6okxv1gs4q4bhvlox38cls5npdr7))

References: [iceberg#18428](https://github.com/apache/iceberg/issues/18428)
<!-- kb:generated:end -->

## Notes
