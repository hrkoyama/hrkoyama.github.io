import json
import struct
import weakref
from fractions import Fraction as F
import numpy as np
import pytest
import time_adjoint as t
from operators import TriFactor, BufferLedger, laplace, dot
from io_contract import fresh_directory, qualified_cache, save_json, digest
from qualify_references import nonsymmetric_fraction


def test_BE_step_against_exact_nonsymmetric_Fraction():
    # B=[[3,-1],[-2,4]], independently inverted exactly.
    B = TriFactor(np.array([-2.]), np.array([3., 4.]), np.array([-1.]))
    actual = B.solve(np.array([1., 2.]))
    expected = np.array([float(F(6, 10)), float(F(8, 10))])
    assert np.allclose(actual, expected, rtol=0, atol=2e-16)


def test_transpose_solve_not_symmetric_shortcut():
    B = TriFactor(np.array([-2.]), np.array([3., 4.]), np.array([-1.]))
    rhs = np.array([1., 2.]); correct = B.transpose().solve(rhs)
    assert np.allclose(correct, [float(F(8, 10)), float(F(7, 10))], rtol=0, atol=2e-16)
    assert not np.array_equal(correct, B.solve(rhs))


def test_terminal_h_weight_and_penalty_derivatives():
    u, d = np.array([.2, .4, .3]), np.array([.1, -.2, .5])
    direction = np.array([1., -2., .5]); h = 2.**-16
    fd = (t.objective(u+h*direction, d, .1, .2)-t.objective(u-h*direction, d, .1, .2))/(2*h)
    assert abs(fd-dot((u-d)/4, direction)) < 1e-11
    for index, expected in [(0, .001), (1, .004)]:
        values = [.1, .2]; values[index] += h
        plus = t.objective(u, d, *values); values[index] -= 2*h
        minus = t.objective(u, d, *values)
        assert abs((plus-minus)/(2*h)-expected) < 1e-11


def test_tangent_vs_reverse_affine_exact_control():
    assert nonsymmetric_fraction()


def test_replay_uses_correct_block_boundaries(tmp_path):
    t.full_window(3, 4, .1, .2, .1, tmp_path)
    result = t.checkpoint_window(3, 4, .1, .2, .1, 2, tmp_path)
    assert result['replay_solves'] == 4
    assert t.compare_replay(tmp_path, np.load(tmp_path/'full-states.npy'))


def test_replay_corruption_detected(tmp_path):
    t.full_window(3, 4, .1, .2, .1, tmp_path)
    t.checkpoint_window(3, 4, .1, .2, .1, 2, tmp_path)
    states = np.load(tmp_path/'full-states.npy'); states[3, 0] += .01
    assert not t.compare_replay(tmp_path, states)


def test_state_buffer_alias_ownership_counted():
    owner = np.zeros((10, 3)); factor = np.ones(7)
    ledger = BufferLedger(); ledger.observe({'view': owner[0], 'another': owner[2]}, {'factor': factor})
    assert ledger.peak_state_elements == 30
    assert ledger.peak_total_bytes == (30+7)*8
    assert ledger.report()['ownership'][0]['arrays'][1]['alias_owner'] == 'view'


def test_full_trajectory_not_live_in_checkpoint_window(tmp_path, monkeypatch):
    roots = []; original = BufferLedger.observe
    def observe(self, state, other):
        if 'states' in state: roots.append(weakref.ref(state['states']))
        if 'checkpoints' in state: assert all(r() is None for r in roots)
        return original(self, state, other)
    monkeypatch.setattr(BufferLedger, 'observe', observe)
    t.full_window(3, 4, .1, .2, .1, tmp_path)
    t.checkpoint_window(3, 4, .1, .2, .1, 2, tmp_path)
    assert all(r() is None for r in roots)


def test_streamed_failure_candidate_retained(tmp_path, monkeypatch):
    original, count = t.advance, [0]
    def broken(*args):
        count[0] += 1
        if count[0] == 3: raise ArithmeticError('injected failure')
        return original(*args)
    monkeypatch.setattr(t, 'advance', broken)
    with pytest.raises(ArithmeticError): t.checkpoint_window(3, 4, .1, .2, .1, 2, tmp_path)
    assert (tmp_path/'failed-checkpoint.npz').exists()
    assert int(np.load(tmp_path/'current-checkpoint.npz')['step']) == 2
    count[0] = 0
    with pytest.raises(ArithmeticError): t.tangent(3, 4, .1, .2, .1, tmp_path/'tangent.npz')
    saved = np.load(tmp_path/'tangent.npz')
    assert int(saved['completed_coupled_steps']) == 2
    assert all(k in saved for k in ['state', 'tangent_kappa', 'tangent_theta'])
    count[0] = 0
    with pytest.raises(ArithmeticError): t.forward_objective(3, 4, .1, .2, .1, tmp_path/'FD.npz')
    assert int(np.load(tmp_path/'FD.npz')['completed_steps']) == 2


def test_reference_binding_or_fresh_output_corruption_rejected(tmp_path):
    (tmp_path/'references').mkdir(); (tmp_path/'inputs.json').write_text('{}')
    (tmp_path/'acceptance.json').write_text('{}')
    save_json(tmp_path/'references/qualification.json', {'passed': True, 'checks': {str(i): True for i in range(67)},
              'input_sha256': 'forged', 'acceptance_sha256': digest(tmp_path/'acceptance.json'), 'source_sha256': {}, 'cache_sha256': {}})
    with pytest.raises(ValueError, match='Stale'): qualified_cache(tmp_path, tmp_path/'inputs.json', tmp_path/'acceptance.json')
    with pytest.raises(ValueError, match='fresh'): fresh_directory(tmp_path)
