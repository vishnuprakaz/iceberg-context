import json

from icekb import frontmatter, state
from icekb.integrate import index
from icekb.validate import pages, privacy


def test_generated_block_keeps_human_text():
    body = "# T\n\n<!-- kb:generated:start -->\nold\n<!-- kb:generated:end -->\n\n## Notes\nkeep me\n"
    out = frontmatter.set_generated(body, "new text")
    assert "new text" in out and "old" not in out and "keep me" in out
    assert frontmatter.markers_ok(out)


def test_generated_block_added_above_notes():
    out = frontmatter.set_generated("# T\n\n## Notes\nmine\n", "gen")
    assert out.index("gen") < out.index("## Notes") and "mine" in out


def test_frontmatter_roundtrip():
    text = frontmatter.dump({"id": "person/x", "type": "person", "title": "X"}, "# X\n")
    meta, body = frontmatter.parse(text)
    assert meta["id"] == "person/x" and body.strip() == "# X"


def test_valid_pages_pass(kb_root):
    assert pages.check(kb_root) == []


def test_broken_link_and_schema_are_reported(kb_root):
    (kb_root / "kb" / "people" / "bob.md").write_text(
        "---\nid: person/bob\ntype: person\ntitle: Bob\n"
        "links:\n- {rel: reviews, to: module/nope, confidence: extracted}\n---\nbody\n"
    )
    problems = "\n".join(pages.check(kb_root))
    assert "'login' is a required property" in problems
    assert "module/nope" in problems
    assert "source" in problems  # extracted links must cite a source


def test_person_page_rejects_personal_fields(kb_root):
    (kb_root / "kb" / "people" / "eve.md").write_text(
        "---\nid: person/eve\ntype: person\ntitle: Eve\nlogin: eve\nlocation: somewhere\n---\nbody\n"
    )
    assert any("eve.md" in p for p in pages.check(kb_root))


def test_privacy_lint():
    address = "someone" + "@" + "corp.io"  # built at runtime so this file passes the lint itself
    assert privacy.find_emails(f"write to {address} now") == [address]
    assert privacy.find_emails("the list is dev@iceberg.apache.org; x@users.noreply.github.com") == []


def test_index_build_and_check(kb_root):
    assert index.write(kb_root, check_only=True) is False
    index.write(kb_root)
    nodes = [json.loads(line) for line in (kb_root / "kb" / "index" / "nodes.jsonl").read_text().splitlines()]
    edges = [json.loads(line) for line in (kb_root / "kb" / "index" / "edges.jsonl").read_text().splitlines()]
    assert {n["id"] for n in nodes} == {"person/ada", "initiative/widgets"}
    assert edges == [{"src": "person/ada", "rel": "champions", "to": "initiative/widgets", "confidence": "observed"}]
    assert index.write(kb_root, check_only=True) is True


def test_state_roundtrip(kb_root):
    state.save(kb_root, "devlist", ok=True, counts={"messages": 3}, cursor="2026-11")
    st = state.save(kb_root, "devlist", ok=False, error="boom")
    assert st["status"] == "failed" and st["cursor"] == "2026-11" and st["counts"] == {"messages": 3}
    assert st["last_success"] and st["error"] == "boom"
