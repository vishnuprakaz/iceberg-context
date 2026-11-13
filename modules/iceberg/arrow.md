---
id: module/iceberg/arrow
type: module
title: 'iceberg: arrow'
repo: apache/iceberg
path: arrow
commits_total: 110
commits_12m: 19
owners:
- nastra
- rdblue
- findepi
- wypoon
- RussellSpitzer
- ebyhr
links:
- rel: part_of
  to: repo/iceberg
  confidence: observed
updated: '2026-11-13'
---

# iceberg: arrow

<!-- kb:generated:start -->
**Path:** `arrow/` in [apache/iceberg](https://github.com/apache/iceberg) · **Commits:** 110 in total, 19 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/nastra|Eduard Tudenhoefner]] (19), [[person/rdblue|Ryan Blue]] (9), [[person/findepi|Piotr Findeisen]] (5), [[person/wypoon|Wing Yew Poon]] (5), [[person/RussellSpitzer|Russell Spitzer]] (4), [[person/ebyhr|Yuya Ebihara]] (4)

Most active authors (last 12 months): [[person/jbewing|jbewing]] (2), [[person/thswlsqls|Eunbin Son]] (2), [[person/nssalian|Neelesh Salian]] (2), [[person/shubham19may|Shubham Baldava]] (1), [[person/pvary|Peter Vary]] (1), [[person/drexler-sky|drexler-sky]] (1), [[person/xndai|Xiening Dai]] (1), [[person/sungwy|Sung Yun]] (1)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-06 Arrow: Fix valuesRead accumulation in VectorizedDeltaEncodedValuesReader (#17121) ([commit](https://github.com/apache/iceberg/commit/9203eaff9eb97fef9d1f5a3ef4460e8453adaed9))
- 2026-11-02 Arrow, Spark: Skip unprojected shredded variants in vectorized Parquet reads (#18434) ([commit](https://github.com/apache/iceberg/commit/c2c460586c7ff79e9b8dc530e5b73d3b4425f34c))
- 2026-10-22 Arrow: Fix vectorized reads of dictionary-encoded TIMESTAMP_MILLIS columns (#18592) ([commit](https://github.com/apache/iceberg/commit/60897e0b828580cc20e591424179d9b5c574e8d6))
- 2026-09-28 Arrow: Cover null decimal values with defaults across batches (#18271) ([commit](https://github.com/apache/iceberg/commit/587f7984ff811b1240b0ccf8e34e73e1a52f94d0))
- 2026-08-20 Arrow: Fix vectorized read of all-null DELTA-encoded Parquet pages (#17017) ([commit](https://github.com/apache/iceberg/commit/660f2328a7ba045c2b5f0a945f07d4fa8bab0a2a))
- 2026-08-17 Arrow: Fix direct memory leak in row lineage vectorized readers (#17296) ([commit](https://github.com/apache/iceberg/commit/c3ec74bca787cc7c1e7f2f1d72ca40de1f8b094e))
- 2026-07-19 Spark: Add vectorized Parquet reads for variant columns (#16292) ([commit](https://github.com/apache/iceberg/commit/9821b252ee766072bece865c22acf372f2938c05))
- 2026-07-13 Arrow: Fix dict-encoded VARCHAR/VARBINARY read for direct ByteBuffers (#17055) ([commit](https://github.com/apache/iceberg/commit/486fd93b402b9f8052d854d951cd4af1e3026a37))
<!-- kb:generated:end -->

## Notes
