---
id: initiative/file-type
type: initiative
title: File type for unstructured data
status: accepted
updated: '2026-11-13'
sources:
- meeting/community/2026-07-15
- thread/t-b5daefa7bb409f3d
- meeting/community/2026-08-26
- thread/t-4cd20220f5ceef8a
- thread/t-07dfa8ee9a2cbc37
- thread/t-019f2b7ebaa9b671
- meeting/community/2026-10-28
- thread/t-709611fe90159e57
- meeting/file-vector-type/2026-11-05
links:
- rel: championed_by
  to: person/talatuyarer
  confidence: extracted
  source: thread/t-4cd20220f5ceef8a
- rel: championed_by
  to: person/sungwy
  confidence: extracted
  source: thread/t-019f2b7ebaa9b671
- rel: championed_by
  to: person/rambleraptor
  confidence: extracted
  source: thread/t-709611fe90159e57
- rel: handled_by
  to: group/file-vector-type
  confidence: extracted
  source: meeting/file-vector-type/2026-11-05
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-4cd20220f5ceef8a
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-019f2b7ebaa9b671
- rel: tracked_in
  to: gh:apache/iceberg#17918
  confidence: extracted
  source: thread/t-4cd20220f5ceef8a
---

# File type for unstructured data

<!-- kb:generated:start -->
## What it is

A `file` data type for V4 tables. A file value is a range of bytes that is either stored inline or is a reference to an external file, following the Parquet FILE logical type ([thread, 2026-10-12](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-4cd202.md); [dev list](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49)). It gives tables a first-class way to reference or embed unstructured files ([thread, 2026-10-12](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-4cd202.md); [dev list](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49)).

## Current state

- The spec change ([#17918](https://github.com/apache/iceberg/pull/17918)) defines six fixed sub-fields (uri, offset, size, content_type, checksum, inline), resolves relative URIs against the table location, and gives mappings for Parquet, Avro and ORC. File values have no equality, ordering or hashing, cannot be identifier fields or partition or sort sources, and are valid only in v4 ([thread, 2026-10-12](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-4cd202.md); [dev list](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49)).
- A vote on [#17918](https://github.com/apache/iceberg/pull/17918) was started on behalf of the FILE type working group. The recorded replies are +1 votes plus one non-binding +0; the records contain no result message ([thread, 2026-10-12](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-4cd202.md); [dev list](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49)) ([thread, 2026-10-14](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-07dfa8.md); [dev list](https://lists.apache.org/thread/ldkpj659fjrf6nrc8vbg0b3fknxwdg38)).
- "File Type in the V4 spec ([#17918](https://github.com/apache/iceberg/pull/17918))" is listed among merged V4 work at the community sync ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- The +0 asked for a field that tells maintenance operations whether the files at the URI are safe to remove, so several tables can point at one media bucket; nobody replied to it in the recorded messages ([thread, 2026-10-14](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-07dfa8.md); [dev list](https://lists.apache.org/thread/ldkpj659fjrf6nrc8vbg0b3fknxwdg38)).
- A batch remote signing endpoint for the REST catalog ([#18254](https://github.com/apache/iceberg/pull/18254)) was proposed because, with the file type, signatures scale with rows instead of files. The thread is open: reviewers want to wait for the FILE implementation, since authorizing references to shared storage may change the request shape ([thread, 2026-10-26](../records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md); [dev list](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd)).
- A proposal to ship generative AI and embedding functions in the Spark and Flink connectors as part of the FILE and VECTOR work drew two replies that questioned or opposed it; no decision ([thread, 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md); [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).
- The file and vector type sync asked whether it should be consolidated with the weekly v4 sync; the notes record no answer ([File and Vector Type Sync, 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).

## Timeline

- 2026-07-15: The FileRef proposal is listed at the community sync with a design document ([Community Sync, 2026-07-15](../records/meetings/community/2026/2026-07-15.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-26: A second, type-only proposal is shared after the Parquet FILE logical type merged; its author agrees to consolidate into the existing proposal ([thread, 2026-07-26](../records/threads/2026/07/discuss-add-a-file-data-type-to-iceberg-v4-b5daef.md); [dev list](https://lists.apache.org/thread/33h4ppbrkmm83no3x6mfxqkv4zdw6ynv)).
- 2026-08-26: The FILE data type and FileRef proposal are listed again at the community sync ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-10-12: Vote to add the file type to the v4 spec ([#17918](https://github.com/apache/iceberg/pull/17918)) starts ([thread, 2026-10-12](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-4cd202.md); [dev list](https://lists.apache.org/thread/7ctclwomk8yqcclzj82z0htlqk2xjf49)).
- 2026-10-14: Later replies to the vote include one non-binding +0 about ownership of referenced files ([thread, 2026-10-14](../records/threads/2026/10/vote-add-the-file-type-to-the-iceberg-v4-spec-07dfa8.md); [dev list](https://lists.apache.org/thread/ldkpj659fjrf6nrc8vbg0b3fknxwdg38)).
- 2026-10-26: Discussion of a batch remote signing endpoint starts ([thread, 2026-10-26](../records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md); [dev list](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd)).
- 2026-10-28: The file type spec change ([#17918](https://github.com/apache/iceberg/pull/17918)) is listed among merged V4 work ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-02: Thread on AI functions for FILE and VECTOR types ([thread, 2026-11-02](../records/threads/2026/11/discuss-ai-functions-for-file-vector-types-709611.md); [dev list](https://lists.apache.org/thread/zv614sbcz0doshl4xpddpcj3oolfgo3b)).
- 2026-11-05: The sync asks whether to consolidate with the weekly v4 sync ([File and Vector Type Sync, 2026-11-05](../records/meetings/file-vector-type/2026/2026-11-05.md); [notes](https://docs.google.com/document/d/1zA8PskNDFKXXJpzWQr25CFoX_aIZHBNHbkxk0t3PteE)).

## Where help is needed

- The batch signing thread is kept open for input; where the authorization context lives in the request (per element or per request) is unresolved ([thread, 2026-10-26](../records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md); [dev list](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd)).
<!-- kb:generated:end -->

## Notes
