"""Small destructive fixtures for identity contracts; no scientific execution."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import stat
import types
import unittest
from unittest import mock
import zipfile

from atlas_identities import (IdentityError, canonical_sha256, file_sha256,
                              binding_key,
                              format_revision, load_json, resolve_pointer,
                              revision_number, safe_path, validate_registry)


class IdentityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="atlas-identities-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "sine"}]})
        self.write_json("data/problem-snapshot.json", {"id": "sine"})
        self.write_json("catalog/atlas-depth-expansion.json", {"case_problem_ids": {"sine-fixed": "sine"}})
        self.write_json("data/case.json", {"id": "sine-fixed", "acceptance": {"error": 1e-6}, "input": {"n": 8}, "reference": "analytic sine", "result": {"id": "sine-fixed", "passed": True}})
        self.write("data/source.py", "# numerical module is not executed\n")
        self.write("data/requirements.txt", "numpy==2.0.2\n")
        files = {name: file_sha256(self.root / "data" / name) for name in ["source.py", "requirements.txt", "case.json"]}
        self.write_json("data/source-manifest.json", {"files": files})
        with zipfile.ZipFile(self.root / "data/source.zip", "w") as archive:
            for name in files:
                archive.write(self.root / "data" / name, "release/" + name)
        self.write_json("data/verification.json", {"case_ids": ["sine-fixed"], "source_manifest_sha256": file_sha256(self.root / "data/source-manifest.json"), "archive_sha256": file_sha256(self.root / "data/source.zip")})
        self.data = {
            "$schema": "./schemas/atlas-identities.schema.json", "schema_version": 1,
            "namespace": "NMA", "scope": "pilot", "revision_policy": "hex-min2-no-wrap-v1",
            "allocation": {"P": 2, "C": 2, "S": 2}, "entities": [
                self.entity("P", "problem", "sine", [self.binding("problem", "data/problem-snapshot.json", "")]),
                self.entity("C", "case", "sine-fixed", [
                    self.binding("case-definition", "data/case.json", ""),
                    self.binding("input", "data/case.json", "/input"),
                    self.binding("acceptance", "data/case.json", "/acceptance"),
                    self.binding("reference", "data/case.json", "/reference"),
                    self.binding("saved-result", "data/case.json", "/result"),
                    self.binding("saved-verification", "data/verification.json")]),
                self.entity("S", "source", "sine-python-release", [
                    self.binding("source", "data/source.py"), self.binding("dependency", "data/requirements.txt"),
                    self.binding("source-manifest", "data/source-manifest.json"), self.binding("archive", "data/source.zip")])]
        }

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_json(self, name, value):
        self.write(name, json.dumps(value, ensure_ascii=False))

    def binding(self, role, path, pointer=None):
        value = {"role": role, "path": path, "sha256": file_sha256(self.root / path)}
        if pointer is not None:
            value["pointer"] = pointer
            value["sha256"] = canonical_sha256(resolve_pointer(load_json(self.root / path), pointer))
        return value

    def entity(self, letter, kind, alias, bindings):
        return {"id": f"NMA-{letter}-000001", "kind": kind, "legacy_ids": [alias], "current_revision": "00", "revisions": [{"revision": "00", "label": {"ja": "固定模型", "en": "Fixed model"}, "problem_refs": [] if letter == "P" else ["NMA-P-000001@00"], "source_refs": ["NMA-S-000001@00"] if letter == "C" else [], "bindings": bindings}]}

    def revision(self, index):
        return self.data["entities"][index]["revisions"][0]

    def reject(self, message=None, baseline=None):
        if message:
            with self.assertRaisesRegex(IdentityError, message):
                validate_registry(self.root, self.data, baseline)
        else:
            with self.assertRaises(IdentityError):
                validate_registry(self.root, self.data, baseline)

    def test_valid_saved_artifacts_and_repeat_check(self):
        first = validate_registry(self.root, self.data, copy.deepcopy(self.data))
        self.assertEqual(first["entities"], 3)
        self.assertEqual(first["archive_bindings_checked"], 1)
        self.assertFalse(first["numerical_execution"])
        self.assertEqual(validate_registry(self.root, self.data), validate_registry(self.root, self.data))

    def test_invalid_ids_and_kind(self):
        original = copy.deepcopy(self.data)
        for identifier in ["NMA-P-000000", "NMA-P-0000001", "NMA-P-123", "nma-P-000001", "NMA-X-000001", "NMA-C-000001"]:
            with self.subTest(identifier=identifier):
                self.data = copy.deepcopy(original)
                self.data["entities"][0]["id"] = identifier
                self.reject()

    def test_duplicate_ids_and_aliases(self):
        self.data["entities"].append(copy.deepcopy(self.data["entities"][0]))
        self.reject("duplicate identity")
        self.data["entities"][-1]["id"] = "NMA-P-000002"
        self.data["allocation"]["P"] = 3
        self.reject("duplicate aliases")

    def test_unknown_fields_and_required_roles(self):
        self.revision(1)["bindings"] = self.revision(1)["bindings"][1:]
        self.reject("required binding roles")
        self.revision(1)["unexpected"] = True
        self.reject("keys")

    def test_missing_exact_reference(self):
        self.revision(1)["source_refs"] = ["NMA-S-000001@01"]
        self.reject("missing exact revision")

    def test_reference_kind(self):
        self.revision(1)["problem_refs"] = ["NMA-S-000001@00"]
        self.reject("wrong reference kind")

    def test_wrong_case_problem_mapping(self):
        self.write_json("catalog/atlas-depth-expansion.json", {"case_problem_ids": {"sine-fixed": "unrelated"}})
        self.reject("case/problem mapping")

    def test_source_bytes_tampered(self):
        self.write("data/source.py", "# changed without source revision\n")
        self.reject("SHA-256 mismatch")

    def test_recomputed_source_hash_still_rejects_manifest_disagreement(self):
        self.write("data/source.py", "# changed\n")
        self.revision(2)["bindings"][0] = self.binding("source", "data/source.py")
        self.reject("source differs from manifest")

    def test_wrong_archive_member_with_recomputed_archive_hash(self):
        with zipfile.ZipFile(self.root / "data/source.zip", "w") as archive:
            archive.writestr("release/source.py", "# substituted source")
            archive.write(self.root / "data/requirements.txt", "release/requirements.txt")
        self.revision(2)["bindings"][-1] = self.binding("archive", "data/source.zip")
        self.reject("archive source differs")

    def test_wrong_saved_verification(self):
        self.write_json("data/verification.json", {"case_ids": ["different"], "source_manifest_sha256": "0" * 64, "archive_sha256": "0" * 64})
        self.revision(1)["bindings"][-1] = self.binding("saved-verification", "data/verification.json")
        self.reject("saved verification misses case")

    def test_wrong_saved_verification_source_hash(self):
        value = load_json(self.root / "data/verification.json")
        value["archive_sha256"] = "0" * 64
        self.write_json("data/verification.json", value)
        self.revision(1)["bindings"][-1] = self.binding("saved-verification", "data/verification.json")
        self.reject("saved verification/source mismatch")

    def test_wrong_saved_case_identity(self):
        value = load_json(self.root / "data/case.json")
        value["result"]["id"] = "other"
        self.write_json("data/case.json", value)
        for index in [0, 4]:
            old = self.revision(1)["bindings"][index]
            self.revision(1)["bindings"][index] = self.binding(old["role"], old["path"], old["pointer"])
        self.reject()

    def test_missing_file_and_pointer(self):
        self.revision(0)["bindings"][0]["path"] = "missing.json"
        self.reject("missing file")
        self.revision(0)["bindings"][0]["path"] = "catalog/atlas-test-problems.json"
        self.revision(0)["bindings"][0]["pointer"] = "/problems/1"
        self.reject("missing JSON pointer")

    def test_unsafe_paths(self):
        binding = self.revision(2)["bindings"][0]
        for path in ["../source.py", "/etc/passwd", "data/./source.py", "data//source.py", "data\\source.py"]:
            with self.subTest(path=path):
                binding["path"] = path
                self.reject("unsafe path")

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory(prefix="atlas-outside-") as outside:
            target = Path(outside) / "file"
            target.write_text("outside")
            (self.root / "outside").symlink_to(target)
            with self.assertRaisesRegex(IdentityError, "escapes root"):
                safe_path(self.root, "outside")

    def test_json_duplicate_keys_and_nonfinite(self):
        for text in ['{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}', '{"a":-Infinity}', '{"a":1e9999}', '{"a":-1e9999}']:
            self.write("invalid.json", text)
            with self.assertRaises(IdentityError):
                load_json(self.root / "invalid.json")

    def test_strict_json_pointer(self):
        self.assertEqual(resolve_pointer({"a/b": {"~": [7]}}, "/a~1b/~0/0"), 7)
        for pointer in ["invalid", "/x~2", "/x/00", "/x/-1"]:
            with self.subTest(pointer=pointer), self.assertRaises(IdentityError):
                resolve_pointer({"x": [1]}, pointer)

    def test_unbumped_revision_rewrite(self):
        baseline = copy.deepcopy(self.data)
        self.revision(0)["label"]["en"] = "Rewritten without revision"
        self.reject("frozen revision rewritten", baseline=baseline)

    def test_removed_identity(self):
        baseline = copy.deepcopy(self.data)
        # Remove only the case so no other reference becomes dangling first.
        self.data["entities"].pop(1)
        self.reject("removed identity", baseline=baseline)

    def test_allocation_never_decreases_or_reuses_reserved_serial(self):
        baseline = copy.deepcopy(self.data)
        baseline["allocation"]["P"] = 5
        self.reject("allocation decreased", baseline=baseline)
        self.data["allocation"]["P"] = 5
        new = copy.deepcopy(self.data["entities"][0])
        new["id"] = "NMA-P-000002"
        new["legacy_ids"] = ["another"]
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "sine"}, {"id": "another"}]})
        new["revisions"][0]["bindings"] = [self.binding("problem", "catalog/atlas-test-problems.json", "/problems/1")]
        self.data["entities"].append(new)
        self.reject("reused reserved serial", baseline=baseline)

    def test_valid_append_and_hex_rollover(self):
        baseline = copy.deepcopy(self.data)
        entity = self.data["entities"][0]
        for number in range(1, 257):
            revision = copy.deepcopy(entity["revisions"][0])
            revision["revision"] = format_revision(number)
            revision["label"]["en"] = f"Revision {number}"
            entity["revisions"].append(revision)
        entity["current_revision"] = "100"
        self.assertTrue(validate_registry(self.root, self.data, baseline)["passed"])
        self.assertEqual(format_revision(255), "FF")
        self.assertEqual(format_revision(256), "100")
        for invalid in ["0", "0a", "000", "010", "0FF"]:
            with self.subTest(revision=invalid), self.assertRaises(IdentityError):
                revision_number(invalid)

    def test_catalog_reordering_does_not_change_problem_snapshot(self):
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "other"}, {"id": "sine"}]})
        self.assertTrue(validate_registry(self.root, self.data)["passed"])

    def test_current_problem_catalog_change_requires_new_snapshot_revision(self):
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "sine", "new_condition": "changed"}]})
        self.reject("current problem snapshot differs")

    def test_case_contract_cannot_change_under_same_source_revision(self):
        changed = copy.deepcopy(self.revision(1))
        changed["revision"] = "01"
        changed["bindings"][1] = self.binding("input", "data/case.json", "/acceptance")
        self.data["entities"][1]["revisions"].append(changed)
        self.data["entities"][1]["current_revision"] = "01"
        self.reject("case contract changed")

    def cli(self, *args):
        script = Path(__file__).resolve().with_name("check-atlas-identities.py")
        return subprocess.run([sys.executable, "-B", str(script), "--root", str(self.root), *args], text=True, capture_output=True)

    def test_new_source_label_cannot_reinterpret_unchanged_release_contract(self):
        new_source = copy.deepcopy(self.revision(2))
        new_source["revision"] = "01"
        self.data["entities"][2]["revisions"].append(new_source)
        self.data["entities"][2]["current_revision"] = "01"
        changed = copy.deepcopy(self.revision(1))
        changed["revision"] = "01"
        changed["source_refs"] = ["NMA-S-000001@01"]
        changed["bindings"][2] = self.binding("acceptance", "data/case.json", "/input")
        self.data["entities"][1]["revisions"].append(changed)
        self.data["entities"][1]["current_revision"] = "01"
        self.reject("case contract changed with unchanged source release bytes")

    def prepare_cli(self):
        self.write_json("catalog/atlas-identities.json", self.data)
        self.write_json("catalog/atlas-identity-history.json", self.data)

    def commit(self):
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=Identity test", "-c", "user.email=identity@example.invalid", "commit", "-qm", "fixture"], check=True, capture_output=True)
        return subprocess.check_output(["git", "-C", str(self.root), "rev-parse", "HEAD"], text=True).strip()

    def test_cli_requires_history_and_cannot_bypass_it_with_explicit_baseline(self):
        self.prepare_cli()
        baseline = copy.deepcopy(self.data)
        self.revision(0)["label"]["en"] = "rewritten initial version"
        self.write_json("catalog/atlas-identities.json", self.data)
        self.write_json("changed-baseline.json", self.data)
        result = self.cli("--baseline", str(self.root / "changed-baseline.json"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("frozen revision rewritten", result.stdout)
        (self.root / "catalog/atlas-identity-history.json").unlink()
        result = self.cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing file", result.stdout)

    def test_cli_rejects_invalid_git_ref(self):
        self.prepare_cli()
        result = self.cli("--baseline-ref", "HEAD;bad")
        self.assertEqual(result.returncode, 1)
        self.assertIn("40-digit", result.stdout)

    def test_cli_git_baseline_initial_rollout_and_later_revision_protection(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        initial = self.commit()
        self.prepare_cli()
        result = self.cli("--baseline-ref", initial)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse(json.loads(result.stdout)["previous_registry_found"])
        appended = copy.deepcopy(self.revision(0))
        appended["revision"] = "01"
        appended["label"]["en"] = "second published version"
        self.data["entities"][0]["revisions"].append(appended)
        self.data["entities"][0]["current_revision"] = "01"
        self.write_json("catalog/atlas-identities.json", self.data)
        previous = self.commit()
        result = self.cli("--baseline-ref", previous)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["git_baseline_checked"])
        appended["label"]["en"] = "rewritten second version"
        self.write_json("catalog/atlas-identities.json", self.data)
        result = self.cli("--baseline-ref", previous)
        self.assertEqual(result.returncode, 1)
        self.assertIn("frozen revision rewritten", result.stdout)

    def expanded_contract(self, *, external=None, standalone=False):
        """Tiny canonical coverage stand-in; real inventory has separate tests."""
        files = load_json(self.root / "data/source-manifest.json")["files"]
        return {
            "source_contracts": {"NMA-S-000001@00": {
                "root": "data", "files": files,
                "archive_path": None if standalone else "data/source.zip",
                "archive_members": {} if standalone else {name: "release/" + name for name in files},
                "kind": "standalone" if standalone else "flat",
            }},
            "allowed_external_case_bindings": external or {},
            "report": {"complete_fixture_coverage": True},
        }

    def coverage(self, contract=None, callback=None):
        module = types.ModuleType("atlas_identity_coverage")
        module.validate_current_coverage = callback or (lambda *args: contract or self.expanded_contract())
        return mock.patch.dict(sys.modules, {"atlas_identity_coverage": module})

    def member_source(self):
        old = self.revision(2)["bindings"][0]
        self.revision(2)["bindings"][0] = {
            "role": "source", "path": "data/source.zip", "member": "release/source.py",
            "sha256": old["sha256"],
        }

    def test_expanded_member_binding_validates_raw_bytes_and_source_archive(self):
        self.data["scope"] = "atlas-current"
        self.member_source()
        with self.coverage():
            report = validate_registry(self.root, self.data)
        self.assertEqual(report["coverage"], "atlas-current")
        self.assertTrue(report["complete_fixture_coverage"])
        self.assertFalse(report["numerical_execution"])
        self.revision(2)["bindings"][0]["sha256"] = "0" * 64
        with self.coverage():
            self.reject("SHA-256 mismatch")

    def test_member_selector_safety_applies_without_artifact_hashing(self):
        self.data["scope"] = "atlas-current"
        self.member_source()
        binding = self.revision(2)["bindings"][0]
        binding["pointer"] = ""
        with self.coverage():
            self.reject("mutually exclusive")
        del binding["pointer"]
        for member in ["../source.py", "/source.py", "C:/source.py", "release//source.py",
                       "release/./source.py", "release\\source.py", "release/\x00source.py",
                       "release/\x7fsource.py", "release/", "missing.py"]:
            with self.subTest(member=member), self.coverage(), self.assertRaises(IdentityError):
                binding["member"] = member
                validate_registry(self.root, self.data, check_artifacts=False)

    def test_unsafe_zip_directory_is_rejected_before_any_member_is_opened(self):
        self.data["scope"] = "atlas-current"
        self.member_source()
        original = (self.root / "data/source.zip").read_bytes()
        variants = ["duplicate", "symlink", "fifo", "traversal", "absolute", "backslash", "nul"]
        for variant in variants:
            with self.subTest(variant=variant):
                (self.root / "data/source.zip").write_bytes(original)
                with zipfile.ZipFile(self.root / "data/source.zip", "a") as archive:
                    if variant == "duplicate":
                        with self.assertWarns(UserWarning):
                            archive.writestr("release/source.py", "duplicate")
                    elif variant in {"symlink", "fifo"}:
                        info = zipfile.ZipInfo("release/special")
                        info.create_system = 3
                        kind = stat.S_IFLNK if variant == "symlink" else stat.S_IFIFO
                        info.external_attr = (kind | 0o777) << 16
                        archive.writestr(info, "target")
                    else:
                        name = {"traversal": "../escape.py", "absolute": "/escape.py",
                                "backslash": "release\\escape.py", "nul": "badX.py"}[variant]
                        archive.writestr(name, "unselected")
                if variant == "nul":
                    path = self.root / "data/source.zip"
                    path.write_bytes(path.read_bytes().replace(b"badX.py", b"bad\x00.py"))
                self.revision(2)["bindings"][-1] = self.binding("archive", "data/source.zip")
                with self.coverage(), mock.patch.object(
                        zipfile.ZipFile, "open", side_effect=AssertionError("unsafe member opened")):
                    self.reject()

    def test_expanded_normal_case_artifacts_still_require_source_membership(self):
        self.data["scope"] = "atlas-current"
        self.write_json("external/input.json", {"n": 8})
        self.revision(1)["bindings"][1] = self.binding("input", "external/input.json", "")
        with self.coverage():
            self.reject("case artifact outside referenced source release")

    def test_only_exact_prevalidated_external_case_bindings_bypass_legacy_checks(self):
        self.data["scope"] = "atlas-current"
        self.write_json("metadata/common.json", {"id": "sine-fixed", "acceptance": {"e": 1e-6},
                                                 "reference": "saved analytic sine"})
        self.write_json("metadata/common-verification.json", {"examples": ["sine-fixed"], "passed": True})
        bindings = self.revision(1)["bindings"]
        for index, role, pointer in [(0, "case-definition", ""), (2, "acceptance", "/acceptance"),
                                     (3, "reference", "/reference")]:
            bindings[index] = self.binding(role, "metadata/common.json", pointer)
        bindings[-1] = self.binding("saved-verification", "metadata/common-verification.json")
        allowed = {binding_key(b) for b in bindings if b["path"].startswith("metadata/")}
        profile = self.expanded_contract(external={"NMA-C-000001@00": allowed})
        with self.coverage(profile):
            self.assertTrue(validate_registry(self.root, self.data)["passed"])
        for omitted in [bindings[2], bindings[-1]]:
            with self.subTest(role=omitted["role"]), self.coverage(self.expanded_contract(
                    external={"NMA-C-000001@00": allowed - {binding_key(omitted)}})):
                self.reject()
        wrong = set(allowed)
        wrong.add(("input", "external/unreviewed.json", None, None, "0" * 64))
        with self.coverage(self.expanded_contract(external={"NMA-C-000001@00": wrong})):
            self.reject("invalid external case binding allowlist")

    def test_expanded_current_coverage_is_not_required_of_historical_baseline(self):
        self.data["scope"] = "atlas-current"
        baseline = copy.deepcopy(self.data)
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "sine"}, {"id": "second"}]})
        self.write_json("data/second.json", {"id": "second"})
        extra = self.entity("P", "problem", "second", [self.binding("problem", "data/second.json", "")])
        extra["id"] = "NMA-P-000002"
        self.data["entities"].append(extra)
        self.data["allocation"]["P"] = 3
        seen = []
        def current_only(root, data, entities, snapshots):
            seen.append(len(entities))
            self.assertEqual(len(entities), 4)
            return self.expanded_contract()
        with self.coverage(callback=current_only):
            self.assertTrue(validate_registry(self.root, self.data, baseline)["passed"])
        self.assertEqual(seen, [4])

    def test_structural_current_validation_still_requires_complete_coverage(self):
        self.data["scope"] = "atlas-current"
        def incomplete(*args):
            raise IdentityError("missing canonical coverage")
        with self.coverage(callback=incomplete), self.assertRaisesRegex(IdentityError, "missing canonical coverage"):
            validate_registry(self.root, self.data, check_artifacts=False)

    def test_expanded_scope_cannot_be_downgraded_to_pilot(self):
        baseline = copy.deepcopy(self.data)
        baseline["scope"] = "atlas-current"
        self.reject("coverage scope downgraded", baseline=baseline)

    def test_expanded_diagnostics_and_frozen_source_problem_subsets(self):
        self.data["scope"] = "atlas-current"
        self.revision(1)["problem_refs"] = []
        self.revision(2)["problem_refs"] = []
        self.write_json("catalog/atlas-depth-expansion.json", {"case_problem_ids": {"sine-fixed": None}})
        with self.coverage():
            self.assertTrue(validate_registry(self.root, self.data)["passed"])
        self.write_json("catalog/atlas-test-problems.json", {"problems": [{"id": "sine"}, {"id": "second"}]})
        self.write_json("data/second.json", {"id": "second"})
        extra = self.entity("P", "problem", "second", [self.binding("problem", "data/second.json", "")])
        extra["id"] = "NMA-P-000002"
        self.data["entities"].append(extra); self.data["allocation"]["P"] = 3
        self.revision(1)["problem_refs"] = ["NMA-P-000002@00"]
        self.revision(2)["problem_refs"] = ["NMA-P-000001@00"]
        self.write_json("catalog/atlas-depth-expansion.json", {"case_problem_ids": {"sine-fixed": "second"}})
        with self.coverage():
            self.assertTrue(validate_registry(self.root, self.data)["passed"])

    def test_only_standalone_source_contract_can_omit_archive(self):
        self.data["scope"] = "atlas-current"
        self.data["entities"].pop(1)
        self.revision(1)["bindings"].pop()
        profile = self.expanded_contract(standalone=True)
        with self.coverage(profile):
            self.assertTrue(validate_registry(self.root, self.data)["passed"])
        profile["source_contracts"]["NMA-S-000001@00"]["kind"] = "flat"
        with self.coverage(profile):
            self.reject("source archive differs from contract")

    def test_same_zip_case_contract_guard_remains_in_expanded_scope(self):
        self.data["scope"] = "atlas-current"
        changed = copy.deepcopy(self.revision(1))
        changed["revision"] = "01"
        changed["bindings"][1] = self.binding("input", "data/case.json", "/acceptance")
        self.data["entities"][1]["revisions"].append(changed)
        self.data["entities"][1]["current_revision"] = "01"
        with self.coverage():
            self.reject("case contract changed with unchanged source release bytes")


if __name__ == "__main__":
    unittest.main()
