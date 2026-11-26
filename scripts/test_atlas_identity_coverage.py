"""Small completeness/mapping regressions; no released code is imported."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from atlas_identities import IdentityError, canonical_sha256
from atlas_identity_coverage import validate_current_coverage


class CurrentCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="atlas-id-coverage-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write("catalog/atlas-identity-history.json", {"entities": []})
        self.problems = [{"id": x, "name": {"ja": x, "en": x}, "evidence": []} for x in ["p", "q"]]
        self.entities = {}
        for number, problem in enumerate(self.problems, 1):
            identifier = f"NMA-P-{number:06d}"
            path = f"catalog/identity-snapshots/{identifier}/00.json"
            self.write(path, problem)
            self.entities[identifier] = self.entity(identifier, "problem", [problem["id"]], [
                self.rev("00", [], [], [{"role": "problem", "path": path, "pointer": "",
                                        "sha256": canonical_sha256(problem)}])])
        self.sources = []
        for key, unit, suffix in [("a", "shared", "00"), ("b", "shared", "01"), ("d", "diagnostic", "00")]:
            bindings = [self.binding("source", f"data/{key}.py"),
                        self.binding("source-manifest", f"data/{key}.json")]
            self.sources.append({"unit_key": unit, "edition": key, "kind": "standalone",
                                 "root": f"data/{key}", "source_manifest": bindings[1],
                                 "archive": None, "bindings": bindings})
        self.entities["NMA-S-000001"] = self.entity("NMA-S-000001", "source", ["data/a.py", "data/b.py"], [
            self.rev("00", ["NMA-P-000001@00"], [], self.sources[0]["bindings"]),
            self.rev("01", [], [], self.sources[1]["bindings"])])
        self.entities["NMA-S-000002"] = self.entity("NMA-S-000002", "source", ["data/d.py"], [
            self.rev("00", [], [], self.sources[2]["bindings"])])
        self.cases = []
        for number, (alias, problems, source) in enumerate([
                ("case-p", ["p"], self.sources[0]), ("case-q", ["q"], self.sources[0]),
                ("diagnostic", [], self.sources[2])], 1):
            bindings = [self.binding("case-definition", f"data/{alias}.json"),
                        self.binding("input", f"data/{alias}-input.json")]
            row = {"legacy_id": alias, "domain": "supplement", "problem_ids": problems,
                   "source_manifest": source["source_manifest"]["path"], "source_archive": None,
                   "bindings_draft": bindings}
            self.cases.append(row)
            source_ref = "NMA-S-000002@00" if not problems else "NMA-S-000001@00"
            prefs = [f"NMA-P-{1 if x == 'p' else 2:06d}@00" for x in problems]
            identifier = f"NMA-C-{number:06d}"
            self.entities[identifier] = self.entity(identifier, "case", [alias], [
                self.rev("00", prefs, [source_ref], bindings)])

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def binding(self, role, path):
        return {"role": role, "path": path, "sha256": "1" * 64}

    def rev(self, revision, problems, sources, bindings):
        return {"revision": revision, "label": {"ja": "x", "en": "x"},
                "problem_refs": problems, "source_refs": sources, "bindings": copy.deepcopy(bindings)}

    def entity(self, identifier, kind, aliases, revisions):
        return {"id": identifier, "kind": kind, "legacy_ids": aliases,
                "current_revision": revisions[-1]["revision"], "revisions": revisions}

    def run_coverage(self):
        snapshots = {f"{e['id']}@{r['revision']}": r for e in self.entities.values() for r in e["revisions"]}
        with patch("atlas_identity_coverage.inventory", return_value=(self.problems, self.cases, self.sources)), \
             patch("atlas_identity_coverage._frozen_pilot", return_value={}), \
             patch("atlas_identity_coverage._source_revision_rules", return_value={"shared": {"a": "00", "b": "01"}}), \
             patch("atlas_identity_sources.source_contract", return_value={"root": "data", "files": {},
                   "archive_path": None, "archive_members": {}, "kind": "standalone"}), \
             patch("atlas_identity_cases.case_bindings", side_effect=lambda root, row, identifier, revision: row["bindings_draft"]):
            return validate_current_coverage(self.root, {}, self.entities, snapshots)

    def reject(self, message):
        with self.assertRaisesRegex(IdentityError, message):
            self.run_coverage()

    def test_complete_diagnostics_frozen_summary_and_older_active_source(self):
        report = self.run_coverage()["report"]
        self.assertEqual(report["canonical_problems"], 2)
        self.assertEqual(report["registered_cases"], 3)
        self.assertEqual(report["source_units"], 2)
        self.assertEqual(report["active_source_revisions"], 3)
        self.assertEqual(report["unarchived_source_units"], 2)
        self.assertEqual(report["diagnostic_cases_without_problem"], ["diagnostic"])

    def test_missing_problem(self):
        del self.entities["NMA-P-000002"]
        self.reject("problem identity coverage")

    def test_merged_problems(self):
        self.entities["NMA-P-000001"]["legacy_ids"].append("q")
        self.reject("merges canonical")

    def test_missing_diagnostic_case(self):
        del self.entities["NMA-C-000003"]
        self.reject("case identity coverage")

    def test_fabricated_problem_for_diagnostic(self):
        self.entities["NMA-C-000003"]["revisions"][0]["problem_refs"] = ["NMA-P-000001@00"]
        self.reject("unrelated problem")

    def test_extra_unrelated_case_problem(self):
        self.entities["NMA-C-000001"]["revisions"][0]["problem_refs"].append("NMA-P-000002@00")
        self.reject("unrelated problem")

    def test_extra_case_source(self):
        self.entities["NMA-C-000001"]["revisions"][0]["source_refs"].append("NMA-S-000002@00")
        self.reject("additional source")

    def test_latest_source_cannot_replace_exact_older_release(self):
        self.entities["NMA-C-000001"]["revisions"][0]["source_refs"] = ["NMA-S-000001@01"]
        self.reject("wrong or additional source")

    def test_missing_active_source_state(self):
        self.entities["NMA-S-000001"]["revisions"].pop()
        self.entities["NMA-S-000001"]["current_revision"] = "00"
        self.entities["NMA-S-000001"]["legacy_ids"] = ["data/a.py"]
        self.reject("source identity coverage")

    def test_duplicate_source_state(self):
        self.entities["NMA-S-000003"] = copy.deepcopy(self.entities["NMA-S-000001"])
        self.entities["NMA-S-000003"]["id"] = "NMA-S-000003"
        self.reject("assigned more than once")

    def test_incomplete_source_bindings(self):
        self.entities["NMA-S-000001"]["revisions"][0]["bindings"].pop(0)
        self.reject("source bindings")

    def test_unrelated_source_problem(self):
        self.entities["NMA-S-000002"]["revisions"][0]["problem_refs"] = ["NMA-P-000002@00"]
        self.reject("unrelated problem")

    def test_missing_case_binding(self):
        self.entities["NMA-C-000001"]["revisions"][0]["bindings"].pop()
        self.reject("case has incomplete")

    def test_problem_snapshot_drift(self):
        self.write("catalog/identity-snapshots/NMA-P-000001/00.json", {"id": "p", "changed": True})
        self.reject("differs from its frozen")

    def test_unknown_additional_case(self):
        extra = copy.deepcopy(self.entities["NMA-C-000001"])
        extra["id"] = "NMA-C-000004"
        extra["legacy_ids"] = ["unknown"]
        self.entities[extra["id"]] = extra
        self.reject("case identity coverage")

    def test_fabricated_source_alias(self):
        self.entities["NMA-S-000001"]["legacy_ids"] = ["invented-package"]
        self.reject("existing published paths")

    def test_unfrozen_noncurrent_source_state_is_not_history(self):
        item = self.entities["NMA-S-000001"]
        item["revisions"].append(self.rev("02", [], [], [
            self.binding("source", "data/unknown.py"),
            self.binding("source-manifest", "data/unknown.json")]))
        item["current_revision"] = "02"
        self.reject("unfrozen historical source")

    def test_reviewed_common_source_revision_order_cannot_be_swapped(self):
        item = self.entities["NMA-S-000001"]
        first, second = item["revisions"]
        first["problem_refs"] = second["problem_refs"] = []
        first["bindings"], second["bindings"] = second["bindings"], first["bindings"]
        self.reject("known source edition has wrong identity revision")

    def test_known_frozen_source_state_can_be_retained_on_append(self):
        item = self.entities["NMA-S-000002"]
        old = self.rev("00", [], [], [self.binding("source", "data/old.py"),
                                      self.binding("source-manifest", "data/old.json")])
        item["revisions"][0]["revision"] = "01"
        item["revisions"].insert(0, old)
        item["current_revision"] = "01"
        item["legacy_ids"].append("data/old.py")
        self.entities["NMA-C-000003"]["revisions"][0]["source_refs"] = ["NMA-S-000002@01"]
        with patch("atlas_identity_coverage._frozen_source_states", return_value={"NMA-S-000002@00": old}):
            self.assertTrue(self.run_coverage()["report"]["complete_current_inventory"])


if __name__ == "__main__":
    unittest.main()
