---
id: thread/t-0fe216b27de16fe7
type: thread
title: 'Vote: recommend a standard User-Agent format for REST clients'
date: '2026-09-23'
url: https://lists.apache.org/thread/79b5p9pfjso9d8tbs1w10619qz61rt85
kind: vote
status: open
messages: 5
sources:
- devlist:79b5p9pfjso9d8tbs1w10619qz61rt85
refs:
- gh:apache/iceberg#17727
- list:d6hkx66o8qc1lolh11l1lmswxlq0bpj9
links: []
updated: '2026-11-13'
---

# Vote: recommend a standard User-Agent format for REST clients

<!-- kb:generated:start -->
**Thread:** [[VOTE] Recommend a standard User-Agent format for REST clients](https://lists.apache.org/thread/79b5p9pfjso9d8tbs1w10619qz61rt85) · **Started:** 2026-09-23 by rahul mahadev · **Messages:** 5 (last 2026-09-24) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rahul mahadev called a vote on standardizing the client User-Agent format in the REST catalog spec (PR #17727), following a discussion thread. A +1 endorses that clients identify themselves with the standard HTTP User-Agent header as whitespace-separated product/version tokens, most specific first (engine, integration or connector, Iceberg library, runtime), with an optional parenthesized comment; that the Iceberg library token must be present when the header is sent; and that the header is advisory, so servers must not reject requests for a missing or malformed header or use it for authentication, though they may refuse client versions known to be unsafe. It is not a capability negotiation mechanism. Three non-binding +1 votes followed. Alex Dutra then said he had posted more comments on the PR that should be addressed before proceeding. No result is stated in the thread.

**Why it matters:** If adopted, the Java, Python, Rust and Go clients would be changed to emit the same User-Agent format.

## Outcome

No result is stated. The thread has 3 non-binding +1 votes and a request to address further PR comments before proceeding.

## Positions

- **rahul mahadev:** Adopt an advisory, RFC 7231 style User-Agent format in the REST spec that always includes the Iceberg library token. ([message](https://lists.apache.org/thread/79b5p9pfjso9d8tbs1w10619qz61rt85))
- **[[person/Xuanwo|Hao Ding]]:** Supports the advisory format, kept separate from authentication and capability negotiation and tolerant of clients that omit the header. ([message](https://lists.apache.org/thread/3ntwsfn5dkjwbkhjtdz3rxz13fmodpq5))
- **Alex Dutra:** Further comments on the PR should be addressed before the vote proceeds. ([message](https://lists.apache.org/thread/3pq21p5cxvpv7k4omrzso6jmq5chb2gz))

References: [iceberg#17727](https://github.com/apache/iceberg/issues/17727), [thread](https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9)
<!-- kb:generated:end -->

## Notes
