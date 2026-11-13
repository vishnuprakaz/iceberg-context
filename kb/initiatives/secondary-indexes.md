---
id: initiative/secondary-indexes
type: initiative
title: Secondary indexes
status: design
updated: '2026-11-13'
sources:
- meeting/index/2026-05-27
- meeting/index/2026-06-08
- meeting/index/2026-06-22
- thread/t-a938dd33b7b841d9
- meeting/index/2026-08-03
- meeting/index/2026-08-17
- meeting/index/2026-09-28
- thread/t-7c950e8f34655555
- meeting/index/2026-10-26
- meeting/index/2026-11-09
links:
- rel: championed_by
  to: person/pvary
  confidence: extracted
  source: meeting/index/2026-11-09
- rel: championed_by
  to: person/huaxingao
  confidence: extracted
  source: meeting/index/2026-10-26
- rel: handled_by
  to: group/index
  confidence: extracted
  source: meeting/index/2026-11-09
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: meeting/index/2026-06-22
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: meeting/index/2026-10-26
- rel: tracked_in
  to: gh:apache/iceberg#16961
  confidence: extracted
  source: meeting/index/2026-11-09
- rel: tracked_in
  to: gh:apache/iceberg#16963
  confidence: extracted
  source: meeting/index/2026-11-09
---

# Secondary indexes

<!-- kb:generated:start -->
## What it is

The index working group is designing a secondary index for Iceberg tables, first for fast key lookup: sorted, non-overlapping index data files in a standard format under a single tracking file that records each file's key range ([index sync 2026-05-27](../records/meetings/index/2026/2026-05-27.md); [thread summary](../records/threads/2026/09/discuss-non-overlapping-index-region-files-7c950e.md), [dev list](https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h)). An index is its own catalog object with its own REST endpoints, reusing table machinery internally but not loadable or writable as a table ([index sync 2026-06-22](../records/meetings/index/2026/2026-06-22.md)). One motivation is letting writers find row positions by key and emit deletion vectors instead of equality deletes ([thread summary](../records/threads/2026/07/discuss-deprecate-equality-deletes-in-iceberg-v4-a938dd.md), [dev list](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6)).

## Current state

- Two pull requests carry the design: the index spec ([#16961](https://github.com/apache/iceberg/pull/16961)) and the REST catalog spec changes ([#16963](https://github.com/apache/iceberg/pull/16963)); neither has gone to a vote ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).
- The index metadata spec is to be settled before the REST spec is reviewed in depth, since the REST spec mirrors its JSON ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).
- Decided: an index is not a table and is a separate catalog entity with no pointers in table metadata ([index sync 2026-06-22](../records/meetings/index/2026/2026-06-22.md)); it reuses Iceberg's deletion vector format and starts copy-on-write only ([index sync 2026-06-08](../records/meetings/index/2026/2026-06-08.md)); index keys are a list of Iceberg expressions with no restriction on functions, and index data files are sorted by them ([index sync 2026-08-17](../records/meetings/index/2026/2026-08-17.md)).
- Decided on 9 November: REST routes are nested under the table, index names are unique per table, an optional endpoint lists a namespace's indexes; indexes follow a table rename and are dropped with the table; multi-table indexes are out of scope; derived columns are taken out of the index spec and handled as a separate proposal ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).
- Open: whether `loadTable` returns a table's indexes by default, and the wording for how read restrictions apply to indexes ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)); where range boundaries are stored, whether the range file schema is stored, and whether stats-only fields are allowed in indexes ([index sync 2026-10-26](../records/meetings/index/2026/2026-10-26.md)); whether to keep the index type field ([index sync 2026-09-28](../records/meetings/index/2026/2026-09-28.md)).
- The requirement that index region files never overlap was questioned on the dev list; its author kept it, arguing it gives one small file read per key lookup ([thread summary](../records/threads/2026/09/discuss-non-overlapping-index-region-files-7c950e.md), [dev list](https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h)).

## Timeline

- 2026-05-27: The sync sketches the structure: one tracking file over non-overlapping leaf files; the first version targets reasonably sized tables such as CDC and has no column updates ([index sync 2026-05-27](../records/meetings/index/2026/2026-05-27.md)).
- 2026-06-08: Agreed to reuse table library code and the existing deletion vector format, start copy-on-write only, and validate the spec with a hand-wired prototype ([index sync 2026-06-08](../records/meetings/index/2026/2026-06-08.md)).
- 2026-06-22: Decided that an index is its own object and a separate catalog entity; draft pull requests for the index spec and the REST spec are shared ([index sync 2026-06-22](../records/meetings/index/2026/2026-06-22.md)).
- 2026-08-03: Recommendation from offline discussions to limit scope to a single layout and full key lookup ([index sync 2026-08-03](../records/meetings/index/2026/2026-08-03.md)).
- 2026-08-17: Agreed that index keys are a list of Iceberg expressions and that region files are sorted by their values ([index sync 2026-08-17](../records/meetings/index/2026/2026-08-17.md)).
- 2026-09-30: Dev list thread on the non-overlap rule for region files ends without a change ([thread summary](../records/threads/2026/09/discuss-non-overlapping-index-region-files-7c950e.md), [dev list](https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h)).
- 2026-10-26: The REST spec pull request's design decisions and open questions are put to the community ([index sync 2026-10-26](../records/meetings/index/2026/2026-10-26.md)).
- 2026-11-09: Decisions on REST route nesting, rename and drop behaviour, and removing derived columns from the index spec ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).

## Where help is needed

- Review of the index spec pull request [#16961](https://github.com/apache/iceberg/pull/16961): its author said on 9 November that it is ready for review and has had no reviews in recent months ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).
- Review of the design decisions in the index REST spec pull request [#16963](https://github.com/apache/iceberg/pull/16963), an action item addressed to the community ([index sync 2026-10-26](../records/meetings/index/2026/2026-10-26.md)).
<!-- kb:generated:end -->

## Notes
