---
id: thread/t-4ba0b50d52976551
type: thread
title: 'Spark: use the catalog''s Hadoop configuration when listing orphan files'
date: '2026-10-28'
url: https://lists.apache.org/thread/5f40shqmwc2l647oskjg1vv8pq7q8od7
kind: discuss
status: consensus
messages: 15
sources:
- devlist:5f40shqmwc2l647oskjg1vv8pq7q8od7
refs:
- gh:apache/iceberg#17862
- gh:apache/iceberg#17860
- gh:apache/iceberg#17790
- gh:apache/iceberg#11906
- gh:apache/iceberg#16932
- gh:apache/iceberg#17387
links: []
updated: '2026-11-13'
---

# Spark: use the catalog's Hadoop configuration when listing orphan files

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Spark: use the catalog's Hadoop configuration when listing orphan files (#17862)](https://lists.apache.org/thread/5f40shqmwc2l647oskjg1vv8pq7q8od7) · **Started:** 2026-10-28 by Sebastian Daberdaku · **Messages:** 15 (last 2026-11-09) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Sebastian Daberdaku asked for agreement on PR #17862, which fixes remove_orphan_files listing the table location with a Hadoop FileSystem built from the Spark session configuration only, so catalogs that use other credentials (for example a cross-account role) fail with AccessDenied. The PR added a public catalogName(String) method to DeleteOrphanFilesSparkAction. Dan Weeks and Russell Spitzer preferred reading the configuration from the table's FileIO when it is HadoopConfigurable, without new API. Sebastian noted that S3FileIO, GCSFileIO and ADLSFileIO are not HadoopConfigurable, so the reported Glue case (#17860) stays unfixed, and proposed hadoopConf(Configuration), a ResolvingFileIO default for Glue, or a parallel prefix listing. JB Onofré and Dan said listing should go through the table FileIO; Dan opposed delimiter-based listing (#17790) and favoured splitting the key space with prefix listing. Sebastian reworked the PR to the HadoopConfigurable shape for Spark 4.2, 4.1, 4.0 and 3.5, with no new API.

**Why it matters:** Orphan file removal with S3FileIO and catalog-specific credentials still needs prefix_listing until a parallel FileIO-based listing exists.

## Outcome

Sebastian reworked #17862 so the listing uses the FileIO's Hadoop configuration when table.io() is HadoopConfigurable and the session configuration otherwise, with no new API, across Spark 4.2, 4.1, 4.0 and 3.5. The S3FileIO case in #17860 is left to a future parallel FileIO listing, whose design (delimiter walk versus prefix enumeration) was still being discussed. ([message](https://lists.apache.org/thread/vjf87md908mf903mdjqrgo2qglopxox2), `devlist:vjf87md908mf903mdjqrgo2qglopxox2`)

## Positions

- **Sebastian Daberdaku:** The listing should pick up the catalog's spark.sql.catalog.<name>.hadoop.* overrides, first via catalogName(String) and later via a proposed hadoopConf(Configuration) setter, because S3FileIO holds no Hadoop configuration. ([message](https://lists.apache.org/thread/0m2gc9yqt77cpy2nvcthm9vkvgsgwrqq))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Read the exact Hadoop configuration from the table's FileIO when it is HadoopConfigurable instead of going through the catalog. ([message](https://lists.apache.org/thread/tymgygw574bh77398ybzndxwm0rcrzws))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Avoid expanding the API; a Hadoop configuration only makes sense for Hadoop-based FileIOs, and there is no reason to allow one for S3FileIO and the other non-Hadoop IOs. ([message](https://lists.apache.org/thread/vzgnwm1hwg6k6rgmb4j5kjo2rxo62369))
- **Jean-Baptiste Onofré:** Do not add catalogName() or hadoopConf(); rework #17862 to use the FileIO's configuration when HadoopConfigurable, fix the S3FileIO case with a parallel listing through table.io(), and do not make ResolvingFileIO the Glue default. ([message](https://lists.apache.org/thread/3t1nq9n9d1oxx78xmyjgshy7nbd8dv94))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Listing should use the table's FileIO, but not through a delimiter-based recursive walk, which does not scale with object store layout; break up the listing namespace and use prefix listing instead. ([message](https://lists.apache.org/thread/gmcj93sjdpwd3dnbq7sov2w48q4b5607))

References: [iceberg#17862](https://github.com/apache/iceberg/issues/17862), [iceberg#17860](https://github.com/apache/iceberg/issues/17860), [iceberg#17790](https://github.com/apache/iceberg/issues/17790), [iceberg#11906](https://github.com/apache/iceberg/issues/11906), [iceberg#16932](https://github.com/apache/iceberg/issues/16932), [iceberg#17387](https://github.com/apache/iceberg/issues/17387)
<!-- kb:generated:end -->

## Notes
