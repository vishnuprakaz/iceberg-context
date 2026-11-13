---
id: thread/t-019f2b7ebaa9b671
type: thread
title: 'REST spec: batch remote signing endpoint'
date: '2026-10-26'
url: https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd
kind: discuss
status: open
messages: 4
sources:
- devlist:8pnj238xly2dmzb55tfb9bjny7sp34nd
refs:
- gh:apache/iceberg#18254
- gh:apache/iceberg#17918
- gh:apache/iceberg#18080
- list:4fxylxkfj0ngp0ksfysgkhn8s6o9x4n5
- list:s283f6obyqf6c14bn37sw7vtf9y1c9mj
links:
- rel: discussed
  to: initiative/rest-auth
  confidence: extracted
  source: devlist:8pnj238xly2dmzb55tfb9bjny7sp34nd
- rel: discussed
  to: initiative/file-type
  confidence: extracted
  source: devlist:8pnj238xly2dmzb55tfb9bjny7sp34nd
- rel: started_by
  to: person/sungwy
  confidence: observed
updated: '2026-11-13'
---

# REST spec: batch remote signing endpoint

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] REST Spec: Batch remote signing endpoint](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd) · **Started:** 2026-10-26 by [[person/sungwy|Sung Yun]] · **Messages:** 4 (last 2026-11-09) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Sung Yun (sungwy) proposed a batch signing endpoint for the REST catalog spec (PR #18254 and a design doc). Today a client signs one object request per signRequest call, which is bounded by files in a scan, but with the FILE type each row may reference an external object, so signatures scale with rows. Daniel Weeks wanted to wait for the FILE implementation before settling, because authorizing references to shared storage may need extra context, such as the data file holding the reference and the source column, which would change the request design. Jean-Baptiste Onofré agreed that authorization should drive the request shape: he suggested an optional, spec-defined context per batch element (data file location and field ID rather than column name), noted that the context is a client claim and not proof, and said per-element authorization justifies partial results. Sung agreed on the semantics, argued the optional context can be added later without blocking the batch API, left open whether it belongs on the element or the request, and kept the thread open.

**Why it matters:** The request shape of batch signing depends on how catalogs authorize FILE references, so the endpoint is unlikely to be voted on before the FILE implementation.

## Outcome

No decision. The thread is kept open while the FILE type implementation settles; where the authorization context lives in the request is unresolved.

## Positions

- **[[person/sungwy|Sung Yun]]:** A batch signing endpoint is needed because with the FILE type the number of signatures scales with rows rather than files. ([message](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd))
- **[[person/danielcweeks|Daniel C. Weeks]]:** The endpoint should wait for the FILE implementation, since authorizing references into shared storage may require per-request context and change the request design. ([message](https://lists.apache.org/thread/mfo1bbd6gcc7969obj7wzzbrhmsdwq38))
- **Jean-Baptiste Onofré:** Authorization context should be an optional, spec-defined field on each batch element using data file location and field ID, treated as a client claim, and a vote should wait for the FILE implementation and #18080. ([message](https://lists.apache.org/thread/9sjdz6rfk2yk0z86ksnf0jx5vc69rpnw))
- **[[person/sungwy|Sung Yun]]:** The context can be an optional later enhancement that does not block the batch API, and whether it lives on the element or the request is still open. ([message](https://lists.apache.org/thread/fhov7qwq42bn8pz0sqd0m2jzod6gxcn7))

References: [iceberg#18254](https://github.com/apache/iceberg/issues/18254), [iceberg#17918](https://github.com/apache/iceberg/issues/17918), [iceberg#18080](https://github.com/apache/iceberg/issues/18080), [thread](https://lists.apache.org/thread/4fxylxkfj0ngp0ksfysgkhn8s6o9x4n5), [thread](https://lists.apache.org/thread/s283f6obyqf6c14bn37sw7vtf9y1c9mj)
<!-- kb:generated:end -->

## Notes
