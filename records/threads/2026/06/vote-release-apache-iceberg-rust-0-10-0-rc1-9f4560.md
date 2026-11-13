---
id: thread/t-9f4560b42e64c533
type: thread
title: Vote to release Apache Iceberg Rust 0.10.0 RC1
date: '2026-06-25'
url: https://lists.apache.org/thread/yk7o9v6f44tym72rmr5qpz9dzxbwh870
kind: release-vote
status: open
messages: 5
sources:
- devlist:yk7o9v6f44tym72rmr5qpz9dzxbwh870
refs:
- gh:apache/iceberg-rust#2725
- gh:apache/iceberg-rust#2740
links:
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Vote to release Apache Iceberg Rust 0.10.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.10.0 RC1](https://lists.apache.org/thread/yk7o9v6f44tym72rmr5qpz9dzxbwh870) · **Started:** 2026-06-25 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 5 (last 2026-06-29) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones called a vote on Apache Iceberg Rust 0.10.0 RC1 (tag v0.10.0-rc.1), with Shawn Chang supporting the release as committer. Three non-binding +1 votes followed, reporting verified signatures, checksums, license headers, builds and tests. Manu Zhang needed a temporary libpython symlink on macOS for Python-linked Rust test binaries and filed a follow-up fix. Danny Jones then voted -1 (non-binding) on his own candidate, citing an issue opened for a regression since 0.9.1: a user can override snapshot summary properties such as added-records after they are computed, which can cause a panic when the value cannot be deserialized as an integer. He reported that his verification was otherwise successful and apologized for the churn. The thread ends there, with no message stating a result or announcing a new release candidate.

## Outcome

No result message is in the thread. Votes cast: three non-binding +1, then a non-binding -1 from the release manager over a regression (iceberg-rust issue #2725).

## Positions

- **[[person/manuzhang|Manu Zhang]]:** The candidate verified on macOS, though Python-linked Rust test binaries needed a temporary libpython symlink, for which a fix was filed. ([message](https://lists.apache.org/thread/ryv9q2pnntdhytzxtp19268hn6hwrf9h))
- **Danny Jones:** The candidate should not be released because of a regression since 0.9.1 in which overridden summary properties can cause a panic. ([message](https://lists.apache.org/thread/fsk5qr6q27fv5q4s1nl30pptj4ypx57q))

References: [iceberg-rust#2725](https://github.com/apache/iceberg-rust/issues/2725), [iceberg-rust#2740](https://github.com/apache/iceberg-rust/issues/2740)
<!-- kb:generated:end -->

## Notes
