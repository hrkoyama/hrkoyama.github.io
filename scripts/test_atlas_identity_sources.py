"""Portable tiny source-inventory fixtures; no solver or real release is run."""
import hashlib
import json
from pathlib import Path
import stat
import tempfile
import unittest
import warnings
import zipfile

from atlas_identity_sources import SourceInventoryError, source_contract, source_inventory


def digest(data):
    return hashlib.sha256(data).hexdigest()


class SourceFixture(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="atlas-identity-sources-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
        return path

    def write_json(self, relative, data):
        return self.write(relative, json.dumps(data, sort_keys=True))

    def write_zip(self, relative, members, defect=None):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(path, "w") as archive:
                for member, data in members.items():
                    archive.writestr(member, data)
                if defect == "duplicate":
                    archive.writestr("pkg/solver.py", members["pkg/solver.py"])
                if defect in {"symlink", "directory-mode"}:
                    item = zipfile.ZipInfo("pkg/link.py")
                    item.create_system = 3
                    mode = stat.S_IFLNK if defect == "symlink" else stat.S_IFDIR
                    item.external_attr = (mode | 0o777) << 16
                    archive.writestr(item, b"solver.py")
        return path

    def binding(self, role, path):
        return {"role": role, "path": path, "sha256": digest((self.root / path).read_bytes())}

    def contract_fixture(self, kind="flat", defect=None):
        files = {"solver.py": b"# fixture is never imported\n", "requirements.txt": b""}
        members = {"pkg/" + name: data for name, data in files.items()}
        if kind == "archive-members":
            members["pkg/reference.json"] = b'{"stored":true}\n'
        if defect == "traversal":
            members["../outside.py"] = b"# not extracted\n"
        archive_path = "code/demo/pkg.zip"
        archive = self.write_zip(archive_path, members, defect)
        manifest_path = "code/demo/source-manifest.json"
        if kind == "flat":
            for name, data in files.items():
                self.write("code/demo/" + name, data)
            manifest = {"files": {name: digest(data) for name, data in files.items()}}
        elif kind == "archive-members":
            manifest_path = "catalog/identity-source-manifests/demo.json"
            manifest = {
                "format": "external-archive-members-v1",
                "archive_sha256": digest(archive.read_bytes()),
                "files": {name: digest(data) for name, data in members.items()},
            }
            if defect == "wrong-member":
                manifest["files"]["pkg/reference.json"] = "0" * 64
            elif defect == "wrong-archive":
                manifest["archive_sha256"] = "0" * 64
            elif defect == "format":
                manifest["format"] = "unknown-v1"
        else:
            manifest_path = "numerical-methods-atlas/assets/demo/manifest.json"
            for name, data in files.items():
                self.write("numerical-methods-atlas/assets/demo/" + name, data)
            manifest = {"files": [{"path": name, "bytes": len(data), "sha256": digest(data)}
                                  for name, data in files.items()]}
            if defect == "size":
                manifest["files"][0]["bytes"] += 1
            elif defect == "hash":
                manifest["files"][0]["sha256"] = "0" * 64
            elif defect == "repeated":
                manifest["files"].append(dict(manifest["files"][0]))
        self.write_json(manifest_path, manifest)
        bindings = [self.binding("source-manifest", manifest_path)]
        if kind != "standalone" or defect == "with-archive":
            bindings.append(self.binding("archive", archive_path))
        if defect == "no-archive":
            bindings = bindings[:1]
        return {"bindings": bindings}

    def complete_inventory_fixture(self):
        """Four tiny states exercise all current-authority discovery branches."""
        label = {"ja": "Fixture", "en": "Fixture"}
        plain = {"solver.py": b"# fixture only\n", "requirements.txt": b""}
        directory = "code/fdtd/fixture"
        method_zip = directory + "/package.zip"
        self.write_zip(method_zip, {"method/" + k: v for k, v in plain.items()})
        for name, data in plain.items():
            self.write(directory + "/" + name, data)
        self.write_json(directory + "/source-manifest.json",
                        {"files": {k: digest(v) for k, v in plain.items()}})
        method_release = {"base": "/" + directory + "/", "edition": "fixture",
                          "archive": "package.zip", "manifest": "source-manifest.json"}
        self.write_json("catalog/atlas-methods.json",
                        {"methods": [{"id": "fdtd", "release": method_release}]})
        extras = [{
            "unit_key": "independent:fdtd", "edition": "fixture", "kind": "flat",
            "root": directory, "manifest": directory + "/source-manifest.json",
            "archive": method_zip, "label": label,
            "authorities": [{"path": "catalog/atlas-methods.json",
                             "method_id": "fdtd", "field": "release"}],
        }]
        for unit, filename, authority, members in [
            ("course:numerical-foundations", "lab",
             "code/numerical-foundations/fixture/release.json",
             {"lab/solver.py": b"# never executed\n", "lab/README.md": b"Standard library only.\n"}),
            ("agent-kit:rkdg2d", "kit", "catalog/atlas-agent-kits.json",
             {"kit/solver.py": b"# never executed\n", "kit/RELEASE.json": b"{}\n"}),
        ]:
            path = "code/" + filename + "/fixture/" + filename + ".zip"
            archive = self.write_zip(path, members)
            manifest = "catalog/identity-source-manifests/" + filename + ".json"
            self.write_json(manifest, {
                "format": "external-archive-members-v1",
                "archive_sha256": digest(archive.read_bytes()),
                "files": {k: digest(v) for k, v in members.items()},
            })
            value = ({"zip": "/" + path, "zip_sha256": digest(archive.read_bytes())}
                     if filename == "lab" else {"archive": "/" + path})
            self.write_json(authority, value)
            extras.append({
                "unit_key": unit, "edition": "fixture", "kind": "archive-members",
                "root": "", "manifest": manifest, "archive": path, "label": label,
                "authorities": [{"path": authority, "pointer": ""}],
            })
        self.write_json("catalog/atlas-foundations-course.json", {"edition": "fixture"})
        self.write_json("catalog/atlas-depth-expansion.json", {"groups": []})
        self.write_json("numerical-methods-atlas/validation/releases.json", {"releases": []})
        self.write_json("numerical-methods-atlas/code-and-data/examples.json", {"examples": []})
        directory = "numerical-methods-atlas/assets/fixture"
        asset_files = {**plain, "README.txt": b"Fixture numerical analysis.\n"}
        for name, data in asset_files.items():
            self.write(directory + "/" + name, data)
        self.write_json(directory + "/manifest.json", {
            "files": [{"path": k, "bytes": len(v), "sha256": digest(v)}
                      for k, v in asset_files.items()],
        })
        partition = [{
            "path": spec["archive"],
            "sha256": digest((self.root / spec["archive"]).read_bytes()),
            "classification": "current", "unit_key": spec["unit_key"],
            "reason": "Synthetic current source authority.",
        } for spec in extras]
        catalog = {
            "schema_version": 1, "scope": "current-atlas-scientific-sources-v1",
            "family_revisions": {}, "extra_sources": extras,
            "standalone_sources": [{
                "unit_key": "standalone:fixture", "edition": "fixture",
                "root": directory, "manifest": directory + "/manifest.json", "label": label,
            }],
            "archive_partition": partition,
        }
        self.write_json("catalog/atlas-identity-sources.json", catalog)
        self.assertEqual(len(source_inventory(self.root)), 4)
        return catalog


class SourceContractTests(SourceFixture):
    def reject(self, kind, defect, message):
        revision = self.contract_fixture(kind, defect)
        with self.assertRaisesRegex(SourceInventoryError, message):
            source_contract(self.root, revision)

    def test_valid_flat_source(self):
        value = source_contract(self.root, self.contract_fixture())
        self.assertEqual(value["kind"], "flat")
        self.assertEqual(value["root"], "code/demo")
        self.assertEqual(value["archive_members"]["solver.py"], "pkg/solver.py")

    def test_valid_archive_member_source(self):
        value = source_contract(self.root, self.contract_fixture("archive-members"))
        self.assertEqual(value["kind"], "archive-members")
        self.assertEqual(value["root"], "")
        self.assertEqual(set(value["files"]), set(value["archive_members"]))

    def test_valid_unarchived_source(self):
        value = source_contract(self.root, self.contract_fixture("standalone"))
        self.assertEqual(value["kind"], "standalone")
        self.assertIsNone(value["archive_path"])
        self.assertEqual(value["archive_members"], {})

    def test_packaged_source_requires_archive(self):
        self.reject("flat", "no-archive", "packaged source needs")

    def test_unarchived_source_rejects_archive(self):
        self.reject("standalone", "with-archive", "invalid unarchived source kind")

    def test_external_manifest_checks_even_nonsource_member_hash(self):
        self.reject("archive-members", "wrong-member", "ZIP member bytes differ")

    def test_external_manifest_requires_exact_archive_hash(self):
        self.reject("archive-members", "wrong-archive", "archive digest differs")

    def test_external_manifest_rejects_unknown_format(self):
        self.reject("archive-members", "format", "unknown external source manifest")

    def test_duplicate_zip_member_is_rejected(self):
        self.reject("flat", "duplicate", "duplicate ZIP member")

    def test_zip_traversal_is_rejected(self):
        self.reject("flat", "traversal", "noncanonical source path")

    def test_nonregular_zip_members_are_rejected(self):
        for defect in ("symlink", "directory-mode"):
            with self.subTest(defect=defect):
                self.reject("flat", defect, "nonregular ZIP member")

    def test_unarchived_manifest_requires_actual_sizes(self):
        self.reject("standalone", "size", "file bytes differ")

    def test_unarchived_manifest_requires_actual_hashes(self):
        self.reject("standalone", "hash", "file bytes differ")

    def test_unarchived_manifest_rejects_duplicate_paths(self):
        self.reject("standalone", "repeated", "duplicate standalone manifest path")


class SourceInventoryTests(SourceFixture):
    def test_still_current_method_cannot_be_reclassified_as_history(self):
        catalog = self.complete_inventory_fixture()
        catalog["extra_sources"] = [s for s in catalog["extra_sources"]
                                    if s["unit_key"] != "independent:fdtd"]
        for row in catalog["archive_partition"]:
            if row["unit_key"] == "independent:fdtd":
                row["classification"] = "retained-history"
        self.write_json("catalog/atlas-identity-sources.json", catalog)
        with self.assertRaisesRegex(SourceInventoryError, "still-current"):
            source_inventory(self.root)

    def test_current_standalone_cannot_be_silently_omitted(self):
        catalog = self.complete_inventory_fixture()
        catalog["standalone_sources"] = []
        self.write_json("catalog/atlas-identity-sources.json", catalog)
        with self.assertRaisesRegex(SourceInventoryError, "standalone numerical source inventory"):
            source_inventory(self.root)

    def test_unknown_nested_archive_cannot_hide_in_named_infrastructure(self):
        self.complete_inventory_fixture()
        self.write_zip("code/fdtd/fixture/node_modules/unknown.zip", {})
        with self.assertRaisesRegex(SourceInventoryError, "physical ZIP inventory"):
            source_inventory(self.root)


if __name__ == "__main__":
    unittest.main()
