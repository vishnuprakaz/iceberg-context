---
id: initiative/community-process
type: initiative
title: Community process, health and events
status: discussion
updated: '2026-11-13'
sources:
- thread/t-03ef420b5ad9206f
- meeting/community/2026-10-28
- thread/t-cf8ecdd2fd7d10db
- thread/t-d0d4a69708620931
- meeting/community/2026-10-07
- thread/t-af00f4d1a06fa71b
- meeting/community/2026-09-16
- thread/t-97adb77b6cd93c6b
- thread/t-7ff555b89c73c647
- meeting/community/2026-06-03
- meeting/spark/2026-06-16
- meeting/read-restrictions/2026-09-15
- meeting/file-vector-type/2026-11-05
- meeting/community/2026-05-13
- thread/t-89ed0cd9b2602f90
- meeting/community/2026-07-15
- meeting/community/2026-08-05
- thread/t-914ce4905899b010
- thread/t-e3a4cbb57895e29d
- meeting/index/2026-11-09
links:
- rel: championed_by
  to: person/kevinjqliu
  source: thread/t-89ed0cd9b2602f90
  confidence: extracted
- rel: championed_by
  to: person/sungwy
  source: thread/t-914ce4905899b010
  confidence: extracted
- rel: championed_by
  to: person/RussellSpitzer
  source: thread/t-03ef420b5ad9206f
  confidence: extracted
- rel: championed_by
  to: person/pvary
  source: thread/t-97adb77b6cd93c6b
  confidence: extracted
- rel: handled_by
  to: group/community
  source: meeting/community/2026-10-28
  confidence: extracted
---

# Community process, health and events

<!-- kb:generated:start -->
## What it is

This page collects how the Apache Iceberg community runs itself, as opposed to what it builds: reviewer capacity and contributor retention, CI resources, how releases and spec changes are announced, and events such as the Iceberg Summit and meetups. These topics come up on the dev list and at the community sync ([thread summary](../records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md), [dev list](https://lists.apache.org/thread/s5jqhbczoknftmojhrvzpsb53w1s7gd6), [community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).

## Current state

- Community health: Russell Spitzer shared a dashboard built from GitHub and dev list data. It shows first-to-second contribution retention trending down, 68% of pull requests labelled stale against a median time to merge of 34 hours, and 45% of last month's dev list threads unanswered. He offered no prescriptions and plans monthly updates ([thread summary](../records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md), [dev list](https://lists.apache.org/thread/s5jqhbczoknftmojhrvzpsb53w1s7gd6), [community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Reviewer bandwidth: a May thread agreed it is a bottleneck across Iceberg projects, with no change decided; replies pointed to building trust through contributions and reviews ([thread summary](../records/threads/2026/05/discuss-reviewer-bandwidth-in-iceberg-rust-cf8ecd.md), [dev list](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r)).
- Iceberg Summit 2027: the PMC approved the proposal, the Selection Committee has been finalized (members not named in the thread) and the call for papers was mentioned at the 2026-10-07 sync ([thread summary](../records/threads/2026/09/discuss-iceberg-summit-2027-selection-committee-d0d4a6.md), [dev list](https://lists.apache.org/thread/hk1gnjrqnfvmjknrsyyphfs6mfxkz20s), [community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- Virtual meetups: all replies supported monthly virtual meetups free of marketing material ([thread summary](../records/threads/2026/08/discuss-virtual-community-meetups-and-showcases-af00f4.md), [dev list](https://lists.apache.org/thread/4fnks078pwlgoyhckjvonvm6dgo0ywc8)); the 2026-09-16 sync notes open with the Apache Iceberg Virtual Meetup Series ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md)).
- Spec changes in release notes: everyone who replied agreed that spec changes should leave the Java release notes ([thread summary](../records/threads/2026/10/discuss-spec-changes-in-release-notes-97adb7.md), [dev list](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl)). Two alternative pull requests, [apache/iceberg#18349](https://github.com/apache/iceberg/pull/18349) and [apache/iceberg#18379](https://github.com/apache/iceberg/pull/18379), were offered and no outcome is recorded ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)). A separate iceberg-format repository drew one supporter and strong opposition ([thread summary](../records/threads/2026/10/discuss-spec-changes-in-release-notes-7ff555.md), [dev list](https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j)).
- CI resources: Spark 3.4 was removed ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md)), parallel Spark test execution cut the run from about 84 to 58 minutes ([Spark sync 2026-06-16](../records/meetings/spark/2026/2026-06-16.md)), and CI moved to ubuntu-24.04 runners as a short-term way around congested shared ASF runner queues ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Working groups: the read restrictions sync asked whether it is still needed ([read restrictions sync 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md)), and the file and vector type sync asked whether to consolidate with the weekly V4 sync ([file and vector type sync 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md)); no answers are recorded.

## Timeline

- 2026-05-13: Shawn Chang and Andrei Tserakhau welcomed as new committers; Summit 2026 selection committee retrospective linked ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md)).
- 2026-05-28: Thread on reviewer bandwidth in iceberg-rust; no concrete action agreed ([thread summary](../records/threads/2026/05/discuss-reviewer-bandwidth-in-iceberg-rust-cf8ecd.md), [dev list](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r)).
- 2026-06-03: Kevin Liu starts early planning for Iceberg Summit 2027; participants agree to start earlier than before, no location or date decided ([thread summary](../records/threads/2026/06/discuss-iceberg-summit-2027-89ed0c.md), [dev list](https://lists.apache.org/thread/vsxpk5glhf38nnm7yx8llh5p1wn5yc20)).
- 2026-06-16: Spark sync reviews CI usage improvements ([Spark sync 2026-06-16](../records/meetings/spark/2026/2026-06-16.md)).
- 2026-07-15: Community sync records a to-do to submit a proposal for Iceberg Summit 2027 ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md)).
- 2026-08-04: Thread on virtual community meetups and showcases ([thread summary](../records/threads/2026/08/discuss-virtual-community-meetups-and-showcases-af00f4.md), [dev list](https://lists.apache.org/thread/4fnks078pwlgoyhckjvonvm6dgo0ywc8)).
- 2026-08-05: Maximilian Michels announced as a new committer ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md)).
- 2026-08-12: Sung Yun announces Summit 2027 planning and a call for early sponsor interest ([thread summary](../records/threads/2026/08/discuss-iceberg-summit-2027-planning-early-sponsor-interest-914ce4.md), [dev list](https://lists.apache.org/thread/0wqsv94hy4sgw1js557ps4xfonjpfbf2)).
- 2026-08-24: A late-September San Francisco meetup is moved to November to avoid competing with another meetup; the PMC stays out of meetup scheduling ([thread summary](../records/threads/2026/08/discuss-sf-iceberg-meetup-in-late-september-e3a4cb.md), [dev list](https://lists.apache.org/thread/3jcdq4w6kvyfjbczddch6hzhbt1qjor0)).
- 2026-09-02: PMC approval of the Summit 2027 proposal announced with a call for Selection Committee volunteers; on 2026-10-19 the committee is reported finalized ([thread summary](../records/threads/2026/09/discuss-iceberg-summit-2027-selection-committee-d0d4a6.md), [dev list](https://lists.apache.org/thread/hk1gnjrqnfvmjknrsyyphfs6mfxkz20s)).
- 2026-10-01: Péter Váry proposes removing spec changes from Java release notes ([thread summary](../records/threads/2026/10/discuss-spec-changes-in-release-notes-97adb7.md), [dev list](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl), [thread summary](../records/threads/2026/10/discuss-spec-changes-in-release-notes-7ff555.md), [dev list](https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j)).
- 2026-10-07: Gang Wu welcomed as a new PMC member; Summit 2027 call for papers mentioned ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- 2026-10-27: Community health dashboard shared on the dev list ([thread summary](../records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md), [dev list](https://lists.apache.org/thread/s5jqhbczoknftmojhrvzpsb53w1s7gd6)).
- 2026-10-28: Dashboard walkthrough at the community sync; Russell agrees to add a metric for stale pull requests that had contributor reviews but no committer review ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- 2026-11-09: The index sync suggests the community may need a document on how to introduce a proposal ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md)).

## Where help is needed

- Open question from the 2026-10-28 sync: should the community act on the stale pull request backlog and unanswered threads, and how ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Kevin Liu asked whether there is enough interest in a merge queue for the Java repository ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md)).
- Spec release notes: a choice between [apache/iceberg#18349](https://github.com/apache/iceberg/pull/18349) and [apache/iceberg#18379](https://github.com/apache/iceberg/pull/18379) is pending ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md)).
- CI: the Spark sync asked whether some tests could use in-memory FileIO, for example by switching the default FileIO to see what breaks ([Spark sync 2026-06-16](../records/meetings/spark/2026/2026-06-16.md)).
<!-- kb:generated:end -->

## Notes
