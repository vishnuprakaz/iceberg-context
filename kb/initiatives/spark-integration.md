---
id: initiative/spark-integration
type: initiative
title: Spark integration and version support
status: implementing
updated: '2026-11-13'
sources:
- thread/t-e6327b02ad166780
- meeting/spark/2026-05-19
- thread/t-3f1ab71baa4cf070
- thread/t-a59bca208d82363d
- meeting/spark/2026-06-16
- meeting/spark/2026-07-21
- thread/t-1f7d78172b69f87c
- meeting/spark/2026-08-18
- meeting/community/2026-09-16
- thread/t-8e05ea5cfb5440f5
- thread/t-b00cc9ec1c194566
- meeting/community/2026-10-07
- meeting/spark/2026-10-20
- thread/t-4ba0b50d52976551
- meeting/spark/2026-11-11
links:
- rel: championed_by
  to: person/anuragmantri
  confidence: extracted
  source: thread/t-3f1ab71baa4cf070
- rel: championed_by
  to: person/kevinjqliu
  confidence: extracted
  source: thread/t-e6327b02ad166780
- rel: championed_by
  to: person/amogh-jahagirdar
  confidence: extracted
  source: thread/t-1f7d78172b69f87c
- rel: handled_by
  to: group/spark
  confidence: extracted
  source: meeting/spark/2026-11-11
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/spark/2026-11-11
- rel: tracked_in
  to: gh:apache/iceberg#17959
  confidence: extracted
  source: meeting/spark/2026-11-11
- rel: tracked_in
  to: gh:apache/iceberg#14984
  confidence: extracted
  source: meeting/spark/2026-07-21
---

# Spark integration and version support

<!-- kb:generated:start -->
## What it is

The Spark connector in the Iceberg Java repository, which is kept as one module per supported Spark version ([thread, 2026-06-01](../records/threads/2026/06/discuss-spark-versioning-strategy-with-accelerated-spark-releases-3f1ab7.md); [dev list](https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl)). This page tracks which Spark versions Iceberg supports, the adoption of new Spark DataSource V2 APIs, the cost of carrying several version copies, and Spark-specific defaults and fixes ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Current state

- Version policy: the dev list converged on supporting the last Spark LTS plus the two latest minors, merging Spark 4.2 support first and then holding a separate vote on removing Spark 4.0 ([thread, 2026-06-01](../records/threads/2026/06/discuss-spark-versioning-strategy-with-accelerated-spark-releases-3f1ab7.md); [dev list](https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl)). Whether to keep 3.5 and 4.0 for longer was asked again later with no recorded outcome ([Community Sync, 2026-10-07](../records/meetings/community/2026/2026-10-07.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Spark 3.4 is removed; 1.11.0 is the last Iceberg version supporting it ([thread, 2025-09-17](../records/threads/2025/09/discuss-deprecating-spark-3-4-e6327b.md); [dev list](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv)).
- Spark 4.2: support ([#14984](https://github.com/apache/iceberg/pull/14984)) is listed among Java highlights ([Community Sync, 2026-09-16](../records/meetings/community/2026/2026-09-16.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), but 4.2 was deliberately excluded from the 1.12.0 convenience binaries ([#18024](https://github.com/apache/iceberg/pull/18024)) because Spark APIs were still evolving ([thread, 2026-09-25](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-8e05ea.md); [dev list](https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77)). Remaining items are tracked in [#17959](https://github.com/apache/iceberg/pull/17959); what gates publishing 4.2 and who owns each missing piece is an open question ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)). Whether the 4.2 jar should be targeted with 1.13 has no recorded answer ([Spark Community Sync, 2026-10-20](../records/meetings/spark/2026/2026-10-20.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Spark 4.3: the pull request adding it ([#18749](https://github.com/apache/iceberg/pull/18749)) is a 661-file copy; whether to skip 4.3, add it, or certify the 4.2 module on it is undecided ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)). Variant extraction pushdown needs Spark 4.3 for its full story ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Shared Spark source: every Spark minor is a full copy of the spark/ tree. A first proof of concept shared 88% of files through per-version shims ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)); a newer approach drops the shim layer and keeps only byte-identical files in spark/common/, with a build check ([Spark Community Sync, 2026-10-20](../records/meetings/spark/2026/2026-10-20.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Streaming default: all replies supported switching Spark streaming writes from fast append to merging append by default in 1.13 ([thread, 2026-07-30](../records/threads/2026/07/discuss-changing-the-default-append-mode-for-spark-streaming-in-iceber-1f7d78.md); [dev list](https://lists.apache.org/thread/sk1j4jo6s7ntr880tt7ktdt636nwzt5n)); merge append as the default for streaming writes is listed as merged ([Spark Community Sync, 2026-10-20](../records/meetings/spark/2026/2026-10-20.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Unreleased fixes: two silent-data-loss fixes ([#18005](https://github.com/apache/iceberg/pull/18005), [#18348](https://github.com/apache/iceberg/pull/18348)) are in no release; whether to do a 1.12.1 or ship them in 1.13 is open ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Sort order: MergingSortedRowDataReader landed for Spark 4.1 ([#14948](https://github.com/apache/iceberg/pull/14948)) ([Spark Community Sync, 2026-10-20](../records/meetings/spark/2026/2026-10-20.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)); SupportsReportOrdering and the k-way merge rewrite strategy are still in the review queue ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- CI: parallel Spark test execution cut the run from about 84 to 58 minutes ([Spark Community Sync, 2026-06-16](../records/meetings/spark/2026/2026-06-16.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)); pull requests selecting the Spark and Flink matrix by changed version were listed ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 1.13: a release manager is named; the date (end of year or early January) and the Spark 4.2 scope are not settled ([thread, 2026-09-30](../records/threads/2026/09/discuss-iceberg-1-13-release-java-b00cc9.md); [dev list](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc)).

## Timeline

- 2025-09-17: Thread proposes deprecating Spark 3.4; the removal ([#14122](https://github.com/apache/iceberg/pull/14122)) is merged in May 2026 ([thread, 2025-09-17](../records/threads/2025/09/discuss-deprecating-spark-3-4-e6327b.md); [dev list](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv)).
- 2026-05-19: Spark sync proposes a matrix of 3.5, 4.1 and 4.2 with 4.0 removed; no decision ([Spark Community Sync, 2026-05-19](../records/meetings/spark/2026/2026-05-19.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-06-01: Thread on Spark versioning with accelerated Spark releases; converges on LTS plus two latest minors ([thread, 2026-06-01](../records/threads/2026/06/discuss-spark-versioning-strategy-with-accelerated-spark-releases-3f1ab7.md); [dev list](https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl)).
- 2026-06-05: 1.12.0 planning: Spark 4.2 support is taken off the milestone, to be merged but excluded from release artifacts ([thread, 2026-06-05](../records/threads/2026/06/discuss-apache-iceberg-1-12-0-release-a59bca.md); [dev list](https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q)).
- 2026-06-16: Spark sync reports Spark 3.4 removed, Spark 4.1 upgraded to 4.1.2 and parallel Spark tests merged ([Spark Community Sync, 2026-06-16](../records/meetings/spark/2026/2026-06-16.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-07-21: Spark 4.2 is released and the pull request adding Spark 4.2.0 support ([#14984](https://github.com/apache/iceberg/pull/14984)) is up for review ([Spark Community Sync, 2026-07-21](../records/meetings/spark/2026/2026-07-21.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-07-30: Thread proposes merging append as the Spark streaming default in 1.13 ([thread, 2026-07-30](../records/threads/2026/07/discuss-changing-the-default-append-mode-for-spark-streaming-in-iceber-1f7d78.md); [dev list](https://lists.apache.org/thread/sk1j4jo6s7ntr880tt7ktdt636nwzt5n)).
- 2026-08-18: Spark sync: Spark candidates for 1.12 go in if ready and otherwise move to 1.13; a freeze-then-merge plan for the 4.2 pull request was agreed on 13 August; first shared-source proof of concept ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-09-16: Spark 4.2.0 support is listed among Java highlights ([Community Sync, 2026-09-16](../records/meetings/community/2026/2026-09-16.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-09-25: 1.12.0 RC2 vote: no Spark 4.2 artifacts are staged, on purpose ([thread, 2026-09-25](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-8e05ea.md); [dev list](https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77)).
- 2026-09-30: 1.13 release thread; Spark 4.2 support is on the wish list ([thread, 2026-09-30](../records/threads/2026/09/discuss-iceberg-1-13-release-java-b00cc9.md); [dev list](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc)).
- 2026-10-20: Spark sync: CREATE TABLE LIKE and schema evolution for Spark 4.2 merged, merge append default for streaming writes merged, new shared-source approach ([Spark Community Sync, 2026-10-20](../records/meetings/spark/2026/2026-10-20.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-10-28: Thread on using the catalog's Hadoop configuration when listing orphan files; [#17862](https://github.com/apache/iceberg/pull/17862) is reworked to use the table FileIO's configuration with no new API ([thread, 2026-10-28](../records/threads/2026/10/discuss-spark-use-the-catalog-s-hadoop-configuration-when-listing-orph-4ba0b5.md); [dev list](https://lists.apache.org/thread/5f40shqmwc2l647oskjg1vv8pq7q8od7)).
- 2026-11-11: Spark sync: 1.12.1 question, Spark 4.2 pending items, Spark 4.3 options, wrong-result bugs needing reviewers ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Where help is needed

- A set of wrong-result bugs needs reviewers and an owner each ([#18557](https://github.com/apache/iceberg/pull/18557), [#18617](https://github.com/apache/iceberg/pull/18617), [#18824](https://github.com/apache/iceberg/pull/18824), [#18621](https://github.com/apache/iceberg/pull/18621), [#18622](https://github.com/apache/iceberg/pull/18622), [#18738](https://github.com/apache/iceberg/pull/18738)) ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- The DSv2 Transaction API pull request for Spark 4.2 has no reviews (inferred to be [#18385](https://github.com/apache/iceberg/pull/18385), the second reference on that agenda item) ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Reviews were requested for SupportsReportOrdering ([#16750](https://github.com/apache/iceberg/pull/16750)), the k-way merge rewrite strategy ([#16305](https://github.com/apache/iceberg/pull/16305)) and selective shredded variant extraction readers ([#16714](https://github.com/apache/iceberg/pull/16714)), among others ([Spark Community Sync, 2026-11-11](../records/meetings/spark/2026/2026-11-11.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
<!-- kb:generated:end -->

## Notes
