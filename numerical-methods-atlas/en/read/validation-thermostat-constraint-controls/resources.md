# Deterministic thermostats and constrained degrees of freedom

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostat-constraint-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare thermostats on small harmonic/quartic systems and check effective degrees of freedom, momentum covariance and transient distributions under fixed linear constraints. Retain unmet statistical goals.

## Methods

- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)

  Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.
- [Stochastic velocity rescaling (CSVR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en>)

  Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.
- [Nosé–Hoover thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=en>)
- [Nosé–Hoover chains](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=en>)
- [Berendsen weak-coupling thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=en>)
- [Direct velocity rescaling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=en>)
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)
- [Stochastic velocity rescaling (CSVR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en>)

## Equations

- [Canonical momentum under fixed linear constraints](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#projected-canonical-model-en>)

  These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical. Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.
- [Two-mode deterministic thermostat model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-mode-thermostat-model-en>)

  This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.
- [Canonical momentum under fixed linear constraints](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#projected-canonical-model-en>)

  These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-algorithm>)

  Symmetrically compose exact frozen-variable bath subflows,two subcycles per half bath. Advance eta only in E subflows and compare short trajectories against independent full extendedODE references.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-algorithm>)

  Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.

## Problem figures

- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png
- [NH,chains,weak coupling and fixed-speed contrasts](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png
- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en>)

  Compare thermostats on small harmonic/quartic systems and check effective degrees of freedom, momentum covariance and transient distributions under fixed linear constraints. Retain unmet statistical goals. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png

## Exact / reference solutions

- [Constraints,centre-of-mass removal and canonical statistics — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#references-en>)

  Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.
- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-projected-canonical-dof-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas. Dimensionless; masses 1/2/3 and kBT=1. Fixed linear constraints Cq=0 and CM⁻¹p=0; redundant rows are compared on the same tangent space. These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.
- [NH,chains,weak coupling and fixed-speed contrasts](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas. Dimensionless, unit masses, kBT=1, frequencies 1/1.7; Q1=2tau², Qj=tau². Two-mode initial-value problem without spatial boundaries; fixed canonical/heated ensembles.
- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-projected-canonical-dof-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas. Dimensionless; masses 1/2/3 and kBT=1. Fixed linear constraints Cq=0 and CM⁻¹p=0; redundant rows are compared on the same tangent space.
- [NH,chains,weak coupling and fixed-speed contrasts — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-validation>)

  Separately test physical reversal,Hext derivative,phi1,local weak-coupling inverses and noninjective rescaling. Retain four distributions,fluctuations,signed correlations and unresolved DKW precision at time20.
- [NH,chains,weak coupling and fixed-speed contrasts](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas. Dimensionless, unit masses, kBT=1, frequencies 1/1.7; Q1=2tau², Qj=tau². Two-mode initial-value problem without spatial boundaries; fixed canonical/heated ensembles. Same two-mode quartic system plus a harmonic control; short-time and finite-sample deterministic-bath comparisons.
- [Constraints,centre-of-mass removal and canonical statistics — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-validation>)

  Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.
- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-projected-canonical-dof-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas. Dimensionless; masses 1/2/3 and kBT=1. Fixed linear constraints Cq=0 and CM⁻¹p=0; redundant rows are compared on the same tangent space. These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en>)

  Compare thermostats on small harmonic/quartic systems and check effective degrees of freedom, momentum covariance and transient distributions under fixed linear constraints. Retain unmet statistical goals. Independently integrate the anharmonic Boltzmann distribution and compare finite-step CSVR/Langevin distributions and moments, not exact stochastic trajectories.
- [NH,chains,weak coupling and fixed-speed contrasts](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Compare thermostats on small harmonic/quartic systems and check effective degrees of freedom, momentum covariance and transient distributions under fixed linear constraints. Retain unmet statistical goals. Semi-analytic reference Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas. Dimensionless, unit masses, kBT=1, frequencies 1/1.7; Q1=2tau², Qj=tau². Two-mode initial-value problem without spatial boundaries; fixed canonical/heated ensembles. Same two-mode quartic system plus a harmonic control; short-time and finite-sample deterministic-bath comparisons.

## Code and validation

- [Constraints,centre-of-mass removal and canonical statistics](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en>)
  availability: run

  Separate effectiveDOF,momentum covariance,transient distributions and time correlations.
- [NH,chains,weak coupling and fixed-speed contrasts](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en>)
  availability: run

  Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.
