---
id: thread/t-a9927e0959daeebf
type: thread
title: Vote to release Apache Iceberg Terraform Provider v0.2.0 RC1
date: '2026-10-26'
url: https://lists.apache.org/thread/7qo3nydsv4fcx9z94p1gb53oqydsl5oc
kind: release-vote
status: passed
messages: 6
sources:
- devlist:7qo3nydsv4fcx9z94p1gb53oqydsl5oc
refs:
- gh:apache/terraform-provider-iceberg#154
links:
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:7qo3nydsv4fcx9z94p1gb53oqydsl5oc
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Vote to release Apache Iceberg Terraform Provider v0.2.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE][Terraform] Release Apache Iceberg Terraform Provider v0.2.0 RC1](https://lists.apache.org/thread/7qo3nydsv4fcx9z94p1gb53oqydsl5oc) · **Started:** 2026-10-26 by [[person/zeroshade|Matthew Topol]] · **Messages:** 6 (last 2026-10-29) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Matt Topol (zeroshade) proposed release candidate 1 of the Apache Iceberg Terraform provider v0.2.0, based on commit 5f869f0, with a source release and convenience binaries for the Terraform and OpenTofu registries attached to a GitHub prerelease. Voters verified signatures and checksums, built the provider, ran the tests and checked the LICENSE and NOTICE files. Alex Stephen (rambleraptor) noted a licensing fix found by Matt in terraform-provider-iceberg PR #154 and hoped the candidate could still be used, since BSD-3 and Go licenses are already listed for other dependencies. Kevin Liu reported a few non-blocking license and notice nits that he would track on GitHub, and Russell Spitzer said the Roaring Bitmap license issue from that PR is not a blocker. Sung Yun also verified the convenience binaries. Matt Topol closed the vote as passed and said he would proceed with the release.

**Why it matters:** The release is meant to get the provider into the Terraform Registry.

## Outcome

The vote passed with 4 binding +1 votes, 1 non-binding +1 vote and no -1 votes. ([message](https://lists.apache.org/thread/zfc96ktz5vhxn1gymv9lohlzj3prq9jm), `devlist:zfc96ktz5vhxn1gymv9lohlzj3prq9jm`)

## Positions

- **[[person/rambleraptor|Alex Stephen]]:** The candidate should go ahead despite the license fix in PR #154, since BSD-3 and Go licenses are already listed for other dependencies. ([message](https://lists.apache.org/thread/79zn6m0lcc5vw5406xvmm21ccgqqg4zo))
- **[[person/kevinjqliu|Kevin Liu]]:** The candidate verifies, and a few license and notice nits are non-blocking and will be tracked on GitHub. ([message](https://lists.apache.org/thread/w4rwgb65wky36pmfto69jjddd70trm9d))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The Roaring Bitmap license issue is not a blocker for the release. ([message](https://lists.apache.org/thread/hnmw12qb28yt9hv0ptzzkfb3zvnmxzss))

References: [terraform-provider-iceberg#154](https://github.com/apache/terraform-provider-iceberg/issues/154)
<!-- kb:generated:end -->

## Notes
