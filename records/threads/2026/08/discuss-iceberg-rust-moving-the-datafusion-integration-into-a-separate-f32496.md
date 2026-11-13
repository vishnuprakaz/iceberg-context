---
id: thread/t-f324967b2d45dc23
type: thread
title: 'Iceberg Rust: moving the DataFusion integration into a separate repository'
date: '2026-08-21'
url: https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9
kind: discuss
status: no-conclusion
messages: 5
sources:
- devlist:pk4yqd4llr85lmq3gskbfl9v31sfqpp9
refs:
- gh:apache/iceberg-rust#3029
- gh:apache/iceberg-rust#2613
- gh:apache/iceberg-rust#3036
links:
- rel: started_by
  to: person/mbutrovich
  confidence: observed
updated: '2026-11-13'
---

# Iceberg Rust: moving the DataFusion integration into a separate repository

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg Rust: moving the DataFusion integration into a separate repository](https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9) · **Started:** 2026-08-21 by [[person/mbutrovich|Matt Butrovich]] · **Messages:** 5 (last 2026-08-26) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Matt Butrovich summarized discussions in both the Iceberg Rust and DataFusion communities about moving the DataFusion TableProvider integration out of the iceberg-rust repository. The motivations given were that issues and pull requests against the integration often go stale for lack of reviewers who use it, that Iceberg Rust wants to stay engine-agnostic, and that projects such as Comet cannot upgrade DataFusion and Arrow until Iceberg Rust does. Open questions were where the code would live and under what governance, and how Iceberg Rust would keep running its sqllogictest suite. Shawn (CTTY), Renjie (liurenjie1024) and Manu Zhang supported a move provided the new home is Apache-governed; Renjie leaned toward moving the sqllogictests to the new repository too. After a community sync, Shawn listed questions still open: whether separation or more DataFusion reviewers is the right fix, where the boundary with core lies, cross-repository testing, and location. No decision was reached.

**Why it matters:** The outcome decides where DataFusion users and projects such as Comet get their Iceberg integration and how iceberg-rust runs its SQL regression tests.

## Outcome

General agreement that the integration has a reviewer-bandwidth problem and that a separate Apache-governed repository could help, but whether to split, where the code would live and how testing would work were left open after the August 26 community sync.

## Positions

- **[[person/mbutrovich|Matt Butrovich]]:** Lays out the case for splitting the DataFusion integration out of iceberg-rust (stale PRs, engine neutrality, dependency upgrade coupling) and the open questions on governance and sqllogictests. ([message](https://lists.apache.org/thread/pk4yqd4llr85lmq3gskbfl9v31sfqpp9))
- **[[person/CTTY|Shawn Chang]]:** Agrees a separate repository can help, but wants it kept under Apache governance and maintained jointly by Iceberg Rust and DataFusion contributors, not owned only by the DataFusion side. ([message](https://lists.apache.org/thread/jppc7p1oklcdh46nkvl11lcts5rk16kk))
- **[[person/liurenjie1024|Renjie Liu]]:** Supports an Apache repository, for example a sub-repository of the DataFusion project, and leans toward moving the sqllogictests there to keep the dependency graph and releases simple. ([message](https://lists.apache.org/thread/090ocgnm2qpbyrlznjhlz2sojg7wc4vf))
- **[[person/manuzhang|Manu Zhang]]:** Supports moving the DataFusion integration and tests into a separate Apache-governed repository. ([message](https://lists.apache.org/thread/gjx388zy633jxw1phdshp0f57odb4qrr))
- **[[person/CTTY|Shawn Chang]]:** The main question is how to improve development velocity without losing the close design, testing and governance relationship between the integration and iceberg-rust core. ([message](https://lists.apache.org/thread/2bmj2mp2ggjd1qz466w06047p20kq64g))

References: [iceberg-rust#3029](https://github.com/apache/iceberg-rust/issues/3029), [iceberg-rust#2613](https://github.com/apache/iceberg-rust/issues/2613), [iceberg-rust#3036](https://github.com/apache/iceberg-rust/issues/3036)
<!-- kb:generated:end -->

## Notes
