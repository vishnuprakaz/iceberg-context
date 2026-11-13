---
id: thread/t-b838f79509420b04
type: thread
title: Should incremental (append) scan semantics be part of the spec?
date: '2026-07-23'
url: https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057
kind: discuss
status: no-conclusion
messages: 5
sources:
- devlist:o0wsy3jot3vos7zpqop4xk48k0hzf057
refs:
- gh:apache/iceberg-python#3512
- gh:apache/iceberg-cpp#559
- gh:apache/iceberg-rust#2337
- yt:G5m039mXgG4
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:o0wsy3jot3vos7zpqop4xk48k0hzf057
- rel: discussed
  to: initiative/v4-general
  confidence: extracted
  source: devlist:o0wsy3jot3vos7zpqop4xk48k0hzf057
- rel: started_by
  to: person/xanderbailey
  confidence: observed
updated: '2026-11-13'
---

# Should incremental (append) scan semantics be part of the spec?

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Should incremental (append) scan semantics be part of the spec?](https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057) · **Started:** 2026-07-23 by [[person/xanderbailey|Xander]] · **Messages:** 5 (last 2026-08-04) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alexander Bailey asked whether incremental append scan semantics should be written into the table spec. Today the spec is silent, the Java IncrementalAppendScan is the de facto reference, and PyIceberg, iceberg-cpp and iceberg-rust each follow it. He noted that the REST scan-planning API already exposes start-snapshot-id (exclusive) and end-snapshot-id (inclusive), so catalogs must produce incremental plans whose correctness is defined only by Java's behaviour, and argued the result should not depend on where the scan is planned. He listed ambiguities to pin down, such as ancestry traversal and what happens when the start is not an ancestor of the end. xndai said the REST plan API returns files and so only covers the append-only case, and that should be clarified. Ryan Blue noted that v4 changes are planned to tighten change-detection requirements so the spec supports all incremental scans. Manu Zhang pointed to the V4 Single File Commits sync to follow that work.

**Why it matters:** Until the spec defines incremental scans, implementations and REST catalogs have only the Java behaviour to follow.

## Outcome

No decision on adding incremental append scan semantics to the current spec; the proposer was pointed to the V4 single file commits sync, where change-detection requirements are being worked on.

## Positions

- **Alexander Bailey:** Incremental append scan semantics should be codified in the spec so client-side and catalog-side planning return the same files, rather than relying on Java's behaviour. ([message](https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057))
- **[[person/xndai|Xiening Dai]]:** The REST plan API returns a file set and so can only support append-only incremental scans; that limit should be stated, and scanning deletes and updates between snapshots needs a separate design. ([message](https://lists.apache.org/thread/rydk12wxqs73ynfj80v21xbsgq520q9h))
- **[[person/rdblue|Ryan Blue]]:** V4 changes are planned to tighten change-detection requirements so the spec supports all kinds of incremental scans without relying on one implementation's conventions. ([message](https://lists.apache.org/thread/ol5mok9821468bfkctq4hm638pynvjvb))

References: [iceberg-python#3512](https://github.com/apache/iceberg-python/issues/3512), [iceberg-cpp#559](https://github.com/apache/iceberg-cpp/issues/559), [iceberg-rust#2337](https://github.com/apache/iceberg-rust/issues/2337), [video](https://www.youtube.com/watch?v=G5m039mXgG4)
<!-- kb:generated:end -->

## Notes
