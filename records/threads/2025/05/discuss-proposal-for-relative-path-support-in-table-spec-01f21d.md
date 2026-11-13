---
id: thread/t-01f21da0dbe27e4f
type: thread
title: Proposal for relative path support in the table spec
date: '2025-05-27'
url: https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2
kind: discuss
status: open
messages: 20
sources:
- devlist:nsj0dtxop4h115j6yrcx2vmxpzwt1ow2
refs:
- gh:apache/iceberg#13141
- gh:apache/iceberg#15630
- gh:apache/iceberg#16174
- doc:1t0RxrK-nsCT83zXeD66kmGx_TMU2X8_xfN1A_k6dCV0
links:
- rel: discussed
  to: initiative/v4-relative-paths
  confidence: extracted
  source: devlist:nsj0dtxop4h115j6yrcx2vmxpzwt1ow2
- rel: started_by
  to: person/talatuyarer
  confidence: observed
updated: '2026-11-13'
---

# Proposal for relative path support in the table spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Proposal for Relative Path Support In Table Spec](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2) · **Started:** 2025-05-27 by [[person/talatuyarer|Talat UYARER]] · **Messages:** 20 (last 2026-05-18) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Talat Uyarer and Daniel Weeks proposed relative paths as a V4 table spec change (issue #13141 and a design doc). A dedicated sync was held in July 2025. Wing Yew Poon asked whether a single copy of metadata with several copies of data would be supported; Weeks answered that multiple locations for the same files under one table is explicitly a non-goal and that the open points were about how paths are constructed, resolved and relativized, with all paths made relative to the table location. A January 2026 meeting reached general agreement on the approach. Steve Zhang noted that with relative paths, changing a table's location breaks reads and cleanup of files written under the old location; Weeks replied that relocating data is the responsibility of the catalog or implementation and that absolute paths remain available. Weeks opened spec PR #15630, revised it after review, and in May 2026 changed the design to join the table location and the relative path on the '/' separator, ahead of a planned vote.

**Why it matters:** With relative paths, changing a table location no longer leaves old files resolvable, so relocation has to move or copy the whole table.

## Outcome

General agreement on the approach was reported after a January 2026 meeting, and spec PR #15630 is under review. The last message announces a change to separator handling before a vote is sent; no vote appears in this thread. ([message](https://lists.apache.org/thread/9bkbfbxnz52lywzjhy0fjn0tz2d1ss69), `devlist:9bkbfbxnz52lywzjhy0fjn0tz2d1ss69`)

## Positions

- **[[person/talatuyarer|Talat UYARER]]:** Relative paths should be added to the table spec in V4 with a scoped-down proposal. ([message](https://lists.apache.org/thread/nsj0dtxop4h115j6yrcx2vmxpzwt1ow2))
- **[[person/wypoon|Wing Yew Poon]]:** Inferring the table location from the metadata path does not support one copy of metadata with two or more copies of data. ([message](https://lists.apache.org/thread/g3vxkp2x2hl5r8cfjrsobz7f6y2lrytt))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Multiple copies or locations of the same data files under one table is a non-goal and is better handled by engine or FileIO implementations; all paths should be relative to the table location. ([message](https://lists.apache.org/thread/qwojqz44s6sh421r5549m5cps01yp6t3))
- **Steve:** With relative paths a location update is no longer a metadata-only operation, so the spec should acknowledge the behavior change and its effect on snapshot expiration and orphan removal. ([message](https://lists.apache.org/thread/wt3ot7vjrc96m713l9rq8hglo4cvokb3))
- **[[person/danielcweeks|Daniel C. Weeks]]:** How data is relocated when the base location changes is the responsibility of the catalog or implementation, and writers can still produce absolute paths to keep the v1-3 behavior. ([message](https://lists.apache.org/thread/58f3n3k5smbj64r62bpryv4g9d464sgb))
- **[[person/danielcweeks|Daniel C. Weeks]]:** The table location and the relative path should be joined on the URI separator '/', which makes relativization unambiguous for similar paths such as 'table' and 'table_v2'. ([message](https://lists.apache.org/thread/9bkbfbxnz52lywzjhy0fjn0tz2d1ss69))

References: [iceberg#13141](https://github.com/apache/iceberg/issues/13141), [iceberg#15630](https://github.com/apache/iceberg/issues/15630), [iceberg#16174](https://github.com/apache/iceberg/issues/16174), [doc](https://docs.google.com/document/d/1t0RxrK-nsCT83zXeD66kmGx_TMU2X8_xfN1A_k6dCV0)
<!-- kb:generated:end -->

## Notes
