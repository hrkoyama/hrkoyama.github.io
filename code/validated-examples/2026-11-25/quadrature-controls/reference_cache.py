"""Verify the portable qualified scalar cache before primary rows."""
from pathlib import Path
import hashlib
import json
import math


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(source):
    source = Path(source)
    cache = json.loads((source/"references/reference-cache.json").read_text())
    qualification_path = source/"references/qualification.json"
    qualification = json.loads(qualification_path.read_text())
    if not (cache["qualified"] is True and qualification["passed"] is True
            and cache["qualification_sha256"] == digest(qualification_path)
            and qualification["check_count"] == len(qualification["checks"]) == 188
            and all(v is True for v in qualification["checks"].values())
            and cache["source_sha256"] == qualification["source_sha256"]
            and cache["input_sha256"] == digest(source/"inputs.json")
            and cache["acceptance_sha256"] == digest(source/"acceptance.json")):
        raise ValueError("Unqualified or stale reference cache")
    for name, expected in cache["source_sha256"].items():
        if digest(source/name) != expected:
            raise ValueError("Changed qualified source: "+name)
    if len(cache["targets"]) != 30:
        raise ValueError("Reference target count differs")
    return cache["targets"]


def bounds(record):
    # Decimal strings were outward-enclosed before caching. Float endpoints
    # expand once more to contain the decimal-to-binary conversion.
    return math.nextafter(float(record["lower"]), -math.inf), math.nextafter(float(record["upper"]), math.inf)


def error_interval(value, record):
    low, high = bounds(record)
    lower = max(0.0, math.nextafter(max(0.0, low-value, value-high), -math.inf))
    upper = math.nextafter(max(abs(value-low), abs(value-high)), math.inf)
    return lower, upper


def goal(lower, upper, tolerance):
    return True if upper <= tolerance else False if lower > tolerance else None


def midpoint(record):
    low, high = bounds(record)
    return low+(high-low)/2
