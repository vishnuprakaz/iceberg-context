---
id: thread/t-14cfe62770f38386
type: thread
title: Name mapping for data files that carry only some field IDs
date: '2026-11-03'
url: https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo
kind: discuss
status: open
messages: 7
sources:
- devlist:tct2yp45ytsb6dqw1tq7b8gnfnp7jndo
refs:
- gh:apache/iceberg#3542
- gh:apache/iceberg#3556
- gh:apache/iceberg#10835
- gh:apache/iceberg-cpp#1108
- gh:apache/iceberg-cpp#1109
- gh:apache/incubator-xtable#911
- gh:apache/iceberg-verification#14
links:
- rel: discussed
  to: initiative/conformance-testing
  confidence: extracted
  source: devlist:tct2yp45ytsb6dqw1tq7b8gnfnp7jndo
updated: '2026-11-13'
---

# Name mapping for data files that carry only some field IDs

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Name mapping for data files that carry only some field IDs](https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo) · **Started:** 2026-11-03 by slachiewicz · **Messages:** 7 (last 2026-11-12) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

slachiewicz reported that the spec is ambiguous for Parquet files where only some fields carry field IDs, and that Java, PyIceberg, iceberg-rust and iceberg-go each resolve such files differently. Delta tables with column mapping but without IcebergCompatV2 produce these files. He proposed the per-field reading: an embedded ID is used, and fields without one fall back to the name mapping. manuzhang and Jean-Baptiste Onofré found it reasonable; JB noted the Java Parquet and ORC visitors would have to stop overwriting embedded IDs and asked the spec to cover ID collisions. wgtmac said partial or broken IDs should stay implementation-specific. RussellSpitzer first supported per-field resolution, then, after checking history, said per-file was the original 2021 intent and the per-column wording arrived unintentionally in 2024; he prefers fixing that sentence and treating partial-ID support as a new feature. No agreement yet.

**Why it matters:** Readers in different languages currently return different results for the same partially-ID'd file, and the outcome decides whether implementations must change their name-mapping fallback.

## Outcome

No agreement. The latest message argues for restoring the per-file meaning in the spec and restarting partial-ID support as a new feature discussion.

## Positions

- **slachiewicz:** The spec should adopt per-field resolution: embedded IDs win and fields without an ID fall back to the name mapping. ([message](https://lists.apache.org/thread/tct2yp45ytsb6dqw1tq7b8gnfnp7jndo))
- **[[person/manuzhang|Manu Zhang]]:** The proposal is reasonable and matches the Java Avro reader; a spec PR should be opened for concrete discussion. ([message](https://lists.apache.org/thread/vbq01jtsfgg2zfomsryvj2xpzlfv2gf3))
- **Jean-Baptiste Onofré:** Per-field resolution makes sense, but the spec should state that a file's ID takes precedence and say what happens when a mapped ID collides with an embedded one. ([message](https://lists.apache.org/thread/2cy1bj1rxxj7lz9984b6y0hql70twb63))
- **[[person/wgtmac|Gang Wu]]:** Handling files with partial or broken field IDs should remain implementation-specific rather than be specified. ([message](https://lists.apache.org/thread/9wd2t4o66gr1t7zs2f6yycsljczk9wkj))
- **[[person/binarybrain-009|Daksh Dave]]:** Scope the change to missing IDs with an unambiguous mapping, and fail the read on collisions, checked before column pruning. ([message](https://lists.apache.org/thread/18k80hydxtsd8m3935r20hpgd2tnw4n7))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Per-file fallback was the original intent, so the 2024 sentence should be corrected and partial-ID support discussed as a new feature starting from use cases. ([message](https://lists.apache.org/thread/vgxtsjvcfhjq06lcg3mnstp2fyglgzbd))

References: [iceberg#3542](https://github.com/apache/iceberg/issues/3542), [iceberg#3556](https://github.com/apache/iceberg/issues/3556), [iceberg#10835](https://github.com/apache/iceberg/issues/10835), [iceberg-cpp#1108](https://github.com/apache/iceberg-cpp/issues/1108), [iceberg-cpp#1109](https://github.com/apache/iceberg-cpp/issues/1109), [incubator-xtable#911](https://github.com/apache/incubator-xtable/issues/911), [iceberg-verification#14](https://github.com/apache/iceberg-verification/issues/14)
<!-- kb:generated:end -->

## Notes
