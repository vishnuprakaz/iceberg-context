---
id: thread/t-e7c5d0287bca96b4
type: thread
title: Release Apache Iceberg Terraform Provider v0.1.0 RC0
date: '2026-07-13'
url: https://lists.apache.org/thread/lfr1kb253m99dg0mbdzpm6g1k3nbd6fc
kind: release-vote
status: open
messages: 5
sources:
- devlist:lfr1kb253m99dg0mbdzpm6g1k3nbd6fc
refs:
- gh:apache/terraform-provider-iceberg#72
links:
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:lfr1kb253m99dg0mbdzpm6g1k3nbd6fc
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg Terraform Provider v0.1.0 RC0

<!-- kb:generated:start -->
**Thread:** [[VOTE][Terraform] Release Apache Iceberg Terraform Provider v0.1.0 RC0](https://lists.apache.org/thread/lfr1kb253m99dg0mbdzpm6g1k3nbd6fc) · **Started:** 2026-07-13 by [[person/zeroshade|Matthew Topol]] · **Messages:** 5 (last 2026-07-15) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zeroshade proposed release candidate RC0 of the Apache Iceberg Terraform provider v0.1.0, based on commit 2fe813329790eacf0b698bd430a57459fbf00e89, with the source release hosted on the ASF dist server and convenience binaries for the Terraform and OpenTofu registries attached to a GitHub prerelease. The vote was to stay open for at least 72 hours. Four non-binding +1 votes followed. Rich Bowen verified signatures, hashes, LICENSE and NOTICE. rambleraptor ran the verification script and noted failures during its cleanup step that do not affect its function, opening a PR for them as a nice-to-have. nssalian verified the checksum, signature, that the source tarball matches the signed tag tree, built and tested from source, and ran the provider with both the terraform and opentofu CLIs. The messages in this thread do not include a result announcement.

**Why it matters:** This is the release candidate for the first (v0.1.0) release of the Apache Iceberg Terraform provider.

## Outcome

Four non-binding +1 votes and no binding votes or objections in the collected messages; no result message is in the thread.

## Positions

- **[[person/rambleraptor|Alex Stephen]]:** Verification passed; the verify script has cleanup failures that do not affect its function, addressed in a follow-up PR as a nice-to-have. ([message](https://lists.apache.org/thread/k7047jl1z4kcf4fp19rsotg7ycjf0zwn))
- **[[person/nssalian|Neelesh Salian]]:** Verified checksums, signature, tag-to-tarball match, build and tests, and ran the provider with both terraform and opentofu. ([message](https://lists.apache.org/thread/xxfcz8f5bq2wcs0h0sns4ollm59p97o4))

References: [terraform-provider-iceberg#72](https://github.com/apache/terraform-provider-iceberg/issues/72)
<!-- kb:generated:end -->

## Notes
