---
id: thread/t-94521177da7f4309
type: thread
title: Require monotonically increasing snapshot timestamps in v4
date: '2026-10-07'
url: https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm
kind: vote
status: passed
messages: 20
sources:
- devlist:y2fvgh4ojfcss7o76drkgdvdrpb17ccm
refs:
- gh:apache/iceberg#16294
- gh:apache/iceberg#16293
- list:cln7xtjy9kw2096gzqlg5c4gg8b9td10
links:
- rel: discussed
  to: initiative/v4-row-lineage-timestamps
  confidence: extracted
  source: devlist:y2fvgh4ojfcss7o76drkgdvdrpb17ccm
- rel: started_by
  to: person/stevenzwu
  confidence: observed
updated: '2026-11-13'
---

# Require monotonically increasing snapshot timestamps in v4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Require monotonically increasing snapshot timestamps in v4](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm) · **Started:** 2026-10-07 by [[person/stevenzwu|Steven Wu]] · **Messages:** 20 (last 2026-10-13) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

stevenzwu called a vote on requiring each new snapshot in a v4 table to have a timestamp-ms strictly greater than its parent snapshot's timestamp on the same branch. Root snapshots are unconstrained and v1 to v3 behavior is unchanged. He said this aligns snapshot timestamps with snapshot order, resolves time travel issues caused by out-of-order timestamps, and can enable a row timestamp metadata column inherited from the snapshot timestamp as a separate follow-up v4 spec change. The vote referenced spec PR 16294 and reference implementation PR 16293. All votes were +1. Xuanwo restated support while noting pre-upgrade snapshots are also left unchanged. Maninder Parmar voted +1 and asked the community to consider extending timestamp-ms to nanosecond precision to allow greater transaction throughput. stevenzwu announced that the vote passed and that he would merge the spec PR.

**Why it matters:** V4 writers must assign each new snapshot a timestamp strictly greater than its parent's on the same branch.

## Outcome

Passed with 9 binding +1 and 11 non-binding +1 votes, and no 0 or -1 votes. The spec PR 16294 is to be merged. ([message](https://lists.apache.org/thread/4fp65bnrh7k6x98yl2wgl931301jg25o), `devlist:4fp65bnrh7k6x98yl2wgl931301jg25o`)

## Positions

- **[[person/stevenzwu|Steven Wu]]:** V4 snapshots should have a timestamp strictly greater than their parent on the same branch, fixing time travel with out-of-order timestamps and enabling an inherited row timestamp column. ([message](https://lists.apache.org/thread/y2fvgh4ojfcss7o76drkgdvdrpb17ccm))
- **Maninder Parmar:** Supports the requirement and asks to consider nanosecond-precision snapshot timestamps to allow greater transaction throughput. ([message](https://lists.apache.org/thread/nh9tgco6ydkqogt7ghrwhhr629720c89))

References: [iceberg#16294](https://github.com/apache/iceberg/issues/16294), [iceberg#16293](https://github.com/apache/iceberg/issues/16293), [thread](https://lists.apache.org/thread/cln7xtjy9kw2096gzqlg5c4gg8b9td10)
<!-- kb:generated:end -->

## Notes
