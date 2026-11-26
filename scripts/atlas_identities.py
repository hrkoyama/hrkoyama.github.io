"""Offline, standard-library validation of Atlas stable identities.

This checks saved bytes and exact metadata references. It never imports released
solvers, extracts archives, or interprets saved success as a new numerical run.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import zipfile


class IdentityError(ValueError):
    """The identity registry is invalid or an immutable binding changed."""


KINDS = {"problem": "P", "case": "C", "source": "S"}
REQUIRED_ROLES = {
    "problem": {"problem"},
    "case": {"case-definition", "input", "acceptance", "reference", "saved-result", "saved-verification"},
    "source": {"source", "dependency", "source-manifest", "archive"},
}
ROLES = set.union(*REQUIRED_ROLES.values()) | {"provenance"}
TOP_KEYS = {"$schema", "schema_version", "namespace", "scope", "revision_policy", "allocation", "entities"}
ENTITY_KEYS = {"id", "kind", "legacy_ids", "current_revision", "revisions"}
REVISION_KEYS = {"revision", "label", "problem_refs", "source_refs", "bindings"}
ID_PATTERN = re.compile(r"NMA-([PCS])-([0-9]{6,})\Z")
SHA_PATTERN = re.compile(r"[0-9a-f]{64}\Z")


def require(condition, message):
    if not condition:
        raise IdentityError(message)


def exact_keys(value, expected, where):
    require(isinstance(value, dict), f"{where}: expected object")
    require(set(value) == expected, f"{where}: unexpected or missing keys: {sorted(set(value) ^ expected)}")


def _pairs(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, f"duplicate JSON key: {key}")
        value[key] = item
    return value


def parse_json(text):
    def finite_float(value):
        number = float(value)
        require(math.isfinite(number), f"nonfinite JSON number: {value}")
        return number

    try:
        return json.loads(text, object_pairs_hook=_pairs,
                          parse_float=finite_float,
                          parse_constant=lambda x: (_ for _ in ()).throw(IdentityError(f"nonfinite JSON number: {x}")))
    except json.JSONDecodeError as exc:
        raise IdentityError(f"invalid JSON: {exc}") from exc


def load_json(path):
    try:
        return parse_json(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise IdentityError(f"cannot read JSON {path}: {exc}") from exc


def canonical_sha256(value):
    try:
        data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise IdentityError(f"noncanonical JSON value: {exc}") from exc
    return hashlib.sha256(data).hexdigest()


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_path(root, relative):
    require(isinstance(relative, str) and relative, "path must be a nonempty string")
    require("\\" not in relative and "\x00" not in relative, f"unsafe path: {relative!r}")
    parts = relative.split("/")
    require(not PurePosixPath(relative).is_absolute() and all(p not in {"", ".", ".."} for p in parts), f"unsafe path: {relative}")
    path = Path(root).resolve() / relative
    require(path.resolve().is_relative_to(Path(root).resolve()), f"path escapes root: {relative}")
    require(path.is_file(), f"missing file: {relative}")
    return path


def resolve_pointer(value, pointer):
    require(isinstance(pointer, str) and (pointer == "" or pointer.startswith("/")), f"invalid JSON pointer: {pointer!r}")
    if pointer == "":
        return value
    for raw in pointer[1:].split("/"):
        require(not re.search(r"~(?![01])", raw), f"invalid JSON pointer escape: {pointer}")
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict):
            require(token in value, f"missing JSON pointer: {pointer}")
            value = value[token]
        elif isinstance(value, list):
            require(bool(re.fullmatch(r"0|[1-9][0-9]*", token)), f"invalid array index: {pointer}")
            index = int(token)
            require(index < len(value), f"missing JSON pointer: {pointer}")
            value = value[index]
        else:
            raise IdentityError(f"JSON pointer traverses scalar: {pointer}")
    return value


def format_revision(number):
    require(type(number) is int and number >= 0, "invalid revision number")
    return f"{number:02X}"


def revision_number(value):
    require(isinstance(value, str) and bool(re.fullmatch(r"[0-9A-F]{2,}", value)), f"invalid hex revision: {value!r}")
    number = int(value, 16)
    require(format_revision(number) == value, f"noncanonical hex revision: {value}")
    return number


def parse_id(value):
    require(isinstance(value, str), "ID must be a string")
    match = ID_PATTERN.fullmatch(value)
    require(match is not None, f"invalid identity ID: {value}")
    kind, serial = match.groups()
    require(int(serial) > 0 and f"{int(serial):06d}" == serial, f"noncanonical identity serial: {value}")
    return kind, int(serial)


def parse_ref(value, expected):
    require(isinstance(value, str) and value.count("@") == 1, f"invalid exact reference: {value!r}")
    identifier, revision = value.split("@")
    kind, _ = parse_id(identifier)
    require(kind == expected, f"wrong reference kind: {value}")
    revision_number(revision)
    return identifier, revision


def validate_baseline(current, baseline):
    """Require append-only history, IDs and allocation when old registry exists."""
    previous = {item["id"]: item for item in baseline["entities"]}
    present = {item["id"]: item for item in current["entities"]}
    for letter in "PCS":
        require(current["allocation"][letter] >= baseline["allocation"][letter], f"allocation decreased: {letter}")
    for identifier, old in previous.items():
        require(identifier in present, f"removed identity: {identifier}")
        new = present[identifier]
        require(new["kind"] == old["kind"] and new["legacy_ids"] == old["legacy_ids"], f"identity or aliases rewritten: {identifier}")
        require(new["revisions"][:len(old["revisions"])] == old["revisions"], f"frozen revision rewritten or removed: {identifier}")
    for identifier in present.keys() - previous.keys():
        letter, serial = parse_id(identifier)
        require(serial >= baseline["allocation"][letter], f"reused reserved serial: {identifier}")


def validate_artifact_relations(root, entities):
    """Reject correctly hashed material attached to the wrong problem or case."""
    def bound_value(binding):
        value = load_json(safe_path(root, binding["path"]))
        return resolve_pointer(value, binding["pointer"]) if "pointer" in binding else value

    canonical_problems = {row["id"]: row for row in load_json(safe_path(root, "catalog/atlas-test-problems.json"))["problems"]}
    member_hashes = {}
    def archived_sha256(archive, relative):
        key = (archive["sha256"], relative)
        if key not in member_hashes:
            try:
                with zipfile.ZipFile(safe_path(root, archive["path"])) as zipped:
                    names = zipped.namelist()
                    candidates = [name for name in names if name == relative or name.endswith("/" + relative)]
                    require(candidates, f"case artifact missing from archive: {relative}")
                    length = min(name.count("/") for name in candidates)
                    members = [name for name in candidates if name.count("/") == length]
                    require(len(members) == 1, f"ambiguous case archive member: {relative}")
                    digest = hashlib.sha256()
                    with zipped.open(members[0]) as stream:
                        for block in iter(lambda: stream.read(1024 * 1024), b""):
                            digest.update(block)
                    member_hashes[key] = digest.hexdigest()
            except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
                raise IdentityError(f"cannot inspect case archive member: {relative}: {exc}") from exc
        return member_hashes[key]

    sources = {}
    for identifier, entity in entities.items():
        for revision in entity["revisions"]:
            if entity["kind"] != "source":
                continue
            bindings = revision["bindings"]
            manifests = [b for b in bindings if b["role"] == "source-manifest"]
            archives = [b for b in bindings if b["role"] == "archive"]
            require(len(manifests) == len(archives) == 1, f"source needs one manifest and archive: {identifier}")
            manifest, archive = manifests[0], archives[0]
            require("pointer" not in manifest, f"source manifest must bind full file: {identifier}")
            value = bound_value(manifest)
            files = value.get("files")
            require(isinstance(files, dict), f"invalid source manifest files: {identifier}")
            parent = PurePosixPath(manifest["path"]).parent
            selected = [b for b in bindings if b["role"] in {"source", "dependency"}]
            try:
                with zipfile.ZipFile(safe_path(root, archive["path"])) as zipped:
                    names = zipped.namelist()
                    require(len(names) == len(set(names)), f"duplicate ZIP members: {identifier}")
                    for binding in selected:
                        require("pointer" not in binding, f"source must bind full file: {identifier}")
                        try:
                            relative = PurePosixPath(binding["path"]).relative_to(parent).as_posix()
                        except ValueError as exc:
                            raise IdentityError(f"source outside manifest directory: {identifier}") from exc
                        require(files.get(relative) == binding["sha256"], f"source differs from manifest: {identifier} {relative}")
                        candidates = [name for name in names if name == relative or name.endswith("/" + relative)]
                        require(candidates, f"source missing from archive: {identifier} {relative}")
                        length = min(name.count("/") for name in candidates)
                        members = [name for name in candidates if name.count("/") == length]
                        require(len(members) == 1, f"ambiguous source archive member: {identifier} {relative}")
                        digest = hashlib.sha256()
                        with zipped.open(members[0]) as stream:
                            for block in iter(lambda: stream.read(1024 * 1024), b""):
                                digest.update(block)
                        require(digest.hexdigest() == binding["sha256"], f"archive source differs: {identifier} {relative}")
            except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
                raise IdentityError(f"cannot inspect source archive: {identifier}: {exc}") from exc
            sources[f"{identifier}@{revision['revision']}"] = (manifest, archive, files)
    for identifier, entity in entities.items():
        for revision in entity["revisions"]:
            if entity["kind"] == "case":
                contract_roles = {"case-definition", "input", "acceptance", "reference"}
                contract = {canonical_sha256(b) for b in revision["bindings"] if b["role"] in contract_roles}
                def fingerprints(record):
                    return {sources[ref][1]["sha256"] for ref in record["source_refs"]}
                for previous in entity["revisions"]:
                    if previous is revision:
                        break
                    if fingerprints(previous) == fingerprints(revision):
                        old = {canonical_sha256(b) for b in previous["bindings"] if b["role"] in contract_roles}
                        require(contract == old, f"case contract changed with unchanged source release bytes: {identifier}")
                for binding in revision["bindings"]:
                    if binding["role"] == "saved-verification":
                        continue
                    matched_release = False
                    for ref in revision["source_refs"]:
                        manifest, archive, files = sources[ref]
                        parent = PurePosixPath(manifest["path"]).parent
                        try:
                            relative = PurePosixPath(binding["path"]).relative_to(parent).as_posix()
                        except ValueError:
                            continue
                        raw_sha = file_sha256(safe_path(root, binding["path"]))
                        require(files.get(relative) == raw_sha, f"case artifact differs from source manifest: {identifier} {relative}")
                        require(archived_sha256(archive, relative) == raw_sha, f"case artifact differs from archive: {identifier} {relative}")
                        matched_release = True
                    require(matched_release, f"case artifact outside referenced source release: {identifier} {binding['path']}")
            for binding in revision["bindings"]:
                if binding["role"] not in {"problem", "case-definition", "saved-result", "saved-verification"}:
                    continue
                value = bound_value(binding)
                if binding["role"] in {"problem", "case-definition"}:
                    require(isinstance(value, dict) and value.get("id") in entity["legacy_ids"], f"bound identity does not match: {identifier}")
                if binding["role"] == "problem" and revision["revision"] == entity["current_revision"]:
                    require(value == canonical_problems[value["id"]], f"current problem snapshot differs from canonical catalog: {identifier}")
                if binding["role"] == "saved-result" and isinstance(value, dict) and "id" in value:
                    require(value["id"] in entity["legacy_ids"], f"saved result belongs to another case: {identifier}")
                    if "input_sha256" in value:
                        inputs = [bound_value(b) for b in revision["bindings"] if b["role"] == "input"]
                        saved_hashes = {hashlib.sha256(json.dumps(v, sort_keys=True).encode()).hexdigest() for v in inputs}
                        require(value["input_sha256"] in saved_hashes, f"saved result/input hash mismatch: {identifier}")
                if binding["role"] == "saved-verification":
                    require(isinstance(value, dict) and set(entity["legacy_ids"]).issubset(value.get("case_ids", [])), f"saved verification misses case: {identifier}")
                    matched = []
                    for ref in revision["source_refs"]:
                        manifest, archive, _ = sources[ref]
                        if value.get("source_manifest_sha256") == manifest["sha256"] and value.get("archive_sha256") == archive["sha256"]:
                            matched.append(ref)
                    require(matched, f"saved verification/source mismatch: {identifier}")


def validate_registry(root, data, baseline=None, check_artifacts=True):
    """Validate structure, canonical catalog membership, bindings and references."""
    root = Path(root).resolve()
    exact_keys(data, TOP_KEYS, "registry")
    require(data["$schema"] == "./schemas/atlas-identities.schema.json", "unexpected schema URL")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "unsupported schema version")
    require(data["namespace"] == "NMA" and data["scope"] == "pilot", "unsupported namespace or scope")
    require(data["revision_policy"] == "hex-min2-no-wrap-v1", "unsupported revision policy")
    exact_keys(data["allocation"], set("PCS"), "allocation")
    for letter, serial in data["allocation"].items():
        require(type(serial) is int and serial > 0, f"invalid next serial: {letter}")
    require(isinstance(data["entities"], list) and data["entities"], "entities must be nonempty list")
    entities, snapshots, aliases = {}, {}, {kind: set() for kind in KINDS}
    binding_count, archive_count = 0, 0
    json_cache, hash_cache = {}, {}
    for item in data["entities"]:
        exact_keys(item, ENTITY_KEYS, "entity")
        identifier = item["id"]
        letter, serial = parse_id(identifier)
        require(item["kind"] in KINDS and KINDS[item["kind"]] == letter, f"ID/kind mismatch: {identifier}")
        require(identifier not in entities, f"duplicate identity: {identifier}")
        entities[identifier] = item
        require(serial < data["allocation"][letter], f"next serial overlaps allocation: {identifier}")
        legacy = item["legacy_ids"]
        require(isinstance(legacy, list) and legacy and all(isinstance(x, str) and x for x in legacy), f"invalid aliases: {identifier}")
        require(len(legacy) == len(set(legacy)) and not aliases[item["kind"]].intersection(legacy), f"duplicate aliases: {identifier}")
        aliases[item["kind"]].update(legacy)
        revisions = item["revisions"]
        require(isinstance(revisions, list) and revisions, f"empty revisions: {identifier}")
        for index, revision in enumerate(revisions):
            exact_keys(revision, REVISION_KEYS, f"revision {identifier}")
            require(revision_number(revision["revision"]) == index, f"noncontiguous revisions: {identifier}")
            exact_keys(revision["label"], {"ja", "en"}, f"label {identifier}")
            require(all(isinstance(x, str) and x.strip() for x in revision["label"].values()), f"empty label: {identifier}")
            for key, expected in [("problem_refs", "P"), ("source_refs", "S")]:
                refs = revision[key]
                require(isinstance(refs, list) and all(isinstance(x, str) for x in refs), f"invalid references: {identifier}")
                require(len(refs) == len(set(refs)), f"duplicate references: {identifier}")
                for ref in refs:
                    parse_ref(ref, expected)
            if item["kind"] == "problem":
                require(not revision["problem_refs"] and not revision["source_refs"], f"problem has implementation references: {identifier}")
            elif item["kind"] == "source":
                require(revision["problem_refs"] and not revision["source_refs"], f"source references invalid: {identifier}")
            else:
                require(revision["problem_refs"] and revision["source_refs"], f"case missing problem/source reference: {identifier}")
            require(isinstance(revision["bindings"], list) and revision["bindings"], f"empty bindings: {identifier}")
            roles, seen = set(), set()
            for binding in revision["bindings"]:
                require(isinstance(binding, dict), f"binding must be object: {identifier}")
                require(set(binding) in ({"role", "path", "sha256"}, {"role", "path", "sha256", "pointer"}), f"binding keys invalid: {identifier}")
                require(isinstance(binding["role"], str) and binding["role"] in ROLES, f"unknown binding role: {identifier}")
                require(isinstance(binding["sha256"], str) and SHA_PATTERN.fullmatch(binding["sha256"]), f"invalid SHA-256: {identifier}")
                pointer = binding.get("pointer")
                require("pointer" not in binding or isinstance(pointer, str), f"invalid pointer type: {identifier}")
                require(isinstance(binding["path"], str), f"invalid path type: {identifier}")
                identity = (binding["role"], binding["path"], pointer)
                require(identity not in seen, f"duplicate binding: {identifier}")
                seen.add(identity); roles.add(binding["role"])
                # Safety applies to structural-only validation as well.
                path = safe_path(root, binding["path"])
                if pointer is not None:
                    if binding["path"] not in json_cache:
                        json_cache[binding["path"]] = load_json(path)
                    fragment = resolve_pointer(json_cache[binding["path"]], pointer)
                    actual = canonical_sha256(fragment)
                elif check_artifacts:
                    if binding["path"] not in hash_cache:
                        hash_cache[binding["path"]] = file_sha256(path)
                    actual = hash_cache[binding["path"]]
                if check_artifacts:
                    require(actual == binding["sha256"], f"binding SHA-256 mismatch: {identifier} {binding['path']} {pointer or ''}")
                if binding["role"] == "archive":
                    require(pointer is None and path.suffix == ".zip", f"archive must bind complete ZIP: {identifier}")
                    archive_count += 1
                binding_count += 1
            require(REQUIRED_ROLES[item["kind"]].issubset(roles), f"missing required binding roles: {identifier}")
            snapshots[f"{identifier}@{revision['revision']}"] = revision
        require(item["current_revision"] == revisions[-1]["revision"], f"current revision not latest: {identifier}")
    problems = load_json(safe_path(root, "catalog/atlas-test-problems.json"))["problems"]
    known_problems = {row["id"] for row in problems}
    case_problems = load_json(safe_path(root, "catalog/atlas-depth-expansion.json"))["case_problem_ids"]
    for identifier, item in entities.items():
        if item["kind"] == "problem":
            require(set(item["legacy_ids"]).issubset(known_problems), f"unknown canonical problem: {identifier}")
        for revision in item["revisions"]:
            for ref in revision["problem_refs"] + revision["source_refs"]:
                require(ref in snapshots, f"missing exact revision reference: {identifier} -> {ref}")
            if item["kind"] != "case":
                continue
            referenced_legacy = {alias for ref in revision["problem_refs"] for alias in entities[ref.split("@")[0]]["legacy_ids"]}
            for alias in item["legacy_ids"]:
                require(alias in case_problems, f"unknown canonical case: {alias}")
                mapped = case_problems[alias]
                mapped = {mapped} if isinstance(mapped, str) else set(mapped)
                require(mapped and mapped.issubset(referenced_legacy), f"case/problem mapping mismatch: {alias}")
            for source_ref in revision["source_refs"]:
                source_problems = set(snapshots[source_ref]["problem_refs"])
                require(source_problems.intersection(revision["problem_refs"]), f"case/source problem mismatch: {identifier} -> {source_ref}")
    if baseline is not None:
        validate_registry(root, baseline, check_artifacts=False)
        validate_baseline(data, baseline)
    if check_artifacts:
        validate_artifact_relations(root, entities)
    return {
        "passed": True, "validation_type": "saved-artifact-integrity-only", "numerical_execution": False,
        "coverage": "pilot-only", "entities": len(entities),
        "problems": sum(x["kind"] == "problem" for x in entities.values()),
        "cases": sum(x["kind"] == "case" for x in entities.values()),
        "sources": sum(x["kind"] == "source" for x in entities.values()),
        "revisions": len(snapshots), "bindings_checked": binding_count,
        "archive_bindings_checked": archive_count, "baseline_checked": baseline is not None,
    }
