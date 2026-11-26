"""Finite saved-metadata fixtures for fixed-case identity adapters."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from atlas_identity_cases import (
    CaseInventoryError, case_bindings, case_inventory, common_row_from_snapshot,
    validate_common_verification,
)

ORIGIN = "https://hrkoyama.github.io/"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False).encode())


class CommonFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.base = "code/example/2026-11-27"
        self.manifest_path = self.base + "/source-manifest.json"
        self.archive_path = self.base + "/example.zip"
        self.receipt_path = "numerical-methods-atlas/code-and-data/verification/2026-11-27.json"
        self.acquisition_path = "code/example/verification-candidates/2026-11-27.json"
        self.inputs = self.put(self.base + "/input.json", {"parameter": 1, "acceptance": {"error": 1e-9}})
        self.result = self.put(self.base + "/result.json", {"value": 1, "failure": {"ok": False}})
        self.manifest = {"files": {"input.json": sha(self.inputs), "result.json": sha(self.result)}}
        manifest_raw = self.put(self.manifest_path, self.manifest)
        archive_file = self.root / self.archive_path
        with zipfile.ZipFile(archive_file, "w") as archive:
            archive.writestr("example/input.json", self.inputs)
            archive.writestr("example/result.json", self.result)
            archive.writestr("example/source-manifest.json", manifest_raw)
        archive_hash = sha(archive_file.read_bytes())
        self.rule = {"id": "value", "pointer": "/value", "comparison": "equals", "expected": 1,
                     "description": {"ja": "value", "en": "value"}}
        self.expected_failure = {"id": "must-fail", "pointer": "/failure", "field": "ok",
                                 "comparison": "equals", "expected": False,
                                 "description": {"ja": "failure", "en": "failure"}}
        self.definition = {
            "id": "example", "name": {"ja": "example", "en": "example"}, "problem_id": "problem",
            "release": {"family": "example", "version": "2026-11-27",
                        "download": ORIGIN + self.archive_path, "sha256": archive_hash,
                        "manifest": ORIGIN + self.manifest_path, "manifest_sha256": sha(manifest_raw),
                        "archive_directory": "example"},
            "execution_group": "example", "shared_runner_cases": ["example"],
            "inputs": {"url": ORIGIN + self.base + "/input.json", "sha256": sha(self.inputs),
                       "path": "input.json"},
            "outputs": [{"id": "results", "url": ORIGIN + self.base + "/result.json",
                         "sha256": sha(self.result), "path": "result.json", "generated_path": "result.json"}],
            "checks": [self.rule], "expected_failures": [self.expected_failure], "references": [],
        }
        registry = {"verification_receipt": ORIGIN + self.receipt_path,
                    "examples": [self.definition]}
        registry_raw = self.put(self.acquisition_path, registry)
        self.put("numerical-methods-atlas/code-and-data/examples.json", registry)
        self.put("catalog/atlas-execution-examples.json", {"examples": [self.definition]})
        self.put("catalog/atlas-test-problems.json", {"problems": [{"id": "problem"}]})
        self.put("catalog/atlas-depth-expansion.json", {"case_problem_ids": {}})
        self.put("numerical-methods-atlas/validation/releases.json", {"releases": []})
        execution = {"group": "example", "started": True, "completed": True, "exit_code": 0,
                     "timed_out": False, "shared_runner_cases": ["example"]}
        numerical = {k: v for k, v in self.rule.items() if k != "description"}
        numerical.update(observed=1, passed=True)
        expected_failure = {k: v for k, v in self.expected_failure.items() if k != "description"}
        expected_failure.update(observed=False, passed=True)
        output = {"id": "output-results", "passed": True, "comparison": "nonempty_artifact",
                  "generated_path": "result.json", "bytes": 42, "sha256": "f" * 64}
        self.receipt = {
            "passed": True, "status": "complete",
            "registry_url": ORIGIN + "numerical-methods-atlas/code-and-data/examples.json",
            "registry_acquisition_url": ORIGIN + self.acquisition_path,
            "registry_sha256": sha(registry_raw), "expected_registry_sha256": sha(registry_raw),
            "examples": [{"id": "example", "problem_id": "problem", "passed": True,
                          "execution": deepcopy(execution),
                          "validation": {"passed": True, "checks": [numerical, output],
                                         "expected_failures": [expected_failure]}}],
            "releases": [{**self.definition["release"], "archive_bytes": archive_file.stat().st_size,
                          "archived_files_verified": len(self.manifest["files"]),
                          "execution": deepcopy(execution), "setup": {"passed": True, "phase": "complete"},
                          "downloaded_artifacts": [
                              {"url": ORIGIN + self.base + "/input.json", "sha256": sha(self.inputs),
                               "bytes": len(self.inputs)},
                              {"url": ORIGIN + self.base + "/result.json", "sha256": sha(self.result),
                               "bytes": len(self.result)}]}],
        }
        self.put(self.receipt_path, self.receipt)
        self.row = case_inventory(self.root)[0]
        self.contract = {"manifest_path": self.manifest_path, "manifest_sha256": sha(manifest_raw),
                         "archive_path": self.archive_path, "archive_sha256": archive_hash}

    def put(self, relative, value):
        raw = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False).encode() + b"\n"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return raw

    def validate(self):
        return validate_common_verification(self.root, self.row, self.contract)

    def save_receipt(self):
        self.put(self.receipt_path, self.receipt)

    def supplement(self, inputs, *, wanted=None):
        base = "code/validated-examples/2026-11-27/supplement"
        selected = inputs.get("cases", {}).get("supplement", inputs.get("a"))
        if wanted is None:
            wanted = sha(json.dumps(selected, sort_keys=True).encode())
        definitions = [{"id": "supplement", "title": {"ja": "supplement", "en": "supplement"},
                        "validation": {"ja": "saved comparison", "en": "saved comparison"}}]
        payload = {"inputs.json": self.put(base + "/inputs.json", inputs),
                   "cases.json": self.put(base + "/cases.json", definitions),
                   "results/result.json": self.put(base + "/results/result.json",
                                                   {"cases": [{"id": "supplement", "input_sha256": wanted}]})}
        manifest = self.put(base + "/source-manifest.json",
                            {"files": {name: sha(raw) for name, raw in payload.items()}})
        archive_path = self.root / base / "supplement.zip"
        with zipfile.ZipFile(archive_path, "w") as archive:
            for name, raw in payload.items():
                archive.writestr("supplement/" + name, raw)
            archive.writestr("supplement/source-manifest.json", manifest)
        archive_hash = sha(archive_path.read_bytes())
        self.put(base + "/verification.json", {"passed": True, "case_ids": ["supplement"],
                                               "source_manifest_sha256": sha(manifest),
                                               "archive_sha256": archive_hash})
        self.put("catalog/atlas-depth-expansion.json", {"case_problem_ids": {"supplement": "problem"}})
        self.put("numerical-methods-atlas/validation/releases.json", {"releases": [{
            "group": "supplement", "base": ORIGIN + base + "/", "archive": "supplement.zip",
            "case_ids": ["supplement"], "manifest_sha256": sha(manifest),
            "archive_sha256": archive_hash,
        }]})
        return next(row for row in case_inventory(self.root) if row["domain"] == "supplement")

    def test_valid_receipt_preserves_original_nonempty_output_semantics(self):
        self.assertNotEqual(self.definition["outputs"][0]["sha256"],
                            self.receipt["examples"][0]["validation"]["checks"][-1]["sha256"])
        self.assertTrue(self.validate()["passed"])

    def test_common_metadata_is_frozen_without_live_catalog_offsets(self):
        bindings = case_bindings(self.root, self.row, "NMA-C-000004")
        metadata = [b for b in bindings if b["path"].startswith("catalog/")]
        self.assertEqual({b["path"] for b in metadata},
                         {"catalog/identity-snapshots/NMA-C-000004/00.json"})
        self.assertEqual({b["pointer"] for b in metadata},
                         {"", "/checks", "/expected_failures", "/references"})
        self.assertEqual(next(b["sha256"] for b in metadata if b["pointer"] == ""),
                         canonical(self.definition))

    def test_historical_snapshot_does_not_read_changed_live_registry(self):
        original = case_bindings(self.root, self.row, "NMA-C-000004")
        self.put("catalog/atlas-execution-examples.json", {"examples": []})
        self.put("numerical-methods-atlas/code-and-data/examples.json", {"examples": []})
        historical = common_row_from_snapshot(
            self.root, self.definition, self.receipt_path,
            snapshot_path="catalog/identity-snapshots/NMA-C-000004/00.json")
        self.assertEqual(case_bindings(self.root, historical, "NMA-C-000004"), original)
        self.assertTrue(validate_common_verification(self.root, historical, self.contract)["passed"])

    def test_duplicate_common_identity_is_rejected(self):
        registry = {"verification_receipt": ORIGIN + self.receipt_path,
                    "examples": [self.definition, self.definition]}
        self.put("catalog/atlas-execution-examples.json", {"examples": registry["examples"]})
        self.put("numerical-methods-atlas/code-and-data/examples.json", registry)
        with self.assertRaises(CaseInventoryError):
            case_inventory(self.root)

    def test_wrong_source_contract_is_rejected(self):
        self.contract["archive_sha256"] = "0" * 64
        with self.assertRaisesRegex(CaseInventoryError, "source contract"):
            self.validate()

    def test_changed_manifest_bytes_are_rejected(self):
        self.put(self.manifest_path, {"files": {}})
        with self.assertRaisesRegex(CaseInventoryError, "source bytes"):
            self.validate()

    def test_changed_frozen_criterion_is_rejected(self):
        self.row["canonical_definition"]["checks"][0]["expected"] = 2
        with self.assertRaisesRegex(CaseInventoryError, "frozen definition"):
            self.validate()

    def test_missing_saved_case_is_rejected(self):
        self.receipt["examples"] = []
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "cover"):
            self.validate()

    def test_true_flag_cannot_hide_a_different_recorded_criterion(self):
        self.receipt["examples"][0]["validation"]["checks"][0]["expected"] = 2
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "criterion"):
            self.validate()

    def test_wrong_saved_release_hash_is_rejected(self):
        self.receipt["releases"][0]["sha256"] = "0" * 64
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "release hashes"):
            self.validate()

    def test_timed_out_saved_execution_is_rejected(self):
        self.receipt["examples"][0]["execution"]["timed_out"] = True
        self.receipt["releases"][0]["execution"]["timed_out"] = True
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "execution"):
            self.validate()

    def test_failed_expected_failure_check_is_not_reclassified_as_success(self):
        self.receipt["examples"][0]["validation"]["expected_failures"][0]["passed"] = False
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "criterion"):
            self.validate()

    def test_empty_generated_output_is_rejected(self):
        self.receipt["examples"][0]["validation"]["checks"][-1]["bytes"] = 0
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "generated output"):
            self.validate()

    def test_wrong_downloaded_source_artifact_is_rejected(self):
        self.receipt["releases"][0]["downloaded_artifacts"][0]["sha256"] = "0" * 64
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "downloaded artifact"):
            self.validate()

    def test_external_registry_acquisition_url_is_rejected(self):
        self.receipt["registry_acquisition_url"] = "https://example.invalid/registry.json"
        self.save_receipt()
        with self.assertRaisesRegex(CaseInventoryError, "HR URL"):
            self.validate()

    def test_saved_case_input_hash_adds_exact_selector_without_dropping_whole_file(self):
        row = self.supplement({"cases": {"supplement": {"steps": 4, "acceptance": {"error": 1e-9}}}})
        inputs = [item for item in row["bindings_draft"] if item["role"] == "input"]
        self.assertEqual([item.get("pointer") for item in inputs], [None, "/cases/supplement"])
        self.assertEqual(row["saved_input_selector"], "/cases/supplement")

    def test_saved_case_input_hash_with_no_exact_object_is_rejected(self):
        with self.assertRaisesRegex(CaseInventoryError, "no exact immutable input selector"):
            self.supplement({"cases": {"supplement": {"steps": 4}}}, wanted="0" * 64)

    def test_identical_input_object_aliases_have_a_deterministic_exact_selector(self):
        configuration = {"steps": 4, "acceptance": {"error": 1e-9}}
        row = self.supplement({"b": configuration, "a": configuration})
        self.assertEqual(row["saved_input_selector"], "/a")


class PublishedInventory(unittest.TestCase):
    def test_current_registered_domains_and_diagnostics_match_their_authorities(self):
        root = Path(__file__).resolve().parents[1]
        expansion = json.loads((root / "catalog/atlas-depth-expansion.json").read_bytes())["case_problem_ids"]
        common = json.loads((root / "catalog/atlas-execution-examples.json").read_bytes())["examples"]
        rows = case_inventory(root)
        self.assertEqual({x["legacy_id"] for x in rows},
                         set(expansion) | {x["id"] for x in common})
        for row in rows:
            if row["domain"] == "supplement":
                self.assertEqual(row["problem_ids"],
                                 [] if expansion[row["legacy_id"]] is None else [expansion[row["legacy_id"]]])


if __name__ == "__main__":
    unittest.main()
