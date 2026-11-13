---
id: thread/t-3a558d67a81956a4
type: thread
title: Adding an unregister table endpoint to the REST spec
date: '2026-05-18'
url: https://lists.apache.org/thread/q60ymn6rq1qzs102zj0vm0fnqjjv0knw
kind: discuss
status: consensus
messages: 12
sources:
- devlist:q60ymn6rq1qzs102zj0vm0fnqjjv0knw
refs:
- gh:apache/iceberg#16400
- gh:apache/iceberg#14743
- gh:apache/iceberg#14869
links:
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:q60ymn6rq1qzs102zj0vm0fnqjjv0knw
- rel: started_by
  to: person/rdblue
  confidence: observed
updated: '2026-11-13'
---

# Adding an unregister table endpoint to the REST spec

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Adding unregister table endpoint to REST spec](https://lists.apache.org/thread/q60ymn6rq1qzs102zj0vm0fnqjjv0knw) · **Started:** 2026-05-18 by [[person/rdblue|Ryan Blue]] · **Messages:** 12 (last 2026-05-20) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Ryan Blue opened PR #16400 to add an `unregister` endpoint to the REST catalog spec. It is the opposite of `register`: it removes a table from a catalog without deleting its data and metadata files, so a table can be moved to another catalog. He gave two reasons the drop endpoint is not enough: most REST catalogs handle file cleanup themselves, so there must be a way to prevent removal, and drop is not safe with concurrent operations, whereas unregister returns the current table state and metadata location with the assurance that it is the latest. Replies were supportive. Ajantha Bhat asked why `purgeRequested` on drop does not already protect files and proposed an unregister-view endpoint as well. Daniel Weeks answered that setting `purgeRequested` to false does not require the server to keep the data. Ryan planned to start a vote that week. A final question about the difference from drop without purge closed the thread.

**Why it matters:** An unregister endpoint gives a standard, concurrency-safe way to move a table between REST catalogs without risking file deletion.

## Outcome

All replies that took a position supported the new endpoint; the proposer planned a vote thread, and no vote happened in this thread.

## Positions

- **[[person/rdblue|Ryan Blue]]:** Add an `unregister` endpoint because drop cannot guarantee that files are kept and does not return the latest metadata location safely under concurrent operations. ([message](https://lists.apache.org/thread/q60ymn6rq1qzs102zj0vm0fnqjjv0knw))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Supports it as completing the portability story between catalogs. ([message](https://lists.apache.org/thread/4bnkv3gz6304cys6dxtpx0qxg8lg44jp))
- **[[person/ajantha-bhat|Ajantha Bhat]]:** Generally in favor because returning the metadata location makes catalog migration atomic, but asks why `purgeRequested` on drop is insufficient and suggests adding unregister-view too. ([message](https://lists.apache.org/thread/wlto1z6h41n8gwrf1gl0qtlo5t0l7yo3))
- **[[person/flyrain|Yufei Gu]]:** Supports the endpoint; concurrent writes are where drop cannot be used safely. ([message](https://lists.apache.org/thread/vohj6979v5f05tmctgh40xnv2gwl6g54))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Supports a new endpoint: `purgeRequested=false` only allows later cleanup and does not oblige the server to preserve data, while unregister specifically detaches the data from catalog management. ([message](https://lists.apache.org/thread/m0s4ocmq7z721xxjd8xssbg1q55kt3f9))
- **[[person/xndai|Xiening Dai]]:** Asks how unregister differs from `dropTable` with `purgeRequested` set to false. ([message](https://lists.apache.org/thread/thxhdlhhl8ln51ncfyl5zn7h53goq99q))

References: [iceberg#16400](https://github.com/apache/iceberg/issues/16400), [iceberg#14743](https://github.com/apache/iceberg/issues/14743), [iceberg#14869](https://github.com/apache/iceberg/issues/14869)
<!-- kb:generated:end -->

## Notes
