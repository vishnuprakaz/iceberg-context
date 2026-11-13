---
id: thread/t-09a6303d5e1af395
type: thread
title: 'Iceberg Rust: moving the DataFusion integration into a separate repository'
date: '2026-09-04'
url: https://lists.apache.org/thread/kyqh5z72qfjknljhm6c5px9ymlrhdycp
kind: discuss
status: consensus
messages: 16
sources:
- devlist:kyqh5z72qfjknljhm6c5px9ymlrhdycp
refs:
- gh:apache/datafusion-iceberg#1
- list:6k5lws31c61y1lx2s34pxo4lmc7334lr
- list:ytb9x7x8ff3b7031kcrc05nzjtmh091s
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:kyqh5z72qfjknljhm6c5px9ymlrhdycp
- rel: started_by
  to: person/kevinjqliu
  confidence: observed
updated: '2026-11-13'
---

# Iceberg Rust: moving the DataFusion integration into a separate repository

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg Rust: moving the DataFusion integration into a separate repository](https://lists.apache.org/thread/kyqh5z72qfjknljhm6c5px9ymlrhdycp) · **Started:** 2026-09-04 by [[person/kevinjqliu|Kevin Liu]] · **Messages:** 16 (last 2026-09-17) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread reached the Iceberg dev list when Kevin Liu added it to a discussion already under way elsewhere, so the original proposal is not among these messages. It concerns moving the Iceberg Rust DataFusion integration into a new repository, apache/datafusion-iceberg. Renjie Liu, Alexander Bailey and Neelesh Salian supported Andrew Lamb's proposal. Lamb filed an infrastructure request and the repository was created on September 9. Asked whether the thread was enough, Lamb said a formal vote should be held in a separate thread in both communities, once there was a repository and a PR to vote on. Gabriel was asked to prepare the PR moving the content, and Kevin Liu approved it. Lamb started a vote on the DataFusion dev list to accept the code and Kevin Liu started the vote on the Iceberg dev list. On September 16 Lamb reported that both votes passed unanimously and that the move could go ahead.

**Why it matters:** The DataFusion integration for Iceberg Rust now lives in apache/datafusion-iceberg rather than in the iceberg-rust repository.

## Outcome

The discussion ended in agreement and the repository apache/datafusion-iceberg was created. Andrew Lamb reported that the separate vote threads on the Iceberg and DataFusion dev lists both passed unanimously. ([message](https://lists.apache.org/thread/9t4l1kp4zjk7cjynd81nlsv2rttjkwcl), `devlist:9t4l1kp4zjk7cjynd81nlsv2rttjkwcl`)

## Positions

- **Andrew Lamb:** The move needs a formal vote in a separate thread in both the Iceberg and DataFusion communities, based on a repository and a PR. ([message](https://lists.apache.org/thread/08o6jbn4dmxbv6vsttbommybk31tn0g4))
- **[[person/nssalian|Neelesh Salian]]:** The integration should move to the new apache/datafusion-iceberg repository. ([message](https://lists.apache.org/thread/tg1pd18jq6bo6y3yrj47qwwddvtgf7bk))
- **[[person/kevinjqliu|Kevin Liu]]:** The PR porting the code to the new repository is approved and the Iceberg side should vote on it. ([message](https://lists.apache.org/thread/1q65f5t3h0v6jsd3fb3mpz7sll8vsq2g))

References: [datafusion-iceberg#1](https://github.com/apache/datafusion-iceberg/issues/1), [thread](https://lists.apache.org/thread/6k5lws31c61y1lx2s34pxo4lmc7334lr), [thread](https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s)
<!-- kb:generated:end -->

## Notes
