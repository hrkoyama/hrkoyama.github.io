"""Regression: match the real public verifier's case-keyed completion contract."""
import json
from run import result_envelope


def test_complete_public_envelope_preserves_cases_and_separates_summary_decisions():
    cases = [dict(id='first', passed=True, checks={'scientific gate': True}, metrics={'error': .01}, records=[{'n': 5}]),
             dict(id='second', passed=True, checks={'wall gate': True}, metrics={'error': .02}, records=[{'n': 9}])]
    summary = {'contract': True, 'all grids': True, 'all cases': True}
    result = result_envelope(cases, summary, input_sha256='0'*64)
    assert result['schema_version'] == 1 and result['passed'] is True
    assert result['checks'] == {'first': True, 'second': True}
    assert result['summary_checks'] == summary and result['cases'] is cases
    assert result['termination'] == 'fixed_budget_completed' and result['failure'] is None
    assert json.loads(json.dumps(result, allow_nan=False)) == result
    cases[1]['passed'] = False
    assert result_envelope(cases, summary)['passed'] is False
    cases[1]['passed'] = True
    assert result_envelope(cases, {**summary, 'contract': False})['passed'] is False
