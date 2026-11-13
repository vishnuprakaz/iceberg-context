---
id: module/iceberg/core
type: module
title: 'iceberg: core'
repo: apache/iceberg
path: core
commits_total: 2462
commits_12m: 426
owners:
- rdblue
- nastra
- aokolnychyi
- amogh-jahagirdar
- gaborkaszab
- RussellSpitzer
links:
- rel: part_of
  to: repo/iceberg
  confidence: observed
updated: '2026-11-13'
---

# iceberg: core

<!-- kb:generated:start -->
Engine-agnostic implementation of the table spec: metadata, snapshots, manifests, commits, REST client.
**Path:** `core/` in [apache/iceberg](https://github.com/apache/iceberg) · **Commits:** 2462 in total, 426 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/rdblue|Ryan Blue]] (409), [[person/nastra|Eduard Tudenhoefner]] (257), [[person/aokolnychyi|Anton Okolnychyi]] (190), [[person/amogh-jahagirdar|Amogh Jahagirdar]] (68), [[person/gaborkaszab|Gabor Kaszab]] (60), [[person/RussellSpitzer|Russell Spitzer]] (51)

Most active authors (last 12 months): [[person/nastra|Eduard Tudenhoefner]] (37), [[person/anoopj|Anoop Johnson]] (36), [[person/gaborkaszab|Gabor Kaszab]] (35), [[person/singhpk234|Prashant Singh]] (17), [[person/ebyhr|Yuya Ebihara]] (17), [[person/rdblue|Ryan Blue]] (16), [[person/stevenzwu|Steven Wu]] (12), [[person/uros-b|Uros]] (10)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-13 Core: Remove unnecessary comments from IncrementalFileCleanup (#18490) ([commit](https://github.com/apache/iceberg/commit/3c2407555f798ed11134e680e064cc87c4e4d2e3))
- 2026-11-13 API, Core: Add Snapshot.rootManifestLocation() (#17523) ([commit](https://github.com/apache/iceberg/commit/58cf9d8bba9fe077cbf55d40eae17fd552eaf790))
- 2026-11-12 Core: Add v4 TrackedFile write wrappers for leaf and root manifests (#18853) ([commit](https://github.com/apache/iceberg/commit/14690428f7a8c0e8f5f1fa04895b1380f371d717))
- 2026-11-12 Core: Use Caffeine's default executor in AuthSessionCache (#18378) ([commit](https://github.com/apache/iceberg/commit/acea99d28a4be93a8c0dfc7bd8ece4a237324243))
- 2026-11-12 Core: Count total data manifests in v4 scan planning (#18905) ([commit](https://github.com/apache/iceberg/commit/e31ea5f39b3e7d4a536cad3a4dbdc16dcf1e1553))
- 2026-11-10 Core: Add util to derive source column bounds from monotonic partition transforms (#18604) ([commit](https://github.com/apache/iceberg/commit/c75374cb0e49c17eac133358776910112c153ff6))
- 2026-11-10 Core: Add a longitude bounds collector for geography (#18811) ([commit](https://github.com/apache/iceberg/commit/83dffbeafc9c86aabf97acfb405c5907bc145d75))
- 2026-11-10 API, Core: Implement v4 file-level tight_stats (#18598) ([commit](https://github.com/apache/iceberg/commit/c136f05607c8a1e477ea307d34f42d5c024e53ef))
<!-- kb:generated:end -->

## Notes
