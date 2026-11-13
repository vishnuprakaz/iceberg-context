---
id: thread/t-b5daefa7bb409f3d
type: thread
title: Adding a file data type to Iceberg v4
date: '2026-07-26'
url: https://lists.apache.org/thread/33h4ppbrkmm83no3x6mfxqkv4zdw6ynv
kind: discuss
status: consensus
messages: 5
sources:
- devlist:33h4ppbrkmm83no3x6mfxqkv4zdw6ynv
refs:
- gh:apache/parquet-format#585
- doc:1W25ztRqm2xXBxOzGtUHK_mv-FLviQeIcKnUcmvCKOuo
- doc:1BdA4G-38GoVcpX6UY4UI-QA1MvrDnH6uSKeCJBadILQ
- list:kz09b2rj7c00j6z2vlqg8v5myh94bgl5
links: []
updated: '2026-11-13'
---

# Adding a file data type to Iceberg v4

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Add a file data type to Iceberg (v4)](https://lists.apache.org/thread/33h4ppbrkmm83no3x6mfxqkv4zdw6ynv) · **Started:** 2026-07-26 by Nitya Kumar Sharma · **Messages:** 5 (last 2026-08-13) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After the Parquet FILE logical type merged (parquet-format#585), Nitya Kumar Sharma shared a proposal document for a matching `file` data type in Iceberg, limited to type-level semantics and leaving credential vending and brokered access to the catalog. He said it was not a counter-proposal to the existing document by Talat Uyarer, Alex Stephen and Sung Yun, which covers both the type and catalog-brokered credential vending. Points for discussion included representing file as a named struct with six fixed leaves, allowing only inline and external forms, resolving relative URIs against the table location, ordinary per-leaf statistics, and no use as a partition, sort or equality-delete key. Russell Spitzer hoped the proposals would converge, and Daniel Weeks asked to consolidate around updating the existing proposal instead of starting a new effort. Nitya agreed to consolidate there and later asked the original authors how best to collaborate; the thread has no further reply.

**Why it matters:** File type design work was steered into a single proposal instead of two competing documents.

## Outcome

The author agreed to fold the work into the existing file type proposal; his later request to its authors about how to collaborate received no reply in the thread. ([message](https://lists.apache.org/thread/c1zrd5mbsgs6ytsn3pcpdhjs5qjjk9nq), `devlist:c1zrd5mbsgs6ytsn3pcpdhjs5qjjk9nq`)

## Positions

- **Nitya Kumar Sharma:** Converge on the file type's semantics separately from access control, with file as a named struct of six fixed leaves and only inline and external forms. ([message](https://lists.apache.org/thread/33h4ppbrkmm83no3x6mfxqkv4zdw6ynv))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Wants consensus between this proposal and the existing one from Talat and co-authors. ([message](https://lists.apache.org/thread/m02cmjo9xjyht62d0g5p3ktzr9tsfnw3))
- **[[person/danielcweeks|Daniel C. Weeks]]:** The community should consolidate around updating the existing proposal instead of starting a new effort. ([message](https://lists.apache.org/thread/qrn0nlw8b84n1qtqztc62kyw61cth5sd))

References: [parquet-format#585](https://github.com/apache/parquet-format/issues/585), [doc](https://docs.google.com/document/d/1W25ztRqm2xXBxOzGtUHK_mv-FLviQeIcKnUcmvCKOuo), [doc](https://docs.google.com/document/d/1BdA4G-38GoVcpX6UY4UI-QA1MvrDnH6uSKeCJBadILQ), [thread](https://lists.apache.org/thread/kz09b2rj7c00j6z2vlqg8v5myh94bgl5)
<!-- kb:generated:end -->

## Notes
