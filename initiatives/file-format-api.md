---
id: initiative/file-format-api
type: initiative
title: File Format API and new file formats
status: discussion
updated: '2026-11-13'
sources:
- meeting/community/2026-05-13
- meeting/python/2026-05-26
- meeting/community/2026-06-03
- meeting/community/2026-06-24
- meeting/python/2026-06-30
- meeting/community/2026-08-05
- thread/t-5c70639b9c0f57ff
- thread/t-f9e1b8daeae100d8
- meeting/column-updates/2026-09-08
- meeting/column-updates/2026-10-06
- meeting/community/2026-10-07
- meeting/file-vector-type/2026-10-08
- meeting/community/2026-10-28
- meeting/v4-metadata/2026-11-02
links:
- rel: championed_by
  to: person/kevinjqliu
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: championed_by
  to: person/stevenzwu
  confidence: extracted
  source: thread/t-5c70639b9c0f57ff
- rel: handled_by
  to: group/community
  confidence: extracted
  source: meeting/community/2026-10-28
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-11-02
- rel: touches
  to: module/iceberg/orc
  confidence: inferred
  source: meeting/community/2026-10-28
- rel: touches
  to: module/iceberg/parquet
  confidence: inferred
  source: thread/t-5c70639b9c0f57ff
- rel: tracked_in
  to: gh:apache/iceberg-python#3381
  confidence: extracted
  source: meeting/python/2026-06-30
---

# File Format API and new file formats

<!-- kb:generated:start -->
## What it is

Iceberg reads and writes data in several file formats (Parquet, Avro and ORC) ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The File Format API puts file formats behind a common interface, a format model registered in a registry, in both the Java library and PyIceberg ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs); [thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)). On top of that, the community is discussing which formats to carry forward: a proposal to add Vortex, and whether V4 should drop ORC and Avro for data files ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Current state

- Released in PyIceberg: 0.12.0 lists a new File Format API among its highlights ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)); the community sync notes list an initial pluggable file format writer API ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and a `ParquetFormatModel` using the format API ([iceberg-python #3381](https://github.com/apache/iceberg-python/pull/3381)) among the PyIceberg changes ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Java: TCK tests for schema evolution in the format model tests were merged ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The column updates read path is built above the `FormatModelRegistry`, which stays responsible for reading single physical files ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)); the `DataFileReadBuilder` is approved for data files only, while delete files go directly to the registry ([column updates sync 2026-10-06](../records/meetings/column-updates/2026/2026-10-06.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- Settled for metadata: V4 manifests are written in Parquet under the merged adaptive metadata tree spec ([#16025](https://github.com/apache/iceberg/pull/16025)); upgraded tables can keep existing Avro manifests, but new or rewritten manifests must be Parquet ([thread 2026-08-11](../records/threads/2026/08/discuss-should-v4-manifests-be-parquet-only-5c7063.md), [dev list](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y)).
- Open: deprecating ORC and Avro as data file formats in V4. At the community sync one participant objected that Iceberg risks overfitting to Parquet and suggested externally maintained plugins, and Steven Wu supported removing ORC in V4 while keeping Avro for now; nothing was decided ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). The V4 metadata sync discussed the dev list thread ([dev list](https://lists.apache.org/thread/5jfzckl0cc9z683kz9vfv41pmhrm1tdb)) and recorded no conclusion ([V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- Open: the proposal to add Vortex as an Iceberg file format has been on the community sync agenda since June, and its author started a dev list discussion ([dev list](https://lists.apache.org/thread/pb66o8gk8nqc6yormfld7pkt6rdfkvh7)) in October; the notes record no outcome ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Open: both syncs asked what the requirements are for a file format to count as supported ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- Related: for the vector type, the rule discussed is to support the type in all supported file formats, and it was suggested, as a question, that vector be left unsupported for ORC ([file and vector type sync 2026-10-08](../records/meetings/file-vector-type/2026/2026-10-08.md), [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).

## Timeline

- 2026-05-13: Vortex integration was an agenda item at the community sync; the notes give no details ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-05-26: review was requested at the PyIceberg sync for the File Format for Parquet pull request ([iceberg-python #3381](https://github.com/apache/iceberg-python/pull/3381)) ([PyIceberg sync 2026-05-26](../records/meetings/python/2026/2026-05-26.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-06-03: deprecating ORC was an agenda item at the community sync; no details are recorded ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-24: a proposal document for adding Vortex as an Iceberg file format was shared at the community sync ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-30: the File Format for Parquet pull request was again listed as needing review ([PyIceberg sync 2026-06-30](../records/meetings/python/2026/2026-06-30.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-08-05: the community sync notes list a `ParquetFormatModel` using the format API among the PyIceberg changes ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-08-11: Steven Wu asked on the dev list whether V4 manifests should be Parquet-only ([thread 2026-08-11](../records/threads/2026/08/discuss-should-v4-manifests-be-parquet-only-5c7063.md), [dev list](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y)).
- 2026-08-24: the PyIceberg 0.12.0 RC2 vote listed the new File Format API among the highlights ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)).
- 2026-09-08: the column updates sync decided to build the column file read path above the `FormatModelRegistry` ([column updates sync 2026-09-08](../records/meetings/column-updates/2026/2026-09-08.md), [notes](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)).
- 2026-10-07: the Vortex proposal's author told the community sync he had started a dev list discussion and asked people interested in new file formats to reply there ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-20: Kevin Liu reported in the Parquet-only manifests thread that the merged spec has V4 manifests written in Parquet, and proposed also dropping ORC and Avro data files in V4; others asked for a separate thread ([thread 2026-08-11](../records/threads/2026/08/discuss-should-v4-manifests-be-parquet-only-5c7063.md), [dev list](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y)).
- 2026-10-28: the community sync discussed deprecating Avro and ORC data files in V4 without a decision; Kevin Liu took the action to start a dev list thread ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-02: the V4 metadata sync discussed the dev list thread on stopping ORC and Avro data file writes in V4; no conclusion is recorded ([V4 metadata sync 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md), [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).

## Where help is needed

- People interested in Vortex, or in adding new file formats in general, were asked to reply on the dev list thread ([dev list](https://lists.apache.org/thread/pb66o8gk8nqc6yormfld7pkt6rdfkvh7)) ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Input was asked for on deprecating ORC and Avro data files in V4 and on criteria for what supporting a file format means ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [dev list](https://lists.apache.org/thread/5jfzckl0cc9z683kz9vfv41pmhrm1tdb)).
<!-- kb:generated:end -->

## Notes
