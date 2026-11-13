---
id: thread/t-33958badf295b701
type: thread
title: 'Vote: default value expressions for V4'
date: '2026-11-02'
url: https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob
kind: vote
status: passed
messages: 20
sources:
- devlist:th30oq0rcvn5gmn2qdx790k8vf4fz1ob
- devlist:h5jnk7l2op325x545hfnrpbo3qmh2ovo
refs:
- gh:apache/iceberg#16777
- doc:1NDMozxdvB3u66L-dTchnyZtQO5JCz3H9lUg14crpy8M
- list:ko8cs3tgol97f0m20yozchpxlotzl1mj
- list:w0xqrm0dpnsgvw0dyvy4r34y0dtzmn7f
links:
- rel: started_by
  to: person/danielcweeks
  confidence: observed
updated: '2026-11-13'
---

# Vote: default value expressions for V4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Default Value Expressions for v4](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob) · **Started:** 2026-11-02 by [[person/danielcweeks|Daniel C. Weeks]] · **Messages:** 20 (last 2026-11-09) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

danielcweeks started a vote on adding default value expressions, as proposed in an earlier discuss thread. The change expands write-default in V4 so that it can hold an expression as defined by the expressions spec, not only a literal. The vote message links the discuss thread, the proposal document and spec PR #16777, and asks for votes within 72 hours. The ballot options in the message are worded as adding stats-only fields to the table spec, although the subject and description are about default value expressions. All replies were +1 votes; pvary and GGraziadei said they had left minor comments. On 6 November danielcweeks thanked voters, said he would add his own +1 and close the vote with a separate result thread. One further +1 arrived afterwards. The result itself is not stated in this thread.

**Why it matters:** If adopted, V4 column defaults can be expressions rather than only literals, which writers will have to evaluate.

## Outcome

No result is stated in this thread; the caller said he would close it with a separate result thread. The thread shows only +1 votes: 8 marked binding, 8 marked non-binding and 2 unmarked, plus the caller's own announced +1.

**Result posted in a separate thread on 2026-11-06:** [[RESULT][VOTE] Default Value Expressions for v4](https://lists.apache.org/thread/h5jnk7l2op325x545hfnrpbo3qmh2ovo) (`devlist:h5jnk7l2op325x545hfnrpbo3qmh2ovo`). Outcome read from that message: passed.

## Positions

- **[[person/danielcweeks|Daniel C. Weeks]]:** Expand write-default in V4 to allow expressions defined by the expressions spec. ([message](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob))

References: [iceberg#16777](https://github.com/apache/iceberg/issues/16777), [doc](https://docs.google.com/document/d/1NDMozxdvB3u66L-dTchnyZtQO5JCz3H9lUg14crpy8M), [thread](https://lists.apache.org/thread/ko8cs3tgol97f0m20yozchpxlotzl1mj), [thread](https://lists.apache.org/thread/w0xqrm0dpnsgvw0dyvy4r34y0dtzmn7f)
<!-- kb:generated:end -->

## Notes
