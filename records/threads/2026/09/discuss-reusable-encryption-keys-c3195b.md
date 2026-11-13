---
id: thread/t-c3195bd81b8adb3b
type: thread
title: Reusable encryption keys
date: '2026-09-23'
url: https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s
kind: discuss
status: open
messages: 9
sources:
- devlist:38rkthkr1fg0s86493fjq755cnl3y90s
refs:
- gh:apache/iceberg#17533
- gh:apache/iceberg#16353
links:
- rel: started_by
  to: person/gaborkaszab
  confidence: observed
updated: '2026-11-13'
---

# Reusable encryption keys

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Reusable encryption keys](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s) · **Started:** 2026-09-23 by [[person/gaborkaszab|Gabor Kaszab]] · **Messages:** 9 (last 2026-10-05) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Gábor Kaszab questioned the assumption behind the table metadata encryption-keys list, namely that one data encryption key (DEK) can be reused for several files. He argued that reuse is hard to do safely because the DEK and nonce pair must never repeat, and that one DEK per file is common practice. V3 manifest lists already use a key-id that points into the list and cannot change, but for new file types such as V4 root manifests and statistics files he proposed storing the encrypted key metadata directly with the file reference, while key encryption keys stay in the shared list. Gidon Gershinsky agreed. Xander Bailey first preferred keeping the existing key-id pattern so implementations share one lookup and lifecycle path, then found the cleanup and list-growth arguments compelling. The thread ends with Gábor asking for feedback on the spec PR (#17533); no decision is recorded.

**Why it matters:** It determines where encryption keys for statistics files and V4 root manifests live in table metadata and how they are cleaned up.

## Outcome

The three participants ended up agreeing on a fresh DEK per file stored inline for new file types, but the thread closes with a request for wider feedback on spec PR #17533 and no recorded decision.

## Positions

- **Gábor Kaszab:** Against reusing DEKs across files; for V4 root manifests and statistics files, store the encrypted key directly instead of a key-id into encryption-keys. ([message](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s))
- **Gidon Gershinsky:** In V4, DEK metadata is best moved into per-file structures while KEKs stay in the shared list; a random DEK per file is the simple and practical solution. ([message](https://lists.apache.org/thread/090brbvtrrn1kofkfrxcr1wqn9877zho))
- **Xander Bailey:** The existing key-id pattern already supports one DEK per file and would keep statistics and manifest lists on one representation and one lifecycle path. ([message](https://lists.apache.org/thread/3t20q7hm3hqgdk6y1hcpgt5lh3dhlvox))
- **Gábor Kaszab:** Keeping the list means every new encrypted file type needs its own key cleanup and the list grows; without key reuse the list has lost its purpose. ([message](https://lists.apache.org/thread/g1sxh4c85tm5kmpszfo2ooch461pr4gq))
- **Xander Bailey:** Finds those arguments compelling and asks for a draft Java implementation. ([message](https://lists.apache.org/thread/jmt0yz78vw2j9c7q311n8w4cmq9vvhsr))

References: [iceberg#17533](https://github.com/apache/iceberg/issues/17533), [iceberg#16353](https://github.com/apache/iceberg/issues/16353)
<!-- kb:generated:end -->

## Notes
