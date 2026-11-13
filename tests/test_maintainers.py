"""Maintainer and PMC features: vote tallies, review queue, release, board report, decisions, loose ends."""
import json

from icekb.integrate import index, votes
from icekb.validate import people
from test_kb import kb


def mail(mid, date, who, subject, body, thread, kind="vote", reply=True):
    return {"id": f"devlist:{mid}", "source": "devlist", "type": "email", "date": date, "url": f"https://lists.apache.org/thread/{mid}",
            "people": [who], "title": ("Re: " if reply else "") + subject, "body": body, "refs": [], "hash": mid,
            "meta": {"thread": thread, "kind": kind, "reply": reply, "subject": subject}}


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))


def roster(asf_id, login, role, since=None, name=None):
    return {"id": f"asf:iceberg:{asf_id}", "source": "asf", "type": "roster", "date": f"{since or '1970-01-01'}T00:00:00Z",
            "url": "https://projects.apache.org/committee.html?iceberg", "people": [login], "title": f"{name}: {role}",
            "hash": asf_id, "meta": {"asf_id": asf_id, "role": role, "pmc_since": since, "name": name}}


def setup_votes(root):
    s = "[VOTE] Release Apache Iceberg 9.9.0 RC1"
    t = "t-00000000000000bb"
    write_jsonl(root / "data" / "raw" / "devlist" / "2026" / "10.jsonl", [
        mail("o1", "2026-10-01T10:00:00Z", "ada", s, "Please vote within 72 hours.\n\n[ ] +1 Release\n[ ] -1 Do not", t, "release-vote", False),
        mail("r1", "2026-10-01T12:00:00Z", "bob", s, "+1 (binding)\n\nOn Wed, Oct 1 Ada wrote:\n> [ ] -1 Do not", t, "release-vote"),
        mail("r2", "2026-10-01T13:00:00Z", "cy", s, "+1 (binding)\nverified signatures", t, "release-vote"),
        mail("r3", "2026-10-01T14:00:00Z", "name:Dee Unknown", s, "+1 (non-binding)", t, "release-vote"),
        mail("r4", "2026-10-01T15:00:00Z", "eve", s, "-1 (binding): the LICENSE is missing", t, "release-vote"),
        mail("r5", "2026-10-02T15:00:00Z", "eve", s, "Fixed now. +1 (binding)", t, "release-vote"),
        mail("res", "2026-10-05T10:00:00Z", "ada", "[RESULT][VOTE] Release Apache Iceberg 9.9.0 RC1",
             "My own vote is +1 (binding)\n\nThe vote passes with 3 binding +1 votes and 2 non-binding +1 votes.",
             "t-00000000000000cc", "result", False),
    ])
    write_jsonl(root / "data" / "raw" / "asf" / "roster.jsonl", [
        roster("ada", "ada", "pmc", "2020-01-01", "Ada Example"),
        roster("bob", "bob", "pmc", "2021-01-01", "Bob Example"),
        roster("eve", "eve", "pmc", "2026-12-01", "Eve Example"),  # joined the PMC after the vote
        roster("cy", "cy", "committer", None, "Cy Example"),
    ])


def test_parse_vote_ignores_quotes_and_templates():
    assert votes.parse_vote("+1 (binding)\n\nOn Mon, Nov 2 X wrote:\n> -1") == ("+1", "binding")
    assert votes.parse_vote("Thanks!\n\n-1 (non-binding), the build fails") == ("-1", "non-binding")
    assert votes.parse_vote("[ ] +1 Release\n[ ] -1 Do not", opener=True) is None
    assert votes.parse_vote("Release 0.11.0 looks good") is None  # a version number is not a vote
    assert votes.parse_vote("My own vote is +1 (binding)", opener=True) == ("+1", "binding")
    assert votes.parse_vote("+0") == ("0", None)


def test_stated_counts():
    assert votes.stated_counts("The vote passes with 4 binding +1 votes, 3 non-binding +1 votes") == {"binding": 4, "non-binding": 3}
    assert votes.stated_counts("   - +1 binding votes: 9\n   - +1 non-binding votes: 5 (including mine)")["binding"] == 9
    assert votes.stated_counts("Binding: 11 +1 votes\nNon-binding: 7 +1 votes") == {"binding": 11, "non-binding": 7}
    assert votes.stated_counts("Binding votes:\n\n  * A\n  * B\n\nNon-Binding votes:\n\n  * C\n\nThanks") == {"binding": 2, "non-binding": 1}


def test_vote_tally_uses_roster_on_vote_date(kb_root):
    setup_votes(kb_root)
    rows = votes.build(kb_root)
    v = next(r for r in rows if "9.9.0" in r["subject"])
    status = {x["who"]: (x["value"], x["status"]) for x in v["votes"]}
    assert status["bob"] == ("+1", "binding")
    assert status["cy"] == ("+1", "non-binding")  # committer, declared binding: still non-binding
    assert status["eve"] == ("+1", "non-binding")  # latest vote counts; not on the PMC yet on the vote date
    assert status["name:Dee Unknown"] == ("+1", "unverified")
    assert status["ada"] == ("+1", "binding")  # the release manager's vote stated in the result email
    assert v["tally"]["binding"]["+1"] == 2
    assert v["result"]["status"] == "passed" and v["result"]["stated"]["binding"] == 3
    assert v["check"].startswith("result email states 3 binding +1, counted 2")


def test_kb_votes_and_release(kb_root):
    setup_votes(kb_root)
    index.write(kb_root)
    out = kb("votes", "--match", "9.9.0")
    assert out.returncode == 0, out.stderr
    assert "binding +1 2, 0 0, -1 0" in out.stdout and "result: passed" in out.stdout
    assert "Dee Unknown (+1, declared non-binding)" in out.stdout
    assert "Binding = PMC member on the vote date" in out.stdout
    out = kb("release", "9.9.0")
    assert out.returncode == 0, out.stderr
    assert "Release manager (opened the vote): @ada" in out.stdout


def pr(number, author, created, reviews=(), last_commit=None, association="CONTRIBUTOR", files=("core/A.java",), state="open"):
    return {"id": f"gh:apache/iceberg#{number}", "source": "github", "type": "pr", "date": created,
            "url": f"https://github.com/apache/iceberg/pull/{number}", "people": [author], "title": f"Change {number}",
            "body": "", "refs": [], "hash": str(number),
            "meta": {"repo": "apache/iceberg", "number": number, "state": state, "draft": False, "files": list(files),
                     "reviews": [{"by": b, "state": s, "at": a} for b, s, a in reviews], "association": association,
                     "last_commit": last_commit, "comments": 0}}


def test_review_queue_buckets(kb_root):
    setup_votes(kb_root)
    write_jsonl(kb_root / "data" / "raw" / "github" / "iceberg" / "prs" / "2026" / "01.jsonl", [
        pr(1, "newbie", "2026-01-02T00:00:00Z", association="FIRST_TIME_CONTRIBUTOR"),
        pr(2, "zed", "2026-01-03T00:00:00Z", [("bob", "CHANGES_REQUESTED", "2026-01-05T00:00:00Z")], "2026-01-04T00:00:00Z"),
        pr(3, "zed", "2026-01-04T00:00:00Z", [("bob", "COMMENTED", "2026-01-05T00:00:00Z")], "2026-01-09T00:00:00Z"),
        pr(4, "zed", "2026-01-05T00:00:00Z", [("bob", "APPROVED", "2026-01-06T00:00:00Z")], "2026-01-05T00:00:00Z"),
        pr(5, "zed", "2026-01-06T00:00:00Z", [("someone", "APPROVED", "2026-01-07T00:00:00Z")], "2026-01-06T00:00:00Z"),
    ])
    index.write(kb_root)
    out = kb("review-queue", "--stale", "1")
    assert out.returncode == 0, out.stderr
    text = out.stdout
    assert "First-time contributors with no review: 1" in text and "#1 " in text
    assert "Waiting on the author: 1" in text
    assert "Updated since the last review: 1" in text
    assert "Approved by a committer, not merged: 1" in text
    assert "Approved by others, needs a committer: 1" in text
    assert "@bob" not in text.split("Time to first review")[-1]  # health numbers are aggregate, not per person


def test_board_report_and_loose_ends_run(kb_root):
    setup_votes(kb_root)
    index.write(kb_root)
    out = kb("board-report", "--quarter", "2026Q4")
    assert out.returncode == 0, out.stderr
    assert "## Membership Data" in out.stdout and "## Community Health" in out.stdout
    out = kb("loose-ends", "--since", "2020-01-01")
    assert out.returncode == 0, out.stderr
    assert "[VOTE] Widgets for v4" not in out.stdout  # a vote is not an unanswered discussion


def test_decisions(kb_root):
    setup_votes(kb_root)
    meet = kb_root / "data" / "extract" / "meetings" / "spark"
    meet.mkdir(parents=True)
    (meet / "2026-10-07.json").write_text(json.dumps({
        "id": "meeting/spark/2026-10-07", "sources": ["meet:spark:2026-10-07"], "summary": "x" * 50,
        "topics": [{"title": "Widgets", "summary": "talked about widgets", "decisions": ["Adopt monotonic widgets in v4."]}]}))
    index.write(kb_root)
    out = kb("decisions", "widgets")
    assert out.returncode == 0, out.stderr
    assert "Adopt monotonic widgets" in out.stdout and "meet:spark:2026-10-07" in out.stdout


def test_people_validator_flags_shared_names_and_missing_roster_names(kb_root):
    setup_votes(kb_root)
    (kb_root / "data" / "aliases.yaml").write_text(
        "people:\n  ada: {names: [Ada Example, Ted Shared]}\n  bob: {names: [Bob Example]}\n  cy: {names: [Cy Example, Ted Shared]}\n"
        "  eve: {names: [Eve E.]}\n")
    problems = people.check(kb_root)
    assert any("'ted shared' is listed under ada, cy" in p for p in problems)
    assert any("eve" in p and "Eve Example" in p for p in problems)
    assert len(problems) == 2
