# MCMC, temperature control and biological models

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Stochastic velocity rescaling (CSVR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Implicit midpoint](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Lie–Trotter splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Strang splitting](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

  Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.
- [Markov-chain Monte Carlo / MCMC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en>)
- [Langevin thermostat](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en>)
- [Centered spatial difference](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en>)
- [Classical RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en>)

## Equations

- [Hamiltonian systems and oscillators](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en>)

  Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity. The Hamiltonian link identifies the harmonic mechanical part; the calculations add friction/noise or a CSVR heat bath.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries. Linear reaction-diffusion u_t=D u_xx+r u, with published D=0.1 and r=0.1. The heat link covers diffusion; compare using the eigenvalue r-Dk² including reaction.
- [Schnakenberg reaction–diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en>)

  A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [Turing reaction–diffusion framework](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en>)

  A framework for diffusion-driven pattern onset around a homogeneous reaction equilibrium, not a unique choice of f and g. A spot image or unequal diffusion coefficients alone do not establish a Turing mechanism. Boundary conditions determine the available modes. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim. Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.
- [FitzHugh–Nagumo excitation and recovery](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fitzhugh-nagumo-en>)

  A normalized fast excitation/slow recovery model for pulses, refractoriness and spiral waves when extended in space. This is a common normalized variant; cubic coefficients, recovery signs and nondimensionalization differ between formulations. Scoped executed example: The executed case has D=0 and no spatial coordinate. Scoped verification of an FHN/BVP-style reduced ODE. It excludes full HH ion channels, spatial axons, patient data and experimental electrophysiology reproduction. The published fixed input is the two-variable ODE limit without spatial diffusion; it does not validate the general propagation PDE.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-algorithm>)

  Use a log-acceptance Metropolis update. Pool FFT within-chain autocovariances and obtain mean-observable ESS from Geyer initial-positive pairs starting at gamma0+gamma1. Also report classical split-Rhat.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-algorithm>)

  Compose force B and drift A half steps with exact OU noise O in B-A-O-A-B order. Record covariance, three CDFs, energy mean/variance and position correlation.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en#reaction-diffusion-fourier-en-algorithm>)

  Advance original periodic second-centered differences with RK4. The spatial sequence uses one small time step; the temporal sequence fixes the spatial operator.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-algorithm>)

  Advance the linearized and short nonlinear PDEs using original centered differences/RK4. Record mode amplitudes/growth on three grids, minimum concentrations and early-pattern amplification.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-algorithm>)

  Use original RK4 with steps 0.1/0.05/0.025, splitting time intervals exactly at pulse discontinuities. At output spacing 0.1, measure the peak and distance from rest.

## Problem figures

- [Gaussian-target MCMC: distribution, autocorrelation and ESS](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png
- [Langevin thermostat: canonical distributions, timestep bias and correlation](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png
- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png
- [Gaussian-target MCMC: distribution, autocorrelation and ESS](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png
- [Langevin thermostat: canonical distributions, timestep bias and correlation](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png
- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png

## Exact / reference solutions

- [Gaussian-target MCMC: distribution, autocorrelation and ESS — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#references-en>)

  Use the known Gaussian target and moments to check sampled distributions, autocorrelation and ESS. The 18-case reference library has no exact MCMC-trajectory card.
- [Langevin thermostat: canonical distributions, timestep bias and correlation — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#references-en>)

  Use analytic canonical-distribution, moment and correlation standards for the harmonic potential to check timestep bias, separately from frictionless, noiseless harmonic trajectories.
- [Reaction-diffusion: separate second-order space and fourth-order time — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en>)

  Separate continuous and semidiscrete Fourier solutions of linear reaction-diffusion to check second-order space/fourth-order time. Do not reuse the pure-diffusion card's decay rate unchanged.
- [Turing instability: linear growth and small-amplitude patterns — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en>)

  Use matrix-exponential linear growth rates at small amplitude; nonlinear supplements check independent Radau references, positivity and refinement. A linearization is not an exact saturated nonlinear pattern.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=en#references-en>)

  Compare the two-variable reduced ODE under a current pulse with an independent DOP853 reference, checking all-output-time errors, temporal refinement and recovery.
- [Gaussian-target MCMC: distribution, autocorrelation and ESS — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-validation>)

  Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.
- [Langevin thermostat: canonical distributions, timestep bias and correlation — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en#langevin-harmonic-en-validation>)

  Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.
- [Reaction-diffusion: separate second-order space and fourth-order time — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en#reaction-diffusion-fourier-en-validation>)

  Measure spatial order against r-Dk² and temporal order against r-4Dsin²(kdx/2)/dx². Both are independent analytic references, rather than a finer-grid run of the same solver.
- [Turing instability: linear growth and small-amplitude patterns — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en#turing-schnakenberg-en-validation>)

  Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en#fitzhugh-nagumo-en-validation>)

  Compare separate SciPy DOP853 at rtol=1e-11 and 1e-13 to check reference sensitivity; measure maximum solution error and time order against the tighter reference. Peak time is resolved only on the output grid.

## Code and validation

- [Gaussian-target MCMC: distribution, autocorrelation and ESS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en>)
  availability: run

  Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.
- [Langevin thermostat: canonical distributions, timestep bias and correlation](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en>)
  availability: run

  Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.
- [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en>)
  availability: run

  Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.
- [Reaction-diffusion: separate second-order space and fourth-order time](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en>)
  availability: run

  Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.
- [Turing instability: linear growth and small-amplitude patterns](<https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en>)
  availability: run

  Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.
- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en>)
  availability: run

  Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.
- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](<https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en>)
  availability: run

  Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.
- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](<https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en>)
  availability: run

  Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.
- [FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=en>)
  availability: run

  Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853.
