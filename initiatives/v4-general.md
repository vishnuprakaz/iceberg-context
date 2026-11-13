---
id: initiative/v4-general
type: initiative
title: 'V4 spec: planning and other changes'
status: design
updated: '2026-11-13'
sources:
- thread/t-1d01d1d5d742962e
- meeting/community/2026-06-24
- thread/t-b838f79509420b04
- meeting/column-updates/2026-07-28
- meeting/community/2026-08-05
- meeting/column-updates/2026-08-11
- thread/t-bd70f40d4eb1876d
- thread/t-4fdcd748e0704aa5
- meeting/community/2026-10-07
- meeting/catalog/2026-10-14
- meeting/community/2026-10-28
- meeting/v4-metadata/2026-11-02
- meeting/catalog/2026-11-04
- meeting/index/2026-11-09
- meeting/materialized-views/2026-11-12
links:
- rel: championed_by
  to: person/danielcweeks
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
- rel: championed_by
  to: person/RussellSpitzer
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-11-02
- rel: handled_by
  to: group/community
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-10-14
- rel: touches
  to: module/iceberg/format
  confidence: inferred
  source: meeting/community/2026-10-28
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
- rel: tracked_in
  to: gh:apache/iceberg#17642
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
---

# V4 spec: planning and other changes

<!-- kb:generated:start -->
## What it is

V4 is the next version of the Iceberg table format, assembled from many separate spec changes that each have their own initiative page (column updates, statistics, row timestamps, encryption and others) ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). This page tracks what cuts across them: overall scope and timeline, how tables upgrade from V3, the REST catalog changes V4 needs, and smaller proposals that have no page of their own ([thread 2026-08-12](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky); [thread 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md), [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).

## Current state

- Scope and timeline: discussed at several community syncs with no decision recorded ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The latest progress report listed column updates ([#16425](https://github.com/apache/iceberg/pull/16425)) as needing review before a vote, vector type as in limbo, stats-only fields as in progress in the notes and as in a vote according to the recording, the row timestamp vote about to start, and default value expressions waiting on expression spec primitives; collations was said to be definable outside V4 and derived columns may or may not make V4 ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Process: a suggestion to run V4 like a release with a release manager was made and not decided ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Upgrade from V3: dev list participants agreed that upgrades stay cheap, that V4 readers must read older manifest lists and manifests, and that moving metadata to V4 structures is an implementation choice needing no spec work; documenting the behaviour of partially migrated tables was left open ([thread 2026-08-12](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky)). The column updates sync reached the same direction: on-demand, incremental migration in which V4 tables reference legacy V3 manifests ([column updates sync 2026-07-28](../records/meetings/column-updates/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- Snapshot operation: the column updates sync decided that the `operation` field in snapshot metadata expresses logical intent, and that the recent change converting an OVERWRITE to an APPEND when no files are deleted is to be reverted ([column updates sync 2026-08-11](../records/meetings/column-updates/2026/2026-08-11.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- REST catalog: participants converged on in-place model changes plus a v2 `loadTable` endpoint that V4 tables must be loaded through; a `rest-v4-changes` branch was created to collect the OpenAPI changes, with [#17642](https://github.com/apache/iceberg/pull/17642) open for feedback. No vote was held ([thread 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md), [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl); [catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- File formats: whether V4 should stop writing ORC and Avro data files is open ([V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)); see [File Format API and new file formats](file-format-api.md).
- Derived (generated) columns: an RFC was presented, proposing only stored columns for V4, and comments on the document were requested ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The index sync agreed to take derived columns out of the index spec until that proposal lands ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md), [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).
- Other proposals with no recorded outcome: `varchar` and `char` types in V4 ([#16829](https://github.com/apache/iceberg/pull/16829)) ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and writing incremental append scan semantics into the spec, where the proposer was pointed to V4 work on change-detection requirements ([thread 2026-07-23](../records/threads/2026/07/discuss-should-incremental-append-scan-semantics-be-part-of-the-spec-b838f7.md), [dev list](https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057)).
- Draft bitmap spec: a vote was held on adding a draft Mumbling bitmap spec to git ([#16518](https://github.com/apache/iceberg/pull/16518)) so it can be evaluated for V4 metadata; the thread shows eight +1 votes and no result message ([thread 2026-06-04](../records/threads/2026/06/vote-add-draft-bitmap-spec-to-git-1d01d1.md), [dev list](https://lists.apache.org/thread/59bn4jty8jmtbks8td8zfqodkcpro1hw)), and the community sync notes later list a draft Mumbling Bitmap spec among the Java merges ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Materialized views are framed as independent of the table spec and V4 ([materialized views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md), [notes](https://docs.google.com/document/d/1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A)).

## Timeline

- 2026-06-04: Ryan Blue called a vote to add a draft bitmap spec to version control, stating that using the format in tables would need future votes ([thread 2026-06-04](../records/threads/2026/06/vote-add-draft-bitmap-spec-to-git-1d01d1.md), [dev list](https://lists.apache.org/thread/59bn4jty8jmtbks8td8zfqodkcpro1hw)).
- 2026-06-24: `varchar` and `char` types in V4 were brought to the community sync; no outcome is recorded ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-23: a dev list thread asked whether incremental append scan semantics should be part of the spec; no decision ([thread 2026-07-23](../records/threads/2026/07/discuss-should-incremental-append-scan-semantics-be-part-of-the-spec-b838f7.md), [dev list](https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057)).
- 2026-07-28: the column updates sync agreed on on-demand, incremental migration from V3 to V4 ([column updates sync 2026-07-28](../records/meetings/column-updates/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- 2026-08-05: V4 scope was an agenda item at the community sync; no details are recorded ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-11: the column updates sync decided the snapshot `operation` field represents logical intent ([column updates sync 2026-08-11](../records/meetings/column-updates/2026/2026-08-11.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- 2026-08-13: the dev list thread on V3 to V4 upgrade expectations reached agreement that migration is an implementation choice ([thread 2026-08-12](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky)).
- 2026-08-13: the first REST spec changes needed for V4 were proposed on the dev list ([thread 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md), [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
- 2026-10-14: the catalog sync explained why a V2 load table endpoint is needed for V4 tables ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-10-28: the community sync heard a V4 progress report and a presentation of the derived columns RFC ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-04: the catalog sync was asked whether V4 REST changes should go into a separate branch; the notes record no outcome, and a branch was created on 2026-11-11 (next entries) ([catalog sync 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-11-09: the index sync agreed to continue derived columns as a table feature in parallel and to take them out of the index spec for now ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md), [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).
- 2026-11-11: a `rest-v4-changes` branch was created to collect the spec and OpenAPI changes for V4 tables ([message](https://lists.apache.org/thread/zrn1jb7g9wm7jgn4fx3klmtxs03k65zg), `devlist:zrn1jb7g9wm7jgn4fx3klmtxs03k65zg`; [thread 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md)).

## Where help is needed

- Column updates ([#16425](https://github.com/apache/iceberg/pull/16425)) was reported as needing review before it can go to a vote ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Comments were requested on the derived columns RFC document ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Feedback was requested on the REST spec changes for V4 in [#17642](https://github.com/apache/iceberg/pull/17642) ([thread 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md), [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
- A request to document how implementations migrate metadata and the limits of tables with mixed pre-V4 and V4 metadata has no recorded owner ([thread 2026-08-12](../records/threads/2026/08/discuss-v3-to-v4-upgrade-expectations-and-migration-practices-bd70f4.md), [dev list](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky)).
<!-- kb:generated:end -->

## Notes
