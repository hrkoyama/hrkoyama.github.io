# Bratu implicit differentiation and discrete adjoints

Supplemental source edition: 2026-11-22.

- Japanese chapter: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/
- English chapter: https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/

The dimensionless Bratu residual is F(u,lambda)=D*u-lambda*exp(u), with the
centered negative second derivative D on [0,1] and fixed zero boundary data.
Here n counts interior nodes and h=1/(n+1). Every nonlinear solve starts from
zero and uses the existing dense Armijo-Newton solver. The selected alpha=1
and alpha=2 exact-family settings are on the smooth lower branch.

Differentiate the residual after convergence in augmented (u,lambda)
coordinates using the included forward AD engine. Solve J*s=-F_lambda for
the implicit state sensitivity. For the discrete scalar objective

    L_h(u,lambda) = .5*h*sum(u_i**2) + .5*beta*lambda**2, beta=.05,

solve J.T*p=h*u and evaluate dL_h/dlambda=beta*lambda-p.T*F_lambda.
The adjoint is a Euclidean discrete vector; its right-hand side includes h.
It is not directly a nodal approximation of a differently normalized
continuous adjoint field. Parameter-dependent boundary conditions are outside
this example; their derivatives cannot generally be omitted.

## Reproduce

Requires Python 3.9 or later. From the extracted directory:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_sensitivity.py
MPLCONFIGDIR=.mplconfig python scripts/build_bratu_sensitivity.py
```

Outputs: docs/figures/bratu-sensitivity.json and bratu-sensitivity.png.
The JSON records six mesh-refinement cases, independently re-solved central
parameter differences, a nonlinear-tolerance sweep, separate primal/tangent/
adjoint residuals, condition numbers, and source/figure SHA-256 hashes.

Independent continuous references differentiate the exact alpha-family

    lambda(alpha)=2*alpha**2/cosh(alpha/2)**2,
    u_alpha(x)=-2*log(cosh(alpha*(x-.5))/cosh(alpha/2)).

The scalar continuous-gradient reference uses 96/192-point Gauss quadrature
of exact u*du/dlambda, not the discrete sensitivity itself. The two grid
sequences should exhibit second-order spatial convergence. All finite-
difference parameter samples re-solve the nonlinear problem from zero and
retain the actual residual and accepted update count. A very small parameter
step can worsen a check through subtraction and nonlinear solve error. Looser
and tighter requested tolerances sometimes accept the same Newton iterate.

The Bratu Jacobian is symmetric. A separate nonsymmetric three-state,
two-parameter manufactured problem therefore tests transpose/sign conventions
and an explicit objective-parameter term independently. The nine tests also
check the exact-family derivative, AD residual partials, primal and derivative
residuals, gradient agreement, independent finite differences and refinement.

This is a finite-dimensional smooth implicit/discrete-adjoint example, not a
reverse-mode AD library, an inverse fit, a continuous/time-dependent adjoint
solver, singular-fold continuation, or a performance comparison. One physical
parameter and one objective do not demonstrate an adjoint speed advantage.
The previous AD edition is unchanged; its AD and Newton modules are copied
byte-for-byte and identified in provenance.json. Floating-point last bits may
differ across hosts.

source-manifest.json hashes every payload file and is included inside the ZIP.
verification.json is beside the archive and records its hash, the nine tests
run after independent extraction, and identical rebuilt numerical evidence.
Code and explanatory text/data have separate terms: LICENSE and LICENSING.md.
