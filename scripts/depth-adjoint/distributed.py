"""Local B/B^T actions and callable-only implicit VJP. No n-by-m primary."""
from pathlib import Path
import numpy as np
from operators import LocalHats, dot, norm, jac_action, tridiagonal_action, poisson_factor
from newton import state, derivative
from io_contract import save_npz


def objectives(u):
    h = 1/(len(u)+1)
    return np.array([h*float(np.sum(u)), u[len(u)//2], .5*h*dot(u, u)])


def objective_q(u):
    h = 1/(len(u)+1)
    middle = np.zeros(len(u)); middle[len(u)//2] = 1
    return [np.full(len(u), h), middle, h*u]


def allocation_check(arrays, n, m):
    """Named semantic inventory; rejects a parameter Jacobian/sensitivity."""
    inventory = []
    for name, array in arrays.items():
        shape = tuple(array.shape)
        if shape in [(n, m), (m, n)] or name in ['parameter_Jacobian', 'sensitivity_matrix', 'dense_B']:
            raise ValueError('Forbidden primary parameter matrix: '+name)
        inventory.append({'name': name, 'shape': list(shape), 'bytes': int(array.nbytes)})
    return inventory


def adjoint_objectives(u, coefficient, hats, qs, settings, partial, factor=None):
    gradients, candidates = [], []
    completed = {}
    for q in qs:
        candidate = derivative(u, coefficient, q, settings['gmres']['strict_tangent_adjoint_rtol'], settings, partial, factor)
        # Required VJP accuracy is independently checked; no unmet target relabeling.
        gradients.append(hats.transpose(np.exp(u)*candidate['x']))
        candidates.append(candidate)
        if partial is not None:
            completed[f'gradient_{len(candidates)-1}'] = gradients[-1]
            completed[f'adjoint_{len(candidates)-1}'] = candidate['x']
            completed[f'history_{len(candidates)-1}'] = candidate['residuals']
            path = Path(partial)
            save_npz(path.with_name(path.stem+'-completed-RHS.npz'), completed)
    return np.stack(gradients), candidates, len(qs)


def run(n, m, settings, cfg, partial, raw_path):
    xi = np.arange(m, dtype=float)/(m-1)
    theta = .2*np.sin(2*np.pi*xi)+.1*np.cos(np.pi*xi)
    hats = LocalHats(n, m)
    coefficient = 2+hats.forward(theta)
    solved = state(n, coefficient, cfg['state_tolerance'], settings, partial)
    u = solved['u']; qs = objective_q(u)
    arrays = {'u': u, 'theta': theta, 'coefficient': coefficient,
              'hat_index': hats.index, 'hat_weight': hats.weight}
    save_npz(raw_path, arrays)
    shared_factor = poisson_factor(n)
    one, one_candidates, one_count = adjoint_objectives(u, coefficient, hats, qs[:1], settings, partial, shared_factor)
    arrays['one_gradient'] = one; save_npz(raw_path, arrays)
    three, candidates, three_count = adjoint_objectives(u, coefficient, hats, qs, settings, partial, shared_factor)
    arrays['gradients'] = three
    for j, candidate in enumerate(candidates):
        arrays[f'adjoint_{j}'] = candidate['x']; arrays[f'history_{j}'] = candidate['residuals']
    save_npz(raw_path, arrays)
    direction = np.arange(1, m+1, dtype=float)/(m+1)
    v = np.arange(1, n+1, dtype=float)/(n+1)
    w = (-1.)**np.arange(n)*(2*np.arange(n)+1)/(2*n+2)
    Jv, JTw = jac_action(u, coefficient, v), jac_action(u, coefficient, w)
    Bv, BTw = hats.forward(direction), hats.transpose(w)
    duality = {'J_error': abs(dot(w, Jv)-dot(v, JTw)),
               'J_scale': max(1., norm(w)*norm(Jv), norm(v)*norm(JTw)),
               'B_error': abs(dot(w, Bv)-dot(direction, BTw)),
               'B_scale': max(1., norm(w)*norm(Bv), norm(direction)*norm(BTw))}
    fd, all_states = [], []
    for exponent in [8, 12, 16]:
        increment = 2.**-exponent; pair = []
        for sign in [-1, 1]:
            a = 2+hats.forward(theta+sign*increment*direction)
            out = state(n, a, cfg['state_tolerance'], settings, partial)
            pair.append(out); all_states.append(out)
            arrays[f'FD_{exponent}_{"minus" if sign < 0 else "plus"}'] = out['u']
            save_npz(raw_path, arrays)
        fd.append({'step': increment,
                   'derivative': (objectives(pair[1]['u'])-objectives(pair[0]['u']))/(2*increment)})
    arrays.update(direction=direction, Jv=Jv, JTw=JTw, Bv=Bv, BTw=BTw)
    visible = {**arrays, 'xi': xi, 'direction': direction, 'duality_v': v, 'duality_w': w,
               **shared_factor.arrays('shared_Poisson')}
    for j, q in enumerate(qs): visible[f'q_{j}'] = q
    for j, candidate in enumerate(one_candidates+candidates):
        visible[f'candidate_{j}'] = candidate['x']
        visible[f'residuals_{j}'] = np.asarray(candidate['residuals'])
    inventory = allocation_check(visible, n, m)
    # Krylov workspace dimensions are fixed n*25/n*24, not parameter dimensions.
    workspace = {'V_shape': [n, min(24, n)+1], 'Z_shape': [n, min(24, n)],
                 'H_shape': [min(24, n)+1, min(24, n)],
                 'scope': 'Reviewed GMRES workspace; no n-by-m parameter Jacobian.'}
    save_npz(raw_path, arrays)
    return {'arrays': arrays, 'state': solved, 'gradients': three,
            'one_candidates': one_candidates, 'candidates': candidates,
            'one_RHS': one_count, 'three_RHS': three_count, 'FD': fd, 'FD_states': all_states,
            'duality': duality, 'inventory': inventory, 'workspace': workspace,
            'B_calls': hats.calls, 'derivative_factor_builds': 1,
            'derivative_factor_solves': sum(c['counts']['preconditioner'] for c in one_candidates+candidates)}


def nonsymmetric_control():
    n = 7
    d, l, r = np.full(n, 4.), np.full(n-1, -1.), np.full(n-1, -2.)
    v, w = np.arange(1., n+1), (-1.)**np.arange(n)
    actual = tridiagonal_action(d, l, r, w, True)
    golden = np.array([4*w[i]-(w[i-1]*2 if i else 0)-(w[i+1] if i+1 < n else 0) for i in range(n)])
    wrong = tridiagonal_action(d, l, r, w, False)
    return bool(np.array_equal(actual, golden) and
                dot(w, tridiagonal_action(d, l, r, v)) == dot(v, actual) and
                not np.array_equal(actual, wrong))


def affine_control(n=63):
    x = np.arange(1., n+1)/(n+1)
    a, b = 2.2, .35
    theta = np.array([a-b-2, a+b-2])
    hats = LocalHats(n, 2)
    correct = 2+hats.forward(theta)
    reference = a+b*(2*x-1)
    wrong = 2+hats.forward(np.array([a-b, a+b]))
    return float(np.max(np.abs(correct-reference))), float(np.max(np.abs(wrong-reference)))
