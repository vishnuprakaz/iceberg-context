---
id: thread/t-d332ec73c7f3e8cc
type: thread
title: Vote to update the spec wording for the geospatial type CRS parameter
date: '2026-05-11'
url: https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7
kind: vote
status: open
messages: 9
sources:
- devlist:8z0kc8vz1379lghwlcwl0jmsoym6shd7
refs:
- gh:apache/iceberg#15834
- gh:apache/parquet-format#560
- list:r5x0do8f241bpf565rx8s5s3wc9ogp0f
links:
- rel: discussed
  to: initiative/geospatial
  confidence: extracted
  source: devlist:8z0kc8vz1379lghwlcwl0jmsoym6shd7
updated: '2026-11-13'
---

# Vote to update the spec wording for the geospatial type CRS parameter

<!-- kb:generated:start -->
**Thread:** [[VOTE] Proposal to update working in spec for Geospatial type CRS. parameter](https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7) · **Started:** 2026-05-11 by milastdbx · **Messages:** 9 (last 2026-05-15) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Milan Stefanovic (milastdbx) called a vote to update the wording of the CRS parameter for the geospatial types in the spec, with the change in PR #15834. Depending on how the current text is read, it can be taken as either suggestive or restrictive about how a CRS field is populated, that is, whether the 'srid:' and 'projjson:' forms are the only allowed formats or just examples. The proposal rewords the text so that the purpose is clear and unambiguous. He noted that a similar proposal was made in the Parquet community. All eight replies were +1. Steven Wu left minor comments on syntax and grammar in the PR and asked that they be addressed before merging. The bundle contains no message that closes the vote or announces the result.

## Outcome

No result message is in the thread. Votes cast: 5 binding +1, 2 non-binding +1 and one +1 with no binding status stated, with no 0 or -1 votes.

## Positions

- **milastdbx:** The CRS wording should be updated so it is unambiguous whether 'srid:' and 'projjson:' are the only allowed formats or examples. ([message](https://lists.apache.org/thread/8z0kc8vz1379lghwlcwl0jmsoym6shd7))
- **[[person/stevenzwu|Steven Wu]]:** Votes +1 (binding) and asks that minor syntax and grammar comments on the PR be addressed before merging. ([message](https://lists.apache.org/thread/tttbovgpx9nh0yn289qsyls615y8h0oq))

References: [iceberg#15834](https://github.com/apache/iceberg/issues/15834), [parquet-format#560](https://github.com/apache/parquet-format/issues/560), [thread](https://lists.apache.org/thread/r5x0do8f241bpf565rx8s5s3wc9ogp0f)
<!-- kb:generated:end -->

## Notes
