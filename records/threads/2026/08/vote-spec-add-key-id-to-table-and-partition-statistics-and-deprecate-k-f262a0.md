---
id: thread/t-f262a08fa26f3d8c
type: thread
title: 'Vote: add key-id to table and partition statistics and deprecate key-metadata'
date: '2026-08-10'
url: https://lists.apache.org/thread/rx0tcnqkq0nzj1phwo64ng79pp51hzf9
kind: vote
status: withdrawn
messages: 11
sources:
- devlist:rx0tcnqkq0nzj1phwo64ng79pp51hzf9
refs:
- gh:apache/iceberg#17533
links:
- rel: started_by
  to: person/gaborkaszab
  confidence: observed
updated: '2026-11-13'
---

# Vote: add key-id to table and partition statistics and deprecate key-metadata

<!-- kb:generated:start -->
**Thread:** [[VOTE] [SPEC] Add key-id to table and partition statistics and deprecate key-metadata](https://lists.apache.org/thread/rx0tcnqkq0nzj1phwo64ng79pp51hzf9) · **Started:** 2026-08-10 by [[person/gaborkaszab|Gabor Kaszab]] · **Messages:** 11 (last 2026-08-25) · **Outcome:** withdrawn

> Summary written by an AI model from the messages. Check the thread before relying on a detail.

## Summary

Gábor Kaszab called a vote on a spec change (PR #17533) to deprecate the raw key-metadata field in table statistics, which he considered insecure because table metadata is not encrypted, and to add a key-id field to table and partition statistics that points to an encrypted key in the encryption-keys list. Several +1 votes followed. Ryan Blue voted -0: the PR's new v4 column disallowed key-metadata, which would force v3 statistics keys to be relocated on upgrade, and the keys table was meant for a few reused keys rather than one per file; he suggested leaving existing keys in place and adding an optional key-id. Gábor argued key-metadata is a security bug that should go. Gidon Gershinsky said other implementations may use key-metadata safely, so keeping it and adding key-id is practical. Gábor accepted this, updated the PR and said he would open another vote thread.

**Why it matters:** The statistics-file key change did not pass in this form, and a revised proposal that keeps key-metadata is expected in a later vote.

## Outcome

No result was announced. Votes cast were five +1 (one marked binding, one non-binding, three unmarked) and one -0 from Ryan Blue. Gábor updated the PR to keep key-metadata and add key-id as an alternative, and said he would open a new vote thread. ([message](https://lists.apache.org/thread/jkdn54z62d7lzgfm2mw8qqxmrkkwt0w9), `devlist:jkdn54z62d7lzgfm2mw8qqxmrkkwt0w9`)

## Positions

- **Gábor Kaszab:** Raw key-metadata in unencrypted table metadata is not secure; deprecate it and add key-id pointing into encryption-keys, as for manifest lists. ([message](https://lists.apache.org/thread/rx0tcnqkq0nzj1phwo64ng79pp51hzf9))
- **[[person/rdblue|Ryan Blue]]:** Voted -0: do not tie key relocation to the v4 upgrade or require per-file keys to move; keep existing keys where they are and add an optional key-id. ([message](https://lists.apache.org/thread/s2649vlgw3xxr2bjptszvv5cgslrgm0p))
- **Gábor Kaszab:** The Java implementation does not write key-metadata for stats, and it should be treated as a security bug to remove rather than an existing feature to keep. ([message](https://lists.apache.org/thread/tqkdm8kvswyo2gzsgbx0qbvwyc3rmsmc))
- **Gidon Gershinsky:** Other implementations may use key-metadata without exposing a cleartext key, so leaving it in place and adding key-id is fine. ([message](https://lists.apache.org/thread/xd4pbvqxdgtd90vmnk0stbd3xgdcbmwq))

References: [iceberg#17533](https://github.com/apache/iceberg/issues/17533)
<!-- kb:generated:end -->

## Notes
