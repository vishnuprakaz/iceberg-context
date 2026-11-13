---
id: initiative/iceberg-go
type: initiative
title: Iceberg Go
status: released
updated: '2026-11-13'
sources:
- meeting/community/2026-05-13
- thread/t-fa69aa12d0302acd
- thread/t-26347b0fcdb11b56
- thread/t-701f75267880be54
- meeting/community/2026-06-03
- meeting/variant/2026-06-04
- meeting/community/2026-06-24
- meeting/variant/2026-07-02
- thread/t-e7c5d0287bca96b4
- meeting/community/2026-07-15
- thread/t-e5e8356da0183206
- meeting/variant/2026-08-06
- thread/t-51925c451e4cf72d
- meeting/community/2026-08-26
- meeting/variant/2026-09-03
- meeting/community/2026-09-16
- thread/t-f30173754f0d73b2
- thread/t-3548f77d85b2a887
- meeting/community/2026-10-07
- thread/t-a9927e0959daeebf
- meeting/community/2026-10-28
links:
- rel: championed_by
  to: person/zeroshade
  confidence: extracted
  source: thread/t-3548f77d85b2a887
---

# Iceberg Go

<!-- kb:generated:start -->
## What it is

Iceberg Go (`apache/iceberg-go`) is the Go implementation of Iceberg, released on its own schedule through votes on the dev list ([thread summary](../records/threads/2026/09/vote-go-release-apache-iceberg-go-v0-7-0-rc0-3548f7.md), [dev list](https://lists.apache.org/thread/18mcytdbd953cdwz5wsvzx6sbqzsvofh)). The same release manager also runs releases of the Apache Iceberg Terraform provider, which depends on iceberg-go ([thread summary](../records/threads/2026/08/vote-terraform-release-apache-iceberg-terraform-provider-v0-1-0-rc2-51925c.md), [dev list](https://lists.apache.org/thread/xwqz0j6g2fcvq4hf5xs63ll4137ch0n6)). This page follows its releases and the features reported in the community sync.

## Current state

- Go 0.7.0 is the latest release on record: its RC0 vote passed on 1 October with 4 binding and 3 non-binding +1 votes ([result message](https://lists.apache.org/thread/k8lo7j1xfq2kq1f0tblvz8kklc49g6tj)), and the 7 October community sync links its release blog post ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- The Terraform provider v0.2.0 RC1 vote passed with 4 binding +1 votes and the release manager said he would proceed with the release ([thread summary](../records/threads/2026/10/vote-terraform-release-apache-iceberg-terraform-provider-v0-2-0-rc1-a9927e.md), [dev list](https://lists.apache.org/thread/7qo3nydsv4fcx9z94p1gb53oqydsl5oc)).
- A v1 release is being prepared: at the 28 October community sync the API surface was reported as being cleaned up for a v1 release, and the speaker said "we plan to do this maybe before the next community sync"; no date is set ([recording at 0:15:42](https://www.youtube.com/watch?v=fPTtFTNf_Tc), `yt:fPTtFTNf_Tc`). The sync also lists encryption, geo logical types and performance work ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Variant: the reader is merged and a shredded variant writer was added ([variant sync 2026-07-02](../records/meetings/variant/2026/2026-07-02.md); [community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)); predicate pushdown was in flight in September ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)). The Go implementation is meant to be the reference for Rust and C++ variant ports ([variant sync 2026-08-06](../records/meetings/variant/2026/2026-08-06.md)).
- Features reported as added during 2026: commit retry and conflict validation, a v3 deletion vector reader ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md)); deletion vector write and validation, view support, geometry and geography encoding ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md)); files metadata tables, incremental append scan and a REST metrics reporter ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md)).

## Timeline

- 2026-05-18: Vote on Go v0.6.0 RC0; withdrawn because the candidate wrote a deprecated manifest field that PyIceberg rejects ([thread summary](../records/threads/2026/05/vote-go-release-apache-iceberg-go-v0-6-0-rc0-fa69aa.md), [dev list](https://lists.apache.org/thread/yvf1ywkwwdw3f28b7xskqt2y0hsmtv2l)).
- 2026-05-20: Thread on the Avro type of `day` partition values in manifests: consensus that the result type is date; Go wrote a plain int and will align once the spec change ([#16446](https://github.com/apache/iceberg/pull/16446)) lands ([thread summary](../records/threads/2026/05/discuss-spec-ambiguity-avro-schema-for-day-partition-transform-fields--26347b.md), [dev list](https://lists.apache.org/thread/o3oycdqw4sm1sqt54hfrj8c2hwxc0yww)).
- 2026-05-21: Vote on Go v0.6.0 RC2 opens ([thread summary](../records/threads/2026/05/vote-go-release-apache-iceberg-go-v0-6-0-rc2-701f75.md), [dev list](https://lists.apache.org/thread/sgtobp6b3w9b3t4xdzo2xfgrsz960yxv)).
- 2026-05-28: The Go v0.6.0 RC2 vote passes with 4 binding and 5 non-binding +1 votes ([result message](https://lists.apache.org/thread/vmm8ybdnwsr2f8w2jf3frnq4gv7fl8h4)).
- 2026-06-03: The community sync reports Go 0.6.0 as out ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md)); it shipped with non-shredded variant support ([variant sync 2026-06-04](../records/meetings/variant/2026/2026-06-04.md)).
- 2026-07-13: Vote on Terraform provider v0.1.0 RC0 ([thread summary](../records/threads/2026/07/vote-terraform-release-apache-iceberg-terraform-provider-v0-1-0-rc0-e7c5d0.md), [dev list](https://lists.apache.org/thread/lfr1kb253m99dg0mbdzpm6g1k3nbd6fc)).
- 2026-07-16: Terraform provider v0.1.0 RC1 withdrawn over schema validation problems (duplicate field IDs on create, invalid schema changes accepted on update) ([thread summary](../records/threads/2026/07/vote-terraform-release-apache-iceberg-terraform-provider-v0-1-0-rc1-e5e835.md), [dev list](https://lists.apache.org/thread/krophr3htb39xhxr3ldbcn7ghqm82ohj)).
- 2026-08-11: Vote on Terraform provider v0.1.0 RC2; a non-binding 0 vote points at LICENSE gaps in the binary distribution ([thread summary](../records/threads/2026/08/vote-terraform-release-apache-iceberg-terraform-provider-v0-1-0-rc2-51925c.md), [dev list](https://lists.apache.org/thread/xwqz0j6g2fcvq4hf5xs63ll4137ch0n6)).
- 2026-09-16: The community sync marks the Terraform provider v0.1.0 as done ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).
- 2026-09-28: Vote on Go v0.7.0 RC0 opens ([thread summary](../records/threads/2026/09/vote-go-release-apache-iceberg-go-v0-7-0-rc0-3548f7.md), [dev list](https://lists.apache.org/thread/18mcytdbd953cdwz5wsvzx6sbqzsvofh)).
- 2026-10-01: The Go v0.7.0 RC0 vote passes with 4 binding and 3 non-binding +1 votes and no -1 votes ([result message](https://lists.apache.org/thread/k8lo7j1xfq2kq1f0tblvz8kklc49g6tj)).
- 2026-10-07: The community sync links the Go 0.7.0 release blog post ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- 2026-10-26: Vote on Terraform provider v0.2.0 RC1; it passed ([thread summary](../records/threads/2026/10/vote-terraform-release-apache-iceberg-terraform-provider-v0-2-0-rc1-a9927e.md), [dev list](https://lists.apache.org/thread/7qo3nydsv4fcx9z94p1gb53oqydsl5oc)).
- 2026-10-28: API cleanup toward a v1 release is reported ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Where help is needed

- A Puffin test (`TestReaderPreservesLZ4ChecksumError`) fails on Go 1.27.1 while passing on 1.25.9; a fix was proposed during the 0.7.0 vote and is needed before that Go version is added to CI ([thread summary](../records/threads/2026/09/vote-go-release-apache-iceberg-go-v0-7-0-rc0-3548f7.md), [dev list](https://lists.apache.org/thread/18mcytdbd953cdwz5wsvzx6sbqzsvofh)).
- It was an open question in September whether row group skipping is part of the variant predicate pushdown work or needs a separate implementation ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md)).
- A proposal to expose catalog labels through the iceberg-go inspect API ([iceberg-go#2101](https://github.com/apache/iceberg-go/pull/2101)) ended with an unanswered objection that the API cannot tell a table without labels from a catalog that does not support them ([thread summary](../records/threads/2026/09/discuss-catalog-provided-metadata-tables-f30173.md), [dev list](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn)).
<!-- kb:generated:end -->

## Notes
