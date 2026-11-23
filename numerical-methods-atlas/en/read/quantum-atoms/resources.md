# Hydrogenic atoms and helium: runnable validation examples

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Coulomb and Hartree potentials](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)
- [Coulomb and Hartree potentials](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en>)
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)

## Equations

- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-hydrogenic-atoms-en>)

  One-electron stationary radial problem in atomic units. A finite radial box with zero Dirichlet boundaries is compared with infinite-domain hydrogenic analytic references; not a general many-electron, molecular or periodic solver.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-helium-ground-state-en>)

  Atomic-unit radial equations restricted to isolated spherical closed-shell 1s² helium. The RHF vH/2 form is specific to two electrons sharing one spatial orbital. LDA is exchange-only, without correlation; no UHF, GGA, hybrid, general molecular or periodic-DFT example.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.

## Problem figures

- [Hydrogenic radial eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png
- [Helium ground state: closed-shell HF and exchange-only LDA](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png

## Exact / reference solutions

- [Hydrogenic radial eigenproblems — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en>)

  Compare with analytic hydrogenic eigenenergies/orbitals and separate finite-radius truncation from mesh error using existing fixed inputs and stored results.
- [Helium ground state: closed-shell HF and exchange-only LDA — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en>)

  Check independent closed-shell HF/exchange-only LDA references, SCF residuals, electron number and mesh refinement. Approximate-functional solutions are not labeled exact many-body helium solutions.
- [Hydrogenic atoms: analytic references and grid refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en#hydrogenic-atoms-en-validation>)

  E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.
- [Helium: closed-shell HF and exchange-only LDA — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en#helium-ground-state-en-validation>)

  PySCF 2.11.0 / Libxc finite-Gaussian references. Distinguish extrapolation, finite-grid values and references. Regenerating the independent reference is outside this measured runner.

## Code and validation

- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en>)
  availability: run

  Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.
- [Helium: closed-shell HF and exchange-only LDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en>)
  availability: run

  Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.
- [Hydrogenic radial eigenproblems — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Helium ground state: closed-shell HF and exchange-only LDA — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
