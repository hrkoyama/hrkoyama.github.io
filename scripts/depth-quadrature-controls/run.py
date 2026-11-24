"""Run all105 fixed rows and preserve raw evidence before later diagnostics."""
from pathlib import Path
import argparse
import hashlib
import json
import time
from experiments import run_row
from reference_cache import load
from io_contract import write_json, write_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("inputs.json"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    config = json.loads(args.input.read_text())
    if hashlib.sha256(args.input.read_bytes()).hexdigest() != hashlib.sha256((source/"inputs.json").read_bytes()).hexdigest():
        raise ValueError("Only the frozen input is supported")
    acceptance = json.loads((source/"acceptance.json").read_text())
    references = load(source)
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    completed, cases, decisions, failure = [], [], {}, None
    try:
        for case_id in config["case_ids"]:
            records, checks = [], {}
            for row in config["primary_rows"]:
                if row["case_id"] != case_id:
                    continue
                record, row_checks = run_row(row, args.output, references, acceptance)
                records.append(record)
                completed.append(record)
                checks.update(row_checks)
                write_json(args.output/"partial-result.json", {"completed_records": completed, "completed_checks": checks})
            expected = config["case_row_counts"][str(records[0]["sequence"])]
            checks[case_id+":fixed-record-count"] = len(records) == expected
            checks[case_id+":unique-record-ids"] = len({r["row_id"] for r in records}) == expected
            metrics = {"records": len(records), "integrand_evaluations": sum(r["evaluations"] for r in records),
                       "accuracy_goals_met": sum(r["accuracy_goal_met"] is True for r in records),
                       "accuracy_goals_unmet": sum(r["accuracy_goal_met"] is False for r in records),
                       "accuracy_goals_unresolved": sum(r["accuracy_goal_met"] is None for r in records),
                       "estimated_converged_rows": sum(r["converged"] for r in records)}
            case = {"id": case_id, "passed": all(checks.values()), "checks": checks,
                    "metrics": metrics, "records": records}
            cases.append(case)
            decisions[case_id] = case["passed"]
            write_csv(args.output/(case_id+".csv"), records)
    except BaseException as error:
        failure = {"type": type(error).__name__, "message": str(error)}
    finally:
        result = {"schema_version": 1, "passed": failure is None and len(completed) == 105 and all(decisions.values()),
                  "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  "termination": "completed_fixed_protocol" if failure is None else "failed_fixed_protocol",
                  "failure": failure, "checks": decisions, "cases": cases,
                  "primary_records": len(completed), "duration_seconds": time.monotonic()-started,
                  "reference_cache_sha256": hashlib.sha256((source/"references/reference-cache.json").read_bytes()).hexdigest()}
        write_json(args.output/"result.json", result)
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
