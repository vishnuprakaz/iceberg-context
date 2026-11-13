---
id: thread/t-9065940068b4c4a3
type: thread
title: 'Switching S3 test backend to address issue #14638'
date: '2026-03-20'
url: https://lists.apache.org/thread/wnt4ojcjsv1frfg1drxpz3gj0l91c5jl
kind: discuss
status: consensus
messages: 9
sources:
- devlist:wnt4ojcjsv1frfg1drxpz3gj0l91c5jl
refs:
- gh:apache/iceberg#14638
- gh:apache/iceberg#15577
- gh:apache/iceberg#18071
- gh:apache/iceberg-python#3928
- gh:apache/iceberg#18246
- gh:apache/iceberg#18247
links: []
updated: '2026-11-13'
---

# Switching S3 test backend to address issue #14638

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Switching S3 test backend to address issue #14638](https://lists.apache.org/thread/wnt4ojcjsv1frfg1drxpz3gj0l91c5jl) · **Started:** 2026-03-20 by chrislusf · **Messages:** 9 (last 2026-09-25) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

In March, Chris (chrislusf), the author of SeaweedFS, proposed switching the S3 test backend from MinIO to SeaweedFS, citing its IAM and STS support for testing credential scenarios, and opened a PR. The thread was quiet until September, when Sreesh Maheshwar revived it after MinIO images were removed from Docker Hub and blocked CI across Iceberg projects; he noted that Polaris and PyIceberg had moved to RustFS. Kevin Liu supported leaving MinIO and suggested RustFS across the Iceberg repositories for consistency; Xuanwo and Szehon (szehon-ho) agreed. Neelesh Salian recalled CVE concerns about RustFS raised in another thread and asked for long-term support and prompt security fixes. After stevenzwu reported Kafka Connect integration test failures tied to MinIO, Kevin Liu said the work was done across all Iceberg repositories, referring to issue 18246.

**Why it matters:** Integration tests and quickstarts across the Iceberg repositories no longer depend on MinIO images.

## Outcome

Replies in September agreed to move away from MinIO, with RustFS preferred for consistency. Kevin Liu reported the work done across all Iceberg repositories, pointing to apache/iceberg#18246. ([message](https://lists.apache.org/thread/j1w7556o1v1gdqd8c8vo5cfmkhdl79fq), `devlist:j1w7556o1v1gdqd8c8vo5cfmkhdl79fq`)

## Positions

- **chrislusf:** Replace MinIO with SeaweedFS as the S3 test backend to improve reliability and enable testing of IAM, STS and vended-credential scenarios; multiple backends are an alternative. ([message](https://lists.apache.org/thread/wnt4ojcjsv1frfg1drxpz3gj0l91c5jl))
- **[[person/smaheshwar-pltr|Sreesh Maheshwar]]:** The removal of MinIO images from Docker Hub is another reason to move quickstarts and integration tests away from MinIO. ([message](https://lists.apache.org/thread/k5hjjtmj1z3gdwtrlf4v5ovz1wp1p14q))
- **[[person/kevinjqliu|Kevin Liu]]:** Move away from MinIO and use RustFS across the Iceberg repositories for consistency, unless something specific is needed from SeaweedFS. ([message](https://lists.apache.org/thread/gvfzk3b4g6c1b6xw0lhhc7xjfcvyvz1l))
- **[[person/Xuanwo|Hao Ding]]:** RustFS is fine; it is only for CI and easy to change later. ([message](https://lists.apache.org/thread/ght0c5ljqb90zd7n3zcqs81ot50wqd2b))
- **[[person/nssalian|Neelesh Salian]]:** Either choice is acceptable provided RustFS has long-term support and prompt security fixes, given CVE concerns raised earlier. ([message](https://lists.apache.org/thread/k4bkk3lmjr00y5k6vqqjsybonmtop4oj))

References: [iceberg#14638](https://github.com/apache/iceberg/issues/14638), [iceberg#15577](https://github.com/apache/iceberg/issues/15577), [iceberg#18071](https://github.com/apache/iceberg/issues/18071), [iceberg-python#3928](https://github.com/apache/iceberg-python/issues/3928), [iceberg#18246](https://github.com/apache/iceberg/issues/18246), [iceberg#18247](https://github.com/apache/iceberg/issues/18247)
<!-- kb:generated:end -->

## Notes
