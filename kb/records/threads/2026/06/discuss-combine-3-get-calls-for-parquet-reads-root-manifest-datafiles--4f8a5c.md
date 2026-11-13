---
id: thread/t-4f8a5ccaf1b60f7d
type: thread
title: Combining the three GET calls for small Parquet file reads
date: '2026-06-08'
url: https://lists.apache.org/thread/yb8nom3w2zplb703m0p052kcc1wwotrr
kind: discuss
status: open
messages: 13
sources:
- devlist:yb8nom3w2zplb703m0p052kcc1wwotrr
refs:
- gh:apache/iceberg#16729
- gh:apache/iceberg#15470
- gh:apache/iceberg#16910
- doc:13shy0RWotwfWC_qQksb95PXdi-vSUCKQyDzjoExQEN0
- list:jz4534dodn0zhwdg2wojwkkohg2dps9p
- list:cy6y5xf5gg8fr12pg64f77gxdrtv52fn
links:
- rel: discussed
  to: initiative/v4-metadata-tree
  confidence: extracted
  source: devlist:yb8nom3w2zplb703m0p052kcc1wwotrr
- rel: started_by
  to: person/varun-lakhyani
  confidence: observed
updated: '2026-11-13'
---

# Combining the three GET calls for small Parquet file reads

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Combine 3 GET calls for parquet reads - Root Manifest, Datafiles and compaction of small files](https://lists.apache.org/thread/yb8nom3w2zplb703m0p052kcc1wwotrr) · **Started:** 2026-06-08 by [[person/varun-lakhyani|Varun Lakhyani]] · **Messages:** 13 (last 2026-06-29) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Varun Lakhyani pointed out that the Spark read path with parquet-mr issues three S3 GET requests per file scan task (footer size, footer, row group) and proposed fetching small files whole in a single GET, either in Iceberg (PR #16729, an EagerInputFile wrapper) or upstream in parquet-mr. His first benchmark showed a 60-65% improvement. Russell Spitzer called the idea critical for the V4 root manifest and index work. Steve Loughran asked for benchmarks against the AWS analytics accelerator (AAL) and for request counts from S3 logs. Daniel Weeks preferred improving the native implementation over relying on the accelerator, and Danny Jones of the S3 team agreed. The follow-up benchmark on EC2 showed about 40-42% improvement over the default and 8-10% over AAL, with one request per file instead of three (default) or two (AAL). Loughran concluded the speedup holds and listed reviews needed, including the PR and work on keeping file sizes in manifests correct. The thread ends without a decision on the PR.

**Why it matters:** Small-file read latency matters for V4, where root manifests and index files are small Parquet files read on the planning path.

## Outcome

No decision was recorded. The last message recommends reviewing PR #16729 for small files, the PR wiring AAL vector reads, and the changes that keep file sizes in manifests correct.

## Positions

- **[[person/varun-lakhyani|Varun Lakhyani]]:** Small files below a threshold should be fetched whole in one GET through a format-independent EagerInputFile wrapper, which also works for object stores other than S3. ([message](https://lists.apache.org/thread/qwy6d50s8n9vyftd28ldxdzwr1o4d54k))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Serial GET requests on small files hurt the V4 root manifest and index work, so an Iceberg-first solution is of interest, though Parquet Java could also support the pattern. ([message](https://lists.apache.org/thread/mpmklm0o5qo654zpp00o7mqpp7q7d3cz))
- **[[person/danielcweeks|Daniel C. Weeks]]:** IO performance is worth investing in, but a Parquet-specific path may not be the right one, and encryption and metrics at the FileIO layer have to be considered. ([message](https://lists.apache.org/thread/xc2yslqh90ygf4n2hj2nn5bynk5f8s6v))
- **[[person/steveloughran|Steve Loughran]]:** The change should be benchmarked against the AWS analytics accelerator stream, and vector read support should be wired through Iceberg, before adding further optimizations. ([message](https://lists.apache.org/thread/rcnyh3sv60fgnc1rqtpkx4jvxyqj78qh))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Iceberg should not rely too much on the analytics accelerator, which has hidden request and memory tradeoffs; a solution that works across implementations is a good improvement. ([message](https://lists.apache.org/thread/nr5jfblqqq9w3y2yz0gs2yvvsgnwzmqs))
- **Danny Jones:** Optimizations upstream in iceberg-java or parquet-mr are welcome so all users benefit, with the accelerator as an opt-in for S3 workloads in the meantime. ([message](https://lists.apache.org/thread/qz983yohy42mmgy7k8r2kthm7hxborh3))
- **[[person/steveloughran|Steve Loughran]]:** The benchmark shows a real but smaller speedup against the accelerator; the PR, the vector read PR and work on correct file sizes in manifests should all be reviewed. ([message](https://lists.apache.org/thread/gwmdy9fj4vd23slcbzc3hqmcvy9kq2x9))

References: [iceberg#16729](https://github.com/apache/iceberg/issues/16729), [iceberg#15470](https://github.com/apache/iceberg/issues/15470), [iceberg#16910](https://github.com/apache/iceberg/issues/16910), [doc](https://docs.google.com/document/d/13shy0RWotwfWC_qQksb95PXdi-vSUCKQyDzjoExQEN0), [thread](https://lists.apache.org/thread/jz4534dodn0zhwdg2wojwkkohg2dps9p), [thread](https://lists.apache.org/thread/cy6y5xf5gg8fr12pg64f77gxdrtv52fn)
<!-- kb:generated:end -->

## Notes
