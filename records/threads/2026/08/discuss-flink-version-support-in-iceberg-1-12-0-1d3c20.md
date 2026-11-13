---
id: thread/t-1d3c20c5c64f7fcb
type: thread
title: Flink version support in Iceberg 1.12.0
date: '2026-08-27'
url: https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy
kind: discuss
status: consensus
messages: 11
sources:
- devlist:8fsqcovm1cn7zdl571t4f9qlyqgf5qxy
refs:
- gh:apache/iceberg#17845
- gh:apache/iceberg#17849
links:
- rel: started_by
  to: person/pvary
  confidence: observed
updated: '2026-11-13'
---

# Flink version support in Iceberg 1.12.0

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Flink version support in Iceberg 1.12.0](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy) · **Started:** 2026-08-27 by [[person/pvary|Peter Vary]] · **Messages:** 11 (last 2026-08-28) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Péter Váry proposed finalizing the Flink matrix for Iceberg 1.12.0 under an LTS plus two latest releases policy: Flink 1.20, 2.2 and 2.3, after 1.11.0 shipped 1.20, 2.0 and 2.1. He noted the drawback that no Flink 2.x version overlaps between the two releases. Manu Zhang questioned upgrading two versions at once so close to the release. Maximilian Michels supported the policy, opened an upgrade PR, and argued that skipping a minor version is not a problem. Talat Uyarer proposed keeping an overlap by supporting 1.20, 2.1, 2.2 and 2.3 in 1.12.0 and opened a PR doing so. Péter merged that PR and preferred keeping Flink 2.1 so users can upgrade Iceberg and Flink independently; Maximilian agreed to keep 2.1 and proceed with the release. Maximilian's idea of a shared source folder for Flink 2.x versions was deferred until after 1.12.0.

**Why it matters:** Iceberg 1.12.0 ships Flink 1.20, 2.1, 2.2 and 2.3 runtimes, so Flink 2.1 users can upgrade Iceberg without changing Flink version.

## Outcome

PR #17849 was merged, adding Flink 2.2 and 2.3; Flink 2.1 is kept alongside 1.20 for Iceberg 1.12.0, and the release proceeds on that basis. ([message](https://lists.apache.org/thread/rx2z86z66pv293x8t04vm3msclo5xtr8), `devlist:rx2z86z66pv293x8t04vm3msclo5xtr8`)

## Positions

- **[[person/pvary|Peter Vary]]:** Adopt LTS plus the two latest Flink releases, giving Flink 1.20, 2.2 and 2.3 for Iceberg 1.12.0, accepting that Flink 2.x versions do not overlap with 1.11.0. ([message](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy))
- **[[person/manuzhang|Manu Zhang]]:** Concerned about adding two Flink versions at once shortly before the release, with little time left to verify. ([message](https://lists.apache.org/thread/bm24xsb17fxtjrnfyghbb5nxk9hcmvtz))
- **[[person/mxm|Maximilian Michels]]:** Supports LTS plus two latest releases; longer term, Flink versions could share a source folder with only incompatible files overlaid, as Apache Beam does. ([message](https://lists.apache.org/thread/xp8yz32x3dr7dr3b77s7f8dcoymqlr09))
- **[[person/talatuyarer|Talat UYARER]]:** Announce the LTS-plus-two policy for future releases but support Flink 1.20, 2.1, 2.2 and 2.3 in 1.12.0 to keep a version overlap. ([message](https://lists.apache.org/thread/pn16b02gbg31l6nffwwo5hzmroop0703))
- **[[person/mxm|Maximilian Michels]]:** No policy announcement is needed and skipping a Flink or Iceberg version is not an inherent problem; LTS plus two releases matches upstream Flink support. ([message](https://lists.apache.org/thread/o4nh8v3p736nk8w77pm77n3l2klr3bdy))
- **[[person/pvary|Peter Vary]]:** Keep Flink 2.1 for now so Iceberg and Flink can be upgraded independently; removing it later is an easy PR. ([message](https://lists.apache.org/thread/hn9qdnvt6v35okpbpvzcsko983hrq352))

References: [iceberg#17845](https://github.com/apache/iceberg/issues/17845), [iceberg#17849](https://github.com/apache/iceberg/issues/17849)
<!-- kb:generated:end -->

## Notes
