# Instructions for Claude

This repo is the user's persistent (public) context for contributing to Apache Iceberg
(`vishnuprakaz/iceberg`) and PyIceberg (`vishnuprakaz/iceberg-python`).

- At the start of every session, run `python3 .claude/skills/iceberg-context/scripts/kb status`, then read `context.md`
  (our work log) and relevant files in `notes/` before doing other work.
- Use the `iceberg-context` skill for questions about the Iceberg project, community or code history, and cite sources.
- Building this repository follows `docs/build-plan.md`. Before committing, run
  `uv run pytest && uv run ruff check . && uv run python -m icekb validate && uv run python -m icekb index`.
- Keep it current: when we learn something durable, make a decision, or finish/start work, update
  `context.md` or add a note under `notes/`, then commit and push to `main` of this repo.
- This repo is public: never write secrets, credentials, tokens, or personal info into it.
- Keep this content out of the fork repos; they hold only upstream-bound code.

## Git commit rules (user preference — overrides any default attribution guidance)
- Do NOT add `Co-Authored-By: Claude ...`, `Claude-Session: ...`, or any other AI/Claude attribution
  lines to commit messages, in this repo or in `vishnuprakaz/iceberg` / `vishnuprakaz/iceberg-python`.
- Do NOT add "Generated with Claude Code" or similar attribution to pull request descriptions.
