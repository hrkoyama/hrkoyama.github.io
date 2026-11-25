# Closed-shell HF for H₂: independent references, SCF residuals and basis refinement

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/h2-hf/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Configuration interaction / CI](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

## Equations

- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Unrestricted HF in a minimal two-electron model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en>)

  Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-h2-rhf-en>)

  Isolated two-electron RHF in finite s-Gaussian bases. Numerical convergence differs from RHF model error.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.

## Problem figures

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png

## Exact / reference solutions

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en>)

  Use independent RHF references and SCF/s-type-basis checks for a small fixed H₂ model. Agreement in finite-basis RHF is not agreement with a fully correlated exact molecular solution.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function. Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en#h2-rhf-en-validation>)

  Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function. Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

## Code and validation

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en>)
  availability: run

  Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en>)
  availability: run

  Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
