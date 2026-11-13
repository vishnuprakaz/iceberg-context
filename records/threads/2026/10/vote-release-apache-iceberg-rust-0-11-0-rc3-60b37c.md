---
id: thread/t-60b37c70a0f57b2a
type: thread
title: Vote on releasing Apache Iceberg Rust 0.11.0 RC3
date: '2026-10-29'
url: https://lists.apache.org/thread/x1mlyjg7xlmkc9hqb1w8x8r97ovb1smq
kind: release-vote
status: passed
messages: 10
sources:
- devlist:x1mlyjg7xlmkc9hqb1w8x8r97ovb1smq
refs:
- list:bvnhbx81620ho11vo1nyps3pnp9x0bth
- list:rfc6bc7lq1xllv2hd4sy80qy39d1vlcc
links:
- rel: started_by
  to: person/dannycjones
  confidence: observed
updated: '2026-11-13'
---

# Vote on releasing Apache Iceberg Rust 0.11.0 RC3

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg Rust 0.11.0 RC3](https://lists.apache.org/thread/x1mlyjg7xlmkc9hqb1w8x8r97ovb1smq) · **Started:** 2026-10-29 by [[person/dannycjones|Daniel Carl Jones]] · **Messages:** 10 (last 2026-11-03) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Danny Jones called a vote to release Apache Iceberg Rust 0.11.0 from tag v0.11.0-rc.3. He noted that the pyiceberg-core bindings now include third-party attribution notices, and the verification checklist gained an item for checking those notices in the produced wheels. Voters reported verifying signatures and checksums, that the source archive matches the tag, license files and headers, the Rust build and tests, and the pyiceberg-core build, tests and wheel notices. Four days in, the release manager said binding votes were still needed. Kevin Liu then voted and also checked that all crates can be published. The release manager announced that the vote passed and linked a separate result thread.

**Why it matters:** Iceberg Rust 0.11.0 was approved for release, with third-party attribution notices now part of the pyiceberg-core wheels and of release verification.

## Outcome

The release manager stated that the vote passed and pointed to a separate result thread; this thread does not give the vote counts. ([message](https://lists.apache.org/thread/k6mhthp778jxgctx94zoqwf8373s0d8r), `devlist:k6mhthp778jxgctx94zoqwf8373s0d8r`)

## Positions

- **[[person/szehon-ho|Szehon Ho]]:** Some .github files lack license headers, but this is consistent with other Apache repositories and is not an issue. ([message](https://lists.apache.org/thread/zf7qpw6syb5dl0z8795hb6lx0x3hmy84))
- **Danny Jones:** The candidate verifies on Linux x86_64, and the vote still needed binding votes at that point. ([message](https://lists.apache.org/thread/y6d7hldtwbq2hmyy4by1wly6yh4r9ggd))
- **[[person/kevinjqliu|Kevin Liu]]:** The candidate passes the checklist, all crates pass a publish dry run on the tag, and pyiceberg-core 0.11.0rc3 was tested against PyIceberg's integration tests. ([message](https://lists.apache.org/thread/v069f1cy7x5bm7g6tobqqkvc56816qzg))

References: [thread](https://lists.apache.org/thread/bvnhbx81620ho11vo1nyps3pnp9x0bth), [thread](https://lists.apache.org/thread/rfc6bc7lq1xllv2hd4sy80qy39d1vlcc)
<!-- kb:generated:end -->

## Notes
