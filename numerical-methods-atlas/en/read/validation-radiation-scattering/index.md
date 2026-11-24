# Isotropically scattering slabs and continuum-angle references

Compare discrete ordinates in an isotropically scattering slab with an independent continuous-angle integral-equation reference.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Isotropic scattering in a finite slab

Solve genuinely coupled signed-angle steady transport and compare R/T/A with an independent continuum-angle Fredholm reference.

**Methods used**

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) (`radiation-transport`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-algorithm)

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

- [Static grey radiative transfer,scattering and linear exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en) (`static-grey-transfer`)

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.


**Problem figure**

![Isotropic scattering in a finite slab: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Isotropic scattering in a finite slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en) (`isotropic-scattering-slab`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isotropic-scattering-slab/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/?lang=en#isotropic-scattering-slab-en-validation)

Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.

- [Isotropically scattering slab: continuous-angle Fredholm flux reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isotropic-scattering-slab-en) (`isotropic-scattering-slab`; Same-problem reference · Semi-analytic reference)

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.
### Assumptions, units and boundaries

Four fixed inputs L=.5/3,albedo=.5/.9;unit left incoming radiance,right vacuum incoming.64/128/256cells at32signed angles and a separate64angle probe.

**Editorial clarification**

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

### Adopted numerical method

Conservative upwind FV with the full discrete angular source coupling solved by sweep-response elimination. Positive hemisphere Gauss weights normalize incoming fluxpi;absorption is independently accumulated from the volume source.

$$
\mu\partial_xI+I=\omega J,\quad J=\frac12\int_{-1}^{1}I\,d\mu
$$

$$
J(x)=\frac12E_2(x)+\frac\omega2\int_0^L E_1(|x-s|)J(s)\,ds
$$

$$
R+T+A=1,\qquad A=4(1-\omega)\int_0^LJ\,dx
$$

### References and validation

Independent reference78checks passed before main.18primary/control solves test budget,positivity,residuals,separate space/angle changes,pure absorption and conservative scattering.

### Limits

Limited to fourfixedisotropic slabs;noMC,generalphase-function/DISORT reproduction,universalorder or rigorouscontinuumerrorbound.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_runs": 18,
    "scattering_slabs": 4,
    "continuum_angle_reference": true,
    "separate_space_angle_probes": true,
    "stochastic_runs": 0
  },
  "checks": {
    "slab0-n64-s32/finite-positive": true,
    "slab0-n64-s32/residual": true,
    "slab0-n64-s32/source_residual": true,
    "slab0-n64-s32/balance": true,
    "slab0-n64-s32/physical-fluxes": true,
    "slab0-n128-s32/finite-positive": true,
    "slab0-n128-s32/residual": true,
    "slab0-n128-s32/source_residual": true,
    "slab0-n128-s32/balance": true,
    "slab0-n128-s32/physical-fluxes": true,
    "slab0-n256-s32/finite-positive": true,
    "slab0-n256-s32/residual": true,
    "slab0-n256-s32/source_residual": true,
    "slab0-n256-s32/balance": true,
    "slab0-n256-s32/physical-fluxes": true,
    "slab0-n256-s64/finite-positive": true,
    "slab0-n256-s64/residual": true,
    "slab0-n256-s64/source_residual": true,
    "slab0-n256-s64/balance": true,
    "slab0-n256-s64/physical-fluxes": true,
    "slab0/refinement-n128": true,
    "slab0/refinement-n256": true,
    "slab0/finest-independent-error": true,
    "slab0/space-probe": true,
    "slab0/angle-probe": true,
    "slab1-n64-s32/finite-positive": true,
    "slab1-n64-s32/residual": true,
    "slab1-n64-s32/source_residual": true,
    "slab1-n64-s32/balance": true,
    "slab1-n64-s32/physical-fluxes": true,
    "slab1-n128-s32/finite-positive": true,
    "slab1-n128-s32/residual": true,
    "slab1-n128-s32/source_residual": true,
    "slab1-n128-s32/balance": true,
    "slab1-n128-s32/physical-fluxes": true,
    "slab1-n256-s32/finite-positive": true,
    "slab1-n256-s32/residual": true,
    "slab1-n256-s32/source_residual": true,
    "slab1-n256-s32/balance": true,
    "slab1-n256-s32/physical-fluxes": true,
    "slab1-n256-s64/finite-positive": true,
    "slab1-n256-s64/residual": true,
    "slab1-n256-s64/source_residual": true,
    "slab1-n256-s64/balance": true,
    "slab1-n256-s64/physical-fluxes": true,
    "slab1/refinement-n128": true,
    "slab1/refinement-n256": true,
    "slab1/finest-independent-error": true,
    "slab1/space-probe": true,
    "slab1/angle-probe": true,
    "slab2-n64-s32/finite-positive": true,
    "slab2-n64-s32/residual": true,
    "slab2-n64-s32/source_residual": true,
    "slab2-n64-s32/balance": true,
    "slab2-n64-s32/physical-fluxes": true,
    "slab2-n128-s32/finite-positive": true,
    "slab2-n128-s32/residual": true,
    "slab2-n128-s32/source_residual": true,
    "slab2-n128-s32/balance": true,
    "slab2-n128-s32/physical-fluxes": true,
    "slab2-n256-s32/finite-positive": true,
    "slab2-n256-s32/residual": true,
    "slab2-n256-s32/source_residual": true,
    "slab2-n256-s32/balance": true,
    "slab2-n256-s32/physical-fluxes": true,
    "slab2-n256-s64/finite-positive": true,
    "slab2-n256-s64/residual": true,
    "slab2-n256-s64/source_residual": true,
    "slab2-n256-s64/balance": true,
    "slab2-n256-s64/physical-fluxes": true,
    "slab2/refinement-n128": true,
    "slab2/refinement-n256": true,
    "slab2/finest-independent-error": true,
    "slab2/space-probe": true,
    "slab2/angle-probe": true,
    "slab3-n64-s32/finite-positive": true,
    "slab3-n64-s32/residual": true,
    "slab3-n64-s32/source_residual": true,
    "slab3-n64-s32/balance": true,
    "slab3-n64-s32/physical-fluxes": true,
    "slab3-n128-s32/finite-positive": true,
    "slab3-n128-s32/residual": true,
    "slab3-n128-s32/source_residual": true,
    "slab3-n128-s32/balance": true,
    "slab3-n128-s32/physical-fluxes": true,
    "slab3-n256-s32/finite-positive": true,
    "slab3-n256-s32/residual": true,
    "slab3-n256-s32/source_residual": true,
    "slab3-n256-s32/balance": true,
    "slab3-n256-s32/physical-fluxes": true,
    "slab3-n256-s64/finite-positive": true,
    "slab3-n256-s64/residual": true,
    "slab3-n256-s64/source_residual": true,
    "slab3-n256-s64/balance": true,
    "slab3-n256-s64/physical-fluxes": true,
    "slab3/refinement-n128": true,
    "slab3/refinement-n256": true,
    "slab3/finest-independent-error": true,
    "slab3/space-probe": true,
    "slab3/angle-probe": true,
    "control0/budget": true,
    "control0/pure-absorption": true,
    "control1/budget": true,
    "control1/conservative": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/isotropic-scattering-slab/index.json

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/isotropic-scattering-slab-preview.png)

Scientific preview from the actual saved numerical fields.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/atlas-radiation-scattering-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/radiation-scattering/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Pharr,Jakob,Humphreys (2023). Physically Based Rendering4e,14.1The Equation of Transfer [accessed 2026-11-24]. https://www.pbr-book.org/4ed/Light_Transport_II_Volume_Rendering/The_Equation_of_Transfer; review_level=primary-author-book-selected-equations
Read14.1transfer/source/finite-ray boundary formulation. Isotropic slab/Fredholm normalization independently derived here;not DISORTpaper/table reproduction.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
