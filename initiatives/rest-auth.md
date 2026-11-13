---
id: initiative/rest-auth
type: initiative
title: REST catalog authentication and credentials
status: implementing
updated: '2026-11-13'
sources:
- thread/t-87bfb68a54b233c9
- meeting/catalog/2026-05-20
- meeting/community/2026-06-24
- meeting/catalog/2026-07-01
- thread/t-643f9a86cf02dd71
- thread/t-7cb3b0fb5a513b73
- meeting/community/2026-08-05
- meeting/community/2026-08-26
- meeting/read-restrictions/2026-09-15
- meeting/catalog/2026-09-23
- thread/t-98226ff1baae6ac7
- meeting/catalog/2026-10-14
- thread/t-4c863ceec72fa0da
- meeting/index/2026-10-26
- thread/t-019f2b7ebaa9b671
- meeting/catalog/2026-11-04
links:
- rel: championed_by
  to: person/adutra
  confidence: extracted
  source: thread/t-7cb3b0fb5a513b73
- rel: championed_by
  to: person/sungwy
  confidence: extracted
  source: thread/t-019f2b7ebaa9b671
- rel: handled_by
  to: group/catalog
  confidence: extracted
  source: meeting/catalog/2026-11-04
- rel: touches
  to: module/iceberg/open-api
  confidence: extracted
  source: thread/t-7cb3b0fb5a513b73
- rel: tracked_in
  to: gh:apache/iceberg#16822
  confidence: extracted
  source: thread/t-7cb3b0fb5a513b73
- rel: tracked_in
  to: gh:apache/iceberg#18480
  confidence: extracted
  source: thread/t-4c863ceec72fa0da
- rel: tracked_in
  to: gh:apache/iceberg#18254
  confidence: extracted
  source: thread/t-019f2b7ebaa9b671
- rel: tracked_in
  to: gh:apache/iceberg#15280
  confidence: extracted
  source: thread/t-87bfb68a54b233c9
---

# REST catalog authentication and credentials

<!-- kb:generated:start -->
## What it is

This covers how a client proves who it is to a REST catalog and how the catalog lets it reach table files in storage. A catalog can hand out short-lived storage credentials or sign storage requests on the client's behalf (remote signing), and the client says which mechanisms it accepts in the `X-Iceberg-Access-Delegation` header ([thread 2026-09-23](../records/threads/2026/09/discuss-rest-spec-expected-server-behavior-when-x-iceberg-access-deleg-98226f.md), [dev list](https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf); [thread 2026-07-20](../records/threads/2026/07/vote-formalize-remote-signing-configuration-in-the-rest-spec-7cb3b0.md), [dev list](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2)). Current work refines these mechanisms in the REST spec and reworks the client-side auth managers in the Java library ([catalog sync 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).

## Current state

- Decided: remote signing configuration is formalized in the REST spec as a `RemoteSigningConfig` object in `LoadTableResult` ([#16822](https://github.com/apache/iceberg/pull/16822)); the vote passed with 5 binding and 2 non-binding votes ([thread 2026-07-20](../records/threads/2026/07/vote-formalize-remote-signing-configuration-in-the-rest-spec-7cb3b0.md), [dev list](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2)), and the community sync notes list the spec change and a Java `RemoteSigningConfig` among later merges ([community sync 2026-08-05](../records/meetings/community/2026/2026-08-05.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg); [community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).
- Decided: `none` is added to the allowed values of `X-Iceberg-Access-Delegation` ([#18480](https://github.com/apache/iceberg/pull/18480)), meaning the client can work without any delegation mechanism; the vote passed with 7 +1 votes (3 binding), with the pull request pending merge ([thread 2026-10-25](../records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md), [dev list](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk)). Whether the spec should also say that servers may reject requests they cannot satisfy was left unresolved ([thread 2026-09-23](../records/threads/2026/09/discuss-rest-spec-expected-server-behavior-when-x-iceberg-access-deleg-98226f.md), [dev list](https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf)).
- Design settled, no vote yet: refreshing storage credentials for staged tables uses a storage refresh token tied to the existing storage credential (1:1), sent in headers, and only on the `loadCredentials` endpoint; the spec pull request is [#15280](https://github.com/apache/iceberg/pull/15280) and an S3 prototype is [#15899](https://github.com/apache/iceberg/pull/15899) ([thread 2026-02-10](../records/threads/2026/02/discuss-refreshing-storage-credentials-for-staged-table-creation-87bfb6.md), [dev list](https://lists.apache.org/thread/35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp); [catalog sync 2026-05-20](../records/meetings/catalog/2026/2026-05-20.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Open: a batch remote signing endpoint ([#18254](https://github.com/apache/iceberg/pull/18254)), motivated by the FILE type where each row may reference an external object; the thread is kept open until the FILE implementation settles, and where the authorization context goes in the request is unresolved ([thread 2026-10-26](../records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md), [dev list](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd)).
- Open: file-level access delegation during scan planning, with pre-signed URLs, scoped credential vending and bulk remote signing as the options discussed ([thread 2026-07-01](../records/threads/2026/07/discuss-proposal-file-level-access-delegation-in-the-iceberg-rest-cata-643f9a.md), [dev list](https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm)); pull requests for scan planning returning pre-signed URLs ([#17457](https://github.com/apache/iceberg/pull/17457)) and for pre-signing through the sign endpoint ([#18080](https://github.com/apache/iceberg/pull/18080)) were listed as calls for review ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Open: encryption with the REST catalog. The REST client does not support V3 encryption today; a hybrid mode with client-side KMS credentials and, longer term, server-vended KMS credentials ([#17155](https://github.com/apache/iceberg/pull/17155)) were discussed and no default was agreed ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- In review: Auth Manager v2 ([#15703](https://github.com/apache/iceberg/pull/15703), [#15704](https://github.com/apache/iceberg/pull/15704)) ([catalog sync 2026-05-20](../records/meetings/catalog/2026/2026-05-20.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)), and a BearerAuthManager and a downscoped OAuth2 v2 manager ([#18754](https://github.com/apache/iceberg/pull/18754), [#18756](https://github.com/apache/iceberg/pull/18756)) ([catalog sync 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)); the notes record no discussion of either.
- Open: whether the Iceberg SDK should support the OAuth token exchange flow, raised for trusted engines; no outcome is recorded ([catalog sync 2026-09-23](../records/meetings/catalog/2026/2026-09-23.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw); [read restrictions sync 2026-09-15](../records/meetings/read-restrictions/2026/2026-09-15.md), [notes](https://docs.google.com/document/d/1iGNydKY7XT1N5Nz056vDPM0P8v0MFymGqNtOlUGUp-c)).
- Other implementations: PyIceberg added REST `loadCredentials` ([community sync 2026-06-24](../records/meetings/community/2026/2026-06-24.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)), and Iceberg Rust added an AuthManager/AuthSession with OAuth2 migrated to it ([community sync 2026-08-26](../records/meetings/community/2026/2026-08-26.md), [notes](https://docs.google.com/document/d/1YuGhUdukLP5gGiqCbk0A5_Wifqe2CZWgOd3TbhY3UQg)).

## Timeline

- 2026-02-10: a proposal to refresh storage credentials for staged table creation was posted ([thread 2026-02-10](../records/threads/2026/02/discuss-refreshing-storage-credentials-for-staged-table-creation-87bfb6.md), [dev list](https://lists.apache.org/thread/35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp)).
- 2026-05-20: the catalog sync asked for review of the S3 prototype for storage credential refresh ([#15899](https://github.com/apache/iceberg/pull/15899)) and carried over signer property passthrough ([#15850](https://github.com/apache/iceberg/pull/15850)) and Auth Manager v2 ([catalog sync 2026-05-20](../records/meetings/catalog/2026/2026-05-20.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-05-21: the author of the credential refresh proposal reported that the last two spec issues were resolved, with an updated pull request to follow ([thread 2026-02-10](../records/threads/2026/02/discuss-refreshing-storage-credentials-for-staged-table-creation-87bfb6.md), [dev list](https://lists.apache.org/thread/35lj7vhtqtwl5nv9rzpln4mw4fbh7gdp)).
- 2026-07-01: file-level access delegation was proposed on the dev list and listed at the catalog sync ([thread 2026-07-01](../records/threads/2026/07/discuss-proposal-file-level-access-delegation-in-the-iceberg-rest-cata-643f9a.md), [dev list](https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm); [catalog sync 2026-07-01](../records/meetings/catalog/2026/2026-07-01.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-07-20: Alexandre Dutra called the vote on formalizing remote signing configuration ([thread 2026-07-20](../records/threads/2026/07/vote-formalize-remote-signing-configuration-in-the-rest-spec-7cb3b0.md), [dev list](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2)).
- 2026-07-30: the remote signing configuration vote was closed as passed with 5 binding and 2 non-binding votes ([thread 2026-07-20](../records/threads/2026/07/vote-formalize-remote-signing-configuration-in-the-rest-spec-7cb3b0.md), [dev list](https://lists.apache.org/thread/n4hyqr3k2gnzbxvs3l1o4cz3ggdfwkx2)).
- 2026-09-23: a dev list thread asked what a server should do when the requested access delegation cannot be satisfied; it converged on adding `none` to the header values ([thread 2026-09-23](../records/threads/2026/09/discuss-rest-spec-expected-server-behavior-when-x-iceberg-access-deleg-98226f.md), [dev list](https://lists.apache.org/thread/6zspb6cpb6j2po5lm57mq1sgcp2hppkf)).
- 2026-09-23: the catalog sync listed questions on pre-signing URLs (request and response parameters, and how a server advertises support); no outcome is recorded ([catalog sync 2026-09-23](../records/meetings/catalog/2026/2026-09-23.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-10-14: the catalog sync discussed V3 encryption with the REST catalog and server-vended KMS credentials, without agreeing a default ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- 2026-10-25: a vote was called on adding `none` to `X-Iceberg-Access-Delegation` ([thread 2026-10-25](../records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md), [dev list](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk)).
- 2026-10-26: Sung Yun proposed a batch remote signing endpoint ([thread 2026-10-26](../records/threads/2026/10/discuss-rest-spec-batch-remote-signing-endpoint-019f2b.md), [dev list](https://lists.apache.org/thread/8pnj238xly2dmzb55tfb9bjny7sp34nd)).
- 2026-10-28: the `none` vote passed with 7 +1 votes (3 binding) ([thread 2026-10-25](../records/threads/2026/10/vote-rest-spec-add-none-to-x-iceberg-access-delegation-header-values-4c863c.md), [dev list](https://lists.apache.org/thread/hc2764vozz7ygx5fjj64104hotrof0lk)).
- 2026-11-04: the catalog sync listed the BearerAuthManager and the downscoped OAuth2 v2 manager ([catalog sync 2026-11-04](../records/meetings/catalog/2026/2026-11-04.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).

## Where help is needed

- Reviews were requested for scan planning returning pre-signed URLs ([#17457](https://github.com/apache/iceberg/pull/17457)) and pre-signing a URL through the sign endpoint ([#18080](https://github.com/apache/iceberg/pull/18080)) ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- Review was requested for the server-vended KMS credentials spec change ([#17155](https://github.com/apache/iceberg/pull/17155)), and a participant was asked to check the catalog-vended KMS credential model with security people ([catalog sync 2026-10-14](../records/meetings/catalog/2026/2026-10-14.md), [notes](https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw)).
- The file-level access delegation author asked for feedback on a proof of concept of bulk remote signing with caching ([thread 2026-07-01](../records/threads/2026/07/discuss-proposal-file-level-access-delegation-in-the-iceberg-rest-cata-643f9a.md), [dev list](https://lists.apache.org/thread/odof6m2npvktwd51cz8qnrxjv95ws4wm)).
- The index REST spec does not yet include routes for refreshing vended credentials or remote signing for index files ([index sync 2026-10-26](../records/meetings/index/2026/2026-10-26.md), [notes](https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0)).
<!-- kb:generated:end -->

## Notes
