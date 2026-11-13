---
id: thread/t-444dbbca629c1693
type: thread
title: Iceberg Rust / pyiceberg-core 0.10.1
date: '2026-07-27'
url: https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l
kind: discuss
status: consensus
messages: 4
sources:
- devlist:nxqw16p5wt8oorrtsbc28phkosp0g55l
refs:
- gh:apache/iceberg-rust#2907
links:
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Iceberg Rust / pyiceberg-core 0.10.1

<!-- kb:generated:start -->
**Thread:** [[DISCUSSION] Iceberg Rust / pyiceberg-core 0.10.1](https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l) · **Started:** 2026-07-27 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 4 (last 2026-07-28) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones reported that the pyiceberg-core release artifacts for 0.10.0 were wrong: they were built from the main branch instead of the 0.10.0 release, and have been yanked after Vova Kot pointed out the problem. The plan is a 0.10.1 release with zero changes, simply a new set of artifacts targeting the right branch, to be published soon; a tracking issue was opened in iceberg-rust. kevinjqliu confirmed he yanked pyiceberg-core 0.10.0 from PyPI because it contained code that was not part of the 0.10.0 release, and suggested starting the 0.10.1 release from the same commit hash as 0.10.0 with a vote thread. liurenjie1024 said the cause was his manual publishing of pyiceberg-core from the wrong branch. No objections to the plan were raised.

**Why it matters:** pyiceberg-core 0.10.0 on PyPI was yanked because it was built from main, so users need 0.10.1 instead.

## Outcome

No objections to a no-change 0.10.1 release from the 0.10.0 commit; pyiceberg-core 0.10.0 was yanked from PyPI. The vote is to happen in a separate thread.

## Positions

- **Danny Jones:** Run a 0.10.1 release with zero changes to republish artifacts from the right branch, as soon as possible. ([message](https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l))
- **[[person/kevinjqliu|Kevin Liu]]:** pyiceberg-core 0.10.0 was yanked from PyPI; start 0.10.1 from the same commit hash as 0.10.0 and open a vote thread. ([message](https://lists.apache.org/thread/3xvhyn1wbq1d2clyxxbnyqolk6mc9g87))
- **[[person/liurenjie1024|Renjie Liu]]:** The wrong artifacts resulted from manually publishing pyiceberg-core from the wrong branch. ([message](https://lists.apache.org/thread/dflwkt9s64sc55zbt7zcqz6bh9bj8lz8))

References: [iceberg-rust#2907](https://github.com/apache/iceberg-rust/issues/2907)
<!-- kb:generated:end -->

## Notes
