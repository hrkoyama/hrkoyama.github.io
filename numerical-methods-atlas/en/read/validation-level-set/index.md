# Level sets: 2D circle translation and rigid rotation

Numerically transport the signed-distance zero contour on32²/64²/128² grids, comparing optional redistancing, analytic interface positions, geometric area and coupled grid/time refinement. VOF is a conceptual comparison only.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## 2D level-set circle translation: interface, area and redistancing

Translate a radius.15 circle from(.3,.35) at velocity(.2,.1) toT=1. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

**Methods used**

- [Level-set method](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en) (`level-set`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-algorithm)

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en) (`level-set-advection`)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.


**Problem figure**

![2D level-set circle translation: interface, area and redistancing: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=en#level-set-translation-en-validation)

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en) (`level-set-translation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en) (`level-set-rotation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
### Assumptions, units and boundaries

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

### Adopted numerical method

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

### References and validation

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

### Limits

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_grid": 128,
    "final_time": 1.0,
    "advection_observed_order": 1.8968704888340944,
    "advection_finest_interface_error": 0.00029557712133185254,
    "advection_finest_relative_area_error": 0.002182466628085633,
    "redistance_finest_interface_error": 0.0011428359418646783,
    "redistance_finest_relative_area_error": 0.00931654728247977,
    "redistance_maximum_area_jump": 0.0005264752370461312,
    "cfl_halving_band_phi_difference_n64": 1.4067607491909376e-05
  },
  "checks": {
    "advection_interface_refines": true,
    "advection_order_resolved": true,
    "advection_finest_interface": true,
    "advection_finest_area": true,
    "redistance_finest_interface": true,
    "redistance_finest_area": true,
    "shared_observation_times": true,
    "courant_bound": true,
    "time_step_sensitivity": true,
    "fixed_redistance_schedule": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs-initial.json

### Sources and review scope

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf; review_level=full-text
  Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://www.sciencedirect.com/science/article/pii/0021999181901455; review_level=abstract-and-metadata
  Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://epubs.siam.org/doi/10.1137/S1064827596298245; review_level=abstract-and-metadata
  Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf; review_level=full-text
  Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2D rigid rotation of an off-center level-set circle

Rotate a radius.15 circle initially centered at(.68,.5) once about(.5,.5), with angular speed2pi. ENO2/Heun on32²/64²/128² grids compares optional redistancing, intermediate interfaces, geometric area and coupled grid/time refinement.

**Methods used**

- [Level-set method](https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=en) (`level-set`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-algorithm)

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

- [Level-set interface advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#level-set-advection-en) (`level-set-advection`)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.


**Problem figure**

![2D rigid rotation of an off-center level-set circle: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Advection of a level-set circle](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en) (`level-set-circle`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=en#level-set-rotation-en-validation)

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

- [2D level-set circle translation: interface, area and redistancing: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-translation-en) (`level-set-translation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.

- [2D rigid rotation of an off-center level-set circle: analytic signed-distance reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-level-set-rotation-en) (`level-set-rotation`; Same-problem reference · Analytic reference)

Analytic circle center motion and signed distance provide references for translation and off-center rigid rotation. Interface/area errors of both modes are measured; this is not a VOF or two-phase fluid execution.
### Assumptions, units and boundaries

All quantities are nondimensional on[0,1]², with phi<0 inside. The prescribed divergence-free rigid motion keeps the circle away from the boundary. Two exterior ghost layers receive analytic data at each RK stage; this is not a periodic boundary. Every interior value is numerically advanced. Observe0/.25/.5/.75/1; max(|u|+|v|)dt/dx<=.35.

### Adopted numerical method

Both modes use the same second-order ENO one-sided differences and Heun RK2, selecting stencils by absolute second differences. Optional redistancing occurs every.1 physical time: five first-order Godunov steps, dtau=.3dx, with the smoothed sign frozen per call. There is no volume correction, interface projection, phi clipping, hidden retry or analytic interior reset.

$$
\Gamma(t)=\{\mathbf{x}:\phi(\mathbf{x},t)=0\},\quad \phi_t+\mathbf{u}\cdot\nabla\phi=0,\quad\phi_{\rm ref}(\mathbf{x},t)=\|\mathbf{x}-\mathbf{c}(t)\|-0.15
$$

$$
\psi_\tau+S_\epsilon(\phi_0)(\|\nabla\psi\|-1)=0,\quad S_\epsilon(z)=z/\sqrt{z^2+\Delta x^2}
$$

$$
E_\Gamma=\max_{t\in\{.25,.5,.75,1\}}\max_{\mathbf{z}\in Z_h(t)}\left|\|\mathbf{z}-\mathbf{c}(t)\|-r\right|,\quad E_A=\max_t\left|A_h(t)/(\pi r^2)-1\right|
$$

### References and validation

Analytic center motion and signed distance provide the reference. Take worst errors over the four positive common observation times. Interface error samples linearly interpolated grid-edge zeros; area comes from the negative portion of a piecewise-linear triangulation between grid centers, retaining initial geometric bias. Also record phi error and distance-gradient quality in|phi_exact|<=2dx, each redistancing area jump and a separateN64 CFL-halving sensitivity.

### Limits

Sampled radial error is not a Hausdorff distance. Observed order refines dx and dt together rather than isolating spatial order. Redistancing need not improve area or position; errors increase here even on the finest grid. No numerical VOF ranking, separate PDE engine, topology change, curvature flow, surface tension or two-phase Navier–Stokes validation is claimed. The two motions are conditions of one transported-circle-interface problem.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_grid": 128,
    "final_time": 1.0,
    "advection_observed_order": 2.0215147988362197,
    "advection_finest_interface_error": 0.0013945082921070773,
    "advection_finest_relative_area_error": 0.010638924591504395,
    "redistance_finest_interface_error": 0.0021776855808661455,
    "redistance_finest_relative_area_error": 0.020243352863389963,
    "redistance_maximum_area_jump": 0.0005648260383181863,
    "cfl_halving_band_phi_difference_n64": 7.785529870305357e-06
  },
  "checks": {
    "advection_interface_refines": true,
    "advection_order_resolved": true,
    "advection_finest_interface": true,
    "advection_finest_area": true,
    "redistance_finest_interface": true,
    "redistance_finest_area": true,
    "shared_observation_times": true,
    "courant_bound": true,
    "time_step_sensitivity": true,
    "fixed_redistance_schedule": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/atlas-level-set-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/inputs-initial.json

### Sources and review scope

- S. Osher and J. A. Sethian (1988). Fronts propagating with curvature-dependent speed: Algorithms based on Hamilton-Jacobi formulations. https://math.berkeley.edu/~sethian/Papers/sethian.osher.88.pdf; review_level=full-text
  Selected author-hosted original passages: abstract, implicit front representation and Hamilton–Jacobi transport/normal-motion formulation. No full-paper audit or reproduction of its full experiment suite.
- C. W. Hirt and B. D. Nichols (1981). Volume of fluid (VOF) method for the dynamics of free boundaries. https://www.sciencedirect.com/science/article/pii/0021999181901455; review_level=abstract-and-metadata
  Publisher bibliography and abstract for the original volume-fraction formulation. No full-text algorithm audit or implementation of its donor–acceptor scheme.
- M. Sussman and E. Fatemi (1999). An Efficient, Interface-Preserving Level Set Redistancing Algorithm and Its Application to Interfacial Incompressible Fluid Flow. https://epubs.siam.org/doi/10.1137/S1064827596298245; review_level=abstract-and-metadata
  Official abstract and bibliography: redistancing quality includes retaining the zero interface; its constrained higher-order algorithm is not the simple Godunov auxiliary iteration implemented here.
- M. Sussman and E. G. Puckett (2000). A Coupled Level Set and Volume-of-Fluid Method for Computing 3D and Axisymmetric Incompressible Two-Phase Flows. https://www.math.ucdavis.edu/~egp/PUBLICATIONS/JOURNAL_ARTICLES/APPEARED/2000/MSS-EGP_2000.pdf; review_level=full-text
  Author-hosted pp.302–305, equations(1)–(6),(9),(12),(15): signed-distance geometry, enclosed-mass issue and volume-fraction conservation. Sign is reversed here to make phi negative inside. No CLSVOF or two-phase fluid experiment executed.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
