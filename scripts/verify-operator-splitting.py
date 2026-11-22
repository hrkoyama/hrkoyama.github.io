#!/usr/bin/env python3
"""Reproduce the reading chapter's small exact-flow illustration (stdlib only).

This is a fixed two-component ODE illustration, not a general PDE solver or a
new version of the atlas's scientific-code distributions. Print JSON to stdout;
--check compares with the saved illustration without changing it.
"""
import argparse
import json
import math
from pathlib import Path


def drift(state, h):
    q, p = state
    return q + h * p, p


def kick(state, h):
    q, p = state
    return q, p - h * q


def step(state, h, method):
    if method == 'lie-trotter':
        return kick(drift(state, h), h)
    if method == 'reverse-lie-trotter':
        return drift(kick(state, h), h)
    if method == 'strang':
        return drift(kick(drift(state, h / 2), h), h / 2)
    raise ValueError(method)


def exact(t):
    return math.cos(t), -math.sin(t)


def error(state, t):
    reference = exact(t)
    return math.hypot(*(a - b for a, b in zip(state, reference)))


def compute():
    result = {
        'schema_version': 1,
        'scope': 'Fixed nondimensional harmonic-oscillator illustration; exact subflows and analytic reference. No spatial grid, general solver release or new registered benchmark.',
        'initial_state': [1.0, 0.0],
        'final_time': 1.0,
        'step_counts': [8, 16, 32, 64],
        'norm': 'Euclidean norm of (q,p) error',
        'reference_at_final_time': list(exact(1.0)),
        'methods': {},
    }
    for method in ['lie-trotter', 'reverse-lie-trotter', 'strang']:
        rows = []
        for n in result['step_counts']:
            h = 1.0 / n
            state = (1.0, 0.0)
            for _ in range(n):
                state = step(state, h, method)
            row = dict(n=n, h=h, state=list(state), global_error=error(state, 1.0),
                       local_defect=error(step((1.0, 0.0), h, method), h))
            if rows:
                for key in ['global_error', 'local_defect']:
                    row[key + '_order'] = math.log2(rows[-1][key] / row[key])
            rows.append(row)
        result['methods'][method] = rows
    # Independent commuting control: A=-I, B=-2I, exact combined flow exp(-3t).
    controls = []
    for n in result['step_counts']:
        h = 1.0 / n
        for method in ['lie-trotter', 'strang']:
            value = 1.0
            for _ in range(n):
                if method == 'lie-trotter':
                    value *= math.exp(-h)
                    value *= math.exp(-2 * h)
                else:
                    value *= math.exp(-h / 2)
                    value *= math.exp(-2 * h)
                    value *= math.exp(-h / 2)
            controls.append(dict(method=method, n=n, absolute_error=abs(value - math.exp(-3))))
    result['commuting_control'] = controls
    return result


def validate(data):
    for method, rows in data['methods'].items():
        expected = 2 if method == 'strang' else 1
        for row in rows[1:]:
            assert abs(row['global_error_order'] - expected) < 0.08, (method, row)
            assert abs(row['local_defect_order'] - expected - 1) < 0.08, (method, row)
    assert max(row['absolute_error'] for row in data['commuting_control']) < 1e-14
    assert data['methods']['lie-trotter'][0]['state'] != data['methods']['reverse-lie-trotter'][0]['state']


def compare(actual, saved):
    if isinstance(actual, dict):
        assert actual.keys() == saved.keys()
        for key in actual:
            compare(actual[key], saved[key])
    elif isinstance(actual, list):
        assert len(actual) == len(saved)
        for value, previous in zip(actual, saved):
            compare(value, previous)
    elif isinstance(actual, float):
        assert math.isclose(actual, saved, rel_tol=2e-8, abs_tol=2e-14), (actual, saved)
    else:
        assert actual == saved


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path, help='Compare a saved illustration JSON; do not write files.')
    args = parser.parse_args()
    data = compute()
    validate(data)
    if args.check:
        compare(data, json.loads(args.check.read_text()))
        print('Operator splitting: fixed-input illustration and saved values agree.')
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))
