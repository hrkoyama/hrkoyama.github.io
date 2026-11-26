"""Saved-byte inventory of the Atlas's current numerical source units.

This module uses only the standard library.  It never extracts an archive,
imports a released solver, runs numerical code, or reads private work records.
Historical source revisions are interpreted from their own immutable bindings,
not from the current-release catalogue.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import unquote, urlsplit
import zipfile


CATALOG = "catalog/atlas-identity-sources.json"
SHA = re.compile(r"[0-9a-f]{64}\Z")
SOURCE_EXTENSIONS = {".py", ".cpp", ".c", ".cc", ".cxx", ".h", ".hpp", ".f",
                     ".f90", ".jl", ".m", ".rs", ".cu", ".sh", ".patch"}
DEPENDENCY_NAMES = {"pyproject.toml", "setup.cfg", "pipfile", "pipfile.lock",
                    "cmakelists.txt", "makefile"}
NONPUBLIC_DIRECTORIES = {".git", ".venv", "venv", "node_modules", "__pycache__",
                         ".pytest_cache", "test-results", "playwright-report"}


class SourceInventoryError(ValueError):
    """The reviewed current source inventory or a frozen source is inconsistent."""


def require(value, message):
    if not value:
        raise SourceInventoryError(message)


def _relative(value):
    require(isinstance(value, str) and value and "\\" not in value
            and not any(ord(c) < 32 for c in value), "invalid source path")
    require(not PurePosixPath(value).is_absolute()
            and all(p not in {"", ".", ".."} for p in value.split("/")),
            "noncanonical source path")
    return value


def _path(root, relative):
    path = Path(root).resolve() / _relative(relative)
    require(path.is_file() and not path.is_symlink()
            and path.resolve().is_relative_to(Path(root).resolve()),
            "missing or linked source file: " + relative)
    return path


def _pairs(rows):
    value = {}
    for key, item in rows:
        require(key not in value, "duplicate JSON key")
        value[key] = item
    return value


def _load(root, relative):
    path = _path(root, relative)
    require(path.stat().st_size <= 8 * 1024**2, "source metadata exceeds limit")
    def finite_float(value):
        number = float(value)
        require(math.isfinite(number), "nonfinite source metadata")
        return number
    return json.loads(path.read_bytes(), object_pairs_hook=_pairs, parse_float=finite_float,
                      parse_constant=lambda _: (_ for _ in ()).throw(
                          SourceInventoryError("nonfinite source metadata")))


def _digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024**2), b""):
            value.update(block)
    return value.hexdigest()


def _binding(root, role, path, member=None):
    value = {"role": role, "path": path}
    if member is None:
        value["sha256"] = _digest(_path(root, path))
    else:
        _relative(member)
        with _archive(root, path) as archive:
            value["sha256"] = hashlib.sha256(archive.read(member)).hexdigest()
        value["member"] = member
    return value


@contextmanager
def _archive(root, path):
    try:
        with zipfile.ZipFile(_path(root, path)) as archive:
            yield archive
    except (OSError, zipfile.BadZipFile, RuntimeError, NotImplementedError) as error:
        raise SourceInventoryError("cannot inspect source ZIP: " + path) from error


def _role(relative):
    name = PurePosixPath(relative).name.lower()
    if name.startswith("requirements") or name in DEPENDENCY_NAMES:
        return "dependency"
    if PurePosixPath(relative).suffix.lower() in SOURCE_EXTENSIONS:
        return "source"
    return None


def _member_names(archive):
    names = {}
    for item in archive.infolist():
        name = item.filename.rstrip("/") if item.is_dir() else item.filename
        _relative(name)
        require(item.filename not in names, "duplicate ZIP member")
        mode = item.external_attr >> 16
        require(stat.S_IFMT(mode) in ({0, stat.S_IFDIR} if item.is_dir() else {0, stat.S_IFREG}),
                "nonregular ZIP member")
        require(not item.flag_bits & 1, "encrypted ZIP member")
        names[item.filename] = item
    return {name: item for name, item in names.items() if not item.is_dir()}


def _manifest_files(value):
    files = value.get("files")
    if isinstance(files, list):
        result = {}
        for item in files:
            require(isinstance(item, dict) and set(item) == {"path", "bytes", "sha256"}
                    and type(item["bytes"]) is int and item["bytes"] >= 0,
                    "invalid standalone manifest entry")
            name = _relative(item["path"])
            require(name not in result, "duplicate standalone manifest path")
            result[name] = item["sha256"]
        kind = "standalone"
    else:
        require(isinstance(files, dict) and files, "invalid source manifest files")
        result = dict(files)
        kind = "archive-members" if value.get("format") == "external-archive-members-v1" else "flat"
        if "format" in value:
            require(kind == "archive-members"
                    and set(value) == {"format", "archive_sha256", "files"},
                    "unknown external source manifest")
    require(result, "empty source manifest")
    for name, digest in result.items():
        _relative(name)
        require(isinstance(digest, str) and SHA.fullmatch(digest),
                "invalid source manifest digest")
    return kind, result


def source_contract(root, revision):
    """Normalize a source revision, including preserved noncurrent revisions."""
    bindings = revision.get("bindings")
    require(isinstance(bindings, list) and all(isinstance(b, dict) for b in bindings),
            "source revision needs bindings")
    manifests = [b for b in bindings if b.get("role") == "source-manifest"]
    archives = [b for b in bindings if b.get("role") == "archive"]
    require(len(manifests) == 1 and len(archives) <= 1, "source manifest/archive count")
    manifest = manifests[0]
    require("pointer" not in manifest and "member" not in manifest,
            "source manifest must bind one full external file")
    path = _path(root, manifest["path"])
    require(_digest(path) == manifest.get("sha256"), "source manifest bytes differ")
    value = _load(root, manifest["path"])
    require(isinstance(value, dict), "source manifest must be an object")
    kind, files = _manifest_files(value)
    archive_path = archives[0]["path"] if archives else None
    member_map = {}
    if kind == "standalone":
        require(archive_path is None
                and manifest["path"].startswith("numerical-methods-atlas/assets/")
                and path.name == "manifest.json", "invalid unarchived source kind")
        parent = PurePosixPath(manifest["path"]).parent
        for item in value["files"]:
            physical = _path(root, (parent / item["path"]).as_posix())
            require(physical.stat().st_size == item["bytes"]
                    and _digest(physical) == item["sha256"],
                    "standalone manifest file bytes differ")
    else:
        require(archive_path is not None and "member" not in archives[0]
                and "pointer" not in archives[0], "packaged source needs one raw archive")
        with _archive(root, archive_path) as archive:
            names = _member_names(archive)
            if kind == "archive-members":
                require(value["archive_sha256"] == archives[0].get("sha256"),
                        "external manifest archive digest differs")
                require(set(files) == set(names), "external manifest ZIP inventory differs")
                member_map = {name: name for name in files}
                for member, expected in files.items():
                    digest = hashlib.sha256()
                    with archive.open(member) as stream:
                        for block in iter(lambda: stream.read(1024**2), b""):
                            digest.update(block)
                    require(digest.hexdigest() == expected,
                            "external manifest ZIP member bytes differ")
            else:
                for relative in files:
                    candidates = [n for n in names if n == relative or n.endswith("/" + relative)]
                    require(candidates, "manifest file missing from ZIP: " + relative)
                    depth = min(n.count("/") for n in candidates)
                    matches = [n for n in candidates if n.count("/") == depth]
                    require(len(matches) == 1, "ambiguous manifest file in ZIP: " + relative)
                    member_map[relative] = matches[0]
    return {"root": "" if kind == "archive-members" else PurePosixPath(manifest["path"]).parent.as_posix(),
            "files": files, "archive_path": archive_path,
            "archive_members": member_map, "kind": kind,
            "manifest_path": manifest["path"], "manifest_sha256": manifest["sha256"],
            "archive_sha256": archives[0]["sha256"] if archives else None,
            "dependency_paths": sorted(p for p in files if _role(p) == "dependency")}


def _public_path(value):
    require(isinstance(value, str), "invalid public source URL")
    parsed = urlsplit(value)
    require(not parsed.query and not parsed.fragment, "unexpected source URL suffix")
    if parsed.scheme or parsed.netloc:
        require(parsed.scheme == "https" and parsed.netloc == "hrkoyama.github.io",
                "source authority must use HR HTTPS")
    return _relative(unquote(parsed.path).lstrip("/"))


def _pointer(value, pointer):
    require(isinstance(pointer, str) and (not pointer or pointer.startswith("/")),
            "invalid source authority pointer")
    for part in pointer.split("/")[1:] if pointer else []:
        require(not re.search(r"~(?![01])", part), "invalid source authority escape")
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            require(re.fullmatch(r"0|[1-9][0-9]*", part), "invalid source authority index")
            value = value[int(part)]
        else:
            require(isinstance(value, dict) and part in value, "missing source authority")
            value = value[part]
    return value


def _authority_archive(value):
    require(isinstance(value, dict), "source authority must be an object")
    if "zip" in value:
        return _public_path(value["zip"])
    if "archive_url" in value:
        return _public_path(value["archive_url"])
    archive = value.get("archive")
    require(isinstance(archive, str), "source authority has no archive")
    if archive.startswith(("/", "https://")):
        return _public_path(archive)
    return _public_path(value["base"].rstrip("/") + "/" + archive)


def _resolve_authority(root, authority):
    if set(authority) == {"path", "pointer"}:
        return (_pointer(_load(root, authority["path"]), authority["pointer"]),
                dict(authority))
    require(set(authority) == {"path", "method_id", "field"}
            and authority["path"] == "catalog/atlas-methods.json",
            "invalid source authority")
    methods = _load(root, authority["path"])["methods"]
    matches = [(i, m) for i, m in enumerate(methods) if m["id"] == authority["method_id"]]
    require(len(matches) == 1 and authority["field"] in matches[0][1],
            "missing or duplicate source method authority")
    index, method = matches[0]
    return method[authority["field"]], {
        "path": authority["path"],
        "pointer": "/methods/" + str(index) + "/" + authority["field"]}


def _zip_inventory(root):
    result = set()
    for directory, dirs, files in os.walk(Path(root).resolve(), followlinks=False):
        if Path(directory) == Path(root).resolve():
            dirs[:] = [d for d in dirs if d not in NONPUBLIC_DIRECTORIES]
        require(not any((Path(directory) / d).is_symlink() for d in dirs),
                "linked public source directory")
        for filename in files:
            if filename.lower().endswith(".zip"):
                path = Path(directory) / filename
                require(not path.is_symlink(), "linked public archive")
                result.add(path.relative_to(Path(root).resolve()).as_posix())
    return result


def _method_archives(value):
    result = set()
    if isinstance(value, dict):
        base = value.get("base")
        if (isinstance(base, str)
                and base.startswith(("/code/", "https://hrkoyama.github.io/code/"))
                and isinstance(value.get("archive"), str)):
            result.add(_authority_archive(value))
        for item in value.values():
            result.update(_method_archives(item))
    elif isinstance(value, list):
        for item in value:
            result.update(_method_archives(item))
    return result


def _shallow_member(files, filename):
    matches = [name for name in files if PurePosixPath(name).name == filename]
    require(matches, "missing source provenance member")
    depth = min(name.count("/") for name in matches)
    matches = [name for name in matches if name.count("/") == depth]
    require(len(matches) == 1, "ambiguous source provenance member")
    return matches[0]


def source_inventory(root):
    """Return every reviewed current source state; allocate no identities."""
    root = Path(root).resolve()
    catalog = _load(root, CATALOG)
    require(set(catalog) == {"schema_version", "scope", "family_revisions",
                             "extra_sources", "standalone_sources", "archive_partition"}
            and type(catalog["schema_version"]) is int and catalog["schema_version"] == 1
            and catalog["scope"] == "current-atlas-scientific-sources-v1",
            "unknown source catalogue schema")
    partition = catalog["archive_partition"]
    require(isinstance(partition, list), "invalid archive partition")
    archive_rows = {}
    for row in partition:
        require(set(row) == {"path", "sha256", "classification", "unit_key", "reason"},
                "invalid archive partition row")
        path = _relative(row["path"])
        require(path not in archive_rows and path.lower().endswith(".zip")
                and row["classification"] in {"current", "retained-history",
                                              "retained-experiment", "instruction"},
                "duplicate or unknown archive partition")
        require(isinstance(row["reason"], str) and row["reason"], "archive partition needs a reason")
        require(_digest(_path(root, path)) == row["sha256"], "reviewed archive bytes differ")
        archive_rows[path] = row
    require(set(archive_rows) == _zip_inventory(root), "physical ZIP inventory differs from reviewed partition")
    specifications = {}
    groups = {v["id"]: v["title"] for v in _load(root, "catalog/atlas-depth-expansion.json")["groups"]}
    releases_path = "numerical-methods-atlas/validation/releases.json"
    for index, release in enumerate(_load(root, releases_path)["releases"]):
        directory = _public_path(release["base"].rstrip("/"))
        path = directory + "/" + release["archive"]
        require(path not in specifications, "duplicate supplement source archive")
        specifications[path] = {"unit_key": "supplement:" + release["group"],
                                "edition": release["edition"], "kind": "flat", "root": directory,
                                "manifest": directory + "/source-manifest.json", "archive": path,
                                "label": groups[release["group"]],
                                "authorities": [{"path": releases_path, "pointer": "/releases/" + str(index)}]}
        require(archive_rows.get(path, {}).get("sha256") == release["archive_sha256"],
                "current supplement archive differs from source catalogue")
        require(_digest(_path(root, directory + "/source-manifest.json")) == release["manifest_sha256"],
                "current supplement manifest differs from release")
        require(_digest(_path(root, directory + "/requirements.txt")) == release["requirements_sha256"],
                "current supplement requirements differ from release")
    common_path = "numerical-methods-atlas/code-and-data/examples.json"
    for index, example in enumerate(_load(root, common_path)["examples"]):
        release = example["release"]
        path = _public_path(release["download"])
        spec = {"unit_key": "shared:" + release["family"], "edition": release["version"],
                "kind": "flat", "root": PurePosixPath(path).parent.as_posix(),
                "manifest": _public_path(release["manifest"]), "archive": path,
                "label": {"ja": "\u5171\u901a\u6570\u5024\u8a08\u7b97\u30d1\u30c3\u30b1\u30fc\u30b8",
                          "en": "Shared numerical-methods package"},
                "authorities": []}
        if path in specifications:
            old = specifications[path]
            require(all(old[k] == spec[k] for k in ("unit_key", "edition", "kind", "root", "manifest", "archive")),
                    "inconsistent shared source release")
        else:
            specifications[path] = spec
        specifications[path]["authorities"].append(
            {"path": common_path, "pointer": "/examples/" + str(index) + "/release"})
        require(archive_rows.get(path, {}).get("sha256") == release["sha256"],
                "current common archive differs from source catalogue")
        require(_digest(_path(root, spec["manifest"])) == release["manifest_sha256"],
                "current common manifest differs from release")
    for extra in catalog["extra_sources"]:
        require(set(extra) == {"unit_key", "edition", "kind", "root", "manifest",
                               "archive", "label", "authorities"}, "invalid extra source declaration")
        path = _relative(extra["archive"])
        require(path not in specifications and extra["kind"] in {"flat", "archive-members"}
                and extra["authorities"], "duplicate or unauthorised extra source")
        normalized_authorities = []
        for authority in extra["authorities"]:
            value, normalized = _resolve_authority(root, authority)
            require(_authority_archive(value) == path, "extra source is no longer the current authority")
            for field in ("archive_sha256", "zip_sha256"):
                if field in value:
                    require(value[field] == archive_rows[path]["sha256"],
                            "extra source authority archive digest differs")
            if "edition" in value or "release" in value:
                require(value.get("edition", value.get("release")) == extra["edition"],
                        "extra source authority edition differs")
            if isinstance(value.get("manifest"), str) and "base" in value:
                require(_public_path(value["base"].rstrip("/") + "/" + value["manifest"]) == extra["manifest"],
                        "extra source manifest differs from authority")
            normalized_authorities.append(normalized)
        specifications[path] = {**extra, "authorities": normalized_authorities}
    required_extras = _method_archives(_load(root, "catalog/atlas-methods.json"))
    required_extras.add(_authority_archive(_load(root, "catalog/atlas-agent-kits.json")))
    course = _load(root, "catalog/atlas-foundations-course.json")
    course_release = "code/numerical-foundations/" + _relative(course["edition"]) + "/release.json"
    required_extras.add(_authority_archive(_load(root, course_release)))
    require(required_extras <= set(specifications),
            "a still-current method, course or agent source was omitted")
    require({p for p, v in archive_rows.items() if v["classification"] == "current"} == set(specifications),
            "current archive partition differs from authoritative sources")
    states = list(specifications.values())
    for standalone in catalog["standalone_sources"]:
        require(set(standalone) == {"unit_key", "edition", "root", "manifest", "label"},
                "invalid standalone declaration")
        states.append({**standalone, "kind": "standalone", "archive": None, "authorities": []})
    family_revisions = catalog["family_revisions"]
    require(isinstance(family_revisions, dict), "invalid adopted source revisions")
    descriptors, seen = [], set()
    for spec in states:
        unit, edition = spec["unit_key"], spec["edition"]
        require(isinstance(unit, str) and unit and isinstance(edition, str) and edition,
                "invalid source unit or edition")
        require((unit, edition) not in seen, "duplicate source state")
        seen.add((unit, edition))
        archive = spec["archive"]
        if archive:
            require(archive_rows[archive]["unit_key"] == unit, "archive assigned to wrong source unit")
        manifest_binding = _binding(root, "source-manifest", spec["manifest"])
        archive_binding = _binding(root, "archive", archive) if archive else None
        structural = [manifest_binding] + ([archive_binding] if archive_binding else [])
        contract = source_contract(root, {"bindings": structural})
        require(contract["kind"] == spec["kind"], "source declaration kind differs from actual manifest")
        require(spec["root"] == contract["root"], "source declaration root differs from manifest")
        bindings = []
        for relative, expected in sorted(contract["files"].items()):
            role = _role(relative)
            if role is None:
                continue
            if contract["kind"] == "archive-members":
                binding = _binding(root, role, archive, relative)
            else:
                binding = _binding(root, role, spec["root"] + "/" + relative)
            require(binding["sha256"] == expected, "source or dependency differs from manifest")
            bindings.append(binding)
        require(any(b["role"] == "source" for b in bindings), "source unit has no implementation")
        if spec["kind"] in {"flat", "standalone"}:
            require(any(b["role"] == "dependency" for b in bindings), "declared dependency file missing")
        if unit == "course:numerical-foundations":
            bindings.append(_binding(root, "provenance", archive,
                                     _shallow_member(contract["files"], "README.md")))
            bindings.append(_binding(root, "provenance", course_release))
        elif unit == "agent-kit:rkdg2d":
            bindings.append(_binding(root, "provenance", archive,
                                     _shallow_member(contract["files"], "RELEASE.json")))
        elif spec["kind"] == "standalone":
            bindings.append(_binding(root, "provenance", spec["root"] + "/README.txt"))
        revision_hint = family_revisions.get(unit, {}).get(edition, "00")
        require(isinstance(revision_hint, str) and re.fullmatch(r"[0-9A-F]{2,}", revision_hint),
                "invalid adopted source revision")
        require(f"{int(revision_hint, 16):02X}" == revision_hint, "noncanonical adopted source revision")
        pilot_id = {"supplement:sem-fr": "NMA-S-000001",
                    "supplement:quantum-small": "NMA-S-000002"}.get(unit)
        descriptors.append({"unit_key": unit, "edition": edition,
                            "revision_hint": revision_hint, "kind": spec["kind"],
                            "root": spec["root"], "label": spec["label"],
                            "source_manifest": manifest_binding, "archive": archive_binding,
                            "bindings": bindings + structural, "files": contract["files"],
                            "archive_members": contract["archive_members"],
                            "authorities": spec["authorities"], "pilot_id": pilot_id,
                            "contract": contract})
    by_unit = {}
    for descriptor in descriptors:
        by_unit.setdefault(descriptor["unit_key"], []).append(descriptor)
    for unit, versions in by_unit.items():
        if len(versions) > 1 or unit in family_revisions:
            require(unit in family_revisions
                    and set(family_revisions[unit]) == {v["edition"] for v in versions}
                    and len({v["revision_hint"] for v in versions}) == len(versions),
                    "coexisting source versions need explicit adopted revisions")
    require(set(family_revisions) <= set(by_unit), "unused adopted source family")
    standalone_paths = [b["path"] for d in descriptors if d["kind"] == "standalone"
                        for b in d["bindings"] if b["role"] == "source"]
    physical_assets = {p.relative_to(root).as_posix()
                       for p in (root / "numerical-methods-atlas/assets").rglob("*.py")}
    require(len(standalone_paths) == len(set(standalone_paths))
            and set(standalone_paths) == physical_assets,
            "standalone numerical source inventory differs from public assets")
    return sorted(descriptors, key=lambda d: (d["unit_key"], int(d["revision_hint"], 16)))
