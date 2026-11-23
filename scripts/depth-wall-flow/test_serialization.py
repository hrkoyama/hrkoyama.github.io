"""Regression for attempt01: the independent table qualifier must be JSON-native."""
import json
import wall_flow
from references.qualify_reference import qualify


def test_reference_qualification_serializes_without_numpy_scalar_adapter():
    report = qualify(wall_flow.manufactured)
    assert all(type(value) is bool for value in report['checks'].values())
    decoded = json.loads(json.dumps(report, allow_nan=False))
    assert decoded == report and decoded['passed'] is True
