---
id: thread/t-50827b2ab1b71544
type: thread
title: Write-path gap for field-id-bound policy during schema evolution
date: '2026-06-16'
url: https://lists.apache.org/thread/3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb
kind: discuss
status: no-conclusion
messages: 4
sources:
- devlist:3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb
refs:
- yt:orAXA5e9pmU
links:
- rel: discussed
  to: initiative/read-restrictions
  confidence: extracted
  source: devlist:3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb
- rel: started_by
  to: person/sungwy
  confidence: observed
updated: '2026-11-13'
---

# Write-path gap for field-id-bound policy during schema evolution

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Write-path gap for field-id-bound policy during schema evolution](https://lists.apache.org/thread/3nxxy6q2cjqwjwvnpnxnj4z5vl3ddlcb) · **Started:** 2026-06-16 by [[person/sungwy|Sung Yun]] · **Messages:** 4 (last 2026-06-22) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The messages here start with Sung Yun (sungwy) replying to Andrei about a broader pattern; Sung wanted the community to first decide whether the 'Drift' and 'Creation' problems described in a Google Doc, which have security consequences for fine-grained access control policies, merit a first-class construct in the REST catalog write path, and planned to bring the policy case to the catalog sync. Prashant Singh saw no gap: catalogs resolve column names to field IDs before persisting a policy attachment, and when ReadRestrictions was modeled, defining and attaching policies was intentionally left as a catalog concern. Sung agreed that binding by field ID addresses drift, but pointed out that a field ID does not exist until the schema change commits, leaving a window in which a new column meant to be protected is not; the question is whether to accept that or let a column land protected in the same commit. Yufei Gu (flyrain) considered this mostly a catalog implementation concern that the spec need not mandate. The thread ends before the sync discussion.

## Outcome

The thread ends without agreement; the topic was put on the agenda of the REST catalog sync.

## Positions

- **[[person/sungwy|Sung Yun]]:** Because a field ID does not exist until the schema change commits, a new column is unprotected until a policy is attached out of band, and the community should decide whether to allow a column to be created already protected. ([message](https://lists.apache.org/thread/70tw7hoftdxjry61yq8txnrsrlfjx8m8))
- **[[person/singhpk234|Prashant Singh]]:** There is no gap, since policies are bound by field ID in catalog metadata and defining and attaching policies was intentionally left to the catalog. ([message](https://lists.apache.org/thread/r3hvf2o8qo1zt45b81y0p25c06lxxv54))
- **[[person/flyrain|Yufei Gu]]:** This is mostly a catalog implementation concern; a catalog may support committing policy with DDL, but the REST spec need not mandate it. ([message](https://lists.apache.org/thread/3dyrmb9j80y9739wzt3mf1tnhvppnzpy))

References: [video](https://www.youtube.com/watch?v=orAXA5e9pmU)
<!-- kb:generated:end -->

## Notes
