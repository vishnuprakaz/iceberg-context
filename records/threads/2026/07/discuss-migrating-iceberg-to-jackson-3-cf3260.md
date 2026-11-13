---
id: thread/t-cf32601a8df15f27
type: thread
title: Migrating Iceberg to Jackson 3
date: '2026-07-16'
url: https://lists.apache.org/thread/r3pfnttb56ml60h1l8jd5okqd2qdomv1
kind: discuss
status: consensus
messages: 8
sources:
- devlist:r3pfnttb56ml60h1l8jd5okqd2qdomv1
refs: []
links:
- rel: started_by
  to: person/adutra
  confidence: observed
updated: '2026-11-13'
---

# Migrating Iceberg to Jackson 3

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Migrating Iceberg to Jackson 3](https://lists.apache.org/thread/r3pfnttb56ml60h1l8jd5okqd2qdomv1) · **Started:** 2026-07-16 by [[person/adutra|Alexandre Dutra]] · **Messages:** 8 (last 2026-11-09) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alex Dutra opened a discussion on moving Iceberg from Jackson 2 to Jackson 3. The main difficulty is iceberg-core, where Jackson types appear in the public API of the parser classes, JsonUtil and the REST HTTP layer; he first suggested Jackson 3 overloads with both versions coexisting. Steve Loughran argued against putting Jackson 3 in signatures and proposed an indirection layer that hides the JSON binding, deprecating the Jackson 2 APIs or moving them to a legacy module. In November Alex adopted that direction: Iceberg-owned shim types, compatibility tests and both Jackson versions shipped during a transition. JB Onofré agreed and proposed doing the shims first while still on Jackson 2, deprecating Jackson-typed APIs in 1.13, running existing parser tests against both backends, and providing thin adapter artifacts with a Jackson module for REST servers. Alex and JB agreed on this phasing, starting with one PR that adds the shim types and migrates one parser package.

**Why it matters:** Downstream users of iceberg-core's Jackson-typed APIs, including REST catalog servers, should expect those APIs to be deprecated in favour of Iceberg-owned types.

## Outcome

Alex Dutra and JB Onofré agreed on a phased plan: shim types and API deprecation first on Jackson 2, then adapter artifacts for the REST layer, dual-backend tests, the switch to Jackson 3, and later removal of Jackson 2. The first step proposed is one PR with the shim types and one migrated parser package; no PR is referenced yet. ([message](https://lists.apache.org/thread/983qkhmh08q2n6bcl9kypxblf3chh0dv), `devlist:983qkhmh08q2n6bcl9kypxblf3chh0dv`)

## Positions

- **[[person/adutra|Alexandre Dutra]]:** Reduce Jackson 2 exposure first by making parser classes and JsonUtil package-private or deprecated, and keep overloads or an indirection only for the ObjectMapper extension points. ([message](https://lists.apache.org/thread/7jon4mpgt2wzdr08mh0sxrk8zz1s0w0j))
- **[[person/steveloughran|Steve Loughran]]:** Do not expose Jackson 3 in public signatures; add an API that hides the JSON binding, deprecate the Jackson 2 APIs with a clear removal plan, and move to Jackson 3 internally. ([message](https://lists.apache.org/thread/y2jpnyy6n5tg3796o7kggb2bnd0n64kp))
- **Alex Dutra:** Introduce Iceberg-owned shims over Jackson types in the serde and REST layers and ship both Jackson versions during a transition period. ([message](https://lists.apache.org/thread/vj3x5knqb1h71j2sgpsbgbbsdb1kz7b6))
- **Jean-Baptiste Onofré:** Introduce the shims first as a pure refactor on Jackson 2, and keep core binding agnostic with separate thin Jackson 2 and Jackson 3 adapter artifacts because REST servers need a Jackson module for their own mapper. ([message](https://lists.apache.org/thread/9xs8bq8q6f3xobxcp1bqvchxj9nsn3f0))
<!-- kb:generated:end -->

## Notes
