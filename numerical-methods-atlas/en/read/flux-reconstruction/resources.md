# Flux reconstruction: flux correction, DG and 1D periodic advection

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/flux-reconstruction/

Resources explicitly registered to the methods, problems and executions of this chapter. Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software.

## Methods

- [Flux reconstruction (FR)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en>)
- [Discontinuous Galerkin / Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=en>)
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=en>)

## Equations

- [Linear advection](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Transport at constant speed a: translation, numerical diffusion and stability.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-algorithm>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

## Problem figures

- [Periodic sine-wave advection](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png
- [1D periodic FR advection: Radau correction and published DG comparison](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/fr-periodic-advection.png

## Exact / reference solutions

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  reference_kind: analytic

  Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
- [Periodic sine-wave advection — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic translation of a periodic sine is the standard. The problem merges different amplitudes and representations; the reference-library amplitude 0.25 is not the input for every execution example. Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.
- [1D periodic FR advection: Radau correction and published DG comparison — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en#fr-periodic-advection-en-validation>)

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Integrate continuous L2 error at additional Gauss points and compare final polynomials with the actual published DG at common points. Check weighted mass at every RK stage and quadratic energy at each completed step. A matrix exponential of the same FR operator separately measures RK3 time error and its timestep-halving response.
- [Advection / sine translation](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Periodic unit interval; constant advection speed 1. Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.
- [WENO critical points: polynomial cell means and analytic periodic transport](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en>)
  relation: related-model
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Local references integrate polynomials over five cells centered around x=0 and evaluate at h/2. Regular, first-critical and second-critical profiles use h=1/64…1/512. The actual periodic-transport reference is the Fourier-integrated cell mean of q₀=cos(2πx)+.1sin³(2πx) on[0,1], speed1,T1, checked independently by Gauss12 point-function quadrature. Local polynomials differ from the evolved profile; neither point samples nor another PDE calculation are substituted for cell means. An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.
- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en>)
  relation: same-problem
  reference_kind: analytic

  Explicitly connects the newly executed fixed inputs to methods, equations, existing physical problems, analytic/manufactured references and release code. It does not validate related external software. Analytic reference Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals. Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

## Code and validation

- [1D periodic FR advection: Radau correction and published DG comparison](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en>)
  availability: run

  Transport0.4+sin(2pi x) toT=.25. Execute Gauss-node/Radau FR and the existing modal DG for p=1/2 and8/16/32 cells; measure analytic error, mass and time-integration error.
- [Flux reconstruction (FR) — code and checks](<https://hrkoyama.github.io/numerical-methods-atlas/methods/flux-reconstruction/?lang=en#method-execution-en>)
  availability: source

  Method-specific editions and related sources; fixed-input runs are listed separately.
