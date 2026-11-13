---
id: thread/t-98226ff1baae6ac7
type: thread
title: 'REST spec: expected server behavior when X-Iceberg-Access-Delegation cannot be satisfied'
date: '2026-09-23'
url: https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf
kind: discuss
status: consensus
messages: 20
sources:
- devlist:6zspb6cpb6j2po5lm57mq1sgcp2hppkf
refs:
- gh:apache/iceberg#18480
links: []
updated: '2026-11-13'
---

# REST spec: expected server behavior when X-Iceberg-Access-Delegation cannot be satisfied

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] REST spec: expected server behavior when X-Iceberg-Access-Delegation cannot be satisfied](https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf) · **Started:** 2026-09-23 by youngrae81 · **Messages:** 20 (last 2026-10-21) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

youngrae81 asked what a REST catalog should do when the X-Iceberg-Access-Delegation header is present but none of the requested mechanisms can be provided; Apache Polaris fails such requests with HTTP 400, and the spec text 'any or none' does not say whether rejection is allowed. Alex Dutra proposed that servers SHOULD return 400 in that case, and flyrain supported fail-fast. danielcweeks disagreed: the wording was intentionally loose, the catalog should decide the access model through storage-credentials and remote-signing-config, and Polaris's behavior is fine as an implementation choice but should not be required. Alex Dutra then suggested a new header value 'local'; danielcweeks preferred 'none', which flyrain and Dmitri Bourlatchkov accepted. A sentence explicitly permitting failure was dropped because a server may always reject a request. youngrae81 opened PR #18480 adding only 'none'. flyrain later asked again to document that servers may fail with a specific reason; youngrae81 offered a separate PR if others agree.

**Why it matters:** Clients gain an explicit way to tell a catalog they do not need delegated access, while failing on unsatisfiable delegation remains a catalog implementation choice rather than a spec requirement.

## Outcome

Agreement to add a 'none' value to the X-Iceberg-Access-Delegation enum and leave the rest of the description unchanged; PR #18480 does this. Whether to also state that servers may reject unsatisfiable requests was raised again at the end and is unresolved. ([message](https://lists.apache.org/thread/70c96rm1zo3xhmrhwb9wb68qf79t2h2g), `devlist:70c96rm1zo3xhmrhwb9wb68qf79t2h2g`)

## Positions

- **youngrae81:** The spec does not settle whether a server may reject a request when no requested delegation mechanism is available, and a clarification is needed. ([message](https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf))
- **Alex Dutra:** The spec should say servers SHOULD return HTTP 400 when none of the requested mechanisms is available, because a 200 without access only moves the failure to first data access. ([message](https://lists.apache.org/thread/vbbhm3wrbdzjn7qy3kzsz7y84wbgrd0h))
- **Alex Dutra:** The header cannot express that a client can work with its own storage credentials, so a new enum value should be added for that. ([message](https://lists.apache.org/thread/l02zjbx3j1pddqhj3wg8gkj10o90l2cp))
- **[[person/danielcweeks|Daniel C. Weeks]]:** The catalog should be the sole authority on access, the loose wording is intentional, and catalogs should not be required to fail when they cannot provide a requested mechanism. ([message](https://lists.apache.org/thread/9zthft8ozrjxn2s88k47pn7yydgdc4jo))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Use 'none' rather than 'local' so the client states it does not need credentials or access from the catalog and the catalog can skip generating them. ([message](https://lists.apache.org/thread/1sfcy4dfvmfts6xz8g27h0qj9zrq9j0n))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Only the 'none' value needs to be added; no clarification about failing is needed because a server may always reject a request. ([message](https://lists.apache.org/thread/nbtw9wg699w07wrp2xy03mjjchob6vjq))
- **[[person/flyrain|Yufei Gu]]:** Failing the request when the requested mechanism cannot be provided is acceptable and expected, and the spec should state explicitly that a server may fail for a specific reason. ([message](https://lists.apache.org/thread/6mcyszh49l25z6k2lcvhjv13hoz2dgtl))
- **Dmitri Bourlatchkov:** 'none' is clearer than 'local', and no specific statement about failing requests is needed. ([message](https://lists.apache.org/thread/dzhzwjpzb1q6lx45p7c1qf6nx7y9wbzx))

References: [iceberg#18480](https://github.com/apache/iceberg/issues/18480)
<!-- kb:generated:end -->

## Notes
