# Bratu inverse problem: two coefficient parameters

Edition: **2026-11-22**. Public release:
<https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/>.

This self-contained NumPy example extends the constant-lambda Bratu model to
`lambda(x)=a+b*(2*x-1)` and estimates the two dimensionless coefficients. It
solves `-u_xx-lambda(x)*exp(u)=0`, with fixed `u(0)=u(1)=0`. The parameter box is
`a in [1,2.8]`, `b in [-0.5,0.5]`, keeping the coefficient between 0.5 and 3.3.
Every state solve starts at zero on the tested smooth smaller-solution branch.
It does not perform continuation, branch identification or fold crossing.

From the extracted directory:

```sh
python -m pip install -r requirements.txt
export OPENBLAS_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```

The fixed thread controls avoid small-matrix BLAS thread overhead and are used
for the saved receipt and identical local rebuild. Numerical tests use explicit
tolerances; cross-platform bitwise identity is not promised. No network is
needed after dependencies are installed. The builder writes
`docs/figures/bratu-multinverse.json` and `bratu-multinverse.png`.

For fixed observation matrix H, positive diagonal weights W and prior theta0,
the objective is `L=.5*r.T*W*r+.5*gamma*||theta-theta0||^2`, `r=H*u-d`. The
regularization matrix is the identity and both declared parameter scales are
one. With `Q_i=(1,2*x_i-1)`, `F_theta=-diag(exp(u))*Q`, the adjoint solves
`J.T*p=H.T*W*r` and returns `g=gamma*(theta-theta0)-F_theta.T*p`. The implemented
model derivatives are analytic. Direct tangent solves and re-solved central
differences independently check both adjoint components away from optima.

The optimizer actually updates with this adjoint gradient. It uses the fixed
positive diagonal metric `P=diag(1,100)` to balance the more weakly observed b
component: `theta_trial=clip(theta-step*P*g,lower,upper)`. Armijo tests the dot
product of the unscaled g with the actual projected displacement, starting at
step 10 and halving it. Stopping instead uses the **unscaled** infinity norm
`||theta-clip(theta-g,lower,upper)||_inf <= 1e-9`. The inner unscaled Euclidean
Bratu residual tolerance is 1e-10, at most 40 Newton updates; optimization allows
1000 updates and 50 backtracks. The stopping tolerance avoids chasing objective
roundoff at nonzero residuals. Actual gradients, projected gradients, objective
terms, residuals, updates and termination reasons are saved. A constrained
stationary point is not a global-optimality or generating-parameter guarantee.

The immutable `inputs/synthetic-observations.json` fixes all observations,
positions, weights, generating parameters `(2.2,0.35)`, noise, priors and starts.
The published experiments distinguish these questions:

1. The same 31-node discrete model generates noiseless observations and fits
   them from three starts. This inverse-crime control checks code consistency.
2. Fixed 1023-node observations come from a separate Thomas-elimination Newton
   implementation of the **same second-order FD approximation**. Its 255/511/
   1023-node self-refinement is recorded. This is a numerical reference, not
   an analytic continuum solution or independent physical model. Inverse grids
   of 15/31/63/127 nodes approach the generating coefficients approximately at
   second order before the finite reference-grid floor becomes important.
   The generator solves a scaled tridiagonal residual to infinity norm 2e-14
   with final correction below 2e-13. Its unscaled L2 residual is reported
   separately (about 1.1e-9 on 1023 nodes); the inverse solver controls are not
   silently changed for the reference.
3. One deterministic sensor perturbation vector is added once, not resampled.
   Gamma values 0, 1e-5, 1e-4 and 1e-3 with prior `(2,0)` compare fits to clean
   and perturbed observations. This perturbation response decreases as gamma
   increases, while parameter error and data misfit increase in this example.
   Regularization stabilizes a chosen criterion but can bias it toward the
   prior. This sweep is not an automatic regularization-selection method.
4. The weighted **data-only** sensitivity `A=sqrt(W)*H*U_theta` has rank two
   for the five separate sensors and at most rank one for one center sensor.
   Full SVD retains the parameter nullspace; singular values are padded to two.
   At b=0, symmetry makes the b sensitivity at the center vanish. Reflection
   b to -b preserves the center measurement even away from b=0. Mirror priors
   select mirror regularized fits with identical center predictions, starting
   from the same `(2,0)` initial parameters in both runs. Stacking
   `sqrt(gamma)*I` can make the penalized Gauss-Newton curvature nonsingular;
   it does not create missing observation information or prove nonlinear
   global uniqueness. Boundary-only observations have data rank zero.

An independent objective-only local Nelder-Mead search checks the four noisy
regularized fits. It uses no adjoint or tangent derivatives and provides no
global convergence proof. Fixed perturbations are not a probability model;
the experiment supplies no confidence intervals, posterior inference, real-data
validation or guarantee about other sensor arrangements and parameter scales.

`numart/autodiff.py`, `krylov.py`, `bratu_sensitivity.py` and `bratu_inverse.py`
are retained byte for byte from the preceding scalar-inverse edition. Their
hashes are in `provenance.json`; old releases are not modified. New files are the
two-parameter helper, evidence builder, tests and fixed inputs.
`source-manifest.json` lists payload hashes. `verification.json` records actual
tests after independent ZIP extraction, archive hash and identical JSON/PNG
rebuild. The receipt stays outside the archive to avoid a circular archive hash.
`LICENSE` and `LICENSING.md` distinguish code from text, plots and saved data.
