---
id: thread/t-87bfb68a54b233c9
type: thread
title: Refreshing storage credentials for staged table creation
date: '2026-02-10'
url: https://lists.apache.org/thread/35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp
kind: discuss
status: consensus
messages: 8
sources:
- devlist:35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp
refs:
- gh:apache/iceberg#15280
- doc:1R1K6X7qYqvIFkPG3m1neV5Mvy8rwWJvhSFr8DgJgQ-E
- list:q5n355d89nxbhywtlv3qhq7dchbyb67d
links: []
updated: '2026-11-13'
---

# Refreshing storage credentials for staged table creation

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Refreshing storage credentials for staged table creation](https://lists.apache.org/thread/35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp) · **Started:** 2026-02-10 by Maninder Parmar · **Messages:** 8 (last 2026-05-21) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Maninder Parmar proposed a way to refresh storage credentials for staged tables (used for CTAS), which are not yet committed and so are not visible to loadTable or the credentials endpoint. The first design returned a stagingSession identifier, modelled on planId. huaxingao asked about treating it as a secret and about cleanup; the author said it is only an identifier and its lifecycle is up to the catalog. After catalog syncs the direction changed to a storage refresh token tied to the existing StorageCredential mechanism, reusable beyond staging, without server-side state; table-uuid, sessions and OAuth scopes were discarded. Later syncs decided refresh happens only on the loadCredentials endpoint, and an S3-only proof of concept was added to PR #15280. In May 2026 the author reported the last two issues resolved: a 1:1 mapping between credential and refresh token, and sending the token in headers rather than URL parameters.

**Why it matters:** Long-running CTAS jobs against REST catalogs can outlive vended credentials, and the refresh-token design is meant to be reused for other credential vending cases.

## Outcome

The author reported that the community sync closed all known spec issues: a 1:1 mapping between storage credential and refresh token, and the token sent in headers. An updated PR was to follow; no vote was held in this thread. ([message](https://lists.apache.org/thread/00ghs2og6pgq402n3xld2rrqj8x0t2rt), `devlist:00ghs2og6pgq402n3xld2rrqj8x0t2rt`)

## Positions

- **Maninder Parmar:** Staged tables need a credential refresh mechanism; after sync feedback it should be a generic storage refresh token on StorageCredential rather than a staging-specific session. ([message](https://lists.apache.org/thread/w9olh0nwwxm2tcrlq5m7q1vsc25rzwd9))
- **[[person/huaxingao|Huaxin Gao]]:** Supports the direction and asks whether the stagingSession should be a secret, who may use it, and how abandoned staged creates are cleaned up. ([message](https://lists.apache.org/thread/yqbnqkpxq9omkp5296314l5pblgy4tmy))

References: [iceberg#15280](https://github.com/apache/iceberg/issues/15280), [doc](https://docs.google.com/document/d/1R1K6X7qYqvIFkPG3m1neV5Mvy8rwWJvhSFr8DgJgQ-E), [thread](https://lists.apache.org/thread/q5n355d89nxbhywtlv3qhq7dchbyb67d)
<!-- kb:generated:end -->

## Notes
