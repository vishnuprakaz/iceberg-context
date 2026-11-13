---
id: initiative/iceberg-cpp
type: initiative
title: Iceberg C++
status: implementing
updated: '2026-11-13'
sources:
- thread/t-cbe85b13658ba33b
- thread/t-dc8bbfb604d6e4b4
- meeting/community/2026-10-07
- thread/t-1579f8b73b2494e8
- meeting/community/2026-10-28
- thread/t-ceb017adb8f59712
- meeting/community/2026-05-13
- thread/t-c8eead2c8a5ef24b
- thread/t-418bd34af8479e56
- thread/t-e1938ca21167e827
- thread/t-7347c79968e5d24f
- meeting/community/2026-06-24
- meeting/community/2026-07-15
- meeting/community/2026-08-05
- meeting/community/2026-08-26
- meeting/variant/2026-08-06
links:
- rel: championed_by
  to: person/zhjwpku
  source: thread/t-7347c79968e5d24f
  confidence: extracted
- rel: championed_by
  to: person/manuzhang
  source: thread/t-dc8bbfb604d6e4b4
  confidence: extracted
- rel: championed_by
  to: person/wgtmac
  source: thread/t-ceb017adb8f59712
  confidence: extracted
---

# Iceberg C++

<!-- kb:generated:start -->
## What it is

Apache Iceberg C++ (apache/iceberg-cpp) is the C++ implementation of the Iceberg table format. During 2026 it added REST catalog authentication, snapshot management, scans, data and delete file writers, and then Iceberg v3 features such as deletion vectors, row lineage and column default values ([thread summary](../records/threads/2026/05/discuss-c-release-apache-iceberg-c-0-3-0-cbe85b.md), [dev list](https://lists.apache.org/thread/3vdtx3m4xbcw5htj246yhjt6wrc5rjo8), [thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)).

## Current state

- Latest release: 0.4.0 ([release page](../releases/iceberg-cpp-0.4.0.md)). The 2026-10-07 community sync notes link its release blog post ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)). The RC0 vote ([thread summary](../records/threads/2026/09/vote-release-apache-iceberg-c-0-4-0-rc0-1579f8.md), [dev list](https://lists.apache.org/thread/qqrg1l5qntf2m8h11gvopyvojrffgbw3)) passed with eight +1 votes, three of them binding, and no 0 or -1 votes ([result message](https://lists.apache.org/thread/99vvhs027n70r95qqfbnqobjs8fktb1s)).
- 0.4.0 covers v3 types, column default values, deletion vectors and row lineage, MergeAppend and RowDelta, parallel manifest reads and writes, REST SigV4 and OAuth2 token exchange, an initial Hive Metastore client, and removal of Meson build support ([thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)).
- Deferred from 0.4.0: variant types, encryption and Puffin statistics; the Arrow C++ variant pull request was expected to take a while ([thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)).
- Release cadence: the 0.4.0 release manager preferred faster, smaller releases, with another one in late October to include CherryPickOperation and RewriteManifests ([thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)). No record of that release exists yet.
- Recent work listed on 2026-10-28: scan plan endpoint, encryption and a bitmap validation fix ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- GitHub Copilot code review is being trialled on iceberg-cpp, because reviewer bandwidth is limited there ([thread summary](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).

## Timeline

- 2026-05-13: Highlights: delete filter for merge-on-read batches, streaming FileIO, a separate iceberg_data library, ReachableFileCleanup and commit retry ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md)).
- 2026-05-26: Junwang Zhao proposes releasing 0.3.0; the release waits for overwrite support, which merges by 2026-06-03 ([thread summary](../records/threads/2026/05/discuss-c-release-apache-iceberg-c-0-3-0-cbe85b.md), [dev list](https://lists.apache.org/thread/3vdtx3m4xbcw5htj246yhjt6wrc5rjo8)).
- 2026-06-06: 0.3.0 RC0 vote aborted over a -SNAPSHOT version string and a verification issue ([thread summary](../records/threads/2026/06/vote-c-release-apache-iceberg-c-0-3-0-rc0-c8eead.md), [dev list](https://lists.apache.org/thread/vo8wfvp4cncggng31c5l6ksh7nnv1bsm)).
- 2026-06-09: 0.3.0 RC1 aborted because version.h was not installed ([thread summary](../records/threads/2026/06/vote-c-release-apache-iceberg-c-0-3-0-rc1-418bd3.md), [dev list](https://lists.apache.org/thread/fkvc8wmzokym5hmtv8gb3w6b9k8fgbp9)); RC2 aborted over how the cpr dependency is resolved ([thread summary](../records/threads/2026/06/vote-c-release-apache-iceberg-c-0-3-0-rc2-e1938c.md), [dev list](https://lists.apache.org/thread/x5y5h0yk8vwzgm7r5b78o0tmp442hyky)).
- 2026-06-10: 0.3.0 RC3 vote called; it passes with 3 binding and 10 non-binding +1 votes ([thread summary](../records/threads/2026/06/vote-c-release-apache-iceberg-c-0-3-0-rc3-7347c7.md), [dev list](https://lists.apache.org/thread/8b145f8kw1mwy0ggn9jyfj6khbkb70l3); [release page](../releases/iceberg-cpp-0.3.0.md)).
- 2026-06-24: C++ 0.3.0 reported as out; highlights include view support, v3 type definitions, REST scan plan endpoints, merge append and row delta updates ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md)).
- 2026-07-15: Highlights: deletion-vector-v1 blobs in Puffin, vended storage credentials, v3 column default values ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)).
- 2026-07-16: Gang Wu proposes enabling ASF-managed Copilot code review, starting with iceberg-cpp; no objections, and he says he will merge [apache/iceberg-cpp#833](https://github.com/apache/iceberg-cpp/pull/833) ([thread summary](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).
- 2026-08-05: Highlights: merging of deletion vectors, row lineage support, metrics ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)).
- 2026-08-26: Highlights: v3 geometry and geography support, ResolvingFileIO ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md)).
- 2026-09-18: Manu Zhang proposes the 0.4.0 release and volunteers as release manager; tracking issue [apache/iceberg-cpp#955](https://github.com/apache/iceberg-cpp/issues/955) ([thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)).
- 2026-09-22: 0.4.0 RC0 vote called ([thread summary](../records/threads/2026/09/vote-release-apache-iceberg-c-0-4-0-rc0-1579f8.md), [dev list](https://lists.apache.org/thread/qqrg1l5qntf2m8h11gvopyvojrffgbw3)).
- 2026-09-26: The 0.4.0 RC0 vote passes with eight +1 votes, three of them binding, and no 0 or -1 votes ([result message](https://lists.apache.org/thread/99vvhs027n70r95qqfbnqobjs8fktb1s)).
- 2026-10-07: Release blog post for C++ 0.4.0 linked in the community sync notes ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- 2026-10-28: Highlights: scan plan endpoint, encryption, bitmap validation fix ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Where help is needed

- Reviews: limited reviewer bandwidth in iceberg-cpp was the stated reason for the Copilot review trial ([thread summary](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).
- Variant: the variant sync wants consistent variant behaviour across implementations, with the nearly complete Go implementation as the reference for the Rust and C++ ports ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)); variant types were deferred from 0.4.0 ([thread summary](../records/threads/2026/09/discuss-iceberg-cpp-0-4-0-release-dc8bbf.md), [dev list](https://lists.apache.org/thread/yfjj2p96w4s0fd7067fkr5dgknwp62d1)).
<!-- kb:generated:end -->

## Notes
