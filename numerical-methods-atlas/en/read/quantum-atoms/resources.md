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

  Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.
- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)
- [Coulomb and Hartree potentials](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en>)
- [LDA, GGA and hybrid functionals](<https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en>)

## Equations

- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-hydrogenic-atoms-en>)

  One-electron stationary radial problem in atomic units. A finite radial box with zero Dirichlet boundaries is compared with infinite-domain hydrogenic analytic references; not a general many-electron, molecular or periodic solver.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-helium-ground-state-en>)

  Atomic-unit radial equations restricted to isolated spherical closed-shell 1s² helium. The RHF vH/2 form is specific to two electrons sharing one spatial orbital. LDA is exchange-only, without correlation; no UHF, GGA, hybrid, general molecular or periodic-DFT example.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.
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

  Compare with analytic hydrogenic eigenenergies/orbitals and separate finite-radius truncation from mesh error using existing fixed inputs and stored results. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.
- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hydrogenic-coulomb-reference-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [Helium ground state: closed-shell HF and exchange-only LDA — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en>)

  Check independent closed-shell HF/exchange-only LDA references, SCF residuals, electron number and mesh refinement. Approximate-functional solutions are not labeled exact many-body helium solutions.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hydrogenic-coulomb-reference-en>)
  reference_kind: analytic

  Analytic reference Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh.
- [Hydrogenic atoms: analytic references and grid refinement — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en#hydrogenic-atoms-en-validation>)

  E_n=−Z²/(2n²) and Laguerre radial solutions, separating finite-grid and finite-box error.
- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hydrogenic-coulomb-reference-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [Helium: closed-shell HF and exchange-only LDA — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en#helium-ground-state-en-validation>)

  PySCF 2.11.0 / Libxc finite-Gaussian references. Distinguish extrapolation, finite-grid values and references. Regenerating the independent reference is outside this measured runner.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.

## Code and validation

- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/hydrogenic-atoms/?lang=en>)
  availability: run

  Isolated one-electron H and He⁺: compare 1s, 2s, 2p and 3d energies and radial orbitals against analytic solutions. Not a direct many-electron or molecular solver.
- [Helium: closed-shell HF and exchange-only LDA](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en>)
  availability: run

  Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en>)
  availability: run

  Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.
- [Hydrogenic radial eigenproblems — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
- [Helium ground state: closed-shell HF and exchange-only LDA — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en>)
  availability: source

  Inspect the corresponding public checks and distribution conditions.
