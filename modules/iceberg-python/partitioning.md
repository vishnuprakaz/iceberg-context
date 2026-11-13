---
id: module/iceberg-python/partitioning
type: module
title: 'iceberg-python: partitioning'
repo: apache/iceberg-python
path: partitioning
commits_total: 39
commits_12m: 9
owners:
- Fokko
- sungwy
- kevinjqliu
- smaheshwar-pltr
- gabeiglio
- rdblue
links:
- rel: part_of
  to: repo/iceberg-python
  confidence: observed
updated: '2026-11-13'
---

# iceberg-python: partitioning

<!-- kb:generated:start -->
**Path:** `partitioning/` in [apache/iceberg-python](https://github.com/apache/iceberg-python) · **Commits:** 39 in total, 9 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/Fokko|Fokko Driesprong]] (10), [[person/sungwy|Sung Yun]] (3), [[person/kevinjqliu|Kevin Liu]] (3), [[person/smaheshwar-pltr|Sreesh Maheshwar]] (2), [[person/gabeiglio|Gabriel Igliozzi]] (2), [[person/rdblue|Ryan Blue]] (1)

Most active authors (last 12 months): [[person/gabeiglio|Gabriel Igliozzi]] (2), [[person/rambleraptor|Alex Stephen]] (1), [[person/kevinjqliu|Kevin Liu]] (1), [[person/anxkhn|Anas Khan]] (1), [[person/ebyhr|Yuya Ebihara]] (1), [[person/mittalpk|Praveen Kumar Mittal]] (1), [[person/sohailshk|Mohammad Sohail Shaikh]] (1), [[person/rahulsmahadev|Rahul Shivu Mahadev]] (1)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-12 Fix append to a table partitioned by bucket on a time column (#4343) ([commit](https://github.com/apache/iceberg-python/commit/2a1439e82b5be7d400bef87625124bd5986fd85a))
- 2026-11-12 Reject duplicate partition field names (#4305) ([commit](https://github.com/apache/iceberg-python/commit/533dea9e8251870abaca9d3bf2af4f28b8aea73d))
- 2026-08-31 fix: Nanosecond partition representation (#3695) ([commit](https://github.com/apache/iceberg-python/commit/d0b58943de09bc8af7209a569eab6ec620d736ca))
- 2026-08-31 Reject conflicted `source-id` and `source-ids` (#3645) ([commit](https://github.com/apache/iceberg-python/commit/e1ddfd3b8d96cc0d49d195f31de2c07a0a2e8c1f))
- 2026-08-15 fix: raise `TypeError` for unsupported partition source type (#3617) ([commit](https://github.com/apache/iceberg-python/commit/d63d4865ba14804874aafd0d9bd642dfc7c6af70))
- 2026-05-25 Reject empty `source-ids` in `PartitionField` / `SortField` (#3411) ([commit](https://github.com/apache/iceberg-python/commit/b7ca7be605043b26e2078da357ad4f94e22e771a))
- 2026-01-27 Block schema field drop if it is reference by an active partition or sort field (#2410) ([commit](https://github.com/apache/iceberg-python/commit/fe6b6fcb312de646177ae591e5a401b78b0a59c3))
- 2025-12-04 Read partitioned tables with source field missing (#2367) ([commit](https://github.com/apache/iceberg-python/commit/8ed913bc48b19460c47746273b4678e7d2e6af70))
<!-- kb:generated:end -->

## Notes
