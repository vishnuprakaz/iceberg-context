---
id: thread/t-4a4da37a5d6b9841
type: thread
title: Column update file representation
date: '2026-06-02'
url: https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo
kind: discuss
status: consensus
messages: 12
sources:
- devlist:1684dbkvsoromj4nnjwjrzzr2zotl5bo
refs:
- gh:apache/iceberg#16285
links:
- rel: discussed
  to: initiative/v4-column-updates
  confidence: extracted
  source: devlist:1684dbkvsoromj4nnjwjrzzr2zotl5bo
- rel: started_by
  to: person/xndai
  confidence: observed
updated: '2026-11-13'
---

# Column update file representation

<!-- kb:generated:start -->
**Thread:** [[Discuss] Column Update File Representation](https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo) · **Started:** 2026-06-02 by [[person/xndai|Xiening Dai]] · **Messages:** 12 (last 2026-07-02) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread covers how V4 column update files represent rows. xndai first raised that bumping the base file's sequence number when adding a column file breaks the spec invariant that a data sequence number never changes, and listed options for the deletion-vector case; anuragmantri moved that part to the metadata thread. anuragmantri reported a sync decision to leave dense versus sparse representation to engines as long as an explicit _pos column is written. pvary objected that leaving it open forces every reader to support sparse. stevenzwu and Gábor Kaszab argued the objections to dense (filler values, statistics, storage size, needing the base record count) are weak, and laskoviymishka proposed mandating dense now with sparse as a later extension tied to column families. anuragmantri agreed, and after the next sync reported the decision: column files must include values for deleted rows, using NULL, so every leaf column in a column update is nullable; partition tuples must always match file content.

**Why it matters:** Readers of V4 column files only need positional, dense stitching and do not have to implement a sparse merge path.

## Outcome

The sync agreed to mandate a column file representation that includes values for deleted rows, aligned with the base file, using NULL for deleted positions, so every leaf column in a column update is nullable. The partition tuple in file metadata must always match the file's content, and updates to it are permitted. ([message](https://lists.apache.org/thread/bj0sgk79yx0yt0wnr8jww2dsjsjc5tqj), `devlist:bj0sgk79yx0yt0wnr8jww2dsjsjc5tqj`)

## Positions

- **[[person/xndai|Xiening Dai]]:** Bumping the base file sequence number when adding a column file breaks the invariant that a data sequence number never changes and needs careful evaluation, including the deletion-vector case. ([message](https://lists.apache.org/thread/1684dbkvsoromj4nnjwjrzzr2zotl5bo))
- **[[person/pvary|Peter Vary]]:** Not specifying dense or sparse effectively requires all engines to support sparse, which adds a materialization step on the performance-sensitive read path. ([message](https://lists.apache.org/thread/274y3nc1q0p838k5x4mqxgmv7zbc36tt))
- **[[person/stevenzwu|Steven Wu]]:** The arguments against filler values are weak, and zero-copy stitching and simpler readers outweigh them; start with the dense representation. ([message](https://lists.apache.org/thread/bs4906f2v0t2p5ky79vf65jlrvcrlcs7))
- **Gábor Kaszab:** Prefers a single dense representation; experiments showed no significant storage difference between sparse and dense because _pos compresses worse as more rows are deleted. ([message](https://lists.apache.org/thread/26fvm80plfosqvf66q8pd38zc7vmh7dv))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Mandate dense now and keep sparse as a documented future extension with its own format version, to be decided as part of the column families effort. ([message](https://lists.apache.org/thread/12dn5tw8zgr1d9z24ncyzjl0d6tqwnc9))
- **[[person/stevenzwu|Steven Wu]]:** Column files are not necessarily short-lived, because separate column files for column families can be a desired long-term state. ([message](https://lists.apache.org/thread/llzndp1q8wn95p46cm12826sgkywk7xd))
- **[[person/anuragmantri|Anurag Mantripragada]]:** Initially reported that the choice between dense and sparse would be left to engines, then was convinced by the arguments for mandating dense. ([message](https://lists.apache.org/thread/c0c0t3vftsynwj5486cwjnynfhvxvbzd))

References: [iceberg#16285](https://github.com/apache/iceberg/issues/16285)
<!-- kb:generated:end -->

## Notes
