---
id: thread/t-7d24fa0351cadc2c
type: thread
title: 'Vote: add stats-only fields for v4'
date: '2026-10-28'
url: https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t
kind: vote
status: passed
messages: 17
sources:
- devlist:f7nwynr69g18kj61nt5h1f45cn8g768t
refs:
- gh:apache/iceberg#18405
- list:t4nm0blbo33y5fnkcok6lrmdc4k4toxr
links:
- rel: discussed
  to: initiative/v4-content-stats
  confidence: extracted
  source: devlist:f7nwynr69g18kj61nt5h1f45cn8g768t
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Vote: add stats-only fields for v4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add stats-only fields for v4](https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t) · **Started:** 2026-10-28 by [[person/rdblue|Ryan Blue]] · **Messages:** 17 (last 2026-10-31) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Ryan Blue called a vote on adding stats-only fields to the table spec, following an earlier discussion thread, with the changes in PR #18405. The change adds a stats-fields list that assigns table field IDs so that statistics for partition fields and for expressions such as to_lower_case can be stored in the content_stats struct. The vote was open for 72 hours. Every reply was a +1 vote, with no discussion of the content in the thread. Ryan Blue closed the vote three days later, stating that it passed with 15 +1 votes and no -1 or -0 votes.

**Why it matters:** V4 content stats can now carry statistics for partition fields and expressions through dedicated stats-only field IDs.

## Outcome

Passed with 15 +1 votes and no -1 or -0, as stated in the result message, which does not split binding and non-binding. ([message](https://lists.apache.org/thread/d90t8lbgomb23d8dtllnncsbx27g69k3), `devlist:d90t8lbgomb23d8dtllnncsbx27g69k3`)

## Positions

- **[[person/rdblue|Ryan Blue]]:** Add a stats-fields list assigning field IDs so stats for partition fields and expressions can be stored in content_stats. ([message](https://lists.apache.org/thread/f7nwynr69g18kj61nt5h1f45cn8g768t))

References: [iceberg#18405](https://github.com/apache/iceberg/issues/18405), [thread](https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr)
<!-- kb:generated:end -->

## Notes
