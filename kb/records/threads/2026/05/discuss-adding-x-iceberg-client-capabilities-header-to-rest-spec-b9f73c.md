---
id: thread/t-b9f73c21a4179dc6
type: thread
title: Adding an X-Iceberg-Client-Capabilities header to the REST spec
date: '2026-05-18'
url: https://lists.apache.org/thread/xlqx6k7g625p38bxxy141wt02d00w2h4
kind: discuss
status: open
messages: 8
sources:
- devlist:xlqx6k7g625p38bxxy141wt02d00w2h4
refs:
- gh:apache/iceberg#16394
- gh:apache/iceberg#13879
- yt:b9p6mI-k-0I
- yt:-KEesN1udyY
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:xlqx6k7g625p38bxxy141wt02d00w2h4
- rel: discussed
  to: initiative/read-restrictions
  confidence: extracted
  source: devlist:xlqx6k7g625p38bxxy141wt02d00w2h4
- rel: started_by
  to: person/singhpk234
  confidence: observed
updated: '2026-11-13'
---

# Adding an X-Iceberg-Client-Capabilities header to the REST spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Adding X-Iceberg-Client-Capabilities header to REST spec](https://lists.apache.org/thread/xlqx6k7g625p38bxxy141wt02d00w2h4) · **Started:** 2026-05-18 by [[person/singhpk234|Prashant Singh]] · **Messages:** 8 (last 2026-06-04) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

singhpk234 proposed a generic X-Iceberg-Client-Capabilities header (PR #16394) sent on catalog requests so that a client can declare which features it understands, such as vended-credentials, remote-signing and scan-planning, with read-restrictions to follow. The header is a forward-compatibility hint, not a security mechanism. sungwy supported it and asked whether capability values need versioning; the author replied that a fail-closed rule makes versions unnecessary. danielcweeks preferred feature-specific headers on the endpoints where they apply, and later listed concerns: capabilities depend on engine and configuration, a global header does not say which endpoints are targeted, and capabilities may proliferate. He and rdblue suggested that a versioned v2 loadTable endpoint is the existing way to introduce forward-breaking changes and should be considered instead. RussellSpitzer saw no reason a generic header must be sent on every request. The thread ends with the v2 endpoint suggestion and no decision.

**Why it matters:** The choice between a capabilities header and a v2 loadTable endpoint decides how clients opt into forward-breaking REST features such as read restrictions.

## Outcome

No agreement. The author reported that the 26 May sync leaned towards a generic header, while danielcweeks and rdblue proposed considering a v2 loadTable endpoint instead.

## Positions

- **[[person/singhpk234|Prashant Singh]]:** A single generic capabilities header with an enum of values is a static advertisement of what the client understands and is easy to extend. ([message](https://lists.apache.org/thread/y5xtx8csdjpxjpl6poqrbfbc3jz81f79))
- **[[person/sungwy|Sung Yun]]:** Supports a generic header for compatibility and response shaping, and asks whether capability values should be versioned contracts. ([message](https://lists.apache.org/thread/qq04pz07frmrg8v3110d6l32ndg2x6q2))
- **[[person/RussellSpitzer|Russell Spitzer]]:** A generic header does not require sending every capability with every request; clients could send only the relevant ones per endpoint. ([message](https://lists.apache.org/thread/gwg4tdpmrlgxsp8t41hymmdp3pon20hg))
- **[[person/danielcweeks|Daniel C. Weeks]]:** A global capabilities header adds complexity that is not narrowly targeted; a v2 loadTable endpoint should be examined instead. ([message](https://lists.apache.org/thread/1yt689xpk435ypcxm6vnr69rmh5zm3p2))
- **[[person/rdblue|Ryan Blue]]:** Versioned endpoints are the existing way to introduce forward-breaking changes, so a v2 loadTable endpoint is cleaner than either header approach. ([message](https://lists.apache.org/thread/mmb0bb8sj12tj64swv8pmm10pqgrpo3c))

References: [iceberg#16394](https://github.com/apache/iceberg/issues/16394), [iceberg#13879](https://github.com/apache/iceberg/issues/13879), [video](https://www.youtube.com/watch?v=b9p6mI-k-0I), [video](https://www.youtube.com/watch?v=-KEesN1udyY)
<!-- kb:generated:end -->

## Notes
