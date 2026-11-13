---
id: thread/t-6c49480676915b91
type: thread
title: 'Vote: add the variant type to the REST catalog spec'
date: '2026-07-30'
url: https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9
kind: vote
status: result-posted
messages: 24
sources:
- devlist:gkj526shb0y96hdmms73sn3tvsw8mgw9
- devlist:2plrmco4k7vvb1jd8ythvjvko6nk6q9w
refs:
- gh:apache/iceberg#17256
- list:ycvrcb60m5y3hmjw2rfhkmxlcwkqnnnj
links:
- rel: discussed
  to: initiative/variant
  confidence: extracted
  source: devlist:gkj526shb0y96hdmms73sn3tvsw8mgw9
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:gkj526shb0y96hdmms73sn3tvsw8mgw9
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Vote: add the variant type to the REST catalog spec

<!-- kb:generated:start -->
**Thread:** [[VOTE][REST-SPEC] Add variant type to the REST catalog spec](https://lists.apache.org/thread/gkj526shb0y96hdmms73sn3tvsw8mgw9) · **Started:** 2026-07-30 by [[person/nssalian|Neelesh Salian]] · **Messages:** 24 (last 2026-08-02) · **Outcome:** result-posted

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Neelesh Salian called a 72-hour vote on adding the variant type to the REST catalog OpenAPI spec (PR #17256), so that variant columns can be represented in table schemas exchanged over REST. The thread consists of +1 votes with no objections. Russell Spitzer, voting binding, said this is what the Java, Rust, Go and C++ implementations already ship. Okumin, non-binding, thanked the author for including REST compatibility kit updates as a follow-up task and said the Apache Hive community relies on the kit to develop its Iceberg REST API. On August 2nd Neelesh said the voting has concluded and that a result email would follow; the result itself is not stated in this thread.

**Why it matters:** Once adopted, REST catalogs and clients have a specified way to exchange schemas that contain variant columns.

## Outcome

Voting concluded on 2026-08-02, but the result is announced in a separate email, not here. The replies show seven +1 votes marked binding, fourteen marked non-binding and one unmarked, with no +0 or -1.

**Result posted in a separate thread on 2026-08-02:** [[VOTE][RESULT] Add variant type to the REST catalog spec](https://lists.apache.org/thread/2plrmco4k7vvb1jd8ythvjvko6nk6q9w) (`devlist:2plrmco4k7vvb1jd8ythvjvko6nk6q9w`). Outcome read from that message: result-posted.

## Positions

- **[[person/RussellSpitzer|Russell Spitzer]]:** +1 binding; the change matches what the Java, Rust, Go and C++ implementations already ship. ([message](https://lists.apache.org/thread/4y2g4yysml95ctklmf70pymr9yf5gh5c))
- **okumin:** +1 non-binding; welcomes the compatibility kit updates as a follow-up, since Apache Hive uses the kit for its Iceberg REST API. ([message](https://lists.apache.org/thread/gdnconfhokobc6mpc01pok71tw13cx0f))

References: [iceberg#17256](https://github.com/apache/iceberg/issues/17256), [thread](https://lists.apache.org/thread/ycvrcb60m5y3hmjw2rfhkmxlcwkqnnnj)
<!-- kb:generated:end -->

## Notes
