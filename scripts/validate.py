"""Dependency-free public skill/package hygiene checks; not a behavioral eval."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOB_FAMILIES = {"gap_filling", "missing_image_retrieval", "category_mapping", "ads_preparation", "supplier_completion"}
EXECUTION_TOOLS = {"wisepim_" + name for name in (
    "apply_product_edits", "apply_project_settings", "apply_prompt_edits",
    "start_enrichment", "start_translation", "apply_bulk_update", "start_web_research",
)} | {"wisepim_start_" + family for family in JOB_FAMILIES}
RETIRED_TOOLS = {"wisepim_apply_changes", "wisepim_list_catalog_job_kinds", "wisepim_estimate_catalog_job", "wisepim_preview_catalog_job"}


def validate_tool_contract(root):
    declared = json.loads((root / "tools.json").read_text())["tools"]
    tools = set(declared)
    assert len(tools) == len(declared), "Duplicate declared tool"
    assert not tools & RETIRED_TOOLS, "Retired dispatcher/discovery tool remains declared"
    required = EXECUTION_TOOLS | {"wisepim_" + verb + "_" + family for family in JOB_FAMILIES for verb in ("estimate", "preview")}
    assert required <= tools, f"Missing explicit workflow tool: {sorted(required - tools)}"
    assert len(tools) == 53, f"Expected 53 declared tools, got {len(tools)}"
    return tools


def validate(root=ROOT):
    tools = validate_tool_contract(root)
    skills = root / "skills"
    names = set()
    for folder in sorted(skills.iterdir()):
        assert folder.is_dir() and not folder.is_symlink(), f"Invalid skill directory: {folder.name}"
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name), folder.name
        path = folder / "SKILL.md"
        text = path.read_text()
        assert not re.search(r"\b(?:WisePIM|Wisepim)\b", text), f"Use WISEPIM branding: {path}"
        front = re.match(r"\A---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", text)
        assert front and front[1] == folder.name and len(front[2]) <= 1024, path
        assert len(text) < 20000, f"Move conditional detail into references: {path}"
        # The nonexistent example in the channel skill is explicitly a prohibition.
        mentioned = set(re.findall(r"`(wisepim_[a-z_]+)`", text))
        prohibited_examples = {"wisepim_check_channel_readiness"} if folder.name == "channel-readiness-review" else set()
        assert mentioned <= tools | prohibited_examples, mentioned - tools - prohibited_examples
        for entry in folder.rglob("*"):
            assert not entry.is_symlink(), f"Symlink disallowed: {entry}"
            if entry.is_file():
                assert entry.suffix == ".md" or entry.name == "openai.yaml", entry
                assert entry.stat().st_size <= 100000, entry
                assert not re.search(r"\b(?:WisePIM|Wisepim)\b", entry.read_text()), f"Use WISEPIM branding: {entry}"
        names.add(folder.name)
    scenarios = json.loads((root / "evals/scenarios.json").read_text())["scenarios"]
    assert len({s["id"] for s in scenarios}) == len(scenarios), "Duplicate scenario IDs"
    assert {s["skill"] for s in scenarios} == names, "Every skill needs evaluation coverage"
    for scenario in scenarios:
        assert scenario["prompt"] and scenario["expected"] and scenario["forbidden"], scenario["id"]
        executor = scenario.get("fixture", {}).get("apply_tool")
        if executor is not None and not scenario.get("executor_mismatch"):
            assert executor in EXECUTION_TOOLS, f"Unknown fixture executor: {scenario['id']}"
    print(f"Validated {len(names)} skills and {len(scenarios)} synthetic scenarios (static only).")


if __name__ == "__main__":
    validate()
