---
id: thread/t-dea37ea5d432effa
type: thread
title: Vote on releasing Apache Iceberg Rust 0.10.0 RC3
date: '2026-07-08'
url: https://lists.apache.org/thread/h8ohxh44g1zc32clg3sgxr80xjc4nnr9
kind: release-vote
status: passed
messages: 11
sources:
- devlist:h8ohxh44g1zc32clg3sgxr80xjc4nnr9
- devlist:fymfyn86yr1zzhlc3l1fb3j27o5v5t75
refs:
- gh:apache/iceberg-rust#2823
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:h8ohxh44g1zc32clg3sgxr80xjc4nnr9
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg Rust 0.10.0 RC3

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.10.0 RC3](https://lists.apache.org/thread/h8ohxh44g1zc32clg3sgxr80xjc4nnr9) · **Started:** 2026-07-08 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 11 (last 2026-07-14) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones called a vote to release Apache Iceberg Rust 0.10.0 from tag v0.10.0-rc.3. Voters reported verifying checksums, signatures, license files and headers, the build and tests, and the pyiceberg-core build and tests; Matt Butrovich also ran DataFusion Comet CI against the candidate. Kevin Liu first voted +1 and noted that Python build directories trip the license header check. On July 14 he changed his vote to -1 because the iceberg-storage-opendal, iceberg-catalog-loader and iceberg-cache-moka crates lack LICENSE and NOTICE files, and said a new release candidate is needed. The thread ends with that message and no result is stated.

**Why it matters:** Each published crate needs its own LICENSE and NOTICE files; their absence in three crates drew a -1 on this candidate.

## Outcome

No result is stated in the thread. Before the -1 there were +1 votes marked binding from liurenjie1024, kevinjqliu and amogh-jahagirdar and seven marked non-binding; kevinjqliu then changed his vote to -1 and asked for a new RC. ([message](https://lists.apache.org/thread/rtn30pj4fjl70m6f0rzzmt8gml82lohw), `devlist:rtn30pj4fjl70m6f0rzzmt8gml82lohw`)

**Result posted in a separate thread on 2026-07-14:** [[RESULT][VOTE] Release Apache Iceberg Rust 0.10.0 RC3](https://lists.apache.org/thread/fymfyn86yr1zzhlc3l1fb3j27o5v5t75) (`devlist:fymfyn86yr1zzhlc3l1fb3j27o5v5t75`). Outcome read from that message: passed.

## Positions

- **[[person/mbutrovich|Matt Butrovich]]:** The candidate verifies on macOS and DataFusion Comet CI, which runs Iceberg Java 1.10 Spark tests against iceberg-rust, is green with it. ([message](https://lists.apache.org/thread/1rsn9dkdr3rn12krz9z7f4sn5zor1166))
- **[[person/kevinjqliu|Kevin Liu]]:** The candidate passes the checklist; bindings/python/.venv/ and .pytest_cache/ should be added to the ignore list in .licenserc.yaml. ([message](https://lists.apache.org/thread/ml7h653yvy5wn8jkvgl4qdlh9wc612jn))
- **[[person/kevinjqliu|Kevin Liu]]:** Three crates are missing LICENSE and NOTICE files and should not be published that way, so the vote changes to -1 and a new RC is needed. ([message](https://lists.apache.org/thread/rtn30pj4fjl70m6f0rzzmt8gml82lohw))

References: [iceberg-rust#2823](https://github.com/apache/iceberg-rust/issues/2823)
<!-- kb:generated:end -->

## Notes
