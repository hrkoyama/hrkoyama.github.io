"""Exact current Atlas identity coverage, separate from immutable old revisions.

This module compares sidecars with the published catalogs and frozen packages.
It does not import a solver, regenerate a reference or run a numerical case.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.parse import urlsplit, unquote

PILOT_CHECKPOINT_SHA256 = "3f747b9b2e9cd436baca0bebddf5b65e2843035aa38a8ee98fbdb6b94fc6b557"
# Filled once after the reviewed first expansion is generated; never regenerated
# from later mutable registries.
EXPANSION_CHECKPOINT_SHA256 = "fd177d1229d127135b3a415deb9e806df0bd258085fe40f57edf59c496377643"


def _core():
    # Called after atlas_identities has finished loading, avoiding an import cycle.
    import atlas_identities
    return atlas_identities


def _revision(entity):
    return next(r for r in entity["revisions"] if r["revision"] == entity["current_revision"])


def _state_key(revision):
    manifests = [b for b in revision["bindings"] if b["role"] == "source-manifest"]
    archives = [b for b in revision["bindings"] if b["role"] == "archive"]
    _core().require(len(manifests) == 1 and len(archives) <= 1, "source manifest/archive cardinality")
    return manifests[0]["path"], archives[0]["path"] if archives else None


def _descriptor_key(source):
    return source["source_manifest"]["path"], source["archive"]["path"] if source.get("archive") else None


def _selector_set(bindings):
    return {_core().binding_key(b) for b in bindings}


def _local_url(value):
    parsed = urlsplit(value)
    _core().require(parsed.scheme == "https" and parsed.netloc == "hrkoyama.github.io"
                    and not parsed.query and not parsed.fragment, "non-HR source metadata URL")
    return unquote(parsed.path.lstrip("/"))


def inventory(root):
    """Return current authorities; no identity numbers are inferred here."""
    from atlas_identity_sources import source_inventory
    from atlas_identity_cases import case_inventory
    core = _core()
    root = Path(root)
    problems = core.load_json(core.safe_path(root, "catalog/atlas-test-problems.json"))["problems"]
    cases = case_inventory(root)
    sources = source_inventory(root)
    core.require(len({p["id"] for p in problems}) == len(problems), "duplicate canonical problem")
    core.require(len({c["legacy_id"] for c in cases}) == len(cases), "duplicate canonical case")
    core.require(len({_descriptor_key(s) for s in sources}) == len(sources), "duplicate current source state")
    return problems, cases, sources


def source_problem_ids(problems, cases, sources):
    """Known relationships only; a frozen S summary is not an exhaustive C join."""
    result = {_descriptor_key(s): set() for s in sources}
    for case in cases:
        key = case["source_manifest"], case["source_archive"]
        _core().require(key in result, "registered case has no current source unit")
        result[key].update(case["problem_ids"])
    for source in sources:
        key = _descriptor_key(source)
        prefix = source.get("root", "").rstrip("/")
        archive = source.get("archive")
        archive_path = archive["path"] if archive else None
        for problem in problems:
            for evidence in problem.get("evidence", []):
                path = evidence.get("path", "")
                if path and (path == archive_path or prefix and path.startswith(prefix + "/")):
                    result[key].add(problem["id"])
    return result


def _frozen_pilot(root):
    path = _core().safe_path(root, "catalog/atlas-identity-history.json")
    _core().require(hashlib.sha256(path.read_bytes()).hexdigest() == PILOT_CHECKPOINT_SHA256,
                    "frozen pilot checkpoint bytes changed")
    data = _core().load_json(path)
    return {e["id"]: e for e in data["entities"]}


def _frozen_source_states(root):
    items = list(_frozen_pilot(root).values())
    path = Path(root) / "catalog/atlas-identity-expansion-history.json"
    if path.exists():
        _core().require(EXPANSION_CHECKPOINT_SHA256 is not None and
                        hashlib.sha256(path.read_bytes()).hexdigest() == EXPANSION_CHECKPOINT_SHA256,
                        "frozen expansion checkpoint bytes changed")
        items.extend(_core().load_json(path)["entities"])
    return {f"{e['id']}@{r['revision']}": r
            for e in items if e["kind"] == "source" for r in e["revisions"]}


def _source_revision_rules(root):
    return _core().load_json(_core().safe_path(root, "catalog/atlas-identity-sources.json"))["family_revisions"]


def _case_snapshot(root, identifier, revision):
    core = _core()
    expected = f"catalog/identity-snapshots/{identifier}/{revision['revision']}.json"
    definitions = [b for b in revision["bindings"] if b["role"] == "case-definition"]
    core.require(len(definitions) == 1 and definitions[0]["path"] == expected
                 and definitions[0].get("pointer") == "" and "member" not in definitions[0],
                 f"common case needs its immutable definition snapshot: {identifier}")
    return core.load_json(core.safe_path(root, expected)), expected


def validate_current_coverage(root, data, entities, snapshots):
    """Validate the current inventory once, never impose it on old baselines."""
    from atlas_identity_cases import (case_bindings, common_row_from_snapshot,
                                      validate_common_verification)
    from atlas_identity_sources import source_contract
    core = _core()
    root = Path(root)
    problems, cases, sources = inventory(root)
    pilot = _frozen_pilot(root)
    problem_records = {p["id"]: p for p in problems}
    expected_cases = {c["legacy_id"]: c for c in cases}
    expected_sources = {_descriptor_key(s): s for s in sources}
    explicit_source_revisions = _source_revision_rules(root)
    p_entities = [e for e in entities.values() if e["kind"] == "problem"]
    c_entities = [e for e in entities.values() if e["kind"] == "case"]
    s_entities = [e for e in entities.values() if e["kind"] == "source"]
    p_by_legacy, c_by_legacy = {}, {}
    for group, target, label in [(p_entities, p_by_legacy, "problem"), (c_entities, c_by_legacy, "case")]:
        for entity in group:
            core.require(len(entity["legacy_ids"]) == 1, f"{label} identity merges canonical units")
            alias = entity["legacy_ids"][0]
            core.require(alias not in target, f"duplicate canonical {label} identity")
            target[alias] = entity
    core.require(set(p_by_legacy) == set(problem_records), "incomplete current problem identity coverage")
    core.require(set(c_by_legacy) == set(expected_cases), "incomplete current case identity coverage")
    p_refs = {alias: f"{e['id']}@{e['current_revision']}" for alias, e in p_by_legacy.items()}
    for alias, entity in p_by_legacy.items():
        revision = _revision(entity)
        expected_path = f"catalog/identity-snapshots/{entity['id']}/{revision['revision']}.json"
        bindings = revision["bindings"]
        core.require(len(bindings) == 1 and bindings[0]["role"] == "problem"
                     and bindings[0]["path"] == expected_path and bindings[0].get("pointer") == "",
                     f"problem must use an immutable full-record snapshot: {alias}")
        frozen = core.load_json(core.safe_path(root, expected_path))
        core.require(core.canonical_sha256(frozen) == core.canonical_sha256(problem_records[alias]),
                     f"current problem differs from its frozen identity: {alias}")
    contracts, source_refs, unit_entities = {}, {}, {}
    related = source_problem_ids(problems, cases, sources)
    for entity in s_entities:
        active_units = set()
        for revision in entity["revisions"]:
            ref = f"{entity['id']}@{revision['revision']}"
            key = _state_key(revision)
            if key not in expected_sources:
                core.require(_frozen_source_states(root).get(ref) == revision,
                             f"unfrozen historical source state: {ref}")
                contracts[ref] = source_contract(root, revision)
                continue
            source = expected_sources[key]
            prescribed = explicit_source_revisions.get(source["unit_key"], {}).get(source["edition"])
            core.require(prescribed is None or revision["revision"] == prescribed,
                         f"known source edition has wrong identity revision: {ref}")
            contracts[ref] = source_contract(root, revision)
            active_units.add(source["unit_key"])
            core.require(key not in source_refs, "current source state assigned more than once")
            source_refs[key] = ref
            if entity["id"] in pilot and revision["revision"] == "00":
                expected = pilot[entity["id"]]["revisions"][0]["bindings"]
            else:
                expected = source["bindings"]
            core.require(_selector_set(revision["bindings"]) == _selector_set(expected),
                         f"incomplete or unexpected source bindings: {ref}")
            allowed_problems = related[key]
            declared = {r.split("@", 1)[0] for r in revision["problem_refs"]}
            permitted = {p_by_legacy[p]["id"] for p in allowed_problems}
            core.require(declared.issubset(permitted), f"source claims an unrelated problem: {ref}")
        core.require(len(active_units) == 1, f"source identity has no current unit or merges units: {entity['id']}")
        unit = next(iter(active_units))
        core.require(unit not in unit_entities, f"source unit split across identities: {unit}")
        unit_entities[unit] = entity["id"]
        if entity["id"] not in pilot:
            genuine_aliases = set()
            for revision in entity["revisions"]:
                for binding in revision["bindings"]:
                    if binding["role"] in {"archive", "source"}:
                        genuine_aliases.add(binding["path"])
            core.require(set(entity["legacy_ids"]).issubset(genuine_aliases),
                         f"source aliases are not existing published paths: {entity['id']}")
    core.require(set(source_refs) == set(expected_sources), "incomplete current source identity coverage")
    core.require(len(unit_entities) == len({s["unit_key"] for s in sources}),
                 "incomplete current source unit coverage")
    allowed_external = {}
    null_cases = []
    for alias, case in expected_cases.items():
        entity = c_by_legacy[alias]
        current = _revision(entity)
        expected_p = {p_refs[p] for p in case["problem_ids"]}
        expected_s = [source_refs[(case["source_manifest"], case["source_archive"])]]
        core.require(set(current["problem_refs"]) == expected_p,
                     f"case has missing or unrelated problem references: {alias}")
        core.require(current["source_refs"] == expected_s,
                     f"case uses the wrong or additional source unit: {alias}")
        if not expected_p:
            null_cases.append(alias)
        if entity["id"] in pilot and current["revision"] == "00":
            expected_bindings = pilot[entity["id"]]["revisions"][0]["bindings"]
        else:
            expected_bindings = case_bindings(root, case, entity["id"], current["revision"])
        core.require(_selector_set(current["bindings"]) == _selector_set(expected_bindings),
                     f"case has incomplete or unexpected bindings: {alias}")
        if case["domain"] != "common":
            continue
        for revision in entity["revisions"]:
            frozen, snapshot_path = _case_snapshot(root, entity["id"], revision)
            if revision is current:
                core.require(core.canonical_sha256(frozen) == core.canonical_sha256(case["canonical_definition"]),
                             f"current common case differs from its frozen contract: {alias}")
                frozen_row = case
            else:
                receipts = [b for b in revision["bindings"] if b["role"] == "saved-verification"]
                core.require(len(receipts) == 1, "historical common receipt cardinality")
                frozen_row = common_row_from_snapshot(root, frozen, receipts[0]["path"])
            ref = f"{entity['id']}@{revision['revision']}"
            core.require(len(revision["source_refs"]) == 1, "common source reference cardinality")
            source_ref = revision["source_refs"][0]
            source_revision = snapshots[source_ref]
            manifests = [b for b in source_revision["bindings"] if b["role"] == "source-manifest"]
            archives = [b for b in source_revision["bindings"] if b["role"] == "archive"]
            core.require(len(manifests) == len(archives) == 1, "common source needs manifest/archive")
            validate_common_verification(root, frozen_row, {
                "manifest_path": manifests[0]["path"], "manifest_sha256": manifests[0]["sha256"],
                "archive_path": archives[0]["path"], "archive_sha256": archives[0]["sha256"],
            })
            expected = case_bindings(root, frozen_row, entity["id"], revision["revision"])
            core.require(_selector_set(revision["bindings"]) == _selector_set(expected),
                         f"common historical bindings differ from frozen contract: {ref}")
            allowed_external[ref] = {
                core.binding_key(b) for b in expected
                if b["path"] == snapshot_path or b["role"] == "saved-verification"
            }
    report = {
        "coverage": "atlas-current", "complete_current_inventory": True,
        "canonical_problems": len(problems), "registered_cases": len(cases),
        "supplement_cases": sum(c["domain"] != "common" for c in cases),
        "common_examples": sum(c["domain"] == "common" for c in cases),
        "source_units": len(unit_entities), "active_source_revisions": len(source_refs),
        "current_source_archives": sum(bool(s.get("archive")) for s in sources),
        "unarchived_source_units": len({s["unit_key"] for s in sources if not s.get("archive")}),
        "diagnostic_cases_without_problem": sorted(null_cases),
        "problems_without_registered_case": sorted(set(problem_records) -
            {p for c in cases for p in c["problem_ids"]}),
        "source_problem_refs_are_nonexhaustive_frozen_summaries": True,
    }
    return {"source_contracts": contracts,
            "allowed_external_case_bindings": allowed_external, "report": report}
