---
id: initiative/v4-column-updates
type: initiative
title: V4 efficient column updates
status: design
updated: '2026-11-13'
sources:
- thread/t-7303ba875d84ed33
- thread/t-4a4da37a5d6b9841
- meeting/column-updates/2026-06-30
- thread/t-555b31c6e34eed92
- meeting/column-updates/2026-09-08
- thread/t-88c698db226931c9
- thread/t-ec167869ed1e0e08
- meeting/v4-metadata/2026-05-18
- meeting/v4-metadata/2026-10-05
- meeting/column-updates/2026-10-06
- meeting/v4-metadata/2026-11-02
- meeting/community/2026-10-28
- thread/t-9a2fc459da7341e3
- meeting/column-updates/2026-06-16
- meeting/column-updates/2026-07-14
- meeting/column-updates/2026-07-28
- meeting/column-updates/2026-08-11
- meeting/v4-metadata/2026-08-24
- meeting/column-updates/2026-10-20
- meeting/community/2026-08-26
links:
- rel: championed_by
  to: person/anuragmantri
  source: thread/t-9a2fc459da7341e3
  confidence: extracted
- rel: championed_by
  to: person/gaborkaszab
  source: thread/t-ec167869ed1e0e08
  confidence: extracted
- rel: handled_by
  to: group/column-updates
  source: meeting/column-updates/2026-10-06
  confidence: extracted
- rel: touches
  to: module/iceberg/format
  source: meeting/column-updates/2026-10-20
  confidence: extracted
- rel: touches
  to: module/iceberg/core
  source: meeting/community/2026-08-26
  confidence: extracted
- rel: tracked_in
  to: gh:apache/iceberg#16425
  source: meeting/community/2026-10-28
  confidence: extracted
- rel: tracked_in
  to: gh:apache/iceberg#16285
  source: thread/t-ec167869ed1e0e08
  confidence: extracted
---

# V4 efficient column updates

<!-- kb:generated:start -->
## What it is

A format version 4 feature that updates or adds columns by writing separate column files next to an existing data file, instead of rewriting the whole data file ([thread summary](../records/threads/2026/01/discuss-efficient-column-updates-in-iceberg-7303ba.md), [dev list](https://lists.apache.org/thread/2z1lxfo33t5rgbrzq5lvcyk9k5qd4509)). Readers stitch the base file and its column files together by row position ([thread summary](../records/threads/2026/06/discuss-column-update-file-representation-4a4da3.md), [dev list](https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo)). It lives in the table format and not in Parquet, because manifests keep complete stats and file lineage and the design is not tied to one file format ([thread summary](../records/threads/2026/01/discuss-efficient-column-updates-in-iceberg-7303ba.md), [dev list](https://lists.apache.org/thread/2z1lxfo33t5rgbrzq5lvcyk9k5qd4509)).

## Current state

- File representation, decided: column files are dense and positionally aligned with the base file, with NULL at positions deleted in the base file, so every leaf column in a column update is nullable ([thread summary](../records/threads/2026/06/discuss-column-update-file-representation-4a4da3.md), [dev list](https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo), [column updates sync 2026-06-30](../records/meetings/column-updates/2026/2026-06-30.md)).
- No persisted _pos column: the dev list thread concludes that _pos is not required and writing it in column files will not be allowed ([thread summary](../records/threads/2026/08/discuss-pos-column-in-efficient-column-updates-in-iceberg-555b31.md), [dev list](https://lists.apache.org/thread/sx4tndlb4vkcpj2yq9cob7fhddzd701x)). The 2026-09-08 sync notes word this as "writers are free to add it, but it will not be in the spec or in the Java implementation" ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)).
- No row group alignment flag in metadata; how writers align row groups is left to implementations ([thread summary](../records/threads/2026/08/discuss-column-updates-row-group-alignment-optimization-88c698.md), [dev list](https://lists.apache.org/thread/lqo71bs2hvzj38f4ljrkz77ncq4boltl)).
- Metadata, decided: the base file stays separate from the list of column files in a TrackedFile ([thread summary](../records/threads/2026/05/discuss-column-update-metadata-representation-ec1678.md), [dev list](https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg)). Changes are detected through REPLACED and MODIFIED entries ([V4 metadata sync 2026-05-18](../records/meetings/v4-metadata/2026/2026-05-18.md)), and the base file's data sequence number tracks the latest column update ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)).
- Metadata, simplification in progress: drop format_version (and, as proposed in the V4 metadata sync, split_offsets) from column files and use two snapshot IDs, created and modified ([V4 metadata sync 2026-10-05](../records/meetings/v4-metadata/2026/2026-10-05.md), [column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md)).
- Equality deletes are not supported with column files; they must be converted to deletion vectors before a column update ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)).
- Nested types: nested fields inside a struct can be updated; partial updates of a list or map are not allowed, replacing a whole list or map is ([V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md)).
- Spec: the column-update spec follow-up [apache/iceberg#16425](https://github.com/apache/iceberg/pull/16425) needs review before a vote ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Java: the pull request with basic fields and schemas for column files, [apache/iceberg#16285](https://github.com/apache/iceberg/pull/16285), was being updated to the simplified spec ([column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md)). The read path is built above the FormatModelRegistry with a stitching layer, exposed through DataFile ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)), and the first commit API is a simple update-and-append interface for column-only changes ([column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md)).

## Timeline

- 2026-01-27: Dev list discussion of Anurag Mantripragada's proposal. A February sync agrees the feature belongs in the table format; a May sync reaches consensus on the dense representation for partial updates ([thread summary](../records/threads/2026/01/discuss-efficient-column-updates-in-iceberg-7303ba.md), [dev list](https://lists.apache.org/thread/2z1lxfo33t5rgbrzq5lvcyk9k5qd4509)).
- 2026-05-18: V4 metadata sync concludes how REPLACED and MODIFIED statuses apply to column update changes ([V4 metadata sync 2026-05-18](../records/meetings/v4-metadata/2026/2026-05-18.md)).
- 2026-05-20: Threads opened on the column file representation when deletion vectors are present ([thread summary](../records/threads/2026/05/discuss-column-update-file-representation-9a2fc4.md), [dev list](https://lists.apache.org/thread/jbh1gbrso5h6l4by9rh9poy2cjjtb8j0)) and on the metadata representation ([thread summary](../records/threads/2026/05/discuss-column-update-metadata-representation-ec1678.md), [dev list](https://lists.apache.org/thread/7jryw9dfvc02s411twn4o7s5gjrybfxg)).
- 2026-06-02: Follow-up thread on file representation; ends with the sync decision to mandate NULL-filled, base-aligned column files ([thread summary](../records/threads/2026/06/discuss-column-update-file-representation-4a4da3.md), [dev list](https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo)).
- 2026-06-16: Sync weighs base file as a special entity versus base file as another ColumnFile; no choice recorded. Updates to partition columns are allowed in V4 ([column updates sync 2026-06-16](../records/meetings/column-updates/2026/2026-06-16.md)).
- 2026-06-30: Sync decides on the dense format with null fillers ([column updates sync 2026-06-30](../records/meetings/column-updates/2026/2026-06-30.md)).
- 2026-07-14: Base file representation discussed again; reviewers pointed to the Column Updates project board ([column updates sync 2026-07-14](../records/meetings/column-updates/2026/2026-07-14.md)).
- 2026-07-28: Sync reaches consensus on an on-demand, incremental v3-to-v4 metadata migration ([column updates sync 2026-07-28](../records/meetings/column-updates/2026/2026-07-28.md)).
- 2026-08-11: Column file structures have been folded into the V4 spec pull request; #16285 listed for review ([column updates sync 2026-08-11](../records/meetings/column-updates/2026/2026-08-11.md)).
- 2026-08-12: Row group alignment flag proposed and judged unnecessary ([thread summary](../records/threads/2026/08/discuss-column-updates-row-group-alignment-optimization-88c698.md), [dev list](https://lists.apache.org/thread/lqo71bs2hvzj38f4ljrkz77ncq4boltl)).
- 2026-08-24: Thread questioning the persisted _pos column; concludes that it will not be written ([thread summary](../records/threads/2026/08/discuss-pos-column-in-efficient-column-updates-in-iceberg-555b31.md), [dev list](https://lists.apache.org/thread/sx4tndlb4vkcpj2yq9cob7fhddzd701x)). The V4 metadata sync discusses an UpdateFiles interface merging RowDelta and column updates ([V4 metadata sync 2026-08-24](../records/meetings/v4-metadata/2026/2026-08-24.md)).
- 2026-09-08: Sync records removal of _pos, sequence number handling, the equality delete rule and the read path placement ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md)).
- 2026-10-05 and 2026-10-06: Spec simplifications for column file metadata; read-side stitching architecture; decision to start with a simple update-and-append commit API ([V4 metadata sync 2026-10-05](../records/meetings/v4-metadata/2026/2026-10-05.md), [column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md)).
- 2026-10-20: Column updates on nested types (structs first) and the spec follow-up #16425 are on the sync agenda ([column updates sync 2026-10-20](../records/meetings/column-updates/2026/2026-10-20.md)).
- 2026-10-28: V4 progress report: column updates (#16425) needs review before a vote ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- 2026-11-02: V4 metadata sync states the update granularity rule for nested types ([V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md)).

## Where help is needed

- Review of the column-update spec pull request [apache/iceberg#16425](https://github.com/apache/iceberg/pull/16425), which needs review before a vote ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Review of [apache/iceberg#16285](https://github.com/apache/iceberg/pull/16285) (basic fields and schemas for column files) was requested at the community sync ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md)).
- Ports to Go, C++, Python and Rust are anticipated: the read pull request is being structured to give them a clearer reference ([column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md)). No record names an owner for those ports.
<!-- kb:generated:end -->

## Notes
