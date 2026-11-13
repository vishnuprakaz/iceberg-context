# Iceberg Contribution Context

Private working memory for contributing to Apache Iceberg (Java) and PyIceberg.
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
- Never commit this context into the fork repos (forks of public repos are public).
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
_None yet._ Next: pick contribution areas (good-first-issues, spec gaps between Java and Python).

## Work log
| Date | Repo | What | Status / Link |
|------|------|------|---------------|
| 2026-11-13 | — | Created context repo | done |

## Open questions / ideas
- 

## Learnings
- 
