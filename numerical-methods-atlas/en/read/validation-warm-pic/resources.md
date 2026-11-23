# Warm PIC: Landau damping and two-stream instability

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-warm-pic/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare self-consistent weighted full-f PIC with independently formulated dielectric dispersion and linear Volterra IVPs.

## Methods

- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [Particle-in-cell / PIC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=en>)
- [Cloud-in-cell assignment and interpolation](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=en>)
- [Velocity Verlet / particle leapfrog](<https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=en>)

## Equations

- [Electrostatic Vlasov–Poisson equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en>)

  1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope. vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.
- [Electrostatic Vlasov–Poisson equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en>)

  1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope. Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.
- [Electrostatic Vlasov–Poisson equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#vlasov-poisson-en>)

  1D1V electrons and fixed neutralizing background. Separate weighted full-f particle,mesh and time approximations from the linear-reference scope.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-algorithm>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-algorithm>)

  Positive Gaussian velocity weights and density-CDF inversion load the joint(x,v) distribution. Recompute CIC deposition, FFT Poisson and matched CIC gathering at every velocity-Verlet kick. Qualify the dielectric root using branch continuation/bracket checks and a separately derived, time-refined Volterra IVP with the same fixed-window estimator.

## Problem figures

- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping-preview.png
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream-preview.png
- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-landau-damping.png
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/warm-pic/results/thermal-two-stream.png

## Exact / reference solutions

- [Warm PIC linear Landau damping — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-landau-damping/?lang=en#references-en>)

  31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.
- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
- [Warm PIC two-stream initial growth — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermal-two-stream/?lang=en#references-en>)

  31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en>)
  reference_kind: semi-analytic

  Semi-analytic reference vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution.
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004.
- [Warm PIC linear Landau damping — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en#thermal-landau-damping-en-validation>)

  31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.
- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-landau-damping-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference vth=omega_p=lambda_D=1,k.5,L4pi,alpha.01,grid32,256spatial strata×128velocity nodes,dt.04,T16,fit[4,12],seeds33001–33004. A separately evolved512-spatial-strata companion changes only particle-space resolution. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.
- [Warm PIC two-stream initial growth — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en#thermal-two-stream-en-validation>)

  31pytest,19self-consistent runs,140/140case gates and17/17independent linear-reference qualifiers passed; shared pytest+main7.283s. Landau256/512particle-space curve gap.001154 and amplitude-half gap.004376 meet the unchanged.03bound. Original64-strata130/131result (.05646>.03) remains an explicitly unmet retained example; amplitudes/all tolerances stayed fixed.
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-thermal-two-stream-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Each stream thermal speed1,drifts±3,k.2,L10pi,alpha1e-5,grid32,64spatial strata×128total velocity nodes,dt.05,T40,fit[12,20],seeds34001–34004. Small fixed1D1V collisionless electrons with fixed ions. Every positive-weight Gauss-velocity full-f carrier moves. Seed SE/t intervals are conditional on quiet spatial shifts, not iid particle noise or N^(-1/2) convergence. Velocity-quadrature bias has a separate doubling probe. The independent reference is a derived linear continuum IVP, not a second nonlinear Vlasov engine. Late two-stream behavior is diagnostic; no saturation-value gate. Even-grid Nyquist charge is separately reported rather than included in a full-spectrum Gauss claim. Four-shift Student-t intervals are nominal conditional summaries; neither coverage of the exact rate nor total error is established.

## Code and validation

- [Warm PIC linear Landau damping](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=en>)
  availability: run

  Advance thermal Maxwellian full-f particles and compare damping rate, frequency and signed-field history with qualified independent linear references.
- [Warm PIC two-stream initial growth](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=en>)
  availability: run

  Evolve counter-streaming warm Maxwellians; distinguish fixed-window growth and transients using dielectric and Volterra references.
