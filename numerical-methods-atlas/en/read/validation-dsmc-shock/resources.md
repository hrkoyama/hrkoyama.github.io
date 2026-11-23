# Mach2 planar shock with hard-sphere DSMC

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-dsmc-shock/

Resources explicitly registered to the methods, problems and executions of this chapter. For a1D-space,3D-velocity open-reservoir shock,distinguish RH far states from independent numerical internal-profile references.

## Methods

- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories.
- [DSMC and kinetic transport](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en>)

## Equations

- [Hard-sphere Boltzmann transport,walls and reservoirs](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en>)

  1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs. {"kind":"shock","cells":192,"length":16,"weight":0.005208333333333333,"dt":0.01,"burn_in":20,"sample_time":20,"blocks":5,"bins":64,"sample_every":10,"hist_velocity":[-4,7]} Twelve independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-algorithm>)

  Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time. Open-reservoir macro counts use unbiased floor(mean)+Bernoulli(fraction) per face/species/half-stream to reduce artificial sampling variance; no Poisson number-fluctuation or thermodynamic-fluctuation reproduction claim. Retain the original four seeds and append the next eight consecutive seeds; uniform permutation/stable integer sorting preserves the ideal within-cell matching law,not RNG consumption or bit-identical trajectories.
- [Hard-sphere Boltzmann transport,walls and reservoirs](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en>)

  1D space,3D velocity monatomic gas. Physical-time speed-dependent hard-sphere collisions,wall flux distributions and open reservoirs.

## Problem figures

- [Hard-sphere DSMC Mach2 planar shock](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock-preview.png
- [Hard-sphere DSMC Mach2 planar shock](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-shock/results/dsmc-planar-shock.png

## Exact / reference solutions

- [Hard-sphere DSMC Mach2 planar shock — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=en#references-en>)

  Predeclare20pytest per group and15new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run. Preserve all81old gates and add48new-run gates=129. Primary12seed t95 usesdf11,reference4seed usesdf3; descriptive approximate-normal whole-seed intervals,not unconditional adaptive-study coverage.
- [Mach2 planar hard-sphere shock](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Monatomic gamma5/3,M1=2, RH inflow/outflow reservoirs at x0/16. Reference lambda2/lambda1=7/16; no profile shifting or shock pinning. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.
- [Mach2 planar hard-sphere shock](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Monatomic gamma5/3,M1=2, RH inflow/outflow reservoirs at x0/16. Reference lambda2/lambda1=7/16; no profile shifting or shock pinning. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs.
- [Hard-sphere DSMC Mach2 planar shock — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en#dsmc-planar-shock-en-validation>)

  Predeclare20pytest per group and15new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run. Preserve all81old gates and add48new-run gates=129. Primary12seed t95 usesdf11,reference4seed usesdf3; descriptive approximate-normal whole-seed intervals,not unconditional adaptive-study coverage.
- [Mach2 planar hard-sphere shock](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-planar-shock-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Monatomic gamma5/3,M1=2, RH inflow/outflow reservoirs at x0/16. Reference lambda2/lambda1=7/16; no profile shifting or shock pinning. All velocities3D; physical position1D. Four independent SPARTA seeds per configuration, fixed native inputs. Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. RH validates far states/full fluxes,not an exact internal shock profile. Saved phase space is not a2D physical flow.

## Code and validation

- [Hard-sphere DSMC Mach2 planar shock](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=en>)
  availability: run

  Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.
