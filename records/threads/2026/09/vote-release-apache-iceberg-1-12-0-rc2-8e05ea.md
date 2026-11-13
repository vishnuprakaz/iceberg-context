---
id: thread/t-8e05ea5cfb5440f5
type: thread
title: Release Apache Iceberg 1.12.0 RC2
date: '2026-09-25'
url: https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77
kind: release-vote
status: passed
messages: 18
sources:
- devlist:l8gjs6z1ocfd70hv6dj923s7p9qm0w77
- devlist:ychjvqbmt7ksmczhct3mnw8j3yowwbcr
refs:
- gh:apache/iceberg#14984
- gh:apache/iceberg#18024
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:l8gjs6z1ocfd70hv6dj923s7p9qm0w77
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:l8gjs6z1ocfd70hv6dj923s7p9qm0w77
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Release Apache Iceberg 1.12.0 RC2

<!-- kb:generated:start -->
**Thread:** [[VOTE] Release Apache Iceberg 1.12.0 RC2](https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77) · **Started:** 2026-09-25 by [[person/nssalian|Neelesh Salian]] · **Messages:** 18 (last 2026-09-29) · **Outcome:** passed

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

nssalian proposed release candidate 2 (commit 212aa894, tag apache-iceberg-1.12.0-rc2) as Apache Iceberg 1.12.0, with voting open until September 29, 2026, 2:00 pm Pacific. Voters verified signatures, checksums, licenses, builds and tests. huaxingao noticed that no Spark 4.2 artifacts were staged because dev/stage-binaries.sh lists only Spark 3.5, 4.0 and 4.1, and suggested another RC; amogh-jahagirdar initially agreed. nssalian and RussellSpitzer pointed out that PR #18024 had excluded 4.2 from convenience binaries on purpose, and amogh-jahagirdar found the earlier thread explaining that 4.2 development continues but is not released because Spark APIs were still evolving. huaxingao withdrew the concern and voted +1, confirming that the LICENSE findings from RC1 and the variant NoSuchMethodError were fixed. The bundle contains no result message.

**Why it matters:** Iceberg 1.12.0 ships Spark 4.2 source but deliberately no Spark 4.2 convenience binaries.

## Outcome

No result message is in the thread. The messages show +1 votes only: one marked binding (RussellSpitzer) and nine marked non-binding; no -1 votes.

**Result posted in a separate thread on 2026-09-29:** [[RESULT][VOTE] Release Apache Iceberg 1.12.0 RC2](https://lists.apache.org/thread/ychjvqbmt7ksmczhct3mnw8j3yowwbcr) (`devlist:ychjvqbmt7ksmczhct3mnw8j3yowwbcr`). Outcome read from that message: passed.

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** Raised that Spark 4.2 artifacts were missing from staging and another RC might be needed, then withdrew the concern after recalling that 4.2 was intentionally not released. ([message](https://lists.apache.org/thread/gyfmws5x8wng91365o629chsw0qt9w6c))
- **[[person/nssalian|Neelesh Salian]]:** Asked for clarification before cutting another RC, citing the review comment on the Spark 4.2 PR about 4.2 support in 1.12. ([message](https://lists.apache.org/thread/491c0065os0fsnsqny9vjhf0g4hg4o2y))
- **[[person/RussellSpitzer|Russell Spitzer]]:** PR #18024 explicitly excluded Spark 4.2 from convenience binaries, and the staged artifacts are good excluding 4.2 as expected. ([message](https://lists.apache.org/thread/bzbzx236nhjy9vzvvkgm2mv3w7xqjj1v))
- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Excluding Spark 4.2 was intentional so development could continue while its release was in doubt due to evolving Spark APIs. ([message](https://lists.apache.org/thread/op2plh6m7893m5o0gnrs288v1f9qpnm7))

References: [iceberg#14984](https://github.com/apache/iceberg/issues/14984), [iceberg#18024](https://github.com/apache/iceberg/issues/18024)
<!-- kb:generated:end -->

## Notes
