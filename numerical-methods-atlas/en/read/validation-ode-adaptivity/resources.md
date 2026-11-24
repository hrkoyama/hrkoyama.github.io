# Stiff ODEs, RK45 and boundary splitting

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-ode-adaptivity/

Resources explicitly registered to the methods, problems and executions of this chapter. Small fixed inputs validate Robertson and van der Pol, RK45 interpolation/events, and splitting with inhomogeneous boundaries. Independent references distinguish local estimates from actual errors and temporal from spatial errors.

## Methods

- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [Differential-algebraic equations / DAE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result. Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)

  Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)

  Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)

  Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

  For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.
- [Lie–Trotter splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en>)

  For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en>)
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en>)
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)
- [Lie–Trotter splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

## Equations

- [Robertson chemical kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en>)

  Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation. A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.
- [Semi-explicit index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en>)

  Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver. A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.
- [Van der Pol oscillator](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en>)

  Compare work and error for fixed mu values over a short interval; this does not validate a full relaxation cycle. The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.
- [Finite-dimensional linear evolution systems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en>)

  Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals. Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.
- [Linear reaction-diffusion with inhomogeneous boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en>)

  Separate temporal errors relative to the same nonperiodic finite-difference system from spatial errors relative to the continuous exact family. Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries. Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-algorithm>)

  BDF2 starts with backward Euler on the same grid. SDIRK2 stages use a weighted maximum residual and reuse Jacobian factors only within one stage. Adaptive steps use an RMS step-doubling estimate and accept the two-half-step result.
- [Robertson chemical kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en>)

  Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-algorithm>)

  Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.
- [Van der Pol oscillator](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en>)

  Compare work and error for fixed mu values over a short interval; this does not validate a full relaxation cycle.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-algorithm>)

  Use actual Dormand–Prince 5(4) stages, a quartic continuous extension, an accepted-state derivative cache and bracket bisection on retained interpolants. A rejected endpoint never replaces the accepted starting derivative.
- [Finite-dimensional linear evolution systems](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-evolution-system-en>)

  Each example distinguishes physical time in damped rotation from pseudo-time used to reduce steady residuals.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-algorithm>)

  For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.
- [Linear reaction-diffusion with inhomogeneous boundaries](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en>)

  Separate temporal errors relative to the same nonperiodic finite-difference system from spatial errors relative to the continuous exact family.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries.

## Problem figures

- [Robertson kinetics: ODE and conservation DAE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png

## Exact / reference solutions

- [Robertson kinetics: ODE and conservation DAE — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en>)

  Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately. Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
- [Van der Pol: an early stiffness transition — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=en#references-en>)

  Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.
- [RK45: embedded errors, dense output and events — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=en#references-en>)

  Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs. There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.
- [Strang splitting: Dirichlet boundary order reduction and correction — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#references-en>)

  First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs. This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en>)
  reference_kind: analytic

  Analytic reference Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs.
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.
- [Robertson kinetics: initial stiffness and actual error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en#robertson-stiff-kinetics-en-validation>)

  Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
- [Van der Pol: an early stiffness transition — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-validation>)

  Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-van-der-pol-stiff-transition-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs. This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.
- [RK45: embedded errors, dense output and events — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en#rk45-dense-events-en-validation>)

  Analytic states and the simple crossings at pi/6 and pi/2 provide independent truth. Check endpoints, 97 off-mesh samples, event times and residuals, and the actual identity nfev = 1 + 6 times the attempted-step count.
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-rk45-dense-events-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use gamma = 0.2, omega = 3, initial state (1, 0), and T = 2. Three paired relative and absolute tolerances with two maximum steps, plus two terminal runs, give eight runs. There is no general guarantee for tangential roots, multiple crossings within a step or systems with resets. Initial-zero and ownership controls are limited component tests; local tolerances and global accuracy remain distinct.
- [Strang splitting: Dirichlet boundary order reduction and correction — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-validation>)

  First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs. This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

## Code and validation

- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=en>)
  availability: run

  Compare BDF2, SDIRK2 and adaptive step doubling on a short fixed interval against qualified Radau and BDF references.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en>)
  availability: run

  Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.
- [Van der Pol: an early stiffness transition](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en>)
  availability: run

  Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.
- [RK45: embedded errors, dense output and events](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=en>)
  availability: run

  Use analytic damped rotation to test acceptance, rejection, FSAL ownership, dense interpolation and directed event times separately.
- [Strang splitting: Dirichlet boundary order reduction and correction](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en>)
  availability: run

  Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.
