---
id: thread/t-07dfa8ee9a2cbc37
type: thread
title: Vote on adding the File type to the Iceberg v4 spec (later votes)
date: '2026-10-14'
url: https://lists.apache.org/thread/ldkpj659fjrf6nrc8vbg0b3fknxwdg38
kind: vote
status: passed
messages: 8
sources:
- devlist:ldkpj659fjrf6nrc8vbg0b3fknxwdg38
- devlist:6b63cbcsf0l69z9hs6v9nc1gp4y96tlp
refs: []
links:
- rel: discussed
  to: initiative/file-type
  confidence: extracted
  source: devlist:ldkpj659fjrf6nrc8vbg0b3fknxwdg38
- rel: started_by
  to: person/sungwy
  confidence: observed
updated: '2026-11-13'
---

# Vote on adding the File type to the Iceberg v4 spec (later votes)

<!-- kb:generated:start -->
**Thread:** [[VOTE] Add the File type to the Iceberg v4 spec](https://lists.apache.org/thread/ldkpj659fjrf6nrc8vbg0b3fknxwdg38) · **Started:** 2026-10-14 by [[person/sungwy|Sung Yun]] · **Messages:** 8 (last 2026-10-19) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

These are later replies to the vote on adding the File type to the Iceberg v4 spec; the opening message of the vote is not among them. Seven of the eight replies are +1 votes, three of them marked binding. Kurtis Wright voted +0 (non-binding) and repeated a comment he had left on the specification PR: he wants a field, under any name, that tells maintenance operations whether the files at the URI are safe to remove or otherwise manipulate. Without it, he argued, there is no way to have a media bucket that several tables point to, which then requires copying the data multiple times. He said the spec need not define how such an indicator is updated, and that he would change his vote to +1 if the field were added. Nobody replied to this point here, and no result is announced in these messages.

**Why it matters:** The one reservation recorded in the vote is that the file type has no way to mark who owns referenced files for cleanup.

## Outcome

No result is announced in these messages. Votes cast here: three binding +1, four non-binding +1 and one non-binding +0.

**Result posted in a separate thread on 2026-10-19:** [[RESULT][VOTE] Add the File type to the Iceberg v4 spec](https://lists.apache.org/thread/6b63cbcsf0l69z9hs6v9nc1gp4y96tlp) (`devlist:6b63cbcsf0l69z9hs6v9nc1gp4y96tlp`). Outcome read from that message: passed.

## Positions

- **[[person/Kurtiscwright|Kurtis Wright]]:** Votes +0 (non-binding): the file type needs a field telling maintenance operations whether referenced files are safe to delete, so several tables can share one media bucket without copying data. ([message](https://lists.apache.org/thread/1nq15gfnxdpkxgxfwr1mxrjxvk3skq7v))
<!-- kb:generated:end -->

## Notes
