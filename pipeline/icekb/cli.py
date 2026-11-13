"""Command line: python -m icekb <command>."""
from __future__ import annotations

import argparse
import sys

from icekb import validate
from icekb.integrate import index
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
        print("kb/index/ is out of date; run `python -m icekb index`", file=sys.stderr)
        return 1
    print("index is up to date" if args.check else "index written")
    return 0


def cmd_collect(args) -> int:
    from icekb import run

    return run.collect(repo_root(), args.source, backfill=args.backfill, option=dict(o.split("=", 1) for o in args.option))


def cmd_integrate(_args) -> int:
    from icekb.integrate import entities
    from icekb.integrate.store import Data

    root = repo_root()
    print("pages changed:", entities.build(Data(root)))
    index.write(root)
    return 0


def cmd_queue(args) -> int:
    import json

    from icekb.integrate.store import Data
    from icekb.process import queue

    data = Data(repo_root())
    since = args.since or data.since(14)
    if args.kind == "meetings":
        items = queue.queue_meetings(data, since, args.transcripts_since or since, args.force)
    else:
        items = queue.queue_threads(data, since, args.min_messages, args.force)
    print(json.dumps(items, indent=1))
    return 0


def cmd_apply(_args) -> int:
    from icekb.process import apply

    root = repo_root()
    result = apply.apply_all(root)
    print(f"meetings: {result['meetings']}, threads: {result['threads']}, rejected: {len(result['rejected'])}")
    for path, errors in result["rejected"].items():
        print(f"  REJECTED {path}")
        for e in errors:
            print(f"    - {e}")
    index.write(root)
    return 1 if result["rejected"] else 0


def cmd_ingest(args) -> int:
    root = repo_root()
    if args.kind == "syncdocs":
        from icekb.ingest import syncdocs

        if not args.group:
            raise SystemExit("ingest syncdocs needs --group <slug from data/sources.yaml>")
        print(syncdocs.ingest(root, args.group, args.file, args.modified))
    elif args.kind == "transcript":
        from icekb.collectors import youtube

        if not args.captions:
            raise SystemExit("ingest transcript needs the yt-dlp .info.json as the file and --captions <.json3 file>")
        print(youtube.ingest_files(root, args.file, args.captions))
    else:
        from icekb.ingest import calendar

        print(calendar.ingest(root, args.file))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="icekb", description="Iceberg Context pipeline")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="check pages, links and privacy rules").set_defaults(fn=cmd_validate)
    p = sub.add_parser("index", help="rebuild kb/index/ from page frontmatter")
    p.add_argument("--check", action="store_true", help="fail if index/ is stale instead of writing it")
    p.set_defaults(fn=cmd_index)
    p = sub.add_parser("collect", help="run one collector, or a named set (daily)")
    p.add_argument("source")
    p.add_argument("--backfill", action="store_true", help="fetch full history instead of only what is new")
    p.add_argument("-o", "--option", action="append", default=[], metavar="KEY=VALUE")
    p.set_defaults(fn=cmd_collect)
    sub.add_parser("integrate", help="regenerate people, group, module, repository and release pages").set_defaults(fn=cmd_integrate)
    p = sub.add_parser("queue", help="list meetings or threads that need AI extraction and write their input bundles")
    p.add_argument("kind", choices=["meetings", "threads"])
    p.add_argument("--since", help="YYYY-MM-DD (default: 14 days ago)")
    p.add_argument("--transcripts-since", help="include recording transcripts for meetings on or after this date (default: --since)")
    p.add_argument("--min-messages", type=int, default=4)
    p.add_argument("--force", action="store_true", help="include items whose extraction is already up to date")
    p.set_defaults(fn=cmd_queue)
    sub.add_parser("apply", help="validate AI extractions against their sources and render record pages").set_defaults(fn=cmd_apply)
    p = sub.add_parser("ingest", help="parse a file saved from a Claude connector (meeting notes or calendar)")
    p.add_argument("kind", choices=["syncdocs", "calendar", "transcript"])
    p.add_argument("file")
    p.add_argument("--group", help="working-group slug, for syncdocs")
    p.add_argument("--captions", help="caption file (.json3), for transcript")
    p.add_argument("--modified", help="the document's modifiedTime, stored to detect changes next time")
    p.set_defaults(fn=cmd_ingest)
    args = parser.parse_args(argv)
    return args.fn(args)
