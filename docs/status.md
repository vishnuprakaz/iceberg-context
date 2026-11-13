# Status and known limits

Last reviewed 2026-11-13. `kb status` gives the live numbers.

## What is synced

| Source | Coverage | Refreshed |
|---|---|---|
| Dev mailing list | Since November 2018 | Every 6 hours |
| Git history, Java and PyIceberg | Full | Every 6 hours |
| Spec and contribution docs | Current files, by section | Every 6 hours |
| ASF roster | PMC members and committers | Every 6 hours |
| Pull requests, apache/iceberg | Full, with reviewers and who merged | Every 6 hours |
| Issues, review comments, apache/iceberg-python | Filling in over successive runs | Every 6 hours |
| Working-group notes | 12 documents | Weekly |
| Community calendar | Next weeks | Weekly |
| Recording transcripts | 3 recordings | Weekly, when reachable |

AI summaries cover meetings and mailing-list threads from May 2026 on. Older material is stored and searchable, not summarized.

## Known limits

- **Recording transcripts.** YouTube answers requests from cloud servers with a bot check, so captions cannot be fetched from
  GitHub Actions or a cloud session. Most meetings are summarized from their notes alone. Captions fetched on a personal machine
  can be added with `icekb ingest transcript`.
- **Pull requests and reviews.** GitHub's token limits mean full history arrives over several days of scheduled runs. Until then
  `kb why` may show a pull request without its reviews.
- **AI summaries.** Meeting and thread pages are written by an AI model and checked mechanically: sources must exist and quotes
  must match the transcript. They can still be wrong; each page links its sources.
- **Thread splitting.** A few long mailing-list threads are stored as two parts when a mail client cut the reply chain.
- **Names.** People are matched to GitHub logins through `data/aliases.yaml`, which is partly unverified. Unmatched names appear
  as plain names.
- **Votes.** Binding status comes from the ASF roster, which records when each person joined the PMC but not when anyone left.
  Senders whose names are not mapped show as unverified. 44 of the 45 past result emails that state a binding count match the
  tally; in the other, the email states 7 binding +1 and eight PMC members voted +1.
- **Review queue.** Counts formal reviews only; comment replies are not collected for every pull request. Commit times and
  author association fill in after the GitHub collector re-reads open pull requests once.
- **Scope.** Java and PyIceberg in depth; Rust, Go and C++ through the mailing list and meeting notes only. Slack is not collected.

## Roadmap

- [x] Collectors, generated pages, AI summaries of six months, initiative pages, overview, opportunities, weekly briefing
- [x] Maintainer and PMC commands: votes, review queue, release, board report, decisions, loose ends
- [ ] A committer or PMC member tries the maintainer commands for a week
- [ ] Weekly sync running unattended for two consecutive weeks
- [ ] Transcripts for all recordings
- [ ] Website with a graph view

## Repository layout

| Path | Contents |
|---|---|
| `kb/` | Everything people and agents read: overview, opportunities, briefings, initiatives, groups, people, modules, releases, meeting and thread records, and the index the skill reads |
| `data/` | Cleaned source records (`raw/`), AI extractions (`extract/`), sync state, the source list and the name map |
| `pipeline/` | Collectors, processing, page generators and validators |
| `skills/`, `agents/` | The skill, the weekly sync runbook and the agents it uses (`.claude/` links to them so sessions with the repository attached load them) |
| `.claude-plugin/` | Plugin and marketplace manifests |
| `schema/`, `tests/` | Rules for records and pages; tests |
| `docs/` | This file, the pipeline reference, plans, research on each source, changelog |
| `notes/` | Human notes; the pipeline never writes here |
