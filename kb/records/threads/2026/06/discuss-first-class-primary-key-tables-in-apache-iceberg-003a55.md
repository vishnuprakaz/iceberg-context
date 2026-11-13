---
id: thread/t-003a5548469ee105
type: thread
title: First-class primary key tables in Apache Iceberg
date: '2026-06-20'
url: https://lists.apache.org/thread/o7tzt04by73l0hpjd58t2wgvl4ct9lrc
kind: discuss
status: no-conclusion
messages: 4
sources:
- devlist:o7tzt04by73l0hpjd58t2wgvl4ct9lrc
refs:
- doc:1re65fx3uqC7I_tJuS79IxLiB7HEN2Grt5qRIDjd3p-4
links:
- rel: discussed
  to: initiative/constraints
  confidence: extracted
  source: devlist:o7tzt04by73l0hpjd58t2wgvl4ct9lrc
updated: '2026-11-13'
---

# First-class primary key tables in Apache Iceberg

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] First-Class Primary Key Tables in Apache Iceberg](https://lists.apache.org/thread/o7tzt04by73l0hpjd58t2wgvl4ct9lrc) · **Started:** 2026-06-20 by chandra sekhar k · **Messages:** 4 (last 2026-07-04) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Chandra Sekhar K opened a discussion on adding a native primary-key table abstraction to Iceberg for CDC ingestion, streaming upserts and changelog consumption. He argued that identifier fields, equality deletes, position deletes and MERGE are low-level primitives that leave write semantics, storage layout, compaction and changelog generation to engine-specific solutions, and pointed to Apache Paimon's primary-key tables as prior art. Matt Butrovich pointed him to the existing constraints proposal, which covers PRIMARY KEY, and asked him to see where his ideas fit. After reading it, Chandra replied that the constraint proposal treats PRIMARY KEY and UNIQUE as informational metadata with enforcement and mutable-data semantics out of scope, and that he sees his work as complementary: the key metadata could be the foundation for optional primary-key table semantics. No one else replied and nothing was decided.

## Outcome

The proposer was redirected to the constraints proposal and described his work as complementary to it; there was no further discussion.

## Positions

- **chandra sekhar k:** Iceberg should standardize a primary-key table abstraction so CDC and upsert workloads do not depend on engine-specific solutions. ([message](https://lists.apache.org/thread/o7tzt04by73l0hpjd58t2wgvl4ct9lrc))
- **[[person/mbutrovich|Matt Butrovich]]:** The idea should be brought to the existing constraints proposal, which already covers PRIMARY KEY. ([message](https://lists.apache.org/thread/lln7l68m6kl5l7lclorqp18z8cgk1yf6))
- **chandra sekhar k:** The constraints proposal and primary-key table semantics are complementary: one standardizes the metadata, the other would build write, compaction and changelog behaviour on it. ([message](https://lists.apache.org/thread/z6rtyds23g81hwgpxjgcjl4yv5zhzdpl))

References: [doc](https://docs.google.com/document/d/1re65fx3uqC7I_tJuS79IxLiB7HEN2Grt5qRIDjd3p-4)
<!-- kb:generated:end -->

## Notes
