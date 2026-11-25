# Independent checks of membrane dynamics and reaction SSA

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-ode-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Check Hodgkin–Huxley clamps, rest and firing alongside exact immigration–death SSA transient laws on fixed small inputs.

## Methods

- [Gillespie direct stochastic simulation (SSA)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

  Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.
- [Gillespie direct stochastic simulation (SSA)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en>)

  Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

## Equations

- [Hodgkin–Huxley membrane dynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en>)

  Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Not implementation of the entire model family. Fixed cases: Hodgkin–Huxley: clamps, rest and firing Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse.
- [Chemical master equation and Gillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en>)

  Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Not implementation of the entire model family. Fixed cases: Immigration–death SSA: exact transient laws Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.
- [Immigration–death reaction and exact transient law](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en>)

  Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble. Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record.
- [Immigration–death reaction and exact transient law](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#immigration-death-model-en>)

  Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-algorithm>)

  Use classicalRK4 with all stages owned by each current segment. Separately qualify removable rate singularities, a Decimal rest root and independently written DP5(4)/Cash–Karp references.
- [Hodgkin–Huxley membrane dynamics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-hodgkin-huxley-en>)

  Voltage and gating variables z=m,h,n describe an ionic excitable membrane. A cable extension adds spatial axial current. The original squid-axon model is not a calibrated human cardiac model. No single rate parameter set is selected by this survey. Not implementation of the entire model family. Fixed cases: Hodgkin–Huxley: clamps, rest and firing
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-algorithm>)

  Use direct GillespieSSA with pending event times preserved across observations. Draw open-grid uniforms from rawPCG64; record finite-grid Poisson initialization and all RNG streams.
- [Chemical master equation and Gillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-chemical-master-en>)

  Integer molecule counts, reaction jumps νj and propensities aj; SSA samples paths of this continuous-time Markov model. The 1977 paper is a foundational SSA reference, not a priority claim for all master equations. SSA is a solver; the reaction network is the model. A seed documents a trajectory, not an ensemble validation. Not implementation of the entire model family. Fixed cases: Immigration–death SSA: exact transient laws

## Problem figures

- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png
- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png
- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png

## Exact / reference solutions

- [Hodgkin–Huxley: clamps, rest and firing — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=en#references-en>)

  Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse. ms, mV, microampere/cm², 6.3°C; dimensionless gates. Spatially uniform single membrane; voltage clamp or segment-current initial-value problem. This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.
- [Immigration–death SSA: exact transient laws — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=en#references-en>)

  Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.
- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record. Integer particle counts and a fixed time unit; death rate 1 per particle and immigration rate 6. Nonnegative integer counts; death propensity vanishes at N=0. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse. ms, mV, microampere/cm², 6.3°C; dimensionless gates. Spatially uniform single membrane; voltage clamp or segment-current initial-value problem.
- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en>)
  reference_kind: analytic

  Analytic reference Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record. Integer particle counts and a fixed time unit; death rate 1 per particle and immigration rate 6. Nonnegative integer counts; death propensity vanishes at N=0.
- [Hodgkin–Huxley: clamps, rest and firing — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en#hodgkin-huxley-controls-en-validation>)

  Retain errors over all accepted times, voltage/gate ranges and Hermite firing events from fresh accepted-endpoint derivatives. Preserve the original1e-8clamp goal even when unmet.
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-hodgkin-huxley-controls-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Fix6.3°C and the NEURON8.2.6 analytic absolute-voltage convention in ms/mV/µA cm⁻². Use four clamp voltages, three steps, a20ms rest and a10–11ms pulse. ms, mV, microampere/cm², 6.3°C; dimensionless gates. Spatially uniform single membrane; voltage clamp or segment-current initial-value problem. This educational membrane model does not reproduce the original voltage convention, TABLE/cnexp, cable propagation or measured physiology. Missing/unresolved events remain explicit; rest-root uniqueness and interval-Hurwitz stability are unclaimed.
- [Immigration–death SSA: exact transient laws — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en#immigration-death-ssa-en-validation>)

  Qualify exact Binomial-plus-Poisson transients with directed80/120digit intervals and tail bounds. Combine20DKW and20exact-sum mean goals under nominal union bound0.01; retain five-SE variance goals separately.
- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-immigration-death-ssa-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use immigration6, per-particle death1 and observations0/0.5/2/4. Compare initial0,5 and nominal stationary Poisson(6), two seeds each and2,048paths per record. Integer particle counts and a fixed time unit; death rate 1 per particle and immigration rate 6. Nonnegative integer counts; death propensity vanishes at N=0. Finite deterministic-start transients are not stationary. Interval qualification concerns the idealIID reference law, without a whole-software PRNG/logarithm coverage guarantee or a claim that one path represents the ensemble.

## Code and validation

- [Immigration–death SSA: exact transient laws](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=en>)
  availability: run

  Separate one displayed path from12,288fixed ensemble paths.
- [Hodgkin–Huxley: clamps, rest and firing](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=en>)
  availability: run

  Compare analytic clamp gates and a four-state system with segment-owned current.
- [Gillespie direct stochastic simulation (SSA) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
