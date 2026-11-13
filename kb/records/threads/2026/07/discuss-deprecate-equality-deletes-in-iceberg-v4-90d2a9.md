---
id: thread/t-90d2a9cd80ec9ab2
type: thread
title: 'Deprecate equality deletes in Iceberg V4 (continued: forbidding new writes)'
date: '2026-07-23'
url: https://lists.apache.org/thread/9rvgx11ly1j3p570rg1rldsg1h10bzcx
kind: discuss
status: consensus
messages: 11
sources:
- devlist:9rvgx11ly1j3p570rg1rldsg1h10bzcx
refs:
- doc:12ifnKwiWemXcLndv19QJXOxh5o4lOsRxw_HsOgQ4sdU
links:
- rel: discussed
  to: initiative/v4-equality-deletes
  confidence: extracted
  source: devlist:9rvgx11ly1j3p570rg1rldsg1h10bzcx
- rel: started_by
  to: person/xndai
  confidence: observed
updated: '2026-11-13'
---

# Deprecate equality deletes in Iceberg V4 (continued: forbidding new writes)

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Deprecate Equality Deletes in Iceberg V4](https://lists.apache.org/thread/9rvgx11ly1j3p570rg1rldsg1h10bzcx) · **Started:** 2026-07-23 by [[person/xndai|Xiening Dai]] · **Messages:** 11 (last 2026-07-24) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

This part of the thread starts with xndai asking whether a V3 table containing equality deletes could upgrade to V4, and how writers could then be prevented from producing them. Respondents supported forbidding new equality delete writes in V4 while keeping existing ones readable. amogh-jahagirdar and rdblue explained that on upgrade the V4 root manifest would reference old V3 delete manifests, while V4 manifests would have no way to store equality deletes, so compliant writers cannot add them; no synchronous rewrite would be required. vaquar khan shared JMH read benchmarks comparing equality deletes with deletion vectors; danielcweeks and stevenzwu said the benchmarks do not capture write-cost differences or production cases with many delete files per data file. pvary listed Flink prerequisites he wants addressed before V4 is released; RussellSpitzer, stevenzwu and rdblue said a complete replacement is not needed before V4 ratification as long as a path exists. No formal decision is recorded.

**Why it matters:** Indicates V4 manifests will likely have no way to carry new equality deletes, so streaming writers must move to deletion vectors to use V4.

## Outcome

All respondents in this part of the thread supported forbidding new equality delete writes in V4 while keeping existing ones readable after upgrade; no vote or formal decision is recorded in these messages.

## Positions

- **[[person/xndai|Xiening Dai]]:** Asked whether V3 tables with equality deletes may upgrade to V4, since allowing their presence seems to leave no way to stop writers generating them, or whether upgrade must rewrite them. ([message](https://lists.apache.org/thread/9rvgx11ly1j3p570rg1rldsg1h10bzcx))
- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Supports forbidding new equality deletes in V4; upgraded tables keep V3 delete manifests referenced from the V4 root, equality deletes are not an allowed type in the V4 root, and rewrite on upgrade should not be required. ([message](https://lists.apache.org/thread/th77ksxhgw0mvb7y3x0016ntmv5fvdb4))
- **Steve:** Forbid new equality delete writes in V4 but keep upgrade a metadata-only operation, following the precedent of deletion vectors in V3; conversion can be a separate maintenance action. ([message](https://lists.apache.org/thread/z86y78ymlq067qgny4qp42by0j2nyy3b))
- **vaquar khan:** Benchmarks show equality delete read cost growing with delete ratio versus flat deletion vector cost; supports forbidding new equality delete writes in V4 while streaming upsert workloads stay on V3 until engines emit DVs. ([message](https://lists.apache.org/thread/2otsc6ndrjyb73jgdnfpmz5qgbco3xyg))
- **[[person/pvary|Peter Vary]]:** Supports disallowing new equality deletes in V4 but wants an approach that avoids committing them to a staging branch and an index written from the Flink job and reused across restarts before V4 is released. ([message](https://lists.apache.org/thread/3gxkk9o69vw6vh18f0ocn3kyhbsmk9rj))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Strongly supports removal; replacements need not exist at V4 ratification, equality deletes in V3 delete manifests are fine, but nothing should add or move one into V4 metadata. ([message](https://lists.apache.org/thread/5cg5xmoczbchftmqq7gr4l3n8fp970ok))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Equality deletes offer near-zero write cost that is hard to replace, but with limited adoption and many downsides he supports deprecating future use, reserving judgment on whether a replacement is needed. ([message](https://lists.apache.org/thread/g37hqf49ct2too1x28hyb0v29sx2hpts))
- **[[person/rdblue|Ryan Blue]]:** Upgrades can leave existing equality deletes in V3 delete manifests; not supporting them in V4 manifests effectively enforces the ban, and V5 could refuse upgrades with V3 delete manifests if abuse appears. ([message](https://lists.apache.org/thread/q0mnlchmg0t2w5495b4mwdvxdypwh396))
- **[[person/stevenzwu|Steven Wu]]:** Supports disallowing new equality deletes in V4; the shared benchmark understates the read problem because production data files can have hundreds or thousands of equality delete files applied. ([message](https://lists.apache.org/thread/d6g5vxkghj6tj4g1ptjpc9gsmr0o2ysk))
- **[[person/rdblue|Ryan Blue]]:** Equality deletes need not be fully replaced first; showing they are not required is enough, and Flink work should not be tightly coupled to V4. ([message](https://lists.apache.org/thread/0shbhczrsqkr67l3t8y5bgolf84fvglk))

References: [doc](https://docs.google.com/document/d/12ifnKwiWemXcLndv19QJXOxh5o4lOsRxw_HsOgQ4sdU)
<!-- kb:generated:end -->

## Notes
