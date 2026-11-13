---
id: initiative/materialized-views
type: initiative
title: Materialized views
status: design
updated: '2026-11-13'
sources:
- meeting/materialized-views/2026-07-07
- meeting/spark/2026-08-18
- meeting/materialized-views/2026-09-17
- meeting/materialized-views/2026-10-01
- meeting/materialized-views/2026-10-29
- meeting/materialized-views/2026-11-12
links:
- rel: handled_by
  to: group/materialized-views
  confidence: extracted
  source: meeting/materialized-views/2026-11-12
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: meeting/materialized-views/2026-11-12
- rel: touches
  to: module/iceberg/spark
  confidence: extracted
  source: meeting/spark/2026-08-18
- rel: tracked_in
  to: gh:apache/iceberg#11041
  confidence: extracted
  source: meeting/materialized-views/2026-11-12
---

# Materialized views

<!-- kb:generated:start -->
## What it is

A materialized view is a view whose query result is also stored in a storage table, so engines can read the stored result when it is still usable ([materialized-views sync 2026-10-01](../records/meetings/materialized-views/2026/2026-10-01.md)). The working group is finishing a spec for how this is represented; it is framed as an extension of the view spec, independent of the table spec and V4, using existing snapshot properties and no new table-side metadata ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).

## Current state

- The spec pull request [#11041](https://github.com/apache/iceberg/pull/11041) has approvals from two PMC members, and the group agreed on 12 November to stop preparing and send the vote; Jan Kaul is to send the vote email on a Monday (the notes give both 12 and 16 November) with a 72-hour window ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)). No vote thread is on record yet.
- The spec will not define freshness: the description of its two dimensions is replaced by a statement that the spec does not define it ([materialized-views sync 2026-10-29](../records/meetings/materialized-views/2026/2026-10-29.md)).
- Whether the materialized view spec depends on table spec versions was raised on the dev list; the notes say the reply suggests no impact ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).
- The REST spec for materialized views still needs to be defined, as a separate workstream ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).
- Implementations: Trino and Spark implementations exist, Flink work is waiting on Iceberg core changes, and the best case for Spark availability is Iceberg 1.13 ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)). In August the Spark materialized views pull request had 37 reviews and one approval ([spark sync 2026-08-18](../records/meetings/spark/2026/2026-08-18.md)).

## Timeline

- 2026-07-07: Contributors from the Apache Gravitino community introduce themselves and offer help with documentation, alignment and implementation ([materialized-views sync 2026-07-07](../records/meetings/materialized-views/2026/2026-07-07.md)).
- 2026-09-17: The group asks everyone interested to review the spec pull request again so that a vote can start in two weeks ([materialized-views sync 2026-09-17](../records/meetings/materialized-views/2026/2026-09-17.md)).
- 2026-10-01: Sequence agreed: finish the wording, working group approves the pull request, further review, then a vote on the mailing list ([materialized-views sync 2026-10-01](../records/meetings/materialized-views/2026/2026-10-01.md)).
- 2026-10-29: Appendix B examples simplified; the freshness description is to be removed; the spec goes to the dev list after internal consent ([materialized-views sync 2026-10-29](../records/meetings/materialized-views/2026/2026-10-29.md)).
- 2026-11-12: Consensus to send the vote and let the process run ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).

## Where help is needed

- Reviews of the Iceberg core pull requests that the Flink implementation is waiting on; the 12 November notes ask to push them forward ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).
- Defining the REST spec for materialized views, which the notes list as still to be done ([materialized-views sync 2026-11-12](../records/meetings/materialized-views/2026/2026-11-12.md)).
<!-- kb:generated:end -->

## Notes
