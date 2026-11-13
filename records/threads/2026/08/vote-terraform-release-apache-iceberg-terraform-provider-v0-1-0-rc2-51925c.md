---
id: thread/t-51925c451e4cf72d
type: thread
title: 'Release vote: Apache Iceberg Terraform Provider v0.1.0 RC2'
date: '2026-08-11'
url: https://lists.apache.org/thread/xwqz0j6g2fcvq4hf5xs63ll4137ch0n6
kind: release-vote
status: open
messages: 4
sources:
- devlist:xwqz0j6g2fcvq4hf5xs63ll4137ch0n6
refs: []
links:
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Release vote: Apache Iceberg Terraform Provider v0.1.0 RC2

<!-- kb:generated:start -->
**Thread:** [[VOTE][Terraform] Release Apache Iceberg Terraform Provider v0.1.0 RC2](https://lists.apache.org/thread/xwqz0j6g2fcvq4hf5xs63ll4137ch0n6) · **Started:** 2026-08-11 by [[person/zeroshade|Matthew Topol]] · **Messages:** 4 (last 2026-08-25) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zeroshade (Matt) proposed release candidate 2 of the Apache Iceberg Terraform provider v0.1.0, based on commit 186d4f48b9e98386b044e1367d6fdf8d47a3ff8d, with the source release on dist.apache.org and convenience binaries for the Terraform and OpenTofu registries attached to a GitHub prerelease. rambleraptor voted +1 non-binding after the release script, RAT check, build, tests and checksums succeeded. JB Onofré voted 0 non-binding: the source distribution is correct, but the LICENSE in the binary distribution omits four dependencies that come transitively from iceberg-go v0.6.0 (hashicorp golang-lru, golang.org/x/oauth2, twmb/avro and clipperhouse/uax29) and lists some that are not in the distribution. Matt replied that he is preparing a PR to fix the LICENSE issues. No vote result is stated in the thread.

**Why it matters:** The first Terraform provider release is held up by licensing details of the binary distribution.

## Outcome

No result is announced. The thread shows one non-binding +1 and one non-binding 0, and the release manager is preparing a fix for the binary LICENSE.

## Positions

- **[[person/rambleraptor|Alex Stephen]]:** +1 non-binding; the release script, RAT check, build, tests and checksums all pass. ([message](https://lists.apache.org/thread/l7mgmm4bg5xvc0wy414ss43v56kf5vok))
- **Jean-Baptiste Onofré:** 0 non-binding; the source distribution is correct, but the binary distribution's LICENSE misses some bundled dependencies and lists others that are not included, and should be fixed. ([message](https://lists.apache.org/thread/lfqdckm995dggtprfyo6r4mr3rqpf518))
- **[[person/zeroshade|Matthew Topol]]:** Is preparing a PR to fix the LICENSE issues. ([message](https://lists.apache.org/thread/d595jc4jg6hqtgnb4ytnp2jx4dgwgbob))
<!-- kb:generated:end -->

## Notes
