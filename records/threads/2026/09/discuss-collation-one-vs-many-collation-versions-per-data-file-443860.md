---
id: thread/t-4438607328a252c1
type: thread
title: 'Collation: one or many collation versions per data file'
date: '2026-09-21'
url: https://lists.apache.org/thread/4p8345gb8jo03l27qh86kbbpvolwc09j
kind: discuss
status: consensus
messages: 4
sources:
- devlist:4p8345gb8jo03l27qh86kbbpvolwc09j
refs:
- gh:apache/iceberg#16972
- doc:1t6_O_OYqSiJTUjveqXo9H5lpO-k7m0TcLMaauAuLXSk
- list:44todz4x460g8pb89y8rpozlnmo8vdhc
- list:t3r68d7mrpjxdlfv8brttr692os2jryc
links:
- rel: started_by
  to: person/laskoviymishka
  confidence: observed
updated: '2026-11-13'
---

# Collation: one or many collation versions per data file

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Collation: one vs many collation versions per data file](https://lists.apache.org/thread/4p8345gb8jo03l27qh86kbbpvolwc09j) · **Started:** 2026-09-21 by [[person/laskoviymishka|Andrei Tserakhau]] · **Messages:** 4 (last 2026-10-27) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Andrei Tserakhau (laskoviymishka) split one decision out of the collation thread and PR #16972: whether a data file may carry collation bounds for more than one collation version. Each bound is tagged with the version it was computed under, and a reader uses it only if it can reproduce that version; this affects pruning, not correctness. With a per-file list of {version, lower, upper}, a file written under one ICU version can be pruned by a reader on another once a bound for that version is added, for example by compaction, at the cost of a slightly larger stats struct. With one version per file, readers on another version cannot prune until the file is rewritten. He preferred multi-version. Alexander Loeser agreed and relayed a concern attributed to Russell about adding many fields to content_stats, with derived non-materialized fields as an alternative. Tserakhau prototyped both layouts and closed the thread: multi-version per file is settled, and how the bounds are stored continues in a new thread.

**Why it matters:** The decision fixes part of the on-disk metadata layout for collated columns and lets bounds for a new ICU version be added to existing files.

## Outcome

Multi-version collation bounds per data file is settled. How the bounds are stored, on top of stats-only fields, continues in a separate thread, and the planned October 28 sync was dropped. ([message](https://lists.apache.org/thread/80wfrnm4gnd3c3sgwxs2y1clc8xjz79f), `devlist:80wfrnm4gnd3c3sgwxs2y1clc8xjz79f`)

## Positions

- **[[person/laskoviymishka|Andrei Tserakhau]]:** A data file should be able to carry bounds for several collation versions, because different ICU versions are live at the same time during upgrades. ([message](https://lists.apache.org/thread/4p8345gb8jo03l27qh86kbbpvolwc09j))
- **Alexander Loeser:** Multi-version is preferable since a second set of metrics helps during ICU upgrades, but the storage format needs more discussion, including derived non-materialized fields that reuse lower_bounds and upper_bounds. ([message](https://lists.apache.org/thread/8f89jt50p53xkorh3z39dtz13jchd0gx))

References: [iceberg#16972](https://github.com/apache/iceberg/issues/16972), [doc](https://docs.google.com/document/d/1t6_O_OYqSiJTUjveqXo9H5lpO-k7m0TcLMaauAuLXSk), [thread](https://lists.apache.org/thread/44todz4x460g8pb89y8rpozlnmo8vdhc), [thread](https://lists.apache.org/thread/t3r68d7mrpjxdlfv8brttr692os2jryc)
<!-- kb:generated:end -->

## Notes
