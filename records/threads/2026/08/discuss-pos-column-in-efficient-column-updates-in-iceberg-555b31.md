---
id: thread/t-555b31c6e34eed92
type: thread
title: _pos column in efficient column updates
date: '2026-08-24'
url: https://lists.apache.org/thread/sx4tndlb4vkcpj2yq9cob7fhddzd701x
kind: discuss
status: consensus
messages: 16
sources:
- devlist:sx4tndlb4vkcpj2yq9cob7fhddzd701x
refs:
- doc:1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs
links: []
updated: '2026-11-13'
---

# _pos column in efficient column updates

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] _pos column in efficient column updates in Iceberg](https://lists.apache.org/thread/sx4tndlb4vkcpj2yq9cob7fhddzd701x) · **Started:** 2026-08-24 by mkroll-db · **Messages:** 16 (last 2026-09-09) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

mkroll-db questioned why column update files in the efficient column updates design persist a _pos column, given that the dense, null-filled representation requires rows to be aligned with the base file and row counts can verify completeness. Leonid Lygin and laskoviymishka said the column is redundant, confusing, and creates two legal ways to implement reads. Gábor Kaszab noted it costs almost no storage with delta encoding and might help debugging, but agreed it adds unnecessary complexity. RussellSpitzer and anoopj favored removing the persisted value while keeping the _pos metadata column readable. anuragmantri said adding it was a conscious earlier choice but supported removal. rdblue preferred keeping it to detect writers that omit deleted rows, though not strongly. mkroll-db suggested making it optional, then agreed with RussellSpitzer that writers should verify alignment at write time. The Efficient Column Updates sync concluded that _pos will not be required and writing it will not be allowed.

**Why it matters:** Column update files rely solely on positional alignment with the base file, so implementations have a single read path and must not write _pos.

## Outcome

The Efficient Column Updates sync concluded that the _pos field will not be required and the spec will not suggest writers may materialize it; writing _pos in column files will not be allowed. ([message](https://lists.apache.org/thread/rxnr8wy4ov3sjrftr47nzxw75fdlvh2v), `devlist:rxnr8wy4ov3sjrftr47nzxw75fdlvh2v`)

## Positions

- **mkroll-db:** The dense null-filled representation implicitly encodes position and row counts verify completeness, so _pos is unnecessary; the doc should state row order must match the base file. ([message](https://lists.apache.org/thread/sx4tndlb4vkcpj2yq9cob7fhddzd701x))
- **Gábor Kaszab:** _pos is not needed with the dense representation except for troubleshooting, and experiments showed essentially no storage cost with delta encoding. ([message](https://lists.apache.org/thread/qvs1d4qsy8z0pgdht9cw3khy6jv41osw))
- **Leonid Lygin:** _pos is redundant, makes readers question the alignment rule, and creates two different legal ways to implement reads. ([message](https://lists.apache.org/thread/hmw7f956j2ppj2z5rk9c2rs6qm258qb2))
- **[[person/laskoviymishka|Andrei Tserakhau]]:** The column looks like a debugging leftover that confuses the read side; removing it simplifies implementation. ([message](https://lists.apache.org/thread/x3ck9x7tj17stw0939nzt7zwl5qgjh9o))
- **[[person/RussellSpitzer|Russell Spitzer]]:** A persisted field makes no sense when perfect alignment is expected; reading the file with the metadata _pos column should still work. ([message](https://lists.apache.org/thread/dx2j72qggpg38d8429skrsoq0z2b1jvb))
- **[[person/anoopj|Anoop Johnson]]:** The persisted _pos column is no longer necessary and should be removed; the _pos metadata column keeps working, which inherited row IDs need anyway. ([message](https://lists.apache.org/thread/o8y0t1bvbolt9s2l4n3m6dy7ph0ff9bn))
- **[[person/anuragmantri|Anurag Mantripragada]]:** Adding _pos was a conscious choice in an earlier sync, not a remnant, but he favors removing it if that eases implementation. ([message](https://lists.apache.org/thread/0gw6wg83m6zwb166twwn9fdq59z51xdj))
- **[[person/rdblue|Ryan Blue]]:** Prefers keeping it, because without the original row position a writer that omits deleted rows causes an undetectable and unrecoverable problem; not a strongly held view. ([message](https://lists.apache.org/thread/540hg5pmsxxmnxvysl7bv60o6o39hhr5))
- **mkroll-db:** Found no precedent for storing data purely for debugging; if not removed, make _pos optional and treat disagreement with the row ordinal as corruption. ([message](https://lists.apache.org/thread/k84jd995o2kw2sl1djotr1lm53lbdd8j))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Writers can detect position mismatches at write time and fail, so nothing needs to be persisted. ([message](https://lists.apache.org/thread/2coxz3444dqo4xxy70oh7jjg7snrt1j5))

References: [doc](https://docs.google.com/document/d/1Bd7JVzgajA8-DozzeEE24mID_GLuz6iwj0g4TlcVJcs)
<!-- kb:generated:end -->

## Notes
