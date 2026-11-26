#!/usr/bin/env python3
"""Prepare reviewed append-only identity sidecars; never execute numerical code.

Existing revisions and snapshots are retained. A changed existing case/problem
requires a separately reviewed revision; this tool does not silently overwrite it.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

from atlas_identities import (IdentityError, canonical_sha256, format_revision,
                              load_json, parse_id, require, validate_registry)
from atlas_identity_coverage import inventory, source_problem_ids
from atlas_identity_cases import case_bindings

REGISTRY = "catalog/atlas-identities.json"
CHECKPOINT = "catalog/atlas-identity-expansion-history.json"


def render(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def source_key(revision):
    manifest = next(b for b in revision["bindings"] if b["role"] == "source-manifest")
    archive = next((b for b in revision["bindings"] if b["role"] == "archive"), None)
    return manifest["path"], archive["path"] if archive else None


def descriptor_key(source):
    return source["source_manifest"]["path"], source["archive"]["path"] if source.get("archive") else None


def entity(identifier, kind, aliases, revisions):
    return {"id": identifier, "kind": kind, "legacy_ids": aliases,
            "current_revision": revisions[-1]["revision"], "revisions": revisions}


def prepare(root, previous):
    problems, cases, sources = inventory(root)
    data = copy.deepcopy(previous)
    data["scope"] = "atlas-current"
    existing = {e["id"]: e for e in data["entities"]}
    pending = {}

    def allocate(letter):
        serial = data["allocation"][letter]
        data["allocation"][letter] += 1
        return f"NMA-{letter}-{serial:06d}"

    def add_snapshot(path, value):
        target = root / path
        if target.exists():
            require(canonical_sha256(load_json(target)) == canonical_sha256(value),
                    f"immutable snapshot differs; review a new revision: {path}")
        else:
            pending[path] = value

    problem_entities = {alias: e for e in existing.values() if e["kind"] == "problem"
                        for alias in e["legacy_ids"]}
    for problem in sorted(problems, key=lambda p: p["id"]):
        alias = problem["id"]
        if alias not in problem_entities:
            identifier = allocate("P")
            path = f"catalog/identity-snapshots/{identifier}/00.json"
            add_snapshot(path, problem)
            revision = {"revision": "00", "label": copy.deepcopy(problem["name"]),
                        "problem_refs": [], "source_refs": [],
                        "bindings": [{"role": "problem", "path": path, "pointer": "",
                                      "sha256": canonical_sha256(problem)}]}
            item = entity(identifier, "problem", [alias], [revision])
            existing[identifier] = item
            problem_entities[alias] = item
    problem_refs = {alias: f"{e['id']}@{e['current_revision']}" for alias, e in problem_entities.items()}
    relationships = source_problem_ids(problems, cases, sources)
    by_unit = {}
    for source in sources:
        by_unit.setdefault(source["unit_key"], []).append(source)
    registered_sources = {source_key(rev): (e, rev) for e in existing.values() if e["kind"] == "source"
                          for rev in e["revisions"]}
    for unit, states in sorted(by_unit.items()):
        states = sorted(states, key=lambda s: (s.get("revision_hint", "00"), s["edition"], descriptor_key(s)[0]))
        known = {registered_sources[descriptor_key(s)][0]["id"] for s in states if descriptor_key(s) in registered_sources}
        require(len(known) <= 1, f"one source family already split across IDs: {unit}")
        item = existing[next(iter(known))] if known else None
        if item is None:
            identifier = allocate("S")
            aliases = sorted({s["archive"]["path"] if s.get("archive") else
                              next(b["path"] for b in s["bindings"] if b["role"] == "source")
                              for s in states})
            item = entity(identifier, "source", aliases, [{"revision": "00"}])
            item["revisions"] = []
            existing[identifier] = item
        for source in states:
            key = descriptor_key(source)
            if key in registered_sources:
                continue
            revision = {"revision": format_revision(len(item["revisions"])),
                        "label": copy.deepcopy(source["label"]),
                        "problem_refs": sorted(problem_refs[p] for p in relationships[key]),
                        "source_refs": [], "bindings": copy.deepcopy(source["bindings"])}
            item["revisions"].append(revision)
            registered_sources[key] = item, revision
        require(item["revisions"], f"empty source family: {unit}")
        item["current_revision"] = item["revisions"][-1]["revision"]
    source_refs = {key: f"{item['id']}@{revision['revision']}"
                   for key, (item, revision) in registered_sources.items()}
    registered_cases = {alias: e for e in existing.values() if e["kind"] == "case"
                        for alias in e["legacy_ids"]}
    for case in sorted(cases, key=lambda c: c["legacy_id"]):
        alias = case["legacy_id"]
        if alias in registered_cases:
            continue
        identifier = allocate("C")
        if case["domain"] == "common":
            add_snapshot(f"catalog/identity-snapshots/{identifier}/00.json", case["canonical_definition"])
        bindings = case_bindings(root, case, identifier)
        revision = {"revision": "00", "label": copy.deepcopy(case["label"]),
                    "problem_refs": sorted(problem_refs[p] for p in case["problem_ids"]),
                    "source_refs": [source_refs[(case["source_manifest"], case["source_archive"])]],
                    "bindings": bindings}
        existing[identifier] = entity(identifier, "case", [alias], [revision])
    order = {"problem": 0, "case": 1, "source": 2}
    data["entities"] = sorted(existing.values(), key=lambda e: (order[e["kind"]], parse_id(e["id"])[1]))
    return data, pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write new reviewed sidecars, never modify scientific distributions")
    mode.add_argument("--check", action="store_true", help="Fail if new allocations/snapshots are required")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        previous = load_json(root / REGISTRY)
        planned, pending = prepare(root, previous)
        if args.check:
            require(planned == previous and not pending, "identity sidecars need a reviewed append")
            require((root / CHECKPOINT).is_file(), "expanded identity checkpoint missing")
        else:
            for path, value in pending.items():
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                require(not target.exists(), f"refusing snapshot overwrite: {path}")
                target.write_text(render(value), encoding="utf-8")
            # Validate all bytes and links before replacing the current registry.
            validate_registry(root, planned, previous)
            if previous["scope"] == "pilot":
                require(not (root / CHECKPOINT).exists(), "initial expansion checkpoint already exists")
                (root / CHECKPOINT).write_text(render(planned), encoding="utf-8")
            else:
                require((root / CHECKPOINT).is_file(), "expanded checkpoint must not be recreated")
            (root / REGISTRY).write_text(render(planned), encoding="utf-8")
        print(json.dumps({"passed": True, "numerical_execution": False,
                          "scope": planned["scope"], "entities": len(planned["entities"]),
                          "allocation": planned["allocation"], "new_snapshots": len(pending)}))
        return 0
    except (IdentityError, ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"passed": False, "numerical_execution": False, "error": str(error)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
