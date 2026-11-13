---
id: thread/t-702d44e21d229af8
type: thread
title: 'Release vote: Apache Iceberg Rust 0.10.0 RC4'
date: '2026-07-15'
url: https://lists.apache.org/thread/221q2qconm1zyxtor0fs86yt3st0xmo6
kind: release-vote
status: passed
messages: 9
sources:
- devlist:221q2qconm1zyxtor0fs86yt3st0xmo6
refs:
- gh:apache/iceberg-rust#2830
- gh:apache/iceberg-rust#2823
- gh:apache/iceberg-rust#2828
links: []
updated: '2026-11-13'
---

# Release vote: Apache Iceberg Rust 0.10.0 RC4

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.10.0 RC4](https://lists.apache.org/thread/221q2qconm1zyxtor0fs86yt3st0xmo6) · **Started:** 2026-07-15 by Danny Jones · **Messages:** 9 (last 2026-07-20) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones, with Shawn Chang, called a vote to release Apache Iceberg Rust 0.10.0 from tag v0.10.0-rc.4, open for at least 72 hours. Voters checked the download links, checksums and signatures, LICENSE and NOTICE files, ASF headers, the source build and tests, and the pyiceberg-core build. Xin Huang and L. C. Hsieh each reported 1839 tests passing. Neelesh Salian noted that the LICENSE and NOTICE files missing from three crates in RC3 are now present through PR #2830, a cherry-pick of #2823 and #2828, and that all ten publishable crates carry both files. liurenjie1024 cast a binding +1 after running the verify_rc.sh script. On July 20th Danny said the vote passes and that a separate result email would follow.

**Why it matters:** Iceberg Rust 0.10.0 is approved for release, with the per-crate licensing gap from RC3 fixed.

## Outcome

Danny Jones stated that the vote passes; the tally is left to a separate result email. The replies in this thread show one binding +1 and six non-binding +1 votes, with no -1. ([message](https://lists.apache.org/thread/57j0bgds22rhomp9ctkjw9w32mbn7r4o), `devlist:57j0bgds22rhomp9ctkjw9w32mbn7r4o`)

## Positions

- **[[person/nssalian|Neelesh Salian]]:** +1 non-binding; the per-crate LICENSE and NOTICE files that were missing in RC3 are present in RC4. ([message](https://lists.apache.org/thread/9k6mj1q09wcgpk99h8y9y11drtxxb3ph))
- **[[person/liurenjie1024|Renjie Liu]]:** +1 binding after verifying signature, checksum, and the builds and tests of iceberg-rust and pyiceberg-core. ([message](https://lists.apache.org/thread/58dpf2hnynhbx26q54rxx5pr70b1cwtx))

References: [iceberg-rust#2830](https://github.com/apache/iceberg-rust/issues/2830), [iceberg-rust#2823](https://github.com/apache/iceberg-rust/issues/2823), [iceberg-rust#2828](https://github.com/apache/iceberg-rust/issues/2828)
<!-- kb:generated:end -->

## Notes
