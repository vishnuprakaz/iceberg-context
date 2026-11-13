---
id: initiative/v4-encryption
type: initiative
title: Table encryption (V3 and V4)
status: design
updated: '2026-11-13'
sources:
- meeting/community/2026-05-13
- meeting/catalog/2026-05-20
- thread/t-8afa728d41cbbd2f
- meeting/community/2026-07-15
- meeting/v4-metadata/2026-07-27
- thread/t-f262a08fa26f3d8c
- meeting/spark/2026-08-18
- meeting/community/2026-08-26
- thread/t-007945f7f6f7274a
- meeting/community/2026-09-16
- thread/t-c3195bd81b8adb3b
- meeting/catalog/2026-10-14
- meeting/community/2026-10-28
- meeting/v4-metadata/2026-11-02
links:
- rel: championed_by
  to: person/gaborkaszab
  confidence: extracted
  source: thread/t-f262a08fa26f3d8c
- rel: championed_by
  to: person/xanderbailey
  confidence: extracted
  source: thread/t-007945f7f6f7274a
- rel: handled_by
  to: group/v4-metadata
  confidence: extracted
  source: meeting/v4-metadata/2026-11-02
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-10-14
- rel: touches
  to: module/iceberg/format
  confidence: extracted
  source: thread/t-007945f7f6f7274a
- rel: touches
  to: module/iceberg/core
  confidence: extracted
  source: thread/t-c3195bd81b8adb3b
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: meeting/catalog/2026-10-14
- rel: tracked_in
  to: gh:apache/iceberg#16527
  confidence: extracted
  source: thread/t-007945f7f6f7274a
- rel: tracked_in
  to: gh:apache/iceberg#17533
  confidence: extracted
  source: thread/t-f262a08fa26f3d8c
- rel: tracked_in
  to: gh:apache/iceberg#17155
  confidence: extracted
  source: meeting/catalog/2026-10-14
---

# Table encryption (V3 and V4)

<!-- kb:generated:start -->
## What it is

Iceberg tables can be encrypted with data keys that are wrapped by keys held in a key management service (KMS). The current work has three parts: writing down the key metadata formats that today exist only in the Java implementation so other languages can interoperate ([thread, 2026-05-20](../records/threads/2026/05/discuss-specifying-the-encryption-key-metadata-formats-for-cross-imple-8afa72.md); [dev list](https://lists.apache.org/thread/4zm5jhwp42z10pfz2sths7q59r9dlf8l)), deciding where keys for statistics files and V4 root manifests live in table metadata ([thread, 2026-09-23](../records/threads/2026/09/discuss-reusable-encryption-keys-c3195b.md); [dev list](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s)), and letting REST catalog clients read encrypted tables ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).

## Current state

- Encryption spec document ([#16527](https://github.com/apache/iceberg/pull/16527)): it documents the standard key metadata format and the two-tier key hierarchy as they exist today. A vote was called but no votes were cast; reviewers asked for it to be less coupled to the table spec and to reflect the statistics-file work, and the proposer agreed to revise the pull request before a new vote ([thread, 2026-09-02](../records/threads/2026/09/vote-spec-document-standard-encryption-key-metadata-007945.md); [dev list](https://lists.apache.org/thread/hpdmzppsl87l0olkpzm3q47occ9cfydo)).
- Statistics file keys ([#17533](https://github.com/apache/iceberg/pull/17533)): a vote to add key-id and deprecate key-metadata did not reach a result. After a -0 and discussion, the pull request was changed to keep key-metadata and add key-id as an alternative, with a new vote thread announced ([thread, 2026-08-10](../records/threads/2026/08/vote-spec-add-key-id-to-table-and-partition-statistics-and-deprecate-k-f262a0.md); [dev list](https://lists.apache.org/thread/rx0tcnqkq0nzj1phwo64ng79pp51hzf9)).
- A later thread questioned reusing one data key for several files. Its three participants ended up agreeing on a fresh key per file, stored with the file reference, for new file types such as V4 root manifests and statistics files; it closes with a request for wider feedback on [#17533](https://github.com/apache/iceberg/pull/17533) and no recorded decision ([thread, 2026-09-23](../records/threads/2026/09/discuss-reusable-encryption-keys-c3195b.md); [dev list](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s)).
- V4 needs a change because key metadata must move now that there is no snapshot list at the top of the metadata ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)). A spec pull request for encryption key metadata is ready for more reviews ([V4 Metadata (AMT / Single File Commits), 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md); [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- REST catalog: the REST client does not support V3 encryption today. A pull request proposes a hybrid mode (storage credentials from the catalog, KMS credentials on the client) and longer-term spec work has the server vend short-lived KMS credentials ([#17155](https://github.com/apache/iceberg/pull/17155)). No default was agreed ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Open questions listed at the community sync: making the KEK expiry configurable (it is hard coded to 730 days) and whether Parquet modular encryption will be used with v4 Parquet manifests ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Other implementations: Iceberg Rust added an EncryptionManager with envelope encryption and a KeyManagementClient trait ([Community Sync, 2026-05-13](../records/meetings/community/2026/2026-05-13.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)) and continued with key management and encrypted IO ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); PyIceberg started encryption support ([Community Sync, 2026-09-16](../records/meetings/community/2026/2026-09-16.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)); Python key management, Go and C++ encryption work are listed in the latest highlights ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Java: client-configured encryption in RESTCatalog had two approvals, and key_metadata with encrypted write support for StatisticsFile had no reviews ([Spark Community Sync, 2026-08-18](../records/meetings/spark/2026/2026-08-18.md); [notes](https://docs.google.com/document/d/19nno1RoPznbbxKOZZddZNHHafa7XULjbN6RPExdr2n4)).

## Timeline

- 2026-05-13: Iceberg Rust's EncryptionManager, KeyManagementClient trait and StandardKeyMetadata are listed as added ([Community Sync, 2026-05-13](../records/meetings/community/2026/2026-05-13.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-05-20: Thread proposes specifying the key metadata formats for cross-implementation interop; [#16527](https://github.com/apache/iceberg/pull/16527) is opened ([thread, 2026-05-20](../records/threads/2026/05/discuss-specifying-the-encryption-key-metadata-formats-for-cross-imple-8afa72.md); [dev list](https://lists.apache.org/thread/4zm5jhwp42z10pfz2sths7q59r9dlf8l)). The catalog sync lists encryption support in the REST catalog (credentials for the KMS) as a new topic ([Catalog Community Sync, 2026-05-20](../records/meetings/catalog/2026/2026-05-20.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-07-15: The encryption-specific spec ([#16527](https://github.com/apache/iceberg/pull/16527)) is raised at the community sync; no outcome recorded ([Community Sync, 2026-07-15](../records/meetings/community/2026/2026-07-15.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-07-27: Encryption keys for deletion vectors is an agenda item at the V4 metadata sync; no outcome recorded ([V4 Metadata (AMT / Single File Commits), 2026-07-27](../records/meetings/v4-metadata/2026/2026-07-27.md); [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- 2026-08-10: Vote on key-id for table and partition statistics ([#17533](https://github.com/apache/iceberg/pull/17533)) starts; it ends without a result and the pull request is revised ([thread, 2026-08-10](../records/threads/2026/08/vote-spec-add-key-id-to-table-and-partition-statistics-and-deprecate-k-f262a0.md); [dev list](https://lists.apache.org/thread/rx0tcnqkq0nzj1phwo64ng79pp51hzf9)).
- 2026-08-26: Community sync lists key-id versus key-metadata, KEK expiry and Parquet modular encryption for v4 manifests; no outcome recorded ([Community Sync, 2026-08-26](../records/meetings/community/2026/2026-08-26.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-09-02: Vote on the encryption spec document ([#16527](https://github.com/apache/iceberg/pull/16527)) is called; no votes are cast and the pull request is to be revised ([thread, 2026-09-02](../records/threads/2026/09/vote-spec-document-standard-encryption-key-metadata-007945.md); [dev list](https://lists.apache.org/thread/hpdmzppsl87l0olkpzm3q47occ9cfydo)).
- 2026-09-23: Thread on reusable encryption keys starts ([thread, 2026-09-23](../records/threads/2026/09/discuss-reusable-encryption-keys-c3195b.md); [dev list](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s)).
- 2026-10-14: Catalog sync discusses V3 encryption with the REST catalog, hybrid mode and server-vended KMS credentials; no default agreed ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-10-28: V4 progress report names the V4 encryption change as in progress ([Community Sync, 2026-10-28](../records/meetings/community/2026/2026-10-28.md); [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- 2026-11-02: The spec pull request for encryption key metadata is reported ready for more reviews ([V4 Metadata (AMT / Single File Commits), 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md); [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).

## Where help is needed

- Review the spec pull request for encryption key metadata (action item from the V4 metadata sync) ([V4 Metadata (AMT / Single File Commits), 2026-11-02](../records/meetings/v4-metadata/2026/2026-11-02.md); [notes](https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw)).
- Wider feedback was requested on [#17533](https://github.com/apache/iceberg/pull/17533), on where keys for statistics files and V4 root manifests are stored ([thread, 2026-09-23](../records/threads/2026/09/discuss-reusable-encryption-keys-c3195b.md); [dev list](https://lists.apache.org/thread/38rkthkr1fg0s86493fjq755cnl3y90s)).
- A call for review is out on [#17155](https://github.com/apache/iceberg/pull/17155) (server-vended KMS credentials), and the group left open whether hybrid mode should sit behind a client flag and whether a catalog vending credentials for a separate KMS is acceptable from a security standpoint ([Catalog Community Sync, 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md); [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
<!-- kb:generated:end -->

## Notes
