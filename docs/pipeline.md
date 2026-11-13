# Pipeline reference

How data gets from its sources into pages. For the design reasoning see [build-plan.md](build-plan.md).

```
collect  →  normalize  →  link  →  process (AI)  →  integrate  →  validate  →  commit
```

## Commands

All run from the repository root with `uv run python -m icekb <command>`.

| Command | What it does | Runs in |
|---|---|---|
| `collect daily` | Runs `devlist`, `git`, `asf`, `github` in turn. A failing collector is recorded in its state file and does not stop the others | GitHub Action, every 6 hours |
| `collect <name> [--backfill] [-o key=value]` | Runs one collector | either |
| `collect youtube -o max_videos=25` | Fetches captions for recordings not yet stored | weekly session |
| `ingest syncdocs <file> --group <slug> [--modified <time>]` | Splits a notes document export into one record per meeting | weekly session |
| `ingest calendar <file>` | Turns calendar events into records | weekly session |
| `queue meetings\|threads [--since DATE]` | Lists items whose AI summary is missing or out of date, and writes an input bundle for each under `.work/queue/` | weekly session |
| `apply` | Validates AI extractions against their sources and renders `kb/records/` pages | weekly session |
| `integrate` | Regenerates people, group, module, repository and release pages and `kb/maps/` from data | weekly session |
| `index [--check]` | Rebuilds `kb/index/nodes.jsonl` and `kb/index/edges.jsonl` from page frontmatter | both |
| `validate` | Schema, link, generated-block and privacy checks | both, and CI |

## Sources

| Source | Collector | Stored under `data/raw/` | New data detected by |
|---|---|---|---|
| Dev mailing list | `collectors/devlist.py` | `devlist/YYYY/MM.jsonl` | Refetches the current month (and the previous one early in a month); records keyed by the archive id |
| Git history | `collectors/git.py` | `git/<repo>/YYYY.jsonl` | Last commit seen per repository |
| Spec and contribution docs | `collectors/git.py` | `spec/<repo>.jsonl` | Rewritten each run from the current files |
| ASF roster | `collectors/asf.py` | `asf/roster.jsonl` | Rewritten each run |
| Pull requests, issues, comments | `collectors/github.py` | `github/<repo>/{prs,issues,comments}/YYYY/MM.jsonl` | "Updated since" timestamp per repository and kind; bounded work per run |
| Meeting notes | `ingest/syncdocs.py` | `syncdocs/<group>/YYYY.jsonl` | Document `modifiedTime`, then a hash per meeting section |
| Calendar | `ingest/calendar.py` | `calendar/YYYY/MM.jsonl` | Event id |
| Recordings | `collectors/youtube.py` | `youtube/YYYY/MM.jsonl` | List of video ids already stored; failures retried |

Sync state is in `data/state/<source>.json`; `kb status` reads it.

## Record format

One JSON object per line; schema in [`schema/raw-record.json`](../schema/raw-record.json). Fields: `id`, `source`, `type`,
`date`, `url`, `people`, `title`, `body`, `refs`, `hash`, `meta`, `ai_generated`.

- `people` holds GitHub logins where the name could be resolved through `data/aliases.yaml`, otherwise `name:<display name>`.
  Unresolved names are counted in `data/state/unresolved-people.json`; add them to the alias file to resolve them.
- `refs` are links to other things: `gh:apache/iceberg#123`, `doc:<Google Doc id>`, `yt:<video id>`, `list:<thread id>`.
  They are what connects a commit to its pull request and a pull request to the threads and meetings that discussed it.
- Email addresses are removed from all text. Mailing-list Message-IDs are never stored.

## AI processing

Extractions are JSON files under `data/extract/`, written by the extractor agents in `.claude/agents/` and checked by `apply`:

- they must match `schema/extract-meeting.json` or `schema/extract-thread.json`;
- every cited source must exist, and for threads must belong to that thread;
- every quote must match the transcript near its timestamp.

A rejected extraction produces no page. Record pages state that they were written by an AI model and link their sources.

## GitHub limits

The Action's built-in token allows about 1,000 GraphQL points and 1,000 REST requests an hour. The collector stops before the
limit and after 25 minutes, saves its cursors, and continues on the next run. Full history of pull requests and issues therefore
arrives over several days; comments are kept from the date set in `data/sources.yaml` (`github.comments_since`).

## Adding a source

1. Add it to `data/sources.yaml`.
2. Write a collector in `pipeline/icekb/collectors/` exposing `collect(root, **options) -> dict`, or an ingester if the data comes
   through a Claude connector. Emit records in the common format and call `util.upsert`.
3. Record state with `state.save`. Add the source name to `SOURCES` in the `kb` script so `kb status` shows it.
4. Add a fixture test in `tests/`.
