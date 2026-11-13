---
id: thread/t-e821af59b904a5ea
type: thread
title: Collation support in the Iceberg spec
date: '2026-03-28'
url: https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk
kind: discuss
status: consensus
messages: 14
sources:
- devlist:zdvc0gmqjgws8whwxv0ztn7h1jqclzyk
refs:
- doc:1m8b7u97uteHYjXk-4DNglJSpQO8OcZOCzW2tApCNTW4
- gh:apache/iceberg#16972
- gh:apache/iceberg-go#1318
links: []
updated: '2026-11-13'
---

# Collation support in the Iceberg spec

<!-- kb:generated:start -->
**Thread:** [[Discussion] Collation Support](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk) · **Started:** 2026-03-28 by Alexander Löser · **Messages:** 14 (last 2026-08-14) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alexander Löser proposed adding collations to the spec as an annotation on string fields, with collation-aware bounds, because UTF-8 bounds are not useful for collated columns. Andrei Tserakhau (laskoviymishka) raised lessons from Delta: ICU sort keys are not stable across versions, non-ICU providers exist, and partition transforms, sort orders and equality deletes need scoping. In June he posted a spec PR (#16972), an iceberg-go implementation and a Java POC that store original values as bounds, tagged with a per-file collation version, and use provider-qualified names. Löser questioned original values versus sort keys (truncation, comparison cost) and noted that letting each engine choose its ICU version also affects query results and equality deletes. A dedicated sync on August 5 agreed that the ICU version stays an engine decision, bounds use original strings with a version tag plus a code-point metric, and equality deletes will be deprecated in V4 or not work on collated columns. A v2 of the design doc followed; how to encode the metrics in the spec is still open.

**Why it matters:** The agreed direction means readers may prune a collated file only when they can handle the ICU version its bounds were written with.

## Outcome

The August 5 sync agreed that the ICU version remains an engine decision with writers tagging bounds by version, that bounds use original strings plus a code-point metric, and that equality deletes will be deprecated in V4 or not work on collated columns. The encoding of the version in the bounds and the shape of the code-point metric remain open. ([message](https://lists.apache.org/thread/ktmz3k8mjg2kzmlo54zz7jx4n4vwpbx6), `devlist:ktmz3k8mjg2kzmlo54zz7jx4n4vwpbx6`)

## Positions

- **Alexander Löser:** Collations should be added to the spec as an annotation on string fields with collation-specific bounds, because users are blocked on migrating collated tables to Iceberg. ([message](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Bounds should store original string values tagged with a per-file collation version rather than sort keys, and collation names should be provider-qualified, because ICU sort keys are not stable across versions. ([message](https://lists.apache.org/thread/44todz4x460g8pb89y8rpozlnmo8vdhc))
- **Alexander Löser:** Sort keys make truncation and comparison simpler and original strings give no extra pruning across ICU versions in the general case, unless extra metadata on the code points in a file is kept. ([message](https://lists.apache.org/thread/n7gmlbq1yoz9v43ob4zjn78vhf5rc5rl))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Original values are a superset of sort keys because a reader on another version can re-interpret them, and per-file versioning is needed because a versionless runtime has several ICU versions live at once. ([message](https://lists.apache.org/thread/zcg6bqk5wj8p05dtlw7rn0vooz8booto))
- **Alexander Löser:** Letting each engine pick its ICU version affects execution results and equality deletes as well as pruning, so the level of interoperability the spec guarantees should be decided deliberately. ([message](https://lists.apache.org/thread/798r8wskc74l6pdsm09thq4o056vjmdp))

References: [doc](https://docs.google.com/document/d/1m8b7u97uteHYjXk-4DNglJSpQO8OcZOCzW2tApCNTW4), [iceberg#16972](https://github.com/apache/iceberg/issues/16972), [iceberg-go#1318](https://github.com/apache/iceberg-go/issues/1318)
<!-- kb:generated:end -->

## Notes
