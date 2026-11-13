---
id: initiative/ai-contributions
type: initiative
title: Policy on AI-assisted contributions and reviews
status: discussion
updated: '2026-11-13'
sources:
- meeting/python/2026-05-26
- thread/t-ceb017adb8f59712
- meeting/community/2026-08-05
- thread/t-5dd317254d01abc3
- meeting/community/2026-08-26
- meeting/community/2026-09-16
- meeting/community/2026-10-07
- thread/t-03ef420b5ad9206f
- meeting/community/2026-10-28
- meeting/index/2026-11-09
links:
- rel: championed_by
  to: person/wgtmac
  confidence: extracted
  source: thread/t-ceb017adb8f59712
- rel: championed_by
  to: person/manuzhang
  confidence: extracted
  source: thread/t-5dd317254d01abc3
- rel: championed_by
  to: person/pvary
  confidence: extracted
  source: meeting/community/2026-10-07
- rel: handled_by
  to: group/community
  confidence: extracted
  source: meeting/community/2026-09-16
- rel: tracked_in
  to: gh:apache/iceberg#17671
  confidence: extracted
  source: thread/t-5dd317254d01abc3
---

# Policy on AI-assisted contributions and reviews

<!-- kb:generated:start -->
## What it is

The project is working out how to handle contributions and reviews produced with AI tools: what contributors must do before posting AI-written code or review comments, how AI use is disclosed and credited, and whether automated AI review should be switched on for the repositories ([thread 2026-08-15](../records/threads/2026/08/discuss-ai-review-comments-5dd317.md), [dev list](https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb); [thread 2026-07-16](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)). Most of the guidance lands in `AGENTS.md` files in the repositories ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Current state

- Agreed for a trial: ASF-managed GitHub Copilot code review is enabled for iceberg-cpp through `.asf.yaml` ([iceberg-cpp #833](https://github.com/apache/iceberg-cpp/pull/833)); nobody objected, and replies asked for custom Copilot instructions and for guidance on how contributors should respond to its feedback ([thread 2026-07-16](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).
- Merged: the community sync notes list three `AGENTS.md` updates in the Java repository, covering AI contribution and disclosure rules ([#18168](https://github.com/apache/iceberg/pull/18168)), testing guidance ([#18166](https://github.com/apache/iceberg/pull/18166)), and Javadoc and test failure guidance ([#18293](https://github.com/apache/iceberg/pull/18293)) ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and "basic assumptions" added to `AGENTS.md` in PyIceberg ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Shared view, no formal decision: respondents on the dev list agreed that AI output must be read and understood before it is posted as a review comment; the thread ended without a decision on the proposed `AGENTS.md` changes in [#17671](https://github.com/apache/iceberg/pull/17671) (issue [#17670](https://github.com/apache/iceberg/issues/17670)) ([thread 2026-08-15](../records/threads/2026/08/discuss-ai-review-comments-5dd317.md), [dev list](https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb)). That pull request was closed without being merged on 2026-10-29 ([#17671](https://github.com/apache/iceberg/pull/17671)).
- Open: at the community sync, possible actions were proposed but not decided: update the contribution page with best practices for people, perhaps update the guidelines for AI-assisted contributions, and update `agents.md` for agents, including a pre-PR checklist such as checking for related pull requests first ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Related signal: in the community health thread, one participant attributed the drop in contributors making a second contribution to AI-assisted contributions overloading a small group of maintainers ([thread 2026-10-27](../records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md), [dev list](https://lists.apache.org/thread/s5jqhbczoknftmojhrvzpsb53w1s7gd6)).
- Related signal: Iceberg Rust introduced a limit of three open non-draft pull requests for users without write access ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); the notes do not tie this to AI use.

## Timeline

- 2026-05-26: SKILLS and `AGENTS.md` was an agenda item at the PyIceberg sync; no outcome is recorded ([PyIceberg sync 2026-05-26](../records/meetings/python/2026/2026-05-26.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-07-16: Gang Wu proposed enabling Copilot code review, starting with iceberg-cpp as a trial ([thread 2026-07-16](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).
- 2026-07-20: after the cost structure was clarified, he said he would merge the iceberg-cpp pull request enabling the trial ([thread 2026-07-16](../records/threads/2026/07/discuss-enable-github-copilot-code-review-ceb017.md), [dev list](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny)).
- 2026-08-05: the community sync notes list "basic assumptions" added to PyIceberg's `AGENTS.md` ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-15: Manu Zhang raised concerns about long, unread AI-generated review comments; a pull request updating `AGENTS.md` ([#17671](https://github.com/apache/iceberg/pull/17671)) was opened in response ([thread 2026-08-15](../records/threads/2026/08/discuss-ai-review-comments-5dd317.md), [dev list](https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb)).
- 2026-08-26: contributions using LLMs was listed as a discussion item at the community sync; no discussion is recorded ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-09-16: the community sync discussed best practices for handling LLM contributions and noted that the burden of checking AI output falls on the reviewer ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-07: the community sync notes list three `AGENTS.md` updates merged in the Java repository, including AI contribution and disclosure rules ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-27: the community health thread linked stalled pull requests to AI-assisted contributions in one reply ([thread 2026-10-27](../records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md), [dev list](https://lists.apache.org/thread/s5jqhbczoknftmojhrvzpsb53w1s7gd6)).
- 2026-11-09: at the index sync, a long, heavily AI-assisted dev list proposal led to a request for a shorter version and a suggestion that the community may need a document on how to introduce a proposal ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md), [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).

## Where help is needed

- The community sync listed, without an owner, updating the contribution page with best practices and adding a pre-PR checklist to `agents.md` ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- The index sync suggested a document on how to introduce a proposal; no owner is recorded ([index sync 2026-11-09](../records/meetings/index/2026/2026-11-09.md), [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).
<!-- kb:generated:end -->

## Notes
