---
id: thread/t-ef8a98c0e0dd42ed
type: thread
title: Vote to recommend a standard User-Agent format for REST clients (reopened)
date: '2026-10-02'
url: https://lists.apache.org/thread/bzs62qqt9k4t9sr76pk0d36l47zwcpyb
kind: vote
status: passed
messages: 20
sources:
- devlist:bzs62qqt9k4t9sr76pk0d36l47zwcpyb
- devlist:pllz983cvffryzcwskglsr0cyo7p0gxx
refs:
- gh:apache/iceberg#17727
- list:d6hkx66o8qc1lolh11l1lmswxlq0bpj9
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:bzs62qqt9k4t9sr76pk0d36l47zwcpyb
updated: '2026-11-13'
---

# Vote to recommend a standard User-Agent format for REST clients (reopened)

<!-- kb:generated:start -->
**Thread:** [[VOTE] Recommend a standard User-Agent format for REST clients [REOPEN]](https://lists.apache.org/thread/bzs62qqt9k4t9sr76pk0d36l47zwcpyb) · **Started:** 2026-10-02 by rahul mahadev · **Messages:** 20 (last 2026-10-08) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Rahul Mahadev reopened the vote on standardizing the client User-Agent format in the REST catalog spec after incorporating review comments from Alex Dutra. A +1 endorses that clients identify themselves with the standard HTTP User-Agent header as whitespace-separated product/version tokens, most specific first (engine, integration or connector, Iceberg library, runtime), with an optional parenthesized comment; that the Iceberg library token must be present when the header is sent; and that the header is advisory, so servers must not reject requests because it is missing or malformed and must not use it for authentication, though they may refuse operations from client versions known to be unsafe. It is not a capability negotiation mechanism. The spec change is PR #17727, with follow-ups to make the Java, Python, Rust and Go clients emit the format. All replies were +1. Zheng Hu (openinx) left comments on the PR and asked whether CVE scanning failures there are blocking. The bundle contains no message announcing the result.

**Why it matters:** If adopted, the Java, Python, Rust and Go clients are to be changed to emit the common User-Agent format.

## Outcome

No result message is in the thread. Votes cast: 9 binding +1, 9 non-binding +1, one +1 with no binding status stated, and no 0 or -1 votes.

**Result posted in a separate thread on 2026-10-09:** [[RESULT][VOTE] Recommend a standard User-Agent format for REST clients](https://lists.apache.org/thread/pllz983cvffryzcwskglsr0cyo7p0gxx) (`devlist:pllz983cvffryzcwskglsr0cyo7p0gxx`). Outcome read from that message: passed.

## Positions

- **rahul mahadev:** The REST spec should recommend an advisory User-Agent format of product/version tokens that always includes the Iceberg library token. ([message](https://lists.apache.org/thread/bzs62qqt9k4t9sr76pk0d36l47zwcpyb))
- **[[person/openinx|Zheng Hu]]:** Votes +1 (binding), with comments left on the PR and a question on whether its CVE scanning failures block it. ([message](https://lists.apache.org/thread/r1hv5ybpbbwg9n7tno3prnlm73nnfn5p))

References: [iceberg#17727](https://github.com/apache/iceberg/issues/17727), [thread](https://lists.apache.org/thread/d6hkx66o8qc1lolh11l1lmswxlq0bpj9)
<!-- kb:generated:end -->

## Notes
