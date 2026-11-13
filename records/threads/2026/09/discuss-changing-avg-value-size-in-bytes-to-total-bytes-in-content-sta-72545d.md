---
id: thread/t-72545de0b328100f
type: thread
title: Changing avg_value_size_in_bytes to total_bytes in content stats
date: '2026-09-29'
url: https://lists.apache.org/thread/8f91nk08cq2pxtsdpf1o34ktthn7jcwk
kind: discuss
status: consensus
messages: 7
sources:
- devlist:8f91nk08cq2pxtsdpf1o34ktthn7jcwk
refs:
- gh:apache/iceberg#18308
links: []
updated: '2026-11-13'
---

# Changing avg_value_size_in_bytes to total_bytes in content stats

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Changing avg_value_size_in_bytes to total_bytes in content stats](https://lists.apache.org/thread/8f91nk08cq2pxtsdpf1o34ktthn7jcwk) · **Started:** 2026-09-29 by Eduard Tudenhöfner · **Messages:** 7 (last 2026-10-01) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Eduard Tudenhöfner announced that, after Slack discussions about avg_value_size_in_bytes making aggregations harder than necessary, the content stats field is being renamed to total_bytes and will track the total instead of the average (PR #18308). danielcweeks asked whether the average can still be derived from total_bytes and value_count; stevenzwu confirmed it can, and rdblue supported using the total. Eduard then noted that avgValueSizes() had just been added to ContentFile, Metrics, BaseFile, ContentFileParser and the REST spec and released in 1.12.0, and asked whether to deprecate it or replace it outright with RevAPI exceptions. rdblue suggested adding totalBytes and having avgValueSize compute its value from it. stevenzwu found that reasonable, with only totalBytes stored on disk, and added that the derived value need not stay in the JSON parser or REST spec since v4 tables are not yet supported there.

**Why it matters:** The V4 content stats field for variable-length value sizes changes from an average to a total, and the Java API released in 1.12.0 has to be adapted.

## Outcome

No one objected to storing total_bytes instead of the average. For the Java API, rdblue and stevenzwu favoured adding totalBytes with avgValueSize derived from it; the thread ends there without a reply from the proposer. ([message](https://lists.apache.org/thread/t42ro7ghnm5hxjy4sd6gs7j6tdzx133p), `devlist:t42ro7ghnm5hxjy4sd6gs7j6tdzx133p`)

## Positions

- **Eduard Tudenhöfner:** Track total bytes instead of the average value size, and asks how to handle the avgValueSizes() API already released in 1.12.0. ([message](https://lists.apache.org/thread/7bl7ccmtt6ro72rog2s0557m34qqs40t))
- **[[person/danielcweeks|Daniel C. Weeks]]:** If the average can be derived from total_bytes and value_count, the total is more valuable for estimation because it gives an explicit upper bound on size. ([message](https://lists.apache.org/thread/82jvzlcgycy8jy4g06prjm2g56pq44mb))
- **[[person/rdblue|Ryan Blue]]:** Use the total, add totalBytes, and keep avgValueSize as a value calculated from it. ([message](https://lists.apache.org/thread/rlnxdclnry12xgn675gd5v6xqokfphn3))
- **[[person/stevenzwu|Steven Wu]]:** Store only totalBytes and expose avgValueSize as a derived value in the Java API, but drop it from the JSON parser and REST spec. ([message](https://lists.apache.org/thread/t42ro7ghnm5hxjy4sd6gs7j6tdzx133p))

References: [iceberg#18308](https://github.com/apache/iceberg/issues/18308)
<!-- kb:generated:end -->

## Notes
