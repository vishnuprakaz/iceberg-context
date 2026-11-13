---
id: thread/t-b00cc9ec1c194566
type: thread
title: Iceberg 1.13 release (Java)
date: '2026-09-30'
url: https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc
kind: release-planning
status: open
messages: 9
sources:
- devlist:mj8czb2ljf8kj1d7ldbfw39sffr9knjc
refs:
- gh:apache/iceberg#14984
- gh:apache/iceberg#17959
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:mj8czb2ljf8kj1d7ldbfw39sffr9knjc
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:mj8czb2ljf8kj1d7ldbfw39sffr9knjc
- rel: started_by
  to: person/anoopj
  confidence: observed
updated: '2026-11-13'
---

# Iceberg 1.13 release (Java)

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg 1.13 release (Java)](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc) · **Started:** 2026-09-30 by [[person/anoopj|Anoop Johnson]] · **Messages:** 9 (last 2026-09-30) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After 1.12 closed, Anoop (anoopj) opened the discussion on 1.13, proposing a release before the end of the year that includes early V4 work, and volunteered as release manager. Anurag Mantripragada had already volunteered for 1.13, so Anoop agreed to take 1.14. Anurag suggested early January because of the holiday season, with the V4 spec PR, related early work and Spark 4.2 support on his wish list; Russell Spitzer and Neelesh Salian also saw December as difficult. Dan (danielcweeks) said it is too early to rule out a release by year end, since releases need not be large. Xin Huang proposed that Spark 4.2 support cover existing Iceberg functionality, with new Spark features such as the Transactional API as best effort. No date or scope was settled.

**Why it matters:** It names the release managers for 1.13 and 1.14 and the candidate scope for 1.13: early V4 work and Spark 4.2 support.

## Outcome

Anurag Mantripragada is release manager for 1.13 and anoopj will take 1.14. The release date (end of year or early January) and the Spark 4.2 scope were not settled.

## Positions

- **[[person/anoopj|Anoop Johnson]]:** Get another release out before the end of the year with some early V4 work, and he volunteers as release manager. ([message](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc))
- **[[person/RussellSpitzer|Russell Spitzer]]:** A December release is usually difficult, and Anurag, who already volunteered, should coordinate 1.13. ([message](https://lists.apache.org/thread/p6fxbls9wbk215wwc4pl1wx6f7gtjood))
- **[[person/anuragmantri|Anurag Mantripragada]]:** He will manage 1.13 and suggests early January, with the V4 spec PR, related early work and Spark 4.2 support in scope. ([message](https://lists.apache.org/thread/x3cb59zf27d6jc6p5h3njcb1n53rc2ns))
- **[[person/huan233usc|Xin Huang]]:** If 1.13 includes Spark 4.2, it should support existing Iceberg functionality and treat integration with new Spark features such as the Transactional API as best effort. ([message](https://lists.apache.org/thread/dttx8o3998xo75120h32gskbgt29h18p))
- **[[person/danielcweeks|Daniel C. Weeks]]:** It is too early to discount a release by the end of the year; not every release needs to be large and several things missed the 1.12 cutoff. ([message](https://lists.apache.org/thread/sn7t3mtp05jvfhwjsf7jyooffp8cn6y5))
- **[[person/nssalian|Neelesh Salian]]:** The Spark 4.2 items in the tracking issue should be completed before deciding whether 1.13 or another release supports Spark 4.2. ([message](https://lists.apache.org/thread/3ol54o3lrd2p440g37ogn5lq8zw98wcp))

References: [iceberg#14984](https://github.com/apache/iceberg/issues/14984), [iceberg#17959](https://github.com/apache/iceberg/issues/17959)
<!-- kb:generated:end -->

## Notes
