# Small learned models and independently checked biological ODEs

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-small-models/

Resources explicitly registered to the methods, problems and executions of this chapter. Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks.

## Methods

- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)

  Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)

  Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)

  Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.
- [PINNs and neural operators](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=en>)
- [Thomas tridiagonal elimination](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=en>)
- [L-stable SDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en>)
- [Adaptive SDIRK2 / step doubling](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en>)
- [Armijo-damped Newton](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [Michaelis–Menten and full enzyme kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en>)

  Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Scoped executed example: These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction. Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.
- [Lotka–Volterra predator–prey](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en>)

  Coupled prey growth and predation; a phase-plane and long-time integration test. Scoped executed example: This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity. Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.
- [Closed SEIR compartment model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#seir-compartment-en>)

  Educational rates with no births or deaths and constant population. Compare the early transient with a full two-by-two matrix exponential; no disease forecast is made. Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.
- [Closed SEIR compartment model](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#seir-compartment-en>)

  Educational rates with no births or deaths and constant population. Compare the early transient with a full two-by-two matrix exponential; no disease forecast is made.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-algorithm>)

  Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.
- [Poisson / Laplace equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en>)

  Elliptic boundary-value problems: check sign conventions, iterative solvers, sparse matrices and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-algorithm>)

  Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-algorithm>)

  Integrate all four states with SDIRK2 step doubling, using the same weighted L∞ residual for Newton convergence and Armijo backtracking. Evolve the reduced Michaelis–Menten equation separately with RK4 in θ, keeping integration error distinct from model-reduction error.
- [Michaelis–Menten and full enzyme kinetics](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-enzyme-en>)

  Enzyme saturation; the full mass-action system resolves the transient complex C, while the rate law eliminates a fast variable. The 1913 rapid-equilibrium interpretation and the 1925 quasi-steady-state derivation must remain distinct. Scoped executed example: These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-algorithm>)

  Integrate physical populations with classical RK4 at 400, 800 and 1600 fixed steps. Independent Radau/BDF references evolve log x and log y; the primary method uses neither a log-coordinate update nor invariant projection.
- [Lotka–Volterra predator–prey](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-lotka-volterra-en>)

  Coupled prey growth and predation; a phase-plane and long-time integration test. Scoped executed example: This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-algorithm>)

  Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

## Problem figures

- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa-preview.png
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra-preview.png
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png
- [Poisson PINN: independent grid error](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/pinn-poisson.png
- [Tiny FNO on held-out heat problems](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/fno-periodic-heat.png
- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/enzyme-qssa.png
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/lotka-volterra.png
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png
- [1D Poisson / smooth Dirichlet manufactured solutions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en>)

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png
- [Periodic Fourier-mode heat decay](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en>)

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png

## Exact / reference solutions

- [Enzyme conservation and QSSA — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/enzyme-qssa/?lang=en#references-en>)

  Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.
- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5. These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.
- [Lotka–Volterra invariant and positivity — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lotka-volterra/?lang=en#references-en>)

  Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lotka-volterra-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant. This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.
- [SEIR conservation and initial linearization — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en#references-en>)

  Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-seir-linearization-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows. These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.
- [Poisson PINN: independent grid error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en>)
  reference_kind: manufactured

  Manufactured solution Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points.
- [Tiny FNO on held-out heat problems](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en>)
  reference_kind: analytic

  Analytic reference Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters.
- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5.
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lotka-volterra-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant.
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-seir-linearization-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.
- [Poisson PINN: independent grid error — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-validation>)

  Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.
- [Poisson PINN: independent grid error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en>)
  relation: related-model
  reference_kind: manufactured

  Manufactured solution Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points. This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.
- [Tiny FNO on held-out heat problems — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-validation>)

  Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.
- [Heat / Fourier-mode decay](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Periodic unit interval; viscosity 0.02. The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
- [Tiny FNO on held-out heat problems](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters. This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.
- [Enzyme conservation and QSSA — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en#enzyme-qssa-en-validation>)

  Compare with independent full-system Radau/BDF references and an implicit scalar identity for the reduced equation. Check E+C=E₀, S+C+P=1, positivity and actual acceptance, rejection and Newton work. Retain both all-time errors including the initial layer and errors on the declared θ≥0.02 window.
- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-enzyme-qssa-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the closed dimensionless reaction E+S⇌C→E+P with k₁=10, k₋₁=k₂=1, S₀=1, C₀=P₀=0 and E₀=0.01 or 0.002. Then Kₘ=0.2, ε=E₀/(Kₘ+S₀)=1/120 or 1/600, and θ=E₀t ranges from 0 to 0.5. These two small-ε fixed-rate examples are educational. ε is a scale ratio, not itself a certified QSSA error bound. The θ≥0.02 window is not a proof that the initial layer has ended, and the calculation is not an in-vivo prediction.
- [Lotka–Volterra invariant and positivity — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en#lotka-volterra-en-validation>)

  Measure state error against the independent reference, drift of H and the minimum saved population separately. The reference stage qualifies analytic Jacobians, Radau/BDF agreement, tolerance refinement and the identity dH/dt=0.
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lotka-volterra-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use the dimensionless predator–prey equations x′=x(1−y), y′=y(x−1), initial state (1.2,0.8) and 0≤t≤20. Evaluate H=x−log x+y−log y only in the positive quadrant. This is a finite-time comparison for one initial state. The continuum closed orbit is not an attracting limit cycle. RK4 is not claimed to preserve H exactly, maintain positivity at arbitrary steps or guarantee long-time geometric fidelity.
- [SEIR conservation and initial linearization — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-validation>)

  Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-seir-linearization-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows. These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.
- [1D Poisson / smooth Dirichlet manufactured solutions — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#references-en>)

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Use manufactured sine solutions, the composite-sine comparison and discrete residuals with zero Dirichlet endpoints. The single sin(πx) reference does not represent every forcing variant. Independently qualify all 49 residual-Jacobian columns, loss-gradient coordinates and spatial derivatives. Save off-training solution error against sin(πx), PDE residual, boundary error and finite-difference error separately. Preserve actual convergence and accuracy decisions; a normal budget return is not convergence.
- [Poisson / manufactured sine](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en>)
  relation: related-model
  reference_kind: manufactured

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Manufactured solution Zero Dirichlet endpoints. The forcing is chosen from the target solution; this is not an arbitrary-source Poisson solution. It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.
- [Poisson PINN: independent grid error](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en>)
  relation: related-model
  reference_kind: manufactured

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Manufactured solution Solve dimensionless −uₓₓ=π² sin(πx) on [0,1] with zero Dirichlet data. Use sixteen hidden units, 49 real parameters, seeds 8401–8403, 64 training points and 257 separate evaluation points. This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.
- [Periodic Fourier-mode heat decay — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en>)

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Analytic exponential decay of a periodic Fourier mode is the standard. Distinguish the saved figure's amplitude 0.25 and viscosity 0.02 from code checks using other frequencies. Qualify all 93 real loss-gradient coordinates at two fixed finite-difference widths and compare Fourier blocks with direct DFT sums. Separate analytic heat-mode errors, grid-restriction differences and ID/OOD diagnostics. Relative error is NA when reference RMS≤10⁻¹²; zero and near-zero controls retain absolute errors.
- [Heat / Fourier-mode decay](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en>)
  relation: related-model
  reference_kind: analytic

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Analytic reference Periodic unit interval; viscosity 0.02. The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.
- [Tiny FNO on held-out heat problems](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en>)
  relation: related-model
  reference_kind: analytic

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Analytic reference Use periodic heat flow uₜ=νuₓₓ on [0,2π) to T=0.25. Split 46 whole problems into 24 training, 6 validation, 8 held-out ID, 4 viscosity-OOD and 4 spectrum-OOD problems. Use two fixed seeds and 93 real parameters. This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

## Code and validation

- [Enzyme conservation and QSSA](<https://hrkoyama.github.io/numerical-methods-atlas/validation/enzyme-qssa/?lang=en>)
  availability: run

  Separate the initial layer, integration error and QSSA modeling error in a four-state enzyme mechanism.
- [Lotka–Volterra invariant and positivity](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lotka-volterra/?lang=en>)
  availability: run

  Compare a positive orbit against an independently integrated log-coordinate reference.
- [SEIR conservation and initial linearization](<https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en>)
  availability: run

  Check population conservation and the full two-mode initial linearization separately.
- [Poisson PINN: independent grid error](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en>)
  availability: run

  Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.
- [Tiny FNO on held-out heat problems](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en>)
  availability: run

  Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.
- [1D Poisson / smooth Dirichlet manufactured solutions — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en>)
  availability: source

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Inspect the corresponding public checks and distribution conditions.
- [Periodic Fourier-mode heat decay — code and validation status](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en>)
  availability: source

  Study a Poisson PINN, periodic-heat FNO and enzyme, predator–prey and SEIR systems under fixed budgets. Original learning and approximation goals remain separate from reproduction checks. Inspect the corresponding public checks and distribution conditions.
