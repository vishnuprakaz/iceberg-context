---
id: thread/t-aa8645f8aa979099
type: thread
title: Vote on PyIceberg 0.12.0rc1
date: '2026-08-06'
url: https://lists.apache.org/thread/5qhn33k5kr0t9g3vvqqxc893bs11jxlc
kind: vote
status: open
messages: 6
sources:
- devlist:5qhn33k5kr0t9g3vvqqxc893bs11jxlc
refs:
- gh:apache/iceberg-python#3758
links:
- rel: discussed
  to: initiative/pyiceberg
  confidence: extracted
  source: devlist:5qhn33k5kr0t9g3vvqqxc893bs11jxlc
- rel: started_by
  to: person/rambleraptor
  confidence: observed
updated: '2026-11-13'
---

# Vote on PyIceberg 0.12.0rc1

<!-- kb:generated:start -->
**Thread:** [[VOTE] PyIceberg 0.12.0rc1](https://lists.apache.org/thread/5qhn33k5kr0t9g3vvqqxc893bs11jxlc) · **Started:** 2026-08-06 by [[person/rambleraptor|Alex Stephen]] · **Messages:** 6 (last 2026-08-10) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alex Stephen proposed release candidate 1 as the official PyIceberg 0.12.0 release, with a 72-hour vote. The highlighted features were view support, geometry and geography type support, Python 3.14 support, a new File Format API, and many bug fixes and improvements. Four non-binding +1 votes followed, with verification of signatures, checksums, license headers and tests on macOS and Linux. One voter noted a pre-existing flaky test, `test_add_files_parallelized`, which fails on machines with many cores. Kevin Liu then cast a binding -1 because a user had reported a regression, issue #3758, which he was able to validate; since it is a correctness issue he asked to fix it and raise a new release candidate. The thread ends with that vote and contains no closing message from the release manager.

**Why it matters:** A correctness regression found during the vote means PyIceberg 0.12.0 needs another release candidate.

## Outcome

No result message in the thread. Votes cast: four non-binding +1 and one binding -1, with the -1 asking for a fix and a new release candidate.

## Positions

- **Abnob Doss:** Votes +1 (non-binding) and notes that `test_add_files_parallelized` is a pre-existing flaky test that fails on high-core machines. ([message](https://lists.apache.org/thread/h2qn6rhbrtbq5hx79q18y6pvpxv4fhhv))
- **[[person/kevinjqliu|Kevin Liu]]:** Votes -1 (binding): a validated regression reported in issue #3758 is a correctness issue, so it should be fixed and a new RC raised. ([message](https://lists.apache.org/thread/v27lp9tpqp3t6hkfcbnkqbm4rxfpqf82))

References: [iceberg-python#3758](https://github.com/apache/iceberg-python/issues/3758)
<!-- kb:generated:end -->

## Notes
