# Source research: 2026-11-13

A survey of every source the knowledge base will ingest: what each one contains, how to access it, how to sync it incrementally, and the pitfalls. Four parallel research passes produced it. The plan that builds on it is [`docs/knowledge-base-plan.md`](../../knowledge-base-plan.md).

| File | Source |
|---|---|
| [dev-mailing-list.md](dev-mailing-list.md) | dev@iceberg.apache.org (PonyMail archive) |
| [meeting-notes.md](meeting-notes.md) | Working-group sync notes (Google Docs) plus the Iceberg Dev Events calendar |
| [meeting-notes-per-doc.md](meeting-notes-per-doc.md) | Per-doc structure, heading formats, and the latest meetings of each working group |
| [meeting-notes-doc-index.md](meeting-notes-doc-index.md) | Doc IDs and metadata |
| [meeting-notes-ingestion-pitfalls.md](meeting-notes-ingestion-pitfalls.md) | Parser pitfalls |
| [youtube.md](youtube.md) | @ApacheIceberg recordings and transcripts |
| [github-git-governance.md](github-git-governance.md) | GitHub PRs and issues, git history, ASF roster, contribution process |

The prototype collectors written during this research became the collectors in `pipeline/icekb/collectors/`. Raw dumps were not kept: the collectors regenerate them.
