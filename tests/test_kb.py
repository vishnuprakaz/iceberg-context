import subprocess
import sys
from pathlib import Path

from icekb import index, state

KB = Path(__file__).resolve().parents[1] / ".claude" / "skills" / "iceberg-context" / "scripts" / "kb"


def kb(*args):
    return subprocess.run([sys.executable, "-I", str(KB), *args], capture_output=True, text=True)


def test_status(kb_root):
    index.write(kb_root)
    state.save(kb_root, "devlist", ok=True, counts={"messages": 1})
    out = kb("status")
    assert out.returncode == 0, out.stderr
    assert "devlist      ok" in out.stdout
    assert "person=1" in out.stdout and "devlist=1" in out.stdout
    assert "youtube      never" in out.stdout


def test_search_finds_pages_and_raw(kb_root):
    index.write(kb_root)
    out = kb("search", "monotonic widgets")
    assert "devlist:<m1>" in out.stdout and "[VOTE] Widgets for v4" in out.stdout
    out = kb("search", "snapshot", "--type", "initiative")
    assert "initiative/widgets" in out.stdout
    assert "no results" in kb("search", "zzzunknownzzz").stdout
    assert kb("search", 'odd "quote AND (').returncode == 0  # punctuation must not break the query


def test_source(kb_root):
    index.write(kb_root)
    out = kb("source", "devlist:<m1>")
    assert "https://lists.apache.org/thread/abc" in out.stdout and "Please vote" in out.stdout
    out = kb("source", "person/ada", "--grep", "keep me")
    assert "keep me" in out.stdout
    assert kb("source", "nope:1").returncode == 1


def test_index_rebuilds_when_files_change(kb_root):
    index.write(kb_root)
    assert "no results" in kb("search", "gizmo").stdout
    (kb_root / "initiatives" / "widgets.md").write_text(
        "---\nid: initiative/widgets\ntype: initiative\ntitle: Widgets\nstatus: design\n---\n# Widgets\n\nNow with gizmo.\n"
    )
    assert "initiative/widgets" in kb("search", "gizmo").stdout
