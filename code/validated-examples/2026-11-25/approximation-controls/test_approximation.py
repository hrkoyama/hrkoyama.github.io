"""Small algebraic goldens, boundary branches and ownership regressions."""
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
import pytest
import interpolation as I
import splines as S
import haar as H
from references import polynomials as P
from references import spline_rational as R
from references import haar_matrix as M
from io_contract import portable, write_csv


def node_table():
    return json.loads((Path(__file__).parent/'inputs.json').read_text())['cases']['runge-barycentric-clenshaw']['positive_cosine32_decimal']


@pytest.mark.parametrize('degree,family', [(8, 'equispaced'), (16, 'equispaced'), (32, 'equispaced'), (8, 'lobatto'), (16, 'lobatto'), (32, 'lobatto')])
def test_node_symmetry_and_distinctness(degree, family):
    x, w = I.nodes_weights(degree, family, node_table())
    assert len(set(x)) == degree+1
    assert np.array_equal(x, -x[::-1])
    assert np.all(w != 0) and np.all(np.sign(w[1:]) != np.sign(w[:-1]))


def test_barycentric_exact_node_and_weight_scale():
    x, y, w = [-1., 0., 1.], [1., 0., 1.], [.5, -1., .5]
    assert I.barycentric(x, y, w, 0.)[0] == 0.
    assert I.barycentric(x, y, w, .25)[0] == I.barycentric(x, y, np.array(w)*8, .25)[0]
    assert P.direct_lagrange(x, y, .25) == F(1, 16)


def test_roundoff_certificate_rejects_bad_result():
    x, y, w = [-1., 0., 1.], [1., 0., 1.], [.5, -1., .5]
    value, _, trace = I.barycentric(x, y, w, .25)
    assert P.barycentric_certificate(x, y, w, .25, value, trace)['passed']
    assert not P.barycentric_certificate(x, y, w, .25, value+1e-4, trace)['passed']


@pytest.mark.parametrize('coefficients', [[2.], [1., 2.], [1., 2., 3.]])
def test_full_coefficient_clenshaw(coefficients):
    value, trace, final = I.clenshaw(coefficients, .25)
    assert abs(value-float(P.direct_chebyshev(coefficients, .25))) < 1e-14
    assert P.clenshaw_certificate(coefficients, .25, value, trace.reshape((-1, 6)), final)['passed']


@pytest.mark.parametrize('order,expected', [(0, 1.), (1, 0.), (2, 0.)])
def test_bspline_partition_derivatives(order, expected):
    knots = [0., 0., 0., 0., .5, 1., 1., 1., 1.]
    assert abs(np.sum(S.basis_vector(knots, 3, .25, order))-expected) < 1e-13


@pytest.mark.parametrize('point', [0., 1.])
def test_deboor_closed_endpoint(point):
    assert S.deboor([0.]*4+[1.]*4, [0., 1/3, 2/3, 1.], point) == point


@pytest.mark.parametrize('kind', ['natural', 'clamped'])
def test_c2_linear_reproduction(kind):
    model = S.fit([-1., 0., 1.], [.5, 1., 1.5], kind, [.5, .5])
    assert np.max(np.abs(S.evaluate(model, [-1., -.25, .5, 1.])-(1+np.array([-1., -.25, .5, 1.])/2))) < 1e-12


@pytest.mark.parametrize('values,expected', [([0, 1, 2], 1), ([0, 1, 5], 0), ([0, 1, -3], 3), ([0, 1, 0], 2), ([0, -1, 3], -3), ([0, 0, 1], 0), ([2, 2, 2], 0)])
def test_pchip_endpoint_branches(values, expected):
    assert S.pchip_slopes([0, 1, 2], values)[0] == expected
    assert S.pchip_slopes([0, 1, 2], values[::-1])[-1] == -expected


def test_pchip_two_point_and_invalid_knots():
    assert np.array_equal(S.pchip_slopes([0, 2], [1, 5]), [2, 2])
    with pytest.raises(ValueError):
        S.pchip_slopes([0, 0], [1, 2])


def test_fraction_plateau_is_actual_binary_input():
    a, b = F.from_float(.01), F.from_float(1.01)
    assert a != F(1, 100) and b != F(101, 100)
    cert = R.plateau_certificates(.01, 1.01)
    x = [0., 1., 2., 3., 4., 5.];y = [.01]*3+[1.01]*3
    for kind in ('natural', 'clamped'):
        xr, c, _ = R.c2_coefficients(x, y, kind, [0., 0.])
        assert R.evaluate(xr, c, 1.5) == cert[kind] < 0


@pytest.mark.parametrize('mode', ['periodic', 'symmetric'])
def test_odd_haar_has_independent_left_inverse(mode):
    signal = np.array([1., 2., -1., 0., 3.])
    model = H.analyze(signal, 2, mode)
    a, s = M.matrices(5, 2, mode)
    assert a.shape == (7, 5) and s.shape == (5, 7)
    assert np.max(np.abs(np.einsum('ij,jk->ik', s, a)-np.eye(5))) < 1e-14
    assert np.max(np.abs(H.synthesize(model)-signal)) < 1e-14


def test_haar_sign_golden():
    assert np.max(np.abs(H.flatten(H.analyze([1., 1., 0., 0.], 2, 'periodic'))-[1., 1., 0., 0.])) < 1e-14


def test_threshold_tie_and_ownership():
    model = H.analyze([1., 0., 0., 1.], 2, 'periodic')
    before = H.flatten(model).copy()
    tau = float(abs(model['details'][0][0]))
    hard = H.threshold(model, 'hard', tau)
    assert hard['details'][0][0] == 0
    hard['coarse'][0] += 1
    assert np.array_equal(H.flatten(model), before)


def test_scalar_json_and_csv_policy(tmp_path):
    assert portable({'flag': np.bool_(True), 'count': np.int64(2)}) == {'flag': True, 'count': 2}
    with pytest.raises(ValueError):portable(np.float64('nan'))
    with pytest.raises(ValueError):write_csv(tmp_path/'bad.csv', [{'x': float('inf')}])
    write_csv(tmp_path/'good.csv', [{'x': 0., 'label': 'zero'}, {'x': 1., 'label': 'one'}])
    assert len((tmp_path/'good.csv').read_text().splitlines()) == 3
