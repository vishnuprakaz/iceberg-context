---
id: thread/t-64d9cbfda2cf0c40
type: thread
title: Recommend a standard User-Agent format for REST clients
date: '2026-09-02'
url: https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9
kind: discuss
status: consensus
messages: 9
sources:
- devlist:d6hkx66o8qc1lolh11l1lmswxlq0bpj9
refs:
- gh:apache/iceberg#17727
- gh:apache/polaris#4236
links: []
updated: '2026-11-13'
---

# Recommend a standard User-Agent format for REST clients

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Recommend a standard User-Agent format for REST clients](https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9) · **Started:** 2026-09-02 by rahul mahadev · **Messages:** 9 (last 2026-09-10) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rahul mahadev proposed a recommended User-Agent format for REST catalog clients. Today iceberg-java sends no User-Agent by default, PyIceberg, iceberg-rust and iceberg-go each use different names, X-Client-Version carries the library version in Java and Python but the REST spec version in Rust and Go, and none of it is in the spec. The proposal uses the standard header with whitespace-separated product/version tokens ordered from engine to integration to Iceberg library to runtime, plus an optional comment; the Iceberg library token is always present. The header is optional and informational: servers must not reject on it or use it for auth, trust or capability negotiation. A draft spec PR was opened, with client library changes to follow. Open questions covered reconciling X-Client-Version, library naming, and an environment token. Alex Dutra and flyrain cited a Polaris attempt to parse client headers as evidence standardization is needed; rdblue, danielcweeks, singhpk234, Eduard Tudenhöfner and liurenjie1024 supported the proposal.

**Why it matters:** If adopted, client libraries in Java, Python, Rust and Go would need to emit a common User-Agent format so catalog operators can identify callers.

## Outcome

Every reply supported the proposal; the thread records no vote and the open questions on X-Client-Version, naming and an environment token were not answered here.

## Positions

- **rahul mahadev:** REST clients should send a consistent, parseable User-Agent of product/version tokens that always includes the Iceberg library token and is informational only. ([message](https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9))
- **Alex Dutra:** Identifying clients in Polaris from User-Agent and X-Client-Version proved complicated and unreliable; this standardization would make it doable. ([message](https://lists.apache.org/thread/27536q0s5vtnhc5m29qlfs2s6cs4ldbn))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Has minor comments on the spec text but the proposal looks great overall. ([message](https://lists.apache.org/thread/305302fy0vqg7z5xvg30v1bco7fkgmzl))
- **[[person/flyrain|Yufei Gu]]:** Downstream projects struggle to build parsers without standardization, as the Polaris PR shows; supports the proposal. ([message](https://lists.apache.org/thread/674xgm61q4v03d6gb0jcdpjfrh420dl9))

References: [iceberg#17727](https://github.com/apache/iceberg/issues/17727), [polaris#4236](https://github.com/apache/polaris/issues/4236)
<!-- kb:generated:end -->

## Notes
