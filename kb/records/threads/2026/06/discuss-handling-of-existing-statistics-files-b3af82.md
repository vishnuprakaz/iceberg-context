---
id: thread/t-b3af82ac2685e2f2
type: thread
title: Handling of existing statistics files
date: '2026-06-25'
url: https://lists.apache.org/thread/owfk09ll0n1crtfbl8jnyzmg8tm1dbrg
kind: discuss
status: no-conclusion
messages: 11
sources:
- devlist:owfk09ll0n1crtfbl8jnyzmg8tm1dbrg
refs: []
links:
- rel: started_by
  to: person/Dzeri96
  confidence: observed
updated: '2026-11-13'
---

# Handling of existing statistics files

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Handling of existing statistics files](https://lists.apache.org/thread/owfk09ll0n1crtfbl8jnyzmg8tm1dbrg) · **Started:** 2026-06-25 by [[person/Dzeri96|Dzeri96]] · **Messages:** 11 (last 2026-07-07) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Dzeri96 reported that a stats-only commit (running ANALYZE TABLE in iceberg-spark) replaced a snapshot's statistics file and dropped proprietary index blobs another writer had stored there. Three options were put forward: require writers to carry unknown blobs over into new Puffin files, allow several statistics files per snapshot, or create a new snapshot when statistics are computed. tmater preferred dropping unknown blobs and tying statistics to a new snapshot. Gábor Kaszab objected to creating snapshots for statistics and to the spec mandating carry-over of proprietary blobs; he found that the spec does not forbid several statistics entries for one snapshot, but the Java TableMetadata builder and the UpdateStatistics.setStatistics contract replace existing ones. Dzeri96 then proposed a 'type' field on statistics file metadata with a required iceberg-statistics-v1 type. The thread ends there without agreement.

**Why it matters:** Until this is settled, a stats-producing operation in one engine can replace the statistics file of a snapshot and drop blobs written by another engine.

## Outcome

The thread stops after Dzeri96's concrete proposal for a 'type' field on statistics files; Dzeri96 asked for more opinions and nobody else replied.

## Positions

- **[[person/Dzeri96|Dzeri96]]:** Writers should not delete each other's statistics metadata; allow multiple statistics files per snapshot and add a 'type' field to statistics file metadata, with iceberg-statistics-v1 required for compliance. ([message](https://lists.apache.org/thread/nznf7tnk9t47kq8dzyw7p9pozq0sxh6z))
- **[[person/tmater|Tamas Mate]]:** Dropping an unknown blob is safer than carrying it forward unvalidated, multiple files per snapshot add planning cost, and creating a snapshot when statistics are written is the simplest model. ([message](https://lists.apache.org/thread/j769l8hcxn0vzq1ly24x5zhdmvsjm2vv))
- **Gábor Kaszab:** Creating a snapshot for statistics breaks the model that snapshots are for data changes, and the spec should not mandate that engines carry over proprietary blobs they do not understand. ([message](https://lists.apache.org/thread/hb4xz96257gkqwxc4khyjzsfm2d8v9h0))
- **Gábor Kaszab:** The spec already permits several statistics entries per snapshot ID and only the Java builder and API contract enforce replacement, but statistics ownership would add spec complexity without benefit for open source engines. ([message](https://lists.apache.org/thread/sz2h9ho13rvwftfz4bzj0qlwxntntjgn))
- **Gábor Kaszab:** Secondary indexes will not be wired through the table metadata statistics field, and gaps should be closed by adding officially supported features to the spec. ([message](https://lists.apache.org/thread/qqbo7byynvd16rop6687b6gxow9gn6b1))
<!-- kb:generated:end -->

## Notes
