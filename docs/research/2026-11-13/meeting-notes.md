# Working-group syncs: calendar and notes docs (2026-11-13)

## How the community meets
The public **Iceberg Dev Events** Google Calendar lists every recurring working-group sync. Each event links a Google Doc of running notes, and most syncs are recorded to YouTube. Between 2026-09-13 and 2026-12-13 it had 53 events:

| Sync | Cadence | Notes doc |
|---|---|---|
| Community Sync (main, recorded) | every ~3 weeks, Wed | `1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg` |
| Catalog Community Sync | every ~3 weeks, Wed | `1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw` |
| MV (materialized views) | ~2 weeks, Thu | `1UnhldHhe3Grz8JBngwXPA6ZZord1xMedY5ukEhZYF-A` |
| Index Support | 2 weeks, Mon | `1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0` |
| File and Vector Type | 2 weeks, Thu | `1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE` (s.apache.org/iceberg-fileref) |
| V4 Metadata / AMT / Single File Commits | 2 weeks, Mon (alternates with Index) | `1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw` ("Meeting notes" tab) |
| Variant | monthly, 1st Thu | `1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s` |
| Spark | monthly, 3rd Tue | `19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4` |
| Efficient Column Updates | 2 weeks, Tue | `1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs` |
| Python library sync | monthly, last Tue | `1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U` |
| Rust Community Sync | ~monthly | (no notes doc; recorded) |
| Read Restrictions | 2 weeks, Tue; looks dormant | `1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c` |
| Constraints | dormant since 2026-06 | `1re65fx3uqC7I_tJuS79IxLiB7HEN2Grt5qRIDjd3p-4` |

Related docs:
- Polaris Community Sync (`1TAAMjCtk4KuWSwfxpCBhhK9vM1k_3n7YE4L28slclXU`)
- Collation Support proposal (`1m8b7u97uteHYjXk-4DNglJSpQO8OcZOCzW2tApCNTW4`)
- Arrow and PyArrow community meeting notes

There are no notes docs for Rust, Go or C++. Their news appears in the Community Sync highlights.

## Doc structure (parseability)
- **Layout:** every doc puts the newest entry first, with one dated section per meeting.
- **Heading formats vary:**
  - Formats: `2026-10-28 ([Recording](..))`, `## Nov 4, 2026`, `# Nov 9, 2026`, plain-text `Nov 5, 2026`, `## **Sep 3, 2026**`, `## 10/27/2026`.
  - Dates can be Docs date chips.
  - Some formats changed over the years.
- **Sections inside a meeting:** Agenda / Highlights / Discussion / Key Takeaways / Next Steps / Action items. Some are AI-generated (Gemini, Granola, "Topics (AI Generated)").
- **Attendee lists are rare.** Use these participation signals instead:
  - `[Name] topic` agenda prefixes
  - "(Thanks X!)" credits in highlights
  - per-person Next Steps
  - person chips
- **Dense with outbound links (graph edges):**
  - Community Sync: about 1,000 GitHub PR/issue URLs plus about 880 bare `#NNNNN` refs, whose repo is inferred from the Java/Python/Rust/Go/C++ subsection.
  - Variant: about 440 links across iceberg, parquet, spark, trino, arrow and the sibling Iceberg repos.
  - Links to dev@ threads, YouTube recordings and other Docs.

Per-doc details and the latest meetings are in [meeting-notes-per-doc.md](meeting-notes-per-doc.md).

## What the working groups are doing now (Nov 2026)
- **V4 spec:**
  - Merged: the AMT baseline (#16025), the ban on new equality deletes (#17783) and tight_stats (#18585).
  - In review: the V4 file planner (#17541) and write adapters (#16936).
  - Column updates (#16425): rules agreed (dense column files, no `_pos`, structs first).
  - Also open: root-manifest encryption (#18503), stats-only fields, row timestamp (#18526), derived/generated columns RFC, collations (#16972), and whether to deprecate ORC/Avro data files (Vortex was proposed).
- **New types and features:**
  - Vector type (`vector(float, 256)`, Java PR #18676).
  - Secondary indexes (REST routes under the table; #16963, #16961).
  - Materialized views: vote planned around mid-November on PR #11041.
  - Read restrictions: spec merged (#13879). Implementation is split across Java, PyIceberg (iceberg-python#3967) and Rust.
  - Constraints.
- **Releases:**
  - Java 1.13 targeted for around early January with Spark 4.2. A possible 1.12.1 is under discussion for the data-loss fixes #18005 and #18348.
  - PyIceberg 0.13 targeted for early December, with V3 writes and a 1.0 API boundary under discussion.
- **Catalog/REST:** BearerAuthManager and OAuth2 v2, pre-signed URLs and sign endpoint, KMS credential vending for V3 encryption, and whether V4 REST changes go on a branch.
- **Variant:** 1.12 shipped the shredded write path. Next are vectorized shredded reads and pushdown. PyIceberg variant is blocked on PyArrow (apache/arrow#50252).
- **Process:** LLM/AI contribution guidance and AGENTS.md, plus a community health dashboard.

## Ingestion recommendations
1. **Use `read_doc` JSON, not the text export.**
   - The JSON has `revisionId`, the tab tree, heading styles and date chips.
   - The text export flattens tabs and cut off the end of the largest doc.
   - Configure which tab holds the notes for each doc.
2. **Detect changes cheaply.** Poll `get_file_metadata` for `modifiedTime`, then fetch. `list_file_revisions` is unreliable here, so store the doc `revisionId` instead.
3. **Split each doc into meetings with a tolerant date matcher.** Hash each section so edits to old meetings are picked up too.
4. **Classify each entry's status:** held / cancelled / agenda-only or future / link-only. Re-ingest future and agenda-only entries after the meeting date.
5. **Normalize the links:**
   - Resolve bare `#NNNNN` refs by subsection language.
   - Dedupe PR URLs.
   - Store Slack/YouTube/Docs links as typed edges.
6. **Discovery is partly manual.** Drive search misses some docs. Keep a seed list, and add docs found through calendar descriptions and cross-doc links.
7. **Privacy:** the docs contain email addresses in person chips and mailto links. Strip them and keep only names and GitHub handles.
8. **Mark provenance on AI-generated sections.**
