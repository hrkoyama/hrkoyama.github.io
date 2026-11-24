# Geometric integration of constraints, orbits and multiple frequencies

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-geometric-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately.

## Methods

- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

  Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.
- [SHAKE constrained integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=en>)
- [RATTLE constrained integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

## Equations

- [Coupled two-frequency harmonic oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en>)

  Separate continuous normal modes, the ideal split map, a map with stored floating-point coefficients, and repeated rounded updates. alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-algorithm>)

  Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en>)

  Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-algorithm>)

  Original central-force KDK Verlet. Fixed, replayed and regenerated schedules are distinct. Positive radial crossings of cubic Hermite trajectories are localized by brentq.
- [Kepler two-body problem](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kepler-two-body-en>)

  Nondimensional planar ellipses separate phase, angular momentum, energy and step-selection effects.
- [Gravitational particle model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en>)

  Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-algorithm>)

  Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.
- [Coupled two-frequency harmonic oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en>)

  Separate continuous normal modes, the ideal split map, a map with stored floating-point coefficients, and repeated rounded updates.

## Problem figures

- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png
- [Kepler eccentricity and time-step controls](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png
- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en>)

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en>)

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/gravity-dynamics/results/gravity-kepler-preview.png

## Exact / reference solutions

- [Coupled frequencies and finite-window resonance — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#references-en>)

  The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.
- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi. The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en>)
  reference_kind: semi-analytic

  Semi-analytic reference L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.
- [Kepler eccentricity and time-step controls](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en>)
  reference_kind: semi-analytic

  Semi-analytic reference a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint.
- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en>)
  reference_kind: semi-analytic

  Semi-analytic reference alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi.
- [SHAKE and RATTLE: constraints and momentum ownership — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en#shake-rattle-pendulum-en-validation>)

  A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion. Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
- [Kepler eccentricity and time-step controls — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en#kepler-eccentricity-en-validation>)

  An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- [Kepler eccentricity and time-step controls](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint. Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.
- [Coupled frequencies and finite-window resonance — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-validation>)

  The 116 main decisions distinguish independent coupled normal modes, Decimal80/120 and Fraction frozen-coefficient maps, and stagewise gamma8 roundoff allowances. Ideal-pi Jordan structure is checked separately by rational identities. Each probe uses the current saved coefficient hex for its own Decimal80/120 actions; six accuracy actions use Decimal80.
- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference alpha=1, omega=10/20, q0=(1,1/omega) and p0=0. Central probes retain the evaluated binary64 h and sin/cos coefficients without snapping to mathematical pi. The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.
- [Constrained planar pendulum — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en>)

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets. A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Semi-analytic reference m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Semi-analytic reference L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion. Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
- [Unsoftened Kepler two-body time error — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=en#references-en>)

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Time refinement/phase, synchronized all-step energy,P/L/COM,independent pair force and root residuals. An independent Kepler-equation family, qualified with brentq and bisection, supports 92 main decisions: full-state error, energy/angular momentum, at least eight periapses, finite-window order and reversal defects.
- [Unsoftened Kepler two-body time error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gravity-kepler-en>)
  relation: same-problem
  reference_kind: analytic

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Analytic reference G=M=a1,e.4,masses.6/.4,epsilon0,128/256/512steps,initialCOM/P0. One orbit at fixed eccentricity only; softened binaries and long-time behavior are outside this exact reference.
- [Kepler eccentricity and time-step controls](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-kepler-eccentricity-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Fixed small examples compare SHAKE/RATTLE, Kepler orbits and coupled oscillators. Constraints, phase, energy and rounding effects are reported separately. Semi-analytic reference a=mu=reduced mass=1, without softening. One-period runs use 512/1024/2048 steps; ten-period controls use h0=2π/2048. Variable steps use h=h0|q| at the current state, with only the final step shortened to the physical endpoint. Small invariant errors do not establish phase accuracy. No canonical symplectic-defect measurement is claimed for the variable-step map, and fixed-h properties are not transferred automatically. R1 resolution was revised to R2 using pre-execution asymptotic planning, not measured calibration.

## Code and validation

- [Coupled frequencies and finite-window resonance](<https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en>)
  availability: run

  A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en>)
  availability: run

  Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.
- [Kepler eccentricity and time-step controls](<https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=en>)
  availability: run

  Sixteen fixed evolutions at e=0.1/0.7 compare invariants, same-time phase error, physical periapsis times and reversal.
