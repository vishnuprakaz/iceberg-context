---
id: thread/t-218176922d9b85f8
type: thread
title: 'Table and column label metadata in the Iceberg REST catalog: moving the read path to a vote'
date: '2026-08-26'
url: https://lists.apache.org/thread/0mpgn3p2xhlf5165m40oxbptmcf7f87m
kind: discuss
status: open
messages: 7
sources:
- devlist:0mpgn3p2xhlf5165m40oxbptmcf7f87m
refs:
- gh:apache/iceberg#15750
- doc:1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI
- yt:lCTV-Rhiwyc
links:
- rel: started_by
  to: person/laskoviymishka
  confidence: observed
updated: '2026-11-13'
---

# Table and column label metadata in the Iceberg REST catalog: moving the read path to a vote

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Table and Column Label Metadata in Iceberg REST Catalog](https://lists.apache.org/thread/0mpgn3p2xhlf5165m40oxbptmcf7f87m) · **Started:** 2026-08-26 by [[person/laskoviymishka|Andrei Tserakhau]] · **Messages:** 7 (last 2026-09-04) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

After a catalog community sync, Andrei Tserakhau restated the labels proposal as a single optional, read-only `labels` field on the load response holding flat key-value metadata the catalog already owns, with no interpretation or enforcement in the spec, and asked to move to a vote on the read path. Prashant Singh asked why the existing `config` map could not carry this and why a structured tag entity should not be defined first, citing inheritance, nested-field conflicts and stable identity for cross-catalog sync. Andrei answered that config is client configuration that can carry credentials, while labels are a separate scope, and that the read surface should precede the structured entity. Ryan Blue called reusing config dangerous and saw no reason to hold back a read-only field. Prashant said he would not veto. Andrei proposed adding guidance that clients treat labels as opaque unless they understand them. Kevin Liu supported the proposal.

**Why it matters:** It records the arguments for a separate `labels` field instead of reusing `config`, and that the read path is headed to a vote ahead of any structured tag model.

## Outcome

No vote result in this thread. The proposer intends to start a vote on the read path; the one stated objector said he would not veto.

## Positions

- **[[person/laskoviymishka|Andrei Tserakhau]]:** Vote on a minimal read-only flat `labels` field now and handle structured tag entities, renames, identity and cross-system sync in a follow-up. ([message](https://lists.apache.org/thread/0mpgn3p2xhlf5165m40oxbptmcf7f87m))
- **[[person/singhpk234|Prashant Singh]]:** Questions the need for labels when `LoadTableResult` config already carries non-standard keys, and prefers defining the structured tag entity first because flat key-values lack inheritance and stable identity for governance and catalog sync. ([message](https://lists.apache.org/thread/3yo28cl70fbspvn8jlokjhg51xg45nl8))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Config is client configuration that clients merge into session and FileIO properties and that may hold secrets, so labels need their own field; the flat read path comes first and the structured entity is added later. ([message](https://lists.apache.org/thread/zy7jrt2dzy5voo3bovr30hfqprq9g7br))
- **[[person/rdblue|Ryan Blue]]:** Mixing this metadata into catalog-controlled config is dangerous, and a read-only field should not wait on other endpoints, as with the function list and load endpoints. ([message](https://lists.apache.org/thread/kxj8nv2jdw15l2fvk6m1zlhto9l2ordy))
- **[[person/singhpk234|Prashant Singh]]:** Still prefers settling what tag metadata looks like (for example multi-valued labels) and consumption guidelines first, and is not convinced flat key-values suffice for governance, but will not veto a vote. ([message](https://lists.apache.org/thread/yhcbd7dtx5yjk7nx9gj7q9nhboxfxpx1))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** Proposes adding spec wording that clients should treat label contents as opaque unless they understand a label's semantics, while keeping the field minimal. ([message](https://lists.apache.org/thread/wn7jh6h9mf8h0go2tb2b5pggsxqry52f))
- **[[person/kevinjqliu|Kevin Liu]]:** Supports the proposal and likes that use cases are left unspecified; wants implementations to keep interoperability in mind. ([message](https://lists.apache.org/thread/n62gnhww3qzgvr1l2b5qg3qcbtlx69tj))

References: [iceberg#15750](https://github.com/apache/iceberg/issues/15750), [doc](https://docs.google.com/document/d/1aj-6JlfBiMYEEVtNuh5WLMOrRQiMCcyYUGbouPM4hXI), [video](https://www.youtube.com/watch?v=lCTV-Rhiwyc)
<!-- kb:generated:end -->

## Notes
