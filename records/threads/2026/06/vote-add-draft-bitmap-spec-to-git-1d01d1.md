---
id: thread/t-1d01d1d5d742962e
type: thread
title: Add draft bitmap spec to git
date: '2026-06-04'
url: https://lists.apache.org/thread/59bn4jty8jmtbks8td8zfqodkcpro1hw
kind: vote
status: open
messages: 9
sources:
- devlist:59bn4jty8jmtbks8td8zfqodkcpro1hw
refs:
- gh:apache/iceberg#16518
links:
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Add draft bitmap spec to git

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add draft bitmap spec to git](https://lists.apache.org/thread/59bn4jty8jmtbks8td8zfqodkcpro1hw) · **Started:** 2026-06-04 by [[person/rdblue|Ryan Blue]] · **Messages:** 9 (last 2026-06-09) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rdblue called a vote to add a draft spec for the Mumbling bitmap format to version control through PR #16518. He stated that the vote is only about getting the draft into git so that the spec and implementations can be iterated on, which will inform whether to use the format in v4 metadata; it does not mean the format is used in tables or elsewhere, and such uses would need future votes. Micah Kornfield voted +1, left comments aimed at clarity for implementers, and asked what the decision factors would be for actually using the format; the thread has no answer to that. amogh-jahagirdar had a comment about exception offsets. pvary supported an initial draft, noting that good compression is needed if delete vectors are to be stored in metadata files. All replies were +1; the bundle contains no result message.

**Why it matters:** Adding the draft lets implementations be built against a written bitmap spec before any vote on using it in v4 metadata.

## Outcome

No result message is in the thread. The messages show eight +1 votes: three marked binding, two marked non-binding and three unmarked; no -1 votes.

## Positions

- **[[person/rdblue|Ryan Blue]]:** The draft Mumbling bitmap spec should be added to git to iterate on it and on implementations, without committing to using the format in tables. ([message](https://lists.apache.org/thread/59bn4jty8jmtbks8td8zfqodkcpro1hw))
- **Micah Kornfield:** Votes +1, suggests clarifications for implementers and asks what will decide whether the format is actually used. ([message](https://lists.apache.org/thread/z6oph21mggjw2jtjrwl6od4g5b57j2q9))
- **[[person/pvary|Peter Vary]]:** Supports adding an initial draft because good compression is needed for delete vectors stored in metadata files, even if details still need work. ([message](https://lists.apache.org/thread/y11xth7bw68bq46hrkbjh6vtk2y8b5bp))

References: [iceberg#16518](https://github.com/apache/iceberg/issues/16518)
<!-- kb:generated:end -->

## Notes
