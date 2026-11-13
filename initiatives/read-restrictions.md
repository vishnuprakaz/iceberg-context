---
id: initiative/read-restrictions
type: initiative
title: Read restrictions (row filters and column masks) in the REST catalog
status: implementing
updated: '2026-11-13'
sources:
- thread/t-b9f73c21a4179dc6
- meeting/read-restrictions/2026-05-26
- thread/t-a1627a890918338f
- meeting/read-restrictions/2026-06-09
- thread/t-50827b2ab1b71544
- meeting/read-restrictions/2026-06-23
- meeting/catalog/2026-07-01
- meeting/read-restrictions/2026-07-07
- meeting/read-restrictions/2026-07-21
- meeting/read-restrictions/2026-08-04
- thread/t-cddba95ff30a75d7
- thread/t-3de1185baccbc276
- meeting/read-restrictions/2026-08-18
- thread/t-08d45a08d5e25761
- meeting/read-restrictions/2026-09-01
- meeting/read-restrictions/2026-09-15
- meeting/community/2026-09-16
- meeting/catalog/2026-09-23
- meeting/catalog/2026-10-14
- meeting/index/2026-11-09
links:
- rel: championed_by
  to: person/singhpk234
  confidence: extracted
  source: thread/t-08d45a08d5e25761
- rel: handled_by
  to: group/read-restrictions
  confidence: extracted
  source: meeting/read-restrictions/2026-09-15
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-10-14
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-08d45a08d5e25761
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/read-restrictions/2026-09-01
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/read-restrictions/2026-08-18
- rel: tracked_in
  to: gh:apache/iceberg#13879
  confidence: extracted
  source: thread/t-08d45a08d5e25761
---

# Read restrictions (row filters and column masks) in the REST catalog

<!-- kb:generated:start -->
## What it is

A REST catalog spec addition that lets a catalog return finer grained read restrictions (row filters and column masks) with the loadTable response, which the client engine must then apply ([thread, 2026-08-31](../records/threads/2026/08/vote-finer-grained-read-restrictions-in-the-iceberg-rest-catalog-spec-08d45a.md); [dev list](https://lists.apache.org/thread/0zloqhp8wkgyn04yg69j71cwcg5n7g74)) ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)). Defining and attaching policies stays a catalog concern ([thread, 2026-06-16](../records/threads/2026/06/discuss-write-path-gap-for-field-id-bound-policy-during-schema-evoluti-50827b.md); [dev list](https://lists.apache.org/thread/3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb)). Restrictions are written as expressions that refer to field ids, so policies survive renames ([Read Restrictions Sync, 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).

## Current state

- Spec: a vote on the spec change ([#13879](https://github.com/apache/iceberg/pull/13879)) was called on 2026-08-31. The recorded replies are 16 +1 votes (4 binding); the records contain no result message ([thread, 2026-08-31](../records/threads/2026/08/vote-finer-grained-read-restrictions-in-the-iceberg-rest-catalog-spec-08d45a.md); [dev list](https://lists.apache.org/thread/0zloqhp8wkgyn04yg69j71cwcg5n7g74)). "Finer grained read restrictions as part of loadTable in the spec" ([#13879](https://github.com/apache/iceberg/pull/13879)) is then listed among Java highlights at the community sync ([Community Sync, 2026-09-16](../records/meetings/community/2026/2026-09-16.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Decided before the vote: no client capabilities header. Read restrictions are allowed on the v1 loadTable endpoint with administrators responsible for verifying enforcement, and support becomes mandatory on a v2 endpoint ([thread, 2026-06-05](../records/threads/2026/06/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-a1627a.md); [dev list](https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9)).
- Decided before the vote: overlapping projections on a nested type and its descendants are disallowed, and readers fail closed ([thread, 2026-08-07](../records/threads/2026/08/discuss-read-restrictions-overlapping-column-projections-on-nested-typ-3de118.md); [dev list](https://lists.apache.org/thread/9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg)). Map keys are excluded from masks and geo types were removed from mask-to-default ([Read Restrictions Sync, 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- V2 load table: the field stays optional for servers; clients must fail if they receive read restrictions they cannot apply. The spec wording is to be tightened ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Implementation: the plan lists Iceberg Java (Actions API, REST scaffolding, generics) first, then PyIceberg and Iceberg Rust, with Spark and Trino as open questions ([Read Restrictions Sync, 2026-09-01](../records/meetings/read-restrictions/2026/2026-09-01.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)). Proofs of concept exist for Iceberg generics and Spark ([#16131](https://github.com/apache/iceberg/pull/16131), [#16082](https://github.com/apache/iceberg/pull/16082)) and a Trino code flow document ([Read Restrictions Sync, 2026-08-18](../records/meetings/read-restrictions/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)); the API for Actions is [#16198](https://github.com/apache/iceberg/pull/16198) ([Read Restrictions Sync, 2026-05-26](../records/meetings/read-restrictions/2026/2026-05-26.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)). The pull request stack is tracked in a GitHub project and is out for review ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Iceberg 1.13 was proposed, with a question mark, as the target for the Actions API and REST scaffolding ([Read Restrictions Sync, 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- Enforcement: in Spark the proof of concept uses an extension, where injected code remains a risk; work is under way in the Spark community to make this a native capability ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)). Whether the SDK should support the OAuth token exchange flow for trusted engines is open ([Catalog Community Sync, 2026-09-23](../records/meetings/catalog/2026/2026-09-23.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Indexes: the direction at the index sync was a general statement in the loadTable read restrictions section that restrictions apply whether the table, the index or both are read; the wording is open ([Index Support Sync, 2026-11-09](../records/meetings/index/2026/2026-11-09.md); [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).

## Timeline

- 2026-05-18: Thread proposes an X-Iceberg-Client-Capabilities header ([#16394](https://github.com/apache/iceberg/pull/16394)) ([thread, 2026-05-18](../records/threads/2026/05/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-b9f73c.md); [dev list](https://lists.apache.org/thread/xlqx6k7g625p38bxxy141wt02d00w2h4)).
- 2026-05-26: Read restrictions sync discusses the header and the dependency on expressions that reference a source id ([Read Restrictions Sync, 2026-05-26](../records/meetings/read-restrictions/2026/2026-05-26.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-06-09: After this sync the capabilities header is dropped in favour of the V1/V2 path and [#13879](https://github.com/apache/iceberg/pull/13879) is updated ([thread, 2026-06-05](../records/threads/2026/06/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-a1627a.md); [dev list](https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9)) ([Read Restrictions Sync, 2026-06-09](../records/meetings/read-restrictions/2026/2026-06-09.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-06-16: Thread on a write-path gap for field-id-bound policies during schema evolution ends without agreement ([thread, 2026-06-16](../records/threads/2026/06/discuss-write-path-gap-for-field-id-bound-policy-during-schema-evoluti-50827b.md); [dev list](https://lists.apache.org/thread/3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb)); the topic is listed at the catalog sync on 2026-07-01 ([Catalog Community Sync, 2026-07-01](../records/meetings/catalog/2026/2026-07-01.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-06-23: Call for review of [#13879](https://github.com/apache/iceberg/pull/13879) and [#16198](https://github.com/apache/iceberg/pull/16198) ([Read Restrictions Sync, 2026-06-23](../records/meetings/read-restrictions/2026/2026-06-23.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-07-07: Changes needed before the vote are named: mirror the adopted expressions spec into [#13879](https://github.com/apache/iceberg/pull/13879) and add IDReference ([Read Restrictions Sync, 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-07-21: The expression REST spec pull request ([#17138](https://github.com/apache/iceberg/pull/17138)) is reported ready for a vote; the plan is to merge it, then rebase and vote on read restrictions ([Read Restrictions Sync, 2026-07-21](../records/meetings/read-restrictions/2026/2026-07-21.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-08-04: Sync and thread on nested and conflicting masks ([Read Restrictions Sync, 2026-08-04](../records/meetings/read-restrictions/2026/2026-08-04.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)) ([thread, 2026-08-04](../records/threads/2026/08/discuss-read-restrictions-overlapping-column-projections-on-nested-typ-cddba9.md); [dev list](https://lists.apache.org/thread/zh25o2msbjw3skd577qzsyrcorobcthz)).
- 2026-08-07: Consensus to disallow overlapping nested projections; the spec pull request is updated ([thread, 2026-08-07](../records/threads/2026/08/discuss-read-restrictions-overlapping-column-projections-on-nested-typ-3de118.md); [dev list](https://lists.apache.org/thread/9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg)).
- 2026-08-18: Sync covers post-v1 evolution (position: no capability negotiation) and the proofs of concept ([Read Restrictions Sync, 2026-08-18](../records/meetings/read-restrictions/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-08-31: Vote on the spec change ([#13879](https://github.com/apache/iceberg/pull/13879)) is called ([thread, 2026-08-31](../records/threads/2026/08/vote-finer-grained-read-restrictions-in-the-iceberg-rest-catalog-spec-08d45a.md); [dev list](https://lists.apache.org/thread/0zloqhp8wkgyn04yg69j71cwcg5n7g74)); the sync on 2026-09-01 notes the vote in progress ([Read Restrictions Sync, 2026-09-01](../records/meetings/read-restrictions/2026/2026-09-01.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-09-15: Sync asks for PyIceberg and Rust volunteers and whether the sync is still needed ([Read Restrictions Sync, 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-09-16: The spec change is listed among Java highlights at the community sync ([Community Sync, 2026-09-16](../records/meetings/community/2026/2026-09-16.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-14: Catalog sync: call for review of the pull request stack, and clarification of the client requirement on V2 load table ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-11-09: Index sync discusses how read restrictions apply to indexes ([Index Support Sync, 2026-11-09](../records/meetings/index/2026/2026-11-09.md); [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).

## Where help is needed

- Volunteers were asked for to implement read restrictions in PyIceberg ([iceberg-python#3967](https://github.com/apache/iceberg-python/issues/3967)) and Iceberg Rust ([iceberg-rust#3361](https://github.com/apache/iceberg-rust/issues/3361)) ([Read Restrictions Sync, 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md); [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- The read restrictions pull request stack is out for review ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
<!-- kb:generated:end -->

## Notes
