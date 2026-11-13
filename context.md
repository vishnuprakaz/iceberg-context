# Iceberg Contribution Context

Working memory for contributing to Apache Iceberg (Java) and PyIceberg.
This repo is **public by design** (may later grow into a shared Iceberg knowledge base).
**Read this first at the start of every session.** Keep it current: update it
whenever we learn something durable, finish a piece of work, or change plans.

## Session start checklist
1. Read this file, then skim `notes/` for the area being worked on.
2. Repos are fresh, shallow (50-commit) clones of the forks:
   - `iceberg` -> `vishnuprakaz/iceberg` (fork of `apache/iceberg`)
   - `iceberg-python` -> `vishnuprakaz/iceberg-python` (fork of `apache/iceberg-python`)
3. If needed: add upstream and unshallow
   - `git remote add upstream https://github.com/apache/<repo> && git fetch upstream main`
   - `git fetch --unshallow`
4. Read each repo's `AGENTS.md` and `CONTRIBUTING.md` before changing code.

## Ground rules
- This repo is public: never put secrets, credentials, tokens, or personal info here.
- Keep this context out of the fork repos; forks hold only upstream-bound code.
- Upstream PRs go fork -> `apache/*`; the user opens them (or approves).
- Follow upstream conventions (see AGENTS.md); small, focused PRs.

## Projects at a glance
### Apache Iceberg (Java)
- Gradle build; JDK 21 available in the environment.
- Default engine versions: Spark 4.1 (known 3.5/4.0/4.1), Flink 2.1 (known 1.20/2.0/2.1), Scala 2.12.
- Key modules: `api` (strongest stability; no breaks), `core` (engine-agnostic spec impl),
  `data`, `parquet`/`orc`/`arrow`, `spark`, `flink`, `open-api` (REST catalog spec),
  cloud catalogs (`aws`, `gcp`, `azure`), `format` (spec docs).
- High-sensitivity: `TableMetadata`, `SnapshotProducer`, `ManifestReader/Group`, parsers (no Jackson
  annotations; kebab-case JSON), REST spec, scan planning.

### PyIceberg
- Version on main: 0.11.0; Python >=3.10; tooling: `uv`, `make`, ruff.
- Key packages: `pyiceberg/catalog`, `table`, `io`, `expressions`, `avro`, `manifest.py`, `schema.py`.

## Current focus
**Iceberg Context is built** per [docs/build-plan.md](docs/build-plan.md); now it needs to run unattended and be used.

State on 2026-11-13:
- Synced: dev list since 2018, git history and spec, ASF roster, 12 notes documents, calendar, pull requests for apache/iceberg.
- Summarized by AI and checked: 87 meetings and 172 threads from the last six months; 35 initiative pages; overview; opportunities.
- Automation: GitHub Action `sync-daily.yml` every 6 hours; scheduled task "Iceberg Context weekly sync" on Mondays 07:47 IST.

Open items, most important first:
1. The weekly scheduled task has no Google Drive or Calendar connector attached (it could not be set from the session that
   created it). Attach both in the claude.ai routines page, or notes and calendar will not refresh.
2. Recording transcripts: YouTube bot-checks cloud addresses. Only 3 transcripts are stored. Fetch captions on a personal machine
   and add them with `icekb ingest transcript`, or decide on another route.
3. GitHub backfill: issues, comments and apache/iceberg-python are still filling in over the next scheduled runs.
4. Mailing-list threads are keyed by the first Message-ID in `References`, so a few long threads are split in two. Fix by
   resolving threads through hashed parent ids; this changes thread ids, so re-run thread extraction afterwards.
5. `data/aliases.yaml` is mostly unverified. Review `data/state/unresolved-people.json` and confirm logins.
6. Run the `open-source-launch` readiness gate before inviting others, and the trigger tests in `docs/skill-testing.md`.
7. Then: pick a contribution from `kb/opportunities.md`.

## Work log
| Date | Repo | What | Status / Link |
|------|------|------|---------------|
| 2026-11-13 | — | Created context repo | done |
| 2026-11-13 | — | Decided: keep repo public; for now it serves our own contribution work | decided |
| 2026-11-13 | — | Build plan approved; Phase 0 foundation built | done |
| 2026-11-13 | — | Phases 1–5 built: collectors, kb commands, summaries, initiative pages, weekly task | done, see open items |
| 2026-11-13 | — | Independent verification: 388 claims checked, 16 failed, all 16 fixed; skills aligned with Anthropic's skill guide | done |
| 2026-11-13 | — | Researched all sources (dev@, sync notes docs + calendar, YouTube, GitHub/git/ASF); wrote KB plan | proposal |

## Open questions / ideas
- Later: turn this repo into a public context system for anyone learning Iceberg.

## Learnings
- Idea lifecycle: issue/[DISCUSS] → design doc + working-group sync → spec PR → [VOTE] (3 binding PMC +1) → impl → release.
- ~14 working groups, each with a notes doc on the public "Iceberg Dev Events" calendar; most are recorded to YouTube.
- Squash merges hide who merged; reviewer activity (`reviewed-by:`) is the gatekeeping signal. Review capacity is
  concentrated (~15 people Java, ~5 PyIceberg) and PR inflow outpaces merges.
- Env access: GitHub search API works; REST/GraphQL on apache/* is blocked; dev@ via lists.apache.org API;
  YouTube auto-captions via yt-dlp (audio download blocked); Google Docs/Calendar via connectors.
