---
id: initiative/udf
type: initiative
title: SQL UDFs in catalogs
status: implementing
updated: '2026-11-13'
sources:
- thread/t-61befdbae30765dd
- meeting/read-restrictions/2026-05-26
- meeting/community/2026-06-24
- thread/t-5cba9bc4818eb482
- meeting/community/2026-07-15
- thread/t-709611fe90159e57
links:
- rel: championed_by
  to: person/huaxingao
  confidence: extracted
  source: thread/t-61befdbae30765dd
- rel: championed_by
  to: person/szehon-ho
  confidence: extracted
  source: thread/t-5cba9bc4818eb482
- rel: handled_by
  to: group/udf
  confidence: inferred
  source: thread/t-61befdbae30765dd
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-61befdbae30765dd
- rel: touches
  to: module/iceberg/format
  confidence: inferred
  source: thread/t-5cba9bc4818eb482
- rel: tracked_in
  to: gh:apache/iceberg#15180
  confidence: extracted
  source: thread/t-61befdbae30765dd
- rel: tracked_in
  to: gh:apache/iceberg#16727
  confidence: extracted
  source: thread/t-5cba9bc4818eb482
---

# SQL UDFs in catalogs

<!-- kb:generated:start -->
## What it is

Iceberg has a UDF spec that lets a catalog store the definition of a SQL function so that different engines can load and run the same function ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)). The current work adds function support to the REST catalog spec, starting with read-only endpoints, and refines the UDF spec itself, for example by naming each overload of a function ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m); [thread 2026-06-25](../records/threads/2026/06/vote-add-specific-name-to-udf-spec-5cba9b.md), [dev list](https://lists.apache.org/thread/75xs4trcgcpog8b2zoxpknf8bq6vfk4c)).

## Current state

- Decided: the REST spec gets two read-only endpoints, one to list the functions in a namespace and one to load a function; the vote passed with 10 +1 votes (5 binding) and the change is spec pull request [#15180](https://github.com/apache/iceberg/pull/15180) ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- Decided: the UDF spec gets a `specific-name` field that identifies one overload of a function; the vote on [#16727](https://github.com/apache/iceberg/pull/16727) passed with 5 binding and 4 non-binding +1 votes ([thread 2026-06-25](../records/threads/2026/06/vote-add-specific-name-to-udf-spec-5cba9b.md), [dev list](https://lists.apache.org/thread/75xs4trcgcpog8b2zoxpknf8bq6vfk4c)).
- Merged: the community sync notes list the list and load function endpoints in the REST spec ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and an optional `specific-name` in the UDF definition model ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) among the Java merges.
- Open: endpoints to create, update and delete functions were left for a separate proposal ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- Open: a proposal to ship generative AI and embedding functions in the Spark and Flink connectors, or as default UDFs under the UDF spec, drew two sceptical replies and no decision ([thread 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md), [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).

## Timeline

- 2026-03-26: Huaxin Gao called the vote on list and load function endpoints in the REST spec ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- 2026-05-26: the read restrictions sync listed decoupling the bound expression spec enhancement so that UDFs can be included; no outcome is recorded ([read restrictions sync 2026-05-26](../records/meetings/read-restrictions/2026/2026-05-26.md), [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- 2026-06-01: the vote was restarted after [#16144](https://github.com/apache/iceberg/pull/16144) merged `CatalogObjectIdentifier` and spec pull request [#15180](https://github.com/apache/iceberg/pull/15180) was changed to use it ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- 2026-06-06: the vote on the list and load function endpoints passed with 10 +1 votes (5 binding) ([thread 2026-03-26](../records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md), [dev list](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m)).
- 2026-06-24: the community sync notes list the function endpoints among the merged REST spec changes ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-25: Szehon Ho started the vote to add `specific-name` to the UDF spec ([thread 2026-06-25](../records/threads/2026/06/vote-add-specific-name-to-udf-spec-5cba9b.md), [dev list](https://lists.apache.org/thread/75xs4trcgcpog8b2zoxpknf8bq6vfk4c)).
- 2026-07-01: the `specific-name` vote passed with 5 binding and 4 non-binding +1 votes ([thread 2026-06-25](../records/threads/2026/06/vote-add-specific-name-to-udf-spec-5cba9b.md), [dev list](https://lists.apache.org/thread/75xs4trcgcpog8b2zoxpknf8bq6vfk4c)).
- 2026-07-15: the community sync notes list an optional `specific-name` in the UDF definition model among the Java merges ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-02: Alex Stephen asked whether Iceberg should ship AI functions in the connectors or as default UDFs; the thread is open ([thread 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md), [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).
<!-- kb:generated:end -->

## Notes
