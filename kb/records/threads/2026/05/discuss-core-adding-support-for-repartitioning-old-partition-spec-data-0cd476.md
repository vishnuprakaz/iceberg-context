---
id: thread/t-0cd4766cfa975dcc
type: thread
title: 'Core: repartitioning data files written with an old partition spec'
date: '2026-05-13'
url: https://lists.apache.org/thread/vkn21zvbcg9vxt2prysp15f269l0s9h0
kind: discuss
status: open
messages: 4
sources:
- devlist:vkn21zvbcg9vxt2prysp15f269l0s9h0
refs:
- gh:apache/iceberg#16190
- gh:apache/iceberg#12083
- gh:apache/iceberg#16515
links:
- rel: started_by
  to: person/mukund-thakur
  confidence: observed
updated: '2026-11-13'
---

# Core: repartitioning data files written with an old partition spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] CORE: Adding support for repartitioning old partition spec data files](https://lists.apache.org/thread/vkn21zvbcg9vxt2prysp15f269l0s9h0) · **Started:** 2026-05-13 by [[person/mukund-thakur|Mukund Thakur]] · **Messages:** 4 (last 2026-06-24) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

mukund-thakur proposed support for rewriting only the data files that belong to an old partition spec so they conform to the current spec (PR #16190). Today such files are skipped by rewrite jobs when they already have the target size. Using rewrite-all with a filter and partial progress does not work well for large tables, because a rerun after a failure picks up the same files again and files cannot be filtered by spec ID. He suggested a new rewrite-partition-spec-mismatch flag used together with partial-progress.enabled, and later mentioned an optimized repartitioning algorithm in PR #16515. Imran Rashid, who works with the author, said this matters for large tables because storage-partitioned joins need consistent partitioning and existing tools cannot make incremental progress. pan3793 supported it, having seen SPJ fail because a scan mixed old-spec files. No committer feedback on the design appears in the thread.

**Why it matters:** Tables whose partition spec has evolved currently have no incremental, restartable way to bring old files to the new spec, which blocks storage-partitioned joins on them.

## Outcome

Two supporting replies; no review of the proposed option or decision appears in the thread.

## Positions

- **[[person/mukund-thakur|Mukund Thakur]]:** Add a rewrite-partition-spec-mismatch option so that rewrite jobs pick up only files written with an old partition spec and can make partial progress. ([message](https://lists.apache.org/thread/vkn21zvbcg9vxt2prysp15f269l0s9h0))
- **Imran Rashid:** Large tables need an incremental way to move old data to the new partitioning, in particular because storage-partitioned joins require consistent partitioning. ([message](https://lists.apache.org/thread/lgmjrhbqcvgk2lnk90j0zobqkjy37b7b))
- **[[person/pan3793|Cheng Pan]]:** Supports the change after finding that SPJ did not work because the scan mixed data files not matching the current partition spec. ([message](https://lists.apache.org/thread/jzh3xyoc3c2qktgxzy7wd74057r8bndj))

References: [iceberg#16190](https://github.com/apache/iceberg/issues/16190), [iceberg#12083](https://github.com/apache/iceberg/issues/12083), [iceberg#16515](https://github.com/apache/iceberg/issues/16515)
<!-- kb:generated:end -->

## Notes
