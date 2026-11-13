---
id: thread/t-9da84e6ec274a52c
type: thread
title: Compact bitmap format (Mumbling)
date: '2026-04-20'
url: https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f
kind: discuss
status: open
messages: 4
sources:
- devlist:ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f
refs:
- gh:apache/iceberg#16518
links:
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Compact bitmap format (Mumbling)

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Compact bitmap format](https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f) · **Started:** 2026-04-20 by [[person/rdblue|Ryan Blue]] · **Messages:** 4 (last 2026-05-21) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Ryan Blue proposed a compact bitmap format, called Mumbling, for the manifest deletion vectors that the v4 adaptive metadata tree embeds in the root manifest. Amogh Jahagirdar's measurements showed Roaring adds roughly 500 to 2,000 bytes per bitmap compared with raw bitmaps at the target scale of about 50,000 entries per manifest. Mumbling uses Roaring's ideas with smaller containers; Ryan shared size comparisons, a spec draft and a compact Rust implementation, and said the Roaring community may take it up. Maximilian Michels found the savings compelling but was concerned about maintaining a custom format across all Iceberg implementations unless it becomes part of Roaring. Andrei Tserakhau said other languages should not block it and estimated one to two weeks for a native Go implementation. Ryan then opened PR #16518 with the spec draft, for coordination only; adopting it will need a vote, and he would not wait for Roaring upstream.

**Why it matters:** If adopted, every Iceberg implementation would need to implement a new bitmap format to read v4 root manifests.

## Outcome

PR #16518 adds the draft spec for coordination only; it does not add the format to the table spec, and a vote is expected when the decision to adopt it is made.

## Positions

- **[[person/rdblue|Ryan Blue]]:** Move forward with the Mumbling format because it saves significant space in the root manifest and has a simple spec. ([message](https://lists.apache.org/thread/ccd7tx23fbg4ry8sc3pl7n6np8s8tl5f))
- **[[person/mxm|Maximilian Michels]]:** The savings are compelling, but maintaining a custom bitmap format in every Iceberg implementation is a concern unless Mumbling is included in Roaring. ([message](https://lists.apache.org/thread/g082cxtvbz6d46flmh9gfbr7o2sktbzw))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Other languages should not be a blocker; a native Go implementation is about one to two weeks of isolated work at worst. ([message](https://lists.apache.org/thread/1m39c3mtr2h5c45fs0oqdm5g1woytkxz))
- **[[person/rdblue|Ryan Blue]]:** Commit the spec draft for coordination without committing to the format, hold a vote later, and do not wait for adoption by the Roaring community. ([message](https://lists.apache.org/thread/359ghby6m4nxllzsvc4s6r7c3fx4wzvc))

References: [iceberg#16518](https://github.com/apache/iceberg/issues/16518)
<!-- kb:generated:end -->

## Notes
