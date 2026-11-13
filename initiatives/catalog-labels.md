---
id: initiative/catalog-labels
type: initiative
title: Catalog labels
status: implementing
updated: '2026-11-13'
sources:
- thread/t-c455572cb549f180
- thread/t-6b0913d5ecae698f
- meeting/catalog/2026-07-22
- meeting/catalog/2026-08-12
- thread/t-218176922d9b85f8
- thread/t-7111d9ac329a3767
- meeting/community/2026-09-16
- thread/t-f30173754f0d73b2
links:
- rel: championed_by
  to: person/laskoviymishka
  confidence: extracted
  source: thread/t-c455572cb549f180
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-08-12
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-c455572cb549f180
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: meeting/catalog/2026-08-12
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/catalog/2026-08-12
- rel: tracked_in
  to: gh:apache/iceberg#15750
  confidence: extracted
  source: thread/t-218176922d9b85f8
---

# Catalog labels

<!-- kb:generated:start -->
## What it is

Labels are an optional, read-only field on the REST catalog load response that lets a catalog return flat key-value metadata it already owns, such as ownership, cost attribution or classification, for a table and its columns ([thread summary](../records/threads/2026/03/discuss-table-and-column-label-metadata-in-iceberg-rest-catalog-c45557.md), [dev list](https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg)). They are kept apart from table properties and from the `config` map, and the spec does not interpret or enforce them ([thread summary](../records/threads/2026/08/discuss-table-and-column-label-metadata-in-iceberg-rest-catalog-218176.md), [dev list](https://lists.apache.org/thread/0mpgn3p2xhlf5165m40oxbptmcf7f87m)). Writing labels and structured tags are left to follow-up work ([thread summary](../records/threads/2026/03/discuss-table-and-column-label-metadata-in-iceberg-rest-catalog-c45557.md), [dev list](https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg)).

## Current state

- The read-path spec change ([#15750](https://github.com/apache/iceberg/pull/15750)) is in the REST spec; it was merged on 2026-09-09 ([#15750](https://github.com/apache/iceberg/pull/15750)). The 16 September community sync lists "a labels field in the REST spec" among Java highlights ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)), and a later thread starts from labels having landed in the REST spec ([thread summary](../records/threads/2026/09/discuss-catalog-provided-metadata-tables-f30173.md), [dev list](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn)). The vote thread on record has only +1 votes and no result message ([thread summary](../records/threads/2026/09/vote-rest-spec-labels-on-the-irc-read-path-7111d9.md), [dev list](https://lists.apache.org/thread/kf6cbb2lyjxcrno17q0wkb2k2hzglb52)).
- Reference implementation pull requests: [#17337](https://github.com/apache/iceberg/pull/17337) adds labels to the load table and view read path, [#17410](https://github.com/apache/iceberg/pull/17410) exposes them through `SupportsLabels`, and [#17411](https://github.com/apache/iceberg/pull/17411) exposes them in Spark 4.1 ([catalog sync 2026-08-12](../records/meetings/catalog/2026/2026-08-12.md)). All three were closed without being merged, on 2026-09-10 ([#17337](https://github.com/apache/iceberg/pull/17337), [#17411](https://github.com/apache/iceberg/pull/17411)) and 2026-09-11 ([#17410](https://github.com/apache/iceberg/pull/17410)).
- A `.labels` metadata table was proposed and dropped; the Java pull request [#18048](https://github.com/apache/iceberg/pull/18048) was closed in favour of Spark `DESCRIBE` ([#18049](https://github.com/apache/iceberg/pull/18049)) ([thread summary](../records/threads/2026/09/discuss-catalog-provided-metadata-tables-f30173.md), [dev list](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn)).
- Open: whether non-Java clients expose labels through their inspect APIs, starting with iceberg-go; the last message is an unanswered objection ([thread summary](../records/threads/2026/09/discuss-catalog-provided-metadata-tables-f30173.md), [dev list](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn)).
- A separate proposal for a first-class Tag entity in the REST catalog ended without a decision ([thread summary](../records/threads/2026/05/discuss-first-class-tag-concept-in-iceberg-rest-catalog-6b0913.md), [dev list](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b)).

## Timeline

- 2026-03-05: Andrei Tserakhau proposes an optional `labels` field on `LoadTableResponse`; later syncs agree to land the read API first and keep labels flat ([thread summary](../records/threads/2026/03/discuss-table-and-column-label-metadata-in-iceberg-rest-catalog-c45557.md), [dev list](https://lists.apache.org/thread/mptyj9nh6xd9zymbyq6qvf35j9x9hwyg)).
- 2026-05-04: Thread on a first-class Tag concept in the REST catalog; no decision ([thread summary](../records/threads/2026/05/discuss-first-class-tag-concept-in-iceberg-rest-catalog-6b0913.md), [dev list](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b)).
- 2026-07-22: A first vote thread on labels on the read path is marked withdrawn in the catalog sync notes ([catalog sync 2026-07-22](../records/meetings/catalog/2026/2026-07-22.md)).
- 2026-08-12: The catalog sync asks for final concerns before a vote ([catalog sync 2026-08-12](../records/meetings/catalog/2026/2026-08-12.md)).
- 2026-08-26: Thread on moving the read path to a vote; the one stated objector says he will not veto ([thread summary](../records/threads/2026/08/discuss-table-and-column-label-metadata-in-iceberg-rest-catalog-218176.md), [dev list](https://lists.apache.org/thread/0mpgn3p2xhlf5165m40oxbptmcf7f87m)).
- 2026-09-03: Vote thread on labels on the read path; five +1 votes captured, four of them binding ([thread summary](../records/threads/2026/09/vote-rest-spec-labels-on-the-irc-read-path-7111d9.md), [dev list](https://lists.apache.org/thread/kf6cbb2lyjxcrno17q0wkb2k2hzglb52)).
- 2026-09-16: The community sync lists the labels field in the REST spec among highlights ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).
- 2026-09-25: Thread on catalog-provided metadata tables; the labels metadata table is dropped ([thread summary](../records/threads/2026/09/discuss-catalog-provided-metadata-tables-f30173.md), [dev list](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn)).
<!-- kb:generated:end -->

## Notes
