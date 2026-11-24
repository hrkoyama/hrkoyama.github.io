# LBM Taylor–Green vortex and finite-Mach errors

Use the exact periodic vortex to examine coupled grid/time/Mach errors and amplitude effects.

These additional validation supplements are managed separately from the common 22-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.

## LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity

Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.

**Methods used**

- [D2Q9–BGK collision and streaming](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en) (`d2q9-bgk`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-algorithm)

Standard BGK and fully periodic streaming. Convert/gauge pressure ascs²(rho−meanrho)(dx/dt)². No analytic field injection after initialization; independently qualify the continuum field by Fourier differentiation.

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.


**Problem figure**

![LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-validation)

22pytest and79gates,sixfixed evolutions. Require finest velocity relativeL2.03,pressure.08,combined velocity order≥1.5,energy.03anddivergence/periodic mass/mean momentum. Save five analyticPDEqualifiers distinctly. Retain the initial N16energy failure5.0018%; refine only thatcoarsegrid to24against the unchanged3%gate. Report order only for thefinest32/64pair.

- [Viscous flow / 2D Taylor–Green](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en) (`taylor-green`; Related-model reference · Analytic reference)

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en) (`lbm-taylor-green`; Related-model reference · Analytic reference)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.
### Assumptions, units and boundaries

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

**Editorial clarification**

Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors.

### Adopted numerical method

Standard BGK and fully periodic streaming. Convert/gauge pressure ascs²(rho−meanrho)(dx/dt)². No analytic field injection after initialization; independently qualify the continuum field by Fourier differentiation.

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

### References and validation

22pytest and79gates,sixfixed evolutions. Require finest velocity relativeL2.03,pressure.08,combined velocity order≥1.5,energy.03anddivergence/periodic mass/mean momentum. Save five analyticPDEqualifiers distinctly. Retain the initial N16energy failure5.0018%; refine only thatcoarsegrid to24against the unchanged3%gate. Report order only for thefinest32/64pair.

### Limits

Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors.

### Stored measurements and decisions

```json
{
  "metrics": {
    "combined_velocity_order": 1.9997408571265982,
    "reference_qualification": {
      "Fourier divergence": 4.718447854656915e-16,
      "Fourier NS x": 3.0878077872387166e-16,
      "Fourier NS y": 3.434752482434078e-16,
      "mean pressure gauge": 6.505213034913027e-19,
      "analytic mean energy": 1.734723475976807e-18
    },
    "scope": "Diffusive grid/time/Mach refinement, amplitude/Re sensitivity, and coupled dt/Mach/tau probe; no pure time or pure Mach order."
  },
  "checks": {
    "analytic reference Fourier divergence": true,
    "analytic reference Fourier NS x": true,
    "analytic reference Fourier NS y": true,
    "analytic reference mean pressure gauge": true,
    "analytic reference analytic mean energy": true,
    "0 finite arrays": true,
    "0 positive density": true,
    "0 actual maximum Mach": true,
    "0 mass ledger": true,
    "0 wall-open momentum ledger": true,
    "0 all fixed integer steps": true,
    "0 declared physical endpoint": true,
    "0 periodic mass": true,
    "0 zero mean momentum": true,
    "0 normalized divergence": true,
    "0 mean kinetic energy": true,
    "1 finite arrays": true,
    "1 positive density": true,
    "1 actual maximum Mach": true,
    "1 mass ledger": true,
    "1 wall-open momentum ledger": true,
    "1 all fixed integer steps": true,
    "1 declared physical endpoint": true,
    "1 periodic mass": true,
    "1 zero mean momentum": true,
    "1 normalized divergence": true,
    "1 mean kinetic energy": true,
    "2 finite arrays": true,
    "2 positive density": true,
    "2 actual maximum Mach": true,
    "2 mass ledger": true,
    "2 wall-open momentum ledger": true,
    "2 all fixed integer steps": true,
    "2 declared physical endpoint": true,
    "2 periodic mass": true,
    "2 zero mean momentum": true,
    "2 normalized divergence": true,
    "2 mean kinetic energy": true,
    "3 finite arrays": true,
    "3 positive density": true,
    "3 actual maximum Mach": true,
    "3 mass ledger": true,
    "3 wall-open momentum ledger": true,
    "3 all fixed integer steps": true,
    "3 declared physical endpoint": true,
    "3 periodic mass": true,
    "3 zero mean momentum": true,
    "3 normalized divergence": true,
    "3 mean kinetic energy": true,
    "4 finite arrays": true,
    "4 positive density": true,
    "4 actual maximum Mach": true,
    "4 mass ledger": true,
    "4 wall-open momentum ledger": true,
    "4 all fixed integer steps": true,
    "4 declared physical endpoint": true,
    "4 periodic mass": true,
    "4 zero mean momentum": true,
    "4 normalized divergence": true,
    "4 mean kinetic energy": true,
    "5 finite arrays": true,
    "5 positive density": true,
    "5 actual maximum Mach": true,
    "5 mass ledger": true,
    "5 wall-open momentum ledger": true,
    "5 all fixed integer steps": true,
    "5 declared physical endpoint": true,
    "5 periodic mass": true,
    "5 zero mean momentum": true,
    "5 normalized divergence": true,
    "5 mean kinetic energy": true,
    "finest combined velocity error": true,
    "finest pressure gauge error": true,
    "combined finest velocity order": true,
    "first diffusive refinement decreases velocity": true,
    "second diffusive refinement decreases velocity": true,
    "same physical endpoint all six runs": true,
    "amplitude probes change actual Mach": true,
    "exactly six distinct prescribed runs": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/index.json

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green-preview.png)

Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.

### Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json

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
Selected primary section via author-content mirror. The implemented two-point interpolation is separately derived/qualified; no2001full-text claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
