---
id: thread/t-59cdd1fc4c8fabde
type: thread
title: Shared conformance fixtures for Apache Iceberg implementations
date: '2026-07-14'
url: https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj
kind: discuss
status: open
messages: 4
sources:
- devlist:8wsvnhktw27h0tqnxljzmnsogwd52tjj
refs:
- doc:1Qr82hccxJhWxKRT7B-3ylhOLSaJTYfc7hU51-mhzK6Y
- list:964630c6q0jovs579x1jzb1t0o19jgjg
- list:87cvl9gk0cjk1of7jh3nvm4lzvzxnc8m
- gh:apache/iceberg-go#1238
- gh:sungwy/iceberg-python#1
- gh:sungwy/iceberg-rust#2
links:
- rel: discussed
  to: initiative/conformance-testing
  confidence: extracted
  source: devlist:8wsvnhktw27h0tqnxljzmnsogwd52tjj
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Shared conformance fixtures for Apache Iceberg implementations

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Shared conformance fixtures for Apache Iceberg implementations](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj) · **Started:** 2026-07-14 by [[person/nssalian|Neelesh Salian]] · **Messages:** 4 (last 2026-08-13) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Neelesh Salian, Sung Yun and Andrei Tserakhau merged two earlier threads into one proposal: a standalone, language-neutral repository of conformance fixtures modelled on parquet-testing, starting with static inputs paired with the value the spec fixes (type strings, transforms) and growing to binary fixtures. There is no harness or central gate; each implementation pins the repository and asserts in its own test suite, with Java and Go first, covering v2 and v3. Proofs of concept exist for PyIceberg, iceberg-rust and iceberg-go. After a community sync, open items were the repository name and verifying both reads and writes. Andrei supported the read-first corpus, favoured the name iceberg-verification, and argued that write verification matters because many divergences are write bugs; he described an engine-free prototype that runs a logical operation log through each implementation and compares a canonical form, with a demo matrix over Go, Rust and Java. A dedicated sync was scheduled for August 19th 2026.

**Why it matters:** If adopted, every Iceberg implementation would test its reading of the spec against the same fixtures instead of only against itself.

## Outcome

The proposal is still under review; repository naming and read-versus-write verification were raised at the community sync, and a dedicated sync was set for 2026-08-19.

## Positions

- **[[person/nssalian|Neelesh Salian]]:** Create a shared, language-neutral fixtures repository with no harness or central gate, starting from the smallest primitives and with Java and Go first. ([message](https://lists.apache.org/thread/8wsvnhktw27h0tqnxljzmnsogwd52tjj))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Supports the read-first corpus and the name iceberg-verification, and argues write verification through an engine-agnostic operation log should follow because many cross-implementation bugs are in what writers produce. ([message](https://lists.apache.org/thread/jnzyx2wp43vl74ctmk01zp7640xml6bn))

References: [doc](https://docs.google.com/document/d/1Qr82hccxJhWxKRT7B-3ylhOLSaJTYfc7hU51-mhzK6Y), [thread](https://lists.apache.org/thread/964630c6q0jovs579x1jzb1t0o19jgjg), [thread](https://lists.apache.org/thread/87cvl9gk0cjk1of7jh3nvm4lzvzxnc8m), [iceberg-go#1238](https://github.com/apache/iceberg-go/issues/1238), [iceberg-python#1](https://github.com/sungwy/iceberg-python/issues/1), [iceberg-rust#2](https://github.com/sungwy/iceberg-rust/issues/2)
<!-- kb:generated:end -->

## Notes
