# Per-doc findings (structure, format, recent meetings, edges)

## community (Iceberg community syncs) — main sync
- Tabs: t.0 "Iceberg community syncs" (header bullets + 2026-10-28 .. 2026-01-07, ends with "<Moved the rest of the syncs to a new tab>"), t.bl0gpabipiyq "Previous syncs" (2025-12-17 .. mid-2020).
- Entry markers vary by era: 2026-05-13..2026-10-28 are NORMAL_TEXT paragraphs "2026-10-28 ([Recording](youtu.be/..))" (NOT headings);
  2026-01..2026-04 and 2023-2025 are HEADING_2 with Google Docs *date chips* (dateElement, timestamp 2026-01-28T12:00:00Z) + "(Recording)";
  2022-2023 "## 15 March 2023", "## 17 Aug 2022"; typo "2024-03–27" (en-dash). Newest first. "(N/A)" / "[NO Sync, Iceberg Summit]" entries = no meeting.
- Per-meeting template (2026): V4 Progress Report / Highlights (Java, Python, Rust, Go, Cpp subsections; "Title (#PR) (Thanks X!)") / Releases / Discussion ("[Name] topic").
- Attendee lists only in 2021-era entries ("**Attendees**: ..."); modern signal = "[Name]" agenda owners + "Thanks X" credits.
- Range May 2020 – 2026-10-28; 3-weekly Wednesdays (10-07, 10-28 -> next 11-18). ~1000 unique GitHub PR/issue links + ~880 bare "#NNNNN" refs (repo implied by Java/Python/Rust/Go/Cpp subsection).
- 2026-10-28: V4 progress (needs consensus: column updates spec #16425, vector type; in progress: stats-only fields, V4 encryption, row timestamp, default value expressions, collations, derived columns). Discussion: [Russ] community health dashboard; [Szehon] derived/generated column RFC; [Andrei] collations PR #16972, CDC for V4 (kafka-connect); [Kevin] deprecate Avro/ORC in V4; [talat] review #18073.
- 2026-10-07: new PMC member Gang Wu; Summit 2027 CFP; releases Java 1.12, Go 0.7.0, C++ 0.4.0, Python 0.12.0; [Peter] spec release info (#18349 vs #18379); [Anurag] 1.13 release ~early Jan, Spark 4.2; Spark 3.5/4.0 retention; [Martin] Vortex file format proposal; [Dan] V4 timeline/scope.
- 2026-09-16: [Ryan] LLM contribution best practices (AGENTS.md, contribute page); Vortex; [Daehong] PositionDeleteIndex.forEachInRange #18027; [Neelesh] iceberg-verification shared testing repo; Rust 0.11 RC2.

## catalog (Iceberg Catalog Community Sync Notes)
- Single tab. Headings mixed: "## Nov 4, 2026", "## Oct 14, 2026 ([RECORDING](..))", "# Sep 23, 2026 (...)", "# 2026-07-22 ([RECORDING](..))" (ISO through Jul 2026, "Mon D, YYYY" since Aug). Newest first. Body: "Discussions:" / "Call for review:" bullets with "[Name] topic".
- Range 2024-09-04 – 2026-11-04 (recording not yet linked). ~3-weekly Wednesdays (next ~11-25). No attendee lists. YouTube playlist link in header.
- Nov 4: [Alex] BearerAuthManager (#18754) + downscoped OAuth2Manager v2 (#18756), design doc + ML threads; [Dhruv] should V4 IRC changes (#17642, #18782) go in a separate branch?
- Oct 14: V3 encryption for REST (hybrid mode flag?; server-vended KMS creds #17155); reviews: scan planning pre-signed URLs #17457 [William/Prashant], presign via sign endpoint #18080 [Sung/William], read-restrictions PR stack (github project 690).
- Sep 23: [Sung/Prashant] presigning URL spec; [Dan] V4 REST additions; [Prashant] trusted engine / OAuth token exchange; [Laurent] OAuth Manager v2 state; [talat] #18073.

## mv (Iceberg Materialized View Spec) — tabs "Agenda" + spec
- "## Nov 12, 2026" (newest first), older "## Jun 25, 2026 ([recording](..), [Gemini notes](..))" — many entries contain ONLY links to recordings/Gemini notes docs (content lives elsewhere).
- Nov 12 entry is pasted Granola notes: every line hyperlinked to PR #11041 and uses H1 "#" sub-headings inside the meeting (breaks heading hierarchy). Inconsistent date ("Monday (12th November)" vs "Monday 16th November").
- Range Oct 8, 2025 – Nov 12, 2026; ~biweekly Thursdays with gaps. Spec PR apache/iceberg#11041.
- Nov 12: vote readiness (approvals Steve, Russell; Dan/Ryan tagged; need 2-3 PMC +1); Jan to send vote email Mon Nov 16, 72h; MV spec independent of table V4 ("View V2"); REST MV spec separate workstream; impl status: Trino (Marius), Spark (Walaa/"Valah"), Flink (Talat, blocked on core), Snowflake waiting, AWS released, BigQuery PR in review; Spark availability ~1.13.
- Oct 29: simplify Appendix B examples (postgres; spark/trino), drop freshness dimensions; share with dev list. Oct 1: MV spec versioning, storage-table field location, Walaa's "serving policy", remove "freshness/staleness" terms.
- Drivers: Jan Kaul (owner), Walaa Eldin Moustafa, Daniel Weeks, Marius Grama, Talat, Nevin Zheng (Datastrato/Gravitino). Slack user links (apache-iceberg.slack.com/team/U...) appear as @mentions.

## index (Iceberg secondary indexes) — tabs "Design" + "Meeting notes"
- Meeting tab: "# Iceberg Index Support Sync" + proposed agenda, then H1 entries "# Nov 9, 2026", "# Oct 26, 2026([recording](..))" (no space before "("). Newest first.
- Range Feb 11, 2026 – Nov 9, 2026; biweekly Mondays (alternates with V4 sync). Owner Peter Vary (pvary).
- Nov 9: derived columns (index-schema only vs generic V4 schema change — Peter prefers V4); dev@ research on index scoping; decision proposal: nest index REST routes under table, names unique per table, optional listNamespaceIndexes (Dan +1); index catalog PR #16963 (Huaxin) with 11 design decisions; open Qs: table rename/drop, multi-table indexes, loadTable include-indexes.
- Oct 26: draft index spec #16961 open Qs: range-file boundaries (reuse partition fieldID 102), store range-file schema, allow stats-only fields (#18405). Sep 28: [talat] bounded overlap in region files; sort order; keep index type.

## vector (Iceberg Vector Type Support Proposal) — tabs "Design" + "Sync notes"
- Sync tab: plain date lines "Nov 19, 2026" / "Nov 5, 2026" / "Oct 22, 2026" / "Oct 8, 2026" (no heading style, no recording links). Newest first. Notes in bold = outcomes.
- **Nov 19, 2026 is a future agenda** (today 2026-11-13) — ingest must handle agenda-only/future entries.
- Range Oct 8 – Nov 5, 2026 (+Nov 19 agenda); biweekly Thu. Author Yan Yan; draft spec PR #18416; s.apache.org/iceberg-fileref.
- Nov 19 agenda: [Philipp] vector as primitive type in Java (#18676); [Alex] AI Functions (s.apache.org/iceberg-ai-functions).
- Nov 5: [Steven] consolidate with weekly V4 sync; [Peter] float16 test results (dev thread 4bwf1khh...); separating physical representation (float16/int8) from table-level type; priority "spec -> interoperability -> performance -> flexibility"; maybe V5.
- Oct 22: decided serialization `vector(float, 256)`; defaults restricted to null; primitive-vs-complex categorization deferred; lower-bit types: focus on float16 next (Peter); Philipp to share Java PR.
- Oct 8: consensus 1-D numeric, no null/NaN/Inf; no stats/distance metadata in spec; Avro via logical-type annotation; ORC unsupported; elements int/long/float/double.

## v4sfc (Iceberg Single File Commits) — 8 MB, ~11 tabs
- Tabs: design "Iceberg Single File Commits", "Meeting notes", "Ongoing Work" (V4 AMT status tables with emoji status), "Diagram Source", "(WIP Merge) Adaptive Metadata Tree", benchmarks, many appendices, "Tab 11". Size is mostly images/diagrams; text ~273k chars.
- Meeting tab: "##  Nov 2, 2026" (double space), "## Aug 24, 2026 \[[Recording](..)\]", "## Apr 3, 2026  [Recording](..)**:**". Newest first. Owner Russell Spitzer.
- Range Apr 3 – Nov 2, 2026; biweekly Mondays.
- Nov 2: encryption key metadata spec PR (Gabor); column files: no partial list/map updates, nested struct fields allowed; [DISCUSS] stop writing ORC/Avro data files in V4 (keep 2 formats? Vortex?).
- Oct 19: tight_bounds -> tight_stats consensus (Anoop spec PR, became #18585 merged). Oct 5: single modified_snapshot_id vs dv/column-file snapshot ids (Amogh); drop split_offsets/format_version for column files.
- Status tab: baseline AMT spec #16025 merged; #17783 forbid new equality deletes merged; root manifest encryption #18503 needs reviews; V4 file planner #17541 needs reviews; write adapters #16936 in progress.

## variant (Iceberg - Variant Community Update)
- Tabs: Overview (status: shipped per release, active work, next milestones; "Updated: Nov 4, 2026"), Active Work Tracker (per-repo issue/PR lists across iceberg, parquet, spark, hive, trino, arrow-*, iceberg-go/rust/python/cpp; "Active Contributors"), Meeting Notes, Benchmarks.
- Meeting tab: "## **Sep 3, 2026**" bold headings; sections **Agenda:** / **Meeting Notes** / **Meeting Recording (Youtube):** / ### Key Takeaways / ### Topics / Next Steps / Action Items (partly Gemini-generated). Monthly 1st Thursday: May 7, Jun 4, Jul 2, Aug 6, Sep 3 2026. No Oct/Nov entries.
- Sep 3: 1.12 RC blockers incl. UTF-8 byte-order fix (decided, no fallback; later merged #17726); PyIceberg variant blocked on Arrow C++ -> PyArrow chain (apache/arrow#50252, noted by Alex Stephen); vectorized shredded reads (Neelesh); row-group skipping; Spark 4.2 needed for pushdown (Qiegang).
- Status Nov 4: 1.12.0 (2026-09-29) shipped full shredded write path; next: vectorized shredded reads #18669, pushdown stack #16714/#16715/#15384/#15385, iceberg-rust/cpp variant reads. Driver: Neelesh Salian. ~440 PR/issue links -> rich edges.

## spark (Iceberg - Spark Community Sync Notes)
- Single tab; "## Nov 11, 2026", "## Sep 15, 2026 (Cancelled)", "## Mar 17, 2026 ([Recording](..))". Newest first. Sections ### Highlights (#### area subheads: DSv2, Write path, Reads...) / ### Discussion points / ### Review requests. Each PR line "Title ([#NNNNN](url))" + italic one-line impact.
- Range Jan 20 – Nov 11, 2026; monthly 3rd Tuesday. Owner Anurag Mantripragada. "Nov 11" is likely the prepared agenda for Nov 17 (written in first person, "Decide:").
- Nov 11: 1.13 freeze/branch; 1.12.1 for silent-data-loss fixes #18005/#18348?; Spark 4.2 tracker #17959 (DSv2 Transaction API #18385 0 reviews); Spark 4.3 (#18749, 661-file copy; propose wait for 4.4); wrong-result bugs needing reviewers (#18557, #18617, #18824, #18621/#18622, #18738).
- Oct 20: 4.2 items, should 4.2 jar ship with 1.13; shared Spark source POC (spark/common, dev thread 6dczl5fz...).

## readrestr (Read Restrictions: Community Syncs)
- Mixed: "## Aug 18, 2026", "## Aug 4, 2026 ([recording](..))", plain "Sep 15, 2026", "Jun 23, 2026([recording](..))". Newest first. Numbered agenda lists; some "### Notes" / "### Action Items" / "Follow Ups:".
- Range Feb 3 – Sep 15, 2026; biweekly Tue. Owner Prashant Singh; participants Nevin Zheng, Daniel, Laurent, Corey, Sung, Russell, Ryan.
- Sep 15: create GH project; volunteers PyIceberg (apache/iceberg-python#3967) and iceberg-rust (#3361); SDK target 1.13 for Actions API/REST scaffolding; mTLS #15235; "Do we need sync or just mailing list?". Sep 1: vote in progress (thread 0zloqhp8...); impl strategy (Java, PyIceberg, Rust; RCK). Spec #13879 merged by Sep 16 (community highlights).

## constraints (Constraint Support in Iceberg)
- Design doc ("Tab 1") + "Meeting notes" tab with only 2 entries: "## Jun 18, 2026 ([recording](..), [Gemini notes](..))", "## Jun 4, 2026 (...)". No inline notes. Owner Huaxin Gao. Design last edited Oct 10.

## colupdates (Efficient Column Updates in Iceberg)
- Tabs: design, Discarded options, Change Detection Scenarios, Column File Representation, Read path, Meeting Notes, Column Updates — Status. Meeting tab: "## Oct 20, 2026", "## Aug 25, 2026 (Cancelled)", "## Aug 11, 2026([recording](..))"; "### Topics (AI Generated)" + "Next Steps" with per-person owners.
- Range Jun 16 – Oct 20, 2026; biweekly Tue. Owner Anurag Mantripragada; Gábor Kaszab, Anoop Johnson, Steven Wu, Ryan.
- Oct 20: row timestamp; nested-type column updates (structs first); review spec #16425. Oct 6: simplify column file metadata (drop format_version; created+modified snapshot ids); read stitching (StitcherRegistry, RowAlignedStitchingIterable); commit API: simple update+append first. Sep 8: drop _pos field; equality deletes must be converted to DVs first.

## python (Iceberg python library syncs) — not in the calendar list
- "# Upcoming Syncs" (contains past dates too!) then "## Previous Sync Notes". Headings "## 10/27/2026", "## 09/30/2025", "##  4/28/2026" (M/D/YYYY, sometimes zero-padded, double spaces). Template: **Attendees**: / **Announcement** / **Agenda [please put the name in the front of the item]:**.
- Range 2021 – 10/27/2026; monthly last Tuesday. Attendee lists present in many 2024-2025 entries (empty template in recent ones).
- 10/27: 0.13 release ~early Dec; release-timeline docs (~3 months); release automation done; docs/DX; build infra (setup.py vs uv). 9/29: 0.13 planning (#3924), V3 write side, 1.0 public API boundary. 7/28: [Jared] pluggable backend architecture #3716; [Kevin] milestone 13.
