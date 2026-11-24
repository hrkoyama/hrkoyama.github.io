# CSVR and Langevin: distributions, fluctuations and correlations

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-thermostats/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Stochastic velocity rescaling (CSVR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Stochastic velocity rescaling (CSVR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en>)
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)

## Equations

- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. The Hamiltonian link identifies the anharmonic mechanical part; validation concerns distributions with added stochastic CSVR/Langevin heat baths.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-algorithm>)

  Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-algorithm>)

  Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-algorithm>)

  Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

## Problem figures

- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png
- [Exact CSVR bath: conditional laws, fluctuations and kinetic correlation](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png

## Exact / reference solutions

- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#references-en>)

  Independently integrate the anharmonic Boltzmann distribution and compare finite-step CSVR/Langevin distributions and moments, not exact stochastic trajectories.
- [Exact CSVR bath: conditional laws, fluctuations and kinetic correlation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-validation>)

  Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-validation>)

  Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.
- [OU weak moments with joint Brownian coupling](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ou-weak-moments-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping. dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.
- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-validation>)

  Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

## Code and validation

- [Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en>)
  availability: run

  Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.
- [Exact CSVR bath: conditional laws, fluctuations and kinetic correlation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en>)
  availability: run

  Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations.
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en>)
  availability: run

  Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.
