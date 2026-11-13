---
id: thread/t-8853b84d399d7c2a
type: thread
title: Multi-table, multi-statement transactions for the REST catalog
date: '2025-06-17'
url: https://lists.apache.org/thread/r5otylsrm4txd4oxyv7c6scdwrbolck9
kind: discuss
status: open
messages: 11
sources:
- devlist:r5otylsrm4txd4oxyv7c6scdwrbolck9
refs:
- doc:1KVgUJc1WgftHfLz118vMbEE7HV8_pUDk4s-GJFDyAOE
- doc:1ew2dOI_BHQFP1C8Q46Y_m_AvNNH4rzzLKaSsB089GTU
- doc:1eXnT0ZiFvdm_Zvk6fLGT_UxVWO-HsiqVywqu1Uk8s7E
- gh:apache/iceberg#6948
- gh:apache/iceberg#10617
- gh:apache/polaris#5833
- list:q7vgnfwdxng5q6mq45m0psghzy7553r7
- list:d5ft79ogcxx15ccr1n1bc0rvsl14tf6v
links: []
updated: '2026-11-13'
---

# Multi-table, multi-statement transactions for the REST catalog

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Multi-statement multi-transaction proposal for Apache REST Catalog](https://lists.apache.org/thread/r5otylsrm4txd4oxyv7c6scdwrbolck9) · **Started:** 2025-06-17 by Maninderjit Singh · **Messages:** 11 (last 2026-10-26) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Maninderjit Singh shared a consolidated proposal for multi-table, multi-statement transactions in the REST catalog, merging earlier proposals based on catalog-authored timestamps and sequence numbers. Dmitri Bourlatchkov asked for more attention to server-side impact and proposed opaque, catalog-managed commit IDs: the catalog returns a commit ID with each change, clients load other tables at that ID and pass it as the base of a multi-table commit, with no durable transaction context on the server. Jagdeep Sidhu noted that an earlier TransactionContext design with opaque IDs was dropped because it needed many catalog calls and server-side transaction state. Maninderjit agreed to add the option to the document and planned a meeting. In October 2026 Qiegang Long reported a proof of concept in Apache Polaris built on table branches and the existing multi-table commit, and asked whether the REST spec should define transactions or only the primitives catalogs need, such as an optional read-point parameter on loadTable. The thread has no replies to that question.

**Why it matters:** How multi-table transactions are exposed determines what catalog servers must implement and whether the REST spec gains transaction endpoints or only smaller primitives.

## Outcome

No decision was reached. A broader meeting was planned in 2025, and the questions raised with the Polaris proof-of-concept report in October 2026 have no replies in the thread.

## Positions

- **Maninderjit Singh:** The consolidated proposal leaves server-side implementation to each vendor and asks which approach, catalog timestamps or sequence numbers, suits users. ([message](https://lists.apache.org/thread/fydc6j5hlz3mwtogh8oymp46q76po0q6))
- **Dmitri Bourlatchkov:** Use commit IDs that are opaque to clients and resolved by the catalog, which needs REST API changes but no table spec change and no server-side transaction state. ([message](https://lists.apache.org/thread/kt9j0lj6lfssxwnsbsy2c0zqmrbow6qn))
- **Jagdeep Sidhu:** The earlier TransactionContext approach with opaque IDs was dropped because it made the protocol chatty and required complex transaction state on the server. ([message](https://lists.apache.org/thread/vwt39ndnp3tz212mhn9mwmx8gqz0szwn))
- **Qiegang Long:** The Iceberg REST spec should add minimal primitives, such as an opaque read point on loadTable, and leave higher-level transaction semantics to catalogs. ([message](https://lists.apache.org/thread/m91m8vkw0g5fhsszmf2ton4djbwb3lr1))

References: [doc](https://docs.google.com/document/d/1KVgUJc1WgftHfLz118vMbEE7HV8_pUDk4s-GJFDyAOE), [doc](https://docs.google.com/document/d/1ew2dOI_BHQFP1C8Q46Y_m_AvNNH4rzzLKaSsB089GTU), [doc](https://docs.google.com/document/d/1eXnT0ZiFvdm_Zvk6fLGT_UxVWO-HsiqVywqu1Uk8s7E), [iceberg#6948](https://github.com/apache/iceberg/issues/6948), [iceberg#10617](https://github.com/apache/iceberg/issues/10617), [polaris#5833](https://github.com/apache/polaris/issues/5833), [thread](https://lists.apache.org/thread/q7vgnfwdxng5q6mq45m0psghzy7553r7), [thread](https://lists.apache.org/thread/d5ft79ogcxx15ccr1n1bc0rvsl14tf6v)
<!-- kb:generated:end -->

## Notes
