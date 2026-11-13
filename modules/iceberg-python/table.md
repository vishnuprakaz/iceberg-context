---
id: module/iceberg-python/table
type: module
title: 'iceberg-python: table'
repo: apache/iceberg-python
path: table
commits_total: 411
commits_12m: 96
owners:
- Fokko
- kevinjqliu
- sungwy
- rambleraptor
- HonahX
- geruh
links:
- rel: part_of
  to: repo/iceberg-python
  confidence: observed
updated: '2026-11-13'
---

# iceberg-python: table

<!-- kb:generated:start -->
**Path:** `table/` in [apache/iceberg-python](https://github.com/apache/iceberg-python) · **Commits:** 411 in total, 96 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/Fokko|Fokko Driesprong]] (112), [[person/kevinjqliu|Kevin Liu]] (30), [[person/sungwy|Sung Yun]] (28), [[person/rambleraptor|Alex Stephen]] (18), [[person/HonahX|Honah J.]] (13), [[person/geruh|Drew Gallardo]] (11)

Most active authors (last 12 months): [[person/rambleraptor|Alex Stephen]] (9), [[person/geruh|Drew Gallardo]] (8), [[person/kevinjqliu|Kevin Liu]] (7), [[person/gabeiglio|Gabriel Igliozzi]] (4), [[person/xanderbailey|Xander]] (4), [[person/anxkhn|Anas Khan]] (3), [[person/avison9|David]] (3), [[person/dossett|Aaron Niskode-Dossett]] (3)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-13 fix: keep last_updated_ms from preceding the latest metadata-log entry (#4273) ([commit](https://github.com/apache/iceberg-python/commit/9eb83957292bd5b17e85c529bea0a84ab8de3a43))
- 2026-11-13 Row lineage: Preserve first_row_id from REST scan planning (#4352) ([commit](https://github.com/apache/iceberg-python/commit/5d043a219e2953b6628fa7d02703301c409c9eef))
- 2026-11-12 Add ManifestEntry.is_live() (#4351) ([commit](https://github.com/apache/iceberg-python/commit/ff5f5d434763310f2976dc24c19f0ad408dc13b4))
- 2026-11-12 Bind conflict-detection filters with the operation's case sensitivity (#4345) ([commit](https://github.com/apache/iceberg-python/commit/8a79207b9cf76b8ac15aaca8387323ad936cb512))
- 2026-11-12 Share unchanged models in update_table_metadata instead of deep-copying (#4303) ([commit](https://github.com/apache/iceberg-python/commit/8d1aa1509078db09711eb6a983d33fdaa105f14a))
- 2026-11-12 Skip copying the table metadata when a transaction has nothing staged (#4302) ([commit](https://github.com/apache/iceberg-python/commit/c97d6fc660709fa1832bb0480f7280c1ed3d80dd))
- 2026-11-11 Match NaN partition values with `IsNaN` in partition predicates (#4281) ([commit](https://github.com/apache/iceberg-python/commit/2b67a43f8edab423d1fd482a94c0c1f3fee87228))
- 2026-11-11 Add row-lineage support with Spark tests (#3972) ([commit](https://github.com/apache/iceberg-python/commit/e6ff315b4b24816f73078eb106e4afbb05758ad3))
<!-- kb:generated:end -->

## Notes
