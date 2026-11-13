---
id: thread/t-f9e1b8daeae100d8
type: thread
title: PyIceberg 0.12.0rc2 release vote
date: '2026-08-24'
url: https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s
kind: vote
status: open
messages: 8
sources:
- devlist:3zq0vpkw5xkp48okq5ocpqft5mnyg03s
refs:
- gh:apache/iceberg-python#3877
links:
- rel: discussed
  to: initiative/pyiceberg
  confidence: extracted
  source: devlist:3zq0vpkw5xkp48okq5ocpqft5mnyg03s
- rel: started_by
  to: person/rambleraptor
  confidence: observed
updated: '2026-11-13'
---

# PyIceberg 0.12.0rc2 release vote

<!-- kb:generated:start -->
**Thread:** [[VOTE] PyIceberg 0.12.0rc2](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s) · **Started:** 2026-08-24 by [[person/rambleraptor|Alex Stephen]] · **Messages:** 8 (last 2026-08-29) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

rambleraptor proposed release candidate 2 (commit 75396614, tag pyiceberg-0.12.0rc2) as PyIceberg 0.12.0, with a 72-hour vote. Listed highlights are view support, geometry and geography types, Python 3.14 support, the new File Format API and commit retry support. Voters verified signatures, checksums, licenses, source builds and unit tests on Windows, macOS and other environments. Jean-Baptiste Onofré voted +1 and noted minor issues in the wheel distributions: the LICENSE refers to vendor/fb303 and vendor/hive_metastore paths that differ in the wheels, the bundled Cython runtime code is not documented in LICENSE, and one source file has an unusual ASF header. kevinjqliu opened iceberg-python issue #3877 to track these. All votes were +1; the bundle contains no result message.

## Outcome

No result message is in the thread. The messages show +1 votes only: two marked binding (danielcweeks, kevinjqliu) and five marked non-binding; no -1 votes.

## Positions

- **Jean-Baptiste Onofré:** Votes +1 and asks that wheel LICENSE paths for the Thrift/Hive code, the undocumented bundled Cython runtime and an odd header in literals.py be fixed in the next release. ([message](https://lists.apache.org/thread/g6strrb3vmtg3yp8fqw6mrwt32gnvv8p))
- **[[person/Xuanwo|Hao Ding]]:** Considers the environment-sensitive integration failures and the distribution/module version distinction non-blocking and the source artifact ready for release. ([message](https://lists.apache.org/thread/6gt6r47mn4589d918hkpyy8d3603d2dt))
- **[[person/kevinjqliu|Kevin Liu]]:** Votes +1 and tracks the license issues from the thread in a GitHub issue. ([message](https://lists.apache.org/thread/mdm4f1ppsz7ocdp03osyw73lsrolzrzr))

References: [iceberg-python#3877](https://github.com/apache/iceberg-python/issues/3877)
<!-- kb:generated:end -->

## Notes
