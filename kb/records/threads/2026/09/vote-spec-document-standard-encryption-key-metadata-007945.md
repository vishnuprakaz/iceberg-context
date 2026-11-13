---
id: thread/t-007945f7f6f7274a
type: thread
title: 'Spec: document standard encryption key metadata'
date: '2026-09-02'
url: https://lists.apache.org/thread/hpdmzppsl87l0olkpzm3q47occ9cfydo
kind: vote
status: no-conclusion
messages: 4
sources:
- devlist:hpdmzppsl87l0olkpzm3q47occ9cfydo
refs:
- gh:apache/iceberg#16527
links:
- rel: discussed
  to: initiative/v4-encryption
  confidence: extracted
  source: devlist:hpdmzppsl87l0olkpzm3q47occ9cfydo
- rel: started_by
  to: person/xanderbailey
  confidence: observed
updated: '2026-11-13'
---

# Spec: document standard encryption key metadata

<!-- kb:generated:start -->
**Thread:** [[VOTE] [SPEC] Document standard encryption key metadata](https://lists.apache.org/thread/hpdmzppsl87l0olkpzm3q47occ9cfydo) · **Started:** 2026-09-02 by [[person/xanderbailey|Xander]] · **Messages:** 4 (last 2026-09-03) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alexander Bailey called a vote on PR #16527, which adds an encryption spec document describing the binary formats used by the standard encryption scheme. Today the spec calls the key_metadata field in manifest entries and encrypted-key-metadata in table metadata implementation-specific, although the Java implementation fixes them, so other implementations such as iceberg-rust must reverse-engineer them. The document covers the standard key metadata format (a version byte followed by an Avro-encoded record with the DEK, AAD prefix and file length) and the two-tier key hierarchy in the encryption-keys list. It documents existing behavior. Gábor Kaszab welcomed it but felt the encryption spec is too coupled to the table spec and should be more generic. Gidon Gershinsky agreed the ongoing statistics-file encryption work should be reflected and favored updating the PR and voting again. Alexander Bailey agreed to revise the PR. No votes were cast.

**Why it matters:** Until the encryption spec is adopted, non-Java implementations have to derive the key metadata format from the Java source.

## Outcome

No votes were cast. The proposer agreed with the review direction and said he would revise the PR; Gidon Gershinsky suggested putting the updated PR to a new vote. ([message](https://lists.apache.org/thread/z1fn13n70q8b0r0pxx47m6ztxkmov3tw), `devlist:z1fn13n70q8b0r0pxx47m6ztxkmov3tw`)

## Positions

- **Alexander Bailey:** The key metadata binary format and key hierarchy fixed by the Java implementation should be documented in a spec so other implementations can read and write encrypted tables. ([message](https://lists.apache.org/thread/hpdmzppsl87l0olkpzm3q47occ9cfydo))
- **Gábor Kaszab:** The encryption spec makes too many assumptions about which table metadata fields use which encryption method and should be more generic. ([message](https://lists.apache.org/thread/cp4wl2opllzxb7mq8x6ncsptxhqjnft8))
- **Gidon Gershinsky:** The document should reflect statistics-file encryption and treat manifest lists as an example of a category while staying precise enough for interop; update the PR and vote again. ([message](https://lists.apache.org/thread/obvxs0tv82oznrltnmwo2swxh88wqlrz))

References: [iceberg#16527](https://github.com/apache/iceberg/issues/16527)
<!-- kb:generated:end -->

## Notes
