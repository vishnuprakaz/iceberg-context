---
id: thread/t-a1beaa110569764f
type: thread
title: 1.11.1 and 1.10.3 patch releases
date: '2026-06-06'
url: https://lists.apache.org/thread/nh8zy6s9kbhd5mvcctfhl71jzgcc1krs
kind: discuss
status: consensus
messages: 14
sources:
- devlist:nh8zy6s9kbhd5mvcctfhl71jzgcc1krs
refs:
- gh:apache/iceberg#16699
- gh:apache/iceberg#16214
- gh:apache/iceberg#15911
- gh:apache/iceberg#16692
- gh:apache/iceberg#15470
links:
- rel: started_by
  to: person/aihuaxu
  confidence: observed
updated: '2026-11-13'
---

# 1.11.1 and 1.10.3 patch releases

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] 1.11.1 / 1.10.3 patch releases?](https://lists.apache.org/thread/nh8zy6s9kbhd5mvcctfhl71jzgcc1krs) · **Started:** 2026-06-06 by [[person/aihuaxu|Aihua Xu]] · **Messages:** 14 (last 2026-06-27) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The body of the opening message is not in the bundle; the replies show a proposal for 1.11.1 and 1.10.3 patch releases built around a v3 correctness fix (PR #16699). Everyone who replied supported both releases. Amogh Jahagirdar created a 1.10.3 milestone and added a fix that preserves encryption metadata when DVs change (PR #15911) and a default-value fix for evaluation against Parquet metrics (PR #16692); he also reported the 1.11.x branch had been created. Matt Butrovich offered a fix for manifest delete file size after table rewrite (PR #15470) as a backport candidate for both lines. Kevin Liu asked to fix the iceberg-rest-fixture Docker image in 1.11.x (PR #16214). On milestones, Amogh said every fix going into 1.10.3 should also go into 1.11.1, while fixes that are not critical correctness issues should go only into 1.11.

**Why it matters:** It sets the backport rule for the two patch lines: critical correctness fixes go to both 1.10.x and 1.11.x, other fixes only to 1.11.x.

## Outcome

All replies supported doing both 1.11.1 and 1.10.3; a 1.10.3 milestone and the 1.11.x branch were created and candidate fixes were being collected. No release candidate is announced in the thread.

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** Supports both releases; the fix is a contained v3 correctness fix and v3 correctness fixes should keep being backported to 1.10. ([message](https://lists.apache.org/thread/1rsv46wrdtbgq65p05wtk158py54chqv))
- **[[person/kevinjqliu|Kevin Liu]]:** Supports both patch lines and wants the iceberg-rest-fixture Docker image fixed in 1.11.x so publishing can be re-enabled. ([message](https://lists.apache.org/thread/nx0fv7991kv1k3vk8w9lj1ohfx90wv1b))
- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Include the fix preserving encryption metadata for DV changes in 1.10.3, because the issue amounts to producing incorrect V3 metadata. ([message](https://lists.apache.org/thread/5mwjy0mr3yj7z34qkkrrk6mj82dmbt7m))
- **[[person/mbutrovich|Matt Butrovich]]:** The fix for manifest delete file size after table rewrite is a backport candidate for both 1.10.x and 1.11.x. ([message](https://lists.apache.org/thread/326gz77wzgcw3gb325214fgq8nmfgs7q))
- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Everything patched into 1.10.3 should be in 1.11.1, but non-critical fixes should go only to 1.11 to limit the backport burden. ([message](https://lists.apache.org/thread/jbtw1zk7w7qk77bo7dr1h87nmj6zon3o))

References: [iceberg#16699](https://github.com/apache/iceberg/issues/16699), [iceberg#16214](https://github.com/apache/iceberg/issues/16214), [iceberg#15911](https://github.com/apache/iceberg/issues/15911), [iceberg#16692](https://github.com/apache/iceberg/issues/16692), [iceberg#15470](https://github.com/apache/iceberg/issues/15470)
<!-- kb:generated:end -->

## Notes
