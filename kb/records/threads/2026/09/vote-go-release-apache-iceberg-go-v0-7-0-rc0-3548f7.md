---
id: thread/t-3548f77d85b2a887
type: thread
title: Vote on releasing Apache Iceberg Go v0.7.0 RC0
date: '2026-09-28'
url: https://lists.apache.org/thread/18mcytdbd953cdwz5wsvzx6sbqzsvofh
kind: release-vote
status: passed
messages: 5
sources:
- devlist:18mcytdbd953cdwz5wsvzx6sbqzsvofh
- devlist:k8lo7j1xfq2kq1f0tblvz8kklc49g6tj
refs:
- gh:apache/iceberg-go#2069
links:
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:18mcytdbd953cdwz5wsvzx6sbqzsvofh
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg Go v0.7.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE][Go] Release Apache Iceberg Go v0.7.0 RC0](https://lists.apache.org/thread/18mcytdbd953cdwz5wsvzx6sbqzsvofh) · **Started:** 2026-09-28 by [[person/zeroshade|Matthew Topol]] · **Messages:** 5 (last 2026-09-30) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zeroshade proposed release candidate RC0 of Apache Iceberg Go v0.7.0, based on commit 89a9104ec3639d38ab07e4461721cb5270e95571, with a vote open for at least 72 hours. Neelesh Salian verified the signature, checksum, license files and headers, that the tarball matches the tag, and the build and unit tests on Go 1.25.9. He flagged, as not a blocker, that the test puffin/TestReaderPreservesLZ4ChecksumError fails on Go 1.27.1 while passing on 1.25.9, and opened a fix. Xuanwo saw the same failure on Go 1.27.1, noted the call still rejected the corrupted input, and considered it non-blocking. Russell Spitzer cast a binding +1 after running the verification suite. The thread contains no result message.

**Why it matters:** A Puffin test in iceberg-go fails on Go 1.27.1 and needs the proposed fix before that Go version is added to CI.

## Outcome

No result is stated in the thread. The replies are +1 votes: one marked binding (RussellSpitzer) and three marked non-binding, with no 0 or -1 votes.

**Result posted in a separate thread on 2026-10-01:** [[RESULT][VOTE][Go] Release Apache Iceberg Go v0.7.0 RC0](https://lists.apache.org/thread/k8lo7j1xfq2kq1f0tblvz8kklc49g6tj) (`devlist:k8lo7j1xfq2kq1f0tblvz8kklc49g6tj`). Outcome read from that message: passed.

## Positions

- **[[person/nssalian|Neelesh Salian]]:** The candidate verifies; a Puffin test fails on Go 1.27.1 but passes on the targeted Go 1.25.9, which is not a blocker and has a fix proposed. ([message](https://lists.apache.org/thread/m7nswpbdbon71ykmg4dopy2qqqxhty59))
- **[[person/Xuanwo|Hao Ding]]:** The candidate verifies with 3,344 tests passing on Go 1.25.9; the Go 1.27.1 failure is an error-message assertion and is non-blocking. ([message](https://lists.apache.org/thread/6sfhg7z7rqt4nxc3m9pgt40354vbgnw1))

References: [iceberg-go#2069](https://github.com/apache/iceberg-go/issues/2069)
<!-- kb:generated:end -->

## Notes
