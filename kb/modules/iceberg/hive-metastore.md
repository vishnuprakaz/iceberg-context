---
id: module/iceberg/hive-metastore
type: module
title: 'iceberg: hive-metastore'
repo: apache/iceberg
path: hive-metastore
commits_total: 185
commits_12m: 20
owners:
- nastra
- pvary
- szehon-ho
- ebyhr
- aokolnychyi
- flyrain
links:
- rel: part_of
  to: repo/iceberg
  confidence: observed
updated: '2026-11-13'
---

# iceberg: hive-metastore

<!-- kb:generated:start -->
**Path:** `hive-metastore/` in [apache/iceberg](https://github.com/apache/iceberg) · **Commits:** 185 in total, 20 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/nastra|Eduard Tudenhoefner]] (13), [[person/pvary|Peter Vary]] (12), [[person/szehon-ho|Szehon Ho]] (6), [[person/ebyhr|Yuya Ebihara]] (6), [[person/aokolnychyi|Anton Okolnychyi]] (5), [[person/flyrain|Yufei Gu]] (5)

Most active authors (last 12 months): [[person/smaheshwar-pltr|Sreesh Maheshwar]] (3), [[person/ggershinsky|Gidon Gershinsky]] (2), [[person/szlta|Adam Szita]] (1), [[person/hiwuya|wuya]] (1), [[person/nastra|Eduard Tudenhoefner]] (1), [[person/manuzhang|Manu Zhang]] (1), [[person/ebyhr|Yuya Ebihara]] (1), [[person/nssalian|Neelesh Salian]] (1)

Most active reviewers (last 6 months): [[person/singhpk234|Prashant Singh]] (5), [[person/pvary|Peter Vary]] (4), [[person/huaxingao|Huaxin Gao]] (3), [[person/ggershinsky|Gidon Gershinsky]] (3), [[person/uros-b|Uros]] (3), [[person/wombatu-kun|Vova Kolmakov]] (2), [[person/gaborkaszab|Gabor Kaszab]] (1), [[person/danielcweeks|Daniel C. Weeks]] (1)

## Latest changes

- 2026-10-20 Hive: Write format-version to HMS table parameters (#18534) ([commit](https://github.com/apache/iceberg/commit/f723526ca7b3bc2eeacba3a47cbec5f018bd4679))
- 2026-09-16 Core, Hive: Commit manifest list encryption keys with the snapshot that uses them (#17984) ([commit](https://github.com/apache/iceberg/commit/e74344ca56029b9af5211d6a474fd1f553170757))
- 2026-09-09 Core, Hive: Fix NPE in commit status check when a create commit fails (#17464) ([commit](https://github.com/apache/iceberg/commit/0630297ef2d0304112ac4a11f610ad493cb6b888))
- 2026-09-04 Core, Hive, Spark: Auto close JsonGenerator using try-with-resources (#17931) ([commit](https://github.com/apache/iceberg/commit/20d616d6a1e5c2f3e7553a2f7312330039fe3a81))
- 2026-08-01 API, AWS, BigQuery, Core, Flink, Hive, Nessie, ORC, Parquet, Spark: Use Locale.ROOT instead of Locale.ENGLISH for case conversion (#17442) ([commit](https://github.com/apache/iceberg/commit/4a1513f1f220cc6adcd96093b64d6ab43e0808f1))
- 2026-07-24 Hive: Fix integer overflow in HMS createTime and lastAccessTime (#16620) ([commit](https://github.com/apache/iceberg/commit/787076dc0c4f5f986521e687aa294ca0fe094de5))
- 2026-07-24 Hive: Use server-side filter to list Iceberg tables in HiveCatalog (#17317) ([commit](https://github.com/apache/iceberg/commit/8f4843394cbfca3583108b8f6174f86f8580071b))
- 2026-06-19 Core, AWS, GCP, Dell, Hive: Fix FileIO leaks and standardize close() across Catalog implementations (#16862) ([commit](https://github.com/apache/iceberg/commit/0ddbeead67275dc785ec2a905f14eb8847d75f98))
<!-- kb:generated:end -->

## Notes
