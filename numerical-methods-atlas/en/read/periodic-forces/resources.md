# From DFT to atomic forces: finite differences, independent references, force convergence and the BOMD interface

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-forces/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Pseudopotentials and PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Periodic electronic structure and k-point sampling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)
- [Pseudopotentials and PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en>)
- [Periodic electronic structure and k-point sampling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en>)

## Equations

- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local KS equations. Runnable code covers spherical-helium spin-unpolarized Dirac exchange-only LDA. Correlation, GGA, hybrids, generalized KS and periodic systems are not implemented. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-periodic-he-forces-en>)

  Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local KS equations. Runnable code covers spherical-helium spin-unpolarized Dirac exchange-only LDA. Correlation, GGA, hybrids, generalized KS and periodic systems are not implemented.

## Problem figures

- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png

## Exact / reference solutions

- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en>)

  Distinguish energy finite differences versus analytic forces, independent DFTK references and stored convergence checks for fixed He₂ configurations. This certifies no long-time first-principles MD accuracy.
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en#periodic-he-forces-en-validation>)

  Independent DFTK plane waves: Gamma/2³ analytic forces, eight cutoff settings and all-six-coordinate energy finite differences. State shared Libxc formulas and different finite-basis limits.

## Code and validation

- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en>)
  availability: run

  Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
