# How Apache Iceberg makes decisions

A short orientation. Sources: the project's contribution guide (`site/docs/contribute.md` in apache/iceberg), `.asf.yaml`, the
dev mailing list, and the research in `research/2026-11-13/`.

## Roles
- **PMC (Project Management Committee):** votes on releases and spec changes; their votes are *binding*. Chair: Ryan Blue.
- **Committers:** can merge pull requests.
- **Contributors:** anyone who sends a pull request, reviews, or takes part in discussion.

## How an idea becomes part of Iceberg
1. A GitHub issue (label `proposal` for larger ideas) or a `[DISCUSS]` thread on the dev mailing list.
2. A design document, usually a Google Doc, and often a recurring working-group sync with public notes and a recording.
3. A pull request. Changes to the table spec (`format/`) or the REST catalog spec (`open-api/rest-catalog*`) need a `[VOTE]`
   thread on the dev list: at least 3 binding +1 votes and more +1 than -1. The outcome is posted as `[RESULT]`.
4. Implementation, usually in Java first, then PyIceberg, Rust, Go and C++.
5. A release, run by a volunteer release manager and approved by a vote on a release candidate.

## Pull requests
- Titles start with the module: `Core: …`, `Spark: …`, `Flink: …`, `API: …`, `Docs: …`. CI checks this in apache/iceberg.
- A committer other than the author merges after at least one approval. Pull requests are squashed.
- New public API waits at least 24 hours before merge. Breaking changes to `api/` are almost never accepted.
- Pull requests with no activity for 30 days are marked stale and closed 7 days later.
- The project has a policy on disclosing AI assistance; read the contribution guide before sending AI-assisted work.

## Where discussion happens
- **Dev mailing list:** the official record. Decisions must be made here.
- **Working-group syncs:** where designs are worked out. Each has a notes document; most are recorded. The schedule is on the
  public "Iceberg Dev Events" calendar.
- **GitHub:** review and implementation detail.
- **Slack:** quick questions. Not a place where decisions are made, and not collected here.
