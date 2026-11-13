# Iceberg Context: end-to-end build plan

> **Layout note (2026-11-13):** this document predates a tidy-up. Knowledge-base pages now live under `kb/`, the name map is `data/aliases.yaml`, and research is under `docs/research/`. See [pipeline.md](pipeline.md) and the repository README for the current layout.

## 1. Context

**The problem.** What you need to know to contribute to Apache Iceberg is scattered across seven places: the dev@ mailing list, GitHub PRs and reviews, git history, about 12 working-group notes docs, a public calendar, 383 YouTube recordings and the ASF roster. None of them links to the others. A coding agent sees only the code. It doesn't see why the code is that way, who decides, or what is being worked on.

**What we're building.** One public repository, `vishnuprakaz/iceberg-context`, with three parts:

1. A **sync pipeline** that pulls from every source on a schedule and links the records together.
2. A **knowledge base** stored as Markdown pages in git. Pages carry typed links to each other, so together they form a graph.
3. A **Claude Code skill** with a small `kb` command-line tool. Any agent or contributor can ask what is happening, why code is the way it is, who to talk to and where to contribute. Every answer cites its source.

**Where we are.** Research on all sources is done and committed in `research/2026-11-13/`. The design is in `docs/knowledge-base-plan.md` (v3). Prototype collectors are in `pipeline/prototypes/` and seed data in `data/seed/`. This plan turns that into a working, professionally structured repository.

**Defaults this plan assumes** (approving the plan approves them; say so to change any):

| Decision | Default |
|---|---|
| Repo name | `iceberg-context`, described as unofficial and not affiliated with the ASF |
| Layout | Single repo: knowledge base, cleaned raw data, pipeline and skill together |
| Daily collection | GitHub Actions enabled on the repo |
| Weekly AI sync | Scheduled Claude session, Monday about 07:47 IST |
| Backfill | Collect raw data for full history; AI-summarize the last 6 months |
| Scope | Java and PyIceberg in depth; Rust, Go and C++ at initiative and release level |
| Licence | Apache-2.0 for code; knowledge pages CC BY 4.0 |
| Commits | No AI attribution lines (per the repo's `CLAUDE.md`) |

## 2. Repository layout

```
iceberg-context/
├── README.md                  what it is, quick start, freshness, "unofficial" notice
├── LICENSE, NOTICE            Apache-2.0; trademark and source attribution
├── CONTRIBUTING.md            how to add notes, fix pages, add a source
├── CODE_OF_CONDUCT.md, SECURITY.md
├── PRIVACY.md                 what we record about people, and how to request a correction or removal
├── CLAUDE.md                  session instructions: run `kb status`, use the skill
├── pyproject.toml             package `icekb` (pipeline); ruff + pytest config
├── .github/
│   ├── workflows/sync-daily.yml     deterministic collectors
│   ├── workflows/ci.yml             lint, tests, schema and link checks, privacy lint
│   ├── ISSUE_TEMPLATE/              correction, new source, privacy request
│   └── PULL_REQUEST_TEMPLATE.md
├── .claude/
│   ├── skills/iceberg-context/      the skill everyone uses (SKILL.md, scripts/kb, references/)
│   ├── skills/iceberg-context-sync/ the maintainer skill: the weekly runbook
│   └── agents/                      sync agent definitions (section 6)
├── docs/                      architecture.md, pipeline.md, schema.md, runbook.md, adding-a-source.md
├── schema/                    JSON Schemas: raw record, each page type, each AI output
├── pipeline/icekb/            collectors/ normalize/ link/ process/ integrate/ validate/ cli.py
├── tests/                     unit tests with small fixtures per source
├── data/
│   ├── raw/<source>/YYYY/MM.jsonl   cleaned captures, append-only
│   ├── links/edges.jsonl            deterministic links between records
│   ├── state/<source>.json          sync cursors, one file per source
│   └── sources.yaml                 registry: docs, playlists, repos, calendars
├── index/                     nodes.jsonl, edges.jsonl, generated on every sync (what `kb` reads)
├── state-of-iceberg.md        always-current overview
├── opportunities.md           ranked places to contribute
├── briefings/weekly/YYYY-Www.md
├── people/  groups/  initiatives/  modules/  releases/      entity pages
├── records/meetings/<group>/YYYY/  records/threads/YYYY/MM/  record pages
├── code-map/                  file → PRs → discussions, per repo
├── maps/                      ownership.md, reviewers.md
├── notes/                     human notes; the pipeline never writes here
└── research/                  the 2026-11-13 source research
```

`context.md` (our own work log) stays as it is. The existing `pipeline/prototypes/` scripts are folded into `pipeline/icekb/` and the folder is removed.

## 3. Data model

**Raw record** (`schema/raw-record.json`), one JSON line per item:
`id, source, type, date, url, people[], title, body, refs[], hash, ai_generated?`

Stable IDs:
- `devlist:<message-id>`
- `gh:apache/iceberg#18585`
- `commit:<repo>@<sha>`
- `meet:<group>:<date>`
- `yt:<video-id>`
- `doc:<doc-id>`
- `spec:<file>#<section>`

**Page types** (Markdown with YAML frontmatter, each validated against a schema):
`person, group, initiative, module, repo, release, meeting, thread`.

**Links** carry a relation, dates, a source record ID and a confidence label:
- `observed`: straight from the data (roster, git, PR, vote counts).
- `extracted`: pulled by the AI from cited text.
- `inferred`: an AI judgment, such as a speaker in an unlabeled transcript.

**Page rules:**
- The pipeline writes only inside `<!-- kb:generated:start/end -->` blocks.
- Timelines are append-only.
- A `## Notes` section on every page belongs to humans.
- Pages link to each other with `[[wiki-links]]`, so the folder opens as a graph in Obsidian.

**Identity.** `people/aliases.yaml` maps each GitHub login to its ASF id and every name variant seen on dev@, in git and in notes docs. Names that don't resolve go to `data/state/unresolved-people.json` for review. The pipeline never guesses.

## 4. Pipeline stages

```
collect → normalize → link → process (AI) → integrate → validate → commit
```

One entry point: `python -m icekb run --daily | --weekly | --source <name> | --backfill`. Each stage reads the previous stage's files, so any stage can be rerun alone.

### 4.1 Collectors

| Collector | Method | Detects new data by | Runs in | Reuses |
|---|---|---|---|---|
| `devlist` | Monthly mbox + `stats.lua` permalinks from lists.apache.org | Message-ID; refetch current and previous month, freeze older | Action, daily | `prototypes/devlist/parse.py`, `analyze.py`, `enrich.py` |
| `github` | GraphQL/REST with the Action token: PRs, issues, reviews, review comments, merged-by, files, milestones, labels | `updated >= cursor` per repo | Action, daily | `prototypes/github/gs.py` (rate limiting and cache pattern), `prstats.py`, `opps.py` |
| `git` | Treeless clones of iceberg and iceberg-python; `git log --name-only` | Last commit SHA | Action, daily | `prototypes/github/gitown.py`, `namemap.py` |
| `spec` | `format/*.md`, `open-api/rest-catalog-open-api.yaml`, contribution docs from the clone, split by section | File hash | Action, daily | new |
| `asf` | whimsy roster JSON; quarterly board reports | Diff | Action, weekly | `data/seed/governance_roster.csv` as the first snapshot |
| `siblings` | Counts and releases for rust, go, cpp, verification, terraform | Monthly | Action, monthly | `opps.py` |
| `syncdocs` | Google Docs connector `read_doc` JSON, tab-aware, per `data/sources.yaml` | `modifiedTime`, then per-meeting section hash | Claude session, weekly | parsing rules in `research/2026-11-13/meeting-notes-*.md` |
| `designdocs` | Follow Google Doc links found in threads, issues and notes; read the public ones | New `doc:` refs | Claude session, weekly | new |
| `calendar` | Calendar connector, Iceberg Dev Events, next 14 days | Event IDs; a new series creates a group stub | Claude session, weekly | new |
| `youtube` | `yt-dlp --flat-playlist` + RSS, then `en-orig` captions | Processed video-ID list; retry failures next run | Claude session, weekly | `prototypes/youtube/clean_json3.py`, `to_markdown.py`; `data/seed/youtube_inventory_*.tsv` |

### 4.2 Normalize
- Strip email addresses and "via dev" sender suffixes.
- Remove quoted reply text and fix encoding.
- Split each notes doc into one record per meeting with a tolerant date parser.
- Turn captions into timestamped paragraphs.
- Resolve people through `aliases.yaml`.
- Tag AI-written sources such as Gemini notes.

### 4.3 Link (no AI)
- **Code map:** the `(#NNNN)` in each commit title gives the PR; the commit's file list gives the files.
- **Thread ↔ PR:** PR numbers in subjects and bodies.
- **Notes ↔ transcript:** same group and date.
- **Meeting ↔ PRs and docs:** links in the notes; a bare `#NNNNN` is resolved by the section it sits in.
- **Vote lifecycle:** DISCUSS → VOTE → RESULT grouped by subject and PR number.
- **Releases:** RC votes → announcement → release manager.

Output: `data/links/edges.jsonl`, all labeled `observed`.

### 4.4 Process (AI, only new or changed records)
`icekb queue` lists records with no extraction or a changed hash. Each extraction must match a schema in `schema/extract-*.json`, and every claim must cite a record ID or it is rejected.

- **Meeting** (notes + transcript):
  - summary, decisions, action items with owners, open questions
  - initiatives and PRs discussed
  - participants: `extracted` when taken from the notes, `inferred` when guessed from the transcript
  - key quotes with video timestamps
- **Thread:** type, positions, outcome, vote tally, linked initiative.
- **Notable PR** (spec change, large, long-running): initiative and why it matters.

### 4.5 Integrate
- Update entity pages inside their generated blocks and append timeline entries.
- Recompute `state-of-iceberg.md`, `opportunities.md`, `maps/` and the week's briefing.
- Regenerate `index/nodes.jsonl` and `index/edges.jsonl`.

Opportunity ranking signals:
- an initiative that is moving but lacks an implementation in Python, Rust or Go
- issues with many 👍 and no PR
- areas with an active reviewer and a review backlog
- good-first-issues
- action items with no owner
- recent bugs

### 4.6 Validate
- Frontmatter matches its schema.
- Every link target exists.
- Every extracted fact has a source.
- Generated-block markers are intact.
- **Privacy lint:** no email addresses, phone numbers or personal details.

Any failure blocks the commit.

## 5. Daily workflow: `.github/workflows/sync-daily.yml`

- **Trigger:** cron daily at about 02:10 UTC, plus manual `workflow_dispatch`.
- **Permissions:** `contents: write`; default `GITHUB_TOKEN` only, no other secrets.
- **Steps:**
  1. Check out the repo.
  2. Set up uv.
  3. Run `icekb run --daily`.
  4. Run the validators.
  5. Commit `sync(raw): YYYY-MM-DD` if anything changed.
  6. `git pull --rebase` and push.
- **Concurrency:** one run at a time (`concurrency: sync`).
- **Conflict safety:** raw files are append-only by month and state is one file per source, so the daily Action and the weekly session never touch the same lines.
- **Failure:** a failing collector is recorded in `data/state/<source>.json` and the run continues. `kb status` shows it.

## 6. Weekly workflow: the sync agents

A scheduled task starts a fresh Claude session each Monday about 07:47 IST in the "Iceberg" environment, with the Google Docs, Drive and Calendar connectors. Its prompt is one line: follow the `iceberg-context-sync` skill. That skill is the runbook. It runs these agents, each defined in `.claude/agents/`:

| # | Agent | Job | Output |
|---|---|---|---|
| 1 | `kb-collector` | Run the connector collectors (syncdocs, designdocs, calendar, youtube), normalize, run the link stage | New raw records and edges; a queue of items to process |
| 2 | `kb-meeting-extractor` (several in parallel) | One meeting each: read notes + transcript, write the meeting record | `records/meetings/...` + extraction JSON |
| 3 | `kb-thread-extractor` (in parallel) | Batches of dev@ threads and notable PRs | `records/threads/...` + extraction JSON |
| 4 | `kb-integrator` | Update people, groups, initiatives, modules, releases; recompute maps, state page, opportunities | Updated entity and synthesis pages, `index/` |
| 5 | `kb-verifier` | Independent check: sample claims against `kb source`, run validators and privacy lint, flag anything unsupported | Pass, or a list of fixes sent back to step 4 |
| 6 | `kb-briefer` | Write the weekly briefing: what changed, decisions, open votes, upcoming syncs, new opportunities | `briefings/weekly/YYYY-Www.md` |

Then the main session commits `sync(kb): YYYY-Www`, pushes, and ends with a short summary. If something failed, the summary lists which sources are stale.

- **Extractor rules:** extractors are read-only on the knowledge base and write only their own record, which keeps parallel runs from colliding. The integrator is the only writer of entity pages.
- **Verifier independence:** the verifier gets the pages and the sources, not the extractors' reasoning.
- **Typical week:** 6–8 meetings, about 100 emails and the PR changes. About one session-hour.
- **On demand:** saying "sync now" in any session runs the same skill.

## 7. The skill: `.claude/skills/iceberg-context/`

```
SKILL.md              when to use it, the workflow, citation rules
scripts/kb            Python, standard library only
references/           process.md (how decisions get made), glossary.md, schema.md
```

`kb` reads `index/*.jsonl` plus the Markdown pages, and builds a local SQLite full-text index on first use (cached outside the repo, rebuilt when the repo's commit changes). No install step, no server.

| Command | Answers |
|---|---|
| `kb status` | How fresh each source is, what failed, what's new since the last sync |
| `kb search <query>` | Full-text search over records and pages |
| `kb why <path> [--symbol X]` | PRs that shaped the file, their review debates, linked threads, votes and meetings. With a local checkout, `--symbol` uses `git log -L` |
| `kb context <paths>` | Before editing: related initiatives and spec sections, open PRs on the same files, active reviewers, recent decisions |
| `kb initiative <name>` | Status, champions, timeline across all sources |
| `kb person <login>` | Public roles, areas, reviews, championed work |
| `kb who-to-ask <path or topic>` | Owners, active reviewers, the right sync to attend |
| `kb whats-new --since <date>` | Change digest |
| `kb upcoming` | Next syncs, agendas, what to read first |
| `kb opportunities [--area] [--level]` | Ranked places to contribute |
| `kb source <id>` | The exact quote and permalink behind a claim |

**Workflow SKILL.md teaches:**
1. Run `kb status` at session start.
2. Run `kb context` and `kb why` before changing Iceberg code.
3. Cite sources in every answer, and say when something is inferred.
4. Check for open PRs on the same files before starting work.
5. Follow the upstream `AGENTS.md` conventions.

**Installing:** attach the repo to a session (or add it to the environment's repository list) and the skill loads automatically. Outside cloud sessions, clone the repo and copy the skill folder to `~/.claude/skills/`. The README documents both.

## 8. Build phases

| Phase | Work | Done when |
|---|---|---|
| **0. Foundation** | Repo scaffolding (section 2 files), `pyproject.toml`, schemas, `aliases.yaml` seeded from `data/seed/`, `sources.yaml`, validators, CI workflow, minimal `kb` (status, search, source) | CI is green; `kb status` runs on an empty knowledge base |
| **1. Deterministic pipeline** | Port prototypes into `icekb` collectors (devlist, github, git, spec, asf); normalize and link stages; code map; daily Action; raw backfill of full history | The daily Action commits new data on its own; `kb why <file>` returns PRs with links |
| **2. Seed knowledge base** | Pages for governance, about 60 people, 14 groups, about 20 initiatives, modules and releases, built from the research; first `state-of-iceberg.md`, `opportunities.md`, maps | `kb initiative v4-amt`, `kb who-to-ask spark` and `kb person <login>` give sourced answers |
| **3. Connector collectors + AI processing** | syncdocs, designdocs, calendar, youtube collectors; extraction schemas and prompts; agent definitions; the sync skill; run it once by hand for the current week | One full weekly run finishes end to end and passes the verifier |
| **4. Backfill 6 months** | About 80 meetings and the DISCUSS/VOTE/RESULT threads since May 2026, in batches | Each initiative page has a timeline from discussion to vote to PRs |
| **5. Automate + polish** | Create the weekly scheduled task; full `kb` command set; SKILL.md polish; README quick start; onboarding path for newcomers; add friends | Two consecutive unattended weekly runs succeed |
| **6. Later** | Website on GitHub Pages (dashboard, graph, timelines); dev@ history back to 2018 summarized on demand; optional MCP wrapper | Not part of this build |

Each phase leaves something usable. Phases 0–2 are the first working session or two.

## 9. Risks and how the plan handles them

| Risk | Handling |
|---|---|
| YouTube bot checks on cloud IPs | Retry next run; never mark a failed video done; `kb status` shows the gap; notes docs still cover the meeting |
| Scheduled sessions may not be allowed to push to `main` | Fall back to pushing a `sync/weekly` branch that an Action fast-forwards into `main` after CI passes |
| Scheduled session lacks the Google connectors | The task is created with those connectors named; if one is missing, the run does the rest and reports it |
| AI summary states something the source doesn't say | Mandatory citations, schema rejection, the independent verifier, confidence labels |
| Wrong identity match | Curated alias file; unresolved queue; no guessing. The seed `name_to_login.json` has known bad entries and is used only as a starting point for manual review |
| Republishing other people's words | Store cleaned text with attribution and links back; `NOTICE` and `PRIVACY.md` state the sources and offer a removal path; people pages hold public project activity only |
| Repo growth | Text only, about 100 MB at full history; sessions clone shallow |
| Upstream format changes (doc headings, API) | Tolerant parsers, fixture tests per source, collector failures isolated from each other |

## 10. Verification

- **Unit tests** (`pytest`): each collector and parser against small fixtures: one mbox month, one notes-doc JSON, one caption file, a short git log.
- **CI on every push:** ruff, pytest, schema checks, link checks, privacy lint.
- **Pipeline check:** run `python -m icekb run --daily` twice in a row; the second run must produce no changes.
- **Daily Action check:** trigger it by hand with `workflow_dispatch`; confirm a `sync(raw)` commit appears and CI passes on it.
- **Skill check, in a fresh session with only the repo attached:**
  - `kb status` shows per-source freshness.
  - `kb why core/src/main/java/org/apache/iceberg/SnapshotProducer.java` returns PRs with working links.
  - `kb initiative v4-amt` shows the October vote and PR #16025.
  - `kb source <id>` prints a quote that matches the linked page.
- **Weekly run check:** run the sync skill by hand once. Compare one meeting record against its notes doc and video by spot-checking three claims and their timestamps.
- **Acceptance for the whole system:** a new session, asked "what is the status of materialized views and who should I talk to about helping?", answers from the knowledge base with sources and no web browsing.
