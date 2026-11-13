---
id: initiative/iceberg-rust
type: initiative
title: Iceberg Rust
status: implementing
updated: '2026-11-13'
sources:
- thread/t-2155678929401961
- thread/t-f324967b2d45dc23
- thread/t-60b37c70a0f57b2a
- thread/t-85a04b03334ef096
- thread/t-09a6303d5e1af395
- meeting/community/2026-09-16
- meeting/community/2026-08-05
- meeting/community/2026-08-26
- meeting/community/2026-10-28
- thread/t-cf8ecdd2fd7d10db
- thread/t-af6ebed2f3531bd4
- meeting/community/2026-05-13
- thread/t-9f4560b42e64c533
- thread/t-13fce5373af3fa44
- thread/t-dea37ea5d432effa
- thread/t-702d44e21d229af8
- thread/t-444dbbca629c1693
- thread/t-cbbca521b592906a
- thread/t-449e67b8e640cd82
- thread/t-6293c79628424192
- meeting/read-restrictions/2026-09-15
- meeting/variant/2026-08-06
links:
- rel: championed_by
  to: person/dannycjones
  source: thread/t-60b37c70a0f57b2a
  confidence: extracted
- rel: championed_by
  to: person/CTTY
  source: thread/t-cbbca521b592906a
  confidence: extracted
- rel: championed_by
  to: person/liurenjie1024
  source: thread/t-449e67b8e640cd82
  confidence: extracted
- rel: championed_by
  to: person/mbutrovich
  source: thread/t-f324967b2d45dc23
  confidence: extracted
- rel: handled_by
  to: group/rust
  confidence: inferred
  source: thread/t-cf8ecdd2fd7d10db
---

# Iceberg Rust

<!-- kb:generated:start -->
## What it is

Apache Iceberg Rust (apache/iceberg-rust) is the Rust implementation of the Iceberg table format. It also ships pyiceberg-core, the Python bindings released together with it ([thread summary](../records/threads/2026/09/discuss-pyiceberg-core-iceberg-rust-python-bindings-appears-not-to-inc-215567.md), [dev list](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4)). Projects such as DataFusion Comet build on it ([thread summary](../records/threads/2026/08/discuss-iceberg-rust-moving-the-datafusion-integration-into-a-separate-f32496.md), [dev list](https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9)).

## Current state

- Latest release: 0.11.0 ([release page](../releases/iceberg-rust-0.11.0.md)). The release manager stated that the RC3 vote passed and pointed to a separate result thread; the vote thread gives no counts ([thread summary](../records/threads/2026/10/vote-release-apache-iceberg-rust-0-11-0-rc3-60b37c.md), [dev list](https://lists.apache.org/thread/x1mlyjg7xlmkc9hqb1w8x8r97ovb1smq)).
- The DataFusion integration is moving out: the Iceberg-side vote to move iceberg-datafusion to apache/datafusion-iceberg under Apache DataFusion passed with 17 +1 votes, 5 binding ([thread summary](../records/threads/2026/09/vote-move-iceberg-datafusion-to-apache-datafusion-85a04b.md), [dev list](https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s)), and both communities' votes were reported as passed ([thread summary](../records/threads/2026/09/discuss-iceberg-rust-moving-the-datafusion-integration-into-a-separate-09a630.md), [dev list](https://lists.apache.org/thread/kyqh5z72qfjknljhm6c5px9ymlrhdycp)).
- pyiceberg-core wheels now ship NOTICE and LICENSE files with all dependencies' notices and licenses appended ([thread summary](../records/threads/2026/09/discuss-pyiceberg-core-iceberg-rust-python-bindings-appears-not-to-inc-215567.md), [dev list](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4)).
- Features added during 2026 include deletion vector read, write and validation support and a PositionDeleteFileWriter ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)), variant support ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)), encryption key management and encrypted IO, and an AuthManager with OAuth2 ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md)).
- Recent work listed on 2026-10-28: freshness-aware table loading, an Avro upgrade that makes manifest reading several times faster, and a limit of three open non-draft pull requests for users without write access ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Reviewer bandwidth was raised as a bottleneck in May, with no change decided ([thread summary](../records/threads/2026/05/discuss-reviewer-bandwidth-in-iceberg-rust-cf8ecd.md), [dev list](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r)).
- Row-delta commits and multi-table transactions exist as draft pull requests ([apache/iceberg-rust#2785](https://github.com/apache/iceberg-rust/pull/2785), [apache/iceberg-rust#2786](https://github.com/apache/iceberg-rust/pull/2786)) that received design feedback; no decision on merging is recorded ([thread summary](../records/threads/2026/07/discuss-row-delta-commits-and-multi-table-transactions-in-iceberg-rust-af6ebe.md), [dev list](https://lists.apache.org/thread/7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0)).

## Timeline

- 2026-05-13: Rust 0.9.1 is out; highlights include an EncryptionManager with envelope encryption and per-scan I/O metrics ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md)).
- 2026-05-28: Thread on reviewer bandwidth in iceberg-rust ([thread summary](../records/threads/2026/05/discuss-reviewer-bandwidth-in-iceberg-rust-cf8ecd.md), [dev list](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r)).
- 2026-06-25: 0.10.0 RC1 vote; the release manager votes -1 on his own candidate over a regression ([thread summary](../records/threads/2026/06/vote-release-apache-iceberg-rust-0-10-0-rc1-9f4560.md), [dev list](https://lists.apache.org/thread/yk7o9v6f44tym72rmr5qpz9dzxbwh870)).
- 2026-07-01: 0.10.0 RC2 abandoned after the source tarball was found not to match the signed tag ([thread summary](../records/threads/2026/07/vote-release-apache-iceberg-rust-0-10-0-rc2-13fce5.md), [dev list](https://lists.apache.org/thread/m35vm2j7z9pdv2o3jtyvd5vls0bko0xj)).
- 2026-07-08: 0.10.0 RC3 vote. On 2026-07-14 a result message announces that it passed with 3 binding and 6 non-binding +1 votes ([result message](https://lists.apache.org/thread/fymfyn86yr1zzhlc3l1fb3j27o5v5t75)); later the same day Kevin Liu changes his vote to -1 because three crates lack LICENSE and NOTICE files and asks for a new candidate ([thread summary](../records/threads/2026/07/vote-release-apache-iceberg-rust-0-10-0-rc3-dea37e.md), [dev list](https://lists.apache.org/thread/h8ohxh44g1zc32clg3sgxr80xjc4nnr9)). Design thread on row-delta commits and multi-table transactions ([thread summary](../records/threads/2026/07/discuss-row-delta-commits-and-multi-table-transactions-in-iceberg-rust-af6ebe.md), [dev list](https://lists.apache.org/thread/7d4mzx3ft3b0x1kb5g1jk91wkxnm0qf0)).
- 2026-07-15: 0.10.0 RC4 vote called; on 2026-07-20 Danny Jones states that it passes ([thread summary](../records/threads/2026/07/vote-release-apache-iceberg-rust-0-10-0-rc4-702d44.md), [dev list](https://lists.apache.org/thread/221q2qconm1zyxtor0fs86yt3st0xmo6); [release page](../releases/iceberg-rust-0.10.0.md)).
- 2026-07-27: pyiceberg-core 0.10.0 artifacts were built from the wrong branch and yanked; a no-change 0.10.1 is planned ([thread summary](../records/threads/2026/07/discussion-iceberg-rust-pyiceberg-core-0-10-1-444dbb.md), [dev list](https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l)).
- 2026-07-28: 0.10.1 RC1 vote called ([thread summary](../records/threads/2026/07/vote-release-apache-iceberg-rust-0-10-1-rc1-cbbca5.md), [dev list](https://lists.apache.org/thread/mgtkn0oprblt1tg7m0h3k1jo3lln6mc2)).
- 2026-08-01: The 0.10.1 RC1 vote passes with 3 binding and 6 non-binding +1 votes and no +0 or -1 votes ([result message](https://lists.apache.org/thread/bg80qn7v5v13s7tqxps9w6kwg4mdt91v)).
- 2026-08-05: Rust 0.10.0 and 0.10.1 reported as released ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md); [release page](../releases/iceberg-rust-0.10.1.md)).
- 2026-08-21: Matt Butrovich opens the discussion on moving the DataFusion integration to a separate repository ([thread summary](../records/threads/2026/08/discuss-iceberg-rust-moving-the-datafusion-integration-into-a-separate-f32496.md), [dev list](https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9)); respondents later favour DataFusion governance within the ASF ([thread summary](../records/threads/2026/08/discuss-iceberg-rust-moving-the-datafusion-integration-into-a-separate-449e67.md), [dev list](https://lists.apache.org/thread/k3rqkf2k7zcxh9ggboblymynkzf3m61c)).
- 2026-09-09: 0.11.0 RC1 abandoned over a circular crate dependency that blocks publishing ([thread summary](../records/threads/2026/09/vote-release-apache-iceberg-rust-0-11-0-rc1-6293c7.md), [dev list](https://lists.apache.org/thread/nj95255r4ofqszpfx6pd8hbf8yxxydzv)). Vote to move iceberg-datafusion to Apache DataFusion called on the Iceberg dev list; it passes ([thread summary](../records/threads/2026/09/vote-move-iceberg-datafusion-to-apache-datafusion-85a04b.md), [dev list](https://lists.apache.org/thread/ytb9x7x8ff3b7031kcrc05nzjtmh091s)).
- 2026-09-16: Both votes on the move reported as passed ([thread summary](../records/threads/2026/09/discuss-iceberg-rust-moving-the-datafusion-integration-into-a-separate-09a630.md), [dev list](https://lists.apache.org/thread/kyqh5z72qfjknljhm6c5px9ymlrhdycp)). Danny Jones reports missing third-party notices in pyiceberg-core wheels ([thread summary](../records/threads/2026/09/discuss-pyiceberg-core-iceberg-rust-python-bindings-appears-not-to-inc-215567.md), [dev list](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4)). Rust 0.11 RC2 listed with a vote thread ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).
- 2026-10-29: Wheel licensing fix reported ([thread summary](../records/threads/2026/09/discuss-pyiceberg-core-iceberg-rust-python-bindings-appears-not-to-inc-215567.md), [dev list](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4)); 0.11.0 RC3 vote called and later stated as passed ([thread summary](../records/threads/2026/10/vote-release-apache-iceberg-rust-0-11-0-rc3-60b37c.md), [dev list](https://lists.apache.org/thread/x1mlyjg7xlmkc9hqb1w8x8r97ovb1smq)).

## Where help is needed

- Read restrictions: the read restrictions sync asked for volunteers to implement them in Iceberg Rust, tracked in [apache/iceberg-rust#3361](https://github.com/apache/iceberg-rust/issues/3361) ([read restrictions sync 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md)).
- Reviews: limited review capacity was reported for iceberg-rust ([thread summary](../records/threads/2026/05/discuss-reviewer-bandwidth-in-iceberg-rust-cf8ecd.md), [dev list](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r)).
- Variant: shredded reading support for Iceberg Rust had an owner assigned at the variant sync, with the Go testing setup to be replicated ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)); check there before starting.
<!-- kb:generated:end -->

## Notes
