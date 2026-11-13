---
id: thread/t-61befdbae30765dd
type: thread
title: 'REST spec: add list and load function endpoints'
date: '2026-03-26'
url: https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m
kind: vote
status: passed
messages: 14
sources:
- devlist:qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m
refs:
- gh:apache/iceberg#15180
- gh:apache/iceberg#16144
links:
- rel: started_by
  to: person/huaxingao
  confidence: observed
updated: '2026-11-13'
---

# REST spec: add list and load function endpoints

<!-- kb:generated:start -->
**Thread:** [[VOTE][REST-SPEC] Add list and load function endpoints](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m) · **Started:** 2026-03-26 by [[person/huaxingao|Huaxin Gao]] · **Messages:** 14 (last 2026-06-06) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

huaxingao called a vote on adding two read-only REST catalog endpoints following the Iceberg UDF spec: GET /v1/{prefix}/namespaces/{namespace}/functions to list functions in a namespace and GET .../functions/{function} to load one. The load result returns inline UDF metadata and an optional metadata-location, following the load table and load view pattern; create, update and delete endpoints are to follow in a separate proposal. The original vote in March listed FunctionIdentifier objects in the list response. On June 1 huaxingao restarted the vote after the FunctionIdentifier versus CatalogObjectIdentifier question was resolved: PR 16144 merged CatalogObjectIdentifier and spec PR 15180 now uses it. szehon-ho voted +1 and suggested that tracking a specific-name in addition to definition-id would let engines refer to each overload, as a general addition to the function spec. The vote passed and huaxingao said she would merge the spec change.

**Why it matters:** REST catalogs gain standard endpoints for listing and loading UDFs, the first function support in the REST spec.

## Outcome

Passed with 10 +1 votes (5 binding), no -1 and no +0. The spec change in PR 15180 is to be merged. ([message](https://lists.apache.org/thread/ns3sm9g8w6pp22cztxmwfhd29v0sh9xo), `devlist:ns3sm9g8w6pp22cztxmwfhd29v0sh9xo`)

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** Add read-only list and load function endpoints to the REST spec, modeled on the table and view endpoints, with CRUD endpoints proposed separately. ([message](https://lists.apache.org/thread/qd7jb3fdx65mcjvcjomrxg7rgxf3yn0m))
- **[[person/szehon-ho|Szehon Ho]]:** Supports the endpoints; suggests the function spec track a specific-name besides definition-id so engines can reference each overloaded version. ([message](https://lists.apache.org/thread/ttmmgzqhsdqt35stgtvzjmfgl42hgvw2))

References: [iceberg#15180](https://github.com/apache/iceberg/issues/15180), [iceberg#16144](https://github.com/apache/iceberg/issues/16144)
<!-- kb:generated:end -->

## Notes
