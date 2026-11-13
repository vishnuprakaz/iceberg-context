---
id: initiative/collations
type: initiative
title: Collation support
status: design
updated: '2026-11-13'
sources:
- thread/t-e821af59b904a5ea
- thread/t-4438607328a252c1
- meeting/community/2026-10-28
- thread/t-44ddd498b576dea4
- meeting/community/2026-07-15
- thread/t-3948c81a19bd7c87
links:
- rel: championed_by
  to: person/laskoviymishka
  source: thread/t-e821af59b904a5ea
  confidence: extracted
- rel: touches
  to: module/iceberg/format
  source: thread/t-4438607328a252c1
  confidence: extracted
- rel: tracked_in
  to: gh:apache/iceberg#16972
  source: thread/t-e821af59b904a5ea
  confidence: extracted
---

# Collation support

<!-- kb:generated:start -->
## What it is

A proposal to let the Iceberg spec mark string fields with a collation (a rule for comparing and ordering text, for example case-insensitive), and to keep file-level lower and upper bounds that respect that collation, because plain UTF-8 bounds are not useful for pruning collated columns ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)). The hard part is that ICU collation results are not stable across ICU versions, so bounds have to say which version produced them ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).

## Current state

- The spec change is pull request [apache/iceberg#16972](https://github.com/apache/iceberg/pull/16972), written by Andrei Tserakhau, with an iceberg-go implementation ([apache/iceberg-go#1318](https://github.com/apache/iceberg-go/pull/1318)) and a Java proof of concept ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).
- Agreed at a dedicated sync on 2026-08-05: the ICU version stays an engine decision, bounds are stored as original strings tagged with the version that produced them plus a code-point metric, and equality deletes will be deprecated in V4 or not work on collated columns ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).
- Agreed on the dev list: a data file may carry collation bounds for more than one collation version. A reader uses a bound only if it can reproduce that version, which affects pruning and not correctness ([thread summary](../records/threads/2026/09/discuss-collation-one-vs-many-collation-versions-per-data-file-443860.md), [dev list](https://lists.apache.org/thread/4p8345gb8jo03l27qh86kbbpvolwc09j)).
- The pull request is now built on V4 stats-only fields, which simplified it; generated columns were mentioned as another way to store the min and max statistics ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Open: how the bounds are stored on top of stats-only fields. Ryan Blue preferred a new type with standardized metadata for collations ([thread summary](../records/threads/2026/10/discuss-stats-only-fields-44ddd4.md), [dev list](https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr)), and the 2026-10-28 sync noted that his latest comment on the pull request should be discussed with him directly ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Open: whether collations need to be part of V4. At the 2026-10-28 sync it was said that, as defined, collations could be added outside a format version ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Timeline

- 2026-03-28: Alexander Löser starts the dev list discussion proposing collations as an annotation on string fields with collation-aware bounds ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).
- 2026-06: Andrei Tserakhau posts spec pull request #16972, an iceberg-go implementation and a Java proof of concept ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).
- 2026-07-15: Collations are raised at the community sync; action item for Andrei to set up a separate sync in two weeks ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)).
- 2026-08-05: A dedicated sync agrees on engine-chosen ICU versions, original-string bounds with a version tag and a code-point metric; a second version of the design document follows ([thread summary](../records/threads/2026/03/discussion-collation-support-e821af.md), [dev list](https://lists.apache.org/thread/zdvc0gmqjgws8whwxv0ztn7h1jqclzyk)).
- 2026-08-31: Ryan Blue's proposal for field IDs of non-materialized columns in V4 lists collation bounds as one of the entry types ([thread summary](../records/threads/2026/08/discuss-field-id-tracking-for-non-materialized-columns-in-v4-3948c8.md), [dev list](https://lists.apache.org/thread/4h53r1nvvgxqymfvx7vcyhqgh1fk8180)).
- 2026-09-21: Thread on one or many collation versions per data file opens; it closes with multi-version bounds per file settled, and a planned 2026-10-28 dedicated sync is dropped ([thread summary](../records/threads/2026/09/discuss-collation-one-vs-many-collation-versions-per-data-file-443860.md), [dev list](https://lists.apache.org/thread/4p8345gb8jo03l27qh86kbbpvolwc09j)).
- 2026-10-22: In the stats-only fields thread, Andrei notes collation support could use them and Ryan Blue states his preference for a new type with standardized collation metadata ([thread summary](../records/threads/2026/10/discuss-stats-only-fields-44ddd4.md), [dev list](https://lists.apache.org/thread/t4nm0blbo33y5fnkcok6lrmdc4k4toxr)).
- 2026-10-28: Andrei asks for reviews of #16972 at the community sync ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Where help is needed

- Reviews of the collations spec pull request [apache/iceberg#16972](https://github.com/apache/iceberg/pull/16972) were requested at the community sync ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
<!-- kb:generated:end -->

## Notes
