---
id: thread/t-6b0913d5ecae698f
type: thread
title: First-class Tag concept in the Iceberg REST Catalog
date: '2026-05-04'
url: https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b
kind: discuss
status: no-conclusion
messages: 5
sources:
- devlist:r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b
refs:
- gh:apache/iceberg#16165
- gh:apache/iceberg#15521
- gh:apache/iceberg#15750
- gh:apache/iceberg#13879
links:
- rel: discussed
  to: initiative/catalog-labels
  confidence: extracted
  source: devlist:r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b
- rel: discussed
  to: initiative/rest-spec
  confidence: extracted
  source: devlist:r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b
updated: '2026-11-13'
---

# First-class Tag concept in the Iceberg REST Catalog

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] First-class Tag concept in Iceberg REST Catalog](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b) · **Started:** 2026-05-04 by EJ Wang · **Messages:** 5 (last 2026-05-22) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

EJ Wang, working on tagging in Apache Polaris, proposed standardizing a first-class Tag in the REST catalog spec: a Tag entity with namespace-level CRUD, attachments with a value on tables, columns (by field-id), views and namespaces, a reverse lookup endpoint, and normative clauses on privileges, visibility and rename atomicity. Typed multi-field values, a governed/standard distinction and tag-to-policy binding were left out of the first pass. flyrain was concerned that catalogs and engines would interpret tags differently, so identical structures would not be interoperable in behavior. laskoviymishka pointed to the labels proposal (#15521, OpenAPI PR #15750) and suggested treating labels as the attachment mechanism with tags as a governance model on top. EJ Wang preferred Tag as a separate first-class REST concept, with storage shared with labels left as a catalog implementation choice, and proposed paired proposals with a coordinated boundary and a sync before the design doc. No decision was reached.

**Why it matters:** Whether tags become a separate REST catalog entity or a layer on labels decides how the two in-flight proposals are scoped.

## Outcome

The thread ends with EJ Wang planning a sync with the labels author and a full design doc, and flyrain still unconvinced that tags belong in the REST catalog spec.

## Positions

- **EJ Wang:** A first-class Tag entity with identity, allowed values and attachments should be standardized in the REST catalog spec, complementing read restrictions as the classification input side. ([message](https://lists.apache.org/thread/r5r3vpmrfy9wmmb4sdybwcjz1c4wld5b))
- **EJ Wang:** Tag should stay a separate first-class REST concept rather than depend on labels at the spec level; reusing label machinery for storage is a catalog implementation choice. ([message](https://lists.apache.org/thread/32mtdxdlq7w5j52rpfn802n6rphvhdrw))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Labels already cover most of the attachment side, so Tag definitions should be built on top of the labels track rather than as a parallel attachment mechanism. ([message](https://lists.apache.org/thread/5g6wpfdy0glphqcgjdol179dzfd9bn5l))
- **[[person/flyrain|Yufei Gu]]:** A new REST catalog entity should improve interoperability, and tags may not because their behavioral semantics vary across systems; if tags are added they should be a separate first-class entity. ([message](https://lists.apache.org/thread/65rrbbl38c31q4dgccxv31zbj89ldfwb))

References: [iceberg#16165](https://github.com/apache/iceberg/issues/16165), [iceberg#15521](https://github.com/apache/iceberg/issues/15521), [iceberg#15750](https://github.com/apache/iceberg/issues/15750), [iceberg#13879](https://github.com/apache/iceberg/issues/13879)
<!-- kb:generated:end -->

## Notes
