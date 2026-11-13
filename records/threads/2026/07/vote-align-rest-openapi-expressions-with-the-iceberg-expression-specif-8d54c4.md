---
id: thread/t-8d54c4be3c9cc0d5
type: thread
title: 'Vote: align REST OpenAPI expressions with the Iceberg expression specification'
date: '2026-07-24'
url: https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38
kind: vote
status: passed
messages: 17
sources:
- devlist:njo5bzgf4m126ly74ydz1pfznhz70h38
- devlist:9ncgm04vd20lds0c3q99smvotjpxzjt8
refs:
- gh:apache/iceberg#17138
- gh:apache/iceberg#16652
links:
- rel: started_by
  to: person/singhpk234
  confidence: observed
updated: '2026-11-13'
---

# Vote: align REST OpenAPI expressions with the Iceberg expression specification

<!-- kb:generated:start -->
**Thread:** [[VOTE] Align REST OpenAPI expressions with the Iceberg expression specification](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38) · **Started:** 2026-07-24 by [[person/singhpk234|Prashant Singh]] · **Messages:** 17 (last 2026-07-27) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Prashant Singh called a vote to adopt PR #17138, which updates the REST catalog OpenAPI specification so that its expression schemas match the expression grammar defined in the Iceberg expression specification (PR #16652). The vote was to stay open for at least 72 hours. Junwang Zhao posted a review comment about the changes to required fields; Prashant replied that the comment had been answered on the PR, and Junwang later voted +1. Ryan Blue voted +1 and said the change fixes scan planning filters and supports new features such as check constraints. All other replies were +1 votes. The thread as captured does not include a message announcing the result.

**Why it matters:** REST catalog servers and clients that exchange filter expressions, for example in scan planning, will follow the shared expression grammar.

## Outcome

No result message is in the thread. Votes cast: 14 +1, of which 3 marked binding, 9 marked non-binding and 2 unmarked; no 0 or -1.

**Result posted in a separate thread on 2026-07-27:** [[RESULT][VOTE] Align REST OpenAPI expressions with the Iceberg expression specification](https://lists.apache.org/thread/9ncgm04vd20lds0c3q99smvotjpxzjt8) (`devlist:9ncgm04vd20lds0c3q99smvotjpxzjt8`). Outcome read from that message: passed.

## Positions

- **[[person/singhpk234|Prashant Singh]]:** Adopt the OpenAPI change so REST expression schemas align with the expression specification grammar. ([message](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38))
- **[[person/zhjwpku|Junwang Zhao]]:** Raised a review comment on the PR about the changes to required fields. ([message](https://lists.apache.org/thread/2jhtld60lm9b0r2ook9zn686gdwqtn13))
- **[[person/rdblue|Ryan Blue]]:** Votes +1; the change fixes up scan planning filters and supports new features like check constraints. ([message](https://lists.apache.org/thread/bxvq7g3f489dvbwqp200vvdnql652pwv))

References: [iceberg#17138](https://github.com/apache/iceberg/issues/17138), [iceberg#16652](https://github.com/apache/iceberg/issues/16652)
<!-- kb:generated:end -->

## Notes
