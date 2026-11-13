---
id: thread/t-6b556fb65dd1775f
type: thread
title: Integrating EagerInputFile into the manifest reader
date: '2026-07-20'
url: https://lists.apache.org/thread/qhn00762nrxl1zmb817wqqq5tzlqolbq
kind: discuss
status: consensus
messages: 20
sources:
- devlist:qhn00762nrxl1zmb817wqqq5tzlqolbq
refs:
- gh:apache/iceberg#17284
- gh:apache/iceberg#16910
links:
- rel: discussed
  to: initiative/v4-metadata-tree
  confidence: extracted
  source: devlist:qhn00762nrxl1zmb817wqqq5tzlqolbq
- rel: started_by
  to: person/varun-lakhyani
  confidence: observed
updated: '2026-11-13'
---

# Integrating EagerInputFile into the manifest reader

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Integrate EagerInputFile into the manifest reader](https://lists.apache.org/thread/qhn00762nrxl1zmb817wqqq5tzlqolbq) · **Started:** 2026-07-20 by [[person/varun-lakhyani|Varun Lakhyani]] · **Messages:** 20 (last 2026-08-26) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Varun Lakhyani reported benchmarks on S3 showing that reading v4 Parquet manifests through EagerInputFile, which fetches a small file in one request, cut read time by roughly 25 to 55 percent, and asked to wire it into the manifest read path with a flag on by default. Russell Spitzer supported making it a default. Daniel Weeks objected to a manifest-specific shortcut and preferred building eager fetching into FileIO implementations so any read benefits. Russell argued the decision belongs to the code opening the file, since it is essentially a Parquet reader fix; Avro benchmarks were roughly neutral. Daniel listed three integration points (FileReader API, FileIO layer, at the point of use) and both agreed on the first. Varun moved the eager read into the Parquet reader, which now buffers files of one megabyte or less in one request. That exposed incorrect manifest lengths written by rewrite-table-path, since fixed. Russell considered the PR ready to merge.

**Why it matters:** The change affects every Parquet read of small files, not only manifests, and makes readers trust the file length passed in from metadata.

## Outcome

Agreed to integrate eager reads at the file reader level for Parquet instead of in the manifest reader or FileIO. The reworked PR buffers Parquet files of 1 MB or less in a single request; on August 26 it was described as ready to merge but not yet merged in the thread. ([message](https://lists.apache.org/thread/f5l472qtqrp2hosjsdfbk3qyhm2df37r), `devlist:f5l472qtqrp2hosjsdfbk3qyhm2df37r`)

## Positions

- **[[person/varun-lakhyani|Varun Lakhyani]]:** Wire EagerInputFile into the manifest read path behind a property that defaults to true, based on benchmark gains for v4 Parquet manifests. ([message](https://lists.apache.org/thread/6fhnlrm2jxbn187txglmf31ydwhzp8fc))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Eager fetching should be native to existing FileIO implementations with a size threshold, so any `InputFile::newStream` is accelerated, instead of a bespoke shortcut in ManifestFiles. ([message](https://lists.apache.org/thread/pzyj0bzy7ns2yyhyzybt5v8bw3sbk1dm))
- **[[person/danielcweeks|Daniel C. Weeks]]:** A full-file fetch is unlikely to be worse for Avro, since Avro files are usually read in full. ([message](https://lists.apache.org/thread/zfxl1dz5xcmqzvmppt4hpqxv8ctwyc5g))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The change is a performance fix for parquet-java and should live in Iceberg's Parquet reader code (Parquet.java), not add complexity to FileIO or apply to files such as Puffin or metadata.json. ([message](https://lists.apache.org/thread/dr7f41zpyzs43dt9plgvn7sdddbd7khw))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Of the three possible integration points, wrapping the stream at the point of use is the tightest coupling; the FileReader API may be the better place. ([message](https://lists.apache.org/thread/6jc5ob7hqkcj8zn8j3p8omszqcdzqvrw))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The eager path should not re-fetch the file length for HadoopInputFile, since that masks bugs and costs an extra request, while the Hadoop configuration pass-through is preserved via HadoopConfigurable. ([message](https://lists.apache.org/thread/z02kw08yskh9ho2j1vpb63sh5pzg5d2j))

References: [iceberg#17284](https://github.com/apache/iceberg/issues/17284), [iceberg#16910](https://github.com/apache/iceberg/issues/16910)
<!-- kb:generated:end -->

## Notes
