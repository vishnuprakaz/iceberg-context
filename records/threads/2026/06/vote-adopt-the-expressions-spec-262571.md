---
id: thread/t-2625714567b6a82f
type: thread
title: 'Vote: adopt the expressions spec'
date: '2026-06-24'
url: https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o
kind: vote
status: open
messages: 19
sources:
- devlist:6wfmjhgthlykwbk3f7df4zgcm40xtm2o
refs:
- gh:apache/iceberg#16652
- doc:1VthBz0S2I39TeQM8oiF9_gSPQu_gHAjWXvdFpv0QqDk
links:
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Vote: adopt the expressions spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Adopt the expressions spec](https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o) · **Started:** 2026-06-24 by [[person/rdblue|Ryan Blue]] · **Messages:** 19 (last 2026-06-29) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Ryan Blue started a vote to adopt a new expressions spec (PR #16652). The spec defines the minimal structure and behaviour of expressions that Iceberg formats need to store and exchange. Its stated purposes are to clean up the expressions used in the REST catalog spec for exchanging query filters, and to enable use cases that store expressions in metadata, including expression defaults such as current_timestamp() and CHECK constraints. The vote was open for 72 hours. Every reply in the thread is a +1; Gang Wu and Junwang Zhao mentioned minor review comments that they did not consider blocking. The thread as captured contains no message announcing the result.

**Why it matters:** The expressions spec is the basis for default value expressions, CHECK constraints and consistent REST filter expressions.

## Outcome

No result message is in the thread. Votes cast: 18 +1, of which 5 binding and 13 non-binding; no +0 or -1.

## Positions

- **[[person/rdblue|Ryan Blue]]:** Adopt the expressions spec to clean up REST filter expressions and to allow expressions stored in metadata, such as default expressions and CHECK constraints. ([message](https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o))
- **[[person/zhjwpku|Junwang Zhao]]:** Votes +1 and would like the minor review comments addressed, though they are not blocking. ([message](https://lists.apache.org/thread/d073g6cknzzrtp8lnfjszp71z0t2x8sv))

References: [iceberg#16652](https://github.com/apache/iceberg/issues/16652), [doc](https://docs.google.com/document/d/1VthBz0S2I39TeQM8oiF9_gSPQu_gHAjWXvdFpv0QqDk)
<!-- kb:generated:end -->

## Notes
