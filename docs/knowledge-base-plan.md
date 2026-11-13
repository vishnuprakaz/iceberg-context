# Iceberg community knowledge base: design and pipeline plan

> **Layout note (2026-11-13):** this document predates a tidy-up. Knowledge-base pages now live under `kb/`, the name map is `data/aliases.yaml`, and research is under `docs/research/`. See [pipeline.md](pipeline.md) and the repository README for the current layout.

Status: **proposal, 2026-11-13 (v3: skill-first delivery, single repo; v2 added the code map).** It builds on the source research in [`research/2026-11-13/`](research/2026-11-13/).

## 1. Goal

A continuously updated, queryable picture of the Apache Iceberg project and community:

- **What is happening now:** proposals, votes, sync decisions, releases, hot PRs.
- **How it got here:** the history of design debates and code evolution.
- **Who does what:** roles, area ownership, who reviews and approves where, who champions which initiative, who works with whom.
- **Where we can contribute:** gaps, stalled work, unreviewed areas, demand with no implementation, and who to talk to.

It must be usable by us and our friends from any Claude session or a browser, editable on the go, and safe to keep public.

**Above all, it must plug into coding agents.** Any agent working on the Iceberg codebase, whether Claude Code, Cursor, Codex or others, should be able to:

- understand *why* the code is the way it is
- know what the community is doing and has decided
- back every claim with a source

The system has three parts:

1. A **sync engine** that runs on a schedule.
2. A **context store** in git, whose source of truth is compiled into a searchable index.
3. An **access layer**: a Claude Code **skill** with a small `kb` CLI. See §7. An MCP server is an optional later addition that would wrap the same CLI.

## 2. How the community actually works (what the research showed)

The structure of the knowledge base follows from this:

1. **Ideas follow a lifecycle that spans every source.** A GitHub issue or [DISCUSS] thread on dev@ leads to a Google design doc and a recurring **working-group sync** (notes doc plus YouTube recording). That leads to a spec PR and a [VOTE] on dev@, needing 3 binding PMC +1s for spec changes, then a [RESULT]. Implementation PRs follow in Java, then Python, Rust, Go and C++, and finally a release.
   - No single source tells the whole story. **The unit of knowledge is the initiative, not the document.**
2. **Work is organized into about 14 working groups**, each with a cadence and a notes doc on the *Iceberg Dev Events* calendar:
   - V4 Metadata/AMT, Index, File and Vector Type, MV, Catalog, Variant, Spark, Column Updates, Python, Rust, Read Restrictions, Constraints, and the main Community Sync.
   - The Community Sync is the hub. Its notes link about 1,000 PRs and cross-reference every other group.
3. **Authority is formal (the ASF roster) but power is in review.**
   - The roster: a 26-member PMC with Ryan Blue as chair, plus 14 other committers.
   - Because squash merges hide who merged, **who reviews is the observable gatekeeping signal.** It is highly concentrated: about 15 people do most Java reviews, and about 5 do PyIceberg.
4. **Demand is outgrowing capacity.**
   - PRs opened rose from about 200 to about 350 a month while merges held at about 170–200.
   - 277 PRs have sat unreviewed for 14 or more days.
   - The contribution strategy follows: pick areas where a reviewer is active and an initiative needs hands, and show up in that working group's sync.
5. **Release managers rotate**, and every repo has its own cadence:
   - Java: a minor every 4–5 months.
   - PyIceberg: every 6–7 months.
   - Rust: every 2–4 months.
   - Go and C++: about every 4 months.

## 3. Storage decision: a git-native knowledge graph, plus a generated index

**Recommendation: don't use a graph database as the source of truth.** Use typed Markdown pages in git, whose YAML frontmatter holds typed edges. Compile them into a SQLite index on demand for graph and full-text queries.

| Option | Verdict |
|---|---|
| Graph DB (Neo4j/Kuzu) as source of truth | ✗ Our sessions are ephemeral containers, so it needs hosting or a binary file in git. Friends can't review edits as diffs, and an LLM reads Markdown better than Cypher results. |
| Vector DB / RAG only | ✗ Loses structure ("who reviews Spark?" is a graph query, not a similarity search) and needs an embedding API key. The corpus is small enough for full-text search plus an LLM. |
| **Markdown entities + frontmatter edges in git → SQLite (FTS5 + edges table)** | ✓ Diffable, PR-reviewable, readable on GitHub and in Obsidian, provenance via git, zero hosting. Recursive CTEs give graph traversal. It exports to Kuzu/Neo4j/graph views later. |
| Add embeddings later (sqlite-vec) | Optional, in phase 3, only if full-text search proves insufficient. |

### One repository: `iceberg-context` (public)
Everything lives here: the skill, the curated knowledge base, cleaned raw captures (`data/raw/`), sync state (`data/state.json`) and the pipeline code.

- **Size:** raw data is text-only, with emails stripped and quoted replies removed. That is about 30–40 MB for dev@ since 2018 plus about 18 MB of transcripts, and should stay under about 100 MB with full history.
- **Clones stay fast:** sessions clone shallow, so the growing history costs nothing.
- **Frozen months:** closed months are frozen and never rewritten.

## 4. Layered model

```
L0  raw capture      (data/raw/)     immutable, per source, regenerable by collectors
L1  records          (kb repo)       one page per meeting / dev thread / video / release / vote — "what was said, when, by whom"
L2  entities (graph) (kb repo)       people, working groups, initiatives, modules, repos, docs — current state + dated timeline
L3  synthesis        (kb repo)       state-of-iceberg, weekly briefings, opportunities, influence & ownership maps
IDX index            (built, not committed)  kb.sqlite: nodes, edges, records, FTS5 — built locally by the kb CLI
```

### Directory layout (kb repo)
```
CLAUDE.md, context.md                 entry points (our own work log stays in context.md)
docs/                                 this plan, schema reference, contributor guide
schema/                               JSON Schemas for frontmatter of each page type (validated in CI)
people/<login>.md                     Person
people/aliases.yaml                   identity resolution: login ↔ names ↔ ASF id ↔ dev@ display names
groups/<slug>.md                      WorkingGroup (cadence, notes doc, playlist, leads, current topics)
initiatives/<slug>.md                 Initiative (v4-amt, column-updates, vector-type, mv-spec, read-restrictions, ...)
modules/<repo>/<module>.md            Module (owners, reviewers, hot spots, recent changes)
repos/<repo>.md                       Repo (release cadence, process, CI, layout)
releases/<repo>-<version>.md          Release (RM, RCs, vote, notable changes)
records/meetings/<group>/<YYYY>/<date>.md     Meeting = notes-doc section + transcript summary
records/threads/<YYYY>/<MM>/<slug>.md         dev@ thread (DISCUSS/VOTE/RESULT/ANNOUNCE ...)
records/videos/...                     only for talks without a meeting record
briefings/weekly/<YYYY>-W<ww>.md      what changed this week, decisions, upcoming meetings, new opportunities
state-of-iceberg.md                   always-current top page: active initiatives, open votes, releases, hot topics
opportunities.md                      ranked contribution opportunities (with who-to-talk-to and where to show up)
maps/ownership.md, maps/influence.md  generated tables (module → owners/reviewers; who drives what)
pipeline/                             collectors, extractors, integrator, validators, build_index, kb CLI
notes/                                free-form human notes and deep dives
```

## 5. Graph schema

### Node types (one page each; `id` = `type/slug`)
| Type | Key fields |
|---|---|
| `person` | login, names[], asf_id, roles[{role: pmc/committer/triage/rm, since}], areas[], status (active/dormant) |
| `group` (working group) | cadence, notes_doc, playlist, calendar_title, leads[], active (bool) |
| `initiative` | status (idea/discuss/design/vote/accepted/implementing/released/abandoned), spec_version, champions[], groups[], modules[], prs[], docs[], votes[] |
| `module` | repo, path, owners[], reviewers[], activity metrics |
| `repo`, `release`, `doc` (design doc), `vote` | |
| records: `meeting`, `thread`, `video` | date, source URL(s), participants[], summary, decisions[], action_items[], mentions[] |

### Edge types (in frontmatter, each with `since`/`as_of` and `sources[]`)
```
person  -[champions]->     initiative        person -[member_of|leads]-> group
person  -[reviews {n,window}]-> module       person -[contributes {n,window}]-> module
person  -[has_role {since}]-> repo           person -[release_manager]-> release
person  -[spoke_in|presented]-> meeting      person -[started|voted {binding}]-> thread
meeting -[of]-> group    meeting|thread -[discussed]-> initiative|pr    meeting -[decided]-> decision text
initiative -[touches]-> module   initiative -[depends_on|blocks|supersedes]-> initiative
pr -[implements]-> initiative    doc -[design_for]-> initiative    vote -[ratifies]-> initiative
```
- **Provenance rule:** every non-trivial fact carries at least one source link (PR, dev@ permalink, notes-doc section, or video timestamp).
- **Confidence labels:** `observed` comes straight from data, such as roster, git, PR or vote counts. `extracted` was pulled by an LLM from text and has a citation. `inferred` is an LLM judgment, such as a speaker in an unlabeled transcript. Pages show confidence, so readers can tell data from interpretation.

### Page shape (entities)
```markdown
---
id: initiative/v4-amt
type: initiative
status: accepted-baseline
champions: [person/amogh-jahagirdar, person/rdblue]
groups: [group/v4-metadata]
modules: [module/iceberg/core, module/iceberg/format]
prs: [apache/iceberg#16025, apache/iceberg#17541]
votes: [record/threads/2026/10/vote-merge-baseline-v4-amt-spec]
updated: 2026-11-13
---
## Current state        <!-- generated: pipeline rewrites this block -->
## Timeline             <!-- generated: append-only dated bullets with citations -->
## Open questions / where help is needed   <!-- generated -->
## Notes                <!-- human: never overwritten by the pipeline -->
```
Generated blocks sit between markers. The pipeline only rewrites those blocks, so human notes and edits from friends are never clobbered.

## 6. Pipeline

```
collect (deterministic)  →  normalize (L0, data/raw/)  →  extract (LLM, per new record)
      →  integrate (update L2 entities + L3 synthesis)  →  validate  →  build index  →  commit/push + weekly briefing
```

### Collectors (prototypes already exist in `pipeline/prototypes/`)
| Source | Method | Change detection | Runs where |
|---|---|---|---|
| dev@ | PonyMail `mbox.lua` per month plus `stats.lua` for permalinks | Message-ID dedupe; freeze closed months | GitHub Action (daily) |
| GitHub PRs/issues | In Actions: the REST/GraphQL API with the default `GITHUB_TOKEN` (full read of public repos: PR bodies, review comments, reviews, `merged_by`, files changed, linked issues). In Claude sessions: the search API only. | `updated:>=last_sync`, upsert by number | GitHub Action (daily) |
| git history | treeless clones; `git log` since last SHA → ownership metrics | last processed SHA | GitHub Action (daily) |
| ASF roster | whimsy `committee-info.json`, `public_ldap_projects.json` | diff | GitHub Action (weekly) |
| Sync notes docs | Google Docs `read_doc` JSON (tab-aware) via the Docs connector | `modifiedTime` → section hashes | Claude scheduled session |
| Calendar | *Iceberg Dev Events* calendar via the Calendar connector | next 14 days plus newly added series | Claude scheduled session |
| YouTube | `yt-dlp --flat-playlist` plus RSS → `en-orig` json3 captions | processed-ID state | Claude scheduled session* |

\*YouTube bot checks hit cloud IPs intermittently. The collector retries with backoff and never marks a failed video done. If it proves unreliable, a cookie-less fallback is to run that one step from a home machine via Remote Control.

**Why the split:**
- The deterministic collectors need no AI and no secrets beyond the default `GITHUB_TOKEN`, so GitHub Actions runs them free and daily.
- The Google connectors exist only inside Claude sessions, and so does the LLM extraction.

### Extractors (LLM, run by Claude in the scheduled session)
- **Meeting:** join the notes-doc section and the transcript for the same group and date, then produce:
  - summary
  - decisions
  - action items with owners
  - open questions
  - initiatives, PRs and docs mentioned
  - participants, labeled observed (from notes) or inferred (from transcript)
  - notable quotes with video timestamps
  - Output is structured JSON validated against `schema/meeting.json`, then rendered to Markdown.
- **dev@ thread:** classify the type, summarize the positions and the outcome, extract the vote tally (binding where known), and link to initiatives.
- **PR batch:** map notable PRs (spec, large, long-running, many reviewers) to initiatives and modules.
- **Cost:** a typical week is about 6–8 meetings × ~65k tokens of transcript, plus about 100 dev@ messages and the PR deltas, which fits comfortably in one session. Transcripts are summarized once; the raw text stays in `data/raw/` for re-querying.

### Integrator
- **Entities:** apply the new edges to entity pages, append timeline bullets, and recompute "Current state", reviewer and owner tables, and initiative status.
- **Synthesis:** regenerate `state-of-iceberg.md`, `opportunities.md` and the `maps/`, and write `briefings/weekly/<week>.md` plus a changelog entry.
- **Opportunity ranking signals:**
  - an initiative is moving but needs hands, such as an implementation in Python, Rust or Go lagging Java
  - an issue has many 👍 and no PR
  - an area has an active reviewer but a review backlog
  - good-first-issues
  - "help wanted" or action items with no owner in sync notes
  - recent bugs in areas we know

  Each opportunity links to who to talk to and which sync to attend.

### Validators (CI on every push)
- Frontmatter matches the JSON Schema.
- Every edge target exists.
- Every extracted fact has a source.
- **Privacy linter:** no email addresses, phone numbers or personal details. People pages may hold only public project activity.
- Generated-block markers are intact.

### Code map (the "why" behind code)
- **Built from git history:** for every commit, the `(#NNNN)` in the squash title gives the PR, and `--name-only` gives the files.
  - This produces `code_map(path, pr, date, author)` for both repos, from about 10k PRs.
  - Each PR links to its issue, review comments, dev@ threads, meetings and initiative.
- **Function level:** at query time, `kb why --symbol` runs `git log -L :<symbol>:<path>` against the user's local checkout when one is available.
- **What it answers:** "why is `SnapshotProducer` written like this", "what was debated when this validation was added", and "which spec rule does this code implement".

### Index and query
`pipeline/build_index.py` compiles everything into `kb.sqlite` in seconds. Tables:
- `nodes(id, type, title, status, updated)`
- `edges(src, rel, dst, since, as_of, confidence, source)`
- `records(id, type, date, group, url)`
- `fts(id, body)` (FTS5)

`kb` CLI examples:
```bash
kb search "monotonic snapshot timestamps"        # full-text over records + entities
kb who reviews module/iceberg/spark --since 6m     # graph query
kb person singhpk234                               # roles, areas, initiatives, recent activity
kb initiative v4-amt --timeline                     # lifecycle across dev@/syncs/PRs
kb upcoming                                         # next syncs + agenda + what to read beforehand
kb opportunities --area python --level starter
```
- **The index is never committed.** The `kb` CLI builds `kb.sqlite` locally from the repo on first use, which takes seconds, and rebuilds it when the repo changes.

## 7. Delivery layer: the `iceberg-context` skill

**A skill, not a server.** It lives at `.claude/skills/iceberg-context/`, so Claude Code loads it automatically in any session that has this repo attached, through the environment's repository list. People outside cloud sessions can copy the folder to `~/.claude/skills/`. There is no server and no hosting.

```
.claude/skills/iceberg-context/
  SKILL.md        when to use it + the workflow below
  scripts/kb      CLI over the repo (builds kb.sqlite locally on first use)
```

### Agent workflow (encoded in SKILL.md)
1. **At session start:** `kb status` shows when each source last synced and what's new since then.
2. **Before changing code:**
   - `kb context <paths>`: related initiatives and spec sections, open PRs on the same files, active reviewers, recent decisions, conventions.
   - `kb why <path> [--symbol X]`: the PRs that shaped the code, their review debates, and the linked threads, votes and meetings.
3. **For project or community questions:** `kb search`, `kb initiative <name>`, `kb person <login>`, `kb who-to-ask <path|topic>`, `kb whats-new --since`, `kb upcoming`, `kb opportunities [--level starter] [--area python]`.
4. **To prove a claim:** `kb source <id>` prints the exact quote and permalink. Every answer cites sources and labels its confidence (observed / extracted / inferred).
5. **When asked to "sync now":** run the pipeline on demand (§6).

New contributors start from `state-of-iceberg.md` and `kb opportunities --level starter`.

### Optional later
- An MCP server wrapping the same CLI, for Cursor, Codex or claude.ai chat.
- Context packs: generated per-area Markdown for agents without skills.

## 8. Collaboration ("update on the go")
- **Friends:** they become collaborators on both repos and add `iceberg-context` to their own Claude environments. The CLAUDE.md loads automatically and tells every session to read `state-of-iceberg.md` first.
- **Human edits:** go in `## Notes` blocks or `notes/` (meeting impressions, conversations, plans). Directly to `main` for small notes, or as PRs for structural changes.
- **On-demand refresh:** saying "sync now" in any session runs the same pipeline as the schedule. `pipeline/state.json` holds the cursors, so concurrent runs don't duplicate work.
- **Our own work:** `context.md` (work log) and `notes/` remain our personal layer on top of the community KB.

## 9. Privacy and ethics guardrails (the repo is public)
- **Sources:** only public sources and public project activity: ASF roster, public lists, public docs and recordings, GitHub.
- **Off limits:**
  - No email addresses: strip them from mbox, Docs person chips and mailto links.
  - No personal lives.
  - No speculation about motives or personalities.
- **"Influence" means the observable record:** roles, votes, reviews, championed proposals and collaboration patterns.
- **Labels:** inferred attributions (speakers in transcripts) are labeled as such, and AI-generated sources such as Gemini notes are marked.
- **Tone:** write people pages as if the person will read them, because they can.

## 10. Roadmap

| Phase | Scope | Deliverables |
|---|---|---|
| **0: Foundation** | repo skeleton; schemas; `people/aliases.yaml` seeded from the research; productionize the prototype collectors; code map; `build_index.py` and the `kb` CLI; CI validators; **the skill with a minimal `kb`** (status / search / why / source) so we use it from day 1 | a working pipeline we can already query |
| **1: Seed** (from the 2026-11-13 research) | governance, people (PMC, committers, top 60 contributors), 14 working groups, about 20 active initiatives, module ownership maps, first `state-of-iceberg.md` and `opportunities.md` | a useful KB on day 1 |
| **2: Backfill (6 months)** | meetings from May to Nov 2026 (notes plus about 80 transcripts), dev@ threads (DISCUSS/VOTE/RESULT), notable PRs, releases | the full recent picture, with timelines |
| **3: Automation** | GitHub Actions daily collectors; scheduled Claude session weekly (Mon morning IST): docs, calendar, YouTube, LLM extraction, briefing | self-updating KB with a weekly briefing |
| **4: Skill v1** | the full `kb` command set (`context`, `whats-new`, `initiative`, `person`, `who-to-ask`, `upcoming`, `opportunities`), polished SKILL.md workflow, a newcomer onboarding path | plug-and-play for Claude Code agents |
| **5: Depth** | dev@ back to 2018 (DISCUSS/VOTE threads only), older syncs (index-level, summarize on demand), git evolution per module, influence and collaboration analytics, context packs, static site and graph view, optional MCP server | history and the "how did we get here" layer |

**Rough effort:**
- Phases 0–1: one or two working sessions.
- Phase 2: a few batched sessions, about 80 transcripts at about 65k tokens each, parallelized with subagents.
- After that: about one session-hour a week.

## 11. Decisions needed
1. **Allow GitHub Actions** on `iceberg-context` for the daily deterministic collectors?
2. **Weekly scheduled session:** Monday 08:00 IST? Plus an optional mid-week light run (dev@ and GitHub only, no LLM).
3. **Backfill depth for LLM summaries:** 6 months (recommended), then deepen on demand.
4. **Scope:** Java and PyIceberg in depth. Rust, Go and C++ at the initiative and release level only. Polaris and Arrow out of scope except where they link in.
