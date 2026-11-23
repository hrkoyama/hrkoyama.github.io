# Independent MHD transport, waves and compression comparisons

Evolve all8conserved components with HLLD/MUSCL/Heun and2D CT. Compare wave means or unmodified Athena++ loop/late-OT fields, separating independent reference spatial/time increments.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Circular Alfven wave: full-state refinement

Evolve all eight conserved variables and compare circular polarization, including nonzero Bz/vz, against analytic cell means.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.


**Problem figure**

![Circular Alfven wave: full-state refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en) (`circular-alfven`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/circular-alfven/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/?lang=en#circular-alfven-refinement-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

- [Circular Alfven wave: analytic full-state conserved cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-circular-alfven-refinement-en) (`circular-alfven-refinement`; Related-model reference · Analytic reference)

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.
### Assumptions, units and boundaries

gamma5/3, periodic[0,1], rho1,p.1,Bx1,amplitude.1, speed1,T1,32/64/128 cells. Initialize/reference conserved analytic cell means; pressure recovered from means differs from constant pointwise pressure.

**Editorial clarification**

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. The observed order is for a 1D aligned wave, not oblique 2D propagation.

### Adopted numerical method

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. One-dimensional finite-volume update with constant Bx.

$$
\partial_tU+\partial_xF_x(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B),\quad\gamma=5/3
$$

$$
\theta_i=2\pi(x_i-t),\quad(\bar B_y,\bar B_z)=.1\frac{\sin(\pi h)}{\pi h}(\cos\theta_i,\sin\theta_i)
$$

$$
\bar\rho=1,\quad\bar B_x=1,\quad(\bar m_y,\bar m_z)=-(\bar B_y,\bar B_z),\quad\bar E=.66
$$

$$
e_2=\frac{\|U-U^{\mathrm{exact}}\|_2}{\|U^{\mathrm{exact}}\|_2},\qquad p_{\mathrm{obs}}=\log_2(e_h/e_{h/2})
$$

### References and validation

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify conserved analytic means by independent Gauss16 quadrature; measure transverse errors, phase and observed order.

### Limits

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. The observed order is for a 1D aligned wave, not oblique 2D propagation.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": 3.3306690738754696e-16
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "independent analytic conserved quadrature": true,
    "circular-alfven-refinement-n32 all stages finite positive": true,
    "circular-alfven-refinement-n32 final time": true,
    "circular-alfven-refinement-n32 five exact snapshots": true,
    "circular-alfven-refinement-n32 fluid integral conservation": true,
    "circular-alfven-refinement-n32 native face divergence": true,
    "circular-alfven-refinement-n32 measured Courant sum": true,
    "circular-alfven-refinement-n32 no cell clips or retries": true,
    "circular-alfven-refinement-n32 explicit fallback accounting": true,
    "circular-alfven-refinement-n64 all stages finite positive": true,
    "circular-alfven-refinement-n64 final time": true,
    "circular-alfven-refinement-n64 five exact snapshots": true,
    "circular-alfven-refinement-n64 fluid integral conservation": true,
    "circular-alfven-refinement-n64 native face divergence": true,
    "circular-alfven-refinement-n64 measured Courant sum": true,
    "circular-alfven-refinement-n64 no cell clips or retries": true,
    "circular-alfven-refinement-n64 explicit fallback accounting": true,
    "circular-alfven-refinement-n128 all stages finite positive": true,
    "circular-alfven-refinement-n128 final time": true,
    "circular-alfven-refinement-n128 five exact snapshots": true,
    "circular-alfven-refinement-n128 fluid integral conservation": true,
    "circular-alfven-refinement-n128 native face divergence": true,
    "circular-alfven-refinement-n128 measured Courant sum": true,
    "circular-alfven-refinement-n128 no cell clips or retries": true,
    "circular-alfven-refinement-n128 explicit fallback accounting": true,
    "circular-alfven-refinement-half-dt all stages finite positive": true,
    "circular-alfven-refinement-half-dt final time": true,
    "circular-alfven-refinement-half-dt five exact snapshots": true,
    "circular-alfven-refinement-half-dt fluid integral conservation": true,
    "circular-alfven-refinement-half-dt native face divergence": true,
    "circular-alfven-refinement-half-dt measured Courant sum": true,
    "circular-alfven-refinement-half-dt no cell clips or retries": true,
    "circular-alfven-refinement-half-dt explicit fallback accounting": true,
    "transverse refinement n64": true,
    "transverse refinement n128": true,
    "transverse finest error": true,
    "transverse separate time contamination fraction": true,
    "selected wave last observed order": true,
    "selected wave phase error": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/circular-alfven-refinement/index.json

![Actual saved primary By(x,t) at five times: one spatial dimension plus time.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/circular-alfven-refinement-preview.png)

Actual saved primary By(x,t) at five times: one spatial dimension plus time.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
Verified the official pinned archive SHA and inspected both generators, configuration and saved columns. Executed the independent engine and checked spatial/time sensitivity. No complete code audit or exact-solution claim.

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
Inspected the author PDF CT section and loop/polarized-wave definitions. Original CTU/PPM and oblique-wave experiments are not replicated. Our wave is 1D aligned; the official loop generator explicitly has vz=2.

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
Bibliographic metadata checked; full publisher text unavailable. No new original-equation/experiment audit is claimed. Full-state HLLD is inherited byte-for-byte from the prior public validated Atlas.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Magnetic loop: independent 2D reference and refinement

Compare genuine 2D magnetic-loop transport with final conserved fields from independent Athena++, qualified in space and time.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.


**Problem figure**

![Magnetic loop: independent 2D reference and refinement: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Magnetic field-loop advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en) (`magnetic-loop`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/magnetic-loop/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/?lang=en#magnetic-loop-independent-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Magnetic loop: pinned independent Athena++ final-field reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-magnetic-loop-independent-en) (`magnetic-loop-independent`; Related-model reference · Finite-grid numerical reference)

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.
### Assumptions, units and boundaries

Periodic[-1,1]x[-.5,.5],rho=p1,Az=.001max(.3-r,0),T1,(Nx,Ny)=(16,8),(32,16),(64,32). Use unchanged official-generator v=(2,1,2), explicitly distinct from old vz0 inputs.

**Editorial clarification**

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

### Adopted numerical method

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
A_z=.001\max(.3-\sqrt{x^2+y^2},0),\qquad\mathbf v=(2,1,2)
$$

### References and validation

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

### Limits

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": null
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "magnetic-loop-independent-n8 all stages finite positive": true,
    "magnetic-loop-independent-n8 final time": true,
    "magnetic-loop-independent-n8 five exact snapshots": true,
    "magnetic-loop-independent-n8 fluid integral conservation": true,
    "magnetic-loop-independent-n8 native face divergence": true,
    "magnetic-loop-independent-n8 measured Courant sum": true,
    "magnetic-loop-independent-n8 no cell clips or retries": true,
    "magnetic-loop-independent-n8 explicit fallback accounting": true,
    "magnetic-loop-independent-n16 all stages finite positive": true,
    "magnetic-loop-independent-n16 final time": true,
    "magnetic-loop-independent-n16 five exact snapshots": true,
    "magnetic-loop-independent-n16 fluid integral conservation": true,
    "magnetic-loop-independent-n16 native face divergence": true,
    "magnetic-loop-independent-n16 measured Courant sum": true,
    "magnetic-loop-independent-n16 no cell clips or retries": true,
    "magnetic-loop-independent-n16 explicit fallback accounting": true,
    "magnetic-loop-independent-n32 all stages finite positive": true,
    "magnetic-loop-independent-n32 final time": true,
    "magnetic-loop-independent-n32 five exact snapshots": true,
    "magnetic-loop-independent-n32 fluid integral conservation": true,
    "magnetic-loop-independent-n32 native face divergence": true,
    "magnetic-loop-independent-n32 measured Courant sum": true,
    "magnetic-loop-independent-n32 no cell clips or retries": true,
    "magnetic-loop-independent-n32 explicit fallback accounting": true,
    "magnetic-loop-independent-half-dt all stages finite positive": true,
    "magnetic-loop-independent-half-dt final time": true,
    "magnetic-loop-independent-half-dt five exact snapshots": true,
    "magnetic-loop-independent-half-dt fluid integral conservation": true,
    "magnetic-loop-independent-half-dt native face divergence": true,
    "magnetic-loop-independent-half-dt measured Courant sum": true,
    "magnetic-loop-independent-half-dt no cell clips or retries": true,
    "magnetic-loop-independent-half-dt explicit fallback accounting": true,
    "magnetic refinement n16": true,
    "magnetic refinement n32": true,
    "magnetic finest error": true,
    "magnetic separate time contamination fraction": true,
    "magnetic reference increment/error": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/magnetic-loop-independent/index.json

![Actual saved primary 2D in-plane magnetic energy at T1.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/magnetic-loop-independent-preview.png)

Actual saved primary 2D in-plane magnetic energy at T1.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
Verified the official pinned archive SHA and inspected both generators, configuration and saved columns. Executed the independent engine and checked spatial/time sensitivity. No complete code audit or exact-solution claim.

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
Inspected the author PDF CT section and loop/polarized-wave definitions. Original CTU/PPM and oblique-wave experiments are not replicated. Our wave is 1D aligned; the official loop generator explicitly has vz=2.

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
Bibliographic metadata checked; full publisher text unavailable. No new original-equation/experiment audit is claimed. Full-state HLLD is inherited byte-for-byte from the prior public validated Atlas.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Late Orszag-Tang: independent reference and compression structure

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

**Methods used**

- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) (`hlld`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) (`ct`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-algorithm)

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

- [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en) (`mhd`)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.


**Problem figure**

![Late Orszag-Tang: independent reference and compression structure: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Orszag–Tang vortex (CT/GLM/error variants merged)](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en) (`orszag-tang`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-validation)

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-postshock-orszag-tang-en) (`postshock-orszag-tang`; Related-model reference · Finite-grid numerical reference)

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.
### Assumptions, units and boundaries

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

**Editorial clarification**

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

### Adopted numerical method

Full-eight-state HLLD fluxes, MC-MUSCL reconstruction and fixed-step Heun. Shared face fluxes and CT-contact corner EMFs update native face B; cell B is adjacent-face averaged. Initial discrete vector-potential curl and sampled fluid states match the official generator.

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

### References and validation

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

### Limits

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

### Stored measurements and decisions

```json
{
  "metrics": {
    "completed_pde_runs": 4,
    "reference_qualification_passed": true,
    "analytic_quadrature_difference": null
  },
  "checks": {
    "four prescribed fixed runs": true,
    "qualified independent reference": true,
    "postshock-orszag-tang-n16 all stages finite positive": true,
    "postshock-orszag-tang-n16 final time": true,
    "postshock-orszag-tang-n16 five exact snapshots": true,
    "postshock-orszag-tang-n16 fluid integral conservation": true,
    "postshock-orszag-tang-n16 native face divergence": true,
    "postshock-orszag-tang-n16 measured Courant sum": true,
    "postshock-orszag-tang-n16 no cell clips or retries": true,
    "postshock-orszag-tang-n16 explicit fallback accounting": true,
    "postshock-orszag-tang-n32 all stages finite positive": true,
    "postshock-orszag-tang-n32 final time": true,
    "postshock-orszag-tang-n32 five exact snapshots": true,
    "postshock-orszag-tang-n32 fluid integral conservation": true,
    "postshock-orszag-tang-n32 native face divergence": true,
    "postshock-orszag-tang-n32 measured Courant sum": true,
    "postshock-orszag-tang-n32 no cell clips or retries": true,
    "postshock-orszag-tang-n32 explicit fallback accounting": true,
    "postshock-orszag-tang-n64 all stages finite positive": true,
    "postshock-orszag-tang-n64 final time": true,
    "postshock-orszag-tang-n64 five exact snapshots": true,
    "postshock-orszag-tang-n64 fluid integral conservation": true,
    "postshock-orszag-tang-n64 native face divergence": true,
    "postshock-orszag-tang-n64 measured Courant sum": true,
    "postshock-orszag-tang-n64 no cell clips or retries": true,
    "postshock-orszag-tang-n64 explicit fallback accounting": true,
    "postshock-orszag-tang-half-dt all stages finite positive": true,
    "postshock-orszag-tang-half-dt final time": true,
    "postshock-orszag-tang-half-dt five exact snapshots": true,
    "postshock-orszag-tang-half-dt fluid integral conservation": true,
    "postshock-orszag-tang-half-dt native face divergence": true,
    "postshock-orszag-tang-half-dt measured Courant sum": true,
    "postshock-orszag-tang-half-dt no cell clips or retries": true,
    "postshock-orszag-tang-half-dt explicit fallback accounting": true,
    "density refinement n32": true,
    "density refinement n64": true,
    "density finest error": true,
    "density separate time contamination fraction": true,
    "density reference increment/error": true,
    "pressure refinement n32": true,
    "pressure refinement n64": true,
    "pressure finest error": true,
    "pressure separate time contamination fraction": true,
    "pressure reference increment/error": true,
    "late density compression diagnostic": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/index.json

![Actual saved primary 2D density field at T.2.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/postshock-orszag-tang-preview.png)

Actual saved primary 2D density field at T.2.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Athena++ collaboration (2026). Athena++ official field_loop and orszag_tang problem generators, pinned source. https://github.com/PrincetonUniversity/athena/tree/1395e2f543f4368d448cb1a2cf92ba1f910e3416; review_level=Official archive SHA verified; selected src/pgen/field_loop.cpp and orszag_tang.cpp, PLM/RK2/output configuration and actual conserved tab headers inspected; not a full Athena code audit
Verified the official pinned archive SHA and inspected both generators, configuration and saved columns. Executed the independent engine and checked spatial/time sensitivity. No complete code audit or exact-solution claim.

- Thomas A. Gardiner and James M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=Author arXiv PDF selected section2.2 equations13–20,3.3.1–3.3.2 and5.1–5.2 inspected; not the full paper or original experiment replication
Inspected the author PDF CT section and loop/polarized-wave definitions. Original CTU/PPM and oblique-wave experiments are not replicated. Our wave is 1D aligned; the official loop generator explicitly has vz=2.

- Takahiro Miyoshi and Kanya Kusano (2005). A multi-state HLL approximate Riemann solver for ideal magnetohydrodynamics. https://doi.org/10.1016/j.jcp.2005.02.017; review_level=Bibliographic metadata checked; publisher full text returned403. This addition did not newly audit original equations or experiments
Bibliographic metadata checked; full publisher text unavailable. No new original-equation/experiment audit is claimed. Full-state HLLD is inherited byte-for-byte from the prior public validated Atlas.

- Steven A. Orszag and Ching-Mao Tang (1979). Small-scale structure of two-dimensional magnetohydrodynamic turbulence. https://doi.org/10.1017/S002211207900210X; review_level=Original publisher abstract/bibliography inspected only; original incompressible viscous/resistive setup differs from the official compressible ideal-MHD generator used here
Inspected publisher abstract and bibliography only. Distinguish the original incompressible viscous/resistive study from the official compressible ideal-MHD setup used here.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
