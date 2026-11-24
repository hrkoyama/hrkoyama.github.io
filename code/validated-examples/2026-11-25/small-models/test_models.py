"""Small causal mathematical/ownership controls; never full training reruns."""
import csv
import json
from pathlib import Path
import numpy as np
import pytest
import pinn
import fno
import biology
from data_family import problems, values
from io_utils import Trace, Deadline, fresh, outcome, summarize
from experiments import lookup, csv_records, optimizer_return_allowed


def test_pinn_hard_boundary():
    u = pinn.fields(pinn.initial(8401), np.array([0., 1.]))[0]
    assert np.array_equal(u, np.zeros(2))


def test_pinn_parameter_draw_reproducible():
    assert len(pinn.initial(8401)) == 49
    assert np.array_equal(pinn.initial(8401), pinn.initial(8401))
    assert not np.array_equal(pinn.initial(8401), pinn.initial(8402))


def test_pinn_constant_network_product_rule():
    theta = np.zeros(49); theta[-1] = .3
    x = np.array([0., .2, .7, 1.]); u, first, second = pinn.fields(theta, x)
    assert np.allclose(u, .3*x*(1-x), atol=1e-16)
    assert np.allclose(first, .3*(1-2*x), atol=1e-16)
    assert np.allclose(second, -.6, atol=1e-16)


def test_pinn_output_bias_residual_column():
    r, j = pinn.residual(np.zeros(49), np.array([.2, .5]), True)
    assert np.allclose(j[:, -1], 2/np.pi**2, atol=1e-16)


def test_pinn_callback_cap_retains_candidate(tmp_path, monkeypatch):
    def optimizer(fun, x, **kwargs):
        fun(x); fun(x); fun(x)
    monkeypatch.setattr(pinn, 'least_squares', optimizer)
    with pytest.raises(RuntimeError, match='cap'):
        pinn.train({'seed': 8401, 'max_fun_calls': 2, 'max_jac_calls': 2}, Trace(tmp_path, 'cap'), Deadline(1))
    assert np.load(tmp_path/'cap-partial.npz')['optimizer_fun__theta'].shape == (49,)


def test_fno_parameter_layout():
    result = fno.structure(np.arange(93, dtype=float))
    assert result[4] == 92
    assert result[2][0][2][1, 0, 0] == complex(16, 17)


def test_fno_output_bias_is_not_hidden():
    theta = np.zeros(93); theta[-1] = .7
    assert np.all(fno.forward(theta, np.zeros((2, 16, 2))) == .7)


def test_fno_dc_control_direct_transform():
    theta = .05*np.arange(93)/93
    x = np.ones((1, 16, 2))
    assert np.max(np.abs(fno.forward(theta, x)-fno.forward(theta, x, direct=True))) < 1e-13


def test_fno_real_coordinate_jacobian_shape():
    y, j = fno.forward(np.zeros(93), np.ones((1, 16, 2)), True)
    assert j.shape == (1, 16, 93)
    assert np.all(j[:, :, -1] == 1)


def test_problem_split_is_whole_function():
    rows = problems()
    assert len(rows) == len({r['id'] for r in rows}) == 46
    assert {r['split'] for r in rows} == {'train', 'validation', 'test', 'ood-nu', 'ood-spectrum'}


def test_heat_initial_and_mode_decay():
    p = {'a': [1., 0., 0.], 'b': [0., 0., 0.], 'nu': .1, 'sixth_cosine': 0.}
    x = 2*np.pi*np.arange(32)/32
    assert np.max(np.abs(values(p, 32, .25)-np.exp(-.025)*np.cos(x))) < 1e-14


def test_same_function_nested_grid():
    p = problems()[0]
    assert np.max(np.abs(values(p, 64, .25)[::2]-values(p, 32, .25))) < 1e-14


def test_enzyme_two_conservation_identities():
    f = biology.enzyme(np.array([.8, .001, .009, .199]))
    assert abs(f[1]+f[2]) < 1e-16
    assert abs(f[0]+f[1]+f[3]) < 1e-16


def test_enzyme_jacobian_conservation():
    j = biology.enzyme_jac(np.array([.8, .001, .009, .199]))
    assert np.max(np.abs(j[1]+j[2])) < 1e-16
    assert np.max(np.abs(j[0]+j[1]+j[3])) < 1e-16


def test_lv_equilibrium_and_positive_log_coordinates():
    assert np.array_equal(biology.lv(np.ones(2)), np.zeros(2))
    y = np.array([1.2, .8]); log_rhs = np.array([1-y[1], y[0]-1])
    assert np.allclose(biology.lv(y), y*log_rhs, atol=1e-16)


def test_seir_total_transfer_identity():
    assert abs(np.sum(biology.seir(np.array([.8, .05, .1, .05])))) < 1e-16


def test_rk4_retains_completed_equilibrium(tmp_path):
    t, y = biology.rk4(biology.lv, [1., 1.], .1, 4, Trace(tmp_path, 'lv'), Deadline(1))
    assert len(t) == 5 and np.array_equal(y, np.ones((5, 2)))
    assert (tmp_path/'lv-partial.npz').is_file()


def test_enzyme_output_grid_contains_initial_layer():
    t = biology.enzyme_times(.01)
    assert t[0] == 0 and t[-1] == 50
    assert all(np.min(np.abs(t-v/12)) == 0 for v in [1, 5, 20])


def test_stage_zero_rhs_retains_true_initial(tmp_path):
    y = np.array([0., 0., .01, 0.])
    counts = {key: 0 for key in ['attempted_steps', 'accepted_steps', 'rejected_steps',
        'clipped_output_steps', 'RHS_calls', 'Jacobian_calls', 'factor_builds',
        'linear_solves', 'Newton_updates', 'backtracks']}
    result = biology.stage(y, .01, y, 1e-6, 1e-10, counts, Trace(tmp_path, 'stage'), Deadline(1))
    assert np.array_equal(result, y)


def test_trace_nonfinite_raw_array_is_not_suppressed(tmp_path):
    trace = Trace(tmp_path, 'raw'); trace.observe('candidate', value=np.inf); trace.flush()
    assert np.isinf(np.load(tmp_path/'raw-partial.npz')['candidate__value'])


def test_fresh_directory_rejects_overwrite(tmp_path):
    (tmp_path/'old.txt').write_text('failure evidence')
    with pytest.raises(ValueError, match='fresh'):
        fresh(tmp_path)


def test_lookup_refuses_interpolation():
    with pytest.raises(ValueError, match='qualified'):
        lookup(np.array([.15]), np.array([0., .1, .2]), np.zeros((2, 3)))


def test_original_false_target_is_preserved():
    case = {'checks': {'faithful': True}}
    summarize(case, {'accuracy': outcome(.2, .1)}, 'a'*64)
    assert case['passed'] is True
    assert case['original_target_results']['accuracy'] is False
    assert case['original_target_summary']['all_met'] is False


def test_NA_relative_CSV_is_blank(tmp_path):
    csv_records(tmp_path/'na.csv', [{'absolute_error': .02, 'relative_error': '', 'relative_applicable': 0}])
    with (tmp_path/'na.csv').open() as stream:
        row = next(csv.DictReader(stream))
    assert row['relative_error'] == '' and float(row['absolute_error']) == .02


def test_normal_budget_return_does_not_mask_abnormal_failure():
    assert optimizer_return_allowed('PINN', 0, False, 300, 0, 'cap')
    assert not optimizer_return_allowed('PINN', 0, True, 300, 0, 'cap')
    assert optimizer_return_allowed('FNO', 1, False, 160, 120, 'ITERATIONS REACHED LIMIT')
    assert not optimizer_return_allowed('FNO', 2, False, 160, 120, 'ABNORMAL_TERMINATION_IN_LNSRCH')
    assert not optimizer_return_allowed('FNO', 1, False, 160, 12, 'ITERATIONS REACHED LIMIT')

