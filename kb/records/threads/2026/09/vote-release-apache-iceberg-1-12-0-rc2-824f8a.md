---
id: thread/t-824f8a51f5314747
type: thread
title: 'Vote: release Apache Iceberg 1.12.0 RC2'
date: '2026-09-29'
url: https://lists.apache.org/thread/26g46qtgy3nr435wdg5wh53q48k17zo3
kind: release-vote
status: passed
messages: 5
sources:
- devlist:26g46qtgy3nr435wdg5wh53q48k17zo3
refs: []
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:26g46qtgy3nr435wdg5wh53q48k17zo3
- rel: started_by
  to: person/Kurtiscwright
  confidence: observed
updated: '2026-11-13'
---

# Vote: release Apache Iceberg 1.12.0 RC2

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.12.0 RC2](https://lists.apache.org/thread/26g46qtgy3nr435wdg5wh53q48k17zo3) · **Started:** 2026-09-29 by [[person/Kurtiscwright|Kurtis Wright]] · **Messages:** 5 (last 2026-09-29) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This is the vote on release candidate 2 of Apache Iceberg 1.12.0; the body of the opening message is not in the bundle. Three binding +1 votes are recorded. Kevin Liu verified signatures, checksums and licenses, ran the build and tests, ran examples on Spark and ran the candidate against the PyIceberg CI. He noted that LICENSE and NOTICE looked good after recent fixes, and that an automated scan had flagged a few correctness issues that also exist in 1.11 or earlier and that he did not consider release blockers. Szehon Ho checked signatures, licenses and the tag and ran a local Spark 4.2.0 test. Amogh Jahagirdar ran build, test and integration tests against RustFS. Neelesh Salian then announced that the voting had concluded and passed, with an official result email to follow.

## Outcome

The vote was announced as concluded and passed; no tally is given in that message. The thread shows three binding +1 votes. ([message](https://lists.apache.org/thread/xcgc68wcjsffmbr8bczv8n9t8zn9q7d5), `devlist:xcgc68wcjsffmbr8bczv8n9t8zn9q7d5`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** Votes +1 binding after verification; correctness issues flagged by a scan predate 1.12 and are not release blockers. ([message](https://lists.apache.org/thread/g845vlpb0qwk7dcvf0y136o5xdnocb3g))
<!-- kb:generated:end -->

## Notes
