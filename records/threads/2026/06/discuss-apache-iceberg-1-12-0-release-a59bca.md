---
id: thread/t-a59bca208d82363d
type: thread
title: Apache Iceberg 1.12.0 release planning
date: '2026-06-05'
url: https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q
kind: release-planning
status: informational
messages: 32
sources:
- devlist:w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q
refs:
- gh:apache/iceberg#14984
- gh:apache/iceberg#16543
- gh:apache/iceberg#17552
- gh:apache/iceberg#17709
- gh:apache/iceberg#17627
- gh:apache/iceberg#16765
- gh:apache/iceberg#18169
- gh:apache/iceberg#17984
- gh:apache/iceberg#17849
- gh:apache/iceberg#17845
- gh:apache/iceberg#15989
- gh:apache/iceberg#16507
- gh:apache/iceberg#16827
- gh:apache/iceberg#13979
- gh:apache/iceberg#17706
links:
- rel: started_by
  to: person/nssalian
  confidence: observed
updated: '2026-11-13'
---

# Apache Iceberg 1.12.0 release planning

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Apache Iceberg 1.12.0 release](https://lists.apache.org/thread/w5qnj9gnl4rjhjnzyxlsbdzjx3kw9j8q) · **Started:** 2026-06-05 by [[person/nssalian|Neelesh Salian]] · **Messages:** 32 (last 2026-09-25) · **Outcome:** informational

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Release manager nssalian opened planning for 1.12.0 with a target of late August or early September 2026, about three months after 1.11.0, to return to a 3-4 month cadence, and tracked work on the 1.12.0 milestone. Contributors asked for specific PRs to be included. Spark 4.2 support was removed from the milestone after aokolnychyi advised against shipping it; the module was to be merged but excluded from release artifacts. Switching the Spark default table version to 3 was judged out of scope for 1.12. Blockers included the shaded-jar LICENSE/NOTICE cleanup, Kafka Connect data-loss fixes and a manifest list encryption key fix. Flink 2.2 and 2.3 upgrades were added to the milestone. RC0 was cut on September 18; after a fix for issue 18191 and a decision to keep the geo type toString change, RC1 and then RC2 were put up for vote, with RC2 voting open until September 29.

**Why it matters:** Shows what made or missed 1.12.0 and that Spark 4.2 support is in main but not in the 1.12 release artifacts.

## Outcome

Planning thread. RC0 and RC1 were superseded; the last message announces RC2 for 1.12.0 is out for vote in a separate thread, with voting open until 2026-09-29. Spark 4.2 support and PR 13979 were deferred past 1.12. ([message](https://lists.apache.org/thread/28lz6onkwb3d2rvpxd8gqfoy3bvy58cp), `devlist:28lz6onkwb3d2rvpxd8gqfoy3bvy58cp`)

## Positions

- **[[person/stevenzwu|Steven Wu]]:** With regular releases every 2-3 months there is normally no need to hold a release for features, only for critical security and correctness issues. ([message](https://lists.apache.org/thread/91zr07ykcd39vqz6zcohpfjvngb24vld))
- **[[person/pan3793|Cheng Pan]]:** Asked whether the default table version created by Spark could move from 2 to 3 in the next release to drive adoption of features such as Variant. ([message](https://lists.apache.org/thread/vz5sm923k7fk0d29f8zvo6nrh1skfq5v))
- **[[person/nssalian|Neelesh Salian]]:** The default should move forward eventually, but gaps remain on Variant and Geo types, so it will not happen in the 1.12 timeline. ([message](https://lists.apache.org/thread/rnpyhvtjqbopwmj0yh6x1t1ym3w64bpm))
- **Felix Perez Diener:** Asked that Flink 2.3 support be included in 1.12.0. ([message](https://lists.apache.org/thread/p7dlfh3hbbj5s32270rko9jhqcf7l8l2))
- **[[person/aokolnychyi|Anton Okolnychyi]]:** Advised against shipping Spark 4.2 support in 1.12: merge the module to main to unblock development but leave it out of the release until the integration matures. ([message](https://lists.apache.org/thread/821bjvx2jym709yvt56xl6vm733z742t))
- **[[person/adutra|Alexandre Dutra]]:** Asked to include PR 17709, which implements the remote signing REST spec changes, so the spec change does not ship unimplemented. ([message](https://lists.apache.org/thread/1gtb67pdpw0cnf0l12yxpw6yywlfbsgh))
- **[[person/manuzhang|Manu Zhang]]:** Following Szehon's suggestion, the Spark 4.2 source can be merged while excluded from both binary and source release tarballs. ([message](https://lists.apache.org/thread/5501y3oxjkksn9cmt00tg1bpoh1phyvd))
- **[[person/stevenzwu|Steven Wu]]:** Flagged that PR 16765 changes geometry and geography toString to always print resolved defaults; reads stay compatible, and he is fine with 1.12 shipping the changed behavior. ([message](https://lists.apache.org/thread/v7wo6tkwwotxhdv9d8p3xrhqgt9fr7gr))
- **Gábor Kaszab:** Asked whether the missing cleanup of unused encryption keys in table metadata (PR 16353) should be addressed in this release. ([message](https://lists.apache.org/thread/5ty5qp0jbqyd3v9c7df4jvqhdgtl3st7))
- **[[person/nssalian|Neelesh Salian]]:** The encryption key cleanup interface change needs more debate and does not need to be rushed into 1.12. ([message](https://lists.apache.org/thread/c5yxp85dp0ottpq10nlbvrsfd51yjfd3))

References: [iceberg#14984](https://github.com/apache/iceberg/issues/14984), [iceberg#16543](https://github.com/apache/iceberg/issues/16543), [iceberg#17552](https://github.com/apache/iceberg/issues/17552), [iceberg#17709](https://github.com/apache/iceberg/issues/17709), [iceberg#17627](https://github.com/apache/iceberg/issues/17627), [iceberg#16765](https://github.com/apache/iceberg/issues/16765), [iceberg#18169](https://github.com/apache/iceberg/issues/18169), [iceberg#17984](https://github.com/apache/iceberg/issues/17984), [iceberg#17849](https://github.com/apache/iceberg/issues/17849), [iceberg#17845](https://github.com/apache/iceberg/issues/17845), [iceberg#15989](https://github.com/apache/iceberg/issues/15989), [iceberg#16507](https://github.com/apache/iceberg/issues/16507), [iceberg#16827](https://github.com/apache/iceberg/issues/16827), [iceberg#13979](https://github.com/apache/iceberg/issues/13979), [iceberg#17706](https://github.com/apache/iceberg/issues/17706)
<!-- kb:generated:end -->

## Notes
