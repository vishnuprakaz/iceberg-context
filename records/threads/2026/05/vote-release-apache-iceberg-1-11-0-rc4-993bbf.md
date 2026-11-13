---
id: thread/t-993bbf42f9af82cf
type: thread
title: Release Apache Iceberg 1.11.0 RC4
date: '2026-05-15'
url: https://lists.apache.org/thread/x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp
kind: release-vote
status: passed
messages: 19
sources:
- devlist:x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp
refs:
- gh:apache/iceberg#16396
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp
- rel: started_by
  to: person/aihuaxu
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg 1.11.0 RC4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.11.0 RC4](https://lists.apache.org/thread/x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp) · **Started:** 2026-05-15 by [[person/aihuaxu|Aihua Xu]] · **Messages:** 19 (last 2026-05-19) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

aihuaxu proposed release candidate 4 (commit 6976e020, tag apache-iceberg-1.11.0-rc4) as Apache Iceberg 1.11.0, with a 72-hour vote. Voters verified signatures, checksums, license checks and source builds; kevinjqliu also ran PyIceberg integration, Yuya Ebihara confirmed Trino CI was green across several catalogs, and bryanck reported validation tests passing on a fork in a test environment. Jean-Baptiste Onofré voted +1 while listing minor LICENSE and NOTICE issues in the AWS, Azure, GCP and Flink runtime bundles, such as files packaged twice and missing NOTICE content from some dependencies. kevinjqliu opened issue #16396 to track those fixes, and aihuaxu said they would be fixed in a following release. No -1 votes were cast and the vote passed.

**Why it matters:** Apache Iceberg 1.11.0 was approved for release, with bundle LICENSE and NOTICE clean-ups deferred to a later release.

## Outcome

Passed with +1: 6 binding and 7 non-binding; no +0 or -1 votes. ([message](https://lists.apache.org/thread/qb466tcgdj4w9lpfj6ly42k9jk4vnqm0), `devlist:qb466tcgdj4w9lpfj6ly42k9jk4vnqm0`)

## Positions

- **Jean-Baptiste Onofré:** Votes +1 but notes minor LICENSE and NOTICE issues in the bundle and Flink runtime jars, including duplicate packaging and missing NOTICE content from some dependencies. ([message](https://lists.apache.org/thread/ddw8cvyrvypoolmzhd673s5wglhdpd5f))
- **[[person/kevinjqliu|Kevin Liu]]:** Verified that the open-api jar is not published and the Kafka Connect artifact contains only Iceberg code, and filed an issue to track the license follow-ups. ([message](https://lists.apache.org/thread/vng16frrh45q2nzzryt2yl2vqfqkw4n1))
- **[[person/aihuaxu|Aihua Xu]]:** The license nits will be fixed in a following release and the 1.11.0 release moves forward. ([message](https://lists.apache.org/thread/fl0b1mn0b64x7hxh3kw1mr3xzgxnjwl2))

References: [iceberg#16396](https://github.com/apache/iceberg/issues/16396)
<!-- kb:generated:end -->

## Notes
