# DAE initialization, conservation and constraint drift

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dae-controls/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references.

## Methods

- [Differential-algebraic equations / DAE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en>)

  Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.
- [Differential-algebraic equations / DAE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en>)

  Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.
- [SHAKE constrained integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=en>)

  Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.
- [RATTLE constrained integration](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=en>)

  Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages. Original scalar Newton position constraints, RATTLE final tangent impulses and SHAKE position pairs. SHAKE momentum is centered only at interior nodes; endpoint momenta are absent. SHAKE solves columns are eta, eta/h^2, position residual and Newton updates. Column1 uses the uniform recurrence normalization eta/h^2. For the first constrained half-step startup, the physical multiplier is 2*eta/h^2; later full position-Verlet steps use eta/h^2. Reverse-pair steps all use the later recurrence convention. RATTLE has its separate five-column normalization. No scientific gate or plot uses SHAKE column1.
- [Differential-algebraic equations / DAE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=en>)
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [Semi-explicit index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en>)

  Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver. Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en>)

  Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps. m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-algorithm>)

  Use coupled Newton with an Armijo search in the same scaled norm, retaining rather than repairing a singular initial guess.
- [Semi-explicit index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#index-one-dae-en>)

  Small fixed examples expose consistent initialization and separate differential/algebraic residuals; this is not a general-purpose DAE solver.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-algorithm>)

  Use fixed BE/Newton with analytic Jacobians and no mass projection or concentration clipping.
- [Robertson chemical kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#robertson-kinetics-en>)

  Distinguish the stiff three-species ODE from an index-one DAE obtained by replacing one equation with conservation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-algorithm>)

  Advance the index-reduced ODE and a critical constraint-error extension with fixed RK4, integrating constraint work at the same stages.
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#constrained-pendulum-en>)

  Distinguish the original position-constrained DAE, an underlying ODE based on differentiated constraints, and the SHAKE/RATTLE discrete maps.
- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

## Problem figures

- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png
- [Constrained planar pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png
- [Robertson kinetics: ODE and conservation DAE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en>)

  Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png

## Exact / reference solutions

- [Consistent initialization and discrete residuals for an index-one DAE — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=en#references-en>)

  Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm. One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.
- [Constrained planar pendulum — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=en#references-en>)

  Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets. A separately qualified Jacobi family and angular DOP853 reference support 74 main decisions. Finite-C centered identities, two-delta reduced-map diagnostics and position-pair versus full-state reversals are distinct.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion. Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en>)
  reference_kind: manufactured

  Manufactured solution Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en>)
  reference_kind: semi-analytic

  Semi-analytic reference m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity.
- [Consistent initialization and discrete residuals for an index-one DAE — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en#index1-dae-consistent-initialization-en-validation>)

  Compare independent Decimal manufactured states, three discrete roots and three fixed grids, checking first-order error and the algebraic constraint.
- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-index1-dae-consistent-initialization-en>)
  relation: same-problem
  reference_kind: manufactured

  Manufactured solution Dimensionless positive branch; differential and algebraic row scales are both one, with the maximum norm. One authored positive branch and fixed BE runs; no IDA execution or general DAE-solver qualification.
- [Robertson conservation DAE and stored official IDA values — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en#robertson-conservation-dae-en-validation>)

  Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.
- [Index reduction, constraint drift and explicit stabilization for a pendulum — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en#high-index-pendulum-en-validation>)

  Qualify the Jacobi family against two independent angular ODE runs, then compare states, exact constraint laws and energy/work budgets.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-high-index-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference m=L=g=1, initial angle 0.7 and zero angular velocity; off-manifold controls explicitly add radial velocity. No projection, normalization or SHAKE/RATTLE; no general index-three-solver or symplecticity claim.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-shake-rattle-pendulum-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference L=m=g=1, initial angle 0.7 and zero angular velocity. C=(q·q−1)/2, T=100 and h=0.04/0.02/0.01; position targets are fixed at 1e−13, with a coarse 1e−10 companion. Original SHAKE and RATTLE full texts remain unread; selected author lecture notes were inspected. The finite-difference symplectic defect is a local proxy, not a general proof, and centered SHAKE velocity is not assigned RATTLE tangency.
- [Robertson kinetics: ODE and conservation DAE — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=en#references-en>)

  Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references. Check actual errors at 22 common times, mass and minimum values at every accepted state, true stage residuals, and actual RHS, Jacobian, factorization and linear-solve counts separately. Evaluate all 39 original targets, retaining the four unmet accuracy/refinement goals as study outcomes. The other 35 requirements, independent references and faithful saved-array recomputation remain mandatory.
- [Robertson kinetics: initial stiffness and actual error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-stiff-kinetics-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references. Finite-grid numerical reference A nondimensional three-species system starts at (1, 0, 0) and ends at T = 0.4. The fixed methods use 512, 1024 and 2048 steps; two adaptive tolerance settings bring the total to eight runs. Conservation and positivity are observations for these inputs, not universal guarantees. Accuracy is sampled on T <= 0.4; this does not validate long-time chemistry or an all-time error bound.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-robertson-conservation-dae-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Compare consistent initialization, an index-one conservation DAE, and an underlying ODE for an index-three pendulum. Comparisons with stored official IDA output are distinguished from newly executed independent ODE references. Finite-grid numerical reference Model time zero to four; the intermediate-species state and residual scale is 1e-4. Printing intervals and numerical errors are distinct. Only two official SUNDIALS v7.1.1 printed rows; zero new IDA executions, with no long-time chemistry or general DAE-performance claim. No asymptotic-convergence or all-original-accuracy-goals claim is made for this fixed schedule.

## Code and validation

- [Consistent initialization and discrete residuals for an index-one DAE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=en>)
  availability: run

  Separate initialization, backward-Euler error and residuals on a known positive index-one DAE branch.
- [Index reduction, constraint drift and explicit stabilization for a pendulum](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=en>)
  availability: run

  Derive an explicit ODE from an index-three position constraint and compare drift and stabilization for consistent and inconsistent starts.
- [SHAKE and RATTLE: constraints and momentum ownership](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=en>)
  availability: run

  Ten fixed pendulum evolutions distinguish position constraints, full-time tangent momentum and interior centered momentum.
- [Robertson conservation DAE and stored official IDA values](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=en>)
  availability: run

  Compare the Robertson conservation DAE and full ODE on the same fixed time grids, with a separate check of stored official IDA values. The first retained run missed four original time-accuracy and refinement goals.
