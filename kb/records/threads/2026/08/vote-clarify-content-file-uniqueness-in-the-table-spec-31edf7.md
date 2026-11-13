---
id: thread/t-31edf75f84e57ef0
type: thread
title: Vote to clarify content file uniqueness in the table spec
date: '2026-08-14'
url: https://lists.apache.org/thread/orwny91fqyfmzx7w7p6wj7cgmndvd8r3
kind: vote
status: passed
messages: 13
sources:
- devlist:orwny91fqyfmzx7w7p6wj7cgmndvd8r3
refs:
- gh:apache/iceberg#17198
- gh:apache/iceberg#4272
links:
- rel: started_by
  to: person/RussellSpitzer
  confidence: observed
updated: '2026-11-13'
---

# Vote to clarify content file uniqueness in the table spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Clarify content file uniqueness in the table spec](https://lists.apache.org/thread/orwny91fqyfmzx7w7p6wj7cgmndvd8r3) · **Started:** 2026-08-14 by [[person/RussellSpitzer|Russell Spitzer]] · **Messages:** 13 (last 2026-08-19) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Russell Spitzer called a vote on a spec clarification in PR #17198. He explained that scan planning has stated since PR #4272 that duplicate live file paths in a snapshot produce undefined scan results, and that the new change makes that expectation explicit as a snapshot invariant in the main body of the spec. He said he believed consensus already existed and raised the vote for awareness before merging. The vote was open for 72 hours. Twelve people replied, all with +1 and without objections. Spitzer then announced that the vote passes, and noted that the language in the PR is being softened to refer just to 'live' entries; further comments belong on the PR, which can be merged once the final wording has consensus there.

**Why it matters:** Writers are expected to keep live file paths unique within a snapshot, and readers may treat duplicates as undefined behavior.

## Outcome

The vote passed; the result message gives no counts. Replies in the thread: 2 binding +1, 9 non-binding +1 and one +1 with no binding status stated, with no -1 votes. The PR wording is being softened to refer to 'live' entries before merging. ([message](https://lists.apache.org/thread/31bkxwff6kc9pp2l0r656yjxt32lxwgw), `devlist:31bkxwff6kc9pp2l0r656yjxt32lxwgw`)

## Positions

- **[[person/RussellSpitzer|Russell Spitzer]]:** The spec should state as a snapshot invariant that live content file paths in a snapshot are unique, since duplicates already produce undefined scan results. ([message](https://lists.apache.org/thread/orwny91fqyfmzx7w7p6wj7cgmndvd8r3))

References: [iceberg#17198](https://github.com/apache/iceberg/issues/17198), [iceberg#4272](https://github.com/apache/iceberg/issues/4272)
<!-- kb:generated:end -->

## Notes
