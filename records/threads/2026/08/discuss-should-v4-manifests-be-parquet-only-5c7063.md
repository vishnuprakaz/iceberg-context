---
id: thread/t-5c70639b9c0f57ff
type: thread
title: Should V4 manifests be Parquet-only?
date: '2026-08-11'
url: https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y
kind: discuss
status: consensus
messages: 13
sources:
- devlist:fym02576n5sqy298fjxl0xmsv9z5rb7y
refs:
- gh:apache/iceberg#16025
- yt:dDZKzz3PKIk
links:
- rel: started_by
  to: person/stevenzwu
  confidence: observed
updated: '2026-11-13'
---

# Should V4 manifests be Parquet-only?

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] should V4 manifests be Parquet-only?](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y) · **Started:** 2026-08-11 by [[person/stevenzwu|Steven Wu]] · **Messages:** 13 (last 2026-10-20) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After a column update sync, Steven Wu asked whether V4 manifests should be Parquet-only rather than keeping Avro as an option. Avro manifests cannot support projection reads such as reading only column stats, and offering both formats forces every integration to choose. Anoop Johnson, Russell Spitzer and Manu Zhang supported Parquet-only; Anoop noted that the root manifest format is not tracked and that upgraded tables would still carry V3 Avro leaf manifests. Péter Váry preferred keeping the infrastructure open to several formats but said he would not oppose removing Avro for metadata. In October Kevin Liu reported that the merged AMT spec has V4 manifests written in Parquet, and proposed also dropping ORC and Avro as data file formats in V4. Others asked for a separate thread for that, and several said data file formats should stay open.

**Why it matters:** Implementations of V4 must write manifests in Parquet while still reading Avro manifests from upgraded tables.

## Outcome

The merged AMT spec (PR #16025) has V4 manifests written in Parquet; upgraded tables can keep existing Avro manifests, but new or rewritten manifests must be Parquet. The follow-on proposal to drop ORC and Avro data files was deferred to a new thread. ([message](https://lists.apache.org/thread/l703q6mcyzbgkfczs91mj5bffk1k5pj4), `devlist:l703q6mcyzbgkfczs91mj5bffk1k5pj4`)

## Positions

- **[[person/stevenzwu|Steven Wu]]:** Require Parquet for V4 manifests to reduce the decision burden on integrations and to get projection reads for scan planning. ([message](https://lists.apache.org/thread/fym02576n5sqy298fjxl0xmsv9z5rb7y))
- **[[person/anoopj|Anoop Johnson]]:** Parquet-only simplifies the spec and implementations; supporting Avro root manifests would require tracking the root manifest format. ([message](https://lists.apache.org/thread/7t93x05mhd33bksfm2mqfpnzxrnkc4oo))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Neutral with a slight bias to Parquet-only, since converging on a single file format is preferable. ([message](https://lists.apache.org/thread/8zfx7owzxhvbdh7snzrns5oz5q81bfjb))
- **[[person/pvary|Peter Vary]]:** Slightly prefers supporting multiple metadata formats and keeping InternalData, but would not oppose removing Avro for metadata; is more concerned about data file formats. ([message](https://lists.apache.org/thread/dwwd62mf3v11yn4376y5ptvskphg0rm3))
- **[[person/kevinjqliu|Kevin Liu]]:** With V4 manifests now Parquet-only, proposes dropping ORC and Avro as data file formats in V4. ([message](https://lists.apache.org/thread/l703q6mcyzbgkfczs91mj5bffk1k5pj4))
- **[[person/manuzhang|Manu Zhang]]:** A data file format change needs its own thread; prefers one format in the Java reference implementation while leaving options open in the spec. ([message](https://lists.apache.org/thread/zqkh0111czrzz39pgrlt7pz7nl0lj9wh))
- **[[person/zhjwpku|Junwang Zhao]]:** Keeping data files in open formats is worth the effort given options like Vortex, Lance and Nimble. ([message](https://lists.apache.org/thread/llgozzmnvyopcjdm3jjl4thxh5q346pt))

References: [iceberg#16025](https://github.com/apache/iceberg/issues/16025), [video](https://www.youtube.com/watch?v=dDZKzz3PKIk)
<!-- kb:generated:end -->

## Notes
