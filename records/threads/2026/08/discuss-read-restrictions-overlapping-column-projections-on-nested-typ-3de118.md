---
id: thread/t-3de1185baccbc276
type: thread
title: 'Read restrictions: overlapping column projections on nested types'
date: '2026-08-07'
url: https://lists.apache.org/thread/9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg
kind: discuss
status: consensus
messages: 4
sources:
- devlist:9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg
refs:
- gh:apache/iceberg#12841
links:
- rel: discussed
  to: initiative/read-restrictions
  confidence: extracted
  source: devlist:9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg
- rel: started_by
  to: person/sungwy
  confidence: observed
updated: '2026-11-13'
---

# Read restrictions: overlapping column projections on nested types

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Read Restrictions: overlapping column projections on nested types](https://lists.apache.org/thread/9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg) · **Started:** 2026-08-07 by [[person/sungwy|Sung Yun]] · **Messages:** 4 (last 2026-08-26) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This part of the thread deals with what should happen when read restrictions returned by a catalog place projections on both a nested container and one of its descendants. Sung Yun withdrew an earlier claim that relaxing a disallow rule later would be fully backward-compatible, and shared a survey of existing systems: each resolves to a single policy per field value, none composes several masking transforms, and most make ancestor-descendant overlap impossible to author. Russell Spitzer pointed to the precedent of nested default values (PR #12841), where the ambiguous configuration was simply disallowed, and supported Option A: catalogs must not emit overlapping nested projections and readers must fail closed. Daniel Weeks, who had wanted a more opinionated stance on the conflict, said he was fine with putting the complexity on the catalog and disallowing overlap. Prashant Singh updated the spec PR with that conclusion.

**Why it matters:** Catalogs must resolve nested policy conflicts themselves, and clients reject overlapping projections instead of implementing precedence rules.

## Outcome

Overlapping projections on a nested type and its descendants are disallowed, with expectations on both the catalog and the client side; the spec PR was updated accordingly. ([message](https://lists.apache.org/thread/d6w5do38zgzrxf4r4nv3f14pvh59n2w3), `devlist:d6w5do38zgzrxf4r4nv3f14pvh59n2w3`)

## Positions

- **[[person/sungwy|Sung Yun]]:** Option A fits how existing policy engines behave, since surveyed systems resolve to one policy per field value; relaxing the rule later would not be fully backward-compatible. ([message](https://lists.apache.org/thread/9gsvkhsd4xr3po9wr3bwtfr9vzyrxqbg))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Follow the default-values precedent and disallow the ambiguous state: catalogs must not emit overlapping nested projections and readers must fail closed. ([message](https://lists.apache.org/thread/m8zh6cy6jh6ck5ygjyhblk02y4wvg9q6))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Would also have accepted a defined application order, but is fine with the catalog deconflicting or failing and overlap being disallowed. ([message](https://lists.apache.org/thread/50d2nhd9f3onwvymqsmkn9soc43y5n5z))

References: [iceberg#12841](https://github.com/apache/iceberg/issues/12841)
<!-- kb:generated:end -->

## Notes
