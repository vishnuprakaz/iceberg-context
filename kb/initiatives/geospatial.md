---
id: initiative/geospatial
type: initiative
title: Geospatial types
status: implementing
updated: '2026-11-13'
sources:
- thread/t-d332ec73c7f3e8cc
- thread/t-eb9773fe398a7232
- meeting/community/2026-06-24
- meeting/read-restrictions/2026-07-07
- meeting/community/2026-07-15
- meeting/spark/2026-07-21
- meeting/community/2026-08-05
- meeting/spark/2026-08-18
- thread/t-f9e1b8daeae100d8
- meeting/community/2026-08-26
- thread/t-36974638264b04f5
- meeting/community/2026-10-28
- meeting/spark/2026-11-11
links:
- rel: handled_by
  to: group/spark
  confidence: extracted
  source: meeting/spark/2026-08-18
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-d332ec73c7f3e8cc
- rel: touches
  to: module/iceberg/parquet
  confidence: extracted
  source: meeting/community/2026-07-15
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/spark/2026-07-21
- rel: tracked_in
  to: gh:apache/iceberg#15834
  confidence: extracted
  source: thread/t-d332ec73c7f3e8cc
---

# Geospatial types

<!-- kb:generated:start -->
## What it is

The table spec has `geometry` and `geography` types for spatial data, each with a coordinate reference system (CRS) parameter ([thread 2026-05-11](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-d332ec.md), [dev list](https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7)). The types are V3 types ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The current work is implementing them across file formats, engines and the language implementations, plus small clarifications to the spec text ([Spark sync 2026-07-21](../records/meetings/spark/2026/2026-07-21.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4); [thread 2026-05-15](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-eb9773.md), [dev list](https://lists.apache.org/thread/y2n3yy1007t6rsyhtro7kww76047kozc)).

## Current state

- Decided and merged: the spec wording for the CRS parameter was clarified in [#15834](https://github.com/apache/iceberg/pull/15834), because the old text could be read as either suggesting or restricting the `srid:` and `projjson:` forms; the vote passed with 8 binding and 2 non-binding +1 votes and the pull request was merged ([thread 2026-05-15](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-eb9773.md), [dev list](https://lists.apache.org/thread/y2n3yy1007t6rsyhtro7kww76047kozc); [thread 2026-05-11](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-d332ec.md), [dev list](https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7)).
- Merged in Java: single-value binary serialization for geometry and geography ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), mapping to Parquet logical types ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), values in Avro ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and geometry bounds emitted by Parquet writers ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Merged in Spark: end-to-end geo type support for Spark 4.1 (type mapping, Parquet reads and writes, DML tests with fallback from vectorized reads) ([Spark sync 2026-07-21](../records/meetings/spark/2026/2026-07-21.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Behaviour change in 1.12.0: [#16765](https://github.com/apache/iceberg/pull/16765) changed `toString()` of the geometry and geography types to always print the resolved CRS and algorithm; reading stays compatible, and the release discussion preferred keeping the change and documenting it ([thread 2026-09-18](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc0-369746.md), [dev list](https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb)).
- Other implementations: PyIceberg 0.12.0 lists geometry and geography type support ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)); Iceberg Go added geometry and geography encoding ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and geo logical types ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); Iceberg C++ added V3 geometry and geography support ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Stalled: the end-to-end spatial file pruning draft carried a stale label and the vectorized geo reads pull request ([#17297](https://github.com/apache/iceberg/pull/17297)) was closed on 21 July; the Spark sync notes ask whether anyone is picking it back up ([Spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Read restrictions: geo types were removed from mask-to-default ([read restrictions sync 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md), [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).

## Timeline

- 2026-05-11: a vote was called on rewording the CRS parameter in the spec ([thread 2026-05-11](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-d332ec.md), [dev list](https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7)).
- 2026-05-18: the vote passed with 8 binding and 2 non-binding +1 votes, and [#15834](https://github.com/apache/iceberg/pull/15834) was merged ([thread 2026-05-15](../records/threads/2026/05/vote-proposal-to-update-working-in-spec-for-geospatial-type-crs-parame-eb9773.md), [dev list](https://lists.apache.org/thread/y2n3yy1007t6rsyhtro7kww76047kozc)).
- 2026-06-24: the community sync notes list single-value binary serialization for geometry and geography among the Java merges ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-07: the read restrictions sync announced that geo types were removed from mask-to-default ([read restrictions sync 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md), [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-07-15: the community sync notes list mapping geometry and geography to Parquet logical types among the Java merges ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-21: the Spark sync reported end-to-end geo type support in Spark 4.1 ([Spark sync 2026-07-21](../records/meetings/spark/2026/2026-07-21.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-08-05: the community sync notes list geometry and geography values in Avro among the Java merges ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-18: the Spark sync reported the spatial file pruning draft as stale and the vectorized geo reads pull request as closed ([Spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-08-26: the community sync notes list V3 geometry and geography support in Iceberg C++ ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-09-18: the 1.12.0 RC0 vote flagged the `toString()` change for geo types; the release manager and others preferred keeping it and documenting it as a behaviour change ([thread 2026-09-18](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc0-369746.md), [dev list](https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb)).
- 2026-11-11: the Spark sync reported that writers now emit geometry bounds in Parquet ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Where help is needed

- Vectorized geo reads in Spark: the pull request [#17297](https://github.com/apache/iceberg/pull/17297) was closed and the Spark sync notes ask whether anyone will pick it up ([Spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Spatial file pruning: the end-to-end draft was marked stale ([Spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
<!-- kb:generated:end -->

## Notes
