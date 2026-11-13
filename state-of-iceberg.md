# State of Apache Iceberg

As of 2026-11-13. This page is rewritten on every sync run; every line points at the page or record it comes from.

## Source freshness

From `kb status` on 2026-11-13: all eight collectors last succeeded less than an hour before this page was written.

| Source | Status | Records reach |
|---|---|---|
| Dev list (`devlist`) | ok | emails to 2026-11-13 |
| GitHub (`github`) | ok, backfill in progress | apache/iceberg pull requests to 2026-11-13; issues only to 2025-11-07 |
| Git history (`git`) | ok | commits to 2026-11-13 |
| Spec (`spec`) | ok | 518 sections, to 2026-11-11 |
| ASF roster (`asf`) | ok | `committers_total=40, pmc=26`, roster records to 2026-09-16 |
| Working-group notes (`syncdocs`) | ok | 12 groups, 318 meetings, notes to 2026-11-19 |
| Calendar (`calendar`) | ok | 53 events, to 2026-12-10 |
| Recordings (`youtube`) | ok | 3 transcripts, to 2026-11-09 |

Limits that affect this page: apache/iceberg issues are only partly synced and apache/iceberg-python pull requests are not synced, so statements about PyIceberg, Go, Rust and C++ work come from meeting notes and dev list threads, not from GitHub state. The generated release pages stop at PyIceberg 0.9.1 ([release page](releases/iceberg-python-0.9.1.md)) and Go 0.5.0 ([release page](releases/iceberg-go-0.5.0.md)); later versions below are taken from meeting notes.

## Releases

| Implementation | Last release | Next release |
|---|---|---|
| Java | 1.12.0, announced 2026-10-01 ([release page](releases/iceberg-1.12.0.md)) | 1.13: a release manager is named, the date (end of year or early January) is not settled, and on 2026-11-11 there was no release candidate, branch or freeze date ([Java releases](initiatives/java-releases.md); [Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)) |
| PyIceberg | 0.12.0, marked done on 2026-09-16 ([PyIceberg roadmap](initiatives/pyiceberg.md); [community sync 2026-09-16](records/meetings/community/2026/2026-09-16.md)) | 0.13, with "Early December?" on the sync agenda and no recorded decision ([PyIceberg sync 2026-10-27](records/meetings/python/2026/2026-10-27.md)) |
| Rust | 0.11.0, announced 2026-11-04 ([release page](releases/iceberg-rust-0.11.0.md); [announcement](https://lists.apache.org/thread/lm4sskbfojckzmo6l3fkko1wcoz5v8h6)) | none on record ([Iceberg Rust](initiatives/iceberg-rust.md)) |
| Go | 0.7.0, release blog post linked on 2026-10-07 ([Iceberg Go](initiatives/iceberg-go.md); [community sync 2026-10-07](records/meetings/community/2026/2026-10-07.md)) | v1, reported as planned "around the next community sync" after API cleanup ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)) |
| C++ | 0.4.0, dated 2026-09-26 ([release page](releases/iceberg-cpp-0.4.0.md)) | a smaller follow-up release in late October was the release manager's stated preference; no record of it exists ([Iceberg C++](initiatives/iceberg-cpp.md)) |
| Terraform provider | 0.2.0, dated 2026-11-04 ([release page](releases/terraform-provider-iceberg-0.2.0.md)) | none on record |

- Java patch lines: whether to cut a 1.12.1 for two silent-data-loss fixes ([#18005](https://github.com/apache/iceberg/pull/18005), [#18348](https://github.com/apache/iceberg/pull/18348)) that are in no release was asked on 2026-11-11 with no recorded outcome ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)).
- Java patch lines: 1.11.1 and 1.10.3 were agreed in June and no release candidate for either is on record ([Java releases](initiatives/java-releases.md)).

## Votes

Open or expected:

- `_last_updated_time` row lineage column for V4 ([#18526](https://github.com/apache/iceberg/pull/18526)): the vote started on 2026-10-30 and no result message is on record; the last message says the change needs more editing ([thread](records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md); [V4 row timestamps](initiatives/v4-row-lineage-timestamps.md)).
- Materialized view spec ([#11041](https://github.com/apache/iceberg/pull/11041)): the working group agreed on 2026-11-12 to send the vote email on the following Monday (inferred: 2026-11-16) with a 72-hour window; no vote thread is on record yet ([materialized views sync 2026-11-12](records/meetings/materialized-views/2026/2026-11-12.md)).

Closed in the last 30 days (from `kb whats-new --since 30d`):

- Default value expressions for V4 ([#16777](https://github.com/apache/iceberg/pull/16777)): passed on 2026-11-06 with 11 binding and 7 non-binding +1 votes ([result](https://lists.apache.org/thread/h5jnk7l2op325x545hfnrpbo3qmh2ovo), `devlist:h5jnk7l2op325x545hfnrpbo3qmh2ovo`); the spec change was merged the same day (git history, `kb whats-new`).
- Stats-only fields for V4 ([#18405](https://github.com/apache/iceberg/pull/18405)): passed on 2026-10-31 with 15 +1 votes ([result](https://lists.apache.org/thread/d90t8lbgomb23d8dtllnncsbx27g69k3), `devlist:d90t8lbgomb23d8dtllnncsbx27g69k3`).
- File-level `tight_stats` for V4 ([#18585](https://github.com/apache/iceberg/pull/18585)): passed on 2026-10-27 with 9 binding and 4 non-binding +1 votes ([result](https://lists.apache.org/thread/g7qvlhkt3kchgf7sgjdcr0z9sksbqgq6), `devlist:g7qvlhkt3kchgf7sgjdcr0z9sksbqgq6`).
- Table constraints in the V4 spec ([#17822](https://github.com/apache/iceberg/pull/17822)): passed with 8 +1 votes, 5 binding ([thread](records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md)).
- `none` as a value of `X-Iceberg-Access-Delegation` ([#18480](https://github.com/apache/iceberg/pull/18480)): passed with 7 +1 votes, 3 binding ([thread](records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md)).
- FILE type in the V4 spec ([#17918](https://github.com/apache/iceberg/pull/17918)): passed on 2026-10-19 with 8 binding and 19 non-binding +1 votes and one non-binding +0 ([result](https://lists.apache.org/thread/6b63cbcsf0l69z9hs6v9nc1gp4y96tlp), `devlist:6b63cbcsf0l69z9hs6v9nc1gp4y96tlp`).
- Iceberg Rust 0.11.0 RC3: the release manager reported the vote as passed ([thread](records/threads/2026/10/vote-release-apache-iceberg-rust-0-11-0-rc3-60b37c.md)).
- Terraform provider v0.2.0 RC1: passed with 4 binding +1 votes ([thread](records/threads/2026/10/vote-terraform-release-apache-iceberg-terraform-provider-v0-2-0-rc1-a9927e.md)).
- Standard User-Agent format for REST clients ([#17727](https://github.com/apache/iceberg/pull/17727)): the reopened vote has only +1 replies and no result message on record ([thread](records/threads/2026/10/vote-recommend-a-standard-user-agent-format-for-rest-clients-reopen-ef8a98.md)); git history shows the OpenAPI change merged on 2026-11-10 (`kb whats-new`).

## Active initiatives

One line per initiative; the status word is the one on the initiative page.

### V4 table format

- [V4 spec: planning and other changes](initiatives/v4-general.md) (design): scope and timeline are not decided; running V4 with a release manager was suggested and not decided ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- [Adaptive metadata tree and single-file commits](initiatives/v4-metadata-tree.md) (implementing): the baseline spec and the first Java building blocks are merged; `Snapshot.rootManifestLocation()` ([#17523](https://github.com/apache/iceberg/pull/17523)) merged on 2026-11-13 (git history, `kb whats-new`).
- [Efficient column updates](initiatives/v4-column-updates.md) (design): the spec pull request [#16425](https://github.com/apache/iceberg/pull/16425) needs review before a vote ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)); the Java pull request for basic column file fields, [#16285](https://github.com/apache/iceberg/pull/16285), merged on 2026-11-05 (GitHub record `gh:apache/iceberg#16285`).
- [Statistics redesign](initiatives/v4-content-stats.md) (implementing): stats-only fields and file-level `tight_stats` both passed their votes and the Java implementation of `tight_stats` ([#18598](https://github.com/apache/iceberg/pull/18598)) merged on 2026-11-10 (results above; git history, `kb whats-new`).
- [Default value expressions](initiatives/v4-default-expressions.md) (vote on the page; the result is now on record): passed on 2026-11-06 and merged ([result](https://lists.apache.org/thread/h5jnk7l2op325x545hfnrpbo3qmh2ovo)).
- [Row timestamps and monotonic snapshot timestamps](initiatives/v4-row-lineage-timestamps.md) (vote): monotonic snapshot timestamps are decided; the `_last_updated_time` vote has no result on record ([thread](records/threads/2026/10/vote-spec-add-last-updated-time-row-lineage-metadata-column-in-v4-447ec5.md)).
- [Deprecating equality deletes](initiatives/v4-equality-deletes.md) (accepted): new equality deletes are forbidden in V4; a clarification of the row-level delete sections ([#18301](https://github.com/apache/iceberg/pull/18301)) merged on 2026-11-04 (git history, `kb whats-new`).
- [Relative paths](initiatives/v4-relative-paths.md) (implementing): the spec change is merged and the REST side waits on [#17642](https://github.com/apache/iceberg/pull/17642) ([thread](records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md)).
- [Table encryption](initiatives/v4-encryption.md) (design): a spec pull request for encryption key metadata is ready for more reviews ([V4 metadata sync 2026-11-02](records/meetings/v4-metadata/2026/2026-11-02.md)).
- [Table constraints](initiatives/constraints.md) (accepted): the V4 spec change passed its vote; no implementation work is on record yet ([thread](records/threads/2026/10/vote-add-table-constraints-to-the-v4-table-spec-9704ae.md)).
- [File type](initiatives/file-type.md) (accepted): in the V4 spec; a batch remote signing endpoint that follows from it is still under discussion ([thread](records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md)).
- [Vector type](initiatives/vector-type.md) (design): narrow element types such as int8 and float16 are the open question ([file and vector type sync 2026-11-05](records/meetings/file-vector-type/2026/2026-11-05.md)).
- [Collations](initiatives/collations.md) (design): the spec pull request [#16972](https://github.com/apache/iceberg/pull/16972) now builds on stats-only fields; how bounds are stored and whether it must be part of V4 are open ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- [Secondary indexes](initiatives/secondary-indexes.md) (design): REST routes nest under the table and derived columns were taken out of the index spec; neither spec pull request has gone to a vote ([index sync 2026-11-09](records/meetings/index/2026/2026-11-09.md)).
- [Expressions spec](initiatives/expressions-spec.md) (accepted): adopted; default value expressions, read restrictions and index keys build on it ([Expressions specification](initiatives/expressions-spec.md)).

### Catalog and REST

- [REST catalog spec: other changes](initiatives/rest-spec.md) (implementing): whether V4 REST changes go into a separate branch was asked on 2026-11-04 with no recorded answer ([catalog sync 2026-11-04](records/meetings/catalog/2026/2026-11-04.md)).
- [REST authentication and credentials](initiatives/rest-auth.md) (implementing): a BearerAuthManager ([#18754](https://github.com/apache/iceberg/pull/18754)) and a downscoped OAuth2 manager ([#18756](https://github.com/apache/iceberg/pull/18756)) are in review ([catalog sync 2026-11-04](records/meetings/catalog/2026/2026-11-04.md)).
- [Read restrictions](initiatives/read-restrictions.md) (implementing): the spec change is merged and the Java pull request stack is out for review ([catalog sync 2026-10-14](records/meetings/catalog/2026/2026-10-14.md)).
- [Catalog labels](initiatives/catalog-labels.md) (implementing): labels are in the REST spec; the REST server test fixture now emits them ([#18047](https://github.com/apache/iceberg/pull/18047), merged 2026-11-09 per git history, `kb whats-new`).
- [SQL UDFs in catalogs](initiatives/udf.md) (implementing): list and load endpoints are in the REST spec; create, update and delete endpoints were left for a later proposal ([thread](records/threads/2026/03/vote-rest-spec-add-list-and-load-function-endpoints-61befd.md)).
- [Materialized views](initiatives/materialized-views.md) (design): the spec is about to go to a vote; the REST spec for materialized views is still to be defined ([materialized views sync 2026-11-12](records/meetings/materialized-views/2026/2026-11-12.md)).

### Engines, formats and types

- [Spark integration](initiatives/spark-integration.md) (implementing): what gates publishing Spark 4.2 support, and whether to add Spark 4.3, are open ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)).
- [Flink integration](initiatives/flink-integration.md) (implementing): the Flink materialized view implementation waits on Iceberg core changes ([materialized views sync 2026-11-12](records/meetings/materialized-views/2026/2026-11-12.md)).
- [Kafka Connect sink](initiatives/kafka-connect.md) (discussion): CDC writes that never commit equality deletes are proposed in [#18003](https://github.com/apache/iceberg/pull/18003), with no decision ([thread](records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md)).
- [File Format API and new file formats](initiatives/file-format-api.md) (discussion): whether V4 stops writing ORC and Avro data files, and what it means to support a file format, are open ([V4 metadata sync 2026-11-02](records/meetings/v4-metadata/2026/2026-11-02.md)).
- [Variant](initiatives/variant.md) (released): shipped in Java; PyIceberg support is blocked on Arrow C++ work ([variant sync 2026-09-03](records/meetings/variant/2026/2026-09-03.md)).
- [Geospatial types](initiatives/geospatial.md) (implementing): Parquet writers now emit geometry bounds ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)); vectorized geo reads in Spark are not picked up ([Spark sync 2026-08-18](records/meetings/spark/2026/2026-08-18.md)).

### Implementations and testing

- [Java releases](initiatives/java-releases.md) (released): see the release table above.
- [PyIceberg](initiatives/pyiceberg.md) (released): 0.13 planning, the V3 write side and the meaning of 1.0 are on the sync agendas without recorded outcomes ([PyIceberg sync 2026-09-29](records/meetings/python/2026/2026-09-29.md); [PyIceberg sync 2026-10-27](records/meetings/python/2026/2026-10-27.md)).
- [Iceberg Rust](initiatives/iceberg-rust.md) (implementing): 0.11.0 is out with client-side encryption writes and incremental V3 support ([announcement](https://lists.apache.org/thread/lm4sskbfojckzmo6l3fkko1wcoz5v8h6), `devlist:lm4sskbfojckzmo6l3fkko1wcoz5v8h6`).
- [Iceberg Go](initiatives/iceberg-go.md) (released): API cleanup toward v1 ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- [Iceberg C++](initiatives/iceberg-cpp.md) (implementing): scan plan endpoint and encryption work were the latest highlights ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- [Shared conformance testing](initiatives/conformance-testing.md) (implementing): fixture work surfaced two spec ambiguities now on the dev list, name mapping for files that carry only some field IDs ([thread](records/threads/2026/11/discuss-name-mapping-for-data-files-that-carry-only-some-field-ids-14cfe6.md)) and rounding before bucket hashing of nanosecond timestamps ([thread](https://lists.apache.org/thread/hcc1yo2pcyrc089rgywo8nh0tt9gs5yl), `devlist:hcc1yo2pcyrc089rgywo8nh0tt9gs5yl`).

### Community

- [Community process, health and events](initiatives/community-process.md) (discussion): a health dashboard showed falling retention of new contributors and a large stale pull request backlog; whether and how to act is open ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- [AI-assisted contributions](initiatives/ai-contributions.md) (discussion): `AGENTS.md` rules are merged; a proposal to switch off automatic Copilot reviews in iceberg-cpp was posted on 2026-11-13 ([thread](https://lists.apache.org/thread/6sbp6m633mpdrbwbq898frh9ogppb0r7), `devlist:6sbp6m633mpdrbwbq898frh9ogppb0r7`).

## Working groups meeting in the next two weeks

From `kb upcoming` on 2026-11-13; times are UTC.

| Date | Meeting | Group page | Last notes on record |
|---|---|---|---|
| 2026-11-17 17:00 | V4 Metadata Sync | [V4 Metadata](groups/v4-metadata.md) | [2026-11-02](records/meetings/v4-metadata/2026/2026-11-02.md) |
| 2026-11-18 17:00 | Iceberg Community Sync | [Community](groups/community.md) | [2026-10-28](records/meetings/community/2026/2026-10-28.md) |
| 2026-11-19 17:00 | File and Vector Type Sync | [File and Vector Type](groups/file-vector-type.md) | [2026-11-05](records/meetings/file-vector-type/2026/2026-11-05.md); an agenda record for 2026-11-19 exists (`meet:file-vector-type:2026-11-19`) |
| 2026-11-23 17:00 | Index Support Sync | [Index Support](groups/index.md) | [2026-11-09](records/meetings/index/2026/2026-11-09.md) |
| 2026-11-24 17:00 | V4 Metadata Sync | [V4 Metadata](groups/v4-metadata.md) | [2026-11-02](records/meetings/v4-metadata/2026/2026-11-02.md) |
| 2026-11-24 17:00 | PyIceberg Sync | [PyIceberg](groups/python.md) | [2026-10-27](records/meetings/python/2026/2026-10-27.md) |
| 2026-11-25 17:00 | Catalog Community Sync | [Catalog](groups/catalog.md) | [2026-11-04](records/meetings/catalog/2026/2026-11-04.md) |
| 2026-11-26 17:00 | Materialized View Sync | [Materialized Views](groups/materialized-views.md) | [2026-11-12](records/meetings/materialized-views/2026/2026-11-12.md) |

- Not in this window: the Spark Community Sync, which last met on 2026-11-11 ([Spark group](groups/spark.md)), and the Iceberg Rust Community Sync, next listed for 2026-12-03 ([Rust group](groups/rust.md)).
- The Variant sync is cancelled for December and resumes in January 2027 ([Variant](initiatives/variant.md)).
- The Read Restrictions sync has no notes since 2026-09-15 and asked then whether it is still needed ([read restrictions sync 2026-09-15](records/meetings/read-restrictions/2026/2026-09-15.md)).

## Process changes

- Spec votes for V4 are taken as agreement on direction, with changes possible until the whole V4 spec is finalized ([V4 statistics redesign](initiatives/v4-content-stats.md); [V4 relative paths](initiatives/v4-relative-paths.md)).
- Spec changes are to leave the Java release notes; two alternative layouts, [#18349](https://github.com/apache/iceberg/pull/18349) and [#18379](https://github.com/apache/iceberg/pull/18379), are pending ([community sync 2026-10-07](records/meetings/community/2026/2026-10-07.md)).
- Spark versions: the dev list converged on supporting the last Spark LTS plus the two latest minors ([thread](records/threads/2026/06/discuss-spark-versioning-strategy-with-accelerated-spark-releases-3f1ab7.md)).
- AI-assisted contributions: disclosure, testing and Javadoc rules were added to `AGENTS.md` in the Java repository ([community sync 2026-10-07](records/meetings/community/2026/2026-10-07.md)).
- Iceberg Rust limits users without write access to three open non-draft pull requests ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- CI: Java CI moved to ubuntu-24.04 runners to get around congested shared ASF runner queues; PyIceberg uses a merge queue, and whether the Java repository wants one was asked ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- PyIceberg is dropping Python 3.10; both replies agreed ([thread](records/threads/2026/10/discuss-drop-pyiceberg-python-3-10-support-e423f0.md)).
- A new repository, apache/iceberg-verification, holds shared conformance fixtures ([thread](records/threads/2026/08/vote-create-the-apache-iceberg-verification-repository-0eb2be.md)).
- The DataFusion integration is moving from iceberg-rust to Apache DataFusion ([thread](records/threads/2026/09/vote-move-iceberg-datafusion-to-apache-datafusion-85a04b.md)).
- Community health statistics are to be reported monthly ([thread](records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md)).
- Working group consolidation: the file and vector type sync asked whether to fold into the weekly V4 sync; no answer is recorded ([file and vector type sync 2026-11-05](records/meetings/file-vector-type/2026/2026-11-05.md)).
- The Iceberg Rust sync time is under discussion after the daylight saving change ([thread](https://lists.apache.org/thread/rmgj7c4rglc9szdvosv3lo15sw9grxf2), `devlist:rmgj7c4rglc9szdvosv3lo15sw9grxf2`).
- Events: the Iceberg Summit 2027 call for papers opened on 2026-11-12 ([announcement](https://lists.apache.org/thread/8qw0omgt78cjpc3vcrsop83dyp026vc6), `devlist:8qw0omgt78cjpc3vcrsop83dyp026vc6`).
