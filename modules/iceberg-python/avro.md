---
id: module/iceberg-python/avro
type: module
title: 'iceberg-python: avro'
repo: apache/iceberg-python
path: avro
commits_total: 73
commits_12m: 12
owners:
- Fokko
- rdblue
- rambleraptor
- samredai
- zhongyujiang
- kevinjqliu
links:
- rel: part_of
  to: repo/iceberg-python
  confidence: observed
updated: '2026-11-13'
---

# iceberg-python: avro

<!-- kb:generated:start -->
**Path:** `avro/` in [apache/iceberg-python](https://github.com/apache/iceberg-python) · **Commits:** 73 in total, 12 in the last 12 months.

## Who works here

Long-term authors (all time): [[person/Fokko|Fokko Driesprong]] (27), [[person/rdblue|Ryan Blue]] (3), [[person/rambleraptor|Alex Stephen]] (3), [[person/samredai|Sam Redai]] (2), [[person/zhongyujiang|Yujiang Zhong]] (2), [[person/kevinjqliu|Kevin Liu]] (2)

Most active authors (last 12 months): [[person/rambleraptor|Alex Stephen]] (2), [[person/geruh|Drew Gallardo]] (1), [[person/SaymV|Sam Verhasselt]] (1), [[person/m0g3r|m0g3r]] (1), [[person/hedger9487|hedger9487]] (1), [[person/akashchamp|akashchamp]] (1), [[person/Rodrigo-Palma|Rodrigo Stachlewski Palma]] (1), [[person/mbutrovich|Matt Butrovich]] (1)

Reviewer counts appear here once pull-request reviews are synced. Until then see `maps/reviewers.md`.

## Latest changes

- 2026-11-11 Skip unknown nested fields when resolving Avro read schemas (#4289) ([commit](https://github.com/apache/iceberg-python/commit/03e80a7b22dcc351935eb4e0dad7a7c75c8e85e1))
- 2026-11-09 Avro: read a file without avro.codec as uncompressed (#4296) ([commit](https://github.com/apache/iceberg-python/commit/2549061f904af87f85e1201f1bd6dc3ab2f1ba2c))
- 2026-10-10 Avro: Replace manual slots with dataclass slots (#4091) ([commit](https://github.com/apache/iceberg-python/commit/b32392dcbafd3b92415a5b5dc0444722ca2091d9))
- 2026-10-02 perf(avro): buffer records into size-bounded blocks (#4008) ([commit](https://github.com/apache/iceberg-python/commit/80e9041c6a4a3ae27b8bbb7b6a7ab0295766d2a4))
- 2026-09-24 fix(avro): advance the decoder when skipping an enum (#4009) ([commit](https://github.com/apache/iceberg-python/commit/0743814334b1caf86a54a2301e3e5b34d80aff0a))
- 2026-09-18 fix(avro): bound Cython decoder input (#3955) ([commit](https://github.com/apache/iceberg-python/commit/8c96d4211aa6571f2a31ad13d886cb25130a2ea0))
- 2026-09-11 Manifest: Use int for equality_ids in manifest schema per Iceberg spec (#3840) (#3842) ([commit](https://github.com/apache/iceberg-python/commit/8275a6f209a37f034373e084fccb6ec388f8e5f8))
- 2026-09-01 fix(avro): read doubles at full precision in the Cython decoder (#3808) ([commit](https://github.com/apache/iceberg-python/commit/d12f68042a459e5d4732bd6ee5a188e891b0dd44))
<!-- kb:generated:end -->

## Notes
