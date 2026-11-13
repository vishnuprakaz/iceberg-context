---
id: thread/t-e5e8356da0183206
type: thread
title: Release Apache Iceberg Terraform provider v0.1.0 RC1
date: '2026-07-16'
url: https://lists.apache.org/thread/krophr3htb39xhxr3ldbcn7ghqm82ohj
kind: release-vote
status: withdrawn
messages: 6
sources:
- devlist:krophr3htb39xhxr3ldbcn7ghqm82ohj
refs: []
links:
- rel: discussed
  to: initiative/iceberg-go
  confidence: extracted
  source: devlist:krophr3htb39xhxr3ldbcn7ghqm82ohj
- rel: started_by
  to: person/zeroshade
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg Terraform provider v0.1.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE][Terraform] Release Apache Iceberg Terraform provider v0.1.0 RC1](https://lists.apache.org/thread/krophr3htb39xhxr3ldbcn7ghqm82ohj) · **Started:** 2026-07-16 by [[person/zeroshade|Matthew Topol]] · **Messages:** 6 (last 2026-07-27) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

zeroshade proposed release candidate 1 of the Apache Iceberg Terraform provider v0.1.0, based on commit ce85caf0, with convenience binaries for the Terraform and OpenTofu registries attached to a GitHub prerelease. sungwy, rambleraptor and Rich Bowen voted +1 after verifying signatures, checksums and license files; two of them also built from source and ran the tests. kevinjqliu then reported a schema-validation problem he considered a release blocker: on table creation, omitted field IDs are serialized as 0, so the published example sends duplicate field IDs and the catalog rejects it; on table update, the provider does not check Iceberg schema evolution rules and committed a long-to-string change and an optional-to-required change. He also noted leftover 'polaris' references and a 1.0.0 version in build.sh. zeroshade said he would fix the issues and cut a new RC.

**Why it matters:** The first Terraform provider release is held back until table schemas are created with valid field IDs and incompatible schema changes are rejected.

## Outcome

The release manager said he would fix the reported schema issues and cut a new RC. Votes cast before that: one +1 binding and two +1 non-binding. ([message](https://lists.apache.org/thread/fcq2x1dw79pj06hcl0z7qf87kqrt8vcz), `devlist:fcq2x1dw79pj06hcl0z7qf87kqrt8vcz`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** The release should wait until the provider submits schemas with unique field IDs on create and rejects table updates that are not valid Iceberg schema evolutions. ([message](https://lists.apache.org/thread/32f91dv0yom2pc309l4y76w4hq0pycqb))
- **[[person/zeroshade|Matthew Topol]]:** Will look into fixing the reported issues and cut a new release candidate when done. ([message](https://lists.apache.org/thread/fcq2x1dw79pj06hcl0z7qf87kqrt8vcz))
<!-- kb:generated:end -->

## Notes
