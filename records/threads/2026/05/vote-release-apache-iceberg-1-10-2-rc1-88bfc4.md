---
id: thread/t-88bfc4197adf37a9
type: thread
title: 'Release vote: Apache Iceberg 1.10.2 RC1'
date: '2026-05-14'
url: https://lists.apache.org/thread/o5rmmlqvyl6my1p5mr6jxxo8cs0lvyo1
kind: release-vote
status: passed
messages: 12
sources:
- devlist:o5rmmlqvyl6my1p5mr6jxxo8cs0lvyo1
refs: []
links:
- rel: started_by
  to: person/amogh-jahagirdar
  confidence: observed
updated: '2026-11-13'
---

# Release vote: Apache Iceberg 1.10.2 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.10.2 RC1](https://lists.apache.org/thread/o5rmmlqvyl6my1p5mr6jxxo8cs0lvyo1) · **Started:** 2026-05-14 by [[person/amogh-jahagirdar|Amogh Jahagirdar]] · **Messages:** 12 (last 2026-05-18) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Amogh Jahagirdar proposed release candidate 1 of Apache Iceberg 1.10.2, built from commit 57396d628cb9f92e121f9c2919398475393f0a3a (tag apache-iceberg-1.10.2-rc1), with a 72-hour vote. Voters verified signatures, checksums, license files, the source build and tests. Russell Spitzer and Eduard Tudenhöfner noted that a NOTICE copyright line on the 1.10.x branch still reads 2017-2025 and both said it does not block the release. Kevin Liu confirmed the open-api jar is not published in this release, unlike 1.10.1, and that the kafka-connect jar still is, as expected. Yuya Ebihara reported Trino CI is green against the staged artifacts across several catalogs, and roryqi ran tests against Gravitino. Amogh closed the vote on May 18th and announced that the release candidate passed.

**Why it matters:** 1.10.2 is approved as a patch release on the 1.10 line.

## Outcome

The vote passed with 5 binding and 5 non-binding +1 votes, and no +0 or -1 votes. ([message](https://lists.apache.org/thread/dry06oboxj8ww6v3z4j52zg5fs00dvny), `devlist:dry06oboxj8ww6v3z4j52zg5fs00dvny`)

## Positions

- **[[person/RussellSpitzer|Russell Spitzer]]:** +1 binding; the NOTICE copyright year was not bumped on the 1.10.x branch, which should be cleaned up but does not block the release. ([message](https://lists.apache.org/thread/ptdcp81xcmt01gc1tygj91zcdq9fr5tj))
- **[[person/kevinjqliu|Kevin Liu]]:** +1 binding; LICENSE and NOTICE match main, the open-api jar is no longer published and the kafka-connect jar is still published as expected. ([message](https://lists.apache.org/thread/k6wpt88k0ok6yz7yd2byfkhzfns86wgl))
- **Yuya Ebihara:** +1 non-binding; Trino CI passes against the staged repository with HMS, Glue, JDBC, REST, Nessie and Snowflake catalogs. ([message](https://lists.apache.org/thread/lpnl4vs602gbot7nzd1ddc2b1zfnd5yr))
<!-- kb:generated:end -->

## Notes
