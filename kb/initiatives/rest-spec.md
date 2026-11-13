---
id: initiative/rest-spec
type: initiative
title: 'REST catalog spec: other changes'
status: implementing
updated: '2026-11-13'
sources:
- thread/t-8853b84d399d7c2a
- thread/t-61befdbae30765dd
- thread/t-6b0913d5ecae698f
- thread/t-2b9326ecf95a23e1
- thread/t-3a558d67a81956a4
- thread/t-b9f73c21a4179dc6
- thread/t-584ad622bd8bd6d8
- meeting/community/2026-06-03
- thread/t-a1627a890918338f
- meeting/catalog/2026-06-10
- meeting/community/2026-06-24
- thread/t-b838f79509420b04
- thread/t-8d54c4be3c9cc0d5
- thread/t-6c49480676915b91
- meeting/community/2026-08-05
- thread/t-4fdcd748e0704aa5
- meeting/catalog/2026-09-02
- thread/t-64d9cbfda2cf0c40
- thread/t-0fe216b27de16fe7
- thread/t-ef8a98c0e0dd42ed
- meeting/catalog/2026-10-14
- thread/t-0fffc650114a3f55
- thread/t-4c863ceec72fa0da
- meeting/community/2026-10-28
- thread/t-fd1e0ca37f3dd78c
- meeting/catalog/2026-11-04
- meeting/index/2026-11-09
links:
- rel: championed_by
  to: person/singhpk234
  confidence: extracted
  source: thread/t-8d54c4be3c9cc0d5
- rel: championed_by
  to: person/rdblue
  confidence: extracted
  source: thread/t-584ad622bd8bd6d8
- rel: championed_by
  to: person/stevenzwu
  confidence: extracted
  source: thread/t-2b9326ecf95a23e1
- rel: championed_by
  to: person/huaxingao
  confidence: extracted
  source: thread/t-61befdbae30765dd
- rel: championed_by
  to: person/rahulsmahadev
  confidence: extracted
  source: thread/t-ef8a98c0e0dd42ed
- rel: championed_by
  to: person/danielcweeks
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-11-04
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-584ad622bd8bd6d8
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: tracked_in
  to: gh:apache/iceberg#17642
  confidence: extracted
  source: thread/t-4fdcd748e0704aa5
- rel: tracked_in
  to: gh:apache/iceberg#17727
  confidence: extracted
  source: thread/t-ef8a98c0e0dd42ed
---

# REST catalog spec: other changes

<!-- kb:generated:start -->
## What it is

The REST catalog specification is the OpenAPI document that defines how clients talk to an Iceberg catalog over HTTP. This page collects the changes to it that do not have their own initiative page: new endpoints and schemas, headers, clarifications, and the adjustments needed for V4 tables ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)). Changes are put to a vote on the dev list ([thread, 2026-05-20](../records/threads/2026/05/vote-add-unregister-endpoint-to-the-rest-spec-584ad6.md); [dev list](https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g)).

## Current state

- Adopted by vote: list and load function endpoints ([#15180](https://github.com/apache/iceberg/pull/15180)) ([thread, 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md); [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)); the CatalogObjectIdentifier schema ([#16144](https://github.com/apache/iceberg/pull/16144)) ([thread, 2026-05-12](../records/threads/2026/05/vote-openapi-add-catalogobjectidentifier-schema-2b9326.md); [dev list](https://lists.apache.org/thread/xyzlndcp4x7zq6xydpcbp192ov9p2skz)); the unregister table endpoint ([#16400](https://github.com/apache/iceberg/pull/16400)) ([thread, 2026-05-20](../records/threads/2026/05/vote-add-unregister-endpoint-to-the-rest-spec-584ad6.md); [dev list](https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g)); and the value `none` for the X-Iceberg-Access-Delegation header ([#18480](https://github.com/apache/iceberg/pull/18480), merged on 2026-10-29) ([thread, 2026-10-25](../records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md); [dev list](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk)).
- Also adopted by vote: aligning the OpenAPI expressions with the expression spec ([#17138](https://github.com/apache/iceberg/pull/17138)) ([thread, 2026-07-24](../records/threads/2026/07/vote-align-rest-openapi-expressions-with-the-iceberg-expression-specif-8d54c4.md); [dev list](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38)), which passed with 4 binding and 10 non-binding +1 votes ([result message](https://lists.apache.org/thread/9ncgm04vd20lds0c3q99smvotjpxzjt8)) and was merged on 2026-07-27; and adding the variant type ([#17256](https://github.com/apache/iceberg/pull/17256)) ([thread, 2026-07-30](../records/threads/2026/07/vote-rest-spec-add-variant-type-to-the-rest-catalog-spec-6c4948.md); [dev list](https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9)), which passed with 7 binding and 15 non-binding +1 votes ([result message](https://lists.apache.org/thread/2plrmco4k7vvb1jd8ythvjvko6nk6q9w)) and was merged on 2026-08-02. Both are listed afterwards among merged REST spec changes, together with a formalized remote signing configuration ([Community Sync, 2026-08-05](../records/meetings/community/2026/2026-08-05.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- User-Agent format ([#17727](https://github.com/apache/iceberg/pull/17727)): a recommended, advisory format for client identification. The vote was reopened after review comments ([thread, 2026-10-02](../records/threads/2026/10/vote-recommend-a-standard-user-agent-format-for-rest-clients-reopen-ef8a98.md); [dev list](https://lists.apache.org/thread/bzs62qqt9k4t9sr76pk0d36l47zwcpyb)) and passed with 19 +1 votes (10 binding, 9 non-binding) and no 0 or -1 votes ([result message](https://lists.apache.org/thread/pllz983cvffryzcwskglsr0cyo7p0gxx)). The pull request was merged on 2026-11-10 ([#17727](https://github.com/apache/iceberg/pull/17727)).
- V4: participants converged on changing the models in place plus a new v2 loadTable endpoint that all V4 tables must be loaded through; [#17642](https://github.com/apache/iceberg/pull/17642) is open for feedback ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)). Metadata updates wait for the check constraints, default values and stats-only fields specs to close ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)). Whether V4 REST changes go into a separate branch was asked at the catalog sync ([Catalog Community Sync, 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)); on 2026-11-11 a `rest-v4-changes` branch was created to collect the spec and OpenAPI changes for V4 tables, isolated to spec changes, while request, response and metadata parser implementations are reviewed as usual ([message, 2026-11-11](https://lists.apache.org/thread/zrn1jb7g9wm7jgn4fx3klmtxs03k65zg), `devlist:zrn1jb7g9wm7jgn4fx3klmtxs03k65zg`).
- A generic client capabilities header ([#16394](https://github.com/apache/iceberg/pull/16394)) was dropped ([thread, 2026-06-05](../records/threads/2026/06/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-a1627a.md); [dev list](https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9)).
- Metrics reporting endpoint: repliers agreed to leave the spec unchanged; clients are not required to retry failed reports ([thread, 2026-11-03](../records/threads/2026/11/discuss-rest-catalog-spec-semantics-of-the-metrics-reporting-endpoint--fd1e0c.md); [dev list](https://lists.apache.org/thread/1nfwnk1j8sppmsry675ygr1jbxyhvrdx)).
- OpenAPI 3.1 validity: replacing `nullable` with type arrays ([#18428](https://github.com/apache/iceberg/pull/18428)) was supported and approved; the thread does not say it was merged ([thread, 2026-10-21](../records/threads/2026/10/discussion-replace-nullable-with-type-arrays-in-rest-catalog-openapi-s-0fffc6.md); [dev list](https://lists.apache.org/thread/6y4txojozlrhoslkkygcp3lkdyv2sktf)).
- Open without a decision: multi-table, multi-statement transactions ([thread, 2025-06-17](../records/threads/2025/06/discuss-multi-statement-multi-transaction-proposal-for-apache-rest-cat-8853b8.md); [dev list](https://lists.apache.org/thread/r5otylsrm4txd4oxyv7c6scdwrbolck9)); a first-class Tag concept alongside labels ([thread, 2026-05-04](../records/threads/2026/05/discuss-first-class-tag-concept-in-iceberg-rest-catalog-6b0913.md); [dev list](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b)); whether incremental append scan semantics belong in the spec ([thread, 2026-07-23](../records/threads/2026/07/discuss-should-incremental-append-scan-semantics-be-part-of-the-spec-b838f7.md); [dev list](https://lists.apache.org/thread/o0wsy3jot3vos7zpqop4xk48k0hzf057)).
- In review: field-id guidance for AddSchemaUpdate versus CreateTableRequest ([#17137](https://github.com/apache/iceberg/pull/17137)) ([Catalog Community Sync, 2026-09-02](../records/meetings/catalog/2026/2026-09-02.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)); scan planning returning pre-signed URLs ([#17457](https://github.com/apache/iceberg/pull/17457)) and pre-signing through the sign endpoint ([#18080](https://github.com/apache/iceberg/pull/18080)) ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Index endpoints: index routes are nested under the table and index names are unique per table; the index metadata spec is to be settled before the REST spec ([#16963](https://github.com/apache/iceberg/pull/16963)) ([Index Support Sync, 2026-11-09](../records/meetings/index/2026/2026-11-09.md); [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).

## Timeline

- 2025-06-17: Thread on multi-table, multi-statement transactions starts; a proof-of-concept report in October 2026 has no replies ([thread, 2025-06-17](../records/threads/2025/06/discuss-multi-statement-multi-transaction-proposal-for-apache-rest-cat-8853b8.md); [dev list](https://lists.apache.org/thread/r5otylsrm4txd4oxyv7c6scdwrbolck9)).
- 2026-03-26: Vote on list and load function endpoints starts; restarted on 1 June and passed ([thread, 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md); [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- 2026-05-04: Thread on a first-class Tag concept; no conclusion ([thread, 2026-05-04](../records/threads/2026/05/discuss-first-class-tag-concept-in-iceberg-rest-catalog-6b0913.md); [dev list](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b)).
- 2026-05-12: Vote on the CatalogObjectIdentifier schema; passed ([thread, 2026-05-12](../records/threads/2026/05/vote-openapi-add-catalogobjectidentifier-schema-2b9326.md); [dev list](https://lists.apache.org/thread/xyzlndcp4x7zq6xydpcbp192ov9p2skz)).
- 2026-05-18: Discussion of an unregister table endpoint ([thread, 2026-05-18](../records/threads/2026/05/discuss-adding-unregister-table-endpoint-to-rest-spec-3a558d.md); [dev list](https://lists.apache.org/thread/q60ymn6rq1qzs102zj0vm0fnqjjv0knw)) and of a client capabilities header ([thread, 2026-05-18](../records/threads/2026/05/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-b9f73c.md); [dev list](https://lists.apache.org/thread/xlqx6k7g625p38bxxy141wt02d00w2h4)).
- 2026-05-20: Vote on the unregister endpoint; passed with 9 binding and 7 non-binding +1 votes ([thread, 2026-05-20](../records/threads/2026/05/vote-add-unregister-endpoint-to-the-rest-spec-584ad6.md); [dev list](https://lists.apache.org/thread/vy9fqyopp9c149oy40brdhb10grpq32g)).
- 2026-06-03: CatalogObjectIdentifier and the unregister endpoint are listed as merged ([Community Sync, 2026-06-03](../records/meetings/community/2026/2026-06-03.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-09: The capabilities header is dropped after the read restrictions sync ([thread, 2026-06-05](../records/threads/2026/06/discuss-adding-x-iceberg-client-capabilities-header-to-rest-spec-a1627a.md); [dev list](https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9)).
- 2026-06-10: Catalog sync calls for review of URL versus form encoding ([#15989](https://github.com/apache/iceberg/pull/15989)), events ([#12584](https://github.com/apache/iceberg/pull/12584)) and definer views ([#15895](https://github.com/apache/iceberg/pull/15895)) ([Catalog Community Sync, 2026-06-10](../records/meetings/catalog/2026/2026-06-10.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-06-24: List and load function endpoints are listed as merged ([Community Sync, 2026-06-24](../records/meetings/community/2026/2026-06-24.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-24: Vote on aligning OpenAPI expressions with the expression spec ([#17138](https://github.com/apache/iceberg/pull/17138)) ([thread, 2026-07-24](../records/threads/2026/07/vote-align-rest-openapi-expressions-with-the-iceberg-expression-specif-8d54c4.md); [dev list](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38)).
- 2026-07-27: The expression alignment vote passes with 4 binding and 10 non-binding +1 votes ([result message](https://lists.apache.org/thread/9ncgm04vd20lds0c3q99smvotjpxzjt8)); [#17138](https://github.com/apache/iceberg/pull/17138) is merged the same day.
- 2026-07-30: Vote on adding the variant type ([#17256](https://github.com/apache/iceberg/pull/17256)) ([thread, 2026-07-30](../records/threads/2026/07/vote-rest-spec-add-variant-type-to-the-rest-catalog-spec-6c4948.md); [dev list](https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9)).
- 2026-08-02: The variant type vote passes with 7 binding and 15 non-binding +1 votes ([result message](https://lists.apache.org/thread/2plrmco4k7vvb1jd8ythvjvko6nk6q9w)); [#17256](https://github.com/apache/iceberg/pull/17256) is merged the same day.
- 2026-08-05: VariantType, remote signing configuration and expression alignment are listed as merged REST spec changes ([Community Sync, 2026-08-05](../records/meetings/community/2026/2026-08-05.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-13: Thread on the initial REST changes for V4 starts ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
- 2026-09-02: Thread proposing a standard User-Agent format; every reply supports it ([thread, 2026-09-02](../records/threads/2026/09/discuss-recommend-a-standard-user-agent-format-for-rest-clients-64d9cb.md); [dev list](https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9)).
- 2026-09-23: First User-Agent vote; paused for further review comments ([thread, 2026-09-23](../records/threads/2026/09/vote-recommend-a-standard-user-agent-format-for-rest-clients-0fe216.md); [dev list](https://lists.apache.org/thread/79b5p9pfjso9d8tbs1w10619qz61rt85)).
- 2026-10-02: User-Agent vote reopened ([thread, 2026-10-02](../records/threads/2026/10/vote-recommend-a-standard-user-agent-format-for-rest-clients-reopen-ef8a98.md); [dev list](https://lists.apache.org/thread/bzs62qqt9k4t9sr76pk0d36l47zwcpyb)).
- 2026-10-09: The User-Agent vote passes with 19 +1 votes (10 binding, 9 non-binding) and no 0 or -1 votes ([result message](https://lists.apache.org/thread/pllz983cvffryzcwskglsr0cyo7p0gxx)).
- 2026-10-14: Catalog sync explains why a V2 load table endpoint is needed for V4 ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-10-21: Thread on replacing `nullable` with type arrays ([#18428](https://github.com/apache/iceberg/pull/18428)) ([thread, 2026-10-21](../records/threads/2026/10/discussion-replace-nullable-with-type-arrays-in-rest-catalog-openapi-s-0fffc6.md); [dev list](https://lists.apache.org/thread/6y4txojozlrhoslkkygcp3lkdyv2sktf)).
- 2026-10-25: Vote on `none` for X-Iceberg-Access-Delegation ([#18480](https://github.com/apache/iceberg/pull/18480)); passed with 3 binding and 4 non-binding +1 votes ([thread, 2026-10-25](../records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md); [dev list](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk)).
- 2026-11-03: Thread on the metrics reporting endpoint; spec left unchanged ([thread, 2026-11-03](../records/threads/2026/11/discuss-rest-catalog-spec-semantics-of-the-metrics-reporting-endpoint--fd1e0c.md); [dev list](https://lists.apache.org/thread/1nfwnk1j8sppmsry675ygr1jbxyhvrdx)).
- 2026-11-04: Catalog sync asks whether V4 REST changes should go into a separate branch ([Catalog Community Sync, 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-11-09: Index sync decides index routes are nested under the table ([Index Support Sync, 2026-11-09](../records/meetings/index/2026/2026-11-09.md); [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).
- 2026-11-10: The User-Agent pull request is merged ([#17727](https://github.com/apache/iceberg/pull/17727)).
- 2026-11-11: A `rest-v4-changes` branch is created to collect the spec and OpenAPI changes for V4 tables, following the catalog sync discussion ([message, 2026-11-11](https://lists.apache.org/thread/zrn1jb7g9wm7jgn4fx3klmtxs03k65zg), `devlist:zrn1jb7g9wm7jgn4fx3klmtxs03k65zg`).

## Where help is needed

- Committers were asked to review [#18073](https://github.com/apache/iceberg/pull/18073), which makes REST clients load only the latest snapshot in refs mode ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Feedback is wanted on [#17642](https://github.com/apache/iceberg/pull/17642), the in-place model changes for V4 ([thread, 2026-08-13](../records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [dev list](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl)).
- Calls for review: scan planning returning pre-signed URLs ([#17457](https://github.com/apache/iceberg/pull/17457)) and pre-signing through the sign endpoint ([#18080](https://github.com/apache/iceberg/pull/18080)) ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- The question whether the REST spec should define transactions or only the primitives catalogs need has no replies ([thread, 2025-06-17](../records/threads/2025/06/discuss-multi-statement-multi-transaction-proposal-for-apache-rest-cat-8853b8.md); [dev list](https://lists.apache.org/thread/r5otylsrm4txd4oxyv7c6scdwrbolck9)).
<!-- kb:generated:end -->

## Notes
