---
id: thread/t-5744501ab331d678
type: thread
title: 'Core: add an OpenTelemetry MetricsReporter'
date: '2026-05-21'
url: https://lists.apache.org/thread/vn4gglocg2g40p69mfrrh86qzkn1rr4b
kind: discuss
status: consensus
messages: 12
sources:
- devlist:vn4gglocg2g40p69mfrrh86qzkn1rr4b
refs:
- gh:apache/iceberg#16169
- gh:apache/iceberg#16250
- gh:apache/iceberg#14360
- gh:apache/iceberg#16573
links:
- rel: started_by
  to: person/moomindani
  confidence: observed
updated: '2026-11-13'
---

# Core: add an OpenTelemetry MetricsReporter

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Core: Add OpenTelemetry MetricsReporter](https://lists.apache.org/thread/vn4gglocg2g40p69mfrrh86qzkn1rr4b) · **Started:** 2026-05-21 by [[person/moomindani|Noritaka Sekiyama]] · **Messages:** 12 (last 2026-06-01) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

moomindani proposed an OpenTelemetry-based MetricsReporter in iceberg-core that exports ScanReport and CommitReport through an SDK registered by the host application, with only opentelemetry-api added as a compileOnly dependency (issue #16169, PR #16250). He asked whether the dependency is acceptable and whether the code belongs in iceberg-core or a separate module. Replies supported the idea. rdblue accepted the compileOnly dependency but asked that packaging meet user expectations. vaquar khan pointed out that the snapshot ID attribute has unbounded cardinality; it was removed. grantatspothero suggested a span-based reporter because per-table attributes can also be high cardinality; the author made the attribute set configurable and deferred spans. Documentation on packaging the exporter was added at Jean-Baptiste Onofré's request. The author said he would proceed with iceberg-core and compileOnly, having heard no objection.

**Why it matters:** It sets the pattern for an optional observability integration in iceberg-core: API-only compileOnly dependency, SDK and exporter supplied by the host, and bounded metric attributes.

## Outcome

No objection was raised to the compileOnly opentelemetry-api dependency or to placing the reporter in iceberg-core, and the author said he would proceed on that basis in PR #16250. Span-based reporting was deferred. ([message](https://lists.apache.org/thread/bhfv9qc17r3d11mh5ymdv03bfr2norf9), `devlist:bhfv9qc17r3d11mh5ymdv03bfr2norf9`)

## Positions

- **[[person/moomindani|Noritaka Sekiyama]]:** Add a metrics-only OpenTelemetry reporter in iceberg-core with opentelemetry-api as compileOnly; span support should be a separate design. ([message](https://lists.apache.org/thread/y1r1nwg849oyzw9xgtx9bw9wmbr4n9vv))
- **[[person/flyrain|Yufei Gu]]:** OpenTelemetry is a good vendor-neutral integration layer, and a REST catalog is usually not the right place to act as a metrics platform. ([message](https://lists.apache.org/thread/yhvxoooh98t1f442m8d5p55xktpby9cz))
- **[[person/rdblue|Ryan Blue]]:** Adding opentelemetry-api as compileOnly is fine, provided the packaging matches what users expect and avoids surprise failures. ([message](https://lists.apache.org/thread/hm5zlkytvmrhy2twgfqzyx3c5z32rzc9))
- **vaquar khan:** The snapshot ID attribute creates unbounded metric cardinality and should be removed, made opt-in or documented; a combined-reporter test should be added. ([message](https://lists.apache.org/thread/ty5vkh56n9ps86t8m4fsrfp6kvfv0kzl))
- **[[person/grantatspothero|Grant Nicholas]]:** A span-based implementation should be considered because table-name attributes can be high cardinality with thousands of tables. ([message](https://lists.apache.org/thread/0w8m9wm3rdsqn4ggosvcxyk2zh4lv5qh))
- **Jean-Baptiste Onofré:** Starting with metrics is reasonable and spans can come later; how to package the exporter should be documented. ([message](https://lists.apache.org/thread/tqwoddq8b1httvslsqcmo7yngcvoh1w3))

References: [iceberg#16169](https://github.com/apache/iceberg/issues/16169), [iceberg#16250](https://github.com/apache/iceberg/issues/16250), [iceberg#14360](https://github.com/apache/iceberg/issues/14360), [iceberg#16573](https://github.com/apache/iceberg/issues/16573)
<!-- kb:generated:end -->

## Notes
