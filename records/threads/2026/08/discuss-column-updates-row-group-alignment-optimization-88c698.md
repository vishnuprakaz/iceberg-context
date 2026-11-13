---
id: thread/t-88c698db226931c9
type: thread
title: 'Column updates: row group alignment optimization'
date: '2026-08-12'
url: https://lists.apache.org/thread/lqo71bs2hvzj38f4ljrkz77ncq4boltl
kind: discuss
status: consensus
messages: 12
sources:
- devlist:lqo71bs2hvzj38f4ljrkz77ncq4boltl
refs: []
links:
- rel: discussed
  to: initiative/v4-column-updates
  confidence: extracted
  source: devlist:lqo71bs2hvzj38f4ljrkz77ncq4boltl
updated: '2026-11-13'
---

# Column updates: row group alignment optimization

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Column Updates: Row Group alignment optimization](https://lists.apache.org/thread/lqo71bs2hvzj38f4ljrkz77ncq4boltl) · **Started:** 2026-08-12 by Leonid Lygin · **Messages:** 12 (last 2026-08-13) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Leonid Lygin proposed an optional metadata flag on column files (for example ColumnFile.containsAlignedRowGroups) indicating that a column file's Parquet row groups have the same row boundaries as the base file, so readers can swap column chunks directly and avoid reading and discarding extra data. RussellSpitzer and anoopj replied that a reader must open both footers before decoding anyway and can detect alignment there by comparing row boundaries. Leonid asked whether scan planning needs the information; danielcweeks and RussellSpitzer answered that planning uses the base file's split offsets and column files are loaded only when projected. Leonid accepted that split offsets cover both planning and execution. pvary saw the flag as unnecessary but would like the reference implementation to be able to write aligned files optionally. anuragmantri summarized that no flag is needed and that how writers align row groups is left to implementations; rdblue advised against adding the topic to the design doc.

**Why it matters:** The column file metadata will not carry a row group alignment field; readers are expected to derive alignment from Parquet footers.

## Outcome

Participants agreed that a separate row group alignment flag is not necessary; how writers produce aligned row groups is left to individual implementations and is not part of the spec. ([message](https://lists.apache.org/thread/z8olpfgblzvtgmxzvxryb7lkt5pvrgw0), `devlist:z8olpfgblzvtgmxzvxryb7lkt5pvrgw0`)

## Positions

- **Leonid Lygin:** Proposed a column file metadata flag marking row groups as aligned with the base file to enable zero-copy reads, then agreed that split offsets solve the planning and execution problem. ([message](https://lists.apache.org/thread/n8c94o9gz6qst9kl7qop9n2onbptfsj3))
- **[[person/pvary|Peter Vary]]:** The flag is unnecessary because the same read algorithm handles aligned and unaligned files, but optionally writing aligned files would be nice to have in the reference implementation. ([message](https://lists.apache.org/thread/gr54vt1jp4c7sn34my2cbbcwt4sjyjsk))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Readers already open both footers and can derive alignment there, so a metadata flag does not change split planning or which column file ranges a task needs. ([message](https://lists.apache.org/thread/92x57xnpt187k7c7mxppgzz2bj60mrc6))
- **[[person/anoopj|Anoop Johnson]]:** There is no advantage to tracking alignment in metadata; split_offsets is justified only because offsets are needed at planning time before footers are opened. ([message](https://lists.apache.org/thread/vsb3gwnkqrndj8321fym23h5t476s3xd))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Scan planning is based only on base files, and column update files are loaded when projected, using row counts to decide which portions to read. ([message](https://lists.apache.org/thread/r5w66o1vvmhm2rpovw2x8twxfrt5hcg2))
- **[[person/rdblue|Ryan Blue]]:** Do not add this to the design doc; readers should automatically read only the column file row groups needed for their tasks. ([message](https://lists.apache.org/thread/h7xr4m1k0n1o9h8cv8sljhwqls03wo3m))
- **[[person/GGraziadei|Gianluca Graziadei]]:** A flag would duplicate information derivable from the footers and the two could drift apart. ([message](https://lists.apache.org/thread/hj2msn2yrb6yfwow52g9j8y9rkmc7mw8))
<!-- kb:generated:end -->

## Notes
