---
id: initiative/java-releases
type: initiative
title: Java releases
status: released
updated: '2026-11-13'
sources:
- thread/t-e6327b02ad166780
- thread/t-98bf4fbbbb6c143a
- thread/t-43bc363d6f78db31
- thread/t-88bfc4197adf37a9
- thread/t-993bbf42f9af82cf
- meeting/community/2026-06-03
- thread/t-a59bca208d82363d
- thread/t-97f54e45553021e0
- thread/t-a1beaa110569764f
- meeting/community/2026-06-24
- meeting/spark/2026-08-18
- thread/t-1d3c20c5c64f7fcb
- meeting/variant/2026-09-03
- thread/t-36974638264b04f5
- thread/t-e2b669d1053d1cbb
- thread/t-197c5e8a5755ba9a
- thread/t-8e05ea5cfb5440f5
- thread/t-824f8a51f5314747
- thread/t-69a16596451dbbe3
- thread/t-b00cc9ec1c194566
- thread/t-7ff555b89c73c647
- thread/t-97adb77b6cd93c6b
- meeting/community/2026-10-07
- meeting/community/2026-10-28
- meeting/spark/2026-11-11
links:
- rel: championed_by
  to: person/nssalian
  confidence: extracted
  source: thread/t-a59bca208d82363d
- rel: championed_by
  to: person/aihuaxu
  confidence: extracted
  source: thread/t-993bbf42f9af82cf
- rel: championed_by
  to: person/amogh-jahagirdar
  confidence: extracted
  source: thread/t-88bfc4197adf37a9
- rel: championed_by
  to: person/anuragmantri
  confidence: extracted
  source: thread/t-b00cc9ec1c194566
- rel: handled_by
  to: group/community
  confidence: extracted
  source: meeting/community/2026-10-07
- rel: handled_by
  to: group/spark
  confidence: extracted
  source: meeting/spark/2026-11-11
- rel: tracked_in
  to: gh:apache/iceberg#17959
  confidence: extracted
  source: meeting/spark/2026-11-11
---

# Java releases

<!-- kb:generated:start -->
## What it is

The Java library in `apache/iceberg` is released as numbered versions (1.11, 1.12, 1.13) with patch releases for older lines. Each release has a volunteer release manager, a milestone, one or more release candidates and a vote on the dev list ([thread 2026-06-05](../records/threads/2026/06/discuss-apache-iceberg-1-12-0-release-a59bca.md), [dev list](https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q); [thread 2026-05-15](../records/threads/2026/05/vote-release-apache-iceberg-1-11-0-rc4-993bbf.md), [dev list](https://lists.apache.org/thread/x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp)). This page follows which release is out, which is next, and what is being argued about for inclusion.

## Current state

- Latest release: 1.12.0. The RC2 vote was announced as concluded and passed on 2026-09-29 ([thread 2026-09-29](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-824f8a.md), [dev list](https://lists.apache.org/thread/26g46qtgy3nr435wdg5wh53q48k17zo3)), with 4 binding and 10 non-binding +1 votes and no +0 or -1 votes ([result message](https://lists.apache.org/thread/ychjvqbmt7ksmczhct3mnw8j3yowwbcr)), and the community sync notes of 2026-10-07 mark Java 1.12 as released ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). Neelesh Salian was release manager ([thread 2026-06-05](../records/threads/2026/06/discuss-apache-iceberg-1-12-0-release-a59bca.md), [dev list](https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q)).
- 1.12.0 contents noted in the records: Flink 1.20, 2.1, 2.2 and 2.3 ([thread 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md), [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)); no Spark 4.2 artifacts, which were excluded from the convenience binaries on purpose ([#18024](https://github.com/apache/iceberg/pull/18024)) ([thread 2026-09-25](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-8e05ea.md), [dev list](https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77)); a changed `toString()` for geometry and geography types, kept as a documented behaviour change ([thread 2026-09-18](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc0-369746.md), [dev list](https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb)).
- Next release: 1.13, with Anurag Mantripragada as release manager and Anoop Johnson taking 1.14; the date (end of year or early January) and the Spark 4.2 scope were not settled ([thread 2026-09-30](../records/threads/2026/09/discuss-iceberg-1-13-release-java-b00cc9.md), [dev list](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc)). As of the Spark sync on 2026-11-11 there was no release candidate or 1.13.x branch, the Spark 4.2 tracker ([#17959](https://github.com/apache/iceberg/issues/17959)) was on the milestone, and a freeze date had not been decided ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Open: whether to do a 1.12.1 now. Two silent-data-loss fixes ([#18005](https://github.com/apache/iceberg/pull/18005), [#18348](https://github.com/apache/iceberg/pull/18348)) are in no release; no outcome is recorded ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Patch lines: 1.10.2 passed its vote on 2026-05-18 ([thread 2026-05-14](../records/threads/2026/05/vote-release-apache-iceberg-1-10-2-rc1-88bfc4.md), [dev list](https://lists.apache.org/thread/o5rmmlqvyl6my1p5mr6jxxo8cs0lvyo1)). Everyone who replied supported 1.11.1 and 1.10.3 patch releases with narrow backports to 1.10; milestones and the 1.11.x branch were created, with Amogh Jahagirdar as release manager ([thread 2026-06-06](../records/threads/2026/06/discuss-1-11-1-1-10-3-patch-releases-a1beaa.md), [dev list](https://lists.apache.org/thread/nh8zy6s9kbhd5mvcctfhl71jzgcc1krs); [community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). No release candidate for either is announced in those threads ([thread 2026-06-06](../records/threads/2026/06/discuss-1-11-1-1-10-3-patch-releases-a1beaa.md), [dev list](https://lists.apache.org/thread/nh8zy6s9kbhd5mvcctfhl71jzgcc1krs)).
- Process: all participants agreed that spec changes should be left out of the Java release notes ([thread 2026-10-01](../records/threads/2026/10/discuss-spec-changes-in-release-notes-97adb7.md), [dev list](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl)); [#18349](https://github.com/apache/iceberg/pull/18349) and an alternative [#18379](https://github.com/apache/iceberg/pull/18379) propose a dedicated layout, and no outcome is recorded ([thread 2026-10-01](../records/threads/2026/10/discuss-spec-changes-in-release-notes-7ff555.md), [dev list](https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j); [community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). A separate `iceberg-format` repository was suggested and strongly opposed by Dan Weeks ([thread 2026-10-01](../records/threads/2026/10/discuss-spec-changes-in-release-notes-7ff555.md), [dev list](https://lists.apache.org/thread/3otgz8ll1zkt3wt3hvjpll6pmzr4w57j)).
- Process: after bundle LICENSE gaps forced a new 1.12.0 candidate, adding a licence check to the release process was suggested ([thread 2026-09-23](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc1-197c5e.md), [dev list](https://lists.apache.org/thread/z5fk8q6pwx6v5nkm3r4l3olf300myghh)). Release automation was an agenda item at the community sync with no details recorded ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Spark versions: 1.11.0 is the last release that supports Spark 3.4 ([thread 2025-09-17](../records/threads/2025/09/discuss-deprecating-spark-3-4-e6327b.md), [dev list](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv)); whether to keep Spark 3.5 and 4.0 for longer was asked with no outcome recorded ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Timeline

- 2025-09-17: Kevin Liu proposed deprecating Spark 3.4 in 1.11 and removing it in 1.12 ([thread 2025-09-17](../records/threads/2025/09/discuss-deprecating-spark-3-4-e6327b.md), [dev list](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv)).
- 2026-05-13: 1.11.0 RC1 was superseded after blockers and Spark 3.4 backports; RC2 and RC3 were built but not put to a vote ([thread 2026-05-13](../records/threads/2026/05/vote-release-apache-iceberg-1-11-0-rc1-43bc36.md), [dev list](https://lists.apache.org/thread/j1v2yc69sbh7p85oftcy9tdqph5sxqt7); [thread 2026-05-11](../records/threads/2026/05/vote-release-apache-iceberg-1-11-0-rc1-98bf4f.md), [dev list](https://lists.apache.org/thread/j83qwbv8vplqcx7b298toxmbrbckvprf)).
- 2026-05-15: Aihua Xu proposed 1.11.0 RC4 ([thread 2026-05-15](../records/threads/2026/05/vote-release-apache-iceberg-1-11-0-rc4-993bbf.md), [dev list](https://lists.apache.org/thread/x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp)).
- 2026-05-18: the 1.10.2 RC1 vote passed with 5 binding and 5 non-binding +1 votes ([thread 2026-05-14](../records/threads/2026/05/vote-release-apache-iceberg-1-10-2-rc1-88bfc4.md), [dev list](https://lists.apache.org/thread/o5rmmlqvyl6my1p5mr6jxxo8cs0lvyo1)).
- 2026-05-19: the 1.11.0 RC4 vote passed with 6 binding and 7 non-binding +1 votes; LICENSE and NOTICE issues in runtime bundles were tracked in [#16396](https://github.com/apache/iceberg/issues/16396) for a later release ([thread 2026-05-15](../records/threads/2026/05/vote-release-apache-iceberg-1-11-0-rc4-993bbf.md), [dev list](https://lists.apache.org/thread/x5x9fzq3j1wybx3fc5orbc5c2mnxmbzp)).
- 2026-05-20: the Spark 3.4 removal ([#14122](https://github.com/apache/iceberg/pull/14122)) was reported merged, making 1.11.0 the last version with Spark 3.4 ([thread 2025-09-17](../records/threads/2025/09/discuss-deprecating-spark-3-4-e6327b.md), [dev list](https://lists.apache.org/thread/n8qy5nsdw35vjog5lb4kp15989b800cv)).
- 2026-06-03: the community sync notes record 1.10.2 and 1.11 as out and name release managers for 1.12 and 1.13 ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-05: planning for 1.12.0 opened with a target of late August or early September 2026 and a return to a 3 to 4 month cadence ([thread 2026-06-05](../records/threads/2026/06/discuss-apache-iceberg-1-12-0-release-a59bca.md), [dev list](https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q)).
- 2026-06-06: 1.11.1 and 1.10.3 patch releases were proposed around a V3 correctness fix ([#16699](https://github.com/apache/iceberg/pull/16699)) and supported by all repliers ([thread 2026-06-06](../records/threads/2026/06/discuss-1-11-1-1-10-3-patch-releases-97f54e.md), [dev list](https://lists.apache.org/thread/k5pfk4rork0mp2p303pd70q9nx0tsl9w); [thread 2026-06-06](../records/threads/2026/06/discuss-1-11-1-1-10-3-patch-releases-a1beaa.md), [dev list](https://lists.apache.org/thread/nh8zy6s9kbhd5mvcctfhl71jzgcc1krs)).
- 2026-08-18: the Spark sync listed Spark candidates for 1.12, to move to 1.13 if not ready ([Spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- 2026-08-28: the Flink matrix for 1.12.0 was settled as 1.20, 2.1, 2.2 and 2.3 ([thread 2026-08-27](../records/threads/2026/08/discuss-flink-version-support-in-iceberg-1-12-0-1d3c20.md), [dev list](https://lists.apache.org/thread/8fsqcovm1cn7zdl571t4f9qlyqgf5qxy)).
- 2026-09-03: the variant sync decided to fix UTF-8 sort order without a backward compatibility fallback, to be prioritized for 1.12 ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md), [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- 2026-09-18: 1.12.0 RC0 was proposed; it was withdrawn after a source-archive licensing fix ([#18191](https://github.com/apache/iceberg/pull/18191)) ([thread 2026-09-18](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc0-369746.md), [dev list](https://lists.apache.org/thread/7qtxrysl1w5sjs7o74y31snt0jrkf5qb)).
- 2026-09-22: 1.12.0 RC1 was proposed ([thread 2026-09-22](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc1-e2b669.md), [dev list](https://lists.apache.org/thread/ptq6gyf6gcd4xwwkn2q3yrt9lxr7ojdk)); it was closed for a new candidate over a variant read failure with older commons-lang3 ([#18164](https://github.com/apache/iceberg/issues/18164)) and missing bundle LICENSE entries ([thread 2026-09-23](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc1-197c5e.md), [dev list](https://lists.apache.org/thread/z5fk8q6pwx6v5nkm3r4l3olf300myghh)).
- 2026-09-25: 1.12.0 RC2 was proposed ([thread 2026-09-25](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-8e05ea.md), [dev list](https://lists.apache.org/thread/l8gjs6z1ocfd70hv6dj923s7p9qm0w77)).
- 2026-09-29: the 1.12.0 RC2 vote was announced as concluded and passed with 4 binding and 10 non-binding +1 votes ([thread 2026-09-29](../records/threads/2026/09/vote-release-apache-iceberg-1-12-0-rc2-824f8a.md), [dev list](https://lists.apache.org/thread/26g46qtgy3nr435wdg5wh53q48k17zo3), [result message](https://lists.apache.org/thread/ychjvqbmt7ksmczhct3mnw8j3yowwbcr); replies to the result: [thread 2026-09-30](../records/threads/2026/09/result-vote-release-apache-iceberg-1-12-0-rc2-69a165.md), [dev list](https://lists.apache.org/thread/l86ozt0zp3t4rr3qstqd4vkmyhj1cdrw)).
- 2026-09-30: planning for 1.13 opened ([thread 2026-09-30](../records/threads/2026/09/discuss-iceberg-1-13-release-java-b00cc9.md), [dev list](https://lists.apache.org/thread/mj8czb2ljf8kj1d7ldbfw39sffr9knjc)).
- 2026-10-01: a dev list thread agreed to take spec changes out of the Java release notes ([thread 2026-10-01](../records/threads/2026/10/discuss-spec-changes-in-release-notes-97adb7.md), [dev list](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl)).
- 2026-10-07: the community sync raised preparing 1.13 for potentially early January ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-11: the Spark sync asked for a 1.13 freeze date and whether to do a 1.12.1 ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Where help is needed

- Wrong-result bugs need reviewers and an owner each, with a call on which block 1.13: [#18557](https://github.com/apache/iceberg/pull/18557), [#18617](https://github.com/apache/iceberg/pull/18617), [#18824](https://github.com/apache/iceberg/pull/18824), [#18621](https://github.com/apache/iceberg/pull/18621), [#18622](https://github.com/apache/iceberg/pull/18622), [#18738](https://github.com/apache/iceberg/pull/18738) ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- A decision was asked for on a 1.12.1 for the two silent-data-loss fixes and on the 1.13 freeze date ([Spark sync 2026-11-11](../records/meetings/spark/2026/2026-11-11.md), [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).
- Kevin Liu took the action to get reviews on the follow-up pull request for the Hive distribution licensing for Kafka Connect ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
<!-- kb:generated:end -->

## Notes
