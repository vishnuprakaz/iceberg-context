---
id: initiative/conformance-testing
type: initiative
title: Shared conformance testing (iceberg-verification)
status: implementing
updated: '2026-11-13'
sources:
- thread/t-59cdd1fc4c8fabde
- thread/t-0eb2bea9a6273744
- thread/t-14cfe62770f38386
- meeting/community/2026-09-16
- thread/t-3aecd28f8883bc90
- meeting/community/2026-07-15
- meeting/community/2026-08-05
- meeting/variant/2026-08-06
links:
- rel: championed_by
  to: person/nssalian
  source: thread/t-0eb2bea9a6273744
  confidence: extracted
- rel: championed_by
  to: person/sungwy
  source: thread/t-59cdd1fc4c8fabde
  confidence: extracted
- rel: championed_by
  to: person/laskoviymishka
  source: thread/t-59cdd1fc4c8fabde
  confidence: extracted
- rel: handled_by
  to: group/conformance
  source: thread/t-59cdd1fc4c8fabde
  confidence: extracted
---

# Shared conformance testing (iceberg-verification)

<!-- kb:generated:start -->
## What it is

A shared, language-neutral set of conformance fixtures, modelled on parquet-testing, so that every Iceberg implementation (Java, Python, Rust, Go, C++) tests its reading of the spec against the same inputs and expected values instead of only against itself ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)). There is no central harness or gate: each implementation pins the fixture repository and asserts in its own test suite ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)). The fixtures live in a new repository, apache/iceberg-verification ([thread summary](../records/threads/2026/08/vote-create-the-apache-iceberg-verification-repository-0eb2be.md), [dev list](https://lists.apache.org/thread/5jm8jpp327w9yn4zznlrlv5165mz4vt3)).

## Current state

- The vote to create the standalone repository apache/iceberg-verification passed, according to the closing message of the vote thread; that message gives no counts and all votes in the thread were +1 ([thread summary](../records/threads/2026/08/vote-create-the-apache-iceberg-verification-repository-0eb2be.md), [dev list](https://lists.apache.org/thread/5jm8jpp327w9yn4zznlrlv5165mz4vt3)).
- Scope of the proposal: start with static inputs paired with the value the spec fixes (type strings, transforms), grow to binary fixtures, cover v2 and v3, with Java and Go first ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)).
- Proofs of concept exist for PyIceberg, iceberg-rust and iceberg-go ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)).
- Write verification was an open item: Andrei Tserakhau argued that many divergences are write bugs and described an engine-free prototype that runs a logical operation log through each implementation and compares a canonical form ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)). No record shows how this was settled.
- The repository is in use (inferred from an issue reference): the November thread on name mapping for partially ID'd files, where Java, PyIceberg, iceberg-rust and iceberg-go each resolve such files differently, references [apache/iceberg-verification#14](https://github.com/apache/iceberg-verification/issues/14) ([thread summary](../records/threads/2026/11/discuss-name-mapping-for-data-files-that-carry-only-some-field-ids-14cfe6.md), [dev list](https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo)).
- An update on iceberg-verification was listed at the 2026-09-16 community sync; the notes record no details ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).

## Timeline

- 2026-06-29: Replies to Neelesh Salian's conformance testing write-up; Sung Yun reports a parallel proposal and the authors agree to merge the two ([thread summary](../records/threads/2026/06/discuss-cross-implementation-conformance-testing-for-iceberg-3aecd2.md), [dev list](https://lists.apache.org/thread/h21x5r8bfrv3zg700y9py84plrfmtmsr)).
- 2026-07-14: Joint proposal by Neelesh Salian, Sung Yun and Andrei Tserakhau posted; a dedicated sync is scheduled for 2026-08-19 ([thread summary](../records/threads/2026/07/discuss-shared-conformance-fixtures-for-apache-iceberg-implementations-59cdd1.md), [dev list](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj)).
- 2026-07-15: Neelesh presents the shared testing repository proposal at the community sync ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)); it is listed again on 2026-08-05 ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)).
- 2026-08-06: The variant sync notes that a shared test suite for variant shredding is being developed, with the Go implementation as reference for Rust and C++ ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).
- 2026-08-19: Vote called to create apache/iceberg-verification; the thread is later closed as passed ([thread summary](../records/threads/2026/08/vote-create-the-apache-iceberg-verification-repository-0eb2be.md), [dev list](https://lists.apache.org/thread/5jm8jpp327w9yn4zznlrlv5165mz4vt3)).
- 2026-09-16: iceberg-verification update listed at the community sync ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).
- 2026-11-03: Thread on name mapping for data files that carry only some field IDs reports diverging behaviour across four implementations and references an iceberg-verification issue; no agreement yet ([thread summary](../records/threads/2026/11/discuss-name-mapping-for-data-files-that-carry-only-some-field-ids-14cfe6.md), [dev list](https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo)).

## Where help is needed

- The name-mapping question is open: whether a file with only some field IDs is resolved per field or per file. The outcome decides what the implementations, and a fixture for this case, must assert ([thread summary](../records/threads/2026/11/discuss-name-mapping-for-data-files-that-carry-only-some-field-ids-14cfe6.md), [dev list](https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo)).
<!-- kb:generated:end -->

## Notes
