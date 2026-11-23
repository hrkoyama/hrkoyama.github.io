# mesh-boundary fixed lightweight PDE cases

Run Python3.10+ with the exact3pins in requirements.txt.

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

Tests and all fixed inputs share one120second group budget. No network/private source is required. The runner rejects changed frozen sources and nonempty output. plot.py reads only saved arrays; it needs Matplotlib3.9.4. NPZ files retain actual grid/fields/reference and stage or face budgets; CSV/result.json retain every decision. PNG/SVG/PDF and preview PNGs are generated from those arrays.

The bilingual cases.json is the detailed model/input/algorithm/reference/limits specification. Selected primary/official source review scopes are under references/. All MMS and numerical code are newly implemented, without copied third-party code. An analytic qualification or same-matrix alternative solve is not an independent PDE engine.

Current cases:
- lshape-fem: L-shaped[-1,1]² minus quadrantIV, theta0..3pi/2, analytic Dirichlet harmonic corner field. N8/16/32, fixed map x→x max(|x|,|y|). Separate unit-square sine MMS uses regular/warped grids. No smooth-square L2 order is imposed on the singular field. Fixed a-priori grading is not an AMR engine. Conditioning is estimated; arbitrary distortion is not certified.
- annular-viscous-mms: 1≤r≤2, periodic angle, mu=1+.2r², lambda0 and zero velocity on both circles. A(s)=(s−1)(4−s), u=(A(1+xy),A(x²−y²)/2). Nr8/16/32,Ntheta2Nr. A linear vector viscous BVP, without divergence-free constraint, pressure or nonlinear Navier–Stokes. r>0 only; no axis stencil certification.
- poisson-neumann: Unit square N16/32/64, cell-centred point DOFs, cosine exact field, homogeneous Neumann; mean0 andN32 mean.25 probe. A different linear solver of the same matrix is not an independent PDE discretization; no general boundary/MG claim.
- poisson-robin: Unit square N16/32/64; cosine-plus-linear exact field. x walls Neumann±1; y walls analytic Robin alpha1,beta.5. The unique Robin problem has no additional mean gauge. Algebraic boundary satisfaction differs from physical flux accuracy.

No original acceptance values or existing releases are changed. MIT applies only to original implementation code; site rights apply separately to prose/inputs/figures.
