---
id: thread/t-1f7d78172b69f87c
type: thread
title: Changing the default append mode for Spark Streaming in Iceberg Java 1.13
date: '2026-07-30'
url: https://lists.apache.org/thread/sk1j4jo6s7ntr880tt7ktdt636nwzt5n
kind: discuss
status: consensus
messages: 9
sources:
- devlist:sk1j4jo6s7ntr880tt7ktdt636nwzt5n
refs:
- gh:apache/iceberg#17403
links:
- rel: discussed
  to: initiative/spark-integration
  confidence: extracted
  source: devlist:sk1j4jo6s7ntr880tt7ktdt636nwzt5n
- rel: started_by
  to: person/amogh-jahagirdar
  confidence: observed
updated: '2026-11-13'
---

# Changing the default append mode for Spark Streaming in Iceberg Java 1.13

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Changing the default append mode for Spark Streaming in Iceberg Java 1.13](https://lists.apache.org/thread/sk1j4jo6s7ntr880tt7ktdt636nwzt5n) · **Started:** 2026-07-30 by [[person/amogh-jahagirdar|Amogh Jahagirdar]] · **Messages:** 9 (last 2026-08-01) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Amogh Jahagirdar proposed that Spark Streaming writes switch from fast append to merging append by default in Iceberg 1.13. Fast append adds one small manifest per commit, which accumulates many tiny manifests and needs aggressive manifest rewriting to keep reads healthy; Flink and Kafka Connect already use merging append. A Spark write conf for the append mode was added in PR #17403 and defaults to fast append in 1.12 so users have time to adjust. Russell Spitzer asked for latency numbers and whether merging could be triggered heuristically. Gianluca Graziadei asked for p99 and maximum commit latency, since periodic merge spikes could exceed a micro-batch trigger interval. Daniel Weeks argued benchmarking is not needed because Flink and Kafka Connect are reference points, and Russell accepted that. Kevin Liu supported the change and said he would file a ticket for PyIceberg, which also uses fast append.

**Why it matters:** Spark Structured Streaming jobs that depend on one manifest per commit will need to set the write conf explicitly after upgrading to 1.13.

## Outcome

All replies supported flipping the default to merging append in 1.13; the request for latency benchmarks was not treated as a blocker. No formal decision message was posted.

## Positions

- **[[person/amogh-jahagirdar|Amogh Jahagirdar]]:** Flip the Spark streaming default to merging append in 1.13; fast append is not a good default, and other client libraries should re-evaluate their use of it. ([message](https://lists.apache.org/thread/sk1j4jo6s7ntr880tt7ktdt636nwzt5n))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Makes sense, but asks for latency numbers and whether merging could switch on automatically based on the number of small manifests. ([message](https://lists.apache.org/thread/qjh49hdw99q86q913t411cb3ccgr1dl6))
- **[[person/GGraziadei|Gianluca Graziadei]]:** Supports it in principle but wants tail commit latency data and consideration of jittering merge thresholds so pipelines do not spike in phase. ([message](https://lists.apache.org/thread/gfz72s9ng8swxd9wc7fy0mjmv6x2n678))
- **[[person/danielcweeks|Daniel C. Weeks]]:** Make the change without benchmarking; Flink and Kafka Connect already default to merging append and inline metadata management is better. ([message](https://lists.apache.org/thread/k99pgdprd4q7c7jmv0lrhdb5gzbhdr02))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Consistency with other engines is reasonable; longer term a default that does several fast appends and then a merge could be considered. ([message](https://lists.apache.org/thread/nosxgctwkh8hd2rjw46cxxrxgzdj098h))
- **Hongyue Zhang:** table.newAppend in iceberg-core already defaults to merge append, so using fast append is what needs justification. ([message](https://lists.apache.org/thread/s0gtgdwmhqd6jh5sxsywg66yq4qq2rht))
- **[[person/kevinjqliu|Kevin Liu]]:** Supports the change, since users can still opt in to fast append, and will file a ticket to switch PyIceberg to merge append. ([message](https://lists.apache.org/thread/589byrnmfwfovbpl7ohko9b75jf3y3v3))

References: [iceberg#17403](https://github.com/apache/iceberg/issues/17403)
<!-- kb:generated:end -->

## Notes
