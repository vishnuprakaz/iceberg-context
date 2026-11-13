---
id: thread/t-6293c79628424192
type: thread
title: Vote to release Apache Iceberg Rust 0.11.0 RC1
date: '2026-09-09'
url: https://lists.apache.org/thread/nj95255r4ofqszpfx6pd8hbf8yxxydzv
kind: release-vote
status: withdrawn
messages: 5
sources:
- devlist:nj95255r4ofqszpfx6pd8hbf8yxxydzv
refs:
- gh:apache/iceberg-rust#3184
- gh:apache/iceberg-rust#3174
- gh:apache/iceberg-rust#1325
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:nj95255r4ofqszpfx6pd8hbf8yxxydzv
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Vote to release Apache Iceberg Rust 0.11.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.11.0 RC1](https://lists.apache.org/thread/nj95255r4ofqszpfx6pd8hbf8yxxydzv) · **Started:** 2026-09-09 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 5 (last 2026-09-10) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones called a vote on Apache Iceberg Rust 0.11.0 RC1 (tag v0.11.0-rc.1). Two non-binding +1 votes came in after verification on macOS and Linux; one verifier saw a flaky REST catalog rename test caused by a locked SQLite test fixture and did not consider it a blocker. Kevin Liu voted -1 because the candidate cannot be published: the iceberg crate depends on the new iceberg-property-macro crate, which has iceberg as a versioned dev-dependency, so cargo publish fails for both. He recalled that the same circular dependency after the 0.5.0 vote forced a 0.5.1 release, and opened a fix that also adds a cargo publish dry-run check to CI. He also noted that make test from the tarball fails at docker-up because the Hive image's apt repository has expired, which a change on main fixes. Danny Jones agreed it is a blocker, voted -1 and said he would prepare RC2.

**Why it matters:** A cargo publish dry-run check in CI is being added so that unpublishable crate dependencies are caught on pull requests.

## Outcome

RC1 was abandoned in favor of an RC2: after two non-binding +1 votes, kevinjqliu voted -1 over a crate circular dependency that blocks publishing, and the release manager agreed with a non-binding -1. No formal result message was sent. ([message](https://lists.apache.org/thread/9dvp6bpz998615m9zlkg6yqf8m6jbct9), `devlist:9dvp6bpz998615m9zlkg6yqf8m6jbct9`)

## Positions

- **[[person/kevinjqliu|Kevin Liu]]:** The candidate cannot be published because of a circular dependency between iceberg and iceberg-property-macro, so it should be fixed and a new RC cut. ([message](https://lists.apache.org/thread/433wxmpfddwx7y49vsc28zvy8fsb9xwt))
- **[[person/anoopj|Anoop Johnson]]:** The candidate verified on Linux; a flaky REST catalog rename test caused by a locked SQLite test fixture is not a blocker. ([message](https://lists.apache.org/thread/2nbm37qpvkykljqzdtbtfqtk75sqfdzl))
- **Danny Jones:** The publishing problem is a blocker for the release and RC2 will follow. ([message](https://lists.apache.org/thread/9dvp6bpz998615m9zlkg6yqf8m6jbct9))

References: [iceberg-rust#3184](https://github.com/apache/iceberg-rust/issues/3184), [iceberg-rust#3174](https://github.com/apache/iceberg-rust/issues/3174), [iceberg-rust#1325](https://github.com/apache/iceberg-rust/issues/1325)
<!-- kb:generated:end -->

## Notes
