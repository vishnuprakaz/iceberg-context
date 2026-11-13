---
id: thread/t-97adb77b6cd93c6b
type: thread
title: Spec changes in release notes
date: '2026-10-01'
url: https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl
kind: release-planning
status: consensus
messages: 4
sources:
- devlist:0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl
refs:
- gh:apache/iceberg#14117
- gh:apache/iceberg#14048
- gh:apache/iceberg#14250
links:
- rel: discussed
  to: initiative/java-releases
  confidence: extracted
  source: devlist:0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl
- rel: discussed
  to: initiative/community-process
  confidence: extracted
  source: devlist:0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl
- rel: started_by
  to: person/pvary
  confidence: observed
updated: '2026-11-13'
---

# Spec changes in release notes

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Spec changes in release notes](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl) · **Started:** 2026-10-01 by [[person/pvary|Peter Vary]] · **Messages:** 4 (last 2026-10-01) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

While reviewing the 1.12.0 release notes, Péter Váry noticed that the Java binary release notes list spec changes, such as the SQL UDF specification (#14117), bringing back added-rows in snapshot fields (#14048) and clarified restrictions for geometry types in V3 (#14250). He called this misleading, because spec changes take effect when the vote happens and the PR merges, or when a spec version is finalized, and have no connection to Java binary releases. He proposed to stop including them in the Java release notes and suggested a separate page for spec version changes. Manu Zhang agreed, noting that the spec and the Java implementation live in one repository but are released separately. Szehon agreed as well. Kevin Liu agreed and suggested removing the spec entries retrospectively from the releases page and perhaps moving them to a changelog on the spec page. Nobody objected.

**Why it matters:** Release notes for Java releases are expected to stop listing spec changes, which may move to a changelog of their own.

## Outcome

All four participants agreed that spec changes should be left out of Java release notes; no PR or follow-up action is recorded in the thread.

## Positions

- **[[person/pvary|Peter Vary]]:** Stop listing spec changes in Java release notes, since spec changes are not tied to Java binary releases, and give them a dedicated page. ([message](https://lists.apache.org/thread/0r9fhdb1zc74ycz0hx2wyl1xyn48jyxl))
- **[[person/manuzhang|Manu Zhang]]:** Agrees; the spec and Java implementation share a repository but are released separately, so their notes should be separated. ([message](https://lists.apache.org/thread/mp9fsgjm9bbtrk4rctrd0ho9p4rg9kjr))
- **[[person/kevinjqliu|Kevin Liu]]:** Agrees, and suggests removing spec entries from past release notes and possibly moving them to a changelog on the spec page. ([message](https://lists.apache.org/thread/1zs16ykm5dv065djhoqbx8r82sv1r3w0))

References: [iceberg#14117](https://github.com/apache/iceberg/issues/14117), [iceberg#14048](https://github.com/apache/iceberg/issues/14048), [iceberg#14250](https://github.com/apache/iceberg/issues/14250)
<!-- kb:generated:end -->

## Notes
