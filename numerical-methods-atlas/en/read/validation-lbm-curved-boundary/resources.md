# LBM curved walls and a Re20 cylinder

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-lbm-curved-boundary/

Resources explicitly registered to the methods, problems and executions of this chapter. Advance actual Re20 cylinder flow with curved walls and an open outlet; compare forces,pressure difference and wake with independent numerical benchmarks.

## Methods

- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

  StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.
- [D2Q9–BGK collision and streaming](<https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=en>)

## Equations

- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow. [0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity. [0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-algorithm>)

  StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.
- [Isothermal lattice BGK](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en>)

  Collision/streaming in lattice units Δx=Δt=1. Examples cover D2Q9 isothermal low-Mach shear waves and Poiseuille flow.
- [Incompressible Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en>)

  Representative constant-density/viscosity flow. In addition to periodic2D MAC projection/Taylor–Green, a separate release verifies a pressure-eliminated nonperiodic Re100 cavity.

## Problem figures

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png
- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20.png

## Exact / reference solutions

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#references-en>)

  Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.
- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference [0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity. Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.
- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference [0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity.
- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-validation>)

  Group28pytest;33cylinder gates. Score distance fromoriginalTable3estimated ranges usingseparate frozen coarse-grid tolerances:CD5%,CLabsolute.01,dp10%,Laabsolute.025. Check26/28/30field/force/dp stationarity,twogrid difference,Ma andwall/open budgets. Retain prior outletinstability anddistinguish the87boundarycomponent qualifiers frommain acceptance.
- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference [0,2.2]x[0,.41],center(.2,.2),R.05,nu.001,rho1,mean.2/peak.3/Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18k/36ksteps. Parabolic inlet;all-nine poststream NEE outletwithrho1andadjacent-interiorvelocity. Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

## Code and validation

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en>)
  availability: run

  Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.
