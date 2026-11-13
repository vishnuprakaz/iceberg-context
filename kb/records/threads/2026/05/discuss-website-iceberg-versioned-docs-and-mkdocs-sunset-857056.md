---
id: thread/t-85705605bcf82331
type: thread
title: 'Website: versioned docs and the future of MkDocs'
date: '2026-05-25'
url: https://lists.apache.org/thread/qvsvdn0nsj4wv3ox004h0948xp0c83bk
kind: discuss
status: consensus
messages: 9
sources:
- devlist:qvsvdn0nsj4wv3ox004h0948xp0c83bk
refs:
- gh:apache/iceberg#14521
- gh:apache/iceberg#16368
- list:vrt3oytl3dwo34wr07tkf73r0kkx0b1h
links: []
updated: '2026-11-13'
---

# Website: versioned docs and the future of MkDocs

<!-- kb:generated:start -->
**Thread:** [[Discuss] Website: Iceberg versioned docs and MkDocs sunset](https://lists.apache.org/thread/qvsvdn0nsj4wv3ox004h0948xp0c83bk) · **Started:** 2026-05-25 by Max Konstantinov · **Messages:** 9 (last 2026-05-26) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Max Konstantinov noted that MkDocs appears abandoned, with no contributions in about 18 months, and asked whether it is still worth pursuing mike (which builds on MkDocs) for a versioned docs dropdown, or whether Iceberg should look for a new documentation engine. rambleraptor said he had a frustrating experience with mike in iceberg-python because its CLI makes commits itself, and that a migration needs strong use cases. kevinjqliu confirmed MkDocs is abandoned but said the pinned older version works, the manual deployment process works, and migrating to mike is a big lift that may not be worth it after recent docs improvements. stevenzwu pointed out that older versions can be reached by URL but search covers only the latest version, so proper versioned docs are still wanted. Max concluded the current state is satisfactory and there is no demand strong enough to justify a new engine or mike; kevinjqliu agreed.

**Why it matters:** The docs site stays on a pinned MkDocs version with the manual versioned deployment, so contributors should not expect a docs engine migration soon.

## Outcome

The participants agreed not to migrate to mike or a new documentation engine for now; per-version search was noted as worth tracking if users ask for it. ([message](https://lists.apache.org/thread/7nt92f494fxh7bwrz8376pg42nrpj3by), `devlist:7nt92f494fxh7bwrz8376pg42nrpj3by`)

## Positions

- **Max Konstantinov:** Wants to know whether investing in mike is wasted effort given MkDocs is abandoned; concludes there is no strong enough need for a new engine or mike yet. ([message](https://lists.apache.org/thread/8y4ywqsd0rxc0pq9dlnqgodq7hp0gzkd))
- **[[person/rambleraptor|Alex Stephen]]:** Would like a different documentation engine in principle, but a migration is a lot of work and needs use cases MkDocs cannot support; mike did not work well for iceberg-python. ([message](https://lists.apache.org/thread/msg7kgfj4kqhpz6qd6k6h54chpr085g9))
- **[[person/kevinjqliu|Kevin Liu]]:** The pinned MkDocs version and manual deployment work, so neither mike nor a new engine is worth the effort now; per-version search indexes might be possible without a big migration. ([message](https://lists.apache.org/thread/7nt92f494fxh7bwrz8376pg42nrpj3by))
- **[[person/stevenzwu|Steven Wu]]:** Navigation and search should work together per version, which needs proper versioned doc support, though that is significant work. ([message](https://lists.apache.org/thread/26v1ckr0w26430gf0r9xk8zvd9pc1b3z))

References: [iceberg#14521](https://github.com/apache/iceberg/issues/14521), [iceberg#16368](https://github.com/apache/iceberg/issues/16368), [thread](https://lists.apache.org/thread/vrt3oytl3dwo34wr07tkf73r0kkx0b1h)
<!-- kb:generated:end -->

## Notes
