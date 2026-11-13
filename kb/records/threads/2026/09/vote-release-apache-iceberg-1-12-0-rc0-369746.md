---
id: thread/t-36974638264b04f5
type: thread
title: Vote on releasing Apache Iceberg 1.12.0 RC0
date: '2026-09-18'
url: https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb
kind: release-vote
status: withdrawn
messages: 17
sources:
- devlist:7qtxrysl1w5sjs7o74y31snt0jrkf5qb
refs:
- gh:apache/iceberg#16560
- gh:apache/iceberg#16765
- gh:apache/iceberg#18169
- gh:apache/iceberg#18164
- gh:apache/iceberg#18191
- gh:apache/iceberg#15994
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:7qtxrysl1w5sjs7o74y31snt0jrkf5qb
- rel: discussed
  to: initiative/geospatial
  confidence: extracted
  source: devlist:7qtxrysl1w5sjs7o74y31snt0jrkf5qb
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg 1.12.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.12.0 RC0](https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb) · **Started:** 2026-09-18 by [[person/nssalian|Neelesh Salian]] · **Messages:** 17 (last 2026-09-21) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Neelesh Salian proposed RC0 as Apache Iceberg 1.12.0. The replies were non-binding +1 votes with verification reports, plus three issues. Yuya Ebihara noted that 1.12.0 removed the old helper logic for partition statistics and the new logic needs the Hadoop-based Parquet client. Xuanwo and Gianluca Graziadei found third-party doc-site assets (a Bootstrap stylesheet and lottie-player.js) in the source archive without matching LICENSE entries, raised as follow-ups rather than blockers. Steven Wu flagged that PR #16765 changed `toString()` of geometry and geography types to always print the resolved CRS and algorithm; reading stays compatible but written strings change. Xin Huang offered a PR restoring the old output, while Szehon, Anoop, Huaxin and the release manager preferred keeping the change and documenting it as a behavior change. After the fix for the license issue (#18191) merged, the release manager announced a new RC with a new vote thread.

**Why it matters:** 1.12.0 RC0 was replaced by a new candidate over third-party license notices, and 1.12 keeps a geometry/geography type-string change that will be documented as a behavior change.

## Outcome

RC0 was not released: after the fix for the source-archive licensing issue (#18191) was merged, the release manager said a new RC would be cut and voted on in a new thread. Only non-binding +1 votes had been cast; no tally was posted. ([message](https://lists.apache.org/thread/57jh9c9lm0j95o0v7o3zc3dylhcmpzpd), `devlist:57jh9c9lm0j95o0v7o3zc3dylhcmpzpd`)

## Positions

- **Yuya Ebihara:** Votes +1 but notes that the new partition statistics read/write logic requires the Hadoop-based Parquet client, which may be a problem for downstream projects that prohibit such dependencies. ([message](https://lists.apache.org/thread/yrsl0jmnbb6kmgywsxsmxbhocx42l6pb))
- **[[person/Xuanwo|Hao Ding]]:** The source archive bundles a Bootstrap CSS file without the MIT permission notice or a root LICENSE entry; this should be fixed for the next release and is not a blocker. ([message](https://lists.apache.org/thread/ko87p9b1tq4ojzq0fpjbnog2rsrpo0w2))
- **[[person/GGraziadei|Gianluca Graziadei]]:** lottie-player.js is also bundled without a license entry, and a pre-existing NoSuchMethodError occurs when reading variant columns with commons-lang3 older than 3.13; neither is a regression or blocker. ([message](https://lists.apache.org/thread/9nohzxmm1pxfbr30hmlht3xxyfns2670))
- **[[person/stevenzwu|Steven Wu]]:** The geometry/geography `toString()` change is a behavior change the community should be aware of; he is fine with 1.12 keeping it because reads are compatible. ([message](https://lists.apache.org/thread/op7tsgngmw17yoth6gr6m37r2mj4q2gw))
- **[[person/huan233usc|Xin Huang]]:** Prefers restoring the old `toString()` output while still serializing explicit CRS and algorithm (PR #18169), but will follow the community's preference. ([message](https://lists.apache.org/thread/k2r9hmxhyl2533kkvpqhss01bkxrc1fv))
- **[[person/szehon-ho|Szehon Ho]]:** Keep the `toString()` change in 1.12 and list it under behavior changes: it is clearer, matches the serialization spec and simplifies the UDF definition-id work. ([message](https://lists.apache.org/thread/1k4bzksqm7vsllvw68495og8grv8gbwh))
- **[[person/anoopj|Anoop Johnson]]:** Keeping the behavior change is reasonable, with the revert PR as a fallback if there are objections. ([message](https://lists.apache.org/thread/62pqj5vnf6nsgl63mw2vbo4djr19r71g))
- **[[person/huaxingao|Huaxin Gao]]:** Keep the #16765 change and document it; old metadata still loads and equal Geography types now print the same, which the UDF work needs. ([message](https://lists.apache.org/thread/lohd2lhx14ly3bd0n1spv8kkyovbl61j))

References: [iceberg#16560](https://github.com/apache/iceberg/issues/16560), [iceberg#16765](https://github.com/apache/iceberg/issues/16765), [iceberg#18169](https://github.com/apache/iceberg/issues/18169), [iceberg#18164](https://github.com/apache/iceberg/issues/18164), [iceberg#18191](https://github.com/apache/iceberg/issues/18191), [iceberg#15994](https://github.com/apache/iceberg/issues/15994)
<!-- kb:generated:end -->

## Notes
