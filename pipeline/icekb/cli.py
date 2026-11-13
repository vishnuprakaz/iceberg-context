"""Command line: python -m icekb <command>."""
from __future__ import annotations

import argparse
import sys

from icekb import index, validate
from icekb.paths import repo_root


def cmd_validate(_args) -> int:
    results = validate.run_all(repo_root())
    failed = 0
    for name, problems in results.items():
        print(f"{name}: {'ok' if not problems else f'{len(problems)} problem(s)'}")
        for p in problems:
            print(f"  - {p}")
        failed += len(problems)
    return 1 if failed else 0


def cmd_index(args) -> int:
    ok = index.write(repo_root(), check_only=args.check)
    if args.check and not ok:
        print("index/ is out of date; run `python -m icekb index`", file=sys.stderr)
        return 1
    print("index is up to date" if args.check else "index written")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="icekb", description="Iceberg Context pipeline")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="check pages, links and privacy rules").set_defaults(fn=cmd_validate)
    p = sub.add_parser("index", help="rebuild index/ from page frontmatter")
    p.add_argument("--check", action="store_true", help="fail if index/ is stale instead of writing it")
    p.set_defaults(fn=cmd_index)
    args = parser.parse_args(argv)
    return args.fn(args)
