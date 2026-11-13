---
id: thread/t-c455572cb549f180
type: thread
title: Table and column label metadata in the Iceberg REST catalog
date: '2026-03-05'
url: https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg
kind: discuss
status: open
messages: 9
sources:
- devlist:mptyj9nh6xd9zymbyq6qvf35j9x9hwyg
refs:
- gh:apache/iceberg#15521
- gh:apache/iceberg#15750
- gh:apache/iceberg-python#3191
- gh:apache/polaris#3222
- gh:apache/polaris#4048
- gh:apache/iceberg#13879
- doc:1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI
links:
- rel: discussed
  to: initiative/catalog-labels
  confidence: extracted
  source: devlist:mptyj9nh6xd9zymbyq6qvf35j9x9hwyg
- rel: started_by
  to: person/laskoviymishka
  confidence: observed
updated: '2026-11-13'
---

# Table and column label metadata in the Iceberg REST catalog

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Table and Column Label Metadata in Iceberg REST Catalog](https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg) · **Started:** 2026-03-05 by [[person/laskoviymishka|Andrei Tserakhau]] · **Messages:** 9 (last 2026-07-07) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Andrei Tserakhau proposed an optional `labels` field on `LoadTableResponse` so catalogs can surface catalog-managed context (ownership, cost attribution, classification, semantic hints) as string key-value pairs without writing it to table properties. Ryan Blue supported it as a generic channel that adds no requirements to catalogs. Andrei followed with a spec PR, a PyIceberg client and proofs of concept in Polaris, Unity Catalog and Lakekeeper. Syncs on May 28 and June 29 agreed to land the read API first with the write API as a separate follow-up, to keep labels flat, and to treat governance as one use case among many, with enforcement left to read restrictions. The shape was consolidated into one `labels` object with `table` and `columns` parts, and a proposed latency requirement was softened to implementation guidance. EJ Wang questioned whether labels should be a separate primitive rather than a projection of a structured Tag model. The thread ends with a call to review the spec PR; structured tags go to a follow-up sync.

**Why it matters:** It sets the direction for a new optional REST catalog field: read-only flat labels first, with write APIs and structured tags handled separately.

## Outcome

As of July 7 the read-path representation (`labels: { table, columns }`) was described as stable and the ask was review of the spec PR before a vote; the write path and structured tags were deferred to follow-up work.

## Positions

- **[[person/laskoviymishka|Andrei Tserakhau]]:** Add an optional, catalog-generated `labels` key-value field to `LoadTableResponse`, separate from table properties, which engines may use or ignore. ([message](https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg))
- **[[person/rdblue|Ryan Blue]]:** Supports labels as a generic way for catalogs to share extra metadata without adding REST spec requirements, and as an alternative to overriding table properties, which he calls an anti-pattern. ([message](https://lists.apache.org/thread/3cyf1g5768jpmm09hr8c31tpyfvmyrn5))
- **EJ Wang:** Before standardizing flat labels as an independent primitive, evaluate making a structured Tag/classification model the source of truth with REST response metadata as a projection of it, and do not pre-decide that tags are only catalog-internal. ([message](https://lists.apache.org/thread/shd3bmm15sry0gzy3xjycto063k8mbv7))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Flat labels are the right shape for the read path and a structured tag layer can build on top; the write path and structured tags should not block read-path review. ([message](https://lists.apache.org/thread/j5310o8cn73x95cmhlwrbq32d7fzjd0d))

References: [iceberg#15521](https://github.com/apache/iceberg/issues/15521), [iceberg#15750](https://github.com/apache/iceberg/issues/15750), [iceberg-python#3191](https://github.com/apache/iceberg-python/issues/3191), [polaris#3222](https://github.com/apache/polaris/issues/3222), [polaris#4048](https://github.com/apache/polaris/issues/4048), [iceberg#13879](https://github.com/apache/iceberg/issues/13879), [doc](https://docs.google.com/document/d/1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI)
<!-- kb:generated:end -->

## Notes
