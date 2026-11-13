---
id: thread/t-2b9326ecf95a23e1
type: thread
title: 'OpenAPI: add CatalogObjectIdentifier schema'
date: '2026-05-12'
url: https://lists.apache.org/thread/xyzlndcp4x7zq6xydpcbp192ov9p2skz
kind: vote
status: passed
messages: 13
sources:
- devlist:xyzlndcp4x7zq6xydpcbp192ov9p2skz
refs:
- gh:apache/iceberg#16144
- gh:apache/iceberg#16160
- gh:apache/iceberg#12584
- gh:apache/iceberg#15830
- gh:apache/iceberg#15180
- doc:1NTQhgNbP2dkIMuXUMA5JdwliVQKCp1TU_ux5J_AaPiw
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:xyzlndcp4x7zq6xydpcbp192ov9p2skz
- rel: started_by
  to: person/stevenzwu
  confidence: observed
updated: '2026-11-13'
---

# OpenAPI: add CatalogObjectIdentifier schema

<!-- kb:generated:start -->
**Thread:** [[VOTE] OpenAPI: Add CatalogObjectIdentifier schema](https://lists.apache.org/thread/xyzlndcp4x7zq6xydpcbp192ov9p2skz) · **Started:** 2026-05-12 by [[person/stevenzwu|Steven Wu]] · **Messages:** 13 (last 2026-05-18) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

stevenzwu called a vote to add a CatalogObjectIdentifier schema to the REST catalog OpenAPI spec (PR #16144). The schema is an ordered list of hierarchical levels, a JSON array of strings, that identifies any catalog object such as a table, view, materialized view, namespace or function. It is structurally the same as Namespace, and the kind of object is determined by context, either the endpoint or a companion type discriminator, not by the identifier. The motivation is that the events endpoint (#12584), the resolve endpoint (#15830) and the functions endpoint (#15180) each need a generic identifier and would otherwise define their own. A Java implementation is in PR #16160. Only +1 votes were cast; pvary left a small suggestion on the PR. stevenzwu closed the vote as passed and said he would merge the OpenAPI change.

**Why it matters:** New REST endpoints for events, resolve and functions can reference one generic identifier schema instead of defining their own.

## Outcome

Passed with 12 +1 votes, 6 of them binding; no -1 or +0 votes. ([message](https://lists.apache.org/thread/4v7w45lm2v9fq6z60k2xwvzc55b4zndj), `devlist:4v7w45lm2v9fq6z60k2xwvzc55b4zndj`)

## Positions

- **[[person/stevenzwu|Steven Wu]]:** One shared CatalogObjectIdentifier schema avoids each new endpoint introducing its own identifier type as object types are added to the spec. ([message](https://lists.apache.org/thread/xyzlndcp4x7zq6xydpcbp192ov9p2skz))

References: [iceberg#16144](https://github.com/apache/iceberg/issues/16144), [iceberg#16160](https://github.com/apache/iceberg/issues/16160), [iceberg#12584](https://github.com/apache/iceberg/issues/12584), [iceberg#15830](https://github.com/apache/iceberg/issues/15830), [iceberg#15180](https://github.com/apache/iceberg/issues/15180), [doc](https://docs.google.com/document/d/1NTQhgNbP2dkIMuXUMA5JdwliVQKCp1TU_ux5J_AaPiw)
<!-- kb:generated:end -->

## Notes
