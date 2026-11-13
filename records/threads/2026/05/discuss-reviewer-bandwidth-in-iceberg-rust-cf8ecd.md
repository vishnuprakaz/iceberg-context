---
id: thread/t-cf8ecdd2fd7d10db
type: thread
title: Reviewer bandwidth in iceberg-rust
date: '2026-05-28'
url: https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r
kind: discuss
status: no-conclusion
messages: 6
sources:
- devlist:hb12b05y2rxv98641dwdvdjh58po0h8r
refs: []
links: []
updated: '2026-11-13'
---

# Reviewer bandwidth in iceberg-rust

<!-- kb:generated:start -->
**Thread:** [[Discuss] Reviewer Bandwidth In Iceberg-Rust](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r) · **Started:** 2026-05-28 by jordepic · **Messages:** 6 (last 2026-05-29) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Jordan Epstein raised limited review capacity in iceberg-rust, saying he had heard of projects keeping their own forks because getting code reviewed is too hard, and listing missing features such as position delete writing, deletion vector writing and HDFS support. He suggested giving review mandates to trusted people from Rust projects that build on Iceberg (DataFusion Comet, RisingWave, Databend, Polars) or from major companies, focused on reaching parity with Java. Shawn (CTTY) agreed there is a reviewer bottleneck, said responsibility for quality rests with whoever merges, and pointed to community syncs where parity features are discussed. Jared Yu described the same bottleneck in PyIceberg and suggested nominating steady unofficial reviewers as committers. Anurag Mantripragada reported similar delays in the Spark connector but said committer standards should not be bypassed. Gang (wgtmac) and Renjie (liurenjie1024) said new reviewers need deep understanding of the codebase and trust built through contributions and quality reviews. No concrete action was agreed.

**Why it matters:** Contributors who want faster reviews are told the route is sustained contributions and quality reviews leading to committership, not delegated review mandates.

## Outcome

Participants agreed reviewer bandwidth is a bottleneck across Iceberg projects, but no change was decided; replies pointed to the existing committer guidelines of building trust through contributions and reviews.

## Positions

- **jordepic:** Increase iceberg-rust review capacity by giving trusted representatives of downstream Rust projects or major companies a mandate to review changes that bring the project to parity with Java. ([message](https://lists.apache.org/thread/hb12b05y2rxv98641dwdvdjh58po0h8r))
- **[[person/CTTY|Shawn Chang]]:** Agrees there is a reviewer bottleneck and welcomes outside reviews, but responsibility for code quality falls on the person who merges and the bottleneck may not be fixable immediately. ([message](https://lists.apache.org/thread/t0mjck5d5szkh6j716g7lct189fhxm29))
- **Jared Yu:** PyIceberg is similarly bottlenecked; the community should nominate reliable, frequent unofficial reviewers to become committers. ([message](https://lists.apache.org/thread/00njkwrm7fcw55n3mnrjlg27kn6syo0y))
- **[[person/anuragmantri|Anurag Mantripragada]]:** The Spark connector has the same bottleneck, and adding committers should not circumvent the qualities in the committer guidelines. ([message](https://lists.apache.org/thread/1h29ocbjbcwbj4s8fnyrl0h070q7h8zh))
- **[[person/wgtmac|Gang Wu]]:** Maintainers also carry long-term maintenance of merged code, so new reviewers must show deep understanding of the codebase and willingness to share that responsibility. ([message](https://lists.apache.org/thread/fhkct439xwz2zbcg3zzg714hq47q0121))
- **[[person/liurenjie1024|Renjie Liu]]:** The bottleneck is understanding, not coding; contributors are encouraged to give high-quality code reviews, which builds trust. ([message](https://lists.apache.org/thread/ztgof407gww4ctjq778w2lmkf3ojt9ch))
<!-- kb:generated:end -->

## Notes
