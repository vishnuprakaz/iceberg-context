---
id: thread/t-dc8bbfb604d6e4b4
type: thread
title: iceberg-cpp 0.4.0 release
date: '2026-09-18'
url: https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1
kind: release-planning
status: consensus
messages: 11
sources:
- devlist:yfjj2p96w4s0fd7067fkr5dgknwp62d1
refs:
- gh:apache/iceberg-cpp#955
- gh:apache/iceberg-cpp#637
- gh:apache/iceberg-cpp#926
links:
- rel: started_by
  to: person/manuzhang
  confidence: observed
updated: '2026-11-13'
---

# iceberg-cpp 0.4.0 release

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] iceberg-cpp 0.4.0 release](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1) · **Started:** 2026-09-18 by [[person/manuzhang|Manu Zhang]] · **Messages:** 11 (last 2026-09-22) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Manu Zhang proposed starting the iceberg-cpp 0.4.0 release and volunteered as release manager with support from Gang Wu. Since 0.3.0 in June, 174 commits had landed, covering Iceberg v3 types, column default values, deletion vectors and row lineage, table update operations such as MergeAppend and RowDelta, parallel manifest reads and writes, REST SigV4 and OAuth2 token exchange, an initial Hive Metastore client, and removal of Meson build support. Variant types, encryption and Puffin statistics were deferred. Gang Wu saw no blockers and noted the Arrow C++ variant PR would take a while. Junwang Zhao asked to postpone to late October to include CherryPickOperation and RewriteManifests; Manu preferred faster, smaller releases with another one in late October, and Junwang agreed. A tracking issue (apache/iceberg-cpp#955) was created for the release.

**Why it matters:** iceberg-cpp 0.4.0 carries v3 support, while variant, encryption, CherryPickOperation and RewriteManifests wait for a later release.

## Outcome

The request to postpone was dropped and the 0.4.0 release went ahead with Manu Zhang as release manager; a tracking issue (apache/iceberg-cpp#955) was created. ([message](https://lists.apache.org/thread/ds15k34koh25c1z7ck3qlqd1sdc9b345), `devlist:ds15k34koh25c1z7ck3qlqd1sdc9b345`)

## Positions

- **[[person/manuzhang|Manu Zhang]]:** Start the 0.4.0 release now and defer variant, encryption and Puffin statistics to a later release. ([message](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1))
- **[[person/wgtmac|Gang Wu]]:** No blockers; variant can move to 0.5.0 because the Arrow C++ variant PR will take a while to merge. ([message](https://lists.apache.org/thread/l3d3t7d1cp22mf7rr1lfczltnmo2ld87))
- **[[person/zhjwpku|Junwang Zhao]]:** Asked to postpone to late October so CherryPickOperation and RewriteManifests could be included. ([message](https://lists.apache.org/thread/bqhtn73jd7mkgwqbwl1yy77ky9s0fqjr))
- **[[person/manuzhang|Manu Zhang]]:** Prefers faster, smaller releases for early user feedback, with another release in late October for the remaining features. ([message](https://lists.apache.org/thread/gt6tcpmhmfkp77tt3f1qy2zp17s88z9w))

References: [iceberg-cpp#955](https://github.com/apache/iceberg-cpp/issues/955), [iceberg-cpp#637](https://github.com/apache/iceberg-cpp/issues/637), [iceberg-cpp#926](https://github.com/apache/iceberg-cpp/issues/926)
<!-- kb:generated:end -->

## Notes
