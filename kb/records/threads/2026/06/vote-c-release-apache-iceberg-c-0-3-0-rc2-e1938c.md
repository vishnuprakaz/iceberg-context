---
id: thread/t-e1938ca21167e827
type: thread
title: Release Apache Iceberg C++ 0.3.0 RC2
date: '2026-06-09'
url: https://lists.apache.org/thread/x5y5h0yk8vwzgm7r5b78o0tmp442hyky
kind: release-vote
status: withdrawn
messages: 10
sources:
- devlist:x5y5h0yk8vwzgm7r5b78o0tmp442hyky
refs:
- gh:apache/iceberg-cpp#717
links:
- rel: discussed
  to: initiative/iceberg-cpp
  confidence: extracted
  source: devlist:x5y5h0yk8vwzgm7r5b78o0tmp442hyky
- rel: started_by
  to: person/zhjwpku
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg C++ 0.3.0 RC2

<!-- kb:generated:start -->
**Thread:** [[VOTE][C++] Release Apache Iceberg C++ 0.3.0 RC2](https://lists.apache.org/thread/x5y5h0yk8vwzgm7r5b78o0tmp442hyky) · **Started:** 2026-06-09 by [[person/zhjwpku|Junwang Zhao]] · **Messages:** 10 (last 2026-06-10) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zhjwpku proposed release candidate 2 of Apache Iceberg C++ 0.3.0, based on commit b6508226. wgtmac and manuzhang voted +1 (non-binding). zeroshade voted -1 (binding): on Ubuntu 25.10 the verify script needed meson and gtest/gmock that are not listed as requirements, and linking libiceberg_rest.so failed because the libcurl pulled in through the cpr dependency was not built as position-independent code. zhjwpku replied that meson is not required and googletest should be fetched by CMake. kevinjqliu suggested running the verify script in a GitHub workflow; wgtmac said one already exists, viewed the problems as third-party dependency issues that should not block the release, and proposed making the script vendor third-party libraries. zhjwpku then aborted the vote, citing an issue in how cpr is resolved, addressed by iceberg-cpp PR #717, and announced an RC3 vote.

## Outcome

The release manager aborted the vote because of an issue with how the cpr dependency is resolved; the fix went into RC3, for which a new vote thread was announced. Votes before the abort: two +1 non-binding and one -1 binding. ([message](https://lists.apache.org/thread/5p3frrkhnjcfvq4hzmlnlh9tjrhy72pg), `devlist:5p3frrkhnjcfvq4hzmlnlh9tjrhy72pg`)

## Positions

- **[[person/zeroshade|Matthew Topol]]:** Votes -1 (binding) because the shared library link fails on Ubuntu 25.10 when the fetched libcurl is not built with position-independent code; the unlisted verify script requirements need not block. ([message](https://lists.apache.org/thread/p4l3clp7z7kknwbjlzytnj3xk9502w6g))
- **[[person/zhjwpku|Junwang Zhao]]:** Meson is not required since the verify script depends on CMake, and googletest should be made available automatically by FetchContent. ([message](https://lists.apache.org/thread/ozclnzp7vkkm1zs7pjz6krktwkrf0n6k))
- **[[person/wgtmac|Gang Wu]]:** The reported problems are third-party dependency issues that should not block the release; the verify script should vendor third-party libraries and fail fast on an incompatible libcurl. ([message](https://lists.apache.org/thread/8g5hgy6y07koyyxg0tls5jt511m9djt6))
- **[[person/kevinjqliu|Kevin Liu]]:** Use a GitHub workflow to run the verification script in a clean workspace. ([message](https://lists.apache.org/thread/p23go2wzy30t5g5brdxy8wk6zbbqhkmc))

References: [iceberg-cpp#717](https://github.com/apache/iceberg-cpp/issues/717)
<!-- kb:generated:end -->

## Notes
