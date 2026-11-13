---
id: thread/t-43bc363d6f78db31
type: thread
title: Vote on releasing Apache Iceberg 1.11.0 RC1
date: '2026-05-13'
url: https://lists.apache.org/thread/j1v2yc69sbh7p85oftcy9tdqph5sxqt7
kind: release-vote
status: withdrawn
messages: 7
sources:
- devlist:j1v2yc69sbh7p85oftcy9tdqph5sxqt7
refs:
- gh:apache/iceberg#15470
- gh:apache/iceberg#16284
- gh:apache/iceberg#16303
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:j1v2yc69sbh7p85oftcy9tdqph5sxqt7
- rel: started_by
  to: person/aihuaxu
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg 1.11.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.11.0 RC1](https://lists.apache.org/thread/j1v2yc69sbh7p85oftcy9tdqph5sxqt7) · **Started:** 2026-05-13 by [[person/aihuaxu|Aihua Xu]] · **Messages:** 7 (last 2026-05-15) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This part of the 1.11.0 RC1 vote thread is about what should go into the next candidate. Aihua, the release manager, asked how critical a long-standing bug was and whether it should be added to the 1.11.0 milestone, and mentioned PR #15470. Huaxin answered that it is a correctness issue affecting readers such as Trino, Impala, Comet and iceberg-rust, but that it already exists in 1.10 and so is not a hard blocker. Steve Loughran said the SerializableFileIOWithSize fix in #16284 makes the file length more of an issue, especially for the GCS FileIO, but that #15470 was still stabilising and would be a risky last-minute patch. Kevin Liu agreed not to wait for it. Aihua reported that the last Spark backport, #16303, had merged and no blockers remained in the milestone, then announced RC4 for vote, RC2 and RC3 having been built but skipped as further backports and issues were found.

**Why it matters:** Iceberg 1.11.0 went to RC4 without PR #15470, leaving a pre-existing correctness issue for a later release.

## Outcome

RC1 was superseded: the release manager published RC4 for a new vote, after RC2 and RC3 were built but not put to a vote. ([message](https://lists.apache.org/thread/n2pvczw75t92070yk5opyjpscx0o1jxj), `devlist:n2pvczw75t92070yk5opyjpscx0o1jxj`)

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** The bug is a correctness issue but exists in 1.10 already, so it is not a hard blocker for 1.11.0. ([message](https://lists.apache.org/thread/kl4ffxynzompo1svwt29bmydol7b1x9d))
- **[[person/steveloughran|Steve Loughran]]:** The #16284 fix makes file length matter more, notably for GCS FileIO, but #15470 is still stabilising and is a dangerous last-minute patch. ([message](https://lists.apache.org/thread/0n1hb3lrgsz8jm8q1skgzs9mf4rvosjz))
- **[[person/aihuaxu|Aihua Xu]]:** With the last Spark backport merged and no blockers left in the milestone, the release should move on to the next candidate without #15470, which is not a regression. ([message](https://lists.apache.org/thread/csplkdc6c2w8whtg98gbort4jbh2g1tx))
- **[[person/kevinjqliu|Kevin Liu]]:** The release should not wait for #15470, with the final call left to the release manager. ([message](https://lists.apache.org/thread/2dws3p3ozk67k177nvy8pvjtkjz02z3w))

References: [iceberg#15470](https://github.com/apache/iceberg/issues/15470), [iceberg#16284](https://github.com/apache/iceberg/issues/16284), [iceberg#16303](https://github.com/apache/iceberg/issues/16303)
<!-- kb:generated:end -->

## Notes
