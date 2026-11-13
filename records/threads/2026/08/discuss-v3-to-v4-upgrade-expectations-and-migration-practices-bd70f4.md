---
id: thread/t-bd70f40d4eb1876d
type: thread
title: V3 to V4 upgrade expectations and migration practices
date: '2026-08-12'
url: https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky
kind: discuss
status: consensus
messages: 7
sources:
- devlist:fhs5rkkzlp3fy7wok2jh05p6dt7csyky
refs:
- gh:apache/iceberg#16100
- list:ko8cs3tgol97f0m20yozchpxlotzl1mj
links:
- rel: started_by
  to: person/Kurtiscwright
  confidence: observed
updated: '2026-11-13'
---

# V3 to V4 upgrade expectations and migration practices

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] V3 to V4 upgrade expectations and migration practices](https://lists.apache.org/thread/fhs5rkkzlp3fy7wok2jh05p6dt7csyky) · **Started:** 2026-08-12 by [[person/Kurtiscwright|Kurtis Wright]] · **Messages:** 7 (last 2026-08-13) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

The thread discusses what an upgrade to format version 4 guarantees when older metadata remains. Amogh Jahagirdar said the format has favoured cheap upgrades in which readers handle older structures, that implementations may still upgrade eagerly on write, that jumping from v1 or v2 to v4 is valid, and that the spec does not need to define migration as long as no degenerate cases exist after upgrade. Russell Spitzer agreed: a V4 reader must read V1, V2 and V3 manifest lists and manifests, moving metadata to V4 is an implementation decision, and V5 could be a breaking point that only accepts pure V4. Anoop Johnson pointed to the adapter layer in iceberg-core (#16100). Shawn (CTTY) accepted this and asked that implementations state how they migrate metadata and that the community document the limits of tables with mixed pre-V4 and V4 metadata. Manu Zhang asked whether this is premature while the V4 spec is early.

**Why it matters:** Implementers of V4 must keep reading pre-V4 manifests, and users should not assume that upgrading the format version gives the whole table V4 benefits at once.

## Outcome

Participants agreed that V4 upgrades stay cheap, V4 readers handle older manifests, and migrating metadata to the V4 structures is an implementation choice that needs no spec work. Whether and when to document the behaviour of partially migrated tables was left open. ([message](https://lists.apache.org/thread/wsjhl80pypnycrh3980d1d9q52pt3yfj), `devlist:wsjhl80pypnycrh3980d1d9q52pt3yfj`)

## Positions

- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** The format should keep enabling cheap upgrades while leaving implementations free to migrate older metadata eagerly or in the background; the spec need not define this. ([message](https://lists.apache.org/thread/6zmxv0zr06j4nvs7cozpz9m2z65nrpmo))
- **[[person/RussellSpitzer|Russell Spitzer]]:** A V4 reader must read V1, V2 and V3 manifest lists and manifests, migration needs no spec work, and V5 could be a breaking point allowing upgrades only from pure V4. ([message](https://lists.apache.org/thread/r6w5j228w724bzcr374zqsy9d2j9kncq))
- **[[person/CTTY|Shawn Chang]]:** Implementations should state if, when and how they migrate existing metadata to V4, and the community should document the behaviour and limitations of mixed pre-V4 and V4 metadata. ([message](https://lists.apache.org/thread/wsjhl80pypnycrh3980d1d9q52pt3yfj))
- **[[person/manuzhang|Manu Zhang]]:** Documentation would help, but the concern may be premature while the V4 spec is in its early stages; lessons from the V3 upgrade could be reused. ([message](https://lists.apache.org/thread/xbmslgxmnfw1lfm2d0nt803ox3zwff10))
- **[[person/CTTY|Shawn Chang]]:** V2 to V3 is not directly comparable because V4 changes the metadata structure, but the position delete to deletion vector guidance in V3 is a useful precedent for setting expectations. ([message](https://lists.apache.org/thread/5jcnrnpyp7r3v8myrhmkvtd10y0qh67o))

References: [iceberg#16100](https://github.com/apache/iceberg/issues/16100), [thread](https://lists.apache.org/thread/ko8cs3tgol97f0m20yozchpxlotzl1mj)
<!-- kb:generated:end -->

## Notes
