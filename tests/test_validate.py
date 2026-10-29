"""Static contract regression tests; no model, provider or live service calls."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("skill_validation",ROOT/"scripts/validate.py")
validation=importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for folder in ("skills","evals"):
            shutil.copytree(ROOT/folder,self.root/folder)
        shutil.copyfile(ROOT/"tools.json",self.root/"tools.json")

    def alter_tools(self,change):
        p=self.root/"tools.json";d=json.loads(p.read_text());change(d["tools"]);p.write_text(json.dumps(d))

    def test_full_explicit_contract_is_accepted(self):
        validation.validate(self.root)

    def test_retired_dispatcher_is_rejected(self):
        self.alter_tools(lambda tools:tools.append("wisepim_apply_changes"))
        with self.assertRaisesRegex(AssertionError,"Retired dispatcher"):
            validation.validate(self.root)

    def test_missing_typed_preview_is_rejected(self):
        self.alter_tools(lambda tools:tools.remove("wisepim_preview_supplier_completion"))
        with self.assertRaisesRegex(AssertionError,"Missing explicit workflow tool"):
            validation.validate(self.root)

    def test_duplicate_tool_is_rejected(self):
        self.alter_tools(lambda tools:tools.append(tools[0]))
        with self.assertRaisesRegex(AssertionError,"Duplicate declared tool"):
            validation.validate(self.root)

    def test_undeclared_tool_in_skill_is_rejected(self):
        p=self.root/"skills/run-catalog-improvement-jobs/SKILL.md"
        p.write_text(p.read_text()+"\nCall `wisepim_arbitrary_execution`.\n")
        with self.assertRaises(AssertionError):
            validation.validate(self.root)

    def test_unknown_positive_fixture_executor_is_rejected(self):
        p=self.root/"evals/scenarios.json";d=json.loads(p.read_text())
        case=next(s for s in d["scenarios"] if s["id"]=="explicit-start-translation")
        case["fixture"]["apply_tool"]="wisepim_unknown_executor"
        p.write_text(json.dumps(d))
        with self.assertRaisesRegex(AssertionError,"Unknown fixture executor"):
            validation.validate(self.root)

if __name__=="__main__":unittest.main()
