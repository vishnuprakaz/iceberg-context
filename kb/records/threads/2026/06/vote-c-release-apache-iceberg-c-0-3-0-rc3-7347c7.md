---
id: thread/t-7347c79968e5d24f
type: thread
title: Vote on releasing Apache Iceberg C++ 0.3.0 RC3
date: '2026-06-10'
url: https://lists.apache.org/thread/8b145f8kw1mwy0ggn9jyfj6khbkb70l3
kind: release-vote
status: passed
messages: 17
sources:
- devlist:8b145f8kw1mwy0ggn9jyfj6khbkb70l3
refs: []
links:
- rel: discussed
  to: initiative/iceberg-cpp
  confidence: extracted
  source: devlist:8b145f8kw1mwy0ggn9jyfj6khbkb70l3
- rel: started_by
  to: person/zhjwpku
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg C++ 0.3.0 RC3

<!-- kb:generated:start -->
**Thread:** [[VOTE][C++] Release Apache Iceberg C++ 0.3.0 RC3](https://lists.apache.org/thread/8b145f8kw1mwy0ggn9jyfj6khbkb70l3) · **Started:** 2026-06-10 by [[person/zhjwpku|Junwang Zhao]] · **Messages:** 17 (last 2026-06-14) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Junwang (zhjwpku) proposed release candidate 3 of Apache Iceberg C++ 0.3.0, based on commit 0284683f, with a vote open for at least 72 hours. Voters verified the candidate on macOS, Ubuntu and Debian, mostly with the `verify_rc.sh` script. Gang (wgtmac) noted that REST catalog verification can be skipped with `VERIFY_REST=0` if libcurl causes problems. Matt (zeroshade) hit such a problem on Ubuntu 25.10: the default libcurl package does not install `libcurl.pc`, so CMake could not find the system curl and failed instead of vendoring or fetching it. He said this was not blocking and suggested updating the README and the CMake configuration; Junwang agreed to fall back to a vendored curl when no system installation is found. The vote passed with 3 binding and 10 non-binding +1 votes, and the release manager said he would proceed with the release and write the release blog.

**Why it matters:** Apache Iceberg C++ 0.3.0 was approved for release, with a follow-up to make the build work when the system libcurl development files are missing.

## Outcome

Passed with 3 binding +1 votes and 10 non-binding +1 votes; no -1 or +0 votes were reported. ([message](https://lists.apache.org/thread/07hqqx26qty7bkdhmdn692objnkpb4l9), `devlist:07hqqx26qty7bkdhmdn692objnkpb4l9`)

## Positions

- **[[person/zeroshade|Matthew Topol]]:** Votes +1 (binding); the build should vendor or fetch libcurl when the system package is not found instead of failing, and the README should say so, but this does not block the release. ([message](https://lists.apache.org/thread/ndn5r2kn7v9zw9lnjqoffz6wyxg6cm17))
- **[[person/zhjwpku|Junwang Zhao]]:** Agrees the build should fall back to a vendored curl when no system installation is found and will work on a fix and a README update. ([message](https://lists.apache.org/thread/00xddzj8vlm5ncqgzb6t3j2j56wln6cs))
<!-- kb:generated:end -->

## Notes
