#!/usr/bin/env python3
"""Create a small auditable full/reuse plan for public ZIP Linux verification."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys

from atlas_depth_scope import Client, InvalidEvent, SHA, plan, strict_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--github-output", type=Path, default=os.environ.get("GITHUB_OUTPUT"))
    args = parser.parse_args()
    code = 0
    try:
        event_path = Path(os.environ["GITHUB_EVENT_PATH"])
        if event_path.stat().st_size > 8 * 1024 * 1024:
            raise InvalidEvent("event-size-exceeded")
        event = strict_json(event_path.read_bytes())
        value = plan(os.environ.get("GITHUB_EVENT_NAME", ""), event, os.environ.get("GITHUB_SHA", ""),
                     os.environ.get("GITHUB_REF", ""), os.environ.get("GITHUB_REPOSITORY", ""),
                     os.environ.get("GITHUB_RUN_ID", ""), Client(os.environ.get("GITHUB_TOKEN", "")))
    except Exception as error:
        # An invalid event cannot bind a trusted successful main commit. A failed
        # planner job prevents its dependent numerical job from starting.
        target = os.environ.get("GITHUB_SHA", "")
        value = {"schema_version": 1, "mode": "blocked", "run_full": False,
                 "target_sha": target if SHA.fullmatch(target) else "",
                 "event": os.environ.get("GITHUB_EVENT_NAME", ""),
                 "reason": str(error) if isinstance(error, InvalidEvent) else "invalid-event-or-environment",
                 "error_type": type(error).__name__, "science_execution": "not-run-invalid-event",
                 "created_at_utc": datetime.now(timezone.utc).isoformat()}
        code = 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write("run_full=" + str(value["run_full"]).lower() + "\n")
            output.write("mode=" + value["mode"] + "\n")
            if SHA.fullmatch(value["target_sha"]):
                output.write("target_sha=" + value["target_sha"] + "\n")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with Path(summary).open("a", encoding="utf-8") as output:
            output.write("## Public ZIP Linux verification scope\n\n")
            output.write("- mode: " + value["mode"] + "\n- reason: " + value["reason"] + "\n")
            output.write("- target SHA: `" + value["target_sha"] + "`\n")
            baseline = value.get("baseline")
            if baseline:
                output.write("- previous actual full run: [" + str(baseline["run_id"]) + "](" + baseline["url"] + ")\n")
                output.write("- previous full SHA: `" + baseline["sha"] + "`\n")
                output.write("- previous full completed: " + baseline["completed_at"] + "\n")
            if value["mode"] == "reuse":
                output.write("\nNo numerical calculation was rerun at this SHA. Reused the linked full-run evidence after a complete safe-diff check.\n")
    print(json.dumps(value, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
