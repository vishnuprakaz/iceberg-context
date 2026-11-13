---
id: thread/t-95092e2c0cd7ae07
type: thread
title: Flink version support after Iceberg 1.11.0
date: '2026-05-26'
url: https://lists.apache.org/thread/kd183vz2v2y69v4kwbz5wbjfxvx3gf1f
kind: discuss
status: no-conclusion
messages: 11
sources:
- devlist:kd183vz2v2y69v4kwbz5wbjfxvx3gf1f
refs:
- gh:apache/iceberg#16517
- gh:apache/iceberg#15476
- gh:apache/iceberg#13714
links:
- rel: discussed
  to: initiative/flink-integration
  confidence: extracted
  source: devlist:kd183vz2v2y69v4kwbz5wbjfxvx3gf1f
- rel: started_by
  to: person/stevenzwu
  confidence: observed
updated: '2026-11-13'
---

# Flink version support after Iceberg 1.11.0

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Flink version support after Iceberg 1.11.0](https://lists.apache.org/thread/kd183vz2v2y69v4kwbz5wbjfxvx3gf1f) · **Started:** 2026-05-26 by [[person/stevenzwu|Steven Wu]] · **Messages:** 11 (last 2026-05-29) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Steven Wu raised the question from PR #16517 of which Flink versions the next Iceberg release should support. He proposed keeping Flink 1.20, an LTS release, dropping 2.0 instead, and skipping 2.2 in favor of 2.3. Jacky Lee reported that the Flink connector community mainly maintains 2.0 and 2.2 and that 2.1 is effectively skipped, so 2.2 should take priority. Steven revised the plan: Iceberg 1.11.0 supports Flink 1.20, 2.0 and 2.1; 1.12.0 would support 1.20, 2.2 and 2.3. Talat Uyarer offered to refresh his Flink 2.2 PR and drop 2.0. Péter Váry was concerned the matrix forces users to upgrade Flink and Iceberg together, and Yu Guo suggested temporarily supporting four Flink versions in 1.12. Maximilian Michels backed LTS plus the two latest releases and floated supporting more versions with a leaner build. Cheng Pan noted Iceberg release cycles are longer than Flink's. The thread ends without a stated resolution of the upgrade-path concern.

**Why it matters:** It determines which Flink runtimes ship with Iceberg 1.12.0 and whether Flink users can upgrade Iceberg without changing Flink version.

## Outcome

There was broad support for keeping Flink 1.20 and adding 2.2 and 2.3 for Iceberg 1.12.0, but the concern about forcing simultaneous Flink and Iceberg upgrades and the proposal to support four versions were left unanswered.

## Positions

- **[[person/stevenzwu|Steven Wu]]:** Keep the Flink 1.20 LTS and the two latest Flink releases; the revised matrix for Iceberg 1.12.0 is Flink 1.20, 2.2 and 2.3, dropping 2.1 when 2.3 is added. ([message](https://lists.apache.org/thread/7yr3ogol6h01d8rg07q19yv6wq370yyy))
- **Jacky Lee:** Retain 1.20, prioritize Flink 2.2 because the Flink connector community maintains 2.0 and 2.2 and skips 2.1, and add 2.3 once it is released. ([message](https://lists.apache.org/thread/yb61tyd9vxk62znrqtlfk7ts1wscj5l6))
- **[[person/kevinjqliu|Kevin Liu]]:** Publish an iceberg-flink-runtime for each Flink release even if only for one Iceberg release, and mark dropped versions as deprecated on the multi-engine support page. ([message](https://lists.apache.org/thread/mykj84w2h383xymofh3v40h5rycrq6km))
- **[[person/talatuyarer|Talat UYARER]]:** Keep Flink 1.20 because the move to 2.0 is a significant change, drop 2.0 and add 2.2 by refreshing his earlier PR. ([message](https://lists.apache.org/thread/p74p08or09q02vhql077o3to07o8vv4h))
- **[[person/pvary|Peter Vary]]:** The proposed matrix forces users to upgrade Flink and Iceberg at the same time, whereas upgrades are better done one change at a time. ([message](https://lists.apache.org/thread/1hr661vrp0mlkg7wtxpm3l1yhpp6rcby))
- **[[person/mxm|Maximilian Michels]]:** Supports LTS plus the two latest Flink releases; more than three versions could be supported if the build matrix is tuned, and older versions might be kept as a diff against the latest. ([message](https://lists.apache.org/thread/zqcg1w1plp9smqf4by6drt64nk69nv36))
- **Yu Guo:** Temporarily support four Flink versions in Iceberg 1.12 (1.20, 2.1, 2.2, 2.3) to ease upgrades, and document which features are unavailable on Flink 1.20. ([message](https://lists.apache.org/thread/j8vcj3rnmhl8f45o4dtljpg3bm7lkv9p))
- **[[person/pan3793|Cheng Pan]]:** Because Iceberg release cycles are longer than Flink's, the assumption of maintaining three versions will eventually break. ([message](https://lists.apache.org/thread/44vjyw3tlbsdobodvfdsgt5952sh2o44))

References: [iceberg#16517](https://github.com/apache/iceberg/issues/16517), [iceberg#15476](https://github.com/apache/iceberg/issues/15476), [iceberg#13714](https://github.com/apache/iceberg/issues/13714)
<!-- kb:generated:end -->

## Notes
