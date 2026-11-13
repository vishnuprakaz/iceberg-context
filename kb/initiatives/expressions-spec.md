---
id: initiative/expressions-spec
type: initiative
title: Expressions specification
status: accepted
updated: '2026-11-13'
sources:
- thread/t-2625714567b6a82f
- thread/t-8ba58766eb647f36
- meeting/community/2026-07-15
- thread/t-8d54c4be3c9cc0d5
- meeting/community/2026-08-05
- meeting/read-restrictions/2026-07-21
- meeting/read-restrictions/2026-07-07
- thread/t-33958badf295b701
- meeting/community/2026-10-28
- meeting/index/2026-08-17
- meeting/read-restrictions/2026-05-26
- thread/t-2932dfb021d2cdf3
- meeting/index/2026-08-03
- meeting/index/2026-08-31
- meeting/index/2026-09-14
links:
- rel: championed_by
  to: person/rdblue
  source: thread/t-2625714567b6a82f
  confidence: extracted
- rel: championed_by
  to: person/singhpk234
  source: thread/t-8d54c4be3c9cc0d5
  confidence: extracted
- rel: touches
  to: module/iceberg/format
  source: thread/t-2625714567b6a82f
  confidence: extracted
- rel: touches
  to: module/iceberg/open-api
  source: thread/t-8d54c4be3c9cc0d5
  confidence: extracted
- rel: tracked_in
  to: gh:apache/iceberg#16652
  source: thread/t-2625714567b6a82f
  confidence: extracted
---

# Expressions specification

<!-- kb:generated:start -->
## What it is

A spec that defines the minimal structure and behaviour of expressions that Iceberg formats need to store and exchange ([thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-262571.md), [dev list](https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o)). It cleans up the filter expressions exchanged through the REST catalog and makes it possible to store expressions in metadata, for example default values such as current_timestamp() and CHECK constraints ([thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-262571.md), [dev list](https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o)).

## Current state

- Adopted: the vote on the expressions spec ([apache/iceberg#16652](https://github.com/apache/iceberg/pull/16652)) passed with 30 +1 votes, 13 of them binding ([thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-8ba587.md), [dev list](https://lists.apache.org/thread/7wmhcjwv8opxh4hgj284w5yl578rnbjz)), and the spec is listed as merged in the 2026-07-15 community sync highlights ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)).
- REST: pull request [apache/iceberg#17138](https://github.com/apache/iceberg/pull/17138) aligns the REST OpenAPI expression schemas with the spec ([thread summary](../records/threads/2026/07/vote-align-rest-openapi-expressions-with-the-iceberg-expression-specif-8d54c4.md), [dev list](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38)). Its vote passed with 4 binding and 10 non-binding +1 votes and no 0 or -1 votes ([result message](https://lists.apache.org/thread/9ncgm04vd20lds0c3q99smvotjpxzjt8)), and the pull request was merged on 2026-07-27 ([#17138](https://github.com/apache/iceberg/pull/17138)). A follow-up pull request was to update the Java parser and model ([read restrictions sync 2026-07-21](../records/meetings/read-restrictions/2026/2026-07-21.md)).
- Read restrictions build on it: [apache/iceberg#13879](https://github.com/apache/iceberg/pull/13879) was to mirror the adopted spec, replace the deprecated 'term' labels with 'left'/'right', and add IDReference so policies bind to field ids ([read restrictions sync 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md)). That pull request was merged on 2026-09-03 ([#13879](https://github.com/apache/iceberg/pull/13879)).
- V4 default value expressions build on it: the vote on [apache/iceberg#16777](https://github.com/apache/iceberg/pull/16777), which lets write-default hold an expression as defined by this spec, passed with 11 binding and 7 non-binding +1 votes ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob), [result message](https://lists.apache.org/thread/h5jnk7l2op325x545hfnrpbo3qmh2ovo)), and the pull request was merged on 2026-11-06 ([#16777](https://github.com/apache/iceberg/pull/16777)). On 2026-10-28 that spec was said to depend on expression spec primitives landing first ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Secondary indexes build on it: the index sync agreed that index_keys are a list of Iceberg expressions, with no restriction on the functions used ([index sync 2026-08-17](../records/meetings/index/2026/2026-08-17.md)).
- A derived (generated) columns RFC that builds on the expressions spec was presented on 2026-10-28, with a request for comments on the document ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Timeline

- 2026-05-26: The read restrictions sync discusses decoupling the bound expression spec enhancement; read restrictions depend on expressions referencing a source id instead of a name ([read restrictions sync 2026-05-26](../records/meetings/read-restrictions/2026/2026-05-26.md)).
- 2026-06-24: Ryan Blue starts the vote to adopt the expressions spec, pull request #16652 ([thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-262571.md), [dev list](https://lists.apache.org/thread/6wfmjhgthlykwbk3f7df4zgcm40xtm2o); further votes in [thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-2932df.md), [dev list](https://lists.apache.org/thread/tnfzjdyjlgvqhzvmwvn80qx7n107mm4m)).
- 2026-06-30: Ryan Blue announces that the vote passes with 30 +1 votes, 13 binding, and no -1 or +0 ([thread summary](../records/threads/2026/06/vote-adopt-the-expressions-spec-8ba587.md), [dev list](https://lists.apache.org/thread/7wmhcjwv8opxh4hgj284w5yl578rnbjz)).
- 2026-07-07: Read restrictions sync: mirror the adopted spec into #13879 and add IDReference before that pull request goes to a vote ([read restrictions sync 2026-07-07](../records/meetings/read-restrictions/2026/2026-07-07.md)).
- 2026-07-15: The expressions spec appears among merged Java changes in the community sync highlights ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)).
- 2026-07-21: The expression REST spec pull request #17138 is reported ready for a vote ([read restrictions sync 2026-07-21](../records/meetings/read-restrictions/2026/2026-07-21.md)).
- 2026-07-24: Prashant Singh calls the vote on aligning REST OpenAPI expressions with the spec ([thread summary](../records/threads/2026/07/vote-align-rest-openapi-expressions-with-the-iceberg-expression-specif-8d54c4.md), [dev list](https://lists.apache.org/thread/njo5bzgf4m126ly74ydz1pfznhz70h38)).
- 2026-07-27: The vote on the REST alignment passes with 4 binding and 10 non-binding +1 votes ([result message](https://lists.apache.org/thread/9ncgm04vd20lds0c3q99smvotjpxzjt8)); the pull request is merged the same day ([#17138](https://github.com/apache/iceberg/pull/17138)).
- 2026-08-05: The REST alignment appears among merged changes in the community sync highlights ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)).
- 2026-08-17: Index sync decides to define index_keys as a list of Iceberg expressions without restricting functions ([index sync 2026-08-17](../records/meetings/index/2026/2026-08-17.md)); the earlier question of enum versus expression for transform functions was raised on 2026-08-03 ([index sync 2026-08-03](../records/meetings/index/2026/2026-08-03.md)).
- 2026-08-31 and 2026-09-14: Index sync discusses materialized and non-materialized (id, expression) index fields; no agreement recorded ([index sync 2026-08-31](../records/meetings/index/2026/2026-08-31.md), [index sync 2026-09-14](../records/meetings/index/2026/2026-09-14.md)).
- 2026-10-28: Derived columns RFC presented; default value expressions said to wait on expression spec primitives ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- 2026-11-02: Vote on default value expressions for V4 opens ([thread summary](../records/threads/2026/11/vote-default-value-expressions-for-v4-33958b.md), [dev list](https://lists.apache.org/thread/th30oq0rcvn5gmn2qdx790k8vf4fz1ob)).
- 2026-11-06: The vote on default value expressions passes with 11 binding and 7 non-binding +1 votes ([result message](https://lists.apache.org/thread/h5jnk7l2op325x545hfnrpbo3qmh2ovo)); the pull request is merged the same day ([#16777](https://github.com/apache/iceberg/pull/16777)).
<!-- kb:generated:end -->

## Notes
