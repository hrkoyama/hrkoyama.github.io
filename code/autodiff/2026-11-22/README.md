# Forward automatic differentiation and Bratu verification

Supplemental source edition: 2026-11-22. Public chapter:
Japanese: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/
English: https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/

This self-contained NumPy example compares an analytic Jacobian, finite
differences and genuine forward automatic differentiation on the same Bratu
residual. It includes the existing damped Newton solver and a minimal package
initializer. The only builder adaptation replaces the original broad-suite test
hash with the packaged dedicated test hash. provenance.json records the original
input hashes. No source checkout or network is needed after dependencies exist.

## Reproduce

Requires Python 3.9 or later. From the extracted directory:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q tests/test_autodiff.py
MPLCONFIGDIR=.mplconfig python scripts/build_autodiff.py
```

Outputs: docs/figures/autodiff-bratu.json and autodiff-bratu.png. The JSON records
all source hashes, derivative checks, finite-difference sweeps and nine Newton
runs. The residual is -u_xx-lambda exp(u)=0 on [0,1], with zero Dirichlet boundary
data, lambda=2/cosh(1/2)^2 and 15/31/63 interior nodes. Each method starts at zero,
uses the same dense Armijo-Newton solver and stops at absolute residual 2-norm
1e-10. Central differences in Newton use absolute perturbation 1e-5. Separate
forward/central sweeps run from 1 down to 1e-14.

This implements one-direction forward AD, with one seed per Jacobian column.
Reverse mode, implicit sensitivity, adaptive integrator differentiation and
nonsmooth shock sensitivities are outside this package. No performance ranking
is claimed. Discrete-root agreement and second-order spatial error are checked
separately. Last-bit rounding can depend on NumPy and the host platform.

source-manifest.json hashes every payload file and is also inside the ZIP.
verification.json is published beside the archive and records its SHA-256,
independent extracted-package test results and the numerical rebuild check.
Code and content have distinct terms; see LICENSE and LICENSING.md.
