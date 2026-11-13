---
id: thread/t-4fdcd748e0704aa5
type: thread
title: Initial REST catalog spec changes needed for Iceberg V4
date: '2026-08-13'
url: https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl
kind: discuss
status: open
messages: 10
sources:
- devlist:6y446mbtrho2r54cbd2x9gzyb13jjlbl
refs:
- gh:apache/iceberg#17543
- gh:apache/iceberg#17642
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:6y446mbtrho2r54cbd2x9gzyb13jjlbl
- rel: discussed
  to: initiative/v4-general
  confidence: extracted
  source: devlist:6y446mbtrho2r54cbd2x9gzyb13jjlbl
- rel: discussed
  to: initiative/v4-relative-paths
  confidence: extracted
  source: devlist:6y446mbtrho2r54cbd2x9gzyb13jjlbl
updated: '2026-11-13'
---

# Initial REST catalog spec changes needed for Iceberg V4

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Initial IRC changes needed for Iceberg V4](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl) · **Started:** 2026-08-13 by dhruvarya-db · **Messages:** 10 (last 2026-11-12) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Dhruv Arya listed the first REST spec changes V4 needs: a root-manifest in Snapshot as an alternative to manifest-list, a table-location in load, commit and unregister responses to allow relative paths, and an optional metadata-location in CommitTableResponse. Because manifest-list and metadata-location are required today, he offered two approaches: duplicating models and endpoints as v2 (PR #17543), or relaxing the required fields in place (PR #17642), which he preferred. Daniel Weeks and Amogh Jahagirdar favoured the smaller model change combined with a new v2 loadTable endpoint that all V4 tables must be loaded through, since clients cannot be relied on to check format-version before failing on a missing field. Yufei Gu agreed that v1 loadTable must not return V4 metadata and suggested an error response instead. In November Daniel Weeks created a rest-v4-changes branch to collect the OpenAPI changes. No vote was held in the thread.

**Why it matters:** It introduces the first versioned (v2) REST endpoint, and catalogs and clients will need it to load V4 tables.

## Outcome

Participants converged on in-place model changes plus a v2 loadTable endpoint for V4 tables. A rest-v4-changes branch was created to collect the spec changes, with PR #17642 open for feedback. ([message](https://lists.apache.org/thread/zrn1jb7g9wm7jgn4fx3klmtxs03k65zg), `devlist:zrn1jb7g9wm7jgn4fx3klmtxs03k65zg`)

## Positions

- **dhruvarya-db:** Leans toward making manifest-list and metadata-location optional in place rather than duplicating models and endpoints as v2. ([message](https://lists.apache.org/thread/6y446mbtrho2r54cbd2x9gzyb13jjlbl))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Prefers the second approach, but with a v2 loadTable endpoint required for all V4 tables; only load table needs a version bump. ([message](https://lists.apache.org/thread/2y5vj6vsyd49p4vsnqxj75tgy0jxxfwq))
- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Agrees with a v2 load endpoint serving v1-v4 tables, and thinks the V4 table spec should be voted before the v2 REST spec. ([message](https://lists.apache.org/thread/9wdwjhog9qlv6jccshbmstjy109s2wol))
- **[[person/flyrain|Yufei Gu]]:** Since format-version is required in TableMetadata, a client should be able to identify the version before interpreting the rest of the metadata. ([message](https://lists.apache.org/thread/3gh3nfy6jl26cfh0cylx8ydqr0k62r48))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Field processing order cannot be guaranteed, so an older client may fail on a missing required location before it can check the version. ([message](https://lists.apache.org/thread/trf8d4rcnbr8fhhqwbh26twwqrr36hp1))
- **[[person/flyrain|Yufei Gu]]:** The v1 loadTable endpoint must not return V4 metadata and should return a documented error; suggested collecting other v2 requirements such as partial metadata loading. ([message](https://lists.apache.org/thread/fxftrwg17dc4b2szhjf4y79x11z7kylp))
- **[[person/danielcweeks|Daniel C. Weeks]]:** An error response for V4 tables on v1 loadTable is right, but is hesitant to take on partial metadata loading as part of the v2 endpoint. ([message](https://lists.apache.org/thread/1sv1fw7zz5rrglxx0vhwnhdj4cmmnnx8))

References: [iceberg#17543](https://github.com/apache/iceberg/issues/17543), [iceberg#17642](https://github.com/apache/iceberg/issues/17642)
<!-- kb:generated:end -->

## Notes
