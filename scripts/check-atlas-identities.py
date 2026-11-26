#!/usr/bin/env python3
"""Check Atlas identity records without running numerical code."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from atlas_identities import IdentityError, load_json, safe_path, validate_registry


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
        frozen = load_json(safe_path(args.root, "catalog/atlas-identity-history.json"))
        report = validate_registry(args.root, data, frozen)
        if args.baseline:
            report = validate_registry(args.root, data, load_json(args.baseline))
        report["additional_baseline_checked"] = args.baseline is not None
        report["git_baseline_checked"] = False
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
                from atlas_identities import parse_json
                validate_registry(args.root, data, parse_json(previous.stdout))
                report["git_baseline_checked"] = True
            report["previous_registry_found"] = bool(listed.stdout.strip())
    except (IdentityError, OSError, KeyError, TypeError) as exc:
        report = {"passed": False, "validation_type": "saved-artifact-integrity-only", "numerical_execution": False, "errors": [str(exc)]}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
