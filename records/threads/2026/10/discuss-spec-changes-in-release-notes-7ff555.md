---
id: thread/t-7ff555b89c73c647
type: thread
title: Spec changes in release notes
date: '2026-10-01'
url: https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j
kind: release-planning
status: open
messages: 7
sources:
- devlist:3otgz8ll1zkt3wt3hvjpll6pmzr4w57j
refs:
- gh:apache/iceberg#18349
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:3otgz8ll1zkt3wt3hvjpll6pmzr4w57j
- rel: discussed
  to: initiative/community-process
  confidence: extracted
  source: devlist:3otgz8ll1zkt3wt3hvjpll6pmzr4w57j
- rel: started_by
  to: person/Kurtiscwright
  confidence: observed
updated: '2026-11-13'
---

# Spec changes in release notes

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Spec changes in release notes](https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j) · **Started:** 2026-10-01 by [[person/Kurtiscwright|Kurtis Wright]] · **Messages:** 7 (last 2026-10-05) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread started from the review of the 1.12.0 release notes: text quoted in the replies observes that spec changes are listed in the Java binary release notes although they take effect when voted and merged, independent of Java releases, and asks to stop including them and to give spec changes their own page. Quoted replies supported removing them, including retrospectively, and moving them to a changelog on the spec page; one asked about a separate iceberg-format repository holding the spec, docs and website. Danny Jones supported such a repository, or otherwise a dedicated spec changelog. Hongyue Zhang and nssalian agreed with separating spec changes, nssalian noting they had appeared in the notes since 1.5.0. pvary opened PR #18349 showing the intended layout; kevinjqliu reviewed it and asked to add the REST catalog spec as a follow-up. danielcweeks strongly opposed a separate iceberg-format repository. The thread ends with the PR under review.

**Why it matters:** Spec changes are set to be tracked in their own changelog rather than in Java release notes, which affects where contributors record them.

## Outcome

All who replied supported taking spec changes out of the Java release notes, and PR #18349 with a dedicated layout is under review. The separate iceberg-format repository idea drew one supporter and strong opposition from danielcweeks; nobody declared a result.

## Positions

- **Danny Jones:** Supports creating an iceberg-format repository dedicated to spec changes, keeping commit history, or failing that a dedicated changelog in the spec. ([message](https://lists.apache.org/thread/1wofcxw41qmbn507lgq0r9cz6s4sd9pf))
- **Hongyue Zhang:** Supports separating binary release notes from spec changes and removing past entries for consistency. ([message](https://lists.apache.org/thread/f12zkcg0bhznfprbk1cmp75c9tnvk8r4))
- **[[person/nssalian|Neelesh Salian]]:** Kept the spec changes in the 1.12.0 notes for consistency since removal had not been discussed before, and likes a dedicated changelog for the spec. ([message](https://lists.apache.org/thread/f6drq2q4x20r87xlqnmhwp9v1hjygzls))
- **[[person/pvary|Peter Vary]]:** Proposes a concrete layout for separating spec changes in PR #18349 and asks for feedback. ([message](https://lists.apache.org/thread/96n6pc0od1j2r95tw28bgp5wxoxhgtkv))
- **[[person/kevinjqliu|Kevin Liu]]:** Approves of the PR's approach and wants the REST catalog spec added as a follow-up because it has changed the most recently. ([message](https://lists.apache.org/thread/12yrx842h8zpfjdckm05shfqnffy9c7m))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Strongly opposes an iceberg-format repository; keeping the specs with the reference implementation works and moving them adds little value. ([message](https://lists.apache.org/thread/41vbbf6hl0fgc8pbkf2r86k05zvo40kk))

References: [iceberg#18349](https://github.com/apache/iceberg/issues/18349)
<!-- kb:generated:end -->

## Notes
