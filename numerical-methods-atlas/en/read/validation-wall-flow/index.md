# Nonperiodic walls: cavity and manufactured flow

Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Re100 lid-driven cavity: Ghia centerline comparison

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-algorithm)

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.


**Problem figure**

![Re100 lid-driven cavity: Ghia centerline comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-validation)

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference · Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference · Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
### Assumptions, units and boundaries

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.

**Editorial clarification**

Educational Re=100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed. Scientific-source revision3, immutable edition2026-11-23-r2, passed22 unit checks and all94 group gates. After the initial NumPy-boolean JSON-serialization failure, the next unpublished candidate lacked completion status and case-ID top-level checks required by the common verifier. This edition only repairs the JSON envelope with termination,failure and case-keyed checks, retaining the prior three diagnostics under summary_checks, and adds one regression. Inputs,acceptance,numerical solver,references and the prior21 tests are unchanged. All six saved NPZ field arrays are bit-identical to the previous candidate. The original unpublished packet is archived outside the public tree, and earlier failure history is retained. Finest Ghia centerline maximum errors are about.00277820 foru and.00590408 forv; the grid primary vortex is(.609375,.734375), with true steady residual about9.68e-10. Pressure is eliminated in streamfunction evolution; cavity pressure is not validated.

### Adopted numerical method

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

### References and validation

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

### Limits

Educational Re=100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_u_ghia_maximum": 0.0027781960789884375,
    "finest_v_ghia_maximum": 0.005904081227178365,
    "finest_vortex_center": [
      0.609375,
      0.734375
    ],
    "finest_steady_residual": 9.684821000721655e-10
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "finest u primary-table maximum error": true,
    "finest v primary-table maximum error": true,
    "Ghia centerline refinement 1": true,
    "Ghia centerline refinement 2": true,
    "finest primary-vortex grid location": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/index.json

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

### Sources and review scope

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
Visually inspected original equations/boundary figure, Re100 columns in TablesI/II and primary vortex in TableV. The public mirror delivers the original paper; its PDF is not redistributed. This independently written solver differs from CSI-MG.

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Read official Sandia/OSTI metadata/abstract and original report printed12 on MMS together with mesh refinement. The polynomial and pressure field are constructed for this example.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Nonperiodic wall MMS: velocity, shear and pressure operator

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-algorithm)

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en) (`forced-incompressible`)

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.


**Problem figure**

![Nonperiodic wall MMS: velocity, shear and pressure operator: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-validation)

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

- [Wall manufactured solution: polynomial velocity and separate pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en) (`wall-mms`; Same-problem reference · Manufactured solution)

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.
### Assumptions, units and boundaries

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.

**Editorial clarification**

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver. Scientific-source revision3, immutable edition2026-11-23-r2, passed22 unit checks and all94 group gates. After the initial NumPy-boolean JSON-serialization failure, the next unpublished candidate lacked completion status and case-ID top-level checks required by the common verifier. This edition only repairs the JSON envelope with termination,failure and case-keyed checks, retaining the prior three diagnostics under summary_checks, and adds one regression. Inputs,acceptance,numerical solver,references and the prior21 tests are unchanged. All six saved NPZ field arrays are bit-identical to the previous candidate. The original unpublished packet is archived outside the public tree, and earlier failure history is retained. Finest velocityL2 is about2.638e-5, with last-pair velocity/streamfunction orders about2.009/2.022. Actual wall-shear order is about1.982, while local Thom truncation on exactpsi is about.989; this does not guarantee a universally second-order wall formula. The separate pressure-operatorp/full-gradient/boundary-gradient orders are about1.978/2.318/1.998, distinct from cavity pressure.

### Adopted numerical method

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

### References and validation

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

### Limits

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_velocity_l2": 2.637991527485713e-05,
    "finest_streamfunction_l2": 3.0579766556845255e-05,
    "observed_orders": {
      "psi_l2": [
        2.0426330065243574,
        2.021783836772359
      ],
      "velocity_l2": [
        1.9917746694984177,
        2.0086644375747413
      ],
      "wall_omega_maximum": [
        1.937772137605888,
        1.9794771588130946
      ],
      "wall_shear_maximum": [
        1.9412705074950394,
        1.9820164294643936
      ],
      "thom_exact_psi_wall_truncation": [
        0.9769163868869587,
        0.9885952367277506
      ],
      "pressure_l2": [
        1.9590185209239261,
        1.9784952274339704
      ],
      "pressure_gradient_l2": [
        2.3544980286788206,
        2.3175253385985015
      ],
      "pressure_boundary_gradient_l2": [
        1.9914961869556822,
        1.9978781190385215
      ]
    },
    "reference_qualification": {
      "checks": {
        "independent tensor-polynomial fields": true,
        "independent tensor-polynomial forcing": true,
        "analytic four-wall no slip": true,
        "analytic incompressibility": true,
        "two primary-table columns each 17 points": true
      },
      "field_maximum": 1.27675647831893e-15,
      "forcing_maximum": 4.038436252074007e-15,
      "exact_wall_speed": 1.27675647831893e-15,
      "passed": true
    },
    "pressure_scope": "Separate manufactured Dirichlet operator; cavity pressure not computed."
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "psi_l2 refinement 1": true,
    "velocity_l2 refinement 1": true,
    "wall_omega_maximum refinement 1": true,
    "wall_shear_maximum refinement 1": true,
    "psi_l2 refinement 2": true,
    "velocity_l2 refinement 2": true,
    "wall_omega_maximum refinement 2": true,
    "wall_shear_maximum refinement 2": true,
    "finest streamfunction order": true,
    "finest velocity order": true,
    "finest streamfunction accuracy": true,
    "finest velocity accuracy": true,
    "n17: separate pressure Dirichlet boundary": true,
    "n17: separate pressure Poisson residual": true,
    "n17: finite separate pressure solution": true,
    "n33: separate pressure Dirichlet boundary": true,
    "n33: separate pressure Poisson residual": true,
    "n33: finite separate pressure solution": true,
    "n65: separate pressure Dirichlet boundary": true,
    "n65: separate pressure Poisson residual": true,
    "n65: finite separate pressure solution": true,
    "finest separate pressure_l2 order": true,
    "finest separate pressure_gradient_l2 order": true,
    "finest separate pressure_boundary_gradient_l2 order": true,
    "independent tensor-polynomial fields": true,
    "independent tensor-polynomial forcing": true,
    "analytic four-wall no slip": true,
    "analytic incompressibility": true,
    "two primary-table columns each 17 points": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/index.json

![Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

### Sources and review scope

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
Visually inspected original equations/boundary figure, Re100 columns in TablesI/II and primary vortex in TableV. The public mirror delivers the original paper; its PDF is not redistributed. This independently written solver differs from CSI-MG.

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Read official Sandia/OSTI metadata/abstract and original report printed12 on MMS together with mesh refinement. The polynomial and pressure field are constructed for this example.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
