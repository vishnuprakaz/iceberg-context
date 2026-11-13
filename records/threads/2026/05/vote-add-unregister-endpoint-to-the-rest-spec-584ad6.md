---
id: thread/t-584ad622bd8bd6d8
type: thread
title: 'Vote: add an unregister endpoint to the REST spec'
date: '2026-05-20'
url: https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g
kind: vote
status: passed
messages: 18
sources:
- devlist:vy9fqyopp9c149oy40brdhb10grpq32g
refs:
- gh:apache/iceberg#16400
links:
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Vote: add an unregister endpoint to the REST spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add unregister endpoint to the REST spec](https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g) · **Started:** 2026-05-20 by [[person/rdblue|Ryan Blue]] · **Messages:** 18 (last 2026-05-26) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rdblue called a vote on adding an unregister endpoint to the REST catalog spec, with the change in PR #16400. Unregister is the opposite of register: it removes a table from a catalog without deleting the underlying data and metadata files, and returns the latest catalog state of the table. The stated purpose is to allow moving a table from one catalog to another, which needs a new endpoint because the files must be left in place. The vote was open for 72 hours. All replies were +1; adutra noted it will be useful for catalog migration, and Maninder Parmar said it defines clearer semantics about data lifecycle. rdblue closed the vote as passed.

**Why it matters:** REST catalogs gain a standard way to drop a table from the catalog without touching its files, which catalog migration tools can rely on.

## Outcome

Passed with 16 +1 votes (9 binding, 7 non-binding) and no +0 or -1 votes. ([message](https://lists.apache.org/thread/30voqgmho92o0bnv79qcz1rzlkwh5z39), `devlist:30voqgmho92o0bnv79qcz1rzlkwh5z39`)

## Positions

- **[[person/rdblue|Ryan Blue]]:** Add an unregister endpoint that removes a table from a catalog while leaving its data and metadata files in place, to support moving tables between catalogs. ([message](https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g))
- **[[person/adutra|Alexandre Dutra]]:** Supports the endpoint as useful for catalog migration scenarios. ([message](https://lists.apache.org/thread/3gy49fhyy6kd1ytb606804z1o797k63c))
- **Maninder Parmar:** Supports the endpoint because it defines clearer semantics about data lifecycle. ([message](https://lists.apache.org/thread/df2sz62rvnx8fhz51m98l21o9tcsxvnw))

References: [iceberg#16400](https://github.com/apache/iceberg/issues/16400)
<!-- kb:generated:end -->

## Notes
