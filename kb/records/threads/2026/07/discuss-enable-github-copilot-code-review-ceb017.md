---
id: thread/t-ceb017adb8f59712
type: thread
title: Enable GitHub Copilot code review
date: '2026-07-16'
url: https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny
kind: discuss
status: consensus
messages: 13
sources:
- devlist:n2s6z7rt745cgftsb8j9yob0kc70cgny
refs:
- gh:apache/iceberg-cpp#833
links:
- rel: discussed
  to: initiative/ai-contributions
  confidence: extracted
  source: devlist:n2s6z7rt745cgftsb8j9yob0kc70cgny
- rel: discussed
  to: initiative/iceberg-cpp
  confidence: extracted
  source: devlist:n2s6z7rt745cgftsb8j9yob0kc70cgny
- rel: started_by
  to: person/wgtmac
  confidence: observed
updated: '2026-11-13'
---

# Enable GitHub Copilot code review

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Enable GitHub Copilot code review](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny) · **Started:** 2026-07-16 by [[person/wgtmac|Gang Wu]] · **Messages:** 13 (last 2026-07-20) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Gang (wgtmac) proposed enabling ASF-managed GitHub Copilot code review through the `.asf.yaml` `github.copilot_code_review` setting, starting with iceberg-cpp as a trial because reviewer bandwidth is limited there. Replies supported the trial. Several asked for custom Copilot instructions, for example comparing against the Java reference implementation, and for guidance on how contributors should respond to its feedback. Kevin Liu asked about quota and CI resource impact, then reported that the setting only creates a ruleset that requests reviews, that AI credits for automatic reviews are attributed to the PR author, that Actions minutes are attributed to the repository, and that he believes reviews will not run for authors without Copilot review access. wgtmac said he would merge the iceberg-cpp PR.

**Why it matters:** iceberg-cpp becomes the trial for automatic Copilot review, and other Iceberg repositories may adopt the same setup depending on how it goes.

## Outcome

No objections were raised. After the cost structure was clarified, wgtmac said he would merge the iceberg-cpp PR enabling Copilot review as a trial. ([message](https://lists.apache.org/thread/fhto0symb2lzlk1rqvzpg0krznzsk86g), `devlist:fhto0symb2lzlk1rqvzpg0krznzsk86g`)

## Positions

- **[[person/wgtmac|Gang Wu]]:** Enable automatic Copilot review on non-draft PRs in iceberg-cpp first as a trial, and let other repositories adopt it later if it works well. ([message](https://lists.apache.org/thread/n2s6z7rt745cgftsb8j9yob0kc70cgny))
- **[[person/rambleraptor|Alex Stephen]]:** The experiment is worth doing, and custom Copilot instructions should make it compare against the Java reference implementation. ([message](https://lists.apache.org/thread/xks0fsr5ps6hnfzybjrwlvd9c2q1n134))
- **[[person/steveloughran|Steve Loughran]]:** Copilot is acceptable as a general reviewer, best at low-level nitpicks; its output must be treated as hints and it needs custom instructions. ([message](https://lists.apache.org/thread/jklh12z5od9w6o8l3fq60z4c77f6mfxd))
- **Danny Jones:** Supports the trial and suggests defining how contributors should respond to Copilot feedback so comments can feed back into tuning the guidance. ([message](https://lists.apache.org/thread/jkb1f6gpgznympvbch5dx7mrhhr80r5m))
- **[[person/kevinjqliu|Kevin Liu]]:** It is helpful as a first review, but the quota and the impact on CI resources should be understood before enabling it. ([message](https://lists.apache.org/thread/sg4hpvn4l6477zrbqgbqgskdp19h5mfv))
- **Scott Haines:** Supports it while wanting the limits understood; classifying or tagging PRs would also be a good use. ([message](https://lists.apache.org/thread/61sy35gy7y6blqhxy23jhgk0yk6skshf))
- **[[person/kevinjqliu|Kevin Liu]]:** With the cost structure understood (credits attributed to the PR author, Actions minutes to the repository), the project can go ahead and try it. ([message](https://lists.apache.org/thread/3dlz3t0g1ffqh98kdwwb04ozrn448vd8))

References: [iceberg-cpp#833](https://github.com/apache/iceberg-cpp/issues/833)
<!-- kb:generated:end -->

## Notes
