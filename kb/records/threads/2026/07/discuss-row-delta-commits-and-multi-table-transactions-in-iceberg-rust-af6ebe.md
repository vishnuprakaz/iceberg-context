---
id: thread/t-af6ebed2f3531bd4
type: thread
title: 'Row-delta commits and multi-table transactions in iceberg-rust: patterns from a CDC producer'
date: '2026-07-08'
url: https://lists.apache.org/thread/7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0
kind: discuss
status: informational
messages: 4
sources:
- devlist:7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0
refs:
- gh:apache/iceberg-rust#2785
- gh:apache/iceberg-rust#2786
- gh:apache/iceberg-rust#2784
- gh:apache/iceberg-rust#2218
- gh:apache/iceberg-rust#2186
- gh:apache/iceberg-go#787
- gh:apache/iceberg-go#817
- gh:apache/iceberg-go#983
- gh:apache/iceberg-go#947
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0
updated: '2026-11-13'
---

# Row-delta commits and multi-table transactions in iceberg-rust: patterns from a CDC producer

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Row-delta commits and multi-table transactions in iceberg-rust ? patterns from a CDC producer](https://lists.apache.org/thread/7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0) · **Started:** 2026-07-08 by steveis · **Messages:** 4 (last 2026-07-29) · **Outcome:** informational

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Steve, building a Postgres-to-Iceberg CDC pipeline on iceberg-rust, opened two draft PRs for discussion: a RowDeltaAction that commits data files and equality or position delete files in one snapshot, and multi-table transaction commits through the REST `transactions/commit` endpoint. Andrei Tserakhau shared lessons from doing the same in iceberg-go: choose the operation type from the content, apply equality deletes only to data files with a strictly lower sequence number, expect most effort on the read side, and reject empty or float/double equality keys. For multi-table commits he advised a separate optional trait, reloading after the 204 response, and treating 5xx responses as commit-state-unknown. Steve applied several points and noted that his `prepare_commit` consumes the transaction. Andrei agreed that consuming is the right default in Rust and pointed to the iceberg-go changes for partition-scoped conflict detection and removal of dangling equality deletes. The PRs remained drafts in the thread.

**Why it matters:** It collects correctness pitfalls for row-delta and multi-table commits that iceberg-go already hit and that the iceberg-rust write path will need to handle.

## Outcome

Design feedback was exchanged and partly applied to the draft PRs; the thread records no decision on merging them.

## Positions

- **steveis:** Proposes adding RowDeltaAction and REST multi-table transaction commits to iceberg-rust and is willing to adapt the APIs to the ongoing merge-on-read work. ([message](https://lists.apache.org/thread/7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Keep multi-table commit as a separate optional trait implemented by REST, split building a commit from committing it, and never blindly retry 5xx responses because the commit state is unknown. ([message](https://lists.apache.org/thread/8sh5ftzkgyz7xyj234gnjgppx3ppv2g0))
- **steveis:** `prepare_commit` should consume the transaction, because Rust ownership then prevents a prepared transaction from also being committed directly. ([message](https://lists.apache.org/thread/ns239wxx2xxfnl9t6rc7nd6c3krcbt0d))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Consuming the transaction is the right default and fits the commit-state-unknown error model; iceberg-go needed a manual committed flag to get the same guarantee. ([message](https://lists.apache.org/thread/ssxgzwdccd4tb51b80t96bm7knj44h31))

References: [iceberg-rust#2785](https://github.com/apache/iceberg-rust/issues/2785), [iceberg-rust#2786](https://github.com/apache/iceberg-rust/issues/2786), [iceberg-rust#2784](https://github.com/apache/iceberg-rust/issues/2784), [iceberg-rust#2218](https://github.com/apache/iceberg-rust/issues/2218), [iceberg-rust#2186](https://github.com/apache/iceberg-rust/issues/2186), [iceberg-go#787](https://github.com/apache/iceberg-go/issues/787), [iceberg-go#817](https://github.com/apache/iceberg-go/issues/817), [iceberg-go#983](https://github.com/apache/iceberg-go/issues/983), [iceberg-go#947](https://github.com/apache/iceberg-go/issues/947)
<!-- kb:generated:end -->

## Notes
