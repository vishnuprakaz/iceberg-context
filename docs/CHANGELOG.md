# Changelog

Notable changes to the tooling and structure of this repository. Knowledge-base content updates are recorded by the
`sync(raw)` and `sync(kb)` commits and the weekly briefings, not here.

## Unreleased

### Changed
- Repository laid out as an Agent Skill and Claude Code plugin: `skills/`, `agents/`, `.claude-plugin/`; knowledge-base content
  grouped under `kb/`. The `kb` script downloads the knowledge base when the skill is installed on its own, and gains `kb update`.

### Added
- Collectors for the dev mailing list, git history and spec, ASF roster, GitHub pull requests/issues/comments, YouTube captions,
  working-group notes documents and the community calendar; a sync workflow that runs them every six hours.
- AI extraction stage (`queue`, `apply`) with schema, citation and quote checks; agent definitions and the
  `iceberg-context-sync` skill for the weekly run.
- `kb` commands: `why`, `context`, `initiative`, `group`, `person`, `who-to-ask`, `whats-new`, `upcoming`, `opportunities`, `show`.
- First content: 16,047 mailing-list messages, 12,813 commits, 518 spec sections, 318 meeting-notes sections, 53 calendar events;
  generated pages for people, groups, modules, repositories and releases; summaries of 87 meetings and 172 threads.
- Repository foundation: licence and community files, `icekb` pipeline package, page and raw-record schemas,
  validators (schema, links, generated blocks, privacy), index builder, CI.
- `iceberg-context` skill with a first `kb` command set: `status`, `search`, `source`.
- Source registry (`data/sources.yaml`) and identity map (`people/aliases.yaml`) seeded from the 2026-11-13 research.
- Source research (`research/2026-11-13/`) and the build plan (`docs/build-plan.md`).
