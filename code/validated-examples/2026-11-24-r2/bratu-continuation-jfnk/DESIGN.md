# Private fixed Bratu proposal: scientific execution has not started

Dimensionless steady problem on 0<x<1:

    F_h(u,lambda) = A_h u - lambda exp(u) = 0,
    (A_h u)_i = (2u_i-u_(i-1)-u_(i+1))/h^2, h=1/(n+1), u_0=u_(n+1)=0.

The independently derived continuous family is

    u_theta(x)=2 log[cosh(theta/2)/cosh(theta(x-1/2))],
    lambda(theta)=2 theta^2/cosh(theta/2)^2.

Here theta is half the parameter in the cited author teaching exercise. The
continuous fold satisfies theta*tanh(theta/2)=2. Decimal80 bisection and field
evaluation in references/analytic_family.py use no numerical-solver imports.
The continuous ODE substitution, endpoints, fixed-lambda roots and published
rounded critical value are separate qualifications. They are not an exact
finite-difference solution or proof of numerical continuation success.

## Case56: actual pseudo-arclength continuation

Fix n31/63/127, ds.1, 80 predictor/corrector steps from (u,lambda)=0. The
weighted norm is h*sum(du^2)+dlambda^2. Tangents satisfy J*tu+F_lambda*tlambda=0,
have unit weighted norm and retain positive weighted orientation with the
previous tangent. A Newton corrector solves F=0 and the previous-tangent
hyperplane through the predictor. There is no adaptive ds, parameter sweep,
analytic-profile reset, endpoint extension or physical-time interpretation.

An augmented solve initialized from the actual continued maximum-lambda state
solves F=0, Jv=0, h*sum(v^2)=1. Its sparse derivative blocks are

    [ J                    -exp(u)          0 ],
    [ diag(-lambda exp(u)v) -exp(u)v         J ],
    [ 0                     0               2h v^T ].

The smallest singular value of symmetric J is min(abs(eigenvalues)); use the
actual tridiagonal spectrum. Nonzero null-vector projections on F_lambda and
F_uu[v,v] distinguish the simple fold. This case explicitly assembles sparse
Jacobians. It is not the Jacobian-free case.

At lambda2, correct lower and upper states from the corresponding continued
branches and compare with independent fixed-lambda analytic solutions. For
the entire curve, declare midpoint value as the analytic family coordinate;
compare all other field points AND lambda. The coordinate fit is disclosed,
and does not replace the independent fixed-lambda tests.

Lambda4 is deliberately outside the discrete existence range. A_h inverse is
positive, so any solution at lambda>0 has u>0. With positive first eigenvector
phi and e^u>=e*u, mu1*phi.u=lambda*phi.exp(u)>=lambda*e*phi.u, hence
lambda<=mu1/e<pi^2/e<4. The saved Newton failure is a no-solution control,
not a general statement about Newton at arbitrary lambda or initial states.

## Case57: true nonlinear-Jacobian-free products

Fix lambda3, n63/127, starts 0 and 4sin(pi*x), analytic/central-FD/forward-AD Jv:
12 solves. Add exactly one n63/lower/analytic companion with constant eta1e-8.
The primary inexact rule is first eta.3, then
clamp(.9*(||F_k||/||F_(k-1)||)^1.5,.001,.5). It is a stated simple residual-ratio
rule, not an uninspected exact Eisenstat-Walker/PETSc default.

JFNK receives only callable products. Two-pass modified Gram-Schmidt and
Givens rotations implement restarted GMRES; restart24/max96, outer max24,
Armijo1e-4 with at most14 trial lengths, nonlinear L2 tolerance1e-9. The
constant-coefficient Poisson right preconditioner uses O(n) Thomas arrays.
Neither the nonlinear Jacobian nor coordinate-seeded AD is constructed by
this solver. A separate regression forbids both assembly entry points.

Central FD is [F(u+delta*v)-F(u-delta*v)]/(2delta), with
delta=eps^(1/3)*(1+||u||_2)/||v||_2; zero directions return zero explicitly.
Forward AD carries ONE tangent through elementary arithmetic, exp and the
linear zero-padding primitive. Analytic Jv is the stencil applied to v minus
lambda*exp(u)*v. For FD/AD solves the analytic forcing check is validation
only, separately counted, and never chooses a correction or stopping step.
The guarded exponential trial range u<=700 rejects unsafe trials without
clipping a state; it is not a general global-convergence guarantee.

Record primal residual evaluations, dual traversals, Jv calls/zero calls,
Poisson applications and validation-only analytic products separately.
Compare solutions and work counts, without requiring a timing speedup or
assuming a dual traversal has the cost of one primal evaluation.

## Frozen validation and retention

The source proposes27 meaningful pytest checks and196 case gates:67 for the
continuation case,129 for JFNK. These numbers and all input/acceptance/source
bytes must be frozen and independently reviewed before pytest or main.
Scientific execution is still zero; runtime is UNMEASURED. One external120s
budget covers pytest and every main calculation; local goal20s is unmeasured.

Save complete branch states/tangents, every Newton/corrector iterate and
residual trace, fold vectors, fixed-lambda candidates, every JFNK line trial,
inner residual histories, full reference fields and finite numeric CSVs.
Partial NPZ/stage JSON exists before or during a solve. Exceptions preserve
available candidates and traceback; no retry or criterion relaxation follows
an observed result without a separately frozen revision.

References were actually read only to the depths in source-review.json.
PETSc is context, not executed reference software. Original Bratu1914 and the
standalone Eisenstat-Walker1996 full text remain unread. Existing published
Bratu sensitivity code uses assembled matrices and only the lower regular
branch; none of its numerical success is borrowed by these new cases.
