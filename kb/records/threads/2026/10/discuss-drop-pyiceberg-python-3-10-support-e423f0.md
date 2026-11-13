---
id: thread/t-e423f0a28f74a2c0
type: thread
title: Dropping Python 3.10 support in PyIceberg
date: '2026-10-28'
url: https://lists.apache.org/thread/967dbjpjqt6kl9pnwv39vkvlvxv9rkcn
kind: discuss
status: consensus
messages: 4
sources:
- devlist:967dbjpjqt6kl9pnwv39vkvlvxv9rkcn
refs:
- gh:apache/iceberg-python#4170
links:
- rel: discussed
  to: initiative/pyiceberg
  confidence: extracted
  source: devlist:967dbjpjqt6kl9pnwv39vkvlvxv9rkcn
- rel: started_by
  to: person/oresttokovenko
  confidence: observed
updated: '2026-11-13'
---

# Dropping Python 3.10 support in PyIceberg

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Drop PyIceberg Python 3.10 support](https://lists.apache.org/thread/967dbjpjqt6kl9pnwv39vkvlvxv9rkcn) · **Started:** 2026-10-28 by [[person/oresttokovenko|Orest Tokovenko]] · **Messages:** 4 (last 2026-10-28) · **Outcome:** consensus

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Orest Tokovenko proposed dropping Python 3.10 from PyIceberg. Python 3.10 reached end of life on 2026-10-01, and pyarrow, a major dependency, no longer ships 3.10 wheels with its 26.x releases, so users on 3.10 get pyarrow 25.x while users on 3.11 and later get 26.x. He would set requires-python to >=3.11, raise the floor versions of some libraries (which would also allow moving the pyarrow floor from >=18.0.0 to >=26.0.0), and remove version gates in pyiceberg/io/pyarrow.py, all in one PR. Users on 3.10 can stay on the last release that supports it, as was done for 3.9 and 3.8. Fokko Driesprong agreed that end-of-life versions should not be supported and asked for a PR, which Tokovenko opened as iceberg-python #4170. Kevin Liu confirmed that the end-of-life date had just passed and thanked him.

**Why it matters:** Once the PR merges, PyIceberg users on Python 3.10 have to stay on the last release that supports it.

## Outcome

Both repliers agreed with dropping Python 3.10, and a PR (iceberg-python #4170) was opened; nobody objected. ([message](https://lists.apache.org/thread/h97sp0ohxskpx27pvwk667772jl7gwot), `devlist:h97sp0ohxskpx27pvwk667772jl7gwot`)

## Positions

- **[[person/oresttokovenko|Orest Tokovenko]]:** PyIceberg should drop Python 3.10, require Python 3.11 or later, raise dependency floors and remove the version gates that are no longer needed. ([message](https://lists.apache.org/thread/967dbjpjqt6kl9pnwv39vkvlvxv9rkcn))
- **[[person/Fokko|Fokko Driesprong]]:** End-of-life Python versions should not be supported, in line with how older versions were dropped before. ([message](https://lists.apache.org/thread/h97sp0ohxskpx27pvwk667772jl7gwot))

References: [iceberg-python#4170](https://github.com/apache/iceberg-python/issues/4170)
<!-- kb:generated:end -->

## Notes
