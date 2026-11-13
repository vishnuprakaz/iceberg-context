---
id: thread/t-2155678929401961
type: thread
title: pyiceberg-core Python bindings missing third-party license and notice files
date: '2026-09-16'
url: https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4
kind: discuss
status: consensus
messages: 5
sources:
- devlist:k72c2y72w2j00xph2mn2bnsbvcbj43o4
refs:
- gh:apache/iceberg-rust#3239
links:
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# pyiceberg-core Python bindings missing third-party license and notice files

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] pyiceberg-core / iceberg-rust Python bindings appears not to include third-party notice files](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4) · **Started:** 2026-09-16 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 5 (last 2026-10-29) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones reported that pyiceberg-core wheels distribute compiled Rust dependencies without reproducing the dependencies' copyright notices, and said this must be fixed before new pyiceberg-core and iceberg-rust releases, which ship together. He opened an issue proposing a THIRD-PARTY-LICENSES file generated at build time. rdblue confirmed that LICENSE and NOTICE for compiled artifacts must reflect everything distributed and that a NOTICE with the required notices is needed. CTTY pointed to the paimon-rust workflow for generating and verifying per-wheel license reports. kevinjqliu explained that the iceberg-rust source release bundles no dependencies, so only the wheels are affected, and that a repo-wide cargo deny check already blocks incompatible licenses. On October 29 Danny Jones reported the issue fixed: the wheels now ship NOTICE and LICENSE files with all dependencies' notices and licenses appended, the Rust crates keep their original files, and 0.11.0 RC3 is proceeding.

**Why it matters:** Binary artifacts such as pyiceberg-core wheels must carry the licenses and notices of every bundled dependency, which held up the Iceberg Rust 0.11.0 release.

## Outcome

Resolved: pyiceberg-core wheels now ship NOTICE and LICENSE files with all dependencies' notices and licenses appended, while source-only Rust crates keep their original files; Iceberg Rust 0.11.0 RC3 is moving forward. ([message](https://lists.apache.org/thread/bvnhbx81620ho11vo1nyps3pnp9x0bth), `devlist:bvnhbx81620ho11vo1nyps3pnp9x0bth`)

## Positions

- **Danny Jones:** pyiceberg-core wheels ship compiled dependencies without their copyright notices; this must be fixed before the next release, for example with a THIRD-PARTY-LICENSES file added at build time. ([message](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4))
- **[[person/rdblue|Ryan Blue]]:** LICENSE and NOTICE of compiled artifacts must cover all distributed third-party code; a separate third-party file is acceptable if referenced from LICENSE, but a NOTICE with required notices is mandatory. ([message](https://lists.apache.org/thread/f1ggto5xyf3fq926nyy34hz8gr8lq0b4))
- **[[person/CTTY|Shawn Chang]]:** Follow the approach used by paimon-rust: derive dependencies from the Python bindings' Cargo.toml, generate a report per wheel, stage it in the artifacts and verify it. ([message](https://lists.apache.org/thread/5w64wjbsbh40prdyrjc5nfyno5s3vcv0))
- **[[person/kevinjqliu|Kevin Liu]]:** Only the wheels are affected because the source release bundles no dependencies; identify what is bundled and add entries to LICENSE and NOTICE before publishing pyiceberg-core again. ([message](https://lists.apache.org/thread/zmb9nzfvdjwqor4s5qmkf1dv599cxv0x))

References: [iceberg-rust#3239](https://github.com/apache/iceberg-rust/issues/3239)
<!-- kb:generated:end -->

## Notes
