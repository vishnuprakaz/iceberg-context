# Maintainer and PMC tasks

These commands help committers and PMC members with votes, reviews, releases and reporting. They read the same knowledge base
as the other commands. `kb` is `python3 SKILL_DIR/scripts/kb`.

## Rules

- Do not suggest, rank or compare people as candidates for committer or PMC membership. Do not guess what was discussed on
  private lists. Those discussions are private by ASF policy and are not in this knowledge base.
- Report health numbers in aggregate (per area or period). Do not turn them into lists of slow or inactive people.
- Give counts with their uncertainty, and pass on any mismatch with the result email.
- The dev@ thread is the record. Link to it for every vote, result and decision.

## `kb votes`

```bash
kb votes                         # votes opened in the last 30 days
kb votes --open                  # only votes with no result posted
kb votes --match default value   # one vote by words in its subject, any year, with every voter
kb votes --kind release --since 6m
```

For each vote: subject, opener, deadline (72 hours unless the opening email says otherwise), result, and the tally in three
groups:

| Group | Meaning |
|---|---|
| binding | The sender is a PMC member on the date of the vote, per the ASF roster. Votes of all Iceberg sub-projects (Rust, Go, C++, Python, Terraform) are binding for the same PMC |
| non-binding | The sender is a known contributor who was not on the PMC on that date, including committers. What they declared does not change this |
| unverified | The sender's name is not mapped to a GitHub login. Their declaration is shown. Every PMC member's ASF name is checked to be in the name map, so an unverified sender is usually not on the PMC |

How a vote is read: each person's latest message in the thread counts; quoted replies and the `[ ] +1 / [ ] -1` template are
ignored; the vote must start a line (`+1`, `-1`, `+0`, `-0`, `0`, also `My vote is +1`), or appear near the start of a short
reply. A result email that contains the release manager's own vote (`My vote is +1 (binding)`) counts it.

`check against the result email` compares the binding +1 count with the count the result email states:

- `match`: the numbers agree.
- `match if the N unverified voter(s) who declared binding are counted`: the result counted people the roster cannot confirm.
- `result email states X, counted Y`: they disagree. Name both numbers to the user and link the thread; either the email or
  the parse may be wrong. Run `kb votes --match WORDS` to see every voter.

Release votes need at least three binding +1 votes and more +1 than -1 votes (ASF release policy). A candidate with no result
that is followed by a later candidate for the same release is shown as superseded.

Votes are tallied in the pipeline from the raw messages every time the index is rebuilt (every six hours). They do not wait for
the weekly AI summaries.

## `kb review-queue`

```bash
kb review-queue                          # all open pull requests
kb review-queue --path flink/ --stale 7  # one area, list items waiting a week or more
kb review-queue --drafts
```

Open pull requests are grouped by whose turn it is:

| Group | Rule |
|---|---|
| First-time contributors with no review | GitHub marks the author as a first-time contributor, and nobody else has reviewed |
| No review yet | No formal review from anyone but the author |
| Updated since the last review | The latest commit is newer than the latest review |
| Approved by a committer, not merged | A committer or PMC member's latest review is an approval and nobody's latest review requests changes |
| Approved by others, needs a committer | Approved, but not by anyone on the ASF roster |
| Waiting on the author | The latest review is newer than the latest commit |

Days waiting are counted from the event that started the wait. The block at the end gives the median time to a first formal
review for pull requests opened in the last 90 days, overall and per top-level directory. Comments that are not formal reviews
are not counted, so it overstates the wait when reviewers reply in comments.

Author association, requested reviewers and commit times come from a newer version of the GitHub collector. Until it has re-read
every open pull request (once, on its next run), some items are shown as `reviewed (push time not collected yet)`.

## `kb release VERSION`

```bash
kb release 1.10.0
kb release 0.10.0 --repo python
```

Shows the release page (announcement and release manager), every release-candidate vote with its tally, the milestone's open
pull requests and the release discussions on dev@. For a release in progress, the milestone and the discussion threads are what
matters; for a past one, the candidates and results.

## `kb board-report`

```bash
kb board-report --quarter 2026Q4
kb board-report                  # the last three months
```

A draft in the layout of an ASF board report: Description, Project Status, Membership Data, Project Activity and Community
Health. It counts releases from announcements, PMC additions from the roster, committer and PMC announcements on dev@,
concluded votes, meetings with published notes, dev@ messages, threads and senders, pull requests opened and merged, and commits
and their authors per repository. Each count is compared with the previous period. Sections that need judgment ("Current
project status", "Issues for the board") are left for the PMC to write. Tell the user that the chair edits and submits the
report; this is only a starting point.

## `kb decisions TOPIC`

```bash
kb decisions equality deletes
kb decisions row lineage
```

Lists votes with a result, outcomes of summarized dev@ threads, and decisions recorded in meeting notes, newest first, with the
source of each. Meeting decisions are proposals until they are confirmed on dev@; say so when you quote one.

## `kb loose-ends`

```bash
kb loose-ends --since 30d
```

Action items from meeting notes with no owner, summarized dev@ discussions with no conclusion (excluding votes that have a
result), and new dev@ threads with no reply. Threads are matched by reply headers, so a reply posted as a new thread can make
a discussion look unanswered; check the source before saying nobody replied.

## Examples

**"Is the row-lineage vote passing?"**
`kb votes --match row lineage` shows the tally, the deadline and whether a result was posted. Answer: "5 binding +1, no -1;
no result posted yet; deadline was 2 November" with the thread link.

**"What is waiting on committers in Flink?"**
`kb review-queue --path flink/ --stale 7`. Give the counts per group and the oldest items, with links. Do not name reviewers who
are slow.

**"Draft our board report"**
`kb board-report --quarter 2026Q4`, then fill the judgment sections only with what the user tells you, and remind them to check
the numbers against `kb status` for how complete each source is.
