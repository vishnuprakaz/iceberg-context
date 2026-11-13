---
id: module/iceberg/spark
type: module
title: 'iceberg: spark'
repo: apache/iceberg
path: spark
commits_total: 2035
commits_12m: 344
owners:
- aokolnychyi
- rdblue
- nastra
- manuzhang
- szehon-ho
- ajantha-bhat
links:
- rel: part_of
  to: repo/iceberg
  confidence: observed
updated: '2026-11-13'
---

# iceberg: spark

<!-- kb:generated:start -->
Spark integration, one copy of the source tree per supported Spark version.
**Path:** `spark/` in [apache/iceberg](https://github.com/apache/iceberg) · **Commits:** 2035 in total, 344 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/aokolnychyi|Anton Okolnychyi]] (279), [[person/rdblue|Ryan Blue]] (174), [[person/nastra|Eduard Tudenhoefner]] (117), [[person/manuzhang|Manu Zhang]] (75), [[person/szehon-ho|Szehon Ho]] (59), [[person/ajantha-bhat|Ajantha Bhat]] (59)

Most active authors (last 12 months): [[person/manuzhang|Manu Zhang]] (22), [[person/nastra|Eduard Tudenhoefner]] (19), [[person/aokolnychyi|Anton Okolnychyi]] (19), [[person/pvary|Peter Vary]] (12), [[person/drexler-sky|drexler-sky]] (11), [[person/anuragmantri|Anurag Mantripragada]] (11), [[person/RussellSpitzer|Russell Spitzer]] (10), [[person/kevinjqliu|Kevin Liu]] (10)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-10 Spark 4.2: Best-effort ExpireSnapshots when metadata reachable only from expired snapshots is missing (#18477) ([commit](https://github.com/apache/iceberg/commit/26c9544ea4744df3d09bb3a9abcefd43997fa595))
- 2026-11-06 ORC: Fix NPE when reading/writing variant type with ORC format (#18387) ([commit](https://github.com/apache/iceberg/commit/4e2a9bda3705c55bf37473c7d728d4ffecb698f6))
- 2026-11-05 Spark 4.1: Backport: Fix predicate pushdown on changelog metadata column (#18148) (#18808) ([commit](https://github.com/apache/iceberg/commit/d2df5101dc39f74e328319845c771fed0afbfe3e))
- 2026-11-04 Spark 3.5: Backport apply session snapshot properties to maintenance actions and procedures (#18801) ([commit](https://github.com/apache/iceberg/commit/f72900ee02cbb9bde4b1523d696a7258690a943c))
- 2026-11-04 Spark 3.5: Backport custom snapshot property from session configuration (#14545) (#18792) ([commit](https://github.com/apache/iceberg/commit/cb5f345a267331a5aef4bb65c3616463c01bbadd))
- 2026-11-04 Spark 3.5, 4.0, 4.1: Backport format model TCK coverage for vectorized reads (#18790) ([commit](https://github.com/apache/iceberg/commit/ea73769d120dc3819d8cfa2253b6dba4bb394886))
- 2026-11-04 Data, Spark 4.2: Add format model TCK coverage for vectorized reads (#17610) ([commit](https://github.com/apache/iceberg/commit/22ed06b9792c7161523e5ffa5dde4b199e0c6629))
- 2026-11-04 Core, Spark: Rethrow ValidationException from REST 400 responses (#18473) ([commit](https://github.com/apache/iceberg/commit/c484d46fde82028ed351e9a8f0b665261d7c1581))
<!-- kb:generated:end -->

## Notes
