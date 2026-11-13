---
id: thread/t-7303ba875d84ed33
type: thread
title: Efficient column updates in Iceberg
date: '2026-01-27'
url: https://lists.apache.org/thread/2z1lxfo33t5rgbrzq5lvcyk9k5qd4509
kind: discuss
status: open
messages: 46
sources:
- devlist:2z1lxfo33t5rgbrzq5lvcyk9k5qd4509
refs:
- doc:1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs
- gh:apache/iceberg#15445
- doc:1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw
links: []
updated: '2026-11-13'
---

# Efficient column updates in Iceberg

<!-- kb:generated:start -->
**Thread:** [[Discuss] Efficient column updates in Iceberg](https://lists.apache.org/thread/2z1lxfo33t5rgbrzq5lvcyk9k5qd4509) · **Started:** 2026-01-27 by Xianjin Ye · **Messages:** 46 (last 2026-05-20) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Discussion of Anurag Mantripragada's proposal to update or add columns by writing separate column files instead of rewriting whole data files. A February sync agreed the feature belongs in the table format, not in Parquet, because manifests keep complete stats and file lineage and the design is not tied to one file format. The thread then debated full versus partial (row-level) updates, sparse versus dense update files, compaction, column families, packing updates for several base files into one file, and interaction with equality deletes, deletion vectors and change detection. A proof of concept for full column updates in Spark showed single-column updates running in about 1.5s against 20s for copy-on-write or merge-on-read, with read cost growing with the number of update files. A May sync reached consensus on the dense ("complete") representation for partial updates; how to represent rows deleted in the base file and whether update files need a position column stayed open.

**Why it matters:** It records why column updates are being designed in the table format with dense update files, and which questions the design still has to answer.

## Outcome

A sync reached consensus on the dense (complete) update file representation for partial updates. How to represent rows deleted in the base file and whether a position column is required were still open when the thread stopped. ([message](https://lists.apache.org/thread/83z91vhlygwrk5zl8dcrv48h4r029zyr), `devlist:83z91vhlygwrk5zl8dcrv48h4r029zyr`)

## Positions

- **Gábor Kaszab:** Equality deletes cannot be applied correctly between stitched column updates, so column updates and equality deletes on the same fields should not be allowed together. ([message](https://lists.apache.org/thread/lwfl739v778kphm31hhblmbd6t5z6zh0))
- **[[person/stevenzwu|Steven Wu]]:** Rejecting a column update on a column that is part of some delete's equality field IDs makes sense, since equality IDs are like primary key fields. ([message](https://lists.apache.org/thread/hxg51o5rh91jtrd9v0zq80xk3083l267))
- **[[person/anuragmantri|Anurag Mantripragada]]:** The Parquet-native approach was dropped because handling updates in Iceberg keeps complete stats and file lineage in manifests, avoids depending on Parquet format changes and releases, and can extend to other formats. ([message](https://lists.apache.org/thread/9ymwgcgr5zhhkrtjfj8p0b6rh2lprq7d))
- **Micah Kornfield:** Sparse update files are a superset of full ones, since writers can write fully populated columns and readers can take a fast path when row counts match. ([message](https://lists.apache.org/thread/9hgvcwo4346hp00o771ozjxhfn83x9oh))
- **Gábor Kaszab:** Full column updates are agreed and simple; row-level partial updates need strong use cases and measurements to justify their complexity, and file-level partial updates are a possible middle ground. ([message](https://lists.apache.org/thread/mqtmk0m8sbx9rs525322y0kf25tgt3t4))
- **[[person/CTTY|Shawn Chang]]:** Additive column files make compaction a must, and compaction could be tied to writes, for example triggered after a number of column files. ([message](https://lists.apache.org/thread/l13vmn5jrq93qpq0fnos9drb7bmfhrxv))
- **[[person/pvary|Peter Vary]]:** Keeping files vertically split can help wide tables, so a sort-order-like column layout enforced by compaction would be useful, without adding it to the commit or write paths. ([message](https://lists.apache.org/thread/t5kcz7d9bx2g01xfws1xpnq3o4dc65gg))
- **[[person/stevenzwu|Steven Wu]]:** When and how to compact column files should be an implementation decision, and column families could be left out of the spec so engines decide grouping. ([message](https://lists.apache.org/thread/bx051p2b69dxwxgbwmj4k32shb9bnfzb))
- **Frank Bertsch:** Column families chosen by engineers would benefit very wide tables that combine many sources. ([message](https://lists.apache.org/thread/f805r6j1lynkt5v7npfkl9dhd3vtlp9r))
- **Micah Kornfield:** Row-level merge-on-read style column updates should be avoided without a strong use case, and a record range in the metadata would let updates for several base files be packed into one file to avoid small files. ([message](https://lists.apache.org/thread/gt9w7o47dzwzc3p69006ql7k0rbmo4j0))
- **[[person/aokolnychyi|Anton Okolnychyi]]:** Spark DML has to be extended in Spark itself for column updates because it cannot be done through Iceberg extensions. ([message](https://lists.apache.org/thread/yvn4fwssjchzrsomo458c2qdms3rq66y))
- **[[person/pvary|Peter Vary]]:** Only full column updates should be supported because cost is dominated by file access, not data volume, and predicate pushdown does not work well with partial updates. ([message](https://lists.apache.org/thread/rx45lxp71r6mh4k5r8nzx1vwz47y9559))
- **[[person/stevenzwu|Steven Wu]]:** If deletion vectors cover updates to few rows and full column updates cover many rows, the sparse representation is only needed for deleted rows, which could instead be filled with nulls or defaults. ([message](https://lists.apache.org/thread/qqzc28zxwy0cd3692smb3vmz78c2jqjt))
- **[[person/pvary|Peter Vary]]:** Tracking changed rows needs a merged _last_updated_sequence_number for both partial and full updates, which shrinks the benefit of partial updates and adds complexity. ([message](https://lists.apache.org/thread/p3y98zdnhwsbhtb79vo6dcrfxr33wg7m))
- **[[person/wgtmac|Gang Wu]]:** Maintaining the last-updated sequence number for the sparse format is too complicated, so full column updates are preferred. ([message](https://lists.apache.org/thread/058dotj2d3gdr9wl1wwqp5cxblc4vtd3))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The spec need not force an encoding for the position column, but engines should use delta encoding, which was 43 kb against 3910 kb for plain in his example. ([message](https://lists.apache.org/thread/j83wxcfnhxlhn6g6b6ddz6gtfz1odfbf))
- **[[person/pvary|Peter Vary]]:** Update files that materialize every row keep vectorized stitching a simple concatenation of column vectors, so that representation is strongly preferred for vectorized reads. ([message](https://lists.apache.org/thread/6bs5o0xb0hbkxr63mjn19cm5dm671oyd))
- **[[person/wgtmac|Gang Wu]]:** Dense update files help reads but complicate the SQL update plan, which must read before-update values or carry per-file metadata such as row counts. ([message](https://lists.apache.org/thread/jq1lo82tnocczbhvkvv8ks93f7yy7omm))
- **mkroll-db:** An internal dense, row-aligned proof of concept was slower than copy-on-write below about 16MB target file size and up to about 5x faster at 1GB, so the spec may need a writer fallback or row-range packing, and an explicit ordering rule with deletion vectors. ([message](https://lists.apache.org/thread/f81dq6bj8gg6woz666for0ry80vwnb78))
- **[[person/anuragmantri|Anurag Mantripragada]]:** The file-size crossover should not be a hard constraint on writers in the spec, and under the V4 single-file-commit design deletion vectors always win over column updates at read time. ([message](https://lists.apache.org/thread/olf541tyyqz5y8boswqgshbhz3782yj8))

References: [doc](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs), [iceberg#15445](https://github.com/apache/iceberg/issues/15445), [doc](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)
<!-- kb:generated:end -->

## Notes
