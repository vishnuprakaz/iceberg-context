---
id: module/iceberg-python/expressions
type: module
title: 'iceberg-python: expressions'
repo: apache/iceberg-python
path: expressions
commits_total: 139
commits_12m: 36
owners:
- Fokko
- kevinjqliu
- rdblue
- rambleraptor
- danielcweeks
- geruh
links:
- rel: part_of
  to: repo/iceberg-python
  confidence: observed
updated: '2026-11-13'
---

# iceberg-python: expressions

<!-- kb:generated:start -->
**Path:** `expressions/` in [apache/iceberg-python](https://github.com/apache/iceberg-python) · **Commits:** 139 in total, 36 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/Fokko|Fokko Driesprong]] (44), [[person/kevinjqliu|Kevin Liu]] (7), [[person/rdblue|Ryan Blue]] (6), [[person/rambleraptor|Alex Stephen]] (5), [[person/danielcweeks|Daniel C. Weeks]] (4), [[person/geruh|Drew Gallardo]] (4)

Most active authors (last 12 months): [[person/kevinjqliu|Kevin Liu]] (5), [[person/rambleraptor|Alex Stephen]] (4), [[person/Fokko|Fokko Driesprong]] (4), [[person/geruh|Drew Gallardo]] (3), [[person/ebyhr|Yuya Ebihara]] (3), [[person/dossett|Aaron Niskode-Dossett]] (3), [[person/Rodrigo-Palma|Rodrigo Stachlewski Palma]] (2), [[person/AP24110011695|ayush]] (2)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-11 fix(expressions): reject non-finite floats on conversion to Decimal (#4287) ([commit](https://github.com/apache/iceberg-python/commit/d570334f2d09c0acead6ba141972b67f203f3fad))
- 2026-11-11 fix: handle negative-scale Decimals in increment, decrement and truncate_decimal (#4285) ([commit](https://github.com/apache/iceberg-python/commit/c5aadd9af07e8a849b5773168ec475644eea60d2))
- 2026-10-28 Cache residuals with stateless evaluators (#3666) ([commit](https://github.com/apache/iceberg-python/commit/0992d661a9bb540265fde4e8f397fecdfb55a510))
- 2026-10-27 fix: raise when binding starts-with with an out-of-range literal (#4144) ([commit](https://github.com/apache/iceberg-python/commit/0a2e7caa65502be3d5090bc053292439c2253cf6))
- 2026-10-24 fix(expressions): reject fractional decimal literals on integer columns (#4029) ([commit](https://github.com/apache/iceberg-python/commit/58df2cca5c82c0e6cdb2668da7f5834b88d3bee9))
- 2026-10-24 fix(conversions): reject a Decimal whose scale is negative (#3997) ([commit](https://github.com/apache/iceberg-python/commit/46669fad031d5b4e7a71c1df13940d17bbc9e71d))
- 2026-10-24 Infra: Replace archived pydocstyle hook with ruff D rules (#4014) ([commit](https://github.com/apache/iceberg-python/commit/5d5ce48f87de5ae4a769f2b77b006151c7c1b240))
- 2026-09-18 fix(expressions): bound the DNF expansion in rewrite_to_dnf (#3995) ([commit](https://github.com/apache/iceberg-python/commit/8408a5dfeab665aa53f64bed5ab0c7b02b39dfbb))
<!-- kb:generated:end -->

## Notes
