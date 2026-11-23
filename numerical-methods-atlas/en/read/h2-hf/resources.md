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
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

## Equations

- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-h2-rhf-en>)

  Isolated two-electron RHF in finite s-Gaussian bases. Numerical convergence differs from RHF model error.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods.

## Problem figures

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png

## Exact / reference solutions

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en>)

  Use independent RHF references and SCF/s-type-basis checks for a small fixed H₂ model. Agreement in finite-basis RHF is not agreement with a fully correlated exact molecular solution.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en#h2-rhf-en-validation>)

  Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.

## Code and validation

- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en>)
  availability: run

  Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
