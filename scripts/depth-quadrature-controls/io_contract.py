"""Owned callback and row retention; JSON is finite, raw arrays precede diagnostics."""
from pathlib import Path
import json
import math
import csv
import numpy as np


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


class Trace:
    def __init__(self, directory, row_id, checkpoint=512):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.stem = row_id.replace(":", "__")
        self.points, self.values = [], []
        self.last_attempt = None
        self.checkpoint = checkpoint

    def begin(self, point):
        coordinates = list(point) if isinstance(point, (list, tuple)) else float(point)
        self.last_attempt = {"point": coordinates, "completed": False}

    def record(self, point, value):
        coordinates = tuple(point) if isinstance(point, (list, tuple)) else (point,)
        self.points.append(tuple(float(x) for x in coordinates))
        self.values.append(float(value))
        if self.last_attempt is not None:
            self.last_attempt["completed"] = True
        if len(self.values) % self.checkpoint == 0:
            self.save()

    def wrap(self, function):
        def evaluate(x):
            self.begin(x)
            value = float(function(x))
            if not math.isfinite(value):
                raise ValueError("Nonfinite callback")
            self.record(x, value)
            self.last_attempt["completed"] = True
            return value
        return evaluate

    def save(self):
        # Owned numeric arrays saved even if subsequent JSON/diagnostics fail.
        np.savez_compressed(self.directory/(self.stem+"-callbacks.npz"),
                            points=np.asarray(self.points, dtype=float),
                            values=np.asarray(self.values, dtype=float))
        write_json(self.directory/(self.stem+"-callback-status.json"),
                   {"completed_callbacks": len(self.values), "last_attempt": self.last_attempt})


def save_candidate(directory, row_id, candidate):
    stem = row_id.replace(":", "__")
    arrays = {}

    def extract(value, name):
        if isinstance(value, np.ndarray):
            arrays[name] = np.array(value, copy=True)
            return {"raw_array": name}
        if isinstance(value, np.generic):
            return extract(value.item(), name)
        if isinstance(value, float) and not math.isfinite(value):
            arrays[name] = np.asarray(value)
            return {"raw_nonfinite_scalar": name}
        if isinstance(value, dict):
            return {str(k): extract(v, name+"__"+str(k)) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            if name.rsplit("__", 1)[-1] in ("keys", "points", "weights", "values", "rows"):
                arrays[name] = np.array(value, copy=True)
                return {"raw_array": name}
            return [extract(v, name+"__"+str(i)) for i, v in enumerate(value)]
        return value

    metadata = extract(candidate, "candidate")
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path/(stem+".npz"), **arrays)
    write_json(path/(stem+".json"), metadata)


def write_csv(path, records):
    columns = ["index", "sequence", "method_code", "dimension", "absolute_tolerance",
               "step", "cutoff", "level", "evaluations", "value", "error_lower",
               "error_upper", "estimated_error", "converged", "accuracy_goal_met"]
    with Path(path).open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(columns)
        for index, row in enumerate(records):
            values = {**row, "index": index}
            output = []
            for name in columns:
                value = values.get(name)
                if value is None:
                    output.append("")
                else:
                    number = float(value)
                    if not math.isfinite(number):
                        raise ValueError("Nonfinite numeric CSV")
                    output.append(str(int(value)) if isinstance(value, bool) else str(value))
            writer.writerow(output)
