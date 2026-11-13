---
id: thread/t-418bd34af8479e56
type: thread
title: Vote on releasing Apache Iceberg C++ 0.3.0 RC1
date: '2026-06-09'
url: https://lists.apache.org/thread/fkvc8wmzokym5hmtv8gb3w6b9k8fgbp9
kind: release-vote
status: withdrawn
messages: 8
sources:
- devlist:fkvc8wmzokym5hmtv8gb3w6b9k8fgbp9
refs:
- gh:apache/iceberg-cpp#710
links:
- rel: started_by
  to: person/zhjwpku
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg C++ 0.3.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE][C++] Release Apache Iceberg C++ 0.3.0 RC1](https://lists.apache.org/thread/fkvc8wmzokym5hmtv8gb3w6b9k8fgbp9) · **Started:** 2026-06-09 by [[person/zhjwpku|Junwang Zhao]] · **Messages:** 8 (last 2026-06-09) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zhjwpku proposed release candidate RC1 of Apache Iceberg C++ 0.3.0, based on commit 9dbad3139df6fcdfc8d3f0bf6127dff9611ca9cd, with a vote open for at least 72 hours. Five non-binding +1 votes arrived within hours, some reporting verification of the signature and checksum, the CMake build, unit tests and the install step. manuzhang then reported that the generated `version.h` header is not installed, said he was unsure whether that blocks the release, and linked a fix. The release manager replied that the problem had not been found in previous releases, and that the vote would be aborted and an RC2 prepared.

**Why it matters:** Iceberg C++ 0.3.0 RC1 was abandoned because the installed package lacked the generated version.h header.

## Outcome

The release manager aborted the vote to prepare RC2 after the missing version.h install was reported. Five non-binding +1 votes had been cast. ([message](https://lists.apache.org/thread/ssxvs911p9h9t31738f0mq441zby89zj), `devlist:ssxvs911p9h9t31738f0mq441zby89zj`)

## Positions

- **[[person/manuzhang|Manu Zhang]]:** The generated version.h header is not installed, which may be a release blocker; a fix is available. ([message](https://lists.apache.org/thread/kort9x9zrnh8h6zg53df3phvr2n1gtfn))
- **[[person/zhjwpku|Junwang Zhao]]:** The issue warrants aborting this vote and preparing RC2. ([message](https://lists.apache.org/thread/ssxvs911p9h9t31738f0mq441zby89zj))

References: [iceberg-cpp#710](https://github.com/apache/iceberg-cpp/issues/710)
<!-- kb:generated:end -->

## Notes
