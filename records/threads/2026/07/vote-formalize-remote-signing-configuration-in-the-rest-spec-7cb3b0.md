---
id: thread/t-7cb3b0fb5a513b73
type: thread
title: Formalize remote signing configuration in the REST spec
date: '2026-07-20'
url: https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2
kind: vote
status: passed
messages: 9
sources:
- devlist:n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2
refs:
- gh:apache/iceberg#16822
links:
- rel: discussed
  to: initiative/rest-auth
  confidence: extracted
  source: devlist:n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2
- rel: started_by
  to: person/adutra
  confidence: observed
updated: '2026-11-13'
---

# Formalize remote signing configuration in the REST spec

<!-- kb:generated:start -->
**Thread:** [[VOTE] Formalize remote signing configuration in the REST spec](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2) · **Started:** 2026-07-20 by [[person/adutra|Alexandre Dutra]] · **Messages:** 9 (last 2026-07-30) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

adutra called a vote to formalize remote signing configuration in the REST catalog spec through PR #16822. The change introduces a new RemoteSigningConfig object in the LoadTableResult schema, containing properties and headers that signers should send back to the signing endpoint. The vote was opened on July 20, 2026 for 72 hours, with links to two earlier discussion threads. No votes arrived in the first week, so adutra sent a reminder on July 28 and cast a non-binding +1. RussellSpitzer, danielcweeks, Eduard Tudenhöfner and flyrain then voted +1 binding, and singhpk234 and laskoviymishka also voted +1. There were no -1 votes or objections in the thread. adutra closed the vote on July 30 as passed and said a separate result mail would follow.

**Why it matters:** Catalogs can tell clients how to use remote signing through a defined field in the load-table response rather than free-form config properties.

## Outcome

Passed with 5 binding and 2 non-binding votes, as stated by the proposer; no -1 votes appear in the thread. ([message](https://lists.apache.org/thread/gbrdff89qk0rvbz4booh1zqpdqgrvdzn), `devlist:gbrdff89qk0rvbz4booh1zqpdqgrvdzn`)

## Positions

- **[[person/adutra|Alexandre Dutra]]:** Remote signing configuration should be a formal RemoteSigningConfig object in LoadTableResult carrying the properties and headers signers send to the signing endpoint. ([message](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2))

References: [iceberg#16822](https://github.com/apache/iceberg/issues/16822)
<!-- kb:generated:end -->

## Notes
