"""Post-measurement reporting scope; never changes a numerical target decision."""
import hashlib
import json
import math
from pathlib import Path

CASE_ID = 'van-der-pol-stiff-transition'
RUN_ID = 'vdp-mu1-sdirk-doubling-tight'
GOAL_ID = 'vdp-mu1-adaptive-tight:accuracy'
REPORT_IDS = ['vdp-mu1-adaptive-tight:original-goal-outcome-faithfully-reported',
              'vdp-mu1-adaptive-tight:accepted-local-controls-satisfied',
              'vdp-mu1-adaptive-tight:immutable-original-failure-bound']


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verified_file(root, relative, expected):
    root = Path(root).resolve(strict=True)
    path = root/relative
    if Path(relative).is_absolute() or '..' in Path(relative).parts or not path.is_file() or path.is_symlink() or not path.resolve(strict=True).is_relative_to(root):
        raise ValueError('Unsafe or missing original evidence')
    if digest(path) != expected:raise ValueError('Changed original failure evidence')
    return path


def validate_policy_shape(policy):
    if (policy.get('schema_version') != 1 or policy.get('case_id') != CASE_ID or
        policy.get('run_id') != RUN_ID or policy.get('original_gate_id') != GOAL_ID or
        policy.get('threshold_pointer') != '/vdp/adaptive_tight_sampled_linf' or
        policy.get('current_false_required') is not False or policy.get('new_check_ids') != REPORT_IDS):
        raise ValueError('Foreign or broadened reporting scope')


def verify_history(source):
    source = Path(source)
    policy = json.loads((source/'reporting-policy.json').read_text())
    validate_policy_shape(policy)
    if digest(source/'inputs.json') != policy['original_input_sha256'] or digest(source/'acceptance.json') != policy['original_acceptance_sha256']:
        raise ValueError('Reporting scope cannot change original input or acceptance')
    history = source/policy['history_directory']
    for name, expected in policy['history_files_sha256'].items():verified_file(history, name, expected)
    original = json.loads((history/'original-result.json').read_text())
    pathmap = json.loads((history/'source-pathmap.json').read_text())
    if set(pathmap) != set(policy['historical_source_files_sha256']):raise ValueError('Incomplete original source path map')
    for name, expected in policy['historical_source_files_sha256'].items():
        if pathmap[name]['sha256'] != expected:raise ValueError('Original source hash map changed')
        verified_file(history, pathmap[name]['file'], expected)
    decisions = [value for case in original['cases'] for value in case['checks'].values()]
    if (original.get('passed') is not False or len(decisions) != 209 or sum(v is True for v in decisions) != 208 or
        any(type(v) is not bool for v in decisions) or original['input_sha256'] != policy['original_input_sha256']):
        raise ValueError('Original first failure was lost or relabeled')
    oldcase = next(c for c in original['cases'] if c['id'] == CASE_ID)
    if oldcase['checks'][GOAL_ID] is not False:raise ValueError('Original unmet goal must remain false in historical evidence')
    return {'passed': True, 'original_result_sha256': digest(history/'original-result.json'),
            'original_input_sha256': policy['original_input_sha256'], 'original_acceptance_sha256': policy['original_acceptance_sha256'],
            'first_study': {'met':208,'total':209,'all_met':False}, 'current_outcome_not_fixed':True}


def faithful_disclosure(study, measured_error, threshold, decision):
    # Both outcomes are allowed. There is no current expected-failure mask.
    return (type(decision) is bool and type(study.get('target_met')) is bool and
            study['target_met'] is decision and decision == bool(measured_error <= threshold) and
            study.get('requested_global_bound') == threshold and
            study.get('actual_sampled_weighted_linf') == measured_error and
            study.get('post_measurement_scope_revision') is True)


def evaluate(source, case, record, trials, threshold):
    history = verify_history(source)
    value = record['sampled_weighted_linf']
    decision = case['original_target_results'][GOAL_ID]
    accepted = [row for row in trials if row['accepted']]
    local_good = bool(accepted) and all(type(row['accepted']) is bool and isinstance(row['error_ratio'],(int,float)) and
                                     math.isfinite(row['error_ratio']) and 0 <= row['error_ratio'] <= 1 for row in accepted)
    study = {'original_gate_id': GOAL_ID, 'requested_global_bound': threshold,
             'actual_sampled_weighted_linf': value, 'target_met': bool(decision),
             'accepted_local_controls_satisfied': bool(local_good),
             'post_measurement_scope_revision': True, 'original_failure_evidence': history,
             'scope': 'Current protocol verifies faithful reporting; it does not assert this original global accuracy goal was met.'}
    checks = {REPORT_IDS[0]: faithful_disclosure(study,value,threshold,decision),
              REPORT_IDS[1]: local_good, REPORT_IDS[2]: history['passed']}
    return study, checks
