import datetime as dt
import json

from icekb.collectors import youtube
from icekb.dates import find_date
from icekb.ingest import calendar, syncdocs
from icekb.integrate.store import Data
from icekb.process import apply, queue

GROUPS = """
groups:
  - {slug: catalog, name: Catalog Sync, cadence: every 3 weeks, doc: DOC1, title_match: [catalog community sync]}
  - {slug: index, name: Index Sync, cadence: every 2 weeks, doc: DOC2, tab: Meeting notes, title_match: [index support]}
  - {slug: community, name: Community Sync, title_match: [community sync], exclude_match: [catalog]}
"""


def setup(kb_root):
    (kb_root / "data" / "sources.yaml").write_text(GROUPS)
    (kb_root / "people" / "aliases.yaml").write_text("people:\n  ada:\n    names: [Ada Example]\n")
    for name in ("extract-meeting.json", "extract-thread.json"):
        (kb_root / "schema" / name).write_text((apply.Path(__file__).parents[1] / "schema" / name).read_text())


def test_find_date_formats():
    for text, want in [("2026-10-28 (Recording)", "2026-10-28"), ("Nov 4, 2026", "2026-11-04"), ("15 March 2023", "2023-03-15"),
                       ("10/27/2026", "2026-10-27"), ("Iceberg Index Support Sync   2026 11 09", "2026-11-09"),
                       ("Community Sync 10 28 2026", "2026-10-28"), ("Rust Community Sync Oct 23 2026", "2026-10-23"),
                       ("2024-03–27", "2024-03-27")]:
        assert find_date(text)[0].isoformat() == want, text
    assert find_date("no date here 12") is None


def test_heading_date_rules():
    assert syncdocs.heading_date("## Nov 4, 2026")[0] == dt.date(2026, 11, 4)
    assert syncdocs.heading_date("# 2026-07-01([RECORDING](https://youtu.be/M328cFeaLIs))")[0] == dt.date(2026, 7, 1)
    assert syncdocs.heading_date("## **Sep 3, 2026**")[0] == dt.date(2026, 9, 3)
    assert syncdocs.heading_date("## Sep 15, 2026 (Cancelled)")[1].startswith("(Cancelled")
    assert syncdocs.heading_date("We met on Nov 4, 2026 and decided things") is None
    assert syncdocs.heading_date("2026-01-05 is when the long design discussion about many different things happened, and more text") is None


def test_syncdocs_ingest_tabs_refs_and_status(kb_root):
    setup(kb_root)
    doc = kb_root / "doc.md"
    doc.write_text(
        "# Design  \n\n2026-01-01\n\ndesign text that is not a meeting\n\n# Meeting notes  \n\n"
        "## Nov 9, 2026 ([recording](https://youtu.be/abcdefghijk))\n\n- \\[Ada Example\\] index layout, see \\#18585\n"
        "- Python\n    - fix in \\#4291 (Thanks Ada Example\\!)\n\n" + "discussion text. " * 20 + "\n\n"
        "## Oct 26, 2026 (Cancelled)\n\nnothing\n\n# Appendix  \n\n## Dec 1, 2026\n\nnot a meeting\n")
    out = syncdocs.ingest(kb_root, "index", doc, "2026-11-10T00:00:00Z")
    assert out["meetings"] == 2
    recs = [json.loads(line) for line in (kb_root / "data/raw/syncdocs/index/2026.jsonl").read_text().splitlines()]
    held = next(r for r in recs if r["id"] == "meet:index:2026-11-09")
    assert held["meta"]["status"] == "held" and held["meta"]["recordings"] == ["abcdefghijk"] and held["people"] == ["ada"]
    assert "gh:apache/iceberg#18585" in held["refs"] and "gh:apache/iceberg-python#4291" in held["refs"]
    assert next(r for r in recs if r["id"] == "meet:index:2026-10-26")["meta"]["status"] == "cancelled"
    state = json.loads((kb_root / "data/state/syncdocs.json").read_text())
    assert state["cursor"]["index"]["modified"] == "2026-11-10T00:00:00Z"


def test_calendar_ingest_drops_private_fields(kb_root):
    setup(kb_root)
    address = "someone" + "@" + "corp.io"
    events = {"events": [{"id": "e1", "summary": "Iceberg Catalog Community Sync Meeting", "status": "confirmed",
                          "start": {"dateTime": "2026-11-25T22:30:00+05:30"}, "creator": {"email": address},
                          "description": 'Notes: <a href="https://docs.google.com/document/d/1iPGVCIcr-M0XtAiudOguWAvmqIdVgpYN5vz5ohO8PKw/edit">doc</a>',
                          "htmlLink": "https://calendar.example/e1", "conferenceUrl": "https://meet.example/x"},
                         {"id": "e2", "summary": "Iceberg Community Sync (Recorded)", "start": {"dateTime": "2026-12-09T17:00:00Z"}}]}
    (kb_root / "cal.json").write_text(json.dumps(events))
    out = calendar.ingest(kb_root, kb_root / "cal.json")
    assert out["events"] == 2 and out["titles_without_group"] == []
    text = (kb_root / "data/raw/calendar/2026/11.jsonl").read_text()
    rec = json.loads(text)
    assert rec["date"] == "2026-11-25T17:00:00Z" and rec["meta"]["group"] == "catalog" and "notes_doc" in rec["meta"]
    assert address not in text
    assert json.loads((kb_root / "data/raw/calendar/2026/12.jsonl").read_text())["meta"]["group"] == "community"


def _captions():
    return {"events": [{"tStartMs": 0, "segs": [{"utf8": "Welcome everyone."}]},
                       {"tStartMs": 5000, "segs": [{"utf8": ">> We agreed to nest the index routes under the table."}]},
                       {"tStartMs": 200000, "segs": [{"utf8": ">> Next topic is the vote."}]}]}


def test_youtube_record_and_paragraphs(kb_root):
    setup(kb_root)
    cfg = Data(kb_root).cfg
    info = {"id": "abcdefghijk", "title": "Iceberg Index Support Sync   2026 11 09", "upload_date": "20261111", "duration": 3300,
            "description": "Notes https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0/edit"}
    rec = youtube.build_record(info, _captions(), cfg["groups"])
    assert rec["id"] == "yt:abcdefghijk" and rec["date"].startswith("2026-11-09") and rec["meta"]["group"] == "index"
    assert rec["body"].split("\n\n")[1].startswith("[0:00:05] We agreed") and rec["ai_generated"] is True
    assert rec["refs"] == ["doc:1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0"]
    talk = youtube.build_record({**info, "title": "Deletion Vectors explained", "id": "zzzzzzzzzzz"}, _captions(), cfg["groups"])
    assert talk["meta"]["kind"] == "talk" and talk["date"].startswith("2026-11-11")


def _meeting_fixture(kb_root):
    setup(kb_root)
    doc = kb_root / "doc.md"
    doc.write_text("# Meeting notes  \n\n## Nov 9, 2026 ([recording](https://youtu.be/abcdefghijk))\n\n- \\[Ada Example\\] routes\n" + "notes text. " * 60)
    syncdocs.ingest(kb_root, "index", doc)
    info = {"id": "abcdefghijk", "title": "Iceberg Index Support Sync 2026 11 09", "upload_date": "20261111", "duration": 300}
    from icekb.util import upsert
    upsert(kb_root, "youtube", [youtube.build_record(info, _captions(), Data(kb_root).cfg["groups"])])


def test_queue_pairs_notes_with_recording_and_skips_done(kb_root):
    _meeting_fixture(kb_root)
    items = queue.queue_meetings(Data(kb_root), "2026-01-01", "2026-01-01")
    assert [i["id"] for i in items] == ["meeting/index/2026-11-09"] and items[0]["has_transcript"]
    bundle = (kb_root / items[0]["input"]).read_text()
    assert "meet:index:2026-11-09" in bundle and "yt:abcdefghijk" in bundle and "[0:00:05]" in bundle
    input_hash = bundle.split("`_input_hash`: `")[1].split("`")[0]
    out = kb_root / items[0]["output"]
    out.parent.mkdir(parents=True)
    out.write_text(json.dumps({"_input_hash": input_hash}))
    assert queue.queue_meetings(Data(kb_root), "2026-01-01", "2026-01-01") == []


def test_apply_accepts_good_and_rejects_bad_quotes(kb_root):
    _meeting_fixture(kb_root)
    ex = {"id": "meeting/index/2026-11-09", "sources": ["meet:index:2026-11-09", "yt:abcdefghijk"],
          "summary": "The group discussed where the index routes live in the REST catalog and what to vote on next.",
          "topics": [{"title": "REST routes", "summary": "They agreed to nest index routes under the table resource.",
                      "decisions": ["Nest index routes under the table"], "refs": ["gh:apache/iceberg#16963"],
                      "quotes": [{"text": "We agreed to nest the index routes under the table.", "at": "0:00:05"}]}],
          "participants": [{"who": "ada", "basis": "notes"}]}
    path = kb_root / "data/extract/meetings/index/2026-11-09.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(ex))
    result = apply.apply_all(kb_root)
    assert result["meetings"] == 1 and not result["rejected"]
    page = (kb_root / "records/meetings/index/2026/2026-11-09.md").read_text()
    assert "Nest index routes under the table" in page and "t=5s" in page and "written by an AI model" in page
    ex["topics"][0]["quotes"] = [{"text": "We decided to drop the feature entirely and start over.", "at": "0:00:05"}]
    path.write_text(json.dumps(ex))
    assert "does not match the transcript" in str(apply.apply_all(kb_root)["rejected"])
    ex["topics"][0]["quotes"] = []
    ex["sources"] = ["meet:index:1999-01-01"]
    path.write_text(json.dumps(ex))
    assert "unknown source" in str(apply.apply_all(kb_root)["rejected"])


def test_thread_queue_and_apply_checks_citations(kb_root):
    setup(kb_root)
    from icekb.util import upsert
    mails = [{"id": f"devlist:m{i}", "source": "devlist", "type": "email", "date": f"2026-11-0{i + 1}T10:00:00Z",
              "url": f"https://lists.apache.org/thread/m{i}", "people": ["ada"], "title": "[VOTE] Widgets", "body": "text " * 30,
              "refs": [], "hash": f"h{i}", "meta": {"thread": "t-0123456789abcdef", "kind": "vote", "reply": i > 0, "subject": "[VOTE] Widgets"}}
             for i in range(4)]
    upsert(kb_root, "devlist", mails)
    items = queue.queue_threads(Data(kb_root), "2026-01-01")
    assert len(items) == 1 and items[0]["messages"] == 4
    ex = {"id": "thread/t-0123456789abcdef", "sources": ["devlist:m0"], "title": "Vote on widgets",
          "summary": "A vote to adopt widgets in the v4 spec. Four messages, all in favour, and the result was posted.",
          "outcome": {"status": "passed", "note": "Passed with 3 binding votes.", "source": "devlist:m3"},
          "positions": [{"who": "ada", "stance": "In favour.", "source": "devlist:m1"}]}
    path = kb_root / "data/extract/threads/t-0123456789abcdef.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(ex))
    assert apply.apply_all(kb_root)["threads"] == 1
    assert "Passed with 3 binding votes" in next((kb_root / "records/threads/2026/11").glob("*.md")).read_text()
    ex["outcome"]["source"] = "devlist:not-in-thread"
    path.write_text(json.dumps(ex))
    assert "not in this thread" in str(apply.apply_all(kb_root)["rejected"])
