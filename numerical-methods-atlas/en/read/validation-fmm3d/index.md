# 3D1/r kernels: expansions,trees and force checks

Check nonzero final contributions through actual3D M2M,M2L,L2L paths and unique interaction ownership.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Actual3D1/r FMM: multilevel translations, force and ownership

Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.

**Methods used**

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) (`fmm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-algorithm)

Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

- [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en) (`particle-gravity`)

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.


**Problem figure**

![Actual3D1/r FMM: multilevel translations, force and ownership: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en) (`fmm3d-inverse-r`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-validation)

Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.

- [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fmm3d-inverse-r-en) (`fmm3d-inverse-r`; Same-problem reference · Finite-grid numerical reference)

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.
### Assumptions, units and boundaries

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

**Editorial clarification**

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

### Adopted numerical method

Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

### References and validation

Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.

### Limits

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_potential_error": 2.8255260194168475e-09,
    "finest_acceleration_error": 3.9236249160985455e-07,
    "primary_runs": 6,
    "additional_fixed_evaluations": 2
  },
  "checks": {
    "p3-d2 finite potential and force": true,
    "p3-d2 exact interaction ownership": true,
    "p3-d2 far path exercised": true,
    "p3-d2 actual forced depth": true,
    "p5-d2 finite potential and force": true,
    "p5-d2 exact interaction ownership": true,
    "p5-d2 far path exercised": true,
    "p5-d2 actual forced depth": true,
    "p7-d2 finite potential and force": true,
    "p7-d2 exact interaction ownership": true,
    "p7-d2 far path exercised": true,
    "p7-d2 actual forced depth": true,
    "p3-d3 finite potential and force": true,
    "p3-d3 exact interaction ownership": true,
    "p3-d3 far path exercised": true,
    "p3-d3 actual forced depth": true,
    "p3-d3 nonzero complete translation chain": true,
    "p5-d3 finite potential and force": true,
    "p5-d3 exact interaction ownership": true,
    "p5-d3 far path exercised": true,
    "p5-d3 actual forced depth": true,
    "p5-d3 nonzero complete translation chain": true,
    "p7-d3 finite potential and force": true,
    "p7-d3 exact interaction ownership": true,
    "p7-d3 far path exercised": true,
    "p7-d3 actual forced depth": true,
    "p7-d3 nonzero complete translation chain": true,
    "adaptive finite fields": true,
    "adaptive exact ownership": true,
    "adaptive far path": true,
    "adaptive unequal actual levels": true,
    "adaptive capped bucket retained": true,
    "adaptive potential accuracy": true,
    "adaptive force accuracy": true,
    "d2 finest potential_error": true,
    "d2 order refinement potential_error": true,
    "d2 finest acceleration_error": true,
    "d2 order refinement acceleration_error": true,
    "d3 finest potential_error": true,
    "d3 order refinement potential_error": true,
    "d3 finest acceleration_error": true,
    "d3 order refinement acceleration_error": true,
    "direct octahedron potential golden": true,
    "direct octahedron acceleration golden": true,
    "rigid transformed potential": true,
    "rigid transformed acceleration": true,
    "rigid transformed ownership": true,
    "rigid transformed actual level": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/index.json

![Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

Validation figure from actual saved fixed-input calculation arrays.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- The black-box fast multipole method. https://mc.stanford.edu/cgi-bin/images/f/fa/Darve_bbfmm_2009.pdf; review_level=primary-selected-sections
Tensor interpolation Eq7 and multilevel stages sections2–3 inspected, printed8715–8717; compression is separate. Original uncompressed educational implementation here, no timing reproduction.

- FMM3D mathematical definitions. https://fmm3d.readthedocs.io/en/latest/math.html; review_level=official-kernel-normalization
Official potential+1/(4pi r), gradient and source-self convention inspected. Our gravitational kernel is-1/r; FMM3D is not installed or run.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
