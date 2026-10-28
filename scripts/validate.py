"""Dependency-free public skill/package hygiene checks; not a behavioral eval."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = set(json.loads((ROOT / "tools.json").read_text())["tools"])


def validate(root=ROOT):
    skills = root / "skills"
    names = set()
    for folder in sorted(skills.iterdir()):
        assert folder.is_dir() and not folder.is_symlink(), f"Invalid skill directory: {folder.name}"
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name), folder.name
        path = folder / "SKILL.md"
        text = path.read_text()
        front = re.match(r"\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", text)
        assert front and front[1] == folder.name and len(front[2]) <= 1024, path
        assert len(text) < 20000, f"Move conditional detail into references: {path}"
        # The nonexistent example in the channel skill is explicitly a prohibition.
        mentioned = set(re.findall(r"`(wisepim_[a-z_]+)`", text))
        prohibited_examples = {"wisepim_check_channel_readiness"} if folder.name == "channel-readiness-review" else set()
        assert mentioned <= TOOLS | prohibited_examples, mentioned - TOOLS - prohibited_examples
        for entry in folder.rglob("*"):
            assert not entry.is_symlink(), f"Symlink disallowed: {entry}"
            if entry.is_file():
                assert entry.suffix == ".md" or entry.name == "openai.yaml", entry
                assert entry.stat().st_size <= 100000, entry
        names.add(folder.name)
    scenarios = json.loads((root / "evals/scenarios.json").read_text())["scenarios"]
    assert len({s["id"] for s in scenarios}) == len(scenarios), "Duplicate scenario IDs"
    assert {s["skill"] for s in scenarios} == names, "Every skill needs evaluation coverage"
    for scenario in scenarios:
        assert scenario["prompt"] and scenario["expected"] and scenario["forbidden"], scenario["id"]
    print(f"Validated {len(names)} skills and {len(scenarios)} synthetic scenarios (static only).")


if __name__ == "__main__":
    validate()
