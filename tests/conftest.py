import shutil
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture
def kb_root(tmp_path, monkeypatch):
    """A tiny, self-contained knowledge base."""
    (tmp_path / "schema").mkdir()
    shutil.copy(REPO / "schema" / "page.json", tmp_path / "schema" / "page.json")
    (tmp_path / "people").mkdir()
    (tmp_path / "initiatives").mkdir()
    (tmp_path / "people" / "ada.md").write_text(
        "---\nid: person/ada\ntype: person\ntitle: Ada Example\nlogin: ada\n"
        "links:\n- {rel: champions, to: initiative/widgets, confidence: observed}\n---\n"
        "# Ada Example\n\n<!-- kb:generated:start -->\nold\n<!-- kb:generated:end -->\n\n## Notes\nkeep me\n"
    )
    (tmp_path / "initiatives" / "widgets.md").write_text(
        "---\nid: initiative/widgets\ntype: initiative\ntitle: Widgets\nstatus: design\n---\n# Widgets\n\nSnapshot timestamps.\n"
    )
    raw = tmp_path / "data" / "raw" / "devlist" / "2026"
    raw.mkdir(parents=True)
    (raw / "11.jsonl").write_text(
        '{"id": "devlist:<m1>", "source": "devlist", "type": "email", "date": "2026-11-02T10:00:00Z", '
        '"url": "https://lists.apache.org/thread/abc", "people": ["ada"], "title": "[VOTE] Widgets for v4", '
        '"body": "I propose we adopt monotonic widgets. Please vote.", "refs": [], "hash": "x"}\n'
    )
    (tmp_path / "people" / "aliases.yaml").write_text("people: {}\n")
    monkeypatch.setenv("ICEBERG_CONTEXT_ROOT", str(tmp_path))
    monkeypatch.setenv("XDG_CACHE_HOME", str(tmp_path / ".cache"))
    return tmp_path
