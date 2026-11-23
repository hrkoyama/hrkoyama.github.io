# Finite-Knudsen Couette and Fourier flows

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-wall/

Resources explicitly registered to the methods, problems and executions of this chapter. Compare physical-time hard-sphere collisions,flux-weighted wall reemission and budgets with independent SPARTA references.

## Methods

- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

## Equations

- [Hard-sphere Boltzmann transport,walls and reservoirs](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en>)

  1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs. {"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,1],"speeds":[-0.5,0.5]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.
- [Hard-sphere Boltzmann transport,walls and reservoirs](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en>)

  1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs. {"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.
- [Hard-sphere Boltzmann transport,walls and reservoirs](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en>)

  1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-algorithm>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-algorithm>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

## Problem figures

- [Hard-sphere DSMC finite-Kn Couette flow](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette-preview.png
- [Hard-sphere DSMC finite-Kn Fourier heat conduction](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png
- [Hard-sphere DSMC finite-Kn Couette flow](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-couette.png
- [Hard-sphere DSMC finite-Kn Fourier heat conduction](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png

## Exact / reference solutions

- [Hard-sphere DSMC finite-Kn Couette flow — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-couette/?lang=en#references-en>)

  Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.
- [Finite-Kn hard-sphere Couette flow](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Twalls1, tangential Uwalls+/-0.5; nonlinear viscous heating retained. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
- [Hard-sphere DSMC finite-Kn Fourier heat conduction — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#references-en>)

  Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.
- [Finite-Kn hard-sphere Fourier heat conduction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Tleft1,Tright2; fixed walls; no continuum linear-temperature reference. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
- [Finite-Kn hard-sphere Couette flow](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Twalls1, tangential Uwalls+/-0.5; nonlinear viscous heating retained. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.
- [Finite-Kn hard-sphere Fourier heat conduction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Tleft1,Tright2; fixed walls; no continuum linear-temperature reference. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.
- [Hard-sphere DSMC finite-Kn Couette flow — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en#dsmc-couette-en-validation>)

  Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.
- [Finite-Kn hard-sphere Couette flow](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-couette-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Twalls1, tangential Uwalls+/-0.5; nonlinear viscous heating retained. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
- [Hard-sphere DSMC finite-Kn Fourier heat conduction — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-validation>)

  Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.
- [Finite-Kn hard-sphere Fourier heat conduction](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference H=2lambda0; diffuse Tleft1,Tright2; fixed walls; no continuum linear-temperature reference. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

## Code and validation

- [Hard-sphere DSMC finite-Kn Couette flow](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-couette/?lang=en>)
  availability: run

  Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
- [Hard-sphere DSMC finite-Kn Fourier heat conduction](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en>)
  availability: run

  Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
