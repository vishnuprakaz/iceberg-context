---
id: thread/t-5dd317254d01abc3
type: thread
title: AI-generated review comments
date: '2026-08-15'
url: https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb
kind: discuss
status: no-conclusion
messages: 4
sources:
- devlist:y93010hlq2m59jjw9lsjbrs38xw8nkdb
refs:
- gh:apache/iceberg#17670
- gh:apache/iceberg#17671
links:
- rel: discussed
  to: initiative/ai-contributions
  confidence: extracted
  source: devlist:y93010hlq2m59jjw9lsjbrs38xw8nkdb
- rel: started_by
  to: person/manuzhang
  confidence: observed
updated: '2026-11-13'
---

# AI-generated review comments

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] AI Review comments](https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb) · **Started:** 2026-08-15 by [[person/manuzhang|Manu Zhang]] · **Messages:** 4 (last 2026-08-17) · **Outcome:** no-conclusion

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

manuzhang raised concerns about AI-generated code review comments on pull requests: they are increasingly long, take time to dissect, can conflict when several AI reviewers work from different context, and may be posted without a human reading them. He prefers reading the AI findings, rephrasing the valid points himself and posting them manually, and asked whether that should be the practice. zhjwpku agreed that comments must be understood before posting, kept AI wording when it is better, and noted this is hard to enforce. vaquar khan agreed and also reported that AI tools are being added as Co-authored-by with several bot identities; he opened issue #17670 and PR #17671 to update AGENTS.md with guidance on review comments, crediting AI, review agent safety and equal review gates. rdblue strongly agreed that contributors must read, understand and improve LLM output before posting. The thread ends without a decision on the PR.

**Why it matters:** Contributors who use AI for reviews or code are expected to vet and shorten its output themselves before posting it to the project.

## Outcome

Respondents agreed that AI output must be read and understood before posting, but the thread ends without a decision on the proposed AGENTS.md changes in PR #17671.

## Positions

- **[[person/manuzhang|Manu Zhang]]:** Reviewers should read AI findings, rephrase the valid points in their own words and post them manually rather than post raw AI comments. ([message](https://lists.apache.org/thread/y93010hlq2m59jjw9lsjbrs38xw8nkdb))
- **[[person/zhjwpku|Junwang Zhao]]:** AI wording can be reused when it is better; the key is not to publish review comments one does not understand, though this is hard to enforce. ([message](https://lists.apache.org/thread/99d1kmr57x6cwmo60c4sx4n9tloxk7hv))
- **vaquar khan:** AGENTS.md should state that humans own each review comment, that AI tools are credited with Generated-by rather than Co-authored-by, and that AI-authored PRs pass the same gates. ([message](https://lists.apache.org/thread/z4wktnznxdph64p87v9m7h0f64glpbj0))
- **[[person/rdblue|Ryan Blue]]:** Contributors must read, understand and improve LLM output and should rarely post it directly; the contributor, not the committers, does the first review of what an LLM produces. ([message](https://lists.apache.org/thread/0o2c3om2roshmn5fpkhb8fs4wbj71dh2))

References: [iceberg#17670](https://github.com/apache/iceberg/issues/17670), [iceberg#17671](https://github.com/apache/iceberg/issues/17671)
<!-- kb:generated:end -->

## Notes
