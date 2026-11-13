from icekb.collectors import devlist, git, github
from icekb.identity import Identity, normalize_display
from icekb.util import extract_refs, strip_emails


def test_extract_refs():
    text = "See https://github.com/apache/iceberg/pull/17727 and #18585, apache/iceberg-python#3967, &#8217; and item #12."
    assert extract_refs(text) == ["gh:apache/iceberg#17727", "gh:apache/iceberg-python#3967", "gh:apache/iceberg#18585"]
    assert extract_refs("doc https://docs.google.com/document/d/1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw/edit") == [
        "doc:1k4x8utgh41Sn1tr98eynDKCWq035SV_f75rtNHcerVw"]


def test_strip_emails():
    address = "a.person" + "@" + "corp.io"
    assert address not in strip_emails(f"mail {address} now")


def test_normalize_display_names():
    assert normalize_display('"Jones, Danny via dev"') == "Danny Jones"
    assert normalize_display("Kevin Liu via dev") == "Kevin Liu"
    assert normalize_display("Sam Example (ACME)") == "Sam Example"


def test_identity_resolves_and_records_unknown(kb_root):
    (kb_root / "data" / "aliases.yaml").write_text(
        "people:\n  ada:\n    names: [Ada Example, Ada Exämple]\n    asf_id: adae\n")
    ident = Identity(kb_root)
    assert ident.person("Example, Ada via dev") == "ada"
    assert ident.person("Ada Example") == "ada"
    assert ident.person("Nobody Known") == "name:Nobody Known"
    assert ident.unresolved == {"Nobody Known": 1}
    assert ident.by_asf["adae"] == "ada"


def test_devlist_classify():
    assert devlist.classify("Re: [VOTE] Release Apache Iceberg 1.12.0 RC2") == "release-vote"
    assert devlist.classify("[VOTE] Add File type to the v4 spec") == "vote"
    assert devlist.classify("[RESULT][VOTE] Default Value Expressions for v4") == "result"
    assert devlist.classify("[Discuss] Deprecate result type handling") == "discuss"
    assert devlist.classify("Question about result type") == "other"
    assert devlist.classify("[ANNOUNCE] Apache Iceberg 1.12.0") == "announce"


def test_devlist_own_text_drops_quotes_and_signature():
    body = "I agree.\n\nOn Mon, 2 Nov 2026 at 10:00, Someone wrote:\n> old text\n> more\nOne more point.\n-- \nSig line\n"
    assert devlist.own_text(body).strip() == "I agree.\n\nOne more point."


def test_git_parse_log(kb_root):
    (kb_root / "data" / "aliases.yaml").write_text("people:\n  ada:\n    names: [Ada Example]\n")
    log = ("\x1eabc123def4567890\x1f2026-11-12T22:53:41-08:00\x1fAda Example\x1fCore: Fix thing (#18899)\n\n"
           "core/src/main/java/A.java\ncore/src/test/java/TestA.java\n")
    (rec,) = git.parse_log(log, "apache/iceberg", Identity(kb_root))
    assert rec["id"] == "commit:apache/iceberg@abc123def456"
    assert rec["date"] == "2026-11-13T06:53:41Z"
    assert rec["people"] == ["ada"] and rec["refs"] == ["gh:apache/iceberg#18899"]
    assert rec["meta"]["pr"] == 18899 and rec["meta"]["files"] == ["core/src/main/java/A.java", "core/src/test/java/TestA.java"]


def test_git_split_markdown_and_openapi():
    md = "# Spec\nintro text\n## Snapshots\nbody a\n```\n# not a heading\n```\n### Timestamps\nbody b\n"
    assert [t for t, _ in git.split_markdown(md)] == ["Spec", "Spec > Snapshots", "Spec > Snapshots > Timestamps"]
    yml = "openapi: 3\npaths:\n  /v1/config:\n    get: x\n  /v1/tables:\n    post: y\ncomponents:\n  schemas:\n    Table:\n      type: object\n"
    assert [t for t, _ in git.split_openapi(yml)] == ["(header)", "/v1/config", "/v1/tables", "Table"]


def _pr_node(number, updated):
    return {"__typename": "PullRequest", "number": number, "title": f"Core: change {number}", "bodyText": "Fixes #17000",
            "state": "MERGED", "isDraft": False, "merged": True, "mergedAt": updated, "closedAt": updated,
            "createdAt": "2026-10-01T00:00:00Z", "updatedAt": updated, "url": f"https://github.com/apache/iceberg/pull/{number}",
            "baseRefName": "main", "additions": 5, "deletions": 1, "changedFiles": 1, "author": {"login": "ada"},
            "mergedBy": {"login": "bob"}, "milestone": None, "labels": {"nodes": [{"name": "core"}]},
            "comments": {"totalCount": 2}, "reviewThreads": {"totalCount": 1}, "reactions": {"totalCount": 0},
            "files": {"nodes": [{"path": "core/A.java"}]},
            "reviews": {"nodes": [{"author": {"login": "bob"}, "state": "APPROVED", "submittedAt": updated},
                                  {"author": {"login": "copilot[bot]"}, "state": "COMMENTED", "submittedAt": updated}]},
            "closingIssuesReferences": {"nodes": []}}


def test_github_item_record():
    rec = github.item_record("apache/iceberg", _pr_node(18000, "2026-11-01T00:00:00Z"))
    assert rec["id"] == "gh:apache/iceberg#18000" and rec["type"] == "pr"
    assert rec["meta"]["state"] == "merged" and rec["meta"]["merged_by"] == "bob" and rec["meta"]["comments"] == 3
    assert rec["meta"]["reviews"] == [{"by": "bob", "state": "APPROVED", "at": "2026-11-01T00:00:00Z"}]
    assert rec["refs"] == ["gh:apache/iceberg#17000"]


def test_github_items_walk_by_update_time(kb_root):
    pages = [[_pr_node(1, "2026-11-01T00:00:00Z"), _pr_node(2, "2026-11-02T00:00:00Z")], [_pr_node(3, "2026-11-03T00:00:00Z")]]
    seen = []

    class Fake:
        def graphql(self, _query, variables):
            seen.append(variables["q"])
            nodes = pages.pop(0)
            return {"search": {"nodes": nodes, "pageInfo": {"hasNextPage": False, "endCursor": None}}}

    cursor = {}
    assert github.collect_items(Fake(), kb_root, "apache/iceberg", "prs", cursor, page_size=2) == 3
    assert "updated:>=2014-01-01" in seen[0] and "updated:>=2026-11-02T00:00:00Z" in seen[1]
    assert cursor == {"prs_updated": "2026-11-03T00:00:00Z", "prs_caught_up": True}
    assert len((kb_root / "data/raw/github/iceberg/prs/2026/10.jsonl").read_text().splitlines()) == 3


def test_github_comment_record_filters_noise():
    base = {"id": 9, "user": {"login": "ada", "type": "User"}, "created_at": "2026-11-01T00:00:00Z", "updated_at": "2026-11-01T00:00:00Z",
            "html_url": "https://github.com/apache/iceberg/pull/18000#discussion_r9",
            "pull_request_url": "https://api.github.com/repos/apache/iceberg/pulls/18000", "path": "core/A.java"}
    rec = github.comment_record("apache/iceberg", {**base, "body": "This should use the builder pattern instead of a setter."}, "review")
    assert rec["id"] == "gh:apache/iceberg#18000/c9" and rec["refs"] == ["gh:apache/iceberg#18000"] and rec["meta"]["path"] == "core/A.java"
    assert github.comment_record("apache/iceberg", {**base, "body": "LGTM"}, "review") is None
    assert github.comment_record("apache/iceberg", {**base, "user": {"login": "dependabot[bot]", "type": "Bot"},
                                                    "body": "Bumps a dependency from one version to another."}, "issue") is None
