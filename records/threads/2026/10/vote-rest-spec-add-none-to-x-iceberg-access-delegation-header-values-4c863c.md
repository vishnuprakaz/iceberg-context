---
id: thread/t-4c863ceec72fa0da
type: thread
title: 'REST spec: add none to X-Iceberg-Access-Delegation header values'
date: '2026-10-25'
url: https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk
kind: vote
status: passed
messages: 9
sources:
- devlist:hc2764vozz7ygx5fjj64104hotrof0lk
refs:
- gh:apache/iceberg#18480
links: []
updated: '2026-11-13'
---

# REST spec: add none to X-Iceberg-Access-Delegation header values

<!-- kb:generated:start -->
**Thread:** [[VOTE] REST spec: Add none to X-Iceberg-Access-Delegation header values](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk) · **Started:** 2026-10-25 by youngrae81 · **Messages:** 9 (last 2026-10-28) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

youngrae81 called a vote on adding the value none to the allowed values of the X-Iceberg-Access-Delegation header in the REST catalog spec, through PR 18480. The value signals that the client is able to operate without any access delegation mechanism. The proposal follows an earlier discussion thread on the expected server behavior when the requested access delegation cannot be satisfied, where, according to the vote email, Dan and Dmitri agreed that only this addition is needed; the PR had approvals from Dan, Dmitri and Alexandre. The vote was open for at least 72 hours and received only +1 votes. youngrae81 announced that it passed and said he would follow up on the PR for the merge.

**Why it matters:** Clients can explicitly tell a REST catalog that they need no vended credentials or remote signing.

## Outcome

Passed with 7 +1 votes (3 binding, 4 non-binding) and no 0 or -1 votes. The change is in PR 18480, pending merge. ([message](https://lists.apache.org/thread/c5ldjw25fplxjfplfx8fnvbkv598yy3p), `devlist:c5ldjw25fplxjfplfx8fnvbkv598yy3p`)

## Positions

- **youngrae81:** Add none to the X-Iceberg-Access-Delegation values so a client can signal it can operate without any access delegation mechanism. ([message](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk))

References: [iceberg#18480](https://github.com/apache/iceberg/issues/18480)
<!-- kb:generated:end -->

## Notes
