---
id: thread/t-f30173754f0d73b2
type: thread
title: Catalog-provided metadata tables
date: '2026-09-25'
url: https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn
kind: discuss
status: no-conclusion
messages: 13
sources:
- devlist:hrcyh8nqf1svrwnm279n466c75r3wwxn
refs:
- gh:apache/iceberg#15750
- gh:apache/iceberg#18046
- gh:apache/iceberg#18048
- gh:apache/iceberg#18049
- gh:apache/iceberg-go#2101
- doc:1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI
links:
- rel: started_by
  to: person/laskoviymishka
  confidence: observed
updated: '2026-11-13'
---

# Catalog-provided metadata tables

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Catalog-provided metadata tables](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn) · **Started:** 2026-09-25 by [[person/laskoviymishka|Andrei Tserakhau]] · **Messages:** 13 (last 2026-10-04) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After labels landed in the REST spec, laskoviymishka asked whether metadata tables may expose catalog-provided data, starting with a .labels table, even though existing metadata tables are deterministic projections of table metadata. rdblue questioned whether a SQL surface is needed at all, since engines consume labels programmatically, and rejected the join example as two unrelated queries. pvary said queryable, joinable labels contradict the agreed design where catalogs need not persist or version labels. manuzhang noted labels exist only for REST catalogs while metadata tables should work for all. laskoviymishka agreed the metadata table is not needed for now, with Spark DESCRIBE covering SQL consumers, and the Java PR was closed. He later proposed letting non-Java clients expose labels through their inspect APIs, beginning with iceberg-go; manuzhang objected that the API cannot distinguish a table without labels from a catalog that does not support them. The thread ends there.

**Why it matters:** Java/Spark metadata tables stay limited to projections of table metadata; labels are surfaced through SupportsLabels and DESCRIBE instead.

## Outcome

The Java labels metadata table (PR 18048) was dropped and closed in favor of DESCRIBE. The follow-up question about exposing labels through client inspect APIs ended with an unanswered objection.

## Positions

- **[[person/laskoviymishka|Andrei Tserakhau]]:** Labels are a reasonable first case for a catalog-provided, read-only metadata table that is empty when the catalog returns nothing. ([message](https://lists.apache.org/thread/hrcyh8nqf1svrwnm279n466c75r3wwxn))
- **[[person/rdblue|Ryan Blue]]:** Fine with a metadata table if there is a use for it, but labels are for engines and a SQL surface should not be assumed; not adding one is simpler. ([message](https://lists.apache.org/thread/87jfjo26vhgjdmppms4h8c72rmj8btoc))
- **[[person/pvary|Peter Vary]]:** Queryable and joinable labels contradict the read-path agreement that catalogs need not persist or version labels; if wanted, reconsider storing them in table metadata or properties. ([message](https://lists.apache.org/thread/s89pj1zdv5b7lwjzblbcx4ht3t4zmvyl))
- **[[person/manuzhang|Manu Zhang]]:** Labels exist only in the REST spec, whereas metadata tables should work for all catalogs. ([message](https://lists.apache.org/thread/jzhd57njpvmmbfp20n3y353r3pmm39rz))
- **[[person/rdblue|Ryan Blue]]:** The composition example is a cartesian join of two unrelated queries, leaving only direct user exposure as a use case, which is a nice-to-have nobody would miss. ([message](https://lists.apache.org/thread/zf3cyb7osw7prcf3zyybc3j02d316jsk))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** SQL-only consumers can be served by DESCRIBE in PR 18049, so the metadata table is not needed for now and can be revisited later. ([message](https://lists.apache.org/thread/7w6nsro9whvvjfq05cl2bh9qp23kpw1b))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Keep the Java/Spark decision but let PyIceberg, iceberg-rust and iceberg-go expose catalog-provided labels through their inspect library APIs, documented as catalog-provided and possibly empty. ([message](https://lists.apache.org/thread/5cnrhd3kfwzxywkj07kdls8o1twoomoq))
- **[[person/manuzhang|Manu Zhang]]:** The proposed inspect API cannot distinguish a table lacking labels from a catalog that does not support labels. ([message](https://lists.apache.org/thread/w9w107k5sblgn67z6bdtx7p4nw8o98kv))

References: [iceberg#15750](https://github.com/apache/iceberg/issues/15750), [iceberg#18046](https://github.com/apache/iceberg/issues/18046), [iceberg#18048](https://github.com/apache/iceberg/issues/18048), [iceberg#18049](https://github.com/apache/iceberg/issues/18049), [iceberg-go#2101](https://github.com/apache/iceberg-go/issues/2101), [doc](https://docs.google.com/document/d/1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI)
<!-- kb:generated:end -->

## Notes
