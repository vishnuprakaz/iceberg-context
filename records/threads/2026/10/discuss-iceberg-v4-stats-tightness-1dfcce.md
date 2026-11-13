---
id: thread/t-1dfccee77a1376e9
type: thread
title: Iceberg v4 stats tightness
date: '2026-10-05'
url: https://lists.apache.org/thread/tv7bvqctdfh5qng1sx5rp8r4r00nsv60
kind: discuss
status: consensus
messages: 9
sources:
- devlist:tv7bvqctdfh5qng1sx5rp8r4r00nsv60
refs:
- doc:13DbwnwKQXjvY3vRcFJo-qVAQWk-GB4zLzzYmFdPntZg
links:
- rel: started_by
  to: person/anoopj
  confidence: observed
updated: '2026-11-13'
---

# Iceberg v4 stats tightness

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg v4 Stats Tightness](https://lists.apache.org/thread/tv7bvqctdfh5qng1sx5rp8r4r00nsv60) · **Started:** 2026-10-05 by [[person/anoopj|Anoop Johnson]] · **Messages:** 9 (last 2026-10-16) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

anoopj raised that in v4, stats tightness (whether lower and upper bounds actually exist among a file's live rows) is assumed lost once a deletion vector is attached, which disables metadata-only query optimizations, and shared a document with options for representing tightness alongside a DV. RussellSpitzer analyzed four usage patterns and concluded the realistic ones, a DV writer that repairs bounds and a command that restores tight stats, only need a file-wide flag rather than per-column tightness. danielcweeks, Eduard Tudenhöfner, Hongyue Zhang, szehon-ho and stevenzwu agreed. Hongyue Zhang noted that truncated bounds on variable-length columns follow from the column type, and that tightness is undefined for entries in upgraded tables. anoopj confirmed entries in existing v3 manifests lack the flag and are treated as wide. He then announced consensus on a file-level flag and proposed extending tightness to null, NaN and value counts and renaming tight_bounds to tight_stats, to be discussed at the next sync.

**Why it matters:** V4 tracks stats tightness per file entry rather than per column, which lets DV writers that repair bounds keep metadata-only optimizations available.

## Outcome

Consensus on a file-level tightness flag. A follow-up proposal to extend tightness to null/NaN/value counts and rename the field to tight_stats was left for the next v4 adaptive metadata tree sync. ([message](https://lists.apache.org/thread/p2kq8pjsy803kv8n66698z8gj4mf7hrm), `devlist:p2kq8pjsy803kv8n66698z8gj4mf7hrm`)

## Positions

- **[[person/anoopj|Anoop Johnson]]:** V4 needs a way to represent stats tightness even when a DV is attached, so metadata-only optimizations keep working. ([message](https://lists.apache.org/thread/tv7bvqctdfh5qng1sx5rp8r4r00nsv60))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The realistic cases, a DV writer that repairs bounds and an all-or-nothing restore command, only need one file-level flag; per-column tightness is unnecessary complexity. ([message](https://lists.apache.org/thread/w9l4n4l40ybwmq455kj5l3d6hndv04cc))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Use cases for per-column tightness are unlikely or narrow; go with the file-wide flag. ([message](https://lists.apache.org/thread/p4volkntwfmmmp7zrwgvg9os7b9dvqb8))
- **Hongyue Zhang:** A per-entry flag simplifies writer bookkeeping; truncation of variable-length columns is a schema property needing no extra metadata, and tightness is undefined for pre-upgrade entries. ([message](https://lists.apache.org/thread/0r64rnn0t3dtlhj1pb4ckkt2s7yow2cq))
- **[[person/anoopj|Anoop Johnson]]:** Files in existing v3 manifests have no flag and are assumed wide; new v4 files get true without DVs and false with an attached DV. ([message](https://lists.apache.org/thread/3hgmpbz2kvzxt5h378w2n72jglhp628p))
- **[[person/anoopj|Anoop Johnson]]:** Proposes expanding tightness to cover null, NaN and value counts and renaming tight_bounds to tight_stats. ([message](https://lists.apache.org/thread/p2kq8pjsy803kv8n66698z8gj4mf7hrm))

References: [doc](https://docs.google.com/document/d/13DbwnwKQXjvY3vRcFJo-qVAQWk-GB4zLzzYmFdPntZg)
<!-- kb:generated:end -->

## Notes
