---
id: thread/t-8fe86d8b03cd0963
type: thread
title: Reduce CI runner time by running JDK 21 only on main/nightly
date: '2026-06-11'
url: https://lists.apache.org/thread/f9xhm6mwyspt15j06v14bkjjb4hts4yz
kind: discuss
status: consensus
messages: 10
sources:
- devlist:f9xhm6mwyspt15j06v14bkjjb4hts4yz
refs:
- gh:apache/iceberg#16945
- gh:apache/iceberg#16566
links:
- rel: started_by
  to: person/wombatu-kun
  confidence: observed
updated: '2026-11-13'
---

# Reduce CI runner time by running JDK 21 only on main/nightly

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Reduce CI runner time by running JDK 21 only on main/nightly](https://lists.apache.org/thread/f9xhm6mwyspt15j06v14bkjjb4hts4yz) · **Started:** 2026-06-11 by [[person/wombatu-kun|Vova Kolmakov]] · **Messages:** 10 (last 2026-07-08) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Vova Kolmakov proposed running pull request CI on JDK 17 only, keeping the JDK 17 and 21 matrix for pushes to main, because the double matrix doubles runner minutes on the shared ASF Actions pool and pushes spark-ci past the 20-job parallel ceiling. Ajantha (ajantha-bhat) pointed to his existing PR doing this, choosing JDK 17 as the lower supported baseline and bytecode target. Kevin Liu later revived the proposal with a new PR that keeps both JDKs for main, release branches and tags. Russell Spitzer asked who would notice and fix JDK 21 failures; Kevin answered that they show on main and on the ci-jobs list. Danny Jones raised GitHub merge queues as an alternative. Kevin merged the PR on July 8.

**Why it matters:** Pull requests to apache/iceberg are now tested on JDK 17 only, so a JDK 21-only failure appears after merge to main.

## Outcome

Kevin Liu merged apache/iceberg#16945, which removes JDK 21 from the CI matrix for pull requests only; both JDK 17 and 21 still run after merge to main. ([message](https://lists.apache.org/thread/zrsvgow4d2qm2ox0k4odcx584g9npynh), `devlist:zrsvgow4d2qm2ox0k4odcx584g9npynh`)

## Positions

- **[[person/wombatu-kun|Vova Kolmakov]]:** Gate pull request runs on JDK 17 only and keep the full matrix on main, optionally with a nightly JDK 21 run or a small JDK 21 smoke subset on PRs. ([message](https://lists.apache.org/thread/f9xhm6mwyspt15j06v14bkjjb4hts4yz))
- **[[person/ajantha-bhat|Ajantha Bhat]]:** JDK 17 is the right PR baseline because it is the lowest supported version and the bytecode target; main and PRs labeled full-ci would still run both JDKs. ([message](https://lists.apache.org/thread/f98h92ly30fv4djsqdr7ynkk8w7g6jnr))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Fine with the change, but there must be a human mechanism so a broken JDK 21 build is noticed and fixed. ([message](https://lists.apache.org/thread/g7jphh0njgydwgcsb8jy00jxc9zcdczl))
- **[[person/kevinjqliu|Kevin Liu]]:** JDK 21 still runs on main and failures are visible in the GitHub UI and on the ci-jobs list; breakage should be rare, so the tradeoff is good. ([message](https://lists.apache.org/thread/33t9jhvs72k6nxjjooxd09pv14dmqobf))
- **Danny Jones:** A GitHub merge queue could run light tests on PRs and the full suite before merging, which avoids relying on people to react to failures on main. ([message](https://lists.apache.org/thread/4t6m94cl3qkc4rmkwhq0ocq2zzspkkvg))
- **[[person/RussellSpitzer|Russell Spitzer]]:** Turning off JDK 21 on PRs is cheaper than a merge queue, and a change that breaks only JDK 21 is unlikely. ([message](https://lists.apache.org/thread/2228kdg4mtx4jnl6g23gdn0t6pmpl6hj))

References: [iceberg#16945](https://github.com/apache/iceberg/issues/16945), [iceberg#16566](https://github.com/apache/iceberg/issues/16566)
<!-- kb:generated:end -->

## Notes
