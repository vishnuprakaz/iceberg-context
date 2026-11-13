---
id: thread/t-643f9a86cf02dd71
type: thread
title: 'Proposal: file-level access delegation in the Iceberg REST catalog spec'
date: '2026-07-01'
url: https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm
kind: discuss
status: open
messages: 4
sources:
- devlist:odof6m2npvktwd51cz8qnrxjv95ws4wm
refs:
- list:ko9kp0gvzhx85n7cvoxqnpw4vwnhmdg6
links:
- rel: discussed
  to: initiative/rest-auth
  confidence: extracted
  source: devlist:odof6m2npvktwd51cz8qnrxjv95ws4wm
- rel: started_by
  to: person/williamhyun
  confidence: observed
updated: '2026-11-13'
---

# Proposal: file-level access delegation in the Iceberg REST catalog spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Proposal: File-Level Access Delegation in the Iceberg REST Catalog Spec](https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm) · **Started:** 2026-07-01 by [[person/williamhyun|William Hyun]] · **Messages:** 4 (last 2026-07-08) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

williamhyun proposed extending the REST catalog spec with file-level access delegation during scan planning. He said delegated access today is table-scoped, which can force over-provisioning or table fragmentation when consumers should only see a subset of partitions or records, and proposed pre-signed URLs to make partition-scoped sharing practical. kevinjqliu welcomed the proposal and noted possible feature gaps in pre-signed URL support in the Java implementation and subprojects. After the July 1 catalog sync, williamhyun summarized two alternatives raised there: scoped credential vending and remote signing with caching and bulk signing. He argued scoped vending fits when access maps to a few stable prefixes but is impractical for many specific files, because on AWS each narrower scope requires a new STS session subject to request-rate and policy-size limits. He then shared a proof-of-concept PR in his fork exploring bulk remote signing with caching and asked for feedback. No decision was reached.

**Why it matters:** Could add partition- or file-scoped data sharing to the REST catalog, with the mechanism (pre-signed URLs or bulk remote signing) still undecided.

## Outcome

No decision. The author is evaluating bulk remote signing with caching through a proof of concept in his fork and asked for feedback.

## Positions

- **[[person/williamhyun|William Hyun]]:** Table-scoped delegation forces over-provisioning or table fragmentation; the REST spec should support file-level delegation during scan planning using pre-signed URLs. ([message](https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm))
- **[[person/kevinjqliu|Kevin Liu]]:** Supports addressing the use case; pre-signed URL support in the Java implementation and subprojects may have gaps that need checking. ([message](https://lists.apache.org/thread/dqnqwyw9gsljo9gjyy3bm4mbmrhk44x6))
- **[[person/williamhyun|William Hyun]]:** Scoped credential vending is impractical for many specific files because each scope needs a new STS session with rate and policy-size limits; bulk remote signing with caching is worth evaluating as an alternative to pre-signed URLs. ([message](https://lists.apache.org/thread/k4kxnr870b6q4wrdnqov8ro98rmq1955))

References: [thread](https://lists.apache.org/thread/ko9kp0gvzhx85n7cvoxqnpw4vwnhmdg6)
<!-- kb:generated:end -->

## Notes
