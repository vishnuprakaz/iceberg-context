---
id: thread/t-3f1ab71baa4cf070
type: thread
title: Spark versioning strategy with accelerated Spark releases
date: '2026-06-01'
url: https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl
kind: discuss
status: consensus
messages: 11
sources:
- devlist:6kmh92wl6qkw08dpgv04bl51v590phbl
refs:
- gh:apache/iceberg#16397
- gh:apache/iceberg#14984
- doc:1gBoZ4KH5zQUWpgK3M7zAN7p6Glz4S_e9bO3PvQA9sQs
links:
- rel: started_by
  to: person/anuragmantri
  confidence: observed
updated: '2026-11-13'
---

# Spark versioning strategy with accelerated Spark releases

<!-- kb:generated:start -->
**Thread:** [[Discuss] Spark versioning strategy with accelerated Spark releases.](https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl) · **Started:** 2026-06-01 by [[person/anuragmantri|Anurag Mantripragada]] · **Messages:** 11 (last 2026-06-17) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

anuragmantri asked how Iceberg should support Spark versions now that Spark plans quarterly minor releases with six-month maintenance and a yearly LTS. Main supports 3.5, 4.0 and 4.1, and CI is already a bottleneck, so he suggested at most three versions and two policy options: the LTS plus a rolling window of the two latest minors, or the LTS plus selected minors. szehon-ho explained that Spark promises no breaking public API changes within a major version, so one Iceberg-Spark jar could in theory run on later minors, but verifying that needs CI. pan3793 doubted this because Iceberg uses Spark internal Catalyst APIs with no compatibility guarantee. The discussion settled on the LTS plus the two latest minors. Participants agreed to merge Spark 4.2 support first and then vote on removing Spark 4.0; aokolnychyi agreed and said a module per Spark version remains necessary.

**Why it matters:** It sets expectations for which Spark versions Iceberg adds and drops as Spark moves to quarterly minors, which affects users' upgrade paths and CI load.

## Outcome

Participants converged on supporting the last Spark LTS plus the two latest minors, merging Spark 4.2 support first and then holding a separate vote to remove Spark 4.0. ([message](https://lists.apache.org/thread/o27vy0wbojp0yorns09kng8nmks8xzzj), `devlist:o27vy0wbojp0yorns09kng8nmks8xzzj`)

## Positions

- **[[person/anuragmantri|Anurag Mantripragada]]:** Adopt an explicit policy with at most three Spark versions, restricted to one LTS and two minors because of CI limits. ([message](https://lists.apache.org/thread/8t1otyz8r1tq5qjfp0pqg6vyv60x823f))
- **[[person/szehon-ho|Szehon Ho]]:** A jar built for one minor would in theory work on later minors of the same major, but given CI limits and lack of confidence the LTS plus two latest minors is more likely. ([message](https://lists.apache.org/thread/rz6fnbd5b6b0pcr61yhqwn75t0rkbnxs))
- **[[person/pan3793|Cheng Pan]]:** Cross-minor compatibility cannot be relied on because Iceberg uses internal Catalyst APIs; LTS plus two minors is reasonable if Iceberg releases about every three months, and 4.2 support should merge before a vote on dropping 4.0. ([message](https://lists.apache.org/thread/qgp9zs3z4y2cc7pltx83prgxd7f8hrt2))
- **[[person/aokolnychyi|Anton Okolnychyi]]:** A module per Spark version is still needed because of reliance on Spark internals; LTS plus a rolling window of two minors is reasonable. ([message](https://lists.apache.org/thread/z7jhm8dl7bm2h7gzglqp43sk802pbw67))

References: [iceberg#16397](https://github.com/apache/iceberg/issues/16397), [iceberg#14984](https://github.com/apache/iceberg/issues/14984), [doc](https://docs.google.com/document/d/1gBoZ4KH5zQUWpgK3M7zAN7p6Glz4S_e9bO3PvQA9sQs)
<!-- kb:generated:end -->

## Notes
