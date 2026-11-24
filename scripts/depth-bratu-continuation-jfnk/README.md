# Bratu continuation and Jacobian-free Newton–Krylov

同じ小さな無次元1次元境界値問題 `-u'' = lambda exp(u)`、`u(0)=u(1)=0` を使う2例です。
`bratu-fold-continuation` は重み付き擬似弧長で単純foldを越え、
`bratu-matrix-free-jfnk` は非線形Jacobianを組み立てない3種類のJvを比較します。
両例は同じ物理問題に属し、格子・枝・Jvの違いを別の物理問題として数えません。

These two educational cases share a small dimensionless one-dimensional Bratu boundary-value problem.
The continuation case deliberately assembles sparse Jacobians. The JFNK case uses callable products and a
constant Poisson preconditioner; it does not assemble the nonlinear Jacobian. The small Hessenberg matrix
and Krylov bases are stored. This distinction is narrower than saying that no matrix is ever used.

## Preserved qualification and this package revision

The preserved R3 execution passed all **27 pytest tests, 16 fixed records and 196 scientific gates**
(67 continuation plus 129 JFNK), with 341 finite numeric CSV rows. Its shared pytest/main time was
14.09155 seconds on the recorded local environment. That is a historical measurement, not a future
machine speed guarantee. Source, inputs, analytic-reference code, acceptance and tests were preserved.

This source draft changes presentation metadata and source-reading notes after that successful execution.
It does not change a solver, input, reference formula, acceptance threshold or test. The current contract
records the original source and receipt hashes. Its portable history is a clearly labeled transcription;
it does not pretend to bundle byte-identical private JUnit/log files. The full original R2 failure and
R3 source/results remain retained separately.

R2 originally failed the identity-callable GMRES test: the operator returned a view of the stored basis,
and in-place orthogonalization overwrote that basis. R3 made a working copy of the operator output.
The original identity regression and all other tests were retained, with no relaxed criterion. The failed
R2 did not reach the main calculations.

公開用の正本確認では、既存packagerがsource側mainと描画を1回、その後に独立ZIP展開の
27 pytestと全mainを1回実行します。これは同じ16記録・196判定の二つの独立な再現確認であり、
新しい科学caseを増やすものではありません。追加の予備mainや予備描画は行いません。
Archive/verification receipts record the actual canonical outcomes separately from the historical R3 pass.

## Reproduce from a fresh directory

Python 3.12 requires exactly `numpy==2.0.2`, `scipy==1.14.1` and `pytest==8.3.5`.
Plotting separately uses `matplotlib==3.9.4`. No PETSc, external AD library, compiler, network or
private checkout is needed. Use a fresh output directory so previous successful or failed results survive.

```sh
python -m pip install -r requirements.txt
python -B -W error -m pytest -q -p no:cacheprovider
python -B -W error run.py --input inputs.json --output output
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

The public independent verification has a shared 120-second pytest-plus-main limit with one BLAS thread.
All fixed inputs and acceptance conditions are in `inputs.json` and `acceptance.json`.
The archive's saved `results` are examples; reproduction should write to a new `output` directory.
`plot.py` accepts a result file or directory and reads accepted NPZ/CSV data only: it invokes no solver,
finite-difference evolution, quadrature or new analytic-reference calculation.

## Continuation: branches, fold and spatial error

The continuous family is

\[
u_\theta(x)=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\qquad
\lambda(\theta)=\frac{2\theta^2}{\cosh^2(\theta/2)}.
\]

The reference evaluates the family and its roots independently with 80-digit Decimal arithmetic.
It is not an exact solution of the centered finite-difference equations. The fixed spatial refinements
use 31, 63 and 127 interior nodes, zero endpoints, 80 steps of `ds=0.1`, and the weighted metric
`h sum(du_i^2) + d-lambda^2`. Predictor/tangent-hyperplane correctors follow the lower and upper branches.
A separate augmented fold solve checks the discrete equation, normalized null vector and simple-fold
transversality. Independent fixed-lambda=2 profiles check both branches.

The whole-curve family comparison uses the computed midpoint value as its explicitly stated family
coordinate. It is separate from the fixed-lambda profile comparison and from the tangent/fold conditions.
The continuous-versus-discrete fold difference is a spatial error. Arc steps are not physical time.

`lambda=4` is an intentional no-solution control, not a generic excuse for Newton failure. For the
positive first discrete eigenvector, and because the inverse Dirichlet Poisson matrix makes every solution at positive lambda positive, `exp(u) >= e*u` implies
`lambda <= mu_1/e < pi^2/e < 4`. The unsuccessful candidate iterates are retained and identified
separately; no other failed numerical condition is counted as a pass.

## JFNK: products, forcing and work

At lambda=3, use 63/127 interior nodes and starts zero or `4 sin(pi*x)` for the two branches.
Twelve solves compare analytic, central finite-difference and one-direction forward-AD products;
one additional analytic solve uses constant eta=1e-8. A Thomas solve applies the constant Poisson
right preconditioner. GMRES uses restart 24, at most 96 iterations, two-pass reorthogonalization and
Givens rotations. The outer method has at most 24 Newton steps and a 1e-9 residual tolerance.

The central product uses two real residual evaluations and
`delta = eps_machine^(1/3) (1+||u||_2) / ||v||_2`. AD differentiates the same residual expression
in one direction, including boundary padding. Zero directions have an explicit branch.
The forcing is initially 0.3, then `clamp(0.9*(||F_k||/||F_(k-1)||)^1.5, 0.001, 0.5)`.
This is an Eisenstat–Walker Choice 2-style residual-ratio rule with declared implementation changes:
the fixed floor/cap and Armijo globalization are not the paper's full safeguarded algorithm or PETSc defaults.
In particular, the fixed eta floor does not establish the original asymptotic convergence theorem.

Analytic Jv checks validate FD/AD results and the true linear-forcing residual, but never steer the
FD/AD iterates; those validation calls are counted separately. Primal and dual traversals, linear residuals,
line-search trials and bounded Krylov storage are saved. Evaluation counts are work diagnostics,
not a wall-clock speedup claim. The AD class supports only the elementary operations needed here,
not a general AD package. No universal speed, global convergence or large-scale performance is claimed.

## Sources and saved figures

Read scopes and URLs are recorded in `source-reading-addendum.json`. Selected primary readings include
Dickson et al. section 2.2, Knoll–Keyes sections on Jv/forcing/globalization, and the author-hosted
Eisenstat–Walker Algorithm IN, Choice 2 and safeguard passages. Langtangen's author exercise gives the
same Bratu family with a parameter twice ours. Original Bratu 1914 and unselected proofs/tables are unread.
PETSc documentation is context only; no PETSc computation or borrowed solver success is used.
The older `references/source-review.json` remains the original pre-R3 reading record; later reading is
an additive provenance record, not a rewrite of that history.

Both figures use actual stored fields and histories. The continuation figure shows the branch, the
independent fixed-lambda profiles, Jacobian singularity along arc steps and three-grid fold error.
The JFNK figure shows Newton residual histories, the finest upper field, saved derivative qualification
and actual evaluation counts. Main and preview images are supplied in PNG/SVG/PDF after authorized rendering.
