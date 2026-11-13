---
id: thread/t-9a2fc459da7341e3
type: thread
title: Column update file representation when deletion vectors are present
date: '2026-05-20'
url: https://lists.apache.org/thread/jbh1gbrso5h6l4by9rh9poy2cjjtb8j0
kind: discuss
status: no-conclusion
messages: 11
sources:
- devlist:jbh1gbrso5h6l4by9rh9poy2cjjtb8j0
refs:
- doc:1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs
links:
- rel: started_by
  to: person/anuragmantri
  confidence: observed
updated: '2026-11-13'
---

# Column update file representation when deletion vectors are present

<!-- kb:generated:start -->
**Thread:** [[Discuss] Column Update File Representation](https://lists.apache.org/thread/jbh1gbrso5h6l4by9rh9poy2cjjtb8j0) · **Started:** 2026-05-20 by [[person/anuragmantri|Anurag Mantripragada]] · **Messages:** 11 (last 2026-05-28) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

With a dense representation for column update files already agreed, Anurag Mantripragada asked what a column file should contain at positions the base file has deleted. Option 1 (positional alignment) keeps the base file's row count and writes filler values such as NULLs at deleted positions, so stitching is a zero-copy column swap. Option 2 (applied deletes) stores only live rows plus a _pos column, which keeps Parquet statistics accurate but needs a scatter operation that PyArrow and arrow-rs do not readily offer. Replies leaned toward Option 1: measurements showed the storage overhead of NULL filler is small, and reviewers from the Rust, Go and Delta side reported Option 1 is simpler to implement. Open points raised were padding trailing deleted rows on write, which statistics writers must correct, row-group misalignment between base and column files, and how equality deletes interact with column files. The thread ends without a formal decision.

**Why it matters:** The choice fixes how every implementation (Java, Python, Rust, Go, C++) must write and stitch V4 column update files.

## Outcome

Replies leaned toward Option 1 (positional alignment), but no decision is stated in the thread and the question of equality-delete handling was still being debated in the last messages.

## Positions

- **[[person/anuragmantri|Anurag Mantripragada]]:** Laid out the two options and found that Option 2 needs a scatter primitive that is cheap in Spark's ColumnVector but missing or costly in PyArrow and arrow-rs. ([message](https://lists.apache.org/thread/jbh1gbrso5h6l4by9rh9poy2cjjtb8j0))
- **[[person/wgtmac|Gang Wu]]:** Option 1 without _pos is more naturally compatible with future column families because stitching relies on implicit row alignment. ([message](https://lists.apache.org/thread/0b7xky2vy370ln6phqj5fx7odqdmgvwq))
- **Gábor Kaszab:** Storage overhead and stats accuracy should not decide the choice; leans toward always writing _pos, and notes positional alignment needs the base row count to pad trailing deleted rows. ([message](https://lists.apache.org/thread/lbt0p0vdhl38yjqxjc03g56lz5xp46zx))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Supports Option 1 based on a Delta proof of concept where positional alignment kept the read path simple, and says arrow-rs and arrow-go lack the kernels Option 2 needs. ([message](https://lists.apache.org/thread/s6zdvf9npbgbny3b206hfl044skgmnpl))
- **[[person/mbutrovich|Matt Butrovich]]:** Neither option is blocked in iceberg-rust; sketched an Option 1 reader and flagged that misaligned Parquet row groups force periodic buffer copies when stitching. ([message](https://lists.apache.org/thread/8rdjpot2oconwnodlkjog544pxrds7m3))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** The spec should state which statistics (null_count, value_count) writers must adjust for filler values and should describe compaction mechanics. ([message](https://lists.apache.org/thread/jlts14wvvd0n5koo3tz780ql9fx6837r))
- **[[person/xndai|Xiening Dai]]:** Not supporting equality deletes with column updates is a major limitation; proposed either evaluating them on the old base column values or materializing them as position deletes when the column file is written. ([message](https://lists.apache.org/thread/46rc8v2ft6grlqkc2hfpzpvgrzjc5fgd))
- **Gábor Kaszab:** Reading old column values for equality deletes is too complex and inefficient, and silently rewriting equality deletes into DVs should be left to users. ([message](https://lists.apache.org/thread/xprc6rtn3wyndrj3vhrngklz9x2wwfoy))

References: [doc](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)
<!-- kb:generated:end -->

## Notes
