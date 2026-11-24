"""Reporting integrity controls; no primary solver or reference trajectory is run."""
import copy
import json
from pathlib import Path
import pytest
import reporting_policy as policy


def test_current_goal_outcome_is_dynamic_and_cannot_be_relabelled():
    for measured, decision in [(3e-5, False), (1e-5, True)]:
        study = {'target_met': decision, 'requested_global_bound': 2e-5,
                 'actual_sampled_weighted_linf': measured, 'post_measurement_scope_revision': True}
        assert policy.faithful_disclosure(study, measured, 2e-5, decision)
        changed = dict(study, target_met=not decision)
        assert not policy.faithful_disclosure(changed, measured, 2e-5, decision)


def test_changed_evidence_and_foreign_case_scope_are_rejected(tmp_path):
    path = tmp_path/'evidence.json';path.write_text('{"passed":false}')
    original = policy.digest(path)
    assert policy.verified_file(tmp_path, path.name, original) == path
    path.write_text('{"passed":true}')
    with pytest.raises(ValueError, match='Changed original'):policy.verified_file(tmp_path, path.name, original)
    config = json.loads(Path(__file__).with_name('reporting-policy.json').read_text())
    policy.validate_policy_shape(config)
    changed = copy.deepcopy(config);changed['case_id'] = 'robertson-stiff-kinetics'
    with pytest.raises(ValueError, match='Foreign'):policy.validate_policy_shape(changed)
    changed = copy.deepcopy(config);changed['current_false_required'] = True
    with pytest.raises(ValueError, match='Foreign'):policy.validate_policy_shape(changed)
