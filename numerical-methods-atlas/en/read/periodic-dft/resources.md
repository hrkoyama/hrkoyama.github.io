# Periodic DFT: Γ points, k-point integration, basis sets, SCF and an independent reference

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Born–Oppenheimer molecular dynamics / BOMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en>)
- [Car–Parrinello molecular dynamics / CPMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en>)
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

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-periodic-he-dft-en>)

  KS-LDA for a fixed 3D periodic He cell. BZ integration meshes differ from band paths; numerical convergence differs from physical-model accuracy.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.

## Problem figures

- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png

## Exact / reference solutions

- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en>)

  Use stored independent DFTK, SCF, basis and k-point checks for a fixed small periodic He cell, limited to the pseudopotential and exchange-only LDA model.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr. Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en#periodic-he-dft-en-validation>)

  Separately executed DFTK plane-wave KS-LDA at Gamma and 2³ for the same model, with cutoff convergence saved. Different finite orbital bases are compared within a stated tolerance, without machine-precision claims.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr. Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

## Code and validation

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en>)
  availability: run

  Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en>)
  availability: run

  Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.
- [Born–Oppenheimer molecular dynamics / BOMD — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Car–Parrinello molecular dynamics / CPMD — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
