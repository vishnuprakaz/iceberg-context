---
id: initiative/pyiceberg
type: initiative
title: PyIceberg roadmap and releases
status: released
updated: '2026-11-13'
sources:
- meeting/community/2026-05-13
- meeting/python/2026-05-26
- meeting/community/2026-06-03
- meeting/python/2026-06-30
- meeting/community/2026-07-15
- thread/t-444dbbca629c1693
- meeting/python/2026-07-28
- meeting/community/2026-08-05
- thread/t-aa8645f8aa979099
- thread/t-f9e1b8daeae100d8
- meeting/community/2026-08-26
- meeting/variant/2026-09-03
- meeting/read-restrictions/2026-09-15
- meeting/community/2026-09-16
- thread/t-2155678929401961
- meeting/python/2026-09-29
- meeting/community/2026-10-07
- meeting/python/2026-10-27
- meeting/community/2026-10-28
- thread/t-e423f0a28f74a2c0
links:
- rel: championed_by
  to: person/rambleraptor
  confidence: extracted
  source: thread/t-f9e1b8daeae100d8
- rel: championed_by
  to: person/kevinjqliu
  confidence: inferred
  source: meeting/python/2026-06-30
- rel: handled_by
  to: group/python
  confidence: extracted
  source: meeting/python/2026-10-27
- rel: touches
  to: module/iceberg-python/io
  confidence: inferred
  source: meeting/python/2026-07-28
- rel: touches
  to: module/iceberg-python/table
  confidence: inferred
  source: meeting/community/2026-08-26
---

# PyIceberg roadmap and releases

<!-- kb:generated:start -->
## What it is

PyIceberg is the Python implementation of Iceberg, developed in `apache/iceberg-python` and released on its own schedule ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)). This page follows its releases and the larger roadmap items discussed in the monthly PyIceberg sync: V3 support, a pluggable compute backend, and what a 1.0 release would mean ([PyIceberg sync 2026-09-29](../records/meetings/python/2026/2026-09-29.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U); [PyIceberg sync 2026-07-28](../records/meetings/python/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).

## Current state

- Latest release: 0.12.0, marked as done in the community sync notes of 2026-09-16 ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). Its listed highlights are view support, geometry and geography types, Python 3.14 support, the new File Format API and commit retry support ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)). The RC2 vote thread shows only +1 votes and contains no result message ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)).
- Next release: 0.13 planning was on the last two PyIceberg sync agendas, with "Early December?" as a possible date and an item to document a release timeline of about three months; no discussion is recorded ([PyIceberg sync 2026-09-29](../records/meetings/python/2026/2026-09-29.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U); [PyIceberg sync 2026-10-27](../records/meetings/python/2026/2026-10-27.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 1.0: what a 1.0 release looks like, with the public API boundary as the sub-point, was an agenda item; no outcome is recorded ([PyIceberg sync 2026-09-29](../records/meetings/python/2026/2026-09-29.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- Python versions: both repliers agreed with dropping Python 3.10, which reached end of life on 2026-10-01, and [iceberg-python #4170](https://github.com/apache/iceberg-python/pull/4170) was opened ([thread 2026-10-28](../records/threads/2026/10/discuss-drop-pyiceberg-python-3-10-support-e423f0.md), [dev list](https://lists.apache.org/thread/967dbjpjqt6kl9pnwv39vkvlvxv9rkcn)).
- Pluggable backend: the direction noted is to add the interface first, move all PyArrow code into `pyarrow.py`, and then look for an abstraction across Polars, DataFusion and PyArrow ([iceberg-python #3716](https://github.com/apache/iceberg-python/pull/3716)) ([PyIceberg sync 2026-07-28](../records/meetings/python/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)). It grew out of a proposal to use DataFusion to avoid out-of-memory problems in merge-on-read ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [iceberg-python #3554](https://github.com/apache/iceberg-python/issues/3554)).
- V3: deletion vector support was added ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and range reads for deletion vectors followed ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); the write side of the V3 implementation was an agenda item with no outcome recorded ([PyIceberg sync 2026-09-29](../records/meetings/python/2026/2026-09-29.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- Variant: blocked on the dependency chain from Arrow C++ to PyArrow to PyIceberg; the Arrow C++ pull request ([arrow #50252](https://github.com/apache/arrow/pull/50252)) was reported as stalled ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md), [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
- Other recent work listed in community sync notes: commit retry and concurrency validation for writes and async REST scan planning ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); REST retry and timeout configuration, the start of encryption support and a merge queue ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); encryption key management and more view support ([community sync 2026-10-28](../records/meetings/community/2026/2026-10-28.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- pyiceberg-core (the Rust-backed bindings released with Iceberg Rust): the 0.10.0 artifacts were yanked from PyPI because they were built from the wrong branch, with a no-change 0.10.1 planned ([thread 2026-07-27](../records/threads/2026/07/discussion-iceberg-rust-pyiceberg-core-0-10-1-444dbb.md), [dev list](https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l)); the community sync later listed Rust 0.10.1 as released ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). Missing third-party licence and notice files in the wheels were reported fixed on 2026-10-29 ([thread 2026-09-16](../records/threads/2026/09/discuss-pyiceberg-core-iceberg-rust-python-bindings-appears-not-to-inc-215567.md), [dev list](https://lists.apache.org/thread/k72c2y72w2j00xph2mn2bnsbvcbj43o4)).

## Timeline

- 2026-05-13: the community sync notes list Python 3.14 in CI and build, `register_view`, REST `load_view` and an initial pluggable file format writer API ([community sync 2026-05-13](../records/meetings/community/2026/2026-05-13.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-05-26: the PyIceberg sync listed equality delete reads ([iceberg-python #3285](https://github.com/apache/iceberg-python/pull/3285)), DeleteOrphanFiles and expire snapshots in the CLI ([iceberg-python #3361](https://github.com/apache/iceberg-python/pull/3361), [iceberg-python #3379](https://github.com/apache/iceberg-python/pull/3379)), and the question of the next release ([PyIceberg sync 2026-05-26](../records/meetings/python/2026/2026-05-26.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-06-03: the community sync listed PyIceberg 0.12.0 as an upcoming release and heard a proposal to add DataFusion for merge-on-read ([community sync 2026-06-03](../records/meetings/community/2026/2026-06-03.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-06-30: the PyIceberg sync named Alex as release manager for 0.12 and listed the pluggable backend architecture design document ([PyIceberg sync 2026-06-30](../records/meetings/python/2026/2026-06-30.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-07-15: the community sync notes list deletion vector support, an incremental append scan and a configurable manifest cache size ([community sync 2026-07-15](../records/meetings/community/2026/2026-07-15.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-27: pyiceberg-core 0.10.0 was reported as built from the wrong branch and yanked from PyPI ([thread 2026-07-27](../records/threads/2026/07/discussion-iceberg-rust-pyiceberg-core-0-10-1-444dbb.md), [dev list](https://lists.apache.org/thread/nxqw16p5wt8oorrtsbc28phkosp0g55l)).
- 2026-07-28: the PyIceberg sync discussed the pluggable backend architecture pull request and design ([PyIceberg sync 2026-07-28](../records/meetings/python/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-08-06: Alex Stephen proposed 0.12.0 RC1 ([thread 2026-08-06](../records/threads/2026/08/vote-pyiceberg-0-12-0rc1-aa8645.md), [dev list](https://lists.apache.org/thread/5qhn33k5kr0t9g3vvqqxc893bs11jxlc)).
- 2026-08-10: RC1 received a binding -1 over a correctness regression ([iceberg-python #3758](https://github.com/apache/iceberg-python/issues/3758)), with a request for a fix and a new candidate ([thread 2026-08-06](../records/threads/2026/08/vote-pyiceberg-0-12-0rc1-aa8645.md), [dev list](https://lists.apache.org/thread/5qhn33k5kr0t9g3vvqqxc893bs11jxlc)).
- 2026-08-24: 0.12.0 RC2 was proposed ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)).
- 2026-09-16: the community sync notes mark PyIceberg 0.12 as done ([community sync 2026-09-16](../records/meetings/community/2026/2026-09-16.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-09-29: the PyIceberg sync agenda covered 0.13 release planning, the V3 write side and what a 1.0 release looks like ([PyIceberg sync 2026-09-29](../records/meetings/python/2026/2026-09-29.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-10-07: the community sync notes link a release blog post for Python 0.12.0 ([community sync 2026-10-07](../records/meetings/community/2026/2026-10-07.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-27: the PyIceberg sync agenda gave "Early December?" for 0.13 and marked release automation with a check mark ([PyIceberg sync 2026-10-27](../records/meetings/python/2026/2026-10-27.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- 2026-10-28: dropping Python 3.10 was proposed and agreed by both repliers ([thread 2026-10-28](../records/threads/2026/10/discuss-drop-pyiceberg-python-3-10-support-e423f0.md), [dev list](https://lists.apache.org/thread/967dbjpjqt6kl9pnwv39vkvlvxv9rkcn)).

## Where help is needed

- Read restrictions: volunteers were asked for to implement read restrictions in PyIceberg, tracked in [iceberg-python #3967](https://github.com/apache/iceberg-python/issues/3967) ([read restrictions sync 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md), [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- Wheel licensing follow-ups from the 0.12.0 RC2 vote (LICENSE paths that differ in the wheels, undocumented bundled Cython runtime code) are tracked in [iceberg-python #3877](https://github.com/apache/iceberg-python/issues/3877) ([thread 2026-08-24](../records/threads/2026/08/vote-pyiceberg-0-12-0rc2-f9e1b8.md), [dev list](https://lists.apache.org/thread/3zq0vpkw5xkp48okq5ocpqft5mnyg03s)).
- The PyIceberg sync noted a Windows CI bug that needs an issue or pull request filed; no owner is recorded ([PyIceberg sync 2026-07-28](../records/meetings/python/2026/2026-07-28.md), [notes](https://docs.google.com/document/d/1oMKodaZJrOJjPfc8PDVAoTdl02eGQKHlhwuggiw7s9U)).
- Variant support is blocked on Arrow C++ work that was reported as stalled ([variant sync 2026-09-03](../records/meetings/variant/2026/2026-09-03.md), [notes](https://docs.google.com/document/d/1IuhLRxw1rcPD_f4jgHuGe3SwFgy7Y5wgEGvLzf6311s)).
<!-- kb:generated:end -->

## Notes
