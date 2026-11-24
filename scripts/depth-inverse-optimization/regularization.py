"""Finite gamma-list selection and fixed-gamma local-model uncertainty."""
import numpy as np


def select_discrepancy(records, gammas, noise_norm, factor=1.05):
    by_gamma = {float(row['gamma']): row for row in records}
    if (len(by_gamma) != len(gammas) or set(by_gamma) != set(float(g) for g in gammas)
            or any(not bool(by_gamma[float(g)]['qualified']) for g in gammas)):
        return dict(status='INCOMPLETE_GAMMA_PATH', selected_gamma=None)
    admitted = [float(g) for g in gammas
                if float(by_gamma[float(g)]['weighted_residual_norm']) <= factor * noise_norm]
    if not admitted:
        return dict(status='NO_ADMISSIBLE_GAMMA', selected_gamma=None)
    return dict(status='SELECTED', selected_gamma=max(admitted))


def fixed_gamma_covariance(k, weights, sigma, gamma):
    k, weights = np.asarray(k, dtype=float), np.asarray(weights, dtype=float)
    g = np.einsum('mi,m,mj->ij', k, weights, k) + gamma * np.eye(k.shape[1])
    response = np.linalg.solve(g, k.T * weights[None, :])
    covariance = sigma**2 * np.einsum('im,jm->ij', response, response)
    return covariance, g, response


def scalar_2x2_statistics(k, weights, sigma, gamma, truth, prior, delta_data):
    """Independent scalar assembly and determinant inverse for the fixed control."""
    a = gamma + sum(float(w)*float(row[0])**2 for row, w in zip(k, weights))
    b = sum(float(w)*float(row[0])*float(row[1]) for row, w in zip(k, weights))
    c = gamma + sum(float(w)*float(row[1])**2 for row, w in zip(k, weights))
    determinant = a*c - b*b
    if determinant <= 0:
        raise ValueError('Scalar control must be positive definite')
    inverse = [[c/determinant, -b/determinant], [-b/determinant, a/determinant]]
    response = [[sum(inverse[i][j]*float(row[j])*float(w) for j in range(2))
                 for row, w in zip(k, weights)] for i in range(2)]
    covariance = [[sigma**2*sum(response[i][m]*response[j][m] for m in range(len(k)))
                   for j in range(2)] for i in range(2)]
    bias = [-gamma*sum(inverse[i][j]*(float(truth[j])-float(prior[j])) for j in range(2))
            for i in range(2)]
    shift = [sum(response[i][m]*float(delta_data[m]) for m in range(len(k))) for i in range(2)]
    return np.asarray(covariance), np.asarray(bias), np.asarray(shift)


def lcurve_chord_curvature(records):
    valid = [row for row in records if row.get('qualified') and row['gamma'] > 0
             and row['weighted_residual_norm'] > 0 and row['parameter_deviation_norm'] > 0]
    if len(valid) != 4:
        return dict(status='NOT_FOUR_FINITE_POSITIVE_POINTS', values=[], gamma_values=[])
    points = np.array([[np.log(row['weighted_residual_norm']),
                        np.log(row['parameter_deviation_norm'])] for row in valid])
    curvature = []
    for i in (1, 2):
        a, b, c = points[i-1:i+2]
        ab, bc, ac = b-a, c-b, c-a
        denominator = float(np.linalg.norm(ab)*np.linalg.norm(bc)*np.linalg.norm(ac))
        cross = float(ab[0]*ac[1]-ab[1]*ac[0])
        curvature.append(2.*abs(cross)/denominator if denominator > 0 else 0.)
    return dict(status='FOUR_POINT_DIAGNOSTIC_ONLY', values=curvature,
                gamma_values=[valid[1]['gamma'], valid[2]['gamma']])


def fixed_noise(seeds):
    return {int(seed): np.random.Generator(np.random.PCG64(int(seed))).standard_normal(5)
            for seed in seeds}
