---
id: thread/t-e2b669d1053d1cbb
type: thread
title: Release Apache Iceberg 1.12.0 RC1
date: '2026-09-22'
url: https://lists.apache.org/thread/ptq6gyf6gcd4xwwkn2q3yrt9lxr7ojdk
kind: release-vote
status: open
messages: 8
sources:
- devlist:ptq6gyf6gcd4xwwkn2q3yrt9lxr7ojdk
refs:
- gh:apache/iceberg#18164
- gh:apache/iceberg#18069
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:ptq6gyf6gcd4xwwkn2q3yrt9lxr7ojdk
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg 1.12.0 RC1

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.12.0 RC1](https://lists.apache.org/thread/ptq6gyf6gcd4xwwkn2q3yrt9lxr7ojdk) · **Started:** 2026-09-22 by [[person/nssalian|Neelesh Salian]] · **Messages:** 8 (last 2026-09-22) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

nssalian proposed release candidate 1 (commit e8d0f0f3, tag apache-iceberg-1.12.0-rc1) as Apache Iceberg 1.12.0, with a 72-hour vote. Voters verified checksums, signatures, licenses and builds. GGraziadei voted +1 and repeated a finding from RC0: reading variant columns throws NoSuchMethodError when commons-lang3 older than 3.13 is on the classpath, because iceberg-parquet uses Streams.of(Iterable) without declaring the dependency. It also exists in 1.11.0, is tracked in issue #18164, and he asked for the fix to be included if a new RC is made. nssalian replied that since it is not a regression it can be patched into the respective branches after the release. szehon-ho asked that PR #18069, another pre-existing issue, be included if there is another RC, and voted +1. The bundle contains no result message for this RC.

## Outcome

No result message is in the thread. The messages show +1 votes only: one marked binding (liurenjie1024), three marked non-binding and one unmarked; no -1 votes.

## Positions

- **[[person/GGraziadei|Gianluca Graziadei]]:** Votes +1; the variant NoSuchMethodError with commons-lang3 older than 3.13 is not a regression and should not block, but the fix should be included if a new RC is cut. ([message](https://lists.apache.org/thread/qy8pj2rdojo2kybds2dj0z21flsxmb6x))
- **[[person/nssalian|Neelesh Salian]]:** Because the issue is not a regression and depends on the commons-lang3 version, it can be fixed with a patch to the respective branches after the release. ([message](https://lists.apache.org/thread/9ovw5bv8gm3fdlqv38dtb7bv73zfj5fr))
- **[[person/szehon-ho|Szehon Ho]]:** PR #18069 fixes another pre-existing issue that is not worth stopping this RC for but should be included if another RC is made. ([message](https://lists.apache.org/thread/fqytwbgt9c3ccgjlj5gzf59t1p4yd2pk))

References: [iceberg#18164](https://github.com/apache/iceberg/issues/18164), [iceberg#18069](https://github.com/apache/iceberg/issues/18069)
<!-- kb:generated:end -->

## Notes
