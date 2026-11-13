# Contributing

Thanks for helping. This repository is a shared map of the Apache Iceberg project and community. There are three ways to contribute.

## 1. Add your own notes

Put free-form notes in `notes/`, or under the `## Notes` heading of any page. The sync pipeline never edits either place.

## 2. Correct a page

Entity pages (`people/`, `groups/`, `initiatives/`, `modules/`, `releases/`) and record pages (`records/`) are partly generated.

- Text between `<!-- kb:generated:start -->` and `<!-- kb:generated:end -->` is rewritten by the pipeline. A manual edit there will
  be overwritten, so fix the cause instead: open a **Correction** issue, or fix the source mapping (for example `people/aliases.yaml`).
- Everything outside those markers is yours to edit.

Every factual claim needs a source: a link to a pull request, a mailing-list thread, a notes document or a video timestamp.

## 3. Improve the pipeline or the skill

```bash
uv sync
uv run pytest
uv run ruff check .
uv run python -m icekb validate
uv run python -m icekb index
```

- Pipeline code lives in `pipeline/icekb/`, tests in `tests/`.
- The skill lives in `.claude/skills/iceberg-context/`. Its `kb` script uses only the Python standard library; keep it that way.
- To add a data source, read `docs/build-plan.md` section 4 and add an entry to `data/sources.yaml`.

## Rules for content about people

This repository is public and the people in it can read it. Record public project activity only: roles, reviews, votes,
proposals, talks. No email addresses, no personal details, no speculation about motives or character. See [PRIVACY.md](PRIVACY.md).
CI rejects email addresses.

## Pull requests

Keep them small and focused. CI must pass. Describe what changed and why.
