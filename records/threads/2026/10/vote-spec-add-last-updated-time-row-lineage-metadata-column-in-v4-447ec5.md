---
id: thread/t-447ec59251977712
type: thread
title: 'Vote: add the _last_updated_time row lineage metadata column in v4'
date: '2026-10-30'
url: https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv
kind: vote
status: open
messages: 14
sources:
- devlist:pwzmjq579svsw7qh0nzpqwg25lqrdgrv
refs:
- gh:apache/iceberg#18526
- gh:apache/iceberg#16294
- list:cln7xtjy9kw2096gzqlg5c4gg8b9td10
links:
- rel: started_by
  to: person/stevenzwu
  confidence: observed
updated: '2026-11-13'
---

# Vote: add the _last_updated_time row lineage metadata column in v4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Spec: Add _last_updated_time row lineage metadata column in v4](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv) · **Started:** 2026-10-30 by [[person/stevenzwu|Steven Wu]] · **Messages:** 14 (last 2026-11-03) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Steven Wu called a 72-hour vote on spec PR #18526, which adds a reserved _last_updated_time metadata column (timestamptz) to row lineage in v4 tables, recording the timestamp of the snapshot that last updated a row. It adds an optional snapshot_timestamp tracking field in v4 manifests that writers leave null for added entries and entries modified by column files; a null value is inherited from the snapshot's timestamp-ms on read. Upgrading to v4 needs no manifest rewrite. The change builds on the v4 requirement for monotonically increasing snapshot timestamps (#16294). Many +1 votes followed. Dan Weeks voted +1 binding but said the type should be timestamp rather than timestamptz, which he did not consider blocking. The last message, from Ryan Blue, said the change is close but not ready until it has had more editing. No result is announced in the thread.

**Why it matters:** The column would let engines answer when a row last changed, and its type (timestamp or timestamptz) was still questioned during the vote.

## Outcome

No result message is in the thread. The replies show five +1 votes marked binding and seven marked non-binding, with no -1; Ryan Blue's final message said the change is not ready without more editing.

## Positions

- **[[person/stevenzwu|Steven Wu]]:** Add _last_updated_time and a snapshot_timestamp manifest field so users can query when a row was last updated without mapping sequence numbers to snapshots that may have expired. ([message](https://lists.apache.org/thread/pwzmjq579svsw7qh0nzpqwg25lqrdgrv))
- **[[person/danielcweeks|Daniel C. Weeks]]:** +1 binding, but the type should be timestamp rather than timestamptz since no time zone should be involved; not a blocker for the vote. ([message](https://lists.apache.org/thread/hdyk9kcwgf0yo7fhnq81r3hocb0dqvwz))
- **[[person/rdblue|Ryan Blue]]:** The change is close but is not ready until it has had more editing. ([message](https://lists.apache.org/thread/71ohx3rjm2qm9k1dw13c47oqsk2nhgry))

References: [iceberg#18526](https://github.com/apache/iceberg/issues/18526), [iceberg#16294](https://github.com/apache/iceberg/issues/16294), [thread](https://lists.apache.org/thread/cln7xtjy9kw2096gzqlg5c4gg8b9td10)
<!-- kb:generated:end -->

## Notes
