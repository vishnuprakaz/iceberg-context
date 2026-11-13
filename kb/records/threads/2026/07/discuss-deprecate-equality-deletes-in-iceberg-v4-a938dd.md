---
id: thread/t-a938dd33b7b841d9
type: thread
title: Deprecate equality deletes in Iceberg V4
date: '2026-07-14'
url: https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
kind: discuss
status: open
messages: 8
sources:
- devlist:ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
refs:
- gh:apache/iceberg#16961
- gh:apache/iceberg#16831
- gh:apache/iceberg#16844
- gh:apache/iceberg#16858
- gh:apache/iceberg#16874
- gh:apache/iceberg#16889
- gh:apache/iceberg#16948
links:
- rel: discussed
  to: initiative/v4-equality-deletes
  confidence: extracted
  source: devlist:ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
- rel: discussed
  to: initiative/secondary-indexes
  confidence: extracted
  source: devlist:ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
- rel: discussed
  to: initiative/flink-integration
  confidence: extracted
  source: devlist:ks01jpv40qjlvz4yop5tlqv4x5oxbwy6
- rel: started_by
  to: person/huaxingao
  confidence: observed
updated: '2026-11-13'
---

# Deprecate equality deletes in Iceberg V4

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Deprecate Equality Deletes in Iceberg V4](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6) · **Started:** 2026-07-14 by [[person/huaxingao|Huaxin Gao]] · **Messages:** 8 (last 2026-07-17) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

huaxingao restarted the 2024 discussion on deprecating equality deletes, now for V4. She argued they are cheap to write but costly to read, block CDC, row lineage and incremental maintenance of materialized views and secondary indexes, and that alternatives are now practical: the Flink ConvertEqualityDeletes task converts them to deletion vectors using a primary-key index, and the proposed secondary index spec includes a key-lookup index that would let writers emit deletion vectors directly. mxm clarified the Flink index is persisted in Flink state and supported deprecation. manuzhang asked how deprecation would work without an engine-agnostic solution. huaxingao first proposed 'deprecated but permitted', separating it from forbidding writes. stevenzwu and mxm favored forbidding equality delete writes in V4, which would simplify the adaptive metadata tree and give engines an incentive to move. huan233usc asked for benchmarks. huaxingao then changed her proposal to forbidding equality delete writes for V4 tables, with upsert workloads staying on V3 until engines are ready.

**Why it matters:** The proposal shifted from soft deprecation to a V4 ban on writing equality deletes, which would require Flink and other streaming writers to emit deletion vectors before adopting V4.

## Outcome

The proposer moved from 'deprecated but permitted' to forbidding equality delete writes in V4 tables; the discussion continues in later messages of the same subject and no decision is recorded here.

## Positions

- **[[person/huaxingao|Huaxin Gao]]:** Equality deletes should be deprecated in V4 because background conversion and a write-time key-lookup index recover their cheap-write advantage, and they block CDC, row lineage and incremental index maintenance. ([message](https://lists.apache.org/thread/ks01jpv40qjlvz4yop5tlqv4x5oxbwy6))
- **[[person/mxm|Maximilian Michels]]:** Supports deprecating in V4; the ConvertEqualityDeletes index is persisted in Flink RocksDB state, but conversion requires Flink today and no cross-engine way to avoid writing equality deletes exists yet. ([message](https://lists.apache.org/thread/2gt23z7soc459d3l2tfg0snl07x87s15))
- **[[person/manuzhang|Manu Zhang]]:** Supports deprecation but sees no clear path to do it in V4 before the index work lands, for example for Kafka Connect writers. ([message](https://lists.apache.org/thread/wfd3s65dpyzto8g8poffcg1tcqpgk5k7))
- **[[person/huaxingao|Huaxin Gao]]:** Initially proposed 'deprecated but permitted' in V4, with forbidding writes gated on an engine-agnostic path. ([message](https://lists.apache.org/thread/245hmv7wkfh9gc8nlsyvxbb9x4lnhpq8))
- **[[person/stevenzwu|Steven Wu]]:** Expected V4 to forbid equality delete writes, which would simplify the V4 adaptive metadata tree; the Flink sink would need to produce DVs only in V4. ([message](https://lists.apache.org/thread/92ym1wfbt4o7hnlbmy8sw4gm9t52sl07))
- **[[person/mxm|Maximilian Michels]]:** Soft deprecation gives engines no real incentive to stop; leans toward removing equality deletes for V4 tables while still reading them in V2 and V3. ([message](https://lists.apache.org/thread/4m8ctx896d2kc85wv2w6kvmwmycqp1zo))
- **[[person/huan233usc|Xin Huang]]:** Conceptually in favor, but asked for benchmarks comparing DVs with single-file commits in V4 against equality deletes in V3. ([message](https://lists.apache.org/thread/q2mbwo0f8pxh5pt8wjvs1mvwwxxoro5g))
- **[[person/huaxingao|Huaxin Gao]]:** Changed position to forbidding equality delete writes for V4 tables: it is a format decision that does not require every engine's write-time DV path on day one, since upsert workloads can stay on V3. ([message](https://lists.apache.org/thread/4y89ww1rx1qy56g4rckjqgvnks8mythf))

References: [iceberg#16961](https://github.com/apache/iceberg/issues/16961), [iceberg#16831](https://github.com/apache/iceberg/issues/16831), [iceberg#16844](https://github.com/apache/iceberg/issues/16844), [iceberg#16858](https://github.com/apache/iceberg/issues/16858), [iceberg#16874](https://github.com/apache/iceberg/issues/16874), [iceberg#16889](https://github.com/apache/iceberg/issues/16889), [iceberg#16948](https://github.com/apache/iceberg/issues/16948)
<!-- kb:generated:end -->

## Notes
