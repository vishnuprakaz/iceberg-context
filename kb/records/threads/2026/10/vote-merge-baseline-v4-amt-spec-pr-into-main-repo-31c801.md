---
id: thread/t-31c8012d43fc214e
type: thread
title: Vote to merge the baseline V4 AMT spec PR into the main repo
date: '2026-10-09'
url: https://lists.apache.org/thread/qch7jjnwb8pm49lt3h7lqfxj82hlg8ps
kind: vote
status: passed
messages: 20
sources:
- devlist:qch7jjnwb8pm49lt3h7lqfxj82hlg8ps
refs:
- gh:apache/iceberg#16025
links:
- rel: discussed
  to: initiative/v4-metadata-tree
  confidence: extracted
  source: devlist:qch7jjnwb8pm49lt3h7lqfxj82hlg8ps
- rel: started_by
  to: person/amogh-jahagirdar
  confidence: observed
updated: '2026-11-13'
---

# Vote to merge the baseline V4 AMT spec PR into the main repo

<!-- kb:generated:start -->
**Thread:** [[VOTE] Merge baseline V4 AMT spec PR into main repo](https://lists.apache.org/thread/qch7jjnwb8pm49lt3h7lqfxj82hlg8ps) · **Started:** 2026-10-09 by [[person/amogh-jahagirdar|Amogh Jahagirdar]] · **Messages:** 20 (last 2026-10-14) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Amogh Jahagirdar called a vote to merge the baseline V4 adaptive metadata tree spec PR into the main repository. He stressed that, like earlier spec votes, this is a vote to merge the changes and not a vote for adoption. Encryption, specific requirements for column file updates, dropping the partition tuple and other areas can be iterated on later; the aim is to land a baseline that will not need extensive rebasing while other V4 work continues. Replies were all in favor. Gábor Kaszab said he would cover the encryption part in an immediate follow-up change, and Szehon Ho left comments on the PR to clarify harder-to-read parts. Amogh announced that the vote passed and said he would merge the PR.

**Why it matters:** The baseline V4 adaptive metadata tree spec text lands in the main repository, giving other V4 changes a common base, without being adopted yet.

## Outcome

Passed with 18 +1 votes (9 binding, 9 non-binding) and no 0 or -1 votes. Amogh Jahagirdar said he would merge the baseline spec PR. ([message](https://lists.apache.org/thread/gw1jf5j1l9hk369lbcz6g4rn4l06t77c), `devlist:gw1jf5j1l9hk369lbcz6g4rn4l06t77c`)

## Positions

- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Merge the baseline V4 AMT spec changes now, as a merge and not an adoption vote, and iterate later on encryption, column file updates and dropping the partition tuple. ([message](https://lists.apache.org/thread/qch7jjnwb8pm49lt3h7lqfxj82hlg8ps))
- **Gábor Kaszab:** Supports the merge and will cover the encryption part with an immediate follow-up change. ([message](https://lists.apache.org/thread/w2mo24kk86jzokxr55nqko349rr2cvcm))
- **[[person/szehon-ho|Szehon Ho]]:** The spec looks correct; he left comments to clarify some of the harder-to-read parts. ([message](https://lists.apache.org/thread/jttjxn4kdkydk5xhb8t97ozjwxco00y0))

References: [iceberg#16025](https://github.com/apache/iceberg/issues/16025)
<!-- kb:generated:end -->

## Notes
