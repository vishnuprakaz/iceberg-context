---
id: thread/t-e6327b02ad166780
type: thread
title: Deprecating Spark 3.4
date: '2025-09-17'
url: https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv
kind: discuss
status: consensus
messages: 34
sources:
- devlist:n8qy5nsdw35vjog5lb4kp15989b800cv
refs:
- gh:apache/iceberg#14098
- gh:apache/iceberg#14099
- gh:apache/iceberg#14122
links:
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:n8qy5nsdw35vjog5lb4kp15989b800cv
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:n8qy5nsdw35vjog5lb4kp15989b800cv
- rel: started_by
  to: person/kevinjqliu
  confidence: observed
updated: '2026-11-13'
---

# Deprecating Spark 3.4

<!-- kb:generated:start -->
**Thread:** [[Discuss] Deprecating Spark 3.4](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv) · **Started:** 2025-09-17 by [[person/kevinjqliu|Kevin Liu]] · **Messages:** 34 (last 2026-05-20) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Kevin Liu proposed marking Spark 3.4, which had reached end of life upstream, as deprecated in Iceberg 1.11 and removing it in 1.12. The proposal drew many +1s. Anton Okolnychyi and Eduard Tudenhöfner questioned the deprecate-then-remove-a-release-later rule and favoured removing it sooner, because old Spark modules slow down format work; Parth Chandra and Huaxin Gao asked to keep 3.4 longer because Comet still supports it. The docs status was changed to Deprecated in October 2025 (PR #14099). In January 2026 Kevin proposed releasing 1.11 with Spark 3.4, with no obligation to backport everything, and removing the module right after. In May 2026 he reported that the removal PR (#14122) was merged and that 1.11.0 is the last Iceberg version supporting Spark 3.4. Manu Zhang noted fixes may still ship on the 1.11.x branch.

**Why it matters:** Changes on main no longer need a Spark 3.4 backport, and users on Spark 3.4 must stay on the Iceberg 1.11 line.

## Outcome

Spark 3.4 was marked Deprecated in the docs (PR #14099) and the removal PR (#14122) was merged in May 2026; 1.11.0 is the last Iceberg version with Spark 3.4 support. ([message](https://lists.apache.org/thread/lzc0ls4zbtj8bhv5r1s8n3qk0v7qhfsr), `devlist:lzc0ls4zbtj8bhv5r1s8n3qk0v7qhfsr`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** Mark Spark 3.4 deprecated in 1.11 and remove it in 1.12, as it is end-of-life upstream. ([message](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv))
- **[[person/aokolnychyi|Anton Okolnychyi]]:** Questions keeping the deprecate-then-remove model, since older Spark modules lag in features and have become a liability that slows format work such as row IDs. ([message](https://lists.apache.org/thread/6s17zrsmfhdsg25nkfy4clqtyq97vsyb))
- **Eduard Tudenhöfner:** Remove Spark 3.4 in the next release; users who need it can stay on Iceberg 1.10. ([message](https://lists.apache.org/thread/wgvv4olykqoctbxh4frok6f4q0d7ltb2))
- **[[person/steveloughran|Steve Loughran]]:** Making Hadoop 3.4.1 the base version already makes Iceberg partly incompatible with Spark 3.4, as shown by classpath failures in a PR using BulkDelete. ([message](https://lists.apache.org/thread/sjrg9ldh4520f9946ng3djllf5zlld5d))
- **Parth Chandra:** Asked for one more Iceberg release with Spark 3.4 so Comet users on 3.4 do not have to build their own. ([message](https://lists.apache.org/thread/r369zpsmx163xntlzpzfdh3w0fgr8wly))
- **[[person/huaxingao|Huaxin Gao]]:** Keep Spark 3.4 for a couple more versions instead of removing it in 1.11. ([message](https://lists.apache.org/thread/ptf4xoj8qsm1pcy59sno7rymrh7jkgy9))
- **[[person/kevinjqliu|Kevin Liu]]:** Release 1.11 with Spark 3.4 without requiring full backports, then remove spark/v3.4 immediately afterwards and mark it end-of-life. ([message](https://lists.apache.org/thread/2ppvhglts8qr5vdwm7wbdb56b9w0ddg4))
- **[[person/manuzhang|Manu Zhang]]:** Formalize the same deprecate, release, remove sequence in the multi-engine support doc for Spark and Flink versions. ([message](https://lists.apache.org/thread/svxf04pyx05hx3om2rzhzkgy6m1w2n9k))
- **[[person/manuzhang|Manu Zhang]]:** Spark 3.4 is not fully end-of-life yet because it stays on the 1.11.x branch, which may see more releases. ([message](https://lists.apache.org/thread/lw13hgc1gryonwk5pjd01sw0b5mbwk8o))

References: [iceberg#14098](https://github.com/apache/iceberg/issues/14098), [iceberg#14099](https://github.com/apache/iceberg/issues/14099), [iceberg#14122](https://github.com/apache/iceberg/issues/14122)
<!-- kb:generated:end -->

## Notes
