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
**Building Iceberg Context** per [docs/build-plan.md](docs/build-plan.md) (approved 2026-11-13).
- Phase 0 (foundation) is done: community files, `icekb` package, schemas, validators, CI workflow, skill with `kb status|search|source`.
- Next: Phase 1, the daily collectors (devlist, github, git, spec, asf), normalize and link stages, the code map, the daily Action.
  Prototypes to port are in `pipeline/prototypes/`.
- Before public launch (Phase 5), run the `open-source-launch` skill's readiness gate.

## Work log
| Date | Repo | What | Status / Link |
|------|------|------|---------------|
| 2026-11-13 | — | Created context repo | done |
| 2026-11-13 | — | Decided: keep repo public; for now it serves our own contribution work | decided |
| 2026-11-13 | — | Build plan approved; Phase 0 foundation built | done |
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
