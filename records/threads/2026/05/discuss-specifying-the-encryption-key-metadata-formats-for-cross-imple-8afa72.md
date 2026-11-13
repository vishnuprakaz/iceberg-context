---
id: thread/t-8afa728d41cbbd2f
type: thread
title: Specifying the encryption key metadata formats for cross-implementation interop
date: '2026-05-20'
url: https://lists.apache.org/thread/4zm5jhwp42z10pfz2sths7q59r9dlf8l
kind: discuss
status: open
messages: 5
sources:
- devlist:4zm5jhwp42z10pfz2sths7q59r9dlf8l
refs:
- gh:apache/iceberg#16527
links: []
updated: '2026-11-13'
---

# Specifying the encryption key metadata formats for cross-implementation interop

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Specifying the encryption key metadata formats for cross-implementation interop](https://lists.apache.org/thread/4zm5jhwp42z10pfz2sths7q59r9dlf8l) · **Started:** 2026-05-20 by Alexander Bailey · **Messages:** 5 (last 2026-07-29) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

While implementing table encryption in iceberg-rust, Alexander Bailey found formats needed for interoperability that the spec calls implementation-specific and that had to be reverse-engineered from Java. He proposed specifying two things: the `StandardKeyMetadata` format used in the `key_metadata` field (a version byte followed by an Avro datum holding the encryption key, an optional AAD prefix and an optional file length), and the convention in the table-level `encryption-keys` list that separates KMS-wrapped key-encryption keys from manifest-list keys wrapped with AES-GCM using the KEK timestamp as AAD. The KMS-wrapped key metadata would stay opaque. Without this, he argued, tables encrypted by one implementation could be unreadable by another that also complies with the spec. Yufei and Szita Ádám agreed. He opened PR #16527 and, following a suggestion on the PR, later refactored it into a new encryption spec document and asked for further review.

**Why it matters:** Until these formats are in the spec, non-Java implementations must copy Java's behavior byte for byte to read or write encrypted tables.

## Outcome

Replies supported the idea; PR #16527 was reworked into a separate encryption spec document and was still awaiting review at the last message.

## Positions

- **Alexander Bailey:** The spec should document the StandardKeyMetadata wire format and the KEK versus wrapped-DEK convention in `encryption-keys`, leaving only the KMS-wrapped KEK metadata implementation-specific. ([message](https://lists.apache.org/thread/4zm5jhwp42z10pfz2sths7q59r9dlf8l))
- **[[person/flyrain|Yufei Gu]]:** Supports putting these formats in the spec because there is currently a gap between spec-compliant and cross-implementation compatible. ([message](https://lists.apache.org/thread/tq6vrnw76lff35oy9wkdvdwfk4476zfk))
- **Szita Ádám:** Agrees the formats need a stricter specification. ([message](https://lists.apache.org/thread/jnkdx9696r9qy1yzykfc97xrgom6wzlr))

References: [iceberg#16527](https://github.com/apache/iceberg/issues/16527)
<!-- kb:generated:end -->

## Notes
