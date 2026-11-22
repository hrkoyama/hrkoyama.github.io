# Bratu inverse estimation — reproducible supplement

Edition: **2026-11-22**. Public release:
<https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/>.

This self-contained Python supplement estimates the scalar parameter lambda from
five fixed point observations of the one-dimensional Bratu equation. It uses a
discrete-adjoint gradient inside a bounded projected-gradient optimizer with
Armijo backtracking. It needs no network after dependencies are installed.

Run from the extracted directory:

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_inverse.py
python scripts/build_bratu_inverse.py
```

The builder writes `docs/figures/bratu-inverse.json` and
`docs/figures/bratu-inverse.png`. All synthetic observations and the fixed
perturbation vector are saved in `inputs/synthetic-observations.json`. The JSON
records settings, complete accepted optimization histories, residuals, parameter
errors, independently re-solved finite-difference checks, objective-only golden
section references, and source/figure SHA-256 hashes. `source-manifest.json`
lists every release payload hash. `verification.json` records actual tests run
after independent ZIP extraction, archive hash, and identical evidence rebuild.
The receipt is outside the archive to avoid a self-referential archive hash.

The forward residual is `F=D*u-lambda*exp(u)` with fixed zero endpoints. For
`r=H*u-d`, `L=.5*r.T*W*r+.5*gamma*(lambda-prior)^2`, solve
`J.T*p=H.T*W*r`, then `g=gamma*(lambda-prior)+p.T*exp(u)`. The five sensor
positions are 0.125, 0.25, 0.5, 0.75 and 0.875; they are exact grid nodes on all
four meshes. No sensor interpolation is hidden. Every forward solve starts
from zero. The bound `[0.2,3.4]` restricts the experiment to the tested smooth
lower branch; continuation and fold crossing are outside this example.

Three checks answer different questions:

1. Same-discrete noiseless observations on 31 interior nodes recover the
   generating parameter from three initial guesses. This is an inverse-crime
   **code-consistency control**, not independent evidence of physical accuracy.
2. Independent observations from the exact continuous family with alpha=1.5
   stay fixed while the inverse mesh uses 15, 31, 63 and 127 interior nodes.
   Their parameter bias decreases at approximately second order.
3. One saved deterministic perturbation vector of order 0.001 per sensor
   changes the fitted parameter and leaves a nonzero data residual. It is not
   a statistical probability model and does not justify confidence intervals.

The optimizer uses only adjoint gradients. Direct implicit derivatives and
central parameter differences are independent diagnostics; the latter solve
the forward problem separately at both perturbed parameters. The golden-section
reference uses objective values only and assumes unimodality on its bracket.
A sampled objective landscape supports this particular example without proving
global convergence or identifiability. Fixed boundary observations alone have
zero information about lambda and are rejected by the unregularized fitter.
An active-bound projected stationary point need not recover the truth.

`numart/autodiff.py`, `numart/krylov.py` and
`numart/bratu_sensitivity.py` are retained byte for byte from the preceding
[implicit/adjoint release](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/).
The new files are the inverse helper, builder, observations and tests.
`LICENSE` and `LICENSING.md` state the reuse terms. Dependencies are NumPy,
Matplotlib and pytest; the verification receipt records the versions used.
