# Bratu fold continuation and Jacobian-free Newton-Krylov

The same one-dimensional Bratu problem compares fold continuation and matrix-free iteration against an independently evaluated analytic family.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Crossing the Bratu fold with pseudo-arclength continuation

Follow the lower and upper branches of the same one-dimensional Bratu boundary-value problem; check tangents, the fold and spatial error against an independent analytic family.

**Methods used**

- [Weighted pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=en) (`pseudo-arclength-continuation`)
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-algorithm)

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.


**Problem figure**

![Crossing the Bratu fold with pseudo-arclength continuation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en) (`bratu-fold-continuation`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=en#bratu-fold-continuation-en-validation)

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

- [Crossing the Bratu fold with pseudo-arclength continuation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-continuation-en) (`bratu-fold-continuation`; Same-problem reference · Analytic reference)

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.
### Assumptions, units and boundaries

Dimensionless x in [0,1] with zero Dirichlet endpoints and 31/63/127 interior nodes. Take 80 fixed ds=0.1 steps from the zero solution. Correct both branches at lambda=2; lambda=4 is a deliberate discrete no-solution control. Pseudo-arclength is not physical time.

**Editorial clarification**

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

### Adopted numerical method

Use a unit tangent in h-sum(du squared)+d-lambda squared, a predictor and a tangent-hyperplane Newton corrector. A separate augmented system locates the fold and a normalized null vector. This case deliberately assembles sparse Jacobians.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

### References and validation

The preserved R3 run passed the shared 27 pytest tests and this case’s 67 fixed gates. Discrete residuals, tangent orientation/normalization, fold/null/transversality conditions, an independent Decimal80 family and fixed three-grid errors are checked separately.

### Limits

A small one-dimensional simple fold only. The whole-curve family comparison uses the computed midpoint as its family coordinate and is distinct from the independent fixed-lambda profile checks. The continuum fold is not an exact discrete solution. No general bifurcation-tracking or large-scale performance claim.

### Stored measurements and decisions

```json
{
  "metrics": {
    "fold_orders": [
      2.0003257002223824,
      2.000081417263765
    ],
    "intended_failure_reason": "line search exhausted",
    "discrete_nonexistence_bound": 3.6300955492983498,
    "matching": "Fullpathfamilycoordinatefrommidpointisexplicit;separatefixedlambda2rootsvalidatebothbrancheswithoutparameterfitting.",
    "reference_qualification_max_ODE": 6e-78
  },
  "checks": {
    "N31/finite complete branch": true,
    "N31/discrete residual": true,
    "N31/unit tangent": true,
    "N31/tangent equation": true,
    "N31/tangent orientation": true,
    "N31/turning tangent": true,
    "N31/lower and upper lambda2 neighborhoods": true,
    "N31/fold discrete equation": true,
    "N31/fold null equation": true,
    "N31/fold null normalization": true,
    "N31/fold sigma_min": true,
    "N31/simple fold parameter transversality": true,
    "N31/simple fold quadratic transversality": true,
    "N31/lower discrete root": true,
    "N31/upper discrete root": true,
    "N31/ordered distinct branches": true,
    "N31/nonzero reference fields": true,
    "N63/finite complete branch": true,
    "N63/discrete residual": true,
    "N63/unit tangent": true,
    "N63/tangent equation": true,
    "N63/tangent orientation": true,
    "N63/turning tangent": true,
    "N63/lower and upper lambda2 neighborhoods": true,
    "N63/fold discrete equation": true,
    "N63/fold null equation": true,
    "N63/fold null normalization": true,
    "N63/fold sigma_min": true,
    "N63/simple fold parameter transversality": true,
    "N63/simple fold quadratic transversality": true,
    "N63/lower discrete root": true,
    "N63/upper discrete root": true,
    "N63/ordered distinct branches": true,
    "N63/nonzero reference fields": true,
    "N127/finite complete branch": true,
    "N127/discrete residual": true,
    "N127/unit tangent": true,
    "N127/tangent equation": true,
    "N127/tangent orientation": true,
    "N127/turning tangent": true,
    "N127/lower and upper lambda2 neighborhoods": true,
    "N127/fold discrete equation": true,
    "N127/fold null equation": true,
    "N127/fold null normalization": true,
    "N127/fold sigma_min": true,
    "N127/simple fold parameter transversality": true,
    "N127/simple fold quadratic transversality": true,
    "N127/lower discrete root": true,
    "N127/upper discrete root": true,
    "N127/ordered distinct branches": true,
    "N127/nonzero reference fields": true,
    "Decimal80 continuum ODE": true,
    "Decimal80 zero endpoints": true,
    "reference fixed lambda": true,
    "reference fold printed anchor": true,
    "no-solution lambda4 proof bound": true,
    "lambda4 Newton reports failure": true,
    "lambda4 finite retained states": true,
    "lambda4 remains above tolerance": true,
    "finest full path shape": true,
    "finest family curve lambda": true,
    "finest continuous fold error": true,
    "fold first refinement order": true,
    "fold second refinement order": true,
    "finest lower exact solution": true,
    "finest upper exact solution": true,
    "both branch errors refine": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/index.json

![Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

Preview of the stored branch,lambda=2 profiles,smallest Jacobian singular value and three-grid fold error. Arclength steps are not physical time.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- K.I.Dickson,C.T.Kelley,I.C.F.Ipsen,I.G.Kevrekidis (2007). Condition Estimates for Pseudo-Arclength Continuation. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=primary-selected-PDF-text
Read selected original sec2.2 tangent,normalization,hyperplane andsimple-fold scope; nofullproof audit.

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
Read author exercise exactfamily/twobranches/roundedcritical; itsparameter istwiceourtheta. Independentderivation/Decimal80qualification;1914originalunread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

**Methods used**

- [Jacobian-free Newton-Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=en) (`jacobian-free-newton-krylov`)
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) (`gmres`)
- [Thomas tridiagonal elimination](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en) (`thomas`)
- [Automatic differentiation](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=en) (`automatic-differentiation`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-algorithm)

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.


**Problem figure**

![Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-validation)

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en) (`bratu-matrix-free-jfnk`; Same-problem reference · Analytic reference)

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.
### Assumptions, units and boundaries

The same dimensionless one-dimensional Dirichlet problem at lambda=3, 63/127 interior nodes, starting from zero or 4sin(pi*x). Twelve mode/grid/branch solves plus one analytic-Jv constant-eta=1e-8 control. GMRES restart24/max96, at most 24 Newton steps and nonlinear tolerance1e-9.

**Editorial clarification**

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

### Adopted numerical method

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

### References and validation

The preserved R3 run passed the shared27 pytest tests and this case’s129 fixed gates: nonzero analytic Jv qualification, discrete residuals, independent analytic branches, mode agreement, forcing, evaluation ledgers, Krylov storage, Armijo and the constant-eta control. Analytic forcing validation is counted separately and does not steer FD/AD iterations.

### Limits

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

### Stored measurements and decisions

```json
{
  "metrics": {
    "mode_gap_max": 4.884981308350689e-15,
    "qualification_AD_relative": 1.1692887409033045e-17,
    "qualification_FD_relative": 8.651069407676375e-11,
    "reasons": [
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual"
    ],
    "evaluation_scope": "Actualsolverevaluations;analyticlinear-forcingvalidationcountedseparately.NoPETScorassemblednonlinearJacobianusedbyJFNK."
  },
  "checks": {
    "nonzero Jv reference": true,
    "AD Jv exact": true,
    "AD primal exact": true,
    "central FD Jv": true,
    "zero Jv branch": true,
    "0/nonlinear converged": true,
    "0/finite states": true,
    "0/discrete residual": true,
    "0/continuous branch error": true,
    "0/analytic verified forcing": true,
    "0/declared eta": true,
    "0/evaluation count ledger": true,
    "0/bounded Krylov storage": true,
    "0/accepted Armijo steps": true,
    "1/nonlinear converged": true,
    "1/finite states": true,
    "1/discrete residual": true,
    "1/continuous branch error": true,
    "1/analytic verified forcing": true,
    "1/declared eta": true,
    "1/evaluation count ledger": true,
    "1/bounded Krylov storage": true,
    "1/accepted Armijo steps": true,
    "2/nonlinear converged": true,
    "2/finite states": true,
    "2/discrete residual": true,
    "2/continuous branch error": true,
    "2/analytic verified forcing": true,
    "2/declared eta": true,
    "2/evaluation count ledger": true,
    "2/bounded Krylov storage": true,
    "2/accepted Armijo steps": true,
    "3/nonlinear converged": true,
    "3/finite states": true,
    "3/discrete residual": true,
    "3/continuous branch error": true,
    "3/analytic verified forcing": true,
    "3/declared eta": true,
    "3/evaluation count ledger": true,
    "3/bounded Krylov storage": true,
    "3/accepted Armijo steps": true,
    "4/nonlinear converged": true,
    "4/finite states": true,
    "4/discrete residual": true,
    "4/continuous branch error": true,
    "4/analytic verified forcing": true,
    "4/declared eta": true,
    "4/evaluation count ledger": true,
    "4/bounded Krylov storage": true,
    "4/accepted Armijo steps": true,
    "5/nonlinear converged": true,
    "5/finite states": true,
    "5/discrete residual": true,
    "5/continuous branch error": true,
    "5/analytic verified forcing": true,
    "5/declared eta": true,
    "5/evaluation count ledger": true,
    "5/bounded Krylov storage": true,
    "5/accepted Armijo steps": true,
    "6/nonlinear converged": true,
    "6/finite states": true,
    "6/discrete residual": true,
    "6/continuous branch error": true,
    "6/analytic verified forcing": true,
    "6/declared eta": true,
    "6/evaluation count ledger": true,
    "6/bounded Krylov storage": true,
    "6/accepted Armijo steps": true,
    "7/nonlinear converged": true,
    "7/finite states": true,
    "7/discrete residual": true,
    "7/continuous branch error": true,
    "7/analytic verified forcing": true,
    "7/declared eta": true,
    "7/evaluation count ledger": true,
    "7/bounded Krylov storage": true,
    "7/accepted Armijo steps": true,
    "8/nonlinear converged": true,
    "8/finite states": true,
    "8/discrete residual": true,
    "8/continuous branch error": true,
    "8/analytic verified forcing": true,
    "8/declared eta": true,
    "8/evaluation count ledger": true,
    "8/bounded Krylov storage": true,
    "8/accepted Armijo steps": true,
    "9/nonlinear converged": true,
    "9/finite states": true,
    "9/discrete residual": true,
    "9/continuous branch error": true,
    "9/analytic verified forcing": true,
    "9/declared eta": true,
    "9/evaluation count ledger": true,
    "9/bounded Krylov storage": true,
    "9/accepted Armijo steps": true,
    "10/nonlinear converged": true,
    "10/finite states": true,
    "10/discrete residual": true,
    "10/continuous branch error": true,
    "10/analytic verified forcing": true,
    "10/declared eta": true,
    "10/evaluation count ledger": true,
    "10/bounded Krylov storage": true,
    "10/accepted Armijo steps": true,
    "11/nonlinear converged": true,
    "11/finite states": true,
    "11/discrete residual": true,
    "11/continuous branch error": true,
    "11/analytic verified forcing": true,
    "11/declared eta": true,
    "11/evaluation count ledger": true,
    "11/bounded Krylov storage": true,
    "11/accepted Armijo steps": true,
    "12/nonlinear converged": true,
    "12/finite states": true,
    "12/discrete residual": true,
    "12/continuous branch error": true,
    "12/analytic verified forcing": true,
    "12/declared eta": true,
    "12/evaluation count ledger": true,
    "12/bounded Krylov storage": true,
    "12/accepted Armijo steps": true,
    "mode agreement N63 lower": true,
    "mode agreement N63 upper": true,
    "mode agreement N127 lower": true,
    "mode agreement N127 upper": true,
    "finest exact branches": true,
    "all mode errors refine": true,
    "constant forcing companion matches": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/index.json

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- D.A.Knoll,D.E.Keyes (2004). Jacobian-free Newton-Krylov methods: a survey of approaches and applications. https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf; review_level=primary-selected-PDF-text-via-course-mirror
Selected primary Jv,FDscale,inexactforcing andpreconditioning sections readvia disclosedcourse mirror; centralFD/cappedrule areexplicitimplementation choices.

- S. C. Eisenstat and H. F. Walker (1996). Choosing the Forcing Terms in an Inexact Newton Method. https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf; review_level=primary-selected-PDF-text
Read selected Algorithm IN, Choice 2 and safeguard passages from the author-hosted original; not a full proof or performance-table audit.

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
Read author exercise exactfamily/twobranches/roundedcritical; itsparameter istwiceourtheta. Independentderivation/Decimal80qualification;1914originalunread.

- PETSc developers (2026). PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length. https://petsc.org/release/manual/snes/; review_level=official-selected-documentation
Selected official3.26.1sections only; noPETSc execution orborrowed result. Distinguish itsquadraticarcconstraint fromourhyperplane.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
