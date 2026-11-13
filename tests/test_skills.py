"""Checks from Anthropic's skill-building guide: naming, frontmatter, description, folder contents."""
import re
from pathlib import Path

import pytest
import yaml

SKILLS = sorted((Path(__file__).resolve().parents[1] / ".claude" / "skills").iterdir())


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_skill_follows_the_guide(skill):
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", skill.name), "folder name must be kebab-case"
    assert (skill / "SKILL.md").exists(), "SKILL.md must exist with exactly this spelling"
    assert not (skill / "README.md").exists(), "no README.md inside a skill folder"
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    assert match, "YAML frontmatter with --- delimiters"
    meta = yaml.safe_load(match.group(1))
    assert meta["name"] == skill.name, "name must match the folder"
    assert not re.search(r"claude|anthropic", meta["name"]), "reserved words in name"
    desc = meta["description"]
    assert 80 <= len(desc) <= 1024
    assert re.search(r"\bUse (when|before|it)\b", desc), "description must say when to use the skill"
    assert "<" not in text and ">" not in text, "no angle brackets in SKILL.md"
    assert meta.get("license") and meta.get("metadata", {}).get("version")
    assert len(meta.get("compatibility", "")) <= 500
    for section in ("## Troubleshooting",):
        assert section in text
    for ref in re.findall(r"`(references/[\w.-]+)`", text):
        assert (skill / ref).exists(), f"{ref} is linked but missing"


def test_kb_script_uses_only_the_standard_library():
    script = (SKILLS[0].parent / "iceberg-context" / "scripts" / "kb").read_text()
    imports = set(re.findall(r"^(?:import|from) ([a-z_0-9]+)", script, re.M))
    assert imports <= {"__future__", "argparse", "datetime", "hashlib", "json", "os", "re", "sqlite3", "subprocess", "sys", "pathlib"}
