---
id: thread/t-1579f8b73b2494e8
type: thread
title: Vote on releasing Apache Iceberg C++ 0.4.0 RC0
date: '2026-09-22'
url: https://lists.apache.org/thread/qqrg1l5qntf2m8h11gvopyvojrffgbw3
kind: release-vote
status: passed
messages: 9
sources:
- devlist:qqrg1l5qntf2m8h11gvopyvojrffgbw3
- devlist:99vvhs027n70r95qqfbnqobjs8fktb1s
refs:
- gh:apache/iceberg-cpp#965
links:
- rel: discussed
  to: initiative/iceberg-cpp
  confidence: extracted
  source: devlist:qqrg1l5qntf2m8h11gvopyvojrffgbw3
- rel: started_by
  to: person/manuzhang
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg C++ 0.4.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg C++ 0.4.0 RC0](https://lists.apache.org/thread/qqrg1l5qntf2m8h11gvopyvojrffgbw3) · **Started:** 2026-09-22 by [[person/manuzhang|Manu Zhang]] · **Messages:** 9 (last 2026-09-25) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Manu (manuzhang) proposed release candidate RC0 of Apache Iceberg C++ 0.4.0, based on commit 64dc66f159bd62c9817a96d74cbce767268934d0, with a vote open for at least 72 hours. Voters reported verifying the checksum and signature, that the source matches the commit, license files, and the build, tests and install on macOS, Debian and Ubuntu, mostly through dev/release/verify_rc.sh. Xuanwo made one non-blocking suggestion for the next release: update the MurmurHash3 paths in LICENSE to src/iceberg/util/murmurhash3_internal.*; he opened an issue to track it. All replies were +1. The thread ends with Kevin Liu's vote and does not contain a result message.

**Why it matters:** The only issue raised against the 0.4.0 candidate was a LICENSE path correction deferred to the next release.

## Outcome

No result is stated in the thread. The replies are +1 votes: three marked binding (wgtmac, liurenjie1024, kevinjqliu) and five marked non-binding, with no 0 or -1 votes.

**Result posted in a separate thread on 2026-09-26:** [[RESULT][VOTE] Release Apache Iceberg C++ 0.4.0 RC0](https://lists.apache.org/thread/99vvhs027n70r95qqfbnqobjs8fktb1s) (`devlist:99vvhs027n70r95qqfbnqobjs8fktb1s`). Outcome read from that message: passed.

## Positions

- **[[person/Xuanwo|Hao Ding]]:** The candidate verifies; for the next release the MurmurHash3 paths in LICENSE should be updated, which does not block this one. ([message](https://lists.apache.org/thread/0lbcx65phho0ytbd0h69cr5crk5lb23m))
- **[[person/manuzhang|Manu Zhang]]:** The candidate verifies on macOS arm64, and the LICENSE path suggestion is tracked in a new issue. ([message](https://lists.apache.org/thread/g54w7clwr5y0tkfz14xoq2o7lg8tcgqb))

References: [iceberg-cpp#965](https://github.com/apache/iceberg-cpp/issues/965)
<!-- kb:generated:end -->

## Notes
