# dev@iceberg.apache.org: source research (2026-11-13)

The analysis covers 14 months (2025-10 → 2026-11-13): **4,540 messages in 680 threads**. Parsed counts match the API's per-month counts.

## Access and incremental sync
- **Bulk:** `https://lists.apache.org/api/mbox.lua?list=dev@iceberg.apache.org&date=YYYY-MM` returns full RFC822 messages with `Message-ID`, `References` and `In-Reply-To`. They parse cleanly with Python's `mailbox`. A month is 2–12 MB.
- **History starts 2018-11.** `stats.lua?list=dev&domain=iceberg.apache.org&d=lte=1d` returns `active_months`, a per-month count since 2018, which can drive backfill and check its completeness.
- **Permalinks:** `stats.lua?...&d=YYYY-MM` maps the Message-ID to the PonyMail `mid`, giving `https://lists.apache.org/thread/<mid>`. Single lookups work through `email.lua?id=` and `thread.lua?id=`. Window queries: `d=dfr=YYYY-MM-DD|dto=YYYY-MM-DD` or `d=lte=Nd`. Search: `q=`.
- **Recommended sync:**
  1. Once a day, re-download the current month's mbox, plus the previous month's during the first days of a month.
  2. Dedupe by Message-ID.
  3. Rebuild threads from the References headers.
  4. Freeze months more than 7 days old.

  The list carries only about 10–20 messages a day.

## Volume (last 12 months)
3.4k–3.7k messages a year, from 313 distinct senders, and rising. September 2026 was the peak, with the 1.12 release and the v4 spec votes: 478 messages, 115 senders.

## Thread types (2026-05-13 → 11-13, 353 threads)
| Type | Threads | Msgs |
|---|---|---|
| [DISCUSS] / proposals / reports | 145 | 807 |
| [VOTE] spec or process | 32 | 509 |
| [VOTE] release RC | 30 | 294 |
| Events / community | 29 | 125 |
| Admin noise (subscribe, Slack invites, bots) | 22 | 47 |
| PR review requests | 20 | 44 |
| Standalone [RESULT] | 17 | 33 |
| Sync-meeting notices | 12 | 31 |
| [ANNOUNCE] release | 10 | 32 |
| Release planning [DISCUSS] | 9 | 110 |
| New committer/PMC announcements | 2 | 70 |

62 threads link a Google Doc. **The typical lifecycle is a [DISCUSS] thread, then a Google Doc plus a recurring sync, then a [VOTE] on a spec PR, then a [RESULT].**

## Significant threads, Aug–Nov 2026
| Date | Subject | Replies | Starter | Gist |
|---|---|---|---|---|
| 08-13 | [VOTE] Deprecate equality deletes in V4 | 30 | huaxin gao | V4 writers can no longer produce equality deletes; readers still apply them. Passed; spec PR #17783 vote on 09-23 |
| 08-19 | [VOTE] Create apache/iceberg-verification repo | 29 | Neelesh Salian | Language-neutral conformance fixtures; passed |
| 08-21 | [DISCUSS] Move Rust DataFusion integration to its own repo | 27 | Matt Butrovich | Led to the 09-09 vote: move to apache/datafusion-iceberg |
| 08-31 | [VOTE] Finer-grained read restrictions in REST spec | 22 | Prashant Singh | Column/row restrictions (PR #13879); passed |
| 08-31 | [DISCUSS] Field ID tracking for non-materialized columns in v4 | 9 | Ryan Blue | Led to the stats-only fields vote |
| 09-02 | [DISCUSS] Iceberg Summit 2027 selection committee | 42 | Sung Yun | Community process |
| 09-17 | New PMC member: Gang Wu | 35 | Fokko Driesprong | Gang Wu leads Iceberg C++ |
| 09-23 | [DISCUSS] REST: X-Iceberg-Access-Delegation not satisfiable | 19 | youngrae kim | Raised from Polaris; led to the 10-25 vote adding `none` |
| 10-02 | [VOTE] Standard User-Agent for REST clients [REOPEN] | 19 | rahul mahadev | Passed |
| 10-07 | [VOTE] Monotonic snapshot timestamps in v4 | 22 | Steven Wu | Passed |
| 10-09 | [VOTE] Merge baseline V4 AMT spec PR | 19 | Amogh Jahagirdar | The Adaptive Metadata Tree replaces the manifest list. Merged as a baseline |
| 10-12 | [VOTE] Add File type to v4 | 29 | Talat Uyarer | Unstructured data; passed 10-19 |
| 10-22/28 | Stats tightness; stats-only fields for v4 | 13/16 | Anoop Johnson / Ryan Blue | v4 statistics redesign |
| 10-22 | [VOTE] Table constraints in v4 | 10 | huaxin gao | Check/unique/PK, plus an `enforced` flag |
| 10-30 | [VOTE] `_last_updated_time` row-lineage column | 13 | Steven Wu | |
| 11-02 | [VOTE] Default value expressions for v4 | 19 | Daniel Weeks | Passed 11-06 |
| 11-10 | [DISCUSS] MV spec ready for broader review | 1 | Jan Kaul | |

Process threads are active too: AI/Copilot reviews, squash-commit titles, a community health dashboard, and spec changes in release notes.

## Releases (last 12 months; release manager = who sent the vote and announcement)
- **Java:**
  - 1.10.1: 12-23, huaxin gao.
  - 1.10.2: 05-19, Amogh Jahagirdar.
  - 1.11.0: 05-20, Aihua Xu.
  - 1.12.0: 10-01, Neelesh Salian.
  - 1.13: Anoop Johnson volunteered; targeting end of year.
  - Cadence: a minor release every 4–5 months.
- **PyIceberg:**
  - 0.11.0: 02-10, Drew.
  - 0.11.1: Kevin Liu.
  - 0.12.0: 09-01, Alex Stephen.
  - Cadence: about every 6–7 months.
- **Rust:**
  - 0.8.0: Xuanwo.
  - 0.9.x: Shawn Chang.
  - 0.10.0: Danny Jones.
  - 0.10.1: Shawn Chang.
  - 0.11.0: 11-04, Danny Jones.
  - Cadence: about every 2–4 months.
- **Go:** v0.5 to v0.7, all by Matt Topol, about every 4 months. Announcements are often missing from dev@.
- **C++:** 0.2 Gang Wu, 0.3 Junwang Zhao, 0.4 Manu Zhang. Cadence: about every 4 months.
- **Terraform provider (new):** Matt Topol.

## Participation (12 months, display names)
- **Top senders:** Kevin Liu 262, Steven Wu 192, Péter Váry 176, Russell Spitzer 157, Ryan Blue 129, Daniel Weeks 128, Neelesh Salian 121, huaxin gao 120, Yufei Gu 110, Amogh Jahagirdar 92.
- **Reviewers and voters (mostly reply, rarely start threads):** Yufei Gu, Jean-Baptiste Onofré, Renjie Liu, Péter Váry, Daniel Weeks.
- **[VOTE] starters:**
  - Release managers: Matt Topol, Danny Jones, Junwang Zhao, Shawn Chang.
  - Spec champions: huaxin gao, Steven Wu, Prashant Singh, Eduard Tudenhöfner, Ryan Blue, Alexandre Dutra.
- **Who drives what:**
  - v4 core spec: Ryan Blue, Daniel Weeks, Steven Wu, Amogh Jahagirdar, Eduard Tudenhöfner, Anoop Johnson.
  - REST spec: Prashant Singh, Alexandre Dutra, Andrei Tserakhau.
  - Rust: Danny Jones, Shawn Chang, Kevin Liu.
  - Go/Terraform: Matt Topol.
  - C++: Gang Wu, Junwang Zhao, Manu Zhang.
  - Community/Summit: Sung Yun, Kevin Liu.

## Other lists
issues@ (about 8.8k a month, a GitHub mirror), commits@ and ci-jobs@ are noise. Use GitHub directly instead. **Only dev@ is worth ingesting.**

## Pitfalls
- **Sender names need normalizing:**
  - Strip "X via dev" suffixes.
  - Rewrite "Last, First" as "First Last".
  - Merge aliases (Alex/Alexandre Dutra), using a curated alias map.
- **Vote results are inconsistent.** A [RESULT] may arrive as a reply or as a new thread, written `[VOTE][RESULT]` or `[RESULT][VOTE]`, or be missing. Votes are often reopened under the same subject, so link them by subject plus PR number. Counting "+1"s ignores whether votes are binding.
- **Match prefixes literally and case-insensitively.** A loose "RESULT" match catches "result type".
- **Window edges leave orphan "Re:" threads.** Fetch one extra month at the start of any window.
- **The list links out.** Design detail lives in the linked Google Docs and PRs, so follow those links.
