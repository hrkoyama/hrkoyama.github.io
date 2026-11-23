# Quantum chemistry and DFT: approximations and equations

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)
- [Electronic-structure basis sets](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en>)
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)
- [Pulay / DIIS acceleration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/diis/?lang=en>)
- [Coulomb and Hartree potentials](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en>)
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)
- [Pseudopotentials and PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en>)
- [Periodic electronic structure and k-point sampling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en>)
- [Band symmetry groups and irreducible representations](<https://hrkoyama.github.io/numerical-methods-atlas/methods/band-symmetry/?lang=en>)
- [MP2 perturbation theory](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en>)
- [Configuration interaction / CI](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en>)
- [Coupled cluster / CCSD(T)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/coupled-cluster/?lang=en>)
- [CASSCF and multireference methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multireference/?lang=en>)
- [Time-dependent density functional theory / TDDFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/tddft/?lang=en>)
- [Quantum Monte Carlo](<https://hrkoyama.github.io/numerical-methods-atlas/methods/quantum-monte-carlo/?lang=en>)
- [DMRG and tensor networks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dmrg/?lang=en>)

## Equations

- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.
- [Time-dependent Kohn–Sham equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#time-dependent-kohn-sham-en>)

  Representative local time-dependent KS equations. Distinguish initial-state dependence, exchange-correlation memory and adiabatic approximations. No dedicated real-time or response implementation is published.

## Problem figures

No chapter-specific association is registered. Atlas-wide index: [Test problems by name and figure](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=en)

## Exact / reference solutions

No chapter-specific association is registered. Atlas-wide index: [Exact and reference solutions](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en)

## Code and validation

- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en>)
  availability: run

  Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en>)
  availability: run

  Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en>)
  availability: run

  Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en>)
  availability: run

  Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.
- [Helium: closed-shell HF and exchange-only LDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en>)
  availability: run

  Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.
- [Schrodinger eigenproblems — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Electronic-structure basis sets — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Hartree–Fock — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Kohn–Sham density functional theory / DFT — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Self-consistent field iteration / SCF — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Coulomb and Hartree potentials — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [LDA, GGA and hybrid functionals — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Pseudopotentials and PAW — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
- [Periodic electronic structure and k-point sampling — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
