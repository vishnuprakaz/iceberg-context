---
id: thread/t-449e67b8e640cd82
type: thread
title: 'Iceberg Rust: moving the DataFusion integration into a separate repository'
date: '2026-08-31'
url: https://lists.apache.org/thread/k3rqkf2k7zcxh9ggboblymynkzf3m61c
kind: discuss
status: open
messages: 6
sources:
- devlist:k3rqkf2k7zcxh9ggboblymynkzf3m61c
refs: []
links:
- rel: discussed
  to: initiative/iceberg-rust
  confidence: extracted
  source: devlist:k3rqkf2k7zcxh9ggboblymynkzf3m61c
updated: '2026-11-13'
---

# Iceberg Rust: moving the DataFusion integration into a separate repository

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Iceberg Rust: moving the DataFusion integration into a separate repository](https://lists.apache.org/thread/k3rqkf2k7zcxh9ggboblymynkzf3m61c) · **Started:** 2026-08-31 by Gabriel Musat · **Messages:** 6 (last 2026-09-04) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Gabriel Musat noted that reviewer bandwidth is slowing the iceberg-datafusion crate in apache/iceberg-rust, while keeping the crate in that repository has value for testing, design and governance. He proposed giving a couple of Apache DataFusion PMC members committer access limited to that crate through a CODEOWNERS file. Renjie Liu was unsure that is feasible and said testing should not block a move; he preferred moving the crate to the Apache DataFusion project, since most of the code relates to DataFusion. Xuanwo and Andy Grove supported moving it under the DataFusion PMC, noting Comet is the largest downstream user. Andrew Lamb, DataFusion PMC chair, saw consensus on moving the code to DataFusion governance within the ASF and proposed a process: create a new Apache repository, open a PR with the code, then hold formal votes on the Iceberg and DataFusion dev lists. The thread ends with that proposal.

**Why it matters:** If carried out, DataFusion integration changes would be reviewed and released under the DataFusion project instead of apache/iceberg-rust.

## Outcome

Respondents favoured moving the integration to DataFusion governance within the ASF; a process with a new repository and votes on both dev lists was proposed but not yet carried out in the thread. ([message](https://lists.apache.org/thread/1mzshyr7mk9r28dvxbjw71nwn3dplwt1), `devlist:1mzshyr7mk9r28dvxbjw71nwn3dplwt1`)

## Positions

- **Gabriel Musat:** Keep iceberg-datafusion in apache/iceberg-rust but grant DataFusion PMC members committer access scoped to the crate via CODEOWNERS. ([message](https://lists.apache.org/thread/k3rqkf2k7zcxh9ggboblymynkzf3m61c))
- **[[person/liurenjie1024|Renjie Liu]]:** Moving the crate to the Apache DataFusion project is more reasonable than scoped access, and testing should not block the move. ([message](https://lists.apache.org/thread/5r2419sqw2wdf5pcq8rh4r4n56q2hj1l))
- **[[person/Xuanwo|Hao Ding]]:** Supports moving to the DataFusion PMC if it accepts the project, since DataFusion is the largest dependency and Comet the largest downstream user. ([message](https://lists.apache.org/thread/8c9ztyo3nq1wd6cjn9nvfbjf578flgko))
- **[[person/andygrove|Andy Grove]]:** Supports moving to the DataFusion PMC; the integration is very important for Comet. ([message](https://lists.apache.org/thread/hwzx0xcq64lc60hv7v9mo9yy0y7oxcdt))
- **Andrew Lamb:** Proposes creating a new Apache repository, a PR with the code, and formal votes on both the Iceberg and DataFusion dev lists. ([message](https://lists.apache.org/thread/1mzshyr7mk9r28dvxbjw71nwn3dplwt1))
<!-- kb:generated:end -->

## Notes
