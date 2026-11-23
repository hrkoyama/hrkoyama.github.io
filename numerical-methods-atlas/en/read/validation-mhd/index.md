# Independent fluid/MHD comparisons and CT/GLM

Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Orszag–Tang: CT, GLM and independent Athena++

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

**Methods used**

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-algorithm)

Reuse the published first-order Rusanov/forward-Euler solvers: shared corner-EMF discrete curl for CT and cell-centered hyperbolic/parabolic GLM cleaning. Independent Athena++ uses HLLD, PLM and RK2.

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Orszag–Tang: CT, GLM and independent Athena++: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en#ct-glm-independent-en-validation)

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
### Assumptions, units and boundaries

Unit square, gamma=5/3, mu0=1, vz=Bz=0, t=0.05. rho=25/(36pi), p=5/(12pi), v=(-sin2piy,sin2pix), B=(-sin2piy,sin4pix)/sqrt(4pi).

**Editorial clarification**

The adopted GLM uses ch=3 and damping rate kappa=0.18 ch n, with n cells per axis: damping is grid dependent. Both use the same continuous initial field, final time and CFL, while actual step counts and native div B operators differ.

### Adopted numerical method

Reuse the published first-order Rusanov/forward-Euler solvers: shared corner-EMF discrete curl for CT and cell-centered hyperbolic/parabolic GLM cleaning. Independent Athena++ uses HLLD, PLM and RK2.

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

### References and validation

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

### Limits

Face CT divergence and centered GLM divergence use different operators; common cell-centered diagnostics are also reported. Athena initializes face-averaged magnetic fields by differencing a vector potential, so comparison includes discretization differences of identical continuous data. This is a short planar test, not validation of shocks, 3D, UCT or CTU.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_density_128_256_l1": 4.631344236627223e-05,
    "ct_glm_finest_density_l1": 0.0016910992352830488
  },
  "checks": {
    "independent_reference_refined": true,
    "ct_native_constraint_16": true,
    "ct_native_constraint_32": true,
    "ct_native_constraint_64": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_refinement": true,
    "conservation": true,
    "positive_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Brio–Wu against an independent HLLD implementation

Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-algorithm)

Atlas uses MC reconstruction and SSPRK2; the independent C++ reference uses HLLD, PLM and RK3. Implementations differ while sharing the HLLD flux family.

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Brio–Wu against an independent HLLD implementation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Brio–Wu shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en) (`brio-wu`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=en#brio-independent-en-validation)

Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

1D, [0,1], t=0.1, gamma=2, Bx=0.75; left/right (rho,p,By)=(1,1,1)/(0.125,0.1,-1), zero velocity, outflow boundaries.

### Adopted numerical method

Atlas uses MC reconstruction and SSPRK2; the independent C++ reference uses HLLD, PLM and RK3. Implementations differ while sharing the HLLD flux family.

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

### References and validation

Compare 128/256/512 cells with conservative averages of independently rerun 2048/4096-cell references. Check density/By L1 errors, refinement and positive density/pressure.

### Limits

This compares numerical solutions including the Brio–Wu compound wave; it is not a claim of a unique exact solution for arbitrary MHD Riemann problems. Reference regeneration requires C++ compilation; routine Python runs use the stored reference.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.00048642415115017165,
    "reference_finest_n": 4096,
    "finest_density_l1": 0.0018299450752667257
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true,
    "magnetic_error": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- M. Brio and C. C. Wu (1988). An upwind differencing scheme for the equations of ideal magnetohydrodynamics. https://doi.org/10.1016/0021-9991(88)90120-9; review_level=bibliographic identity and official Athena test definition

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Shu–Osher: independent reference and mesh refinement

Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code.

**Methods used**

- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-algorithm)

Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Shu–Osher: independent reference and mesh refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=en#shu-independent-en-validation)

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

gamma=1.4, [-5,5], t=1.8. For x<-4, (rho,u,p)=(3.857143,2.629369,10.33333); to the right rho=1+0.2sin5x,u=0,p=1.

### Adopted numerical method

Atlas uses MC-MUSCL/HLLC/SSPRK3; Athena++ uses PLM/HLLC/RK3. A saved problem-generator patch matches only shock location and sinusoid wavenumber; the independent solver is unchanged.

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

### References and validation

Measure density L1 error, refinement and positivity on 100/200/400 cells; also compare 2048/4096/8192 reference differences with a predeclared bound. The shock has not reached the boundaries at the fixed comparison time.

### Limits

The reference is an independent finite-grid numerical solution, not an exact solution. No universal flux ranking, WENO-order claim or positivity guarantee is inferred. The 2048-to-4096 reference L1 increment0.005346 missed the predeclared0.005 bound, so8192 cells were added. The earlier miss remains recorded.

### Stored measurements and decisions

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.003374178434921656,
    "reference_finest_n": 8192,
    "finest_density_l1": 0.05377749991959067
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- C.-W. Shu and S. Osher (1989). Efficient implementation of essentially non-oscillatory shock-capturing schemes, II. https://doi.org/10.1016/0021-9991(89)90222-2; review_level=bibliographic identity and official Athena problem generator

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## GLM longitudinal mode: analytic damping

Compare a longitudinal magnetic Fourier mode of GLM cleaning with the continuous linear matrix-exponential solution.

**Methods used**

- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) (`glm`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-algorithm)

Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![GLM longitudinal mode: analytic damping: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=en#glm-fourier-mode-en-validation)

Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
### Assumptions, units and boundaries

Periodic [0,1], Bx=cos2pix, psi=0, ch=1, damping kappa=2, t=1. This linear diagnostic omits fluid coupling.

### Adopted numerical method

Integrate Bx_t=-psi_x and psi_t=-ch² Bx_x-kappa psi with centered differences/RK4. The independent reference exponentiates the continuous 2x2 Fourier symbol.

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

### References and validation

Check L2 error, second-order spatial refinement and damping of the divergence-mode amplitude at 16/32/64 points.

### Limits

Linear-mode damping does not guarantee divergence control or global accuracy for every nonlinear MHD problem. A monopole mode that CT cannot represent is not used as a matched CT comparison.

### Stored measurements and decisions

```json
{
  "metrics": {
    "observed_order": 2.001546730427675,
    "continuum_amplitude_ratio": 0.3619556718500278
  },
  "checks": {
    "analytic_expm_comparison": true,
    "spatial_order": true,
    "divergence_damping": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/index.json

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
