"""Identity descriptors for the published supplement and common fixed cases.

Only saved metadata and bytes are inspected. No released solver is imported,
no archive is extracted, and no saved success is treated as a new execution.
"""
from __future__ import annotations

from copy import deepcopy
from functools import wraps
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlsplit

ORIGIN = "https://hrkoyama.github.io"
COMMON_CATALOG = "catalog/atlas-execution-examples.json"
COMMON_PUBLIC = "numerical-methods-atlas/code-and-data/examples.json"
SUPPLEMENT_CATALOG = "catalog/atlas-depth-expansion.json"
SUPPLEMENT_RELEASES = "numerical-methods-atlas/validation/releases.json"
MAX_JSON_BYTES = 32 * 1024 * 1024
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
CASE_ID = re.compile(r"[a-z][a-z0-9-]*\Z")


class CaseInventoryError(ValueError):
    """Published fixed-case metadata or its saved verification is inconsistent."""


def _case_boundary(function):
    @wraps(function)
    def checked(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except CaseInventoryError:
            raise
        except (KeyError, IndexError, TypeError, ValueError, OSError, UnicodeError) as exc:
            raise CaseInventoryError("invalid fixed-case metadata: " + type(exc).__name__) from exc
    return checked


def _require(condition, message):
    if not condition:
        raise CaseInventoryError(message)


def _relative(value):
    _require(isinstance(value, str) and value and "\\" not in value
             and not any(ord(c) < 32 for c in value), "invalid case artifact path")
    p = PurePosixPath(value)
    _require(not p.is_absolute() and p.as_posix() == value
             and all(x not in {"", ".", ".."} for x in value.split("/")),
             "unsafe case artifact path")
    return value


def _file(root, relative):
    relative = _relative(relative)
    root = Path(root).resolve()
    path = root / relative
    _require(path.is_file() and not path.is_symlink()
             and path.resolve().is_relative_to(root), "missing or unsafe case artifact: " + relative)
    return path


def _url_path(value):
    _require(isinstance(value, str), "case URL must be a string")
    url = urlsplit(value)
    _require(url.scheme == "https" and url.netloc == "hrkoyama.github.io"
             and not url.query and not url.fragment and url.path.startswith("/"),
             "case artifact must have a canonical HR URL")
    return _relative(url.path[1:])


def _hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json(root, relative):
    path = _file(root, relative)
    _require(path.stat().st_size <= MAX_JSON_BYTES, "case JSON exceeds the metadata budget")

    def pairs(items):
        value = {}
        for key, item in items:
            _require(key not in value, "duplicate case JSON key: " + key)
            value[key] = item
        return value

    def finite(value):
        number = float(value)
        _require(math.isfinite(number), "nonfinite case JSON number")
        return number

    def constant(_):
        raise CaseInventoryError("nonfinite case JSON number")

    try:
        return json.loads(path.read_bytes(), object_pairs_hook=pairs,
                          parse_float=finite, parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise CaseInventoryError("invalid case JSON: " + relative) from exc


def _canonical(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def _pointer(value, pointer):
    _require(isinstance(pointer, str) and (pointer == "" or pointer.startswith("/")),
             "invalid case JSON pointer")
    if not pointer:
        return value
    for raw in pointer[1:].split("/"):
        _require(not re.search(r"~(?![01])", raw), "invalid case JSON pointer escape")
        key = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, dict):
            _require(key in value, "missing case JSON pointer")
            value = value[key]
        else:
            _require(isinstance(value, list) and re.fullmatch(r"0|[1-9][0-9]*", key),
                     "invalid case JSON array pointer")
            _require(int(key) < len(value), "missing case JSON array element")
            value = value[int(key)]
    return value


def _unique(items, key, where):
    _require(isinstance(items, list), where + " must be a list")
    result = {}
    for item in items:
        _require(isinstance(item, dict) and key in item, where + " record is invalid")
        value = item[key]
        _require(isinstance(value, str) and value and value not in result,
                 where + " identifier is missing or repeated")
        result[value] = item
    return result


def _problems(value, known):
    _require(value is None or isinstance(value, str), "unsupported authoritative case/problem mapping")
    result = [] if value is None else [value]
    _require(set(result) <= known, "case refers to an unknown canonical problem")
    return result


def _saved_input_selector(inputs, case, saved):
    """Locate the exact archived JSON object used by an existing case hash.

    The historical case runners used json.dumps(sort_keys=True), rather than
    the compact canonical encoding used by identity bindings. Keep that
    original hash convention; never infer or reconstruct a merged input.
    """
    if "input_sha256" not in saved:
        return None
    wanted = saved["input_sha256"]
    _require(isinstance(wanted, str) and SHA256.fullmatch(wanted), "invalid saved case input hash")

    def encoded(value):
        return json.dumps(value, sort_keys=True, allow_nan=False).encode()

    if hashlib.sha256(encoded(inputs)).hexdigest() == wanted:
        return None
    token = case["id"].replace("~", "~0").replace("/", "~1")
    preferred = "/cases/" + token
    if isinstance(inputs, dict) and isinstance(inputs.get("cases"), dict) and case["id"] in inputs["cases"]:
        if hashlib.sha256(encoded(inputs["cases"][case["id"]])).hexdigest() == wanted:
            return preferred

    def objects(value, pointer=""):
        if isinstance(value, (dict, list)):
            yield pointer, value
            entries = value.items() if isinstance(value, dict) else enumerate(value)
            for key, item in entries:
                escaped = str(key).replace("~", "~0").replace("/", "~1")
                yield from objects(item, pointer + "/" + escaped)

    matches = [(pointer, encoded(value)) for pointer, value in objects(inputs)
               if hashlib.sha256(encoded(value)).hexdigest() == wanted]
    _require(matches, "saved case input hash has no exact immutable input selector: " + case["id"])
    _require(len({raw for _, raw in matches}) == 1, "saved case input hash has conflicting input objects")
    return min((pointer for pointer, _ in matches), key=lambda p: (p.count("/"), p))


@_case_boundary
def case_inventory(root):
    """Return current case descriptors; IDs are allocated by the outer registry.

    New supplement cases conservatively freeze their complete shared input and
    acceptance files. Existing pilot revisions are retained by the caller.
    """
    root = Path(root).resolve()
    problems = _unique(_json(root, "catalog/atlas-test-problems.json")["problems"], "id", "problem")
    expansion = _json(root, SUPPLEMENT_CATALOG)
    mapping = expansion["case_problem_ids"]
    _require(isinstance(mapping, dict), "supplement problem mapping must be an object")
    releases = _json(root, SUPPLEMENT_RELEASES)["releases"]
    _unique(releases, "group", "supplement release")
    json_cache, hash_cache = {}, {}

    def binding(role, path, pointer=None):
        result = {"role": role, "path": _relative(path)}
        if pointer is None:
            if path not in hash_cache:
                hash_cache[path] = _hash(_file(root, path))
            result["sha256"] = hash_cache[path]
        else:
            if path not in json_cache:
                json_cache[path] = _json(root, path)
            result.update(pointer=pointer, sha256=_canonical(_pointer(json_cache[path], pointer)))
        return result

    rows = []
    for release in releases:
        base = _url_path(release["base"].rstrip("/"))
        manifest_path = base + "/source-manifest.json"
        manifest = _json(root, manifest_path)
        archive = base + "/" + _relative(release["archive"])
        _require(PurePosixPath(release["archive"]).name == release["archive"], "invalid release archive name")
        definition_path = base + "/cases.json"
        definitions = _json(root, definition_path)
        prefix = "/cases/" if isinstance(definitions, dict) else "/"
        definitions = definitions["cases"] if isinstance(definitions, dict) else definitions
        by_id = _unique(definitions, "id", "supplement definition")
        input_data = _json(root, base + "/inputs.json")
        saved = _json(root, base + "/results/result.json")["cases"]
        saved_by_id = _unique(saved, "id", "supplement saved result")
        _require(set(by_id) == set(saved_by_id) == set(release["case_ids"]),
                 "supplement definitions, results and release cases differ")
        saved_indices = {item["id"]: i for i, item in enumerate(saved)}
        for index, case in enumerate(definitions):
            identifier = case["id"]
            _require(CASE_ID.fullmatch(identifier) and identifier in mapping, "unknown supplement case")
            ptr = prefix + str(index)
            acceptance = base + "/acceptance.json"
            if not (root / acceptance).is_file():
                acceptance = base + "/inputs.json"
            bindings = [binding("case-definition", definition_path, ptr),
                        binding("input", base + "/inputs.json"), binding("acceptance", acceptance)]
            input_selector = _saved_input_selector(input_data, case, saved_by_id[identifier])
            if input_selector is not None:
                bindings.insert(2, binding("input", base + "/inputs.json", input_selector))
            for field in ("formulas", "equations", "validation"):
                if field in case:
                    bindings.append(binding("reference", definition_path, ptr + "/" + field))
            for relative in case.get("reference_files", []):
                _require(relative in manifest["files"], "case reference is absent from its manifest")
                bindings.append(binding("reference", base + "/" + relative))
            result_pointer = "/cases/" + str(saved_indices[identifier])
            bindings.extend([binding("saved-result", base + "/results/result.json", result_pointer),
                             binding("saved-verification", base + "/verification.json")])
            rows.append({"legacy_id": identifier, "domain": "supplement", "label": deepcopy(case["title"]),
                         "problem_ids": _problems(mapping[identifier], set(problems)),
                         "source_manifest": manifest_path, "source_archive": archive,
                         "source_manifest_sha256": release["manifest_sha256"],
                         "source_archive_sha256": release["archive_sha256"],
                         "canonical_definition": deepcopy(case), "definition_path": definition_path,
                         "definition_pointer": ptr, "saved_result_pointer": result_pointer,
                         "saved_input_selector": input_selector,
                         "verification_path": base + "/verification.json",
                         "bindings_draft": _deduplicate(bindings)})
    _require({row["legacy_id"] for row in rows} == set(mapping), "supplement mapping is not completely covered")
    canonical = _json(root, COMMON_CATALOG)["examples"]
    public = _json(root, COMMON_PUBLIC)
    _require(canonical == public["examples"], "common public registry differs from canonical records")
    _unique(canonical, "id", "common definition")
    receipt_path = _url_path(public["verification_receipt"])
    for index, case in enumerate(canonical):
        row = _common_row(root, case, receipt_path, COMMON_CATALOG, "/examples/" + str(index))
        _require(set(row["problem_ids"]) <= problems.keys(), "common case refers to an unknown canonical problem")
        rows.append(row)
    _unique(rows, "legacy_id", "registered case")
    return sorted(rows, key=lambda row: row["legacy_id"])


def _deduplicate(bindings):
    seen, result = set(), []
    for binding in bindings:
        key = (binding["role"], binding["path"], binding.get("pointer"))
        if key not in seen:
            seen.add(key)
            result.append(binding)
    return result


def _common_row(root, definition, receipt_path, definition_path, definition_pointer):
    """Describe supplied common metadata without rereading a mutable catalog."""
    case = deepcopy(definition)
    identifier = case["id"]
    _require(isinstance(identifier, str) and CASE_ID.fullmatch(identifier), "invalid common case identifier")
    _require(isinstance(case.get("problem_id"), str) and case["problem_id"], "common problem identity is missing")
    definition_path = _relative(definition_path)
    manifest_path = _url_path(case["release"]["manifest"])
    base = manifest_path.rsplit("/", 1)[0]
    manifest = _json(root, manifest_path)

    def material(role, path, pointer=None):
        return {"role": role, "path": _relative(path),
                **({"pointer": pointer, "sha256": _canonical(_pointer(_json(root, path), pointer))}
                   if pointer is not None else {"sha256": _hash(_file(root, path))})}

    def metadata(role, pointer):
        return {"role": role, "path": definition_path, "pointer": definition_pointer + pointer,
                "sha256": _canonical(_pointer(case, pointer))}

    ipath = _url_path(case["inputs"]["url"])
    _require(ipath.startswith(base + "/") and ipath[len(base) + 1:] in manifest["files"],
             "common input is outside its source manifest")
    _require(_hash(_file(root, ipath)) == case["inputs"]["sha256"], "common input hash differs")
    bindings = [metadata("case-definition", ""), material("input", ipath),
                metadata("acceptance", "/checks"), metadata("acceptance", "/expected_failures"),
                metadata("reference", "/references")]
    if "acceptance" in _json(root, ipath):
        bindings.append(material("acceptance", ipath, "/acceptance"))
    for reference in case["references"]:
        url = urlsplit(reference.get("url", ""))
        if url.netloc != "hrkoyama.github.io" or not url.path.startswith("/" + base + "/"):
            continue
        path = _url_path(reference["url"])
        _require(path[len(base) + 1:] in manifest["files"], "common local reference is not archived")
        bindings.append(material("reference", path))
    outputs = [item for item in case["outputs"] if item["id"] == "results"]
    _require(len(outputs) == 1, "common case needs one saved results record")
    result_path = _url_path(outputs[0]["url"])
    _require(result_path.startswith(base + "/") and result_path[len(base) + 1:] in manifest["files"],
             "common result is outside its source manifest")
    _require(_hash(_file(root, result_path)) == outputs[0]["sha256"], "common saved result hash differs")
    bindings.extend([material("saved-result", result_path), material("saved-verification", receipt_path)])
    return {"legacy_id": identifier, "domain": "common", "label": deepcopy(case["name"]),
            "problem_ids": [case["problem_id"]], "source_manifest": manifest_path,
            "source_archive": _url_path(case["release"]["download"]),
            "source_manifest_sha256": case["release"]["manifest_sha256"],
            "source_archive_sha256": case["release"]["sha256"],
            "canonical_definition": case, "definition_path": definition_path,
            "definition_pointer": definition_pointer, "verification_path": receipt_path,
            "common_receipt_path": receipt_path, "bindings_draft": _deduplicate(bindings)}


@_case_boundary
def common_row_from_snapshot(root, definition, receipt_path, *, snapshot_path=None):
    """Describe a retained common C record using its dated receipt, not live data.

    Supplying the real snapshot path records its origin. If not supplied the
    metadata draft uses the catalog path as a placeholder; case_bindings always
    replaces it with the requested immutable C/revision path before publication.
    """
    return _common_row(root, definition, receipt_path, snapshot_path or COMMON_CATALOG, "")


@_case_boundary
def case_bindings(root, row, identifier, revision="00"):
    """Return bindings, freezing common metadata in this C revision's snapshot.

    The caller writes canonical_definition to that snapshot. Its hash can be
    computed before the file is written; live catalog offsets are never frozen.
    """
    match = re.fullmatch(r"NMA-C-([0-9]{6,})", identifier or "")
    _require(match and int(match[1]) > 0 and f"{int(match[1]):06d}" == match[1], "invalid stable case ID")
    _require(isinstance(revision, str) and re.fullmatch(r"[0-9A-F]{2,}", revision)
             and f"{int(revision, 16):02X}" == revision, "invalid stable case revision")
    bindings = deepcopy(row["bindings_draft"])
    if row["domain"] == "common":
        snapshot = "catalog/identity-snapshots/" + identifier + "/" + revision + ".json"
        prefix = row["definition_pointer"]
        for binding in bindings:
            if binding["path"] != row["definition_path"]:
                continue
            pointer = binding.get("pointer")
            _require(isinstance(pointer, str) and (pointer == prefix or pointer.startswith(prefix + "/")),
                     "common metadata selector is outside its case")
            pointer = pointer[len(prefix):]
            binding.update(path=snapshot, pointer=pointer,
                           sha256=_canonical(_pointer(row["canonical_definition"], pointer)))
    return bindings


@_case_boundary
def validate_common_verification(root, row, source_contract):
    """Bind an immutable common receipt to its exact case and source release.

    The generic identity artifact verifier checks ZIP members. Here source
    hashes, saved receipt processes/criteria, and the receipt's immutable
    acquisition-registry snapshot are checked without rerunning calculations.
    Generated JSON outputs may differ bytewise from stored reference outputs,
    as allowed by the original nonempty-artifact and numerical checks.
    """
    _require(row["domain"] == "common", "common verification needs a common case")
    case = row["canonical_definition"]
    _require(case["id"] == row["legacy_id"], "common definition identity differs")
    expected = {"manifest_path": row["source_manifest"], "manifest_sha256": row["source_manifest_sha256"],
                "archive_path": row["source_archive"], "archive_sha256": row["source_archive_sha256"]}
    _require(isinstance(source_contract, dict)
             and all(source_contract.get(k) == v for k, v in expected.items()), "common source contract differs")
    for path_key, hash_key in (("manifest_path", "manifest_sha256"), ("archive_path", "archive_sha256")):
        _require(SHA256.fullmatch(expected[hash_key] or "")
                 and _hash(_file(root, expected[path_key])) == expected[hash_key], "common source bytes differ")
    manifest = _json(root, expected["manifest_path"])
    _require(isinstance(manifest.get("files"), dict) and manifest["files"], "common source manifest is invalid")
    receipt_path = row.get("common_receipt_path", row["verification_path"])
    _require(receipt_path.startswith("numerical-methods-atlas/code-and-data/verification/")
             and receipt_path.endswith(".json"), "common receipt must be a retained dated public record")
    receipt = _json(root, receipt_path)
    _require(receipt.get("passed") is True and receipt.get("status") == "complete"
             and receipt.get("registry_url") == ORIGIN + "/" + COMMON_PUBLIC, "common saved verification is incomplete")
    acquisition = _url_path(receipt["registry_acquisition_url"])
    _require(acquisition.startswith("code/") and "/verification-candidates/" in acquisition
             and acquisition.endswith(".json"), "common verification registry snapshot is not immutable")
    registry_sha = receipt.get("registry_sha256", "")
    _require(SHA256.fullmatch(registry_sha) and _hash(_file(root, acquisition)) == registry_sha
             and receipt.get("expected_registry_sha256") == registry_sha, "common saved registry hash differs")
    registry = _json(root, acquisition)
    recorded = _unique(registry["examples"], "id", "saved common registry")
    _require(recorded.get(case["id"]) == case, "common frozen definition differs from saved verification registry")
    examples = _unique(receipt["examples"], "id", "common saved example")
    _require(set(examples) == set(recorded), "common verification does not cover its saved registry")
    result = examples[case["id"]]
    _require(result.get("problem_id") == case["problem_id"] and result.get("passed") is True,
             "common saved case/problem identity differs")
    validation = result.get("validation", {})
    _require(validation.get("passed") is True, "common case validation did not pass")
    checks = _unique(validation.get("checks"), "id", "common numerical check")
    outputs = _unique(case["outputs"], "id", "common output")
    _require(set(checks) == {item["id"] for item in case["checks"]}
             | {"output-" + key for key in outputs}, "common verification check inventory differs")
    for category in ("checks", "expected_failures"):
        observed = _unique(validation.get(category), "id", "common " + category)
        wanted = _unique(case[category], "id", "common expected " + category)
        if category == "expected_failures":
            _require(set(observed) == set(wanted), "common expected-failure inventory differs")
        for ident, rule in wanted.items():
            actual = observed.get(ident, {})
            _require(actual.get("passed") is True and
                     all(actual.get(k) == v for k, v in rule.items() if k != "description"),
                     "common verification criterion differs")
    release = case["release"]
    candidates = [item for item in receipt["releases"]
                  if item.get("family") == release["family"] and item.get("version") == release["version"]
                  and item.get("download") == release["download"]
                  and item.get("execution", {}).get("group") == case["execution_group"]]
    _require(len(candidates) == 1, "common saved release/runner is ambiguous or missing")
    saved_release = candidates[0]
    _require(all(saved_release.get(k) == release[k] for k in ("download", "sha256", "manifest", "manifest_sha256")),
             "common saved release hashes differ")
    _require(saved_release.get("archive_bytes") == _file(root, row["source_archive"]).stat().st_size
             and saved_release.get("archived_files_verified") == len(manifest["files"]),
             "common saved archive inventory differs")
    process = saved_release.get("execution", {})
    _require(process == result.get("execution") and process.get("started") is True
             and process.get("completed") is True and process.get("exit_code") == 0
             and process.get("timed_out") is False
             and process.get("shared_runner_cases") == case["shared_runner_cases"]
             and case["id"] in process["shared_runner_cases"], "common saved execution is incomplete or wrong")
    _require(saved_release.get("setup", {}).get("passed") is True
             and saved_release["setup"].get("phase") == "complete", "common saved setup did not pass")
    artifacts = _unique(saved_release["downloaded_artifacts"], "url", "common downloaded artifact")
    base = row["source_manifest"].rsplit("/", 1)[0] + "/"
    for artifact in [case["inputs"], *case["outputs"]]:
        path = _url_path(artifact["url"])
        _require(path.startswith(base) and manifest["files"].get(path[len(base):]) == artifact["sha256"]
                 and _hash(_file(root, path)) == artifact["sha256"], "common case artifact differs from its manifest")
        saved = artifacts.get(artifact["url"], {})
        _require(saved.get("sha256") == artifact["sha256"]
                 and saved.get("bytes") == _file(root, path).stat().st_size, "common downloaded artifact record differs")
    for ident, output in outputs.items():
        observed = checks["output-" + ident]
        _require(observed.get("passed") is True and observed.get("comparison") == "nonempty_artifact"
                 and observed.get("generated_path") == output["generated_path"]
                 and type(observed.get("bytes")) is int and observed["bytes"] > 0
                 and SHA256.fullmatch(observed.get("sha256", "")), "common generated output record is invalid")
    return {"passed": True, "receipt_path": receipt_path,
            "receipt_sha256": _hash(_file(root, receipt_path)),
            "registry_snapshot_path": acquisition, "registry_sha256": registry_sha,
            "case_pointer": "/examples/" + str(list(examples).index(case["id"])),
            "release_pointer": "/releases/" + str(receipt["releases"].index(saved_release))}
