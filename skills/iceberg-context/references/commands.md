# kb command reference

`kb` is `python3 SKILL_DIR/scripts/kb`. Every command prints plain text. Ids in square brackets can be passed to `kb source`.

## Ids

| Prefix | Meaning | Example |
|---|---|---|
| `devlist:` | A dev mailing-list message | `devlist:f7nwynr69g18kj61nt5h1f45cn8g768t` |
| `gh:` | A pull request, issue or comment | `gh:apache/iceberg#17523` |
| `commit:` | A commit | `commit:apache/iceberg@58cf9d8bba9f` |
| `meet:` | A section of a working group's notes document | `meet:index:2026-11-09` |
| `yt:` | A recording transcript | `yt:q-A9Y5FMRY8` |
| `spec:` | A section of the spec or contribution docs | `spec:apache/iceberg:format/spec.md#snapshots` |
| `cal:` | A calendar event | |
| `person/`, `group/`, `initiative/`, `module/`, `release/`, `meeting/`, `thread/` | Pages | `initiative/v4-metadata-tree` |

## Search

```bash
kb search snapshot timestamp --type spec-section        # what the spec says
kb search "equality deletes" --type thread               # summarized list threads
kb search vended credentials --type email --since 3m     # raw messages, recent
kb search derived columns --type meeting                 # summarized meetings
kb search tight_stats --type pr                          # pull requests
```

`--since` takes a date (`2026-10-01`) or a span (`30d`, `6w`, `3m`, `1y`). Pages have no date and always pass the filter.

## Source

```bash
kb source gh:apache/iceberg#17523                 # state, reviewers, merged by, files, description
kb source yt:q-A9Y5FMRY8 --grep "derived columns" # only the passages of a transcript that mention a phrase
kb source meet:community:2026-10-28 --chars 8000  # more of a long record
```

Transcripts carry `[h:mm:ss]` markers; append `&t=SECONDSs` to the video URL to link to the moment.

## Why and context

```bash
kb why core/src/main/java/org/apache/iceberg/SnapshotProducer.java --limit 20
kb why pyiceberg/table/                                   # a directory
kb why SnapshotProducer.java --symbol commit --checkout ~/src/iceberg   # one method, needs a local clone with history
kb context api/src/main/java/org/apache/iceberg/Snapshot.java core/src/main/java/org/apache/iceberg/BaseSnapshot.java
```

`why` goes from file to commits to pull requests to the list threads and meetings that mention those pull requests.
`context` adds who is active there now and which open pull requests touch the same files.

## People, groups, initiatives

```bash
kb initiative v4                 # matches by id, then by title
kb group catalog
kb person stevenzwu
kb who-to-ask spark/             # a path: authors and reviewers
kb who-to-ask "read restrictions"  # a topic: initiative, group and the people linked to them
kb show release/iceberg-1.12.0
```

Pages for people record public project activity only. Links marked `extracted` or `inferred` come from an AI model reading a
source; `observed` ones come straight from data.

## Time

```bash
kb whats-new --since 14d --area REST
kb upcoming --days 21
```

## Opportunities

```bash
kb opportunities                      # full ranked list
kb opportunities --area flink
kb opportunities --level starter      # starter, intermediate or advanced
```
