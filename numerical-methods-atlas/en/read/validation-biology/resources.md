# Independent validation of nonlinear reaction–diffusion and pattern formation

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

## Equations

- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-algorithm>)

  Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-algorithm>)

  Strang-compose exact half-step diffusion of the FD matrix, diagonalized by FFT with symbol −4sin²(πk/N)/dx², and a full implicit-midpoint reaction step solved by local2×2 Newton iterations. FFT does not change FD space into spectral space. Fail on nonconvergence/budget excess; never clip concentrations.

## Problem figures

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-nonlinear.png
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/schnakenberg-pattern.png

## Exact / reference solutions

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en#schnakenberg-nonlinear-en-validation>)

  Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en#schnakenberg-pattern-en-validation>)

  Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

## Code and validation

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
