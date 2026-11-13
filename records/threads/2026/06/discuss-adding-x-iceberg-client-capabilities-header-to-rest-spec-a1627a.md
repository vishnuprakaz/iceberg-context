---
id: thread/t-a1627a890918338f
type: thread
title: Adding X-Iceberg-Client-Capabilities header to REST spec
date: '2026-06-05'
url: https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9
kind: discuss
status: consensus
messages: 12
sources:
- devlist:qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9
refs:
- gh:apache/iceberg#13879
- list:wfgqlsnpyvt1t42fg6o4q48w8nc14oof
links:
- rel: started_by
  to: person/Kurtiscwright
  confidence: observed
updated: '2026-11-13'
---

# Adding X-Iceberg-Client-Capabilities header to REST spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Adding X-Iceberg-Client-Capabilities header to REST spec](https://lists.apache.org/thread/qtjkm2xhby3x8hp0yvfj22bsvhyz6ro9) · **Started:** 2026-06-05 by [[person/Kurtiscwright|Kurtis Wright]] · **Messages:** 12 (last 2026-06-09) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread debated whether read restrictions in the REST catalog need a client capabilities header or a v2 loadTable endpoint so that catalogs know a client will honor restrictions. RussellSpitzer, Christian Thiel, flyrain and singhpk234 argued that neither a header nor an endpoint version can bind an untrusted caller, that the catalog must decide out of band which principals receive restrictions, and that read restrictions should ship in v1 with v2 pursued separately. rdblue and danielcweeks argued that requiring clients to fail on unenforced restrictions is a forward-incompatible contract change that belongs in a v2 endpoint, and opposed capability headers that alter endpoint behavior. rdblue proposed a compromise: allow read restrictions on v1 with administrators responsible for verifying enforcement, and make support mandatory on v2. After the June 9 read restrictions sync, the capabilities header was dropped in favor of that V1/V2 path and spec PR 13879 was updated.

**Why it matters:** Read restrictions proceed on the v1 loadTable endpoint without a client capabilities header, with mandatory support reserved for a future v2 endpoint.

## Outcome

After the 2026-06-09 read restrictions sync the capabilities header was dropped and the V1/V2 path was adopted; spec PR 13879 was updated with the agreed wording. ([message](https://lists.apache.org/thread/l9m8mzbfttqk0l413yfrwp2m5gzryyj6), `devlist:l9m8mzbfttqk0l413yfrwp2m5gzryyj6`)

## Positions

- **[[person/RussellSpitzer|Russell Spitzer]]:** A header is advisory at best and a v2 endpoint is redundant for this feature because neither binds an untrusted caller; ship read restrictions in v1 without the capability flag and do v2 in parallel. ([message](https://lists.apache.org/thread/zdbkr040329f34sqlgd8l2c8xkqso3s5))
- **Christian Thiel:** Coupling read restrictions to v2 forces every client that wants the v2 cleanups to handle restrictions and would slow v2 adoption; introduce them in v1. ([message](https://lists.apache.org/thread/gl7gkvh5nlbsh51bxdwfrqfltg626ttw))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Clients only need to know about the field and fail when it is present, not implement it; behavior changes should be explicit per endpoint rather than introduced as side effects. ([message](https://lists.apache.org/thread/nosnwt9yo7j8lcv5vkwzxgb79vm7hpky))
- **[[person/rdblue|Ryan Blue]]:** Putting read restrictions in v2 guarantees clients parse the field and fail on unenforced restrictions, preventing accidental violations by trusted but older clients. ([message](https://lists.apache.org/thread/vk4lhxw3nxdsd1wy5nl40hzhk641f6dj))
- **[[person/flyrain|Yufei Gu]]:** Admins must verify client support either way, so v2 does not meaningfully reduce their diligence; catalogs should return restrictions only when explicitly enabled per principal or engine. ([message](https://lists.apache.org/thread/zb3gjd16lpfwo29syvvjhn8kl6dph3dr))
- **[[person/singhpk234|Prashant Singh]]:** The header was only an informational fail-fast hint and can be dropped; read restrictions should be decoupled from v2 requirements. ([message](https://lists.apache.org/thread/flgj7d5ym9m2ds9joclb9hxbh5o8bd49))
- **[[person/rdblue|Ryan Blue]]:** Compromise: allow read restrictions on v1 with SHOULD-fail language and admin responsibility, and make support required on the v2 path. ([message](https://lists.apache.org/thread/hz4qc8hp38xqb66by37kfdvjx1mp6jyx))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Either the feature is forward compatible and needs no capabilities, or it is not and needs v2; using capabilities to augment endpoint behavior adds complexity without security. ([message](https://lists.apache.org/thread/bxbz94dzrrh5zkptp3lzssz759k70tqt))
- **[[person/Kurtiscwright|Kurtis Wright]]:** A global capabilities header should be discussed separately or dropped; agrees with MUST enforcement language for v2 as long as read restrictions proceed without waiting for v2. ([message](https://lists.apache.org/thread/5odxbj8rvrqw3y618yydcy3240447gxt))

References: [iceberg#13879](https://github.com/apache/iceberg/issues/13879), [thread](https://lists.apache.org/thread/wfgqlsnpyvt1t42fg6o4q48w8nc14oof)
<!-- kb:generated:end -->

## Notes
