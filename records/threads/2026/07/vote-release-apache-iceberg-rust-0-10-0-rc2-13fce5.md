---
id: thread/t-13fce5373af3fa44
type: thread
title: Release Apache Iceberg Rust 0.10.0 RC2
date: '2026-07-01'
url: https://lists.apache.org/thread/m35vm2j7z9pdv2o3jtyvd5vls0bko0xj
kind: release-vote
status: withdrawn
messages: 12
sources:
- devlist:m35vm2j7z9pdv2o3jtyvd5vls0bko0xj
refs:
- gh:apache/iceberg-rust#2760
- gh:apache/iceberg-rust#2527
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:m35vm2j7z9pdv2o3jtyvd5vls0bko0xj
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg Rust 0.10.0 RC2

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.10.0 RC2](https://lists.apache.org/thread/m35vm2j7z9pdv2o3jtyvd5vls0bko0xj) · **Started:** 2026-07-01 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 12 (last 2026-07-03) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones called a vote on Apache Iceberg Rust 0.10.0 RC2 (tag v0.10.0-rc.2). Several voters verified checksums, signatures, license headers, builds and tests on macOS and Linux and voted +1, including one binding +1 from liurenjie1024; mbutrovich also ran DataFusion Comet CI against the tag. manuzhang voted -1 (non-binding) because the ASF source tarball did not match the signed Git tag: a CI workflow file and CHANGELOG.md differed. CTTY considered the differences too minor for a new RC but asked for other opinions. manuzhang and liurenjie1024 asked to fix the release process and cut another RC, using the create_rc.sh script and a dedicated 0.10.0-rc branch. CTTY created the branch, said he would work with Danny on RC3, and opened a draft PR to make verify_rc.sh catch tag and tarball mismatches.

**Why it matters:** Established that iceberg-rust release candidates must have a source tarball identical to the signed tag and be cut from a release branch.

## Outcome

RC2 was abandoned in favor of an RC3 cut from a new 0.10.0-rc branch after a tarball and tag mismatch was found. Before that RC2 had one binding +1, five non-binding +1 and one non-binding -1; no result was announced. ([message](https://lists.apache.org/thread/fj1x03kobztzsz2fzo8ktvs03b4lz685), `devlist:fj1x03kobztzsz2fzo8ktvs03b4lz685`)

## Positions

- **[[person/manuzhang|Manu Zhang]]:** Voted -1 (non-binding) because the source tarball differs from the signed tag in a CI workflow file and CHANGELOG.md. ([message](https://lists.apache.org/thread/nzq1vt0hxznzkzhyfcqmlqrybq4kf2xr))
- **[[person/CTTY|Shawn Chang]]:** The mismatches do not affect released source, license or build output, so they may not justify another RC, but he is open to other opinions. ([message](https://lists.apache.org/thread/k669yqqdd7bndt8340yvk3tf00zj115b))
- **[[person/manuzhang|Manu Zhang]]:** Fix the release process and cut another RC so tag and tarball never mismatch again, since next time it could be a source file. ([message](https://lists.apache.org/thread/1903jy6xqykc492kfm1y006kkn5qd8d0))
- **[[person/liurenjie1024|Renjie Liu]]:** Agrees a new RC is needed; use dev/release/create_rc.sh and cut the RC from a 0.10.0-rc branch. ([message](https://lists.apache.org/thread/3wxc8k22rcbg8g8x9njg9glvvgxmcf6t))

References: [iceberg-rust#2760](https://github.com/apache/iceberg-rust/issues/2760), [iceberg-rust#2527](https://github.com/apache/iceberg-rust/issues/2527)
<!-- kb:generated:end -->

## Notes
