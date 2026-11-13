---
id: thread/t-b9627d1f1c298c57
type: thread
title: Migrating to Java switch expressions
date: '2026-01-30'
url: https://lists.apache.org/thread/k2cg9v6rxs8lb74qbok166k68h1r0f3k
kind: discuss
status: withdrawn
messages: 10
sources:
- devlist:k2cg9v6rxs8lb74qbok166k68h1r0f3k
refs:
- gh:apache/iceberg#15176
- gh:apache/iceberg#15494
- gh:apache/iceberg#16881
- gh:apache/iceberg#16953
- list:b29jyys3lnr72dbscb5rlg9601c4hbh1
links:
- rel: started_by
  to: person/pvary
  confidence: observed
updated: '2026-11-13'
---

# Migrating to Java switch expressions

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Switching to new switches :)](https://lists.apache.org/thread/k2cg9v6rxs8lb74qbok166k68h1r0f3k) · **Started:** 2026-01-30 by [[person/pvary|Peter Vary]] · **Messages:** 10 (last 2026-06-24) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After Java 11 was dropped, Peter (pvary) asked how to adopt the new switch syntax, given that Manu Zhang's PR #15176 migrates all switch statements at once and disrupts large in-flight PRs and internal forks. He listed three options: one large PR now, merging it shortly before a release, or migrating incrementally in new or touched code; he preferred the first or second. Maximilian Michels and Manu favoured merging before the release. In June Neelesh Salian revived the thread for 1.12, scoping the work to switches and pattern-matching instanceof in iceberg-core based on #15494. Eduard Tudenhöfner and Kevin Liu asked for the instanceof changes in a separate PR. The core switch change merged as #16881, but concerns about switching in large chunks were raised at the community sync on June 24th; Neelesh reported the decision to revert the core changes for now, with similar future changes in individual PRs at the reviewer's discretion. Eduard linked the revert PR #16953.

**Why it matters:** Bulk syntax-modernization PRs are not being accepted for now; contributors should keep such changes small and expect them to be at the reviewer's discretion.

## Outcome

The core switch-expression change (#16881) was merged, then concerns were raised at the community sync; Neelesh Salian reported the decision to revert the core changes for now (revert PR #16953), with similar changes going forward in individual PRs at the reviewer's discretion. ([message](https://lists.apache.org/thread/90z8rdrr3m3qfr3b6mcp93tfymcgr8w5), `devlist:90z8rdrr3m3qfr3b6mcp93tfymcgr8w5`)

## Positions

- **[[person/pvary|Peter Vary]]:** Prefers one large migration PR, either now or shortly before the release, over incremental adoption. ([message](https://lists.apache.org/thread/k2cg9v6rxs8lb74qbok166k68h1r0f3k))
- **[[person/mxm|Maximilian Michels]]:** Favours using Java 17 language features and merging the migration shortly before the release, noting that Flink 1.20 lacks proper Java 17 support. ([message](https://lists.apache.org/thread/vhswww1h3c1jdqw19wwh7mk699ocfkqh))
- **[[person/manuzhang|Manu Zhang]]:** Merging shortly before the release works for most people, and IDE support makes it easy to reapply the changes. ([message](https://lists.apache.org/thread/gns12y8xpoc9hdrph8pbtkodv89lfy3c))
- **[[person/nssalian|Neelesh Salian]]:** Do a scoped change for 1.12 covering switches and pattern-matching instanceof in iceberg-core only. ([message](https://lists.apache.org/thread/moc536sr3m46fsgq2jnn4oo32t85rjxm))
- **Eduard Tudenhöfner:** In favour of switch expressions for readability, but the instanceof changes should be a separate PR. ([message](https://lists.apache.org/thread/kmbzo3n5j1jvhty7jdp59jxpv6crnbt7))

References: [iceberg#15176](https://github.com/apache/iceberg/issues/15176), [iceberg#15494](https://github.com/apache/iceberg/issues/15494), [iceberg#16881](https://github.com/apache/iceberg/issues/16881), [iceberg#16953](https://github.com/apache/iceberg/issues/16953), [thread](https://lists.apache.org/thread/b29jyys3lnr72dbscb5rlg9601c4hbh1)
<!-- kb:generated:end -->

## Notes
