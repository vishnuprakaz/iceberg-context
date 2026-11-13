---
id: thread/t-db8ec8a6f20fbd0d
type: thread
title: 'Spec: replace per-column tight_bounds with file-level tight_stats in v4'
date: '2026-10-22'
url: https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl
kind: vote
status: passed
messages: 14
sources:
- devlist:txorrcfb5ft95q8kq2gypdcj1gd7zzxl
- devlist:g7qvlhkt3kchgf7sgjdcr0z9sksbqgq6
refs:
- gh:apache/iceberg#18585
- doc:13DbwnwKQXjvY3vRcFJo-qVAQWk-GB4zLzzYmFdPntZg
links:
- rel: started_by
  to: person/anoopj
  confidence: observed
updated: '2026-11-13'
---

# Spec: replace per-column tight_bounds with file-level tight_stats in v4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Spec: Replace per-column tight_bounds with file-level tight_stats in v4](https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl) · **Started:** 2026-10-22 by [[person/anoopj|Anoop Johnson]] · **Messages:** 14 (last 2026-10-25) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

anoopj called a vote on the V4 spec change in PR #18585 that replaces the per-column tight_bounds field with a single file-level tight_stats flag on the tracked file. Under the change, tightness is tracked once per file and covers all statistics (bounds and null, NaN and value counts), so metadata-only queries can trust the counts as well. When the flag is absent, readers must assume stats are not tight. A deletion vector no longer implicitly makes stats wide: tight_stats is the authoritative indicator, and engines may retighten stats without rewriting data files. The vote was open for 72 hours. Thirteen replies were all +1; anuragmantri added that the change also applies well to column updates. The bundle contains no message announcing the result.

**Why it matters:** If adopted, V4 writers and readers use one per-file flag to decide whether all of a file's statistics can be trusted, and engines can retighten stats without rewriting data.

## Outcome

No result message is in the thread. The messages show 13 +1 votes, nine marked binding and four non-binding; no -1 votes.

**Result posted in a separate thread on 2026-10-27:** [[RESULT][VOTE] Spec: Replace per-column tight_bounds with file-level tight_stats in v4](https://lists.apache.org/thread/g7qvlhkt3kchgf7sgjdcr0z9sksbqgq6) (`devlist:g7qvlhkt3kchgf7sgjdcr0z9sksbqgq6`). Outcome read from that message: passed.

## Positions

- **[[person/anoopj|Anoop Johnson]]:** Stats tightness should be tracked once per file with a tight_stats flag covering bounds and counts, with absence meaning not tight and deletion vectors no longer implying wide stats. ([message](https://lists.apache.org/thread/txorrcfb5ft95q8kq2gypdcj1gd7zzxl))
- **[[person/anuragmantri|Anurag Mantripragada]]:** Votes +1 and notes the change applies nicely to column updates too. ([message](https://lists.apache.org/thread/04nj579mlkdllb866lz5661wlqjz7d2m))

References: [iceberg#18585](https://github.com/apache/iceberg/issues/18585), [doc](https://docs.google.com/document/d/13DbwnwKQXjvY3vRcFJo-qVAQWk-GB4zLzzYmFdPntZg)
<!-- kb:generated:end -->

## Notes
