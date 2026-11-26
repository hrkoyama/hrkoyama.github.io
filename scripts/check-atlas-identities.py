#!/usr/bin/env python3
"""Check Atlas identity records without running numerical code."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from atlas_identities import (IdentityError, file_sha256, load_json, parse_json,
                              safe_path, validate_baseline, validate_registry)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--registry", default="catalog/atlas-identities.json")
    parser.add_argument("--baseline", type=Path, help="Previously frozen identity registry; enforce append-only revisions")
    parser.add_argument("--baseline-ref", help="Exact previous Git commit SHA; check its registry as an additional baseline")
    parser.add_argument("--report", type=Path, help="Write the JSON check report outside the published registry")
    args = parser.parse_args()
    try:
        data = load_json(safe_path(args.root, args.registry))
        pilot_path = safe_path(args.root, "catalog/atlas-identity-history.json")
        baselines = [load_json(pilot_path)]
        expanded_path = args.root / "catalog/atlas-identity-expansion-history.json"
        expanded_namespace = (data["scope"] == "atlas-current" or expanded_path.exists()
                              or (args.root / "catalog/atlas-identity-sources.json").exists())
        if expanded_namespace:
            from atlas_identity_coverage import (EXPANSION_CHECKPOINT_SHA256,
                                                  PILOT_CHECKPOINT_SHA256)
            if data["scope"] != "atlas-current":
                raise IdentityError("cannot downgrade expanded identity scope")
            if file_sha256(pilot_path) != PILOT_CHECKPOINT_SHA256:
                raise IdentityError("frozen pilot checkpoint bytes changed")
            expanded_path = safe_path(args.root, "catalog/atlas-identity-expansion-history.json")
            if file_sha256(expanded_path) != EXPANSION_CHECKPOINT_SHA256:
                raise IdentityError("frozen expansion checkpoint bytes changed")
            baselines.append(load_json(expanded_path))
        frozen_count = len(baselines)
        if args.baseline:
            baselines.append(load_json(args.baseline))
        git_checked = False
        previous_found = False
        if args.baseline_ref:
            if not re.fullmatch(r"[0-9a-fA-F]{40}", args.baseline_ref):
                raise IdentityError("baseline-ref must be an exact 40-digit Git commit SHA")
            command = ["git", "-C", str(args.root)]
            commit = subprocess.run(command + ["cat-file", "-t", args.baseline_ref], text=True, capture_output=True)
            if commit.returncode or commit.stdout.strip() != "commit":
                raise IdentityError("baseline-ref commit is unavailable")
            old_path = "catalog/atlas-identities.json"
            listed = subprocess.run(command + ["ls-tree", "--name-only", args.baseline_ref, "--", old_path], text=True, capture_output=True)
            if listed.returncode:
                raise IdentityError("cannot inspect baseline-ref tree")
            if listed.stdout.strip():
                previous = subprocess.run(command + ["show", args.baseline_ref + ":" + old_path], text=True, capture_output=True)
                if previous.returncode:
                    raise IdentityError("cannot read baseline-ref registry")
                # Same strict duplicate-key and finite-number parser as files.
                baselines.append(parse_json(previous.stdout))
                git_checked = True
            previous_found = bool(listed.stdout.strip())
        # One artifact pass, with structural/append-only checks for every frozen
        # baseline. Historical checkpoints never need today's complete inventory.
        report = validate_registry(args.root, data, baselines[0])
        for baseline in baselines[1:]:
            validate_registry(args.root, baseline, check_artifacts=False, _historical=True)
            validate_baseline(data, baseline)
        report["frozen_checkpoints_checked"] = frozen_count
        report["additional_baseline_checked"] = args.baseline is not None
        report["git_baseline_checked"] = git_checked
        if args.baseline_ref:
            report["previous_registry_found"] = previous_found
    except (IdentityError, OSError, KeyError, TypeError) as exc:
        report = {"passed": False, "validation_type": "saved-artifact-integrity-only", "numerical_execution": False, "errors": [str(exc)]}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
