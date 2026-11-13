---
id: module/iceberg/api
type: module
title: 'iceberg: api'
repo: apache/iceberg
path: api
commits_total: 894
commits_12m: 124
owners:
- rdblue
- nastra
- aokolnychyi
- amogh-jahagirdar
- Fokko
- RussellSpitzer
links:
- rel: part_of
  to: repo/iceberg
  confidence: observed
updated: '2026-11-13'
---

# iceberg: api

<!-- kb:generated:start -->
Public interfaces and types. Strongest stability guarantees; breaking changes are almost never accepted.
**Path:** `api/` in [apache/iceberg](https://github.com/apache/iceberg) · **Commits:** 894 in total, 124 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/rdblue|Ryan Blue]] (195), [[person/nastra|Eduard Tudenhoefner]] (85), [[person/aokolnychyi|Anton Okolnychyi]] (68), [[person/amogh-jahagirdar|Amogh Jahagirdar]] (35), [[person/Fokko|Fokko Driesprong]] (29), [[person/RussellSpitzer|Russell Spitzer]] (29)

Most active authors (last 12 months): [[person/nastra|Eduard Tudenhoefner]] (13), [[person/anoopj|Anoop Johnson]] (13), [[person/uros-b|Uros]] (10), [[person/rdblue|Ryan Blue]] (7), [[person/ebyhr|Yuya Ebihara]] (5), [[person/stevenzwu|Steven Wu]] (5), [[person/singhpk234|Prashant Singh]] (4), [[person/gaborkaszab|Gabor Kaszab]] (4)

Most active reviewers (last 6 months): [[person/nastra|Eduard Tudenhoefner]] (12), [[person/uros-b|Uros]] (12), [[person/szehon-ho|Szehon Ho]] (12), [[person/huaxingao|Huaxin Gao]] (12), [[person/wombatu-kun|Vova Kolmakov]] (11), [[person/anoopj|Anoop Johnson]] (10), [[person/ebyhr|Yuya Ebihara]] (10), [[person/amogh-jahagirdar|Amogh Jahagirdar]] (10)

## Latest changes

- 2026-11-13 API, Core: Add Snapshot.rootManifestLocation() (#17523) ([commit](https://github.com/apache/iceberg/commit/58cf9d8bba9fe077cbf55d40eae17fd552eaf790))
- 2026-11-11 API: Fix ClassCastException when sanitizing bound IN/NOT_IN predicates (#18413) ([commit](https://github.com/apache/iceberg/commit/85d5fb99a3a0b39ebf0c5de545feb704953f1f09))
- 2026-11-10 Core: Add util to derive source column bounds from monotonic partition transforms (#18604) ([commit](https://github.com/apache/iceberg/commit/c75374cb0e49c17eac133358776910112c153ff6))
- 2026-11-10 API, Core: Implement v4 file-level tight_stats (#18598) ([commit](https://github.com/apache/iceberg/commit/c136f05607c8a1e477ea307d34f42d5c024e53ef))
- 2026-11-09 API, Core: improve toString in struct implementations (#18353) ([commit](https://github.com/apache/iceberg/commit/0e05c5659fac18bc711dad2d8d891a833016a304))
- 2026-11-03 Spark: [3/N] Support sending referenced-by to all endpoints (#13979) ([commit](https://github.com/apache/iceberg/commit/b71a64ddc28e4b39e07cec71cd12bc5ed293f8bb))
- 2026-10-29 API: Fix failed scans and wrong results for IN/NOT IN on timestamp_ns partitions (#18478) ([commit](https://github.com/apache/iceberg/commit/6955fcd1f350856d96a572e3f53f01bdab748e7f))
- 2026-10-27 Core: Read geometry and geography bounds as GeospatialBound (#18394) ([commit](https://github.com/apache/iceberg/commit/ea47af380c0bf41a64fac858d0d89d1227db0418))
<!-- kb:generated:end -->

## Notes
