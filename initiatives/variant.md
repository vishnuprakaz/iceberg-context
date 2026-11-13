---
id: initiative/variant
type: initiative
title: Variant type and shredding
status: released
updated: '2026-11-13'
sources:
- thread/t-9b4ac94de3e00827
- meeting/spark/2026-05-19
- meeting/variant/2026-06-04
- thread/t-8a1d2c357afe958e
- meeting/variant/2026-07-02
- meeting/spark/2026-07-21
- thread/t-6c49480676915b91
- meeting/community/2026-08-05
- meeting/variant/2026-08-06
- meeting/spark/2026-08-18
- meeting/variant/2026-09-03
- meeting/spark/2026-11-11
links:
- rel: championed_by
  to: person/nssalian
  confidence: extracted
  source: thread/t-9b4ac94de3e00827
- rel: handled_by
  to: group/variant
  confidence: extracted
  source: thread/t-9b4ac94de3e00827
- rel: touches
  to: module/iceberg/parquet
  confidence: extracted
  source: meeting/variant/2026-08-06
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/spark/2026-05-19
- rel: touches
  to: module/iceberg/flink
  confidence: extracted
  source: meeting/variant/2026-06-04
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-6c49480676915b91
- rel: tracked_in
  to: gh:apache/iceberg#10392
  confidence: extracted
  source: thread/t-9b4ac94de3e00827
---

# Variant type and shredding

<!-- kb:generated:start -->
## What it is

Variant is a type for semi-structured data; "shredding" stores chosen fields of a variant as typed Parquet columns so they can be read and filtered without decoding the whole value ([variant sync 2026-06-04](../records/meetings/variant/2026/2026-06-04.md)). The work spans Iceberg, Spark, Parquet and Flink and is coordinated through a tracking document and a monthly Variant sync ([thread summary](../records/threads/2026/04/discuss-iceberg-variant-tracking-document-sync-proposal-9b4ac9.md), [dev list](https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l)). Current work is about read performance, a shared rule for which fields writers shred, and support in the non-Java implementations ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).

## Current state

- Released in Java: Iceberg 1.11 shipped with shredding ([variant sync 2026-06-04](../records/meetings/variant/2026/2026-06-04.md)); the 6 August sync lists shredding fixes and a vectorized reader for unshredded variant columns as shipped in 1.11 and 1.12 ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).
- REST catalog spec: a vote on adding the variant type ([#17256](https://github.com/apache/iceberg/pull/17256)) was held; the thread has only +1 votes and no result message ([thread summary](../records/threads/2026/07/vote-rest-spec-add-variant-type-to-the-rest-catalog-spec-6c4948.md), [dev list](https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9)), the 5 August community sync lists the REST spec change among merged work ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)) and the variant sync notes call it voted in ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).
- Shredding policy: the group rejected a user-declared shredding schema in favour of a canonical inference algorithm ([variant sync 2026-06-04](../records/meetings/variant/2026/2026-06-04.md)); the "uniform" rule (shred a field only if all sampled non-null values are of one type family) was selected and its pull request [#17424](https://github.com/apache/iceberg/pull/17424) was under review ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)). The proposal thread has no vote yet ([thread summary](../records/threads/2026/06/discuss-variant-shredding-policy-across-iceberg-implementations-8a1d2c.md), [dev list](https://lists.apache.org/thread/ztrygfd46607pns9t2d4hs0x95595cb2)).
- Read performance: vectorized Parquet reads for variant columns merged ([spark sync 2026-07-21](../records/meetings/spark/2026/2026-07-21.md)); vectorized reads of shredded data were in progress in September ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)). Variant filter pushdown depends on newer Spark versions ([variant sync 2026-07-02](../records/meetings/variant/2026/2026-07-02.md); [variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)).
- Other implementations: Rust added variant support ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)); Go was near completion with predicate pushdown as the last task ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)); PyIceberg is blocked on a stalled Arrow C++ pull request ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)).
- The December 2026 sync is cancelled; the sync resumes in January 2027 ([thread summary](../records/threads/2026/04/discuss-iceberg-variant-tracking-document-sync-proposal-9b4ac9.md), [dev list](https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l)).

## Timeline

- 2026-04-19: Neelesh Salian shares the Variant tracking document and proposes a monthly sync, which starts on 7 May ([thread summary](../records/threads/2026/04/discuss-iceberg-variant-tracking-document-sync-proposal-9b4ac9.md), [dev list](https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l)).
- 2026-05-19: Writing shredded variant in Spark 4.1 is reported as merged, with a Spark 4.0 backport ([spark sync 2026-05-19](../records/meetings/spark/2026/2026-05-19.md)).
- 2026-06-04: Benchmarks show shredded reads 4x to 5x slower than unshredded, attributed to disabled vectorization and missing sub-field projection; the group turns from a user-declared shredding schema to automated inference ([variant sync 2026-06-04](../records/meetings/variant/2026/2026-06-04.md)).
- 2026-06-04: Thread on a shared shredding policy across implementations opens ([thread summary](../records/threads/2026/06/discuss-variant-shredding-policy-across-iceberg-implementations-8a1d2c.md), [dev list](https://lists.apache.org/thread/ztrygfd46607pns9t2d4hs0x95595cb2)).
- 2026-07-21: Vectorized Parquet reads for variant columns merged ([spark sync 2026-07-21](../records/meetings/spark/2026/2026-07-21.md)).
- 2026-07-30: Vote on adding the variant type to the REST catalog spec opens ([thread summary](../records/threads/2026/07/vote-rest-spec-add-variant-type-to-the-rest-catalog-spec-6c4948.md), [dev list](https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9)).
- 2026-08-06: The "uniform" shredding algorithm is selected ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).
- 2026-09-03: Decision to fix string ordering to UTF-8 byte order without a backward compatibility fallback, prioritized for 1.12 ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)).
- 2026-11-11: A fix for unprojected shredded variants in vectorized reads is reported as merged, and writing variant to ORC now fails with a clear error ([spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md)).

## Where help is needed

- PyIceberg variant support is blocked by the chain Arrow C++ to PyArrow to PyIceberg; the Arrow C++ pull request was described as stalled ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)).
- Review of the updated shredding inference proposal was requested on the dev list ([thread summary](../records/threads/2026/06/discuss-variant-shredding-policy-across-iceberg-implementations-8a1d2c.md), [dev list](https://lists.apache.org/thread/ztrygfd46607pns9t2d4hs0x95595cb2)).
- In August the selective shredded variant extraction readers ([#16714](https://github.com/apache/iceberg/pull/16714)) had been quiet since 26 July with a split decision pending, and variant extraction pushdown had no reviews ([spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md)).
<!-- kb:generated:end -->

## Notes
