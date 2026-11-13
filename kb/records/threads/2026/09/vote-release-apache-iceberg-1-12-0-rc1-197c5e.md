---
id: thread/t-197c5e8a5755ba9a
type: thread
title: 'Vote: release Apache Iceberg 1.12.0 RC1'
date: '2026-09-23'
url: https://lists.apache.org/thread/z5fk8q6pwx6v5nkm3r4l3olf300myghh
kind: release-vote
status: withdrawn
messages: 6
sources:
- devlist:z5fk8q6pwx6v5nkm3r4l3olf300myghh
refs:
- gh:apache/iceberg#18164
- gh:apache/iceberg#18208
- gh:apache/iceberg#18069
- gh:apache/iceberg#18218
- gh:apache/iceberg#18226
- gh:apache/iceberg#18227
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:z5fk8q6pwx6v5nkm3r4l3olf300myghh
- rel: started_by
  to: person/Kurtiscwright
  confidence: observed
updated: '2026-11-13'
---

# Vote: release Apache Iceberg 1.12.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.12.0 RC1](https://lists.apache.org/thread/z5fk8q6pwx6v5nkm3r4l3olf300myghh) · **Started:** 2026-09-23 by [[person/Kurtiscwright|Kurtis Wright]] · **Messages:** 6 (last 2026-09-24) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The vote thread for Apache Iceberg 1.12.0 RC1 surfaced several issues. nssalian summarized them: a fix for issue #18164 (reading variant columns failed with commons-lang3 older than 3.13) in PR #18208 should go into the next RC; the fix in PR #18069 was already in this RC; and a missing Caffeine LICENSE entry found by Kurtis needs a new RC. He closed the thread and said a new candidate would be built with Amogh. kevinjqliu then reviewed bundled dependencies: Caffeine was fixed by PR #18218, OpenTelemetry and Apache HttpComponents 5 were already covered, CEL Java is a non-blocking nit (PR #18226), and a new gap for Jackson was found (PR #18227). He suggested adding a license check to the release process. Jean-Baptiste Onofré voted -1 (non-binding) over the incomplete bundle LICENSE files. nssalian reported the license fixes merged.

**Why it matters:** Incomplete LICENSE entries in bundled runtime jars were enough to restart the 1.12.0 release candidate, and a license check in the release process was suggested.

## Outcome

The release manager closed the thread and said a new release candidate would be cut to include the fixes; the license fixes were later reported merged. ([message](https://lists.apache.org/thread/sgqpwxyo6wm5zkb3d86lq90jnv5q0mx0), `devlist:sgqpwxyo6wm5zkb3d86lq90jnv5q0mx0`)

## Positions

- **[[person/nssalian|Neelesh Salian]]:** A new release candidate is needed to include the commons-lang3 variant fix and the missing Caffeine license entry. ([message](https://lists.apache.org/thread/sgqpwxyo6wm5zkb3d86lq90jnv5q0mx0))
- **[[person/kevinjqliu|Kevin Liu]]:** The Jackson attribution gap in PR #18227 is what blocks the next RC, and the release process should include a license check. ([message](https://lists.apache.org/thread/j69x3778c4xkdb15yf8lo9ggcfpnt3sh))
- **Jean-Baptiste Onofré:** Votes -1 because the GCP bundle LICENSE omits Caffeine and the Jackson (FastDoubleParser) entry needs updating in several bundle and runtime LICENSE files. ([message](https://lists.apache.org/thread/gfy6p268pw7npz0wmjxb2gh77g7k4pzl))

References: [iceberg#18164](https://github.com/apache/iceberg/issues/18164), [iceberg#18208](https://github.com/apache/iceberg/issues/18208), [iceberg#18069](https://github.com/apache/iceberg/issues/18069), [iceberg#18218](https://github.com/apache/iceberg/issues/18218), [iceberg#18226](https://github.com/apache/iceberg/issues/18226), [iceberg#18227](https://github.com/apache/iceberg/issues/18227)
<!-- kb:generated:end -->

## Notes
