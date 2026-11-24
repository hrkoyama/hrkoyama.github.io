# Annular Couette control for curved-wall LBM

Refine the grid at identical physical conditions and compare interpolated/stair walls with analytic velocity,pointwise pressure and torque.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## Curved LBM annular Couette control: velocity,pressure andtorque

Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.

**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-algorithm)

Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.


**Problem figure**

![Curved LBM annular Couette control: velocity,pressure andtorque: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-validation)

Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.

- [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en) (`lbm-annular-couette-control`; Same-problem reference · Analytic reference)

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.
### Assumptions, units and boundaries

Rin.2/Rout.4,center(.5,.5),inner tangential speed.02,stationary outerwall,nu.01. N80/160/240,tau.7,T4,integer3840/15360/34560steps; both boundaries give sixruns. Initialize equilibrium moments of the analytic field.

**Editorial clarification**

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

### Adopted numerical method

Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.

$$
u_\theta=Ar+B/r,\quad A=-U_iR_i/(R_o^2-R_i^2),\quad B=U_iR_iR_o^2/(R_o^2-R_i^2)
$$

$$
p=\tfrac12A^2r^2+2AB\log r-\tfrac12B^2/r^2+C,\quad T_{inner}=-4\pi\rho\nu B
$$

### References and validation

Group28pytest;80annular gates. Sevenindependent radial/Cartesian qualifiers,finest velocity.03,fullpointwise pressure-gauge.08,torque relative.05,stationarity/refinement/stair comparison andwallinclusive budgets. Separate87component qualifiers passed; this doesnot imply main success. Separate29newmeshcomponentqualifierspassed.

### Limits

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

### Stored measurements and decisions

```json
{
  "metrics": {
    "finest_interpolated": {
      "variant": 0,
      "n": 240,
      "steps": 34560,
      "dx": 0.004166666666666667,
      "dt": 0.00011574074074074072,
      "time": 3.999999999999999,
      "tau": 0.7,
      "nu": 0.01,
      "velocity_error": 4.1181013570439095e-05,
      "pressure_error": 0.056576140457462176,
      "torque": -0.0006702247827550396,
      "exact_torque": -0.0006702064327658225,
      "torque_error": 2.7379607714759232e-05,
      "stationarity": 5.063686002269724e-08,
      "torque_drift": 4.646498909951803e-09,
      "mass_drift": 4.200271990063427e-07,
      "mass_ledger": 2.7512395413137817e-12,
      "momentum_ledger": 9.763298584209473e-13,
      "max_mach": 0.0009599923524199409,
      "min_rho": 0.9999997461691433,
      "max_rho": 1.0000004573310033,
      "min_population": 0.027712534590816466,
      "wall_mass_exchange": 0.00912977083678769,
      "open_mass_exchange": 0.0,
      "final_lattice_momentum_x": 4.615197113366776e-13,
      "final_lattice_momentum_y": 5.0622700475955185e-14
    },
    "finest_stair": {
      "variant": 1,
      "n": 240,
      "steps": 34560,
      "dx": 0.004166666666666667,
      "dt": 0.00011574074074074072,
      "time": 3.999999999999999,
      "tau": 0.7,
      "nu": 0.01,
      "velocity_error": 0.0056320234931158345,
      "pressure_error": 5.0386965555033765,
      "torque": -0.0006741976046875688,
      "exact_torque": -0.0006702064327658225,
      "torque_error": 0.005955138188207717,
      "stationarity": 2.173500599846503e-07,
      "torque_drift": 4.07061909864866e-07,
      "mass_drift": 2.7425432799505342e-12,
      "mass_ledger": 2.7517486245531947e-12,
      "momentum_ledger": 8.644174008350578e-13,
      "max_mach": 0.0009599923524199409,
      "min_rho": 0.9999925252188234,
      "max_rho": 1.000007128199855,
      "min_population": 0.027712460348227712,
      "wall_mass_exchange": -1.4606371667724716e-15,
      "open_mass_exchange": 0.0,
      "final_lattice_momentum_x": -3.0608848788915566e-13,
      "final_lattice_momentum_y": 5.230781086051906e-13
    },
    "reference_qualification": {
      "radial viscous equation": 5.551115123125783e-17,
      "radial pressure equation": 2.574980159653073e-19,
      "Cartesian divergence": 1.3877787807814457e-17,
      "Cartesian x momentum": 4.336808689942018e-19,
      "Cartesian y momentum": 2.168404344971009e-19,
      "inner wall speed": 0.0,
      "outer wall speed": 1.734723475976807e-18
    },
    "scope": "Stationary rotating-wall annulus only; does not substitute for actual cylinder flow."
  },
  "checks": {
    "analytic reference radial viscous equation": true,
    "analytic reference radial pressure equation": true,
    "analytic reference Cartesian divergence": true,
    "analytic reference Cartesian x momentum": true,
    "analytic reference Cartesian y momentum": true,
    "analytic reference inner wall speed": true,
    "analytic reference outer wall speed": true,
    "0-80 finite arrays": true,
    "0-80 positive density": true,
    "0-80 actual maximum Mach": true,
    "0-80 mass ledger": true,
    "0-80 wall-open momentum ledger": true,
    "0-80 all fixed integer steps": true,
    "0-80 declared physical endpoint": true,
    "0-80 total mass drift diagnostic bound": true,
    "0-80 late velocity stationarity": true,
    "0-80 late torque stationarity": true,
    "0-80 correct inner resisting torque sign": true,
    "0-160 finite arrays": true,
    "0-160 positive density": true,
    "0-160 actual maximum Mach": true,
    "0-160 mass ledger": true,
    "0-160 wall-open momentum ledger": true,
    "0-160 all fixed integer steps": true,
    "0-160 declared physical endpoint": true,
    "0-160 total mass drift diagnostic bound": true,
    "0-160 late velocity stationarity": true,
    "0-160 late torque stationarity": true,
    "0-160 correct inner resisting torque sign": true,
    "0-240 finite arrays": true,
    "0-240 positive density": true,
    "0-240 actual maximum Mach": true,
    "0-240 mass ledger": true,
    "0-240 wall-open momentum ledger": true,
    "0-240 all fixed integer steps": true,
    "0-240 declared physical endpoint": true,
    "0-240 total mass drift diagnostic bound": true,
    "0-240 late velocity stationarity": true,
    "0-240 late torque stationarity": true,
    "0-240 correct inner resisting torque sign": true,
    "1-80 finite arrays": true,
    "1-80 positive density": true,
    "1-80 actual maximum Mach": true,
    "1-80 mass ledger": true,
    "1-80 wall-open momentum ledger": true,
    "1-80 all fixed integer steps": true,
    "1-80 declared physical endpoint": true,
    "1-80 total mass drift diagnostic bound": true,
    "1-80 late velocity stationarity": true,
    "1-80 late torque stationarity": true,
    "1-80 correct inner resisting torque sign": true,
    "1-160 finite arrays": true,
    "1-160 positive density": true,
    "1-160 actual maximum Mach": true,
    "1-160 mass ledger": true,
    "1-160 wall-open momentum ledger": true,
    "1-160 all fixed integer steps": true,
    "1-160 declared physical endpoint": true,
    "1-160 total mass drift diagnostic bound": true,
    "1-160 late velocity stationarity": true,
    "1-160 late torque stationarity": true,
    "1-160 correct inner resisting torque sign": true,
    "1-240 finite arrays": true,
    "1-240 positive density": true,
    "1-240 actual maximum Mach": true,
    "1-240 mass ledger": true,
    "1-240 wall-open momentum ledger": true,
    "1-240 all fixed integer steps": true,
    "1-240 declared physical endpoint": true,
    "1-240 total mass drift diagnostic bound": true,
    "1-240 late velocity stationarity": true,
    "1-240 late torque stationarity": true,
    "1-240 correct inner resisting torque sign": true,
    "finest interpolated velocity": true,
    "finest interpolated pressure gauge": true,
    "finest interpolated torque": true,
    "interpolated velocity refinement": true,
    "interpolated pressure refinement": true,
    "interpolated improves finest stair velocity": true,
    "three grids with both boundary variants": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/index.json

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

### Sources and review scope

- Qisu Zou and Xiaoyi He (1996). On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model. https://arxiv.org/abs/comp-gas/9611001; review_level=primary-selected-extracted-text
Selected primary equations and flat-boundary/corner/compressibility discussion read; special d2q9i successes are not borrowed.

- Pierre Lallemand and Li-Shi Luo (2003). Lattice Boltzmann method for moving boundaries. https://doi.org/10.1016/S0021-9991(02)00022-0; review_level=primary-selected-text-via-mirror
Read selected original Eq12–15 on quadratic links,wall correction,momentum exchange andmassnonconservation; qualify by a generic-Lagrange scalar oracle. No2001fulltext orlocalPDFsymbol audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
