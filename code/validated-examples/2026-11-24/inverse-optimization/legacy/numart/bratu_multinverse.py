"""Two-coefficient Bratu fitting, discrete adjoints and data-only diagnostics.

The coefficient is a+b*(2*x-1), a declared extension of the constant-lambda
model. Only the tested positive, smooth smaller-solution branch is considered.
The optimizer uses adjoint gradients and a fixed positive diagonal metric.
"""
import numpy as np
from .autodiff import bratu_matrix
from .bratu_inverse import observation_matrix, POSITIONS, FIXED_NOISE
from .bratu_sensitivity import adjoint_gradient, implicit_sensitivity
from .krylov import newton

TRUTH = np.array([2.2, .35])
LOWER = np.array([1., -.5])
UPPER = np.array([2.8, .5])
METRIC = np.array([1., 100.])


def basis(n):
    bratu_matrix(n)
    x = np.arange(1, n+1)/(n+1)
    return np.column_stack((np.ones(n), 2*x-1))


def _theta(theta):
    theta = np.asarray(theta, dtype=float)
    if (theta.shape != (2,) or not np.all(np.isfinite(theta))
            or theta[0]-abs(theta[1]) <= 0 or theta[0]+abs(theta[1]) > 3.3+1e-14):
        raise ValueError('Two finite coefficients with 0<a-|b| and a+|b|<=3.3 required')
    return theta


def residual(u, theta):
    u = np.asarray(u, dtype=float)
    q = basis(len(u))
    return np.einsum('ij,j->i', bratu_matrix(len(u)), u)-np.einsum('ij,j->i', q, _theta(theta))*np.exp(u)


def derivatives(u, theta):
    u = np.asarray(u, dtype=float)
    q = basis(len(u))
    coefficient = np.einsum('ij,j->i', q, _theta(theta))
    return bratu_matrix(len(u))-np.diag(coefficient*np.exp(u)), -np.exp(u)[:, None]*q


def solve_state(n, theta, tolerance=1e-10):
    theta = _theta(theta)
    if not np.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Positive finite nonlinear tolerance required')
    return newton(lambda u:residual(u, theta), lambda u:derivatives(u, theta)[0],
                  np.zeros(n), tolerance=tolerance, maxiter=40, linear_solver='dense')


def _specification(n, data, positions, weights, gamma, prior):
    h = observation_matrix(n, positions)
    data = np.asarray(data, dtype=float)
    prior = np.asarray(prior, dtype=float)
    weights = np.ones(len(h))/len(h) if weights is None else np.asarray(weights, dtype=float)
    if data.shape != (len(h),) or not np.all(np.isfinite(data)):
        raise ValueError('One finite datum per observation required')
    if weights.shape != data.shape or np.any(weights <= 0) or not np.all(np.isfinite(weights)):
        raise ValueError('Finite strictly positive observation weights required')
    if prior.shape != (2,) or not np.all(np.isfinite(prior)) or not np.isfinite(gamma) or gamma < 0:
        raise ValueError('Finite two-component prior and nonnegative regularization required')
    return h, data, weights, prior


def evaluate(n, theta, data, positions=POSITIONS, weights=None, gamma=0.,
             prior=(2., 0.), primal_tolerance=1e-10, gradient=True):
    """Fresh zero-start state solve, weighted least squares and one adjoint solve.

    L=.5*r.T*W*r+.5*gamma*||theta-prior||^2. Parameter scales are both one.
    J.T*p=H.T*W*r; g=gamma*(theta-prior)-F_theta.T*p.
    """
    theta = _theta(theta)
    h, data, weights, prior = _specification(n, data, positions, weights, gamma, prior)
    root = solve_state(n, theta, primal_tolerance)
    norm = float(np.linalg.norm(residual(root.x, theta)))
    if not root.converged or norm > primal_tolerance:
        raise RuntimeError('Primal solve failed: '+root.reason)
    predicted = np.einsum('ij,j->i', h, root.x)
    misfit = predicted-data
    data_objective = float(.5*np.sum(weights*misfit**2))
    penalty = float(.5*gamma*np.sum((theta-prior)**2))
    out = dict(parameters=theta.copy(), state=root.x, predicted=predicted,
        misfit=misfit, objective=data_objective+penalty, data_objective=data_objective,
        penalty=penalty, data_rms=float(np.sqrt(np.mean(misfit**2))),
        primal_residual_l2=norm, primal_updates=len(root.step_lengths),
        primal_residual_history=root.residuals)
    if gradient:
        j, ft = derivatives(root.x, theta)
        q = np.einsum('ij,i->j', h, weights*misfit)
        explicit = gamma*(theta-prior)
        g, p = adjoint_gradient(j, ft, q, explicit)
        ar = np.einsum('ji,j->i', j, p)-q
        out.update(gradient=g, adjoint=p, objective_state=q,
            explicit_gradient=explicit, adjoint_residual_l2=float(np.linalg.norm(ar)),
            adjoint_residual_relative_l2=float(np.linalg.norm(ar)/max(np.linalg.norm(q),1e-300)))
    return out


def sensitivity_diagnostic(n, theta, positions=POSITIONS, weights=None,
                           gamma=0., primal_tolerance=1e-10, relative_rank_tolerance=1e-10):
    """Raw dimensionless data Jacobian and SVD; penalties never add data rank.

    The two parameter scales are explicitly 1. Singular values are padded to
    length two, including a true parameter nullspace for a one-row operator.
    Augmented singular values describe the penalized Gauss-Newton curvature,
    not statistical information or the exact nonlinear objective Hessian.
    """
    h = observation_matrix(n, positions)
    weights = np.ones(len(h))/len(h) if weights is None else np.asarray(weights, dtype=float)
    _specification(n, np.zeros(len(h)), positions, weights, gamma, (0.,0.))
    if not np.isfinite(relative_rank_tolerance) or relative_rank_tolerance <= 0:
        raise ValueError('Positive finite relative rank tolerance required')
    state = solve_state(n, theta, primal_tolerance)
    if not state.converged:
        raise RuntimeError('Sensitivity state failed')
    j, ft = derivatives(state.x, theta)
    s = implicit_sensitivity(j, ft)
    a = np.sqrt(weights)[:,None]*np.einsum('ij,jk->ik', h, s)
    _, values, vt = np.linalg.svd(a, full_matrices=True)
    values = np.pad(values, (0, 2-len(values)))
    tolerance = relative_rank_tolerance*values[0]
    rank = int(np.sum(values > tolerance)) if values[0] > 0 else 0
    augmented = np.linalg.svd(np.vstack((a,np.sqrt(gamma)*np.eye(2))),compute_uv=False)
    return dict(parameters=np.asarray(theta,dtype=float), positions=np.asarray(positions,dtype=float),
        weights=weights, weighted_data_jacobian=a, state_sensitivity=s,
        parameter_scales=np.ones(2), data_singular_values=values,
        right_singular_vectors=vt, data_rank=rank,
        rank_relative_tolerance=relative_rank_tolerance, rank_absolute_tolerance=tolerance,
        data_condition_number=float(values[0]/values[-1]) if rank==2 else None,
        weakest_parameter_direction=vt[-1], gamma=float(gamma),
        augmented_singular_values=augmented,
        sensitivity_residual_l2=float(np.linalg.norm(np.einsum('ij,jk->ik',j,s)+ft)))


def _bounds(bounds):
    bounds = np.asarray(bounds, dtype=float)
    if (bounds.shape!=(2,2) or not np.all(np.isfinite(bounds))
            or np.any(bounds[:,0]>=bounds[:,1])
            or bounds[0,0]-np.max(abs(bounds[1])) <= 0
            or bounds[0,1]+np.max(abs(bounds[1])) > 3.3+1e-14):
        raise ValueError('Box must stay within the tested positive coefficient range')
    return bounds[:,0],bounds[:,1]


def fit_parameters(n, data, initial, positions=POSITIONS, weights=None, gamma=0.,
                   prior=(2.,0.), bounds=((1.,2.8),(-.5,.5)), metric=METRIC,
                   primal_tolerance=1e-10, gradient_tolerance=1e-9,
                   maxiter=1000, initial_step=10.):
    """Fixed diagonal-metric projected adjoint gradients with Armijo search.

    Direction is -diag(metric)*g before box projection. The sufficient-decrease
    test uses g.dot(actual displacement). Stopping uses the UNscaled unit-step
    projected gradient, so metric changes cannot fake stationarity.
    """
    lo,hi = _bounds(bounds)
    theta = _theta(initial).copy()
    h,_,_,_ = _specification(n,data,positions,weights,gamma,prior)
    metric = np.asarray(metric,dtype=float)
    if np.any(theta<lo) or np.any(theta>hi):
        raise ValueError('Initial parameters must lie in the box')
    if metric.shape!=(2,) or not np.all(np.isfinite(metric)) or np.any(metric<=0):
        raise ValueError('Two finite positive metric entries required')
    if (not np.isfinite(gradient_tolerance) or gradient_tolerance<=0
            or not isinstance(maxiter,(int,np.integer)) or maxiter<1
            or not np.isfinite(initial_step) or initial_step<=0):
        raise ValueError('Positive optimization controls required')
    if not np.any(h) and gamma==0:
        raise ValueError('Boundary-only data contain no parameter information')
    history=[]; evaluations=1
    current=evaluate(n,theta,data,positions,weights,gamma,prior,primal_tolerance)
    for iteration in range(maxiter+1):
        g=current['gradient']
        pg=float(np.linalg.norm(theta-np.clip(theta-g,lo,hi),ord=np.inf))
        history.append(dict(iteration=iteration, parameters=theta.copy(),
            objective=current['objective'],data_objective=current['data_objective'],
            penalty=current['penalty'],gradient=g.copy(),projected_gradient_inf=pg,
            primal_residual_l2=current['primal_residual_l2'],
            adjoint_residual_l2=current['adjoint_residual_l2']))
        if pg<=gradient_tolerance:
            return dict(converged=True,reason='unscaled projected adjoint-gradient tolerance',
                parameters=theta,history=history,evaluations=evaluations,result=current)
        if iteration==maxiter:break
        step=float(initial_step)
        for backtrack in range(50):
            candidate=np.clip(theta-step*metric*g,lo,hi)
            displacement=candidate-theta
            trial=evaluate(n,candidate,data,positions,weights,gamma,prior,primal_tolerance)
            evaluations+=1
            rhs=current['objective']+1e-4*float(np.sum(g*displacement))
            if trial['objective']<=rhs:
                history[-1].update(accepted_step=step,backtracks=backtrack,
                    parameter_step=displacement,armijo_rhs=rhs)
                theta,current=candidate,trial
                break
            step*=.5
        else:
            return dict(converged=False,reason='Armijo line search failed',
                parameters=theta,history=history,evaluations=evaluations,result=current)
    return dict(converged=False,reason='optimization iteration limit',
        parameters=theta,history=history,evaluations=evaluations,result=current)


def objective_reference(n,data,initial=(2.,0.),positions=POSITIONS,weights=None,
                        gamma=0.,prior=(2.,0.),bounds=((1.,2.8),(-.5,.5)),
                        diameter_tolerance=1e-8):
    """Independent bounded Nelder-Mead reference using objective values only.

    This small reference assumes no derivatives and provides no global-optimum
    theorem. All published comparisons have interior minima; box clipping is
    explicitly part of this local reference algorithm.
    """
    lo,hi=_bounds(bounds)
    initial=np.asarray(initial,dtype=float)
    if (initial.shape!=(2,) or not np.all(np.isfinite(initial))
            or np.any(initial<lo) or np.any(initial>hi)
            or not np.isfinite(diameter_tolerance) or diameter_tolerance<=0):
        raise ValueError('Finite initial point inside the box and positive reference tolerance required')
    simplex=np.tile(initial,(3,1))
    for axis in range(2):
        step=min(.05,.1*(hi[axis]-lo[axis]))
        simplex[axis+1,axis]+=step if initial[axis]+step<=hi[axis] else -step
    evaluations=0
    def value(theta):
        nonlocal evaluations
        evaluations+=1
        return evaluate(n,theta,data,positions,weights,gamma,prior,gradient=False)['objective']
    values=np.array([value(x) for x in simplex])
    for iteration in range(1000):
        order=np.argsort(values);simplex,values=simplex[order],values[order]
        diameter=float(np.max(np.linalg.norm(simplex-simplex[0],axis=1)))
        if diameter<=diameter_tolerance:
            return dict(parameters=simplex[0],objective=float(values[0]),
                simplex_diameter=diameter,evaluations=evaluations,iterations=iteration)
        center=np.mean(simplex[:2],axis=0)
        reflected=np.clip(center+(center-simplex[2]),lo,hi);fr=value(reflected)
        if fr<values[0]:
            expanded=np.clip(center+2*(reflected-center),lo,hi);fe=value(expanded)
            simplex[2],values[2]=(expanded,fe) if fe<fr else (reflected,fr)
        elif fr<values[1]:simplex[2],values[2]=reflected,fr
        else:
            outside=fr<values[2]
            contracted=np.clip(center+.5*((reflected if outside else simplex[2])-center),lo,hi)
            fc=value(contracted)
            if fc<(fr if outside else values[2]):simplex[2],values[2]=contracted,fc
            else:
                simplex[1:]=simplex[0]+.5*(simplex[1:]-simplex[0])
                values[1:]=[value(x) for x in simplex[1:]]
    raise RuntimeError('Objective-only simplex reference iteration limit')


def fine_reference(n,theta,positions=POSITIONS):
    """Independent tridiagonal-Newton data generator on a finer FD grid.

    This implementation solves the scaled tridiagonal residual directly, with
    a Thomas elimination instead of the dense Newton/adjoint code. It is a
    numerical reference, not an analytic solution or an independent PDE model.
    """
    theta=_theta(theta);h=1/(n+1);x=np.arange(1,n+1)*h
    coefficient=theta[0]+theta[1]*(2*x-1);u=np.zeros(n)
    def scaled(v):
        return 2*v-np.r_[0.,v[:-1]]-np.r_[v[1:],0.]-h*h*coefficient*np.exp(v)
    for updates in range(40):
        f=scaled(u);diagonal=2-h*h*coefficient*np.exp(u)
        upper=-np.ones(n-1);rhs=-f.copy();diag=diagonal.copy()
        for i in range(1,n):
            multiplier=-1/diag[i-1];diag[i]-=multiplier*upper[i-1];rhs[i]-=multiplier*rhs[i-1]
        delta=np.empty(n);delta[-1]=rhs[-1]/diag[-1]
        for i in range(n-2,-1,-1):delta[i]=(rhs[i]-upper[i]*delta[i+1])/diag[i]
        u+=delta
        if np.max(abs(delta))<2e-13 and np.max(abs(scaled(u)))<2e-14:
            predicted=np.einsum('ij,j->i',observation_matrix(n,positions),u)
            return dict(n=n,parameters=theta,predicted=predicted,updates=updates+1,
                scaled_residual_inf=float(np.max(abs(scaled(u)))),
                unscaled_residual_l2=float(np.linalg.norm(scaled(u))/(h*h)),
                final_correction_inf=float(np.max(abs(delta))))
    raise RuntimeError('Independent fine-grid Newton failed')
