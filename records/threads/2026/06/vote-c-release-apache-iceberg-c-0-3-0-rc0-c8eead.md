---
id: thread/t-c8eead2c8a5ef24b
type: thread
title: Release Apache Iceberg C++ 0.3.0 RC0
date: '2026-06-06'
url: https://lists.apache.org/thread/vo8wfvp4cncggng31c5l6ksh7nnv1bsm
kind: release-vote
status: withdrawn
messages: 13
sources:
- devlist:vo8wfvp4cncggng31c5l6ksh7nnv1bsm
refs:
- gh:apache/iceberg-cpp#705
- gh:apache/avro#3788
links:
- rel: started_by
  to: person/zhjwpku
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg C++ 0.3.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE][C++] Release Apache Iceberg C++ 0.3.0 RC0](https://lists.apache.org/thread/vo8wfvp4cncggng31c5l6ksh7nnv1bsm) · **Started:** 2026-06-06 by [[person/zhjwpku|Junwang Zhao]] · **Messages:** 13 (last 2026-06-08) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zhjwpku proposed release candidate 0 of Apache Iceberg C++ 0.3.0, based on commit ae29c3d4. Several +1 votes followed. stevenzwu voted +1 but reported that dev/release/verify_rc.sh failed out of the box on recent macOS because the vendored avro-cpp pins fmt 10.2.1, which no longer compiles under Apple Clang 21; installing a newer fmt with Homebrew worked around it. wgtmac and zhjwpku said this is a known issue already fixed upstream in avro-cpp (apache/avro PR #3788) and will go away when the dependency is bumped. manuzhang pointed out that the RC source builds with a 0.3.0-SNAPSHOT version, which a REST client would send in its User-Agent header; zhjwpku agreed and opened iceberg-cpp PR #705. zhjwpku then aborted the vote to fix both issues and prepare RC1.

## Outcome

The release manager aborted the vote because of the -SNAPSHOT suffix in the CMake version string and a verification issue caused by the vendored fmt version; RC1 is to follow. Only +1 votes had been cast. ([message](https://lists.apache.org/thread/sf2xb2h3qo60vzrm0r8xqyhqdq59k5q5), `devlist:sf2xb2h3qo60vzrm0r8xqyhqdq59k5q5`)

## Positions

- **[[person/stevenzwu|Steven Wu]]:** Votes +1; the verify script fails on recent macOS because the vendored avro-cpp pins fmt 10.2.1, which is not a blocker but needs a follow-up. ([message](https://lists.apache.org/thread/l05dk23t42ntbhxbl8g5d249rh4b2tph))
- **[[person/wgtmac|Gang Wu]]:** The fmt problem is already fixed in avro-cpp, which now uses std::format, and will disappear once the avro-cpp version is bumped. ([message](https://lists.apache.org/thread/lfcd8z9j02oc09qpwf94pg60ovmgltmt))
- **[[person/manuzhang|Manu Zhang]]:** An RC should not carry a SNAPSHOT suffix in its version, since a REST client built from it would send iceberg-cpp/0.3.0-SNAPSHOT as User-Agent. ([message](https://lists.apache.org/thread/f01pyvzc97j932cf64bq6b02kl6bj9mw))
- **[[person/zhjwpku|Junwang Zhao]]:** The RC source should not build as 0.3.0-SNAPSHOT; both that and the vendored fmt verification issue will be fixed in RC1. ([message](https://lists.apache.org/thread/sf2xb2h3qo60vzrm0r8xqyhqdq59k5q5))

References: [iceberg-cpp#705](https://github.com/apache/iceberg-cpp/issues/705), [avro#3788](https://github.com/apache/avro/issues/3788)
<!-- kb:generated:end -->

## Notes
