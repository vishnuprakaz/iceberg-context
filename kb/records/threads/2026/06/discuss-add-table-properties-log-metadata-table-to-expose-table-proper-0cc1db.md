---
id: thread/t-0cc1db5961938593
type: thread
title: Adding a table_properties_log metadata table to expose table property history
date: '2026-06-30'
url: https://lists.apache.org/thread/73tvsbmfnfhsow0nyq2lrblwbmbw00rb
kind: discuss
status: open
messages: 4
sources:
- devlist:73tvsbmfnfhsow0nyq2lrblwbmbw00rb
refs:
- gh:apache/iceberg#16859
- gh:apache/iceberg#9844
- gh:apache/iceberg#8856
- gh:apache/iceberg#14881
links: []
updated: '2026-11-13'
---

# Adding a table_properties_log metadata table to expose table property history

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Add `table_properties_log` metadata table to expose table property history](https://lists.apache.org/thread/73tvsbmfnfhsow0nyq2lrblwbmbw00rb) · **Started:** 2026-06-30 by Tomohiro Tanaka · **Messages:** 4 (last 2026-08-31) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Tomohiro Tanaka asked whether a read-only table_properties_log metadata table (PR #16859) is worth adding. It would return one row per retained metadata version with the table properties at that version, by reading previous metadata.json files, without a spec or write-path change. Tanmay Rauth found the need real but noted that no existing metadata table re-reads historical root metadata: the scan would read up to write.metadata.previous-versions-max files at planning time and fail entirely if one file is unreadable. Andrei Tserakhau (laskoviymishka) framed it as a pattern question, whether a metadata table's cost and failure surface may scale with retention config, and suggested a catalog could instead materialize property history as a normal table, which matters more with server-side scan planning. Tanaka then reworked the PR: instead of a new table, an optional properties column on metadata_log_entries, with historical files read only when the column is used and a missing file yielding null. He kept the implementation in core for portability. No further replies followed.

## Outcome

No decision is recorded. The author changed the PR to add a properties column to metadata_log_entries and asked for further feedback.

## Positions

- **Tomohiro Tanaka:** Property history should be exposed through metadata table syntax by reading retained previous metadata files, with no spec or write-path change. ([message](https://lists.apache.org/thread/73tvsbmfnfhsow0nyq2lrblwbmbw00rb))
- **[[person/tanmayrauth|Tanmay Rauth]]:** It is worth pursuing only if the read cost and failure handling are settled, because the scan cost scales with the number of retained metadata versions and one unreadable file fails the scan. ([message](https://lists.apache.org/thread/zw4t6tpf64270vtf1d4n7hggtpjfctn8))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** The community should decide the pattern first: an engine-core metadata table that reads files on demand, or a table the catalog materializes; for file reading, per-row degradation is close to required. ([message](https://lists.apache.org/thread/ov5kk6dbl77jjnxnnqpkwwjty3mqvnvk))
- **Tomohiro Tanaka:** An optional properties column on metadata_log_entries, read lazily and returning null for a missing file, keeps the feature portable across catalogs; catalog materialization can be explored separately. ([message](https://lists.apache.org/thread/875sjy3k2x2x8w5ny9vk5m3nzgbqb04y))

References: [iceberg#16859](https://github.com/apache/iceberg/issues/16859), [iceberg#9844](https://github.com/apache/iceberg/issues/9844), [iceberg#8856](https://github.com/apache/iceberg/issues/8856), [iceberg#14881](https://github.com/apache/iceberg/issues/14881)
<!-- kb:generated:end -->

## Notes
