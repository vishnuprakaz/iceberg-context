---
id: thread/t-7c950e8f34655555
type: thread
title: Non-overlapping index region files
date: '2026-09-30'
url: https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h
kind: discuss
status: no-conclusion
messages: 6
sources:
- devlist:8zq10wdsz5rx8v35zgon24r4gnsjsv9h
refs: []
links:
- rel: discussed
  to: initiative/secondary-indexes
  confidence: extracted
  source: devlist:8zq10wdsz5rx8v35zgon24r4gnsjsv9h
- rel: started_by
  to: person/CTTY
  confidence: observed
updated: '2026-11-13'
---

# Non-overlapping index region files

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Non-overlapping index region files](https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h) · **Started:** 2026-09-30 by [[person/CTTY|Shawn Chang]] · **Messages:** 6 (last 2026-10-02) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Shawn Chang asked why the index spec requires region files to be globally ordered and non-overlapping, pointing to write amplification, maintenance complexity and the difficulty of relaxing the rule later, and asked for the alternatives considered to be documented. Péter Váry answered that the design optimizes for fast, predictable single-key lookups: with cached index metadata, a key resolves with one small region file read. He listed three alternatives that were considered (a table-like layout, bounded overlay files in a mini-LSM style, and a global update file), each of which makes readers consult several files. Shawn replied that a strict cap on overlay files would still bound the worst case and would help covering indexes. Péter responded that region files are expected to be about 4 MB, so writing an overlay costs about as much as rewriting the region, and that covering indexes are not being optimized for at this stage. The thread ends there.

**Why it matters:** It records the reasoning behind a format-level invariant that index writers and maintenance jobs must uphold.

## Outcome

The rationale for the non-overlap invariant was explained and its author kept the position; the thread ends without a change to the spec or a stated agreement.

## Positions

- **[[person/CTTY|Shawn Chang]]:** The non-overlap invariant brings write amplification and maintenance cost, and its rationale versus alternatives like a mini LSM should be documented, including why it is a format rule rather than writer guidance. ([message](https://lists.apache.org/thread/8zq10wdsz5rx8v35zgon24r4gnsjsv9h))
- **[[person/pvary|Peter Vary]]:** Non-overlapping ranges give a single region-file lookup per key; alternatives make lookup time depend on maintenance state, and recommendations alone have not been enough in past experience. ([message](https://lists.apache.org/thread/nbq4hfxqm05q72zcmbmd1xbvf1pdk61q))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Understood that Ryan's proposal with a single bounded region file, so at most two files per region, had already been settled on. ([message](https://lists.apache.org/thread/ov6k4d58drvsvvf245ozcs0zykpv5hp8))
- **[[person/pvary|Peter Vary]]:** Start with the simpler non-overlapping solution and move on only when more data supports it. ([message](https://lists.apache.org/thread/dqjv7n4mg7wjkmxkm9bzbo0ktfh6dbpv))
- **[[person/CTTY|Shawn Chang]]:** A capped number of overlay files keeps worst-case reads bounded and lets maintenance absorb small updates, which may be a good trade for covering indexes. ([message](https://lists.apache.org/thread/fwqx0mp3dv07tqbzymg5bw8djzcwqx6n))
- **[[person/pvary|Peter Vary]]:** With region files around 4 MB an overlay costs about the same as rewriting the region; covering indexes are a separate discussion. ([message](https://lists.apache.org/thread/w4poj7wroo94309xwrclsjgz3p3vxlwp))
<!-- kb:generated:end -->

## Notes
