# Nonuniform ALE transport and2D rotating shallow-water waves

Time-advance conservative ALE transport on genuinely nonuniform moving cells with GCL, and2D linear rotating C-grid shallow-water waves. Saltzman pistons and global Williamson problems remain future work.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## ALE scalar transport on genuinely nonuniform moving cells

Advance cell integrals and face positions with identical Heun stages, transporting a nonuniform analytic wave beyond a uniform GCL check.

**Methods used**

- [ALE uniform-state / geometric-conservation model](https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=en) (`ale`)
- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-algorithm)

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

- [ALE scalar conservation on moving cells](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#ale-scalar-transport-en) (`ale-scalar-transport`)

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.


**Problem figure**

![ALE scalar transport on genuinely nonuniform moving cells: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[ALE scalar transport on genuinely nonuniform moving cells](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en) (`ale-nonuniform-transport`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/ale-nonuniform-transport/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/?lang=en#ale-nonuniform-transport-en-validation)

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

- [ALE: analytic moving-cell integrals and separate time reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ale-nonuniform-transport-en) (`ale-nonuniform-transport`; Same-problem reference · Analytic reference)

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
### Assumptions, units and boundaries

Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps.

**Editorial clarification**

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

### Adopted numerical method

Upwind relative flux(a-w)q advances actual masses with identical predictor/corrector face geometry; record stage volumes and Courant numbers.

$$
\dot m_i=-[(a-w)q]_{i+1/2}+[(a-w)q]_{i-1/2},\quad V_i=x_{i+1/2}-x_{i-1/2}
$$

$$
x(\xi,t)=\xi+0.2\sin(2\pi\xi)\sin(2\pi t)/(2\pi)
$$

### References and validation

Separate analytic moving-cell-integral error, global/stage mass, constant GCL and geometry error. Qualify an independent DOP853 integration of the same FV ODE with two tolerances.

### Limits

First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 40,
    "steps": 128,
    "time": 0.25,
    "error": 0.01079017856620466,
    "minimum_volume": 0.02002059881546564,
    "minimum_value": 0.8008335429751757,
    "maximum_cfl": 0.07049500497645084,
    "mass_defect": 0.0,
    "step_mass_defect": 2.220446049250313e-16,
    "gcl_defect": 1.9786689647860456e-16,
    "geometry_error": 3.9947516627947266e-07,
    "temporal_error": 2.0565741803957238e-07
  },
  "checks": {
    "adaptive-time reference qualification": true,
    "space-n40 mass_defect": true,
    "space-n40 step_mass_defect": true,
    "space-n40 gcl_defect": true,
    "space-n40 maximum_cfl": true,
    "space-n40 positive volumes and values": true,
    "space-n40 five saved times": true,
    "space-n80 mass_defect": true,
    "space-n80 step_mass_defect": true,
    "space-n80 gcl_defect": true,
    "space-n80 maximum_cfl": true,
    "space-n80 positive volumes and values": true,
    "space-n80 five saved times": true,
    "space-n160 mass_defect": true,
    "space-n160 step_mass_defect": true,
    "space-n160 gcl_defect": true,
    "space-n160 maximum_cfl": true,
    "space-n160 positive volumes and values": true,
    "space-n160 five saved times": true,
    "gcl-n40 mass_defect": true,
    "gcl-n40 step_mass_defect": true,
    "gcl-n40 gcl_defect": true,
    "gcl-n40 maximum_cfl": true,
    "gcl-n40 positive volumes and values": true,
    "gcl-n40 five saved times": true,
    "time-n40-s32 mass_defect": true,
    "time-n40-s32 step_mass_defect": true,
    "time-n40-s32 gcl_defect": true,
    "time-n40-s32 maximum_cfl": true,
    "time-n40-s32 positive volumes and values": true,
    "time-n40-s32 five saved times": true,
    "time-n40-s64 mass_defect": true,
    "time-n40-s64 step_mass_defect": true,
    "time-n40-s64 gcl_defect": true,
    "time-n40-s64 maximum_cfl": true,
    "time-n40-s64 positive volumes and values": true,
    "time-n40-s64 five saved times": true,
    "time-n40-s128 mass_defect": true,
    "time-n40-s128 step_mass_defect": true,
    "time-n40-s128 gcl_defect": true,
    "time-n40-s128 maximum_cfl": true,
    "time-n40-s128 positive volumes and values": true,
    "time-n40-s128 five saved times": true,
    "space refinement 1": true,
    "space refinement 2": true,
    "time refinement 1": true,
    "time refinement 2": true,
    "finest transport error": true,
    "constant-state GCL preservation": true,
    "finest time error": true,
    "reference analytic moving-face velocity": true,
    "reference periodic analytic mass": true,
    "reference skew-Hermitian discrete symbol": true,
    "reference continuous wave frequency": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ale-nonuniform-transport/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/ale-nonuniform-transport-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- Dennis L. Huff (1987). Numerical Simulations of Unsteady, Viscous, Transonic Flow Over Isolated and Cascaded Airfoils Using a Deforming Grid. https://ntrs.nasa.gov/api/citations/19870015002/downloads/19870015002.pdf; review_level=selected-primary-report-grid-treatment

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Actual2D C-grid rotating shallow-water time advance

Time-advance actual2D staggered fields and distinguish continuous-wave references from semidiscrete symbols.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-algorithm)

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

- [Linear rotating shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-rotating-shallow-water-en) (`linear-rotating-shallow-water`)

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.


**Problem figure**

![Actual2D C-grid rotating shallow-water time advance: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Actual2D C-grid rotating shallow-water time advance](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en) (`cgrid-rotating-wave`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/cgrid-rotating-wave/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/?lang=en#cgrid-rotating-wave-en-validation)

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

- [C-grid: continuous Fourier solution and discrete-symbol exponential](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-cgrid-rotating-wave-en) (`cgrid-rotating-wave`; Same-problem reference · Analytic reference)

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.
### Assumptions, units and boundaries

Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes.

**Editorial clarification**

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

### Adopted numerical method

Actual2D cell-height/face-velocity differences and four-point Coriolis interpolation use RK4. The3×3 matrix exponential is reference-only, never the PDE update.

$$
\eta_t+u_x+v_y=0,\quad u_t=v-\eta_x,\quad v_t=-u-\eta_y
$$

$$
\tilde k=2\sin(kh/2)/h,\quad C=\cos(kh/2)\cos(lh/2),\quad U_h(t)=e^{tL_h}U_h(0)
$$

### References and validation

Retain continuous-PDE spatial and discrete-symbol temporal errors, mass/energy, stencil-symbol identity, zero-mode inertia and discrete steady balance.

### Limits

Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

### Stored measurements and decisions

```json
{
  "metrics": {
    "n": 16,
    "steps": 64,
    "time": 0.5,
    "semidiscrete_error": 6.989513057798398e-16,
    "continuous_error": 0.0069533426306616995,
    "mean_height_change": 1.2705494208814505e-20,
    "relative_energy_change": 2.220446049250313e-16,
    "energy_rhs_defect": 2.1352767681718556e-19,
    "steady_change": 1.8041124150158794e-16
  },
  "checks": {
    "space-n16-s64 mean_height_change": true,
    "space-n16-s64 relative_energy_change": true,
    "space-n16-s64 energy_rhs_defect": true,
    "space-n16-s64 finite actual 2D RK arrays": true,
    "space-n32-s128 mean_height_change": true,
    "space-n32-s128 relative_energy_change": true,
    "space-n32-s128 energy_rhs_defect": true,
    "space-n32-s128 finite actual 2D RK arrays": true,
    "space-n64-s256 mean_height_change": true,
    "space-n64-s256 relative_energy_change": true,
    "space-n64-s256 energy_rhs_defect": true,
    "space-n64-s256 finite actual 2D RK arrays": true,
    "time-n16-s16 mean_height_change": true,
    "time-n16-s16 relative_energy_change": true,
    "time-n16-s16 energy_rhs_defect": true,
    "time-n16-s16 finite actual 2D RK arrays": true,
    "time-n16-s32 mean_height_change": true,
    "time-n16-s32 relative_energy_change": true,
    "time-n16-s32 energy_rhs_defect": true,
    "time-n16-s32 finite actual 2D RK arrays": true,
    "time-n16-s64 mean_height_change": true,
    "time-n16-s64 relative_energy_change": true,
    "time-n16-s64 energy_rhs_defect": true,
    "time-n16-s64 finite actual 2D RK arrays": true,
    "zero-n8-s64 mean_height_change": true,
    "zero-n8-s64 relative_energy_change": true,
    "zero-n8-s64 energy_rhs_defect": true,
    "zero-n8-s64 finite actual 2D RK arrays": true,
    "balance-n16-s64 mean_height_change": true,
    "balance-n16-s64 relative_energy_change": true,
    "balance-n16-s64 energy_rhs_defect": true,
    "balance-n16-s64 finite actual 2D RK arrays": true,
    "continuous spatial refinement 1": true,
    "continuous spatial refinement 2": true,
    "semidiscrete temporal refinement 1": true,
    "semidiscrete temporal refinement 2": true,
    "finest continuous error": true,
    "finest semidiscrete error": true,
    "zero-mode temporal accuracy": true,
    "discrete geostrophic stationarity": true,
    "reference analytic moving-face velocity": true,
    "reference periodic analytic mass": true,
    "reference skew-Hermitian discrete symbol": true,
    "reference continuous wave frequency": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/cgrid-rotating-wave/index.json

![Validation preview from actual saved PDE arrays and fixed-input refinement measurements.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/cgrid-rotating-wave-preview.png)

Validation preview from actual saved PDE arrays and fixed-input refinement measurements.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/atlas-moving-waves-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/moving-waves/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

### Sources and review scope

- P. Korn and S. Danilov (n.d.). Elementary dispersion analysis of some mimetic discretizations on triangular C-grids. https://epic.awi.de/id/eprint/42760/1/c-grid_jcp_v5-1.pdf; review_level=selected-primary-author-manuscript

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
