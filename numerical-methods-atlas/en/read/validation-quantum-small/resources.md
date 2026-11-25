# Small quantum models and saved-reference cards

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/

Resources explicitly registered to the methods, problems and executions of this chapter. Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified.

## Methods

- [Born–Oppenheimer molecular dynamics / BOMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en>)

  Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.
- [Car–Parrinello molecular dynamics / CPMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en>)

  Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)

  Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.
- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)

  Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)

  Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.
- [MP2 perturbation theory](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en>)

  Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.
- [Configuration interaction / CI](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en>)

  Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)

  Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.
- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)

  Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.
- [Pseudopotentials and PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en>)

  Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.
- [Born–Oppenheimer molecular dynamics / BOMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=en>)
- [Car–Parrinello molecular dynamics / CPMD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=en>)
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)
- [Schrodinger eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en>)
- [Hartree–Fock](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en>)
- [Kohn–Sham density functional theory / DFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en>)
- [Configuration interaction / CI](<https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en>)
- [Self-consistent field iteration / SCF](<https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en>)
- [MP2 perturbation theory](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en>)
- [Pseudopotentials and PAW](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en>)

## Equations

- [Two-state electronic-angle/nuclear BO and CP-type model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en>)

  Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified. Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules. Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules. Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee. Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.
- [Three-wave nonlocal kernel and mean Fermi occupations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en>)

  Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation. Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.
- [Two-state electronic-angle/nuclear BO and CP-type model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#two-state-bo-cp-model-en>)

  Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.
- [Unrestricted HF in a minimal two-electron model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en>)

  Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
- [Three-wave nonlocal kernel and mean Fermi occupations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en>)

  Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-algorithm>)

  Use analytic BO forces and the declared CP-type action with Verlet/BAOAB; record nuclear heat and fictitious electronic kinetic energy separately.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-algorithm>)

  Audit existing formulas and three stored energy rows; distinguish radial from volume density and orbital from total energy.
- [Stationary electronic Schrödinger equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en>)

  Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.
- [Closed-shell Hartree–Fock equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en>)

  Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.
- [Local Kohn–Sham DFT](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en>)

  Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-algorithm>)

  Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-algorithm>)

  Run fixed SCF and diagonalize the4x4 two-electron Hamiltonian using the unchanged explicit H STO-3G contraction.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-algorithm>)

  Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-algorithm>)

  Audit arithmetic of saved energy differences, analytic forces and Gaussian/PW comparisons under the original bounds.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-algorithm>)

  Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

## Problem figures

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png
- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png
- [Helium ground state: closed-shell HF and exchange-only LDA](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png
- [Hydrogenic radial eigenproblems](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/hydrogenic.png
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png

## Exact / reference solutions

- [A two-state BO / CP-type model with a short nuclear thermostat coupling — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=en#references-en>)

  Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.
- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.
- [Small 1D box and quantum harmonic-oscillator eigenpairs — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#references-en>)

  Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions. Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.
- [A tiny three-center H3+ RHF / MP2 / FCI example — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#references-en>)

  Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.
- [A three-wave periodic projector and Fermi-occupation model — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#references-en>)

  Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.
- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows.
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en>)
  reference_kind: analytic

  Analytic reference Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping.
- [A two-state BO / CP-type model with a short nuclear thermostat coupling — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en#two-state-bo-cp-ou-en-validation>)

  Check energy gradients, fixed4096/8192 RK4 sensitivity, extended energy, OU heat bookkeeping and conditional temperature variance.
- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-two-state-bo-cp-ou-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Actual coupled normalized electronic angle and nuclear coordinate, short NVE plus one nuclear OU trajectory. No first-principles/long NVE/canonical sampling/production CPMD. BO and mu.04 state comparisons use fixed4096/8192 RK4 companions; mu.01 receives energy checks only. Authored dimensionless model units with M=20 and angular fictitious mass mu=.04/.01; these are not cp.x emass units. Long first-principles NVE, general multi-orbital orthonormality/SCF errors, general electronic/nuclear baths, canonical equilibration, adiabatic/ergodic certification and materials remain unverified.
- [Hydrogenic formulas and immutable finite-basis helium reference cards — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en#atomic-reference-cards-en-validation>)

  Each of three saved rows uses40 uncontracted functions. Check exact values and electron counts without rerunning SCF or independent references.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [Small 1D box and quantum harmonic-oscillator eigenpairs — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-validation>)

  Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions. Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-validation>)

  Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function. Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
- [A tiny three-center H3+ RHF / MP2 / FCI example — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-validation>)

  Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.
- [Immutable periodic-helium energy and force reference audit — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-validation>)

  Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr. Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.
- [A three-wave periodic projector and Fermi-occupation model — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-validation>)

  Check an independent cubic spectral oracle, Hermiticity, electron number, entropy, analytic force and fixed-N free-energy differences.
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Authored rank-one periodic linear model and finite-N Helmholtz forces. No real metal/element pseudopotential/norm conservation/Hartree-XC/long MD claim. N=1.5 is a mean independent-particle Fermi occupation count, not an integer-N canonical many-body ensemble. Dimensionless G=-1,0,1,p=G+k,k=±.25 with equal.5weights,T=.05,mean electron countN=1.5 and spin factor2. No physical lattice-constant or metal mapping. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.
- [Helium ground state: closed-shell HF and exchange-only LDA — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#references-en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Check independent closed-shell HF/exchange-only LDA references, SCF residuals, electron number and mesh refinement. Approximate-functional solutions are not labeled exact many-body helium solutions.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [Hydrogenic radial eigenproblems — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hydrogenic-atoms/?lang=en#references-en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Compare with analytic hydrogenic eigenenergies/orbitals and separate finite-radius truncation from mesh error using existing fixed inputs and stored results. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.
- [Hydrogenic atoms: analytic references and grid refinement](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hydrogenic-coulomb-reference-en>)
  relation: same-problem
  reference_kind: analytic

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Analytic reference Nonrelativistic infinite-mass point nucleus, Z=1,2. Reduced radial orbitals use second-order central differences on a uniform mesh. An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-atomic-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Finite-grid numerical reference Three saved 40-function He reference rows, hydrogenic analytic equations, p versus n and finite-grid/basis/model limits. Energies in hartree, radius in bohr; u in bohr^-1/2, p in bohr^-1 and n in bohr^-3. Three saved rows each use40basis functions, not40computed rows. Curation and saved-value audit only: zero new SCF/independent-reference runs. No correlated-exact He, complete-basis limit or full orbital rerun claim.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Use independent RHF references and SCF/s-type-basis checks for a small fixed H₂ model. Agreement in finite-basis RHF is not agreement with a fully correlated exact molecular solution.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Semi-analytic reference Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function. Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Distinguish energy finite differences versus analytic forces, independent DFTK references and stored convergence checks for fixed He₂ configurations. This certifies no long-time first-principles MD accuracy.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr. Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.
- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en>)

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Use stored independent DFTK, SCF, basis and k-point checks for a fixed small periodic He cell, limited to the pseudopotential and exchange-only LDA model.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Finite-grid numerical reference Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr. Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

## Code and validation

- [A two-state BO / CP-type model with a short nuclear thermostat coupling](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=en>)
  availability: run

  Compare a normalized two-state electronic degree of freedom coupled to a nuclear coordinate, short NVE and one nuclear OU bath.
- [Small 1D box and quantum harmonic-oscillator eigenpairs](<https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en>)
  availability: run

  Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.
- [A tiny three-center H3+ RHF / MP2 / FCI example](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en>)
  availability: run

  Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.
- [A three-wave periodic projector and Fermi-occupation model](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en>)
  availability: run

  Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.
- [Hydrogenic formulas and immutable finite-basis helium reference cards](<https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=en>)
  availability: run

  Map existing H/He formulas and saved finite-basis references to units, normalization and model limits.
- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](<https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en>)
  availability: run

  Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.
- [Immutable periodic-helium energy and force reference audit](<https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en>)
  availability: run

  Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.
- [Helium ground state: closed-shell HF and exchange-only LDA — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=en#code-en>)
  availability: source

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Inspect the corresponding public checks and distribution conditions.
- [H₂ molecular RHF: independent reference, SCF and s-basis refinement — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en>)
  availability: source

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Inspect the corresponding public checks and distribution conditions.
- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en>)
  availability: source

  Fixed two-state dynamics,1D eigenpairs,minimal molecules and a3-wave model plus saved H/He and periodic-He audits. Broad expensive tails remain unverified. Inspect the corresponding public checks and distribution conditions.
