---
id: thread/t-48a3b37c45d4bf29
type: thread
title: Defining gc.enabled semantics across engines and clients
date: '2026-09-11'
url: https://lists.apache.org/thread/nxbxbs0x8h7xc73czgg3pryl42tr0zz5
kind: discuss
status: open
messages: 4
sources:
- devlist:nxbxbs0x8h7xc73czgg3pryl42tr0zz5
refs:
- gh:apache/iceberg#17791
links:
- rel: started_by
  to: person/xanderbailey
  confidence: observed
updated: '2026-11-13'
---

# Defining gc.enabled semantics across engines and clients

<!-- kb:generated:start -->
**Thread:** [[DISCUSS] Defining gc.enabled semantics across engines and clients](https://lists.apache.org/thread/nxbxbs0x8h7xc73czgg3pryl42tr0zz5) · **Started:** 2026-09-11 by [[person/xanderbailey|Xander]] · **Messages:** 4 (last 2026-09-15) · **Outcome:** open

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Alexander Bailey asked the list to define what `gc.enabled=false` means before his PR relaxing it for snapshot expiry proceeds. He showed that the property is not in the spec and that Java treats it in several ways: dropTableData skips data files but deletes metadata, RemoveSnapshots and the Spark actions fail outright, and the Hive helper maps it to a drop-purge flag. Rust and C++ copy Java's rejection of expiry, Go documents the same, and PyIceberg has no check. Russell Spitzer said the invariant is simply not to remove the table's data files and nothing needs to change. Dan (danielcweeks) said it is a convention that should not be codified, and that catalogs should enforce requirements. Bailey dropped the formal definition and asked whether a narrower change would be acceptable; no reply is in the thread.

**Why it matters:** Implementations differ on what gc.enabled=false blocks, and the thread leaves the property as an unspecified convention.

## Outcome

The proposal to formally define the property was set aside. The question whether the narrowed change in apache/iceberg#17791 can proceed had no reply when the thread stopped.

## Positions

- **Alexander Bailey:** The meaning of gc.enabled=false should be settled on the list, allowing snapshot expiry that deletes no files while rejecting expiry that would delete files. ([message](https://lists.apache.org/thread/nxbxbs0x8h7xc73czgg3pryl42tr0zz5))
- **[[person/RussellSpitzer|Russell Spitzer]]:** The property was added for tables whose data files are owned by another system; the invariant is not to remove the table's data files, enforcement may differ, and it could be written in a spec appendix. ([message](https://lists.apache.org/thread/3o56vo64rjd94mkf75nc4on7qh5hwwqx))
- **[[person/danielcweeks|Daniel C. Weeks]]:** gc.enabled is a convention clients should generally follow but it should not be codified; catalogs should enforce requirements when necessary. ([message](https://lists.apache.org/thread/rzsw267fw7lcn187d2bh0ww9bxw3jmch))
- **Alexander Bailey:** Leave the formal definition aside and narrow the PR to allow expiry under gc.enabled=false only with CleanupLevel.NONE, keeping the default and METADATA_ONLY modes blocked. ([message](https://lists.apache.org/thread/xf30qn3vs9r3qzvw5hclcyt91673nf8h))

References: [iceberg#17791](https://github.com/apache/iceberg/issues/17791)
<!-- kb:generated:end -->

## Notes
