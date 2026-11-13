---
id: module/iceberg-python/io
type: module
title: 'iceberg-python: io'
repo: apache/iceberg-python
path: io
commits_total: 292
commits_12m: 57
owners:
- Fokko
- sungwy
- kevinjqliu
- rambleraptor
- samredai
- HonahX
links:
- rel: part_of
  to: repo/iceberg-python
  confidence: observed
updated: '2026-11-13'
---

# iceberg-python: io

<!-- kb:generated:start -->
**Path:** `io/` in [apache/iceberg-python](https://github.com/apache/iceberg-python) · **Commits:** 292 in total, 57 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/Fokko|Fokko Driesprong]] (91), [[person/sungwy|Sung Yun]] (24), [[person/kevinjqliu|Kevin Liu]] (20), [[person/rambleraptor|Alex Stephen]] (6), [[person/samredai|Sam Redai]] (4), [[person/HonahX|Honah J.]] (4)

Most active authors (last 12 months): [[person/kevinjqliu|Kevin Liu]] (4), [[person/nssalian|Neelesh Salian]] (4), [[person/rahulsmahadev|Rahul Shivu Mahadev]] (4), [[person/rambleraptor|Alex Stephen]] (3), [[person/010Soham|Soham]] (3), [[person/krishnakaanchan-png|Kaanchan Krishna]] (3), [[person/ebyhr|Yuya Ebihara]] (2), [[person/fallintoplace|Minh Vu]] (2)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-13 Fix append to a table identity-partitioned on a uuid column (#4360) ([commit](https://github.com/apache/iceberg-python/commit/45774e7c10792270abc2b40ffc81167c069368b1))
- 2026-11-12 Rewrite NOT in row filters before the Arrow scan (#4350) ([commit](https://github.com/apache/iceberg-python/commit/2317c25c2683baf2fb522828f0457720b7a72770))
- 2026-11-12 Order -0.0 below 0.0 in data file metrics bounds (#4331) ([commit](https://github.com/apache/iceberg-python/commit/aeaddb18f0c0e2f8f25c85e960410afdd5eda0d4))
- 2026-11-11 fix(io): keep null lists of structs when projecting Arrow data (#4065) ([commit](https://github.com/apache/iceberg-python/commit/c4cd5130382d3240ff034c67ebcf74d3d9c986cc))
- 2026-11-11 Fix append when a data column is named like a partition helper column (#4344) ([commit](https://github.com/apache/iceberg-python/commit/640c4145c1267ad7b0ef50b8529b01ca2ac2a83d))
- 2026-11-11 Widen decimal literal precision in scan filters (#4348) ([commit](https://github.com/apache/iceberg-python/commit/260b8d17de174d63f1525fa24fadaf19bf711440))
- 2026-11-10 Drop column bounds when a row group with values has no min/max (#4313) ([commit](https://github.com/apache/iceberg-python/commit/aafad6e912c35e72ab74a6c08147c5d204a067f1))
- 2026-11-10 feat(encryption): [12/N] Read encrypted deletion vectors (#4326) ([commit](https://github.com/apache/iceberg-python/commit/9cbf09a1176af290cc10c7f27745edeb9c21d5f4))
<!-- kb:generated:end -->

## Notes
