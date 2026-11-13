# Opportunities to contribute to Apache Iceberg

As of 2026-11-13. A ranked list: entries at the top have the most concrete and most recent evidence. Level is `starter`, `intermediate` or `advanced`. Meeting dates come from `kb upcoming` on 2026-11-13 (UTC).

Limits of the data: apache/iceberg pull requests are synced with their reviews, so "no reviews" below means none in the GitHub record of 2026-11-13. Issues are only partly synced (to 2025-11-07), so no entry is based on issue reactions. apache/iceberg-python, iceberg-rust and iceberg-go pull requests are not synced, so for those repositories check the linked issue or pull request for an owner before starting. Review state changes quickly; re-check a pull request before acting on an entry.

### 1. Review the Spark wrong-result fixes ahead of 1.13

- **Area:** apache/iceberg, `spark` and `core`
- **Level:** intermediate
- **Why now:** The Spark sync of 2026-11-11 asked for a reviewer and an owner for each of a set of correctness fixes, and for a call on which block 1.13 ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md); [Java releases](initiatives/java-releases.md)). In the GitHub record, [#18557](https://github.com/apache/iceberg/pull/18557) (scans compared by hash code in SparkBatch equality, opened 2026-10-17) has no reviews; [#18738](https://github.com/apache/iceberg/pull/18738) (ExpireSnapshots inside a transaction) and [#18824](https://github.com/apache/iceberg/pull/18824) (`spark.wap.id` in metadata deletes) each have comments from one reviewer and no approval. [#18622](https://github.com/apache/iceberg/pull/18622) is on the list and is not in the synced data.
- **Who to talk to:** [@anuragmantri](people/anuragmantri.md) (1.13 release manager, per [Java releases](initiatives/java-releases.md)); recent `spark` reviewers [@huaxingao](people/huaxingao.md), [@szehon-ho](people/szehon-ho.md), [@RussellSpitzer](people/RussellSpitzer.md) and [@nssalian](people/nssalian.md) (`kb who-to-ask spark/`). Working group: [Spark Community Sync](groups/spark.md), last met 2026-11-11, no meeting listed in the next 14 days.
- **First step:** Check out #18557, run its new test against `main` to see the failure it fixes, and leave a review that says what you verified.

### 2. Review the DSv2 Transaction API pull request for Spark 4.2

- **Area:** apache/iceberg, `spark` (Spark 4.2)
- **Level:** advanced
- **Why now:** The Spark sync notes of 2026-11-11 say this pull request has no reviews and closes around 14 November, and list it among the items that gate Spark 4.2 ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)). [#18385](https://github.com/apache/iceberg/pull/18385), opened 2026-10-05, has no reviews in the GitHub record; that it is the pull request meant is inferred on the [Spark integration](initiatives/spark-integration.md) page.
- **Who to talk to:** [@developer-rpai](people/developer-rpai.md) (author); `spark` reviewers [@huaxingao](people/huaxingao.md), [@szehon-ho](people/szehon-ho.md) and [@RussellSpitzer](people/RussellSpitzer.md) (`kb who-to-ask spark/`). Working group: [Spark Community Sync](groups/spark.md), no meeting listed in the next 14 days.
- **First step:** Read the Spark 4.2 tracker [#17959](https://github.com/apache/iceberg/issues/17959) to see where the Transaction API sits, then review #18385 or comment so that it is not closed as inactive.

### 3. Review the secondary index spec

- **Area:** apache/iceberg, `format` (index spec) and `open-api`
- **Level:** advanced
- **Why now:** On 2026-11-09 the author of the index spec pull request [#16961](https://github.com/apache/iceberg/pull/16961) said it is ready for review and has had no reviews in recent months ([index sync 2026-11-09](records/meetings/index/2026/2026-11-09.md)). The sync of 2026-10-26 addressed an action item to the community: review the design decisions in the index REST spec pull request [#16963](https://github.com/apache/iceberg/pull/16963) ([index sync 2026-10-26](records/meetings/index/2026/2026-10-26.md)). The group wants the index metadata spec settled before the REST spec ([Secondary indexes](initiatives/secondary-indexes.md)).
- **Who to talk to:** [@pvary](people/pvary.md) (index spec author) and [@huaxingao](people/huaxingao.md) (REST pull request author). Working group: [Index Support Sync](groups/index.md), next meeting 2026-11-23 17:00.
- **First step:** Read #16961 with the 9 November decisions in hand (derived columns are being removed, index names are unique per table) and comment on one open question, such as whether `loadTable` returns indexes by default.

### 4. Review the Iceberg core pull requests that materialized views wait on

- **Area:** apache/iceberg, `core`, `spark` and `format` (view spec)
- **Level:** advanced
- **Why now:** The materialized view sync of 2026-11-12 has an action item without an owner: push the Iceberg core pull request reviews forward, because the Flink implementation is blocked until they merge ([materialized views sync 2026-11-12](records/meetings/materialized-views/2026/2026-11-12.md)). The spec pull request [#11041](https://github.com/apache/iceberg/pull/11041) was opened for broader review on the dev list on 2026-11-10, with the Spark proof of concept [#9830](https://github.com/apache/iceberg/pull/9830) ([thread](https://lists.apache.org/thread/zpl1pk6v7k49s30gmm3kr986bc9y7jyv), `devlist:zpl1pk6v7k49s30gmm3kr986bc9y7jyv`). The notes do not name the core pull requests; the same notes list defining the REST spec for materialized views as still to be done.
- **Who to talk to:** [@JanKaul](people/JanKaul.md) (spec author), [@wmoustafa](people/wmoustafa.md) (author of #9830) and [@talatuyarer](people/talatuyarer.md) (Flink implementation; login inferred from "Talat" in the notes). Working group: [Materialized View Sync](groups/materialized-views.md), next meeting 2026-11-26 17:00.
- **First step:** Read #11041 before the vote, then ask in the sync notes or on the dev list thread which core pull requests are the blocking ones and review one of them.

### 5. PyIceberg: document the release timeline

- **Area:** apache/iceberg-python, `mkdocs` documentation (python)
- **Level:** starter
- **Why now:** The PyIceberg sync agenda of 2026-10-27 has an item to add documentation about the release timeline of about three months, next to 0.13 planning with "Early December?" as a date; no owner or discussion is recorded ([PyIceberg sync 2026-10-27](records/meetings/python/2026/2026-10-27.md); [PyIceberg roadmap](initiatives/pyiceberg.md)). iceberg-python pull requests are not synced, so whether someone has started is unknown.
- **Who to talk to:** [@kevinjqliu](people/kevinjqliu.md) and [@rambleraptor](people/rambleraptor.md), the most active authors in `iceberg-python/docs` over the last 12 months ([ownership map](maps/ownership.md)). Working group: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00.
- **First step:** Search apache/iceberg-python for an open issue or pull request on release cadence; if there is none, open an issue that proposes the text and offer a docs pull request.

### 6. PyIceberg: check bucket hashing of pre-epoch nanosecond timestamps

- **Area:** apache/iceberg-python, `pyiceberg/transforms.py` (python), and apache/iceberg-verification
- **Level:** starter
- **Why now:** A dev list thread of 2026-11-06 found that the spec does not say how to round negative values when nanosecond timestamps are converted to microseconds before bucket hashing: for one nanosecond before the epoch, floor division gives `bucket[100] = 12` and truncation gives 76. The thread states that Java, Go and Rust use floor division and proposes a spec sentence ([thread](https://lists.apache.org/thread/hcc1yo2pcyrc089rgywo8nh0tt9gs5yl), `devlist:hcc1yo2pcyrc089rgywo8nh0tt9gs5yl`). PyIceberg is not named in the thread; that its behaviour is unverified is inferred from that omission, and no record reports a bug.
- **Who to talk to:** [@laskoviymishka](people/laskoviymishka.md) (named in the thread as co-finder); [@Fokko](people/Fokko.md) and [@rambleraptor](people/rambleraptor.md), recent authors in `iceberg-python/transforms` ([ownership map](maps/ownership.md)). Working groups: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00; the [Shared Conformance Testing Sync](groups/conformance.md) has no meeting on the calendar.
- **First step:** Compute `bucket[100]` for `1969-12-31T23:59:59.999999999` in PyIceberg, compare it with 12, and report the result on the thread; add a unit test whichever way it comes out.

### 7. Review the V4 column updates spec

- **Area:** apache/iceberg, `format` (V4 spec)
- **Level:** advanced
- **Why now:** The V4 status round on 2026-10-28 reported that the column updates spec pull request [#16425](https://github.com/apache/iceberg/pull/16425) needs review before it can go to a vote ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)), and the column updates sync of 2026-10-20 lists it under spec pull requests to review ([column updates sync 2026-10-20](records/meetings/column-updates/2026/2026-10-20.md)). The first Java pull request, [#16285](https://github.com/apache/iceberg/pull/16285), merged on 2026-11-05 (GitHub record). Ports to Go, C++, Python and Rust are anticipated and no record names an owner for them ([V4 column updates](initiatives/v4-column-updates.md)).
- **Who to talk to:** [@anuragmantri](people/anuragmantri.md) (spec author) and [@gaborkaszab](people/gaborkaszab.md) (author of #16285); reviewers on the spec pull request include [@stevenzwu](people/stevenzwu.md), [@pvary](people/pvary.md) and [@RussellSpitzer](people/RussellSpitzer.md) (GitHub record). Working groups: [Efficient Column Updates Sync](groups/column-updates.md), every two weeks, none listed in the next 14 days; [V4 Metadata Sync](groups/v4-metadata.md), next meeting 2026-11-17 17:00.
- **First step:** Read the decided points on the [V4 column updates](initiatives/v4-column-updates.md) page (dense column files, no persisted `_pos`, no equality deletes) and check that #16425 states each of them.

### 8. Review the encryption key metadata spec changes

- **Area:** apache/iceberg, `format` (encryption) and `core`
- **Level:** advanced
- **Why now:** The V4 metadata sync of 2026-11-02 has an action item without an owner: review the spec pull request for encryption key metadata, which its author described as ready for more reviews ([V4 metadata sync 2026-11-02](records/meetings/v4-metadata/2026/2026-11-02.md)). The notes do not give its number. A related change, [#17533](https://github.com/apache/iceberg/pull/17533) (keys for table and partition statistics files), closed its dev list thread with a request for wider feedback ([thread](records/threads/2026/09/discuss-reusable-encryption-keys-c3195b.md); [Table encryption](initiatives/v4-encryption.md)).
- **Who to talk to:** [@gaborkaszab](people/gaborkaszab.md) (author) and [@ggershinsky](people/ggershinsky.md) (reviewer on #17533, GitHub record). Working group: [V4 Metadata Sync](groups/v4-metadata.md), next meeting 2026-11-17 17:00.
- **First step:** Read the reusable-keys thread summary, then comment on #17533 on where keys for statistics files and V4 root manifests should be stored.

### 9. PyIceberg: pin down name mapping for files that carry only some field IDs

- **Area:** apache/iceberg-python, `pyiceberg/io/pyarrow.py` and `pyiceberg/table/name_mapping.py` (python), and apache/iceberg-verification
- **Level:** intermediate
- **Why now:** A dev list thread started 2026-11-03 reports that Java, PyIceberg, iceberg-rust and iceberg-go each resolve Parquet files with partial field IDs differently; it has no agreement yet between per-field and per-file resolution, and it references [apache/iceberg-verification#14](https://github.com/apache/iceberg-verification/issues/14) ([thread](records/threads/2026/11/discuss-name-mapping-for-data-files-that-carry-only-some-field-ids-14cfe6.md); [Shared conformance testing](initiatives/conformance-testing.md)). Whatever is decided, each implementation needs a test that fixes its behaviour.
- **Who to talk to:** [@RussellSpitzer](people/RussellSpitzer.md) and [@manuzhang](people/manuzhang.md) (positions in the thread); [@kevinjqliu](people/kevinjqliu.md) and [@rambleraptor](people/rambleraptor.md) for the PyIceberg side ([ownership map](maps/ownership.md), `iceberg-python/io`). Working group: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00.
- **First step:** Write a small Parquet file in which only some columns carry field IDs, read it with PyIceberg with and without a name mapping, and post what happens on the thread or the verification issue.

### 10. Review small spec and docs pull requests that have no reviews

- **Area:** apache/iceberg, `format`, `open-api` and `docs`
- **Level:** starter
- **Why now:** The community health statistics shared on 2026-10-27 show a large stale pull request backlog, and the community sync asked whether and how to act on it ([thread](records/threads/2026/10/discuss-iceberg-community-health-stats-03ef42.md); [community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)). In the GitHub record these one- to three-file pull requests have no reviews, and all but the first carry the `stale` label: [#18468](https://github.com/apache/iceberg/pull/18468) (docs: Spark branch write precedence over the WAP branch), [#18429](https://github.com/apache/iceberg/pull/18429) (spec: snapshot summary metrics are informational), [#18433](https://github.com/apache/iceberg/pull/18433) (spec and OpenAPI: hex case for binary and fixed values) and [#18431](https://github.com/apache/iceberg/pull/18431) (OpenAPI: remove deprecated TrueExpression and FalseExpression).
- **Who to talk to:** recent reviewers of `format/spec.md` ([@RussellSpitzer](people/RussellSpitzer.md), [@stevenzwu](people/stevenzwu.md), [@singhpk234](people/singhpk234.md)), `open-api/` ([@huaxingao](people/huaxingao.md), [@danielcweeks](people/danielcweeks.md)) and `docs/` ([@pvary](people/pvary.md), [@ebyhr](people/ebyhr.md)), from `kb who-to-ask`. Working group: [Iceberg Community Sync](groups/community.md), next meeting 2026-11-18 17:00.
- **First step:** Pick #18468, check the documented precedence against the Spark write code, and leave a review; a non-binding review also keeps the pull request from being closed as inactive.

### 11. Review the Parquet statistics unit fixes

- **Area:** apache/iceberg, `parquet`
- **Level:** starter
- **Why now:** The Spark sync of 2026-11-11 requested reviews for converting TIMESTAMP_MILLIS statistics to micros ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md)); in the GitHub record [#18321](https://github.com/apache/iceberg/pull/18321) (3 files) has one approval. Its sibling for TIME_MILLIS, [#18466](https://github.com/apache/iceberg/pull/18466) (2 files, opened 2026-10-12), has no reviews and carries the `stale` label.
- **Who to talk to:** recent `parquet` reviewers [@nssalian](people/nssalian.md), [@huaxingao](people/huaxingao.md), [@uros-b](people/uros-b.md) and [@pvary](people/pvary.md) (`kb who-to-ask parquet/`). Working group: [Spark Community Sync](groups/spark.md), no meeting listed in the next 14 days; [Iceberg Community Sync](groups/community.md), 2026-11-18 17:00.
- **First step:** Read both pull requests side by side, run their tests, and note in a review whether the two conversions are consistent with each other.

### 12. Work through the Spark sync's review queue

- **Area:** apache/iceberg, `spark`, `core` and `parquet`
- **Level:** intermediate
- **Why now:** The Spark sync of 2026-11-11 closes with a list of review requests ([Spark sync 2026-11-11](records/meetings/spark/2026/2026-11-11.md); [Spark integration](initiatives/spark-integration.md)). From the GitHub record: the k-way merge rewrite strategy [#16305](https://github.com/apache/iceberg/pull/16305) is on the 1.13.0 milestone with comments and no approval; selective shredded variant extraction readers [#16714](https://github.com/apache/iceberg/pull/16714) has comments and no approval since June; applying `ReadBuilder.set()` properties to Parquet read options [#18238](https://github.com/apache/iceberg/pull/18238) carries the `stale` label; variant extraction pushdown [#16715](https://github.com/apache/iceberg/pull/16715), opened 2026-06-08, has no reviews. SupportsReportOrdering ([#16750](https://github.com/apache/iceberg/pull/16750)) is on the list and is not in the synced data.
- **Who to talk to:** [@anuragmantri](people/anuragmantri.md) (author of #16305) and `@qlong` (author of #16714 and #16715); `spark` reviewers [@huaxingao](people/huaxingao.md), [@szehon-ho](people/szehon-ho.md) and [@RussellSpitzer](people/RussellSpitzer.md) (`kb who-to-ask spark/`). Working group: [Spark Community Sync](groups/spark.md), no meeting listed in the next 14 days.
- **First step:** Start with #18238, the smallest (2 files), which the notes relate to the 1.11 out-of-memory issue.

### 13. Help settle the orphan file sibling-prefix fix

- **Area:** apache/iceberg, `spark` (actions)
- **Level:** intermediate
- **Why now:** `remove_orphan_files` with a file list filters by raw prefix, so a location `s3://bucket/table` also matches `s3://bucket/table-backup/` and files in the sibling directory can be deleted. A dev list thread of 2026-10-31 asks for objections to fixing this as a behaviour change in [#16498](https://github.com/apache/iceberg/pull/16498), with [#18029](https://github.com/apache/iceberg/pull/18029) as an alternative that differs on one case ([thread](https://lists.apache.org/thread/cgsbm3rbplyo8wnm6281dwp0rx5vrtbn), `devlist:cgsbm3rbplyo8wnm6281dwp0rx5vrtbn`). Both are open with comments and no approval in the GitHub record.
- **Who to talk to:** [@wombatu-kun](people/wombatu-kun.md) (author of #16498 and of the thread); [@sungwy](people/sungwy.md) and [@uros-b](people/uros-b.md) (reviewers on #16498, GitHub record). Working group: [Spark Community Sync](groups/spark.md), no meeting listed in the next 14 days.
- **First step:** Compare how the two pull requests treat an entry equal to the location itself, and reply on the thread or review #16498 with the case you tested.

### 14. Review the REST pull requests the catalog sync called out

- **Area:** apache/iceberg, `open-api`, `core` (REST) and `aws`
- **Level:** advanced
- **Why now:** The catalog sync of 2026-10-14 listed calls for review on scan planning that returns pre-signed URLs ([#17457](https://github.com/apache/iceberg/pull/17457)), pre-signing through the sign endpoint ([#18080](https://github.com/apache/iceberg/pull/18080)) and server-vended KMS credentials ([#17155](https://github.com/apache/iceberg/pull/17155)) ([catalog sync 2026-10-14](records/meetings/catalog/2026/2026-10-14.md); [REST authentication](initiatives/rest-auth.md)). All three are open without an approval in the GitHub record; #17457 is on the 1.13.0 milestone. The same sync asked an unnamed participant to check the catalog-vended KMS credential model with security people.
- **Who to talk to:** [@williamhyun](people/williamhyun.md) (#17457), [@sungwy](people/sungwy.md) (#18080) and [@szlta](people/szlta.md) (#17155); reviewers [@danielcweeks](people/danielcweeks.md), [@singhpk234](people/singhpk234.md) and [@adutra](people/adutra.md) (GitHub record). Working group: [Catalog Community Sync](groups/catalog.md), next meeting 2026-11-25 17:00.
- **First step:** Read the file-level access delegation thread summary ([thread](records/threads/2026/07/discuss-proposal-file-level-access-delegation-in-the-iceberg-rest-cata-643f9a.md)) and review #18080, the smallest of the three (2 files).

### 15. Give feedback on the REST catalog changes for V4

- **Area:** apache/iceberg, `open-api`
- **Level:** advanced
- **Why now:** Feedback is requested on [#17642](https://github.com/apache/iceberg/pull/17642), which changes the REST models in place for V4 and carries the table-location field that relative paths need ([thread](records/threads/2026/08/discuss-initial-irc-changes-needed-for-iceberg-v4-4fdcd7.md); [REST catalog spec](initiatives/rest-spec.md)). On 2026-11-11 a `rest-v4-changes` branch was created to collect the spec and OpenAPI changes for V4 tables, and the message asks for feedback on the pull request ([message](https://lists.apache.org/thread/zrn1jb7g9wm7jgn4fx3klmtxs03k65zg), `devlist:zrn1jb7g9wm7jgn4fx3klmtxs03k65zg`). The pull request is open with comments and no approval (GitHub record).
- **Who to talk to:** `@dhruvarya-db` (author); reviewers [@danielcweeks](people/danielcweeks.md), [@amogh-jahagirdar](people/amogh-jahagirdar.md) and [@gaborkaszab](people/gaborkaszab.md) (GitHub record). Working group: [Catalog Community Sync](groups/catalog.md), next meeting 2026-11-25 17:00.
- **First step:** Read the thread summary, then review #17642 for one V4 feature you know (relative paths, constraints or default values) and say whether the relaxed responses cover it.

### 16. Kafka Connect: test the equality-delete-free CDC proposal

- **Area:** apache/iceberg, `kafka-connect`
- **Level:** advanced
- **Why now:** The dev list thread of 2026-10-26 on CDC writes that never commit equality deletes ([#18003](https://github.com/apache/iceberg/pull/18003)) is open: reviewers asked whether the community wants CDC in the sink and asked for performance testing before any merge ([thread](records/threads/2026/10/discuss-kafka-connect-cdc-writes-without-equality-deletes-34ed4d.md); [Kafka Connect sink](initiatives/kafka-connect.md)). The community sync of 2026-10-28 voiced the position not to add anything that produces new equality deletes and to explore upserts through a primary key index ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- **Who to talk to:** `@koodin9` (author of #18003), [@laskoviymishka](people/laskoviymishka.md) (reviewer on it, and owner of the action item to check the mainline sink) and [@pvary](people/pvary.md) (asked for performance testing, per the thread summary). Working group: [Iceberg Community Sync](groups/community.md), next meeting 2026-11-18 17:00.
- **First step:** Reproduce the benchmark reported in the thread (increasing IDs against random UUID keys on a 10,000-file table) and post your numbers and setup.

### 17. Review the GCS bulk delete failure handling

- **Area:** apache/iceberg, `gcp`
- **Level:** intermediate
- **Why now:** A review request went to the dev list on 2026-10-30 for [#18463](https://github.com/apache/iceberg/pull/18463): `GCSFileIO.deleteFiles` cannot tell a missing object from a failed delete, so real failures are swallowed ([thread](https://lists.apache.org/thread/6jg89899o7j968wjss7vordchp1m00l1), `devlist:6jg89899o7j968wjss7vordchp1m00l1`). The pull request has comments from one reviewer and no approval in the GitHub record.
- **Who to talk to:** `@munendrasn` (author); recent `gcp` reviewers [@nastra](people/nastra.md), [@ajreid21](people/ajreid21.md) and [@anoopj](people/anoopj.md) (`kb who-to-ask gcp/`). Working group: none specific; [Iceberg Community Sync](groups/community.md), next meeting 2026-11-18 17:00.
- **First step:** Review how the pull request maps per-object batch results to `BulkDeletionFailureException` and whether retries stay safe to repeat.

### 18. Review the collations spec

- **Area:** apache/iceberg, `format` (spec)
- **Level:** advanced
- **Why now:** Reviews of [#16972](https://github.com/apache/iceberg/pull/16972) were requested at the community sync of 2026-10-28, after it was rebuilt on V4 stats-only fields; how bounds are stored is the open point ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md); [Collation support](initiatives/collations.md)). It is open with comments and no approval (GitHub record).
- **Who to talk to:** [@laskoviymishka](people/laskoviymishka.md) (author); reviewers [@szehon-ho](people/szehon-ho.md), [@RussellSpitzer](people/RussellSpitzer.md) and [@danielcweeks](people/danielcweeks.md) (GitHub record). Working group: [Iceberg Community Sync](groups/community.md), next meeting 2026-11-18 17:00.
- **First step:** Read the stats-only fields thread summary ([thread](records/threads/2026/10/discuss-stats-only-fields-44ddd4.md)) and comment on #16972 on the bounds representation.

### 19. PyIceberg: implement read restrictions

- **Area:** apache/iceberg-python, `pyiceberg/catalog/rest` and `pyiceberg/table` (python)
- **Level:** advanced
- **Why now:** The read restrictions sync of 2026-09-15 asked for volunteers to implement read restrictions in PyIceberg, tracked in [iceberg-python#3967](https://github.com/apache/iceberg-python/issues/3967) ([read restrictions sync 2026-09-15](records/meetings/read-restrictions/2026/2026-09-15.md); [Read restrictions](initiatives/read-restrictions.md)). The spec change is merged, and a client that receives restrictions it cannot apply must fail ([catalog sync 2026-10-14](records/meetings/catalog/2026/2026-10-14.md)). The request is two months old and iceberg-python pull requests are not synced, so check the issue for an assignee first.
- **Who to talk to:** [@singhpk234](people/singhpk234.md) (author of the Java Actions API [#16198](https://github.com/apache/iceberg/pull/16198)); [@kevinjqliu](people/kevinjqliu.md) and [@rambleraptor](people/rambleraptor.md) for PyIceberg ([ownership map](maps/ownership.md)). Working groups: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00; [Catalog Community Sync](groups/catalog.md), 2026-11-25 17:00. The Read Restrictions sync has no notes since September.
- **First step:** Read the issue and the Java pull request #16198, then propose on the issue a first slice: parse the restrictions in the load table response and fail closed when they cannot be applied.

### 20. Iceberg Rust: implement read restrictions

- **Area:** apache/iceberg-rust, REST catalog client and scan
- **Level:** advanced
- **Why now:** The same sync asked for volunteers for Iceberg Rust, tracked in [iceberg-rust#3361](https://github.com/apache/iceberg-rust/issues/3361) ([read restrictions sync 2026-09-15](records/meetings/read-restrictions/2026/2026-09-15.md); [Iceberg Rust](initiatives/iceberg-rust.md)). iceberg-rust pull requests are not synced, so check the issue for an assignee. Users without write access are limited to three open non-draft pull requests there ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)).
- **Who to talk to:** [@singhpk234](people/singhpk234.md) (author of the Java Actions API). Working group: [Iceberg Rust Community Sync](groups/rust.md), next listed 2026-12-03 15:00, outside the 14-day window; its time is under discussion ([thread](https://lists.apache.org/thread/rmgj7c4rglc9szdvosv3lo15sw9grxf2)).
- **First step:** Comment on the issue with the part you would take and ask for a reviewer before writing code.

### 21. Write the missing contributor guidance

- **Area:** apache/iceberg, `site` (contribution page) and `AGENTS.md`
- **Level:** starter
- **Why now:** The index sync of 2026-11-09 suggested a document on how to introduce a proposal, with no owner recorded ([index sync 2026-11-09](records/meetings/index/2026/2026-11-09.md)). The community sync of 2026-09-16 listed, also without an owner, updating the contribution page with best practices and adding a pre-PR checklist to `AGENTS.md`, such as checking for related pull requests first ([community sync 2026-09-16](records/meetings/community/2026/2026-09-16.md); [AI-assisted contributions](initiatives/ai-contributions.md)).
- **Who to talk to:** [@kevinjqliu](people/kevinjqliu.md), the most active author and reviewer in `iceberg/site` ([ownership map](maps/ownership.md)); [@RussellSpitzer](people/RussellSpitzer.md), who presented the community health statistics ([community sync 2026-10-28](records/meetings/community/2026/2026-10-28.md)). Working group: [Iceberg Community Sync](groups/community.md), next meeting 2026-11-18 17:00.
- **First step:** Ask on the dev list whether anyone has started either document, then draft the pre-PR checklist as a small pull request against `AGENTS.md`.

### 22. PyIceberg: finish the wheel licensing follow-ups

- **Area:** apache/iceberg-python, packaging (`pyproject.toml`, LICENSE and NOTICE files) (python)
- **Level:** starter
- **Why now:** The 0.12.0 RC2 vote found LICENSE paths that differ inside the wheels and bundled Cython runtime code that is not documented; the follow-ups are tracked in [iceberg-python#3877](https://github.com/apache/iceberg-python/issues/3877) ([thread](records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md); [PyIceberg roadmap](initiatives/pyiceberg.md)). 0.13 release planning is on the sync agenda with "Early December?" under it and no recorded discussion ([PyIceberg sync 2026-10-27](records/meetings/python/2026/2026-10-27.md)). The evidence is from August and iceberg-python is not synced, so the issue may already be resolved.
- **Who to talk to:** [@rambleraptor](people/rambleraptor.md) (0.12.0 release manager, per [PyIceberg roadmap](initiatives/pyiceberg.md)) and [@kevinjqliu](people/kevinjqliu.md). Working group: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00.
- **First step:** Open the issue, build a wheel locally, list the licence files it contains and compare them with what the issue asks for.

### 23. PyIceberg: inventory PyArrow use outside `pyarrow.py`

- **Area:** apache/iceberg-python, `pyiceberg/io` and `pyiceberg/table` (python)
- **Level:** intermediate
- **Why now:** For the pluggable backend ([iceberg-python#3716](https://github.com/apache/iceberg-python/pull/3716)) the PyIceberg sync of 2026-07-28 called for an inventory of everything related to PyArrow, asked why there are PyArrow calls outside `pyarrow.py`, and set moving that code into `pyarrow.py` as the step before looking for an abstraction across Polars, DataFusion and PyArrow ([PyIceberg sync 2026-07-28](records/meetings/python/2026/2026-07-28.md); [PyIceberg roadmap](initiatives/pyiceberg.md)). No owner is recorded; the evidence is from July and iceberg-python is not synced.
- **Who to talk to:** [@kevinjqliu](people/kevinjqliu.md) and [@rambleraptor](people/rambleraptor.md) ([ownership map](maps/ownership.md), `iceberg-python/io`). Working group: [PyIceberg Sync](groups/python.md), next meeting 2026-11-24 17:00.
- **First step:** Check the state of #3716, then list the `import pyarrow` sites outside `pyiceberg/io/pyarrow.py` and post the list on that pull request or in an issue.

### 24. Spark: pick up vectorized reads for geometry and geography

- **Area:** apache/iceberg, `spark` and `arrow`
- **Level:** advanced
- **Why now:** The pull request for vectorized geo reads in Spark 4.1, [#17297](https://github.com/apache/iceberg/pull/17297), was closed as a draft on 2026-07-21 (GitHub record), and the Spark sync of 2026-08-18 asked whether anyone is picking it back up ([Spark sync 2026-08-18](records/meetings/spark/2026/2026-08-18.md); [Geospatial types](initiatives/geospatial.md)). Geo columns currently fall back from vectorized reads ([Spark sync 2026-07-21](records/meetings/spark/2026/2026-07-21.md)). No newer pull request for this is in the synced data; the evidence is three months old.
- **Who to talk to:** [@huan233usc](people/huan233usc.md) (author of #17297 and of the fallback); `spark` reviewers [@szehon-ho](people/szehon-ho.md) and [@huaxingao](people/huaxingao.md) (`kb who-to-ask spark/`). Working group: [Spark Community Sync](groups/spark.md), no meeting listed in the next 14 days.
- **First step:** Ask on #17297 why it was closed and whether the author plans to return to it before starting from its branch.
