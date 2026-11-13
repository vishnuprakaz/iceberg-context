---
id: thread/t-97f54e45553021e0
type: thread
title: 1.11.1 and 1.10.3 patch releases
date: '2026-06-06'
url: https://lists.apache.org/thread/k5pfk4rork0mp2p303pd70q9nx0tsl9w
kind: discuss
status: consensus
messages: 4
sources:
- devlist:k5pfk4rork0mp2p303pd70q9nx0tsl9w
refs:
- gh:apache/iceberg#16699
links:
- rel: started_by
  to: person/amogh-jahagirdar
  confidence: observed
updated: '2026-11-13'
---

# 1.11.1 and 1.10.3 patch releases

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] 1.11.1 / 1.10.3 patch releases?](https://lists.apache.org/thread/k5pfk4rork0mp2p303pd70q9nx0tsl9w) · **Started:** 2026-06-06 by [[person/amogh-jahagirdar|Amogh Jahagirdar]] · **Messages:** 4 (last 2026-06-06) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Amogh Jahagirdar opened a discussion on patch releases after finding a bug where the Spark rewrite manifests procedure does not carry over first row IDs correctly, for which he has a fix in PR #16699. He asked which other fixes people want included, reminding that patch releases typically cover correctness fixes, security fixes or significant regressions. He also asked whether v3 metadata correctness fixes should keep being backported to 1.10 or only go to 1.11, and argued for continuing on 1.10 because many clients run it and a patch upgrade is easier than a minor upgrade. Steven Wu supported both a 1.11.1 and a 1.10.3 release and noted that a 1.11.1 milestone already exists. Yufei Gu agreed. Dan Weeks agreed as well, provided the 1.10 backports stay narrow.

**Why it matters:** The 1.10 line continues to receive v3 correctness fixes, so users on 1.10 can pick them up with a patch upgrade.

## Outcome

All repliers supported doing both 1.11.1 and 1.10.3 patch releases, with narrow backports to 1.10.

## Positions

- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Do patch releases, and keep backporting v3 metadata correctness fixes to 1.10 since many clients are on it. ([message](https://lists.apache.org/thread/k5pfk4rork0mp2p303pd70q9nx0tsl9w))
- **[[person/stevenzwu|Steven Wu]]:** Supports both 1.11.1 and 1.10.3; a 1.11.1 milestone already exists. ([message](https://lists.apache.org/thread/o81rwpwhcvvro6qlxyfmwzostjr9zg1l))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Supports it as long as the 1.10 backports are kept narrow. ([message](https://lists.apache.org/thread/dxkp581cs9kq2s1qh68dxtgctvffvxyj))

References: [iceberg#16699](https://github.com/apache/iceberg/issues/16699)
<!-- kb:generated:end -->

## Notes
