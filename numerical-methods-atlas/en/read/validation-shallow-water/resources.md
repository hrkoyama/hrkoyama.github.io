# Shallow water: topography, lakes and dry beds

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/

Resources explicitly registered to the methods, problems and executions of this chapter.

## Methods

- [Godunov-type finite volumes](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en>)

  Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

  Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [Godunov-type finite volumes](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en>)

  The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)

  The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

  The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [Godunov-type finite volumes](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en>)
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en>)
- [Forward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en>)

## Equations

- [Shallow-water equations with bed source](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en>)

  One-dimensional frictionless Saint–Venant flow without rainfall. Distinguish the continuous topography from represented piecewise-constant bed means when checking hydrostatic balance. At a genuinely dry state h=q=0, define the advective momentum flux q²/h as0. 1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.
- [Shallow-water equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en>)

  The first two equations are 1D flat-bed, frictionless flow; the remaining lines are the linear rotating system about depth H. Distinguish nonlinear flow tests from rotating-system Fourier-symbol checks. Flat frictionless bed on[-10,10]m, dam0, hL=1m/hR=0, initial velocity0, g=9.81, t=.5s,800/1600/3200 cells. The Ritter formula uses an explicit rescaling distinct from the paper numerical example.
- [Shallow-water equations with bed source](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en>)

  One-dimensional frictionless Saint–Venant flow without rainfall. Distinguish the continuous topography from represented piecewise-constant bed means when checking hydrostatic balance. At a genuinely dry state h=q=0, define the advective momentum flux q²/h as0.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-algorithm>)

  Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-algorithm>)

  The FV solver supports h=q=0 directly; one-sided dry HLL speeds use u-c/u+2c and their reflection. Forward Euler at face CFL .4 records every minimum and shared-flux budget without raising cell depths. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.
- [Shallow-water equations](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en>)

  The first two equations are 1D flat-bed, frictionless flow; the remaining lines are the linear rotating system about depth H. Distinguish nonlinear flow tests from rotating-system Fourier-symbol checks.

## Problem figures

- [SWASHES lakes and steady shallow flow over topography](<https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png
- [Ritter dam break onto a dry bed](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break-preview.png
- [SWASHES topographic flow: lakes and nonzero steady discharge](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography.png
- [Dry-bed dam break: actual wetting and dry states](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/dry-bed-dam-break.png

## Exact / reference solutions

- [SWASHES lakes and steady shallow flow over topography — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/?lang=en#references-en>)

  Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.
- [Lake at rest: wet and emerged equilibrium over represented bed](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use g9.81,[0,25]m and200cells. Represent z=.2−.05(x−10)² on8<x<12 by split Gauss8 cell means, initializing h_i=max(eta0−z_i,0),q_i0 with eta0=.5/.1m. Hydrostatic reconstruction preserves equilibrium over this represented piecewise-constant bed; this differs from directly averaging depth over the continuous bed. Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
- [SWASHES steady flow: subcritical Bernoulli root](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Use g9.81,[0,25]m, the parabolic bed, discharge q4.42m²/s and downstream depth2m. Independently bisect the subcritical root of h+z+q²/(2gh²)=2+q²/(8g) and qualify cell quadrature. PDE runs on100/200/400cells start from the steady reference and advance to t2; they do not reproduce the original rest-to-steady transient. Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
- [Ritter dam break onto a dry bed — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/dry-bed-dam-break/?lang=en#references-en>)

  Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m.
- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Flat frictionless[-10,10]m, dam x00,hL1m/hR0,zero initial velocity,g9.81,t.5s. Split conserved(h,hu) cell means at the rarefaction head−sqrt(g)t and genuine dry front2sqrt(g)t. Separately track the fixed depth.001m contour. These dedicated gravity/domain/time inputs differ from the historical card, whose values remain unchanged. The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.
- [Shallow water / dry-bed fan](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver. Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.
- [Lake at rest: wet and emerged equilibrium over represented bed](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en>)
  reference_kind: analytic

  Analytic reference Use g9.81,[0,25]m and200cells. Represent z=.2−.05(x−10)² on8<x<12 by split Gauss8 cell means, initializing h_i=max(eta0−z_i,0),q_i0 with eta0=.5/.1m. Hydrostatic reconstruction preserves equilibrium over this represented piecewise-constant bed; this differs from directly averaging depth over the continuous bed.
- [SWASHES steady flow: subcritical Bernoulli root](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Use g9.81,[0,25]m, the parabolic bed, discharge q4.42m²/s and downstream depth2m. Independently bisect the subcritical root of h+z+q²/(2gh²)=2+q²/(8g) and qualify cell quadrature. PDE runs on100/200/400cells start from the steady reference and advance to t2; they do not reproduce the original rest-to-steady transient.
- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en>)
  reference_kind: analytic

  Analytic reference Flat frictionless[-10,10]m, dam x00,hL1m/hR0,zero initial velocity,g9.81,t.5s. Split conserved(h,hu) cell means at the rarefaction head−sqrt(g)t and genuine dry front2sqrt(g)t. Separately track the fixed depth.001m contour. These dedicated gravity/domain/time inputs differ from the historical card, whose values remain unchanged.
- [SWASHES topographic flow: lakes and nonzero steady discharge — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-validation>)

  Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.
- [Lake at rest: wet and emerged equilibrium over represented bed](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lake-at-rest-bed-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Use g9.81,[0,25]m and200cells. Represent z=.2−.05(x−10)² on8<x<12 by split Gauss8 cell means, initializing h_i=max(eta0−z_i,0),q_i0 with eta0=.5/.1m. Hydrostatic reconstruction preserves equilibrium over this represented piecewise-constant bed; this differs from directly averaging depth over the continuous bed. Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
- [SWASHES steady flow: subcritical Bernoulli root](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swashes-bernoulli-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Use g9.81,[0,25]m, the parabolic bed, discharge q4.42m²/s and downstream depth2m. Independently bisect the subcritical root of h+z+q²/(2gh²)=2+q²/(8g) and qualify cell quadrature. PDE runs on100/200/400cells start from the steady reference and advance to t2; they do not reproduce the original rest-to-steady transient. Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.
- [Dry-bed dam break: actual wetting and dry states — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en#dry-bed-dam-break-en-validation>)

  Record all FE minima, newly wetted and remaining dry cells, boundary-aware mass/momentum budgets, and L1 refinement. Split Gauss8 h/hu references are qualified by Gauss16, mass and PDE identities. Diagnose the rightmost cell center with mean h>=.001m. Depth acceptance uses the original fixed5m2 reference mass, preventing domain extension from weakening the criterion; full-domain relativeL1 remains a separate diagnostic.
- [Ritter dry-bed dam break: dedicated g9.81 cell-mean reference](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ritter-dry-bed-en>)
  relation: same-problem
  reference_kind: analytic

  Analytic reference Flat frictionless[-10,10]m, dam x00,hL1m/hR0,zero initial velocity,g9.81,t.5s. Split conserved(h,hu) cell means at the rarefaction head−sqrt(g)t and genuine dry front2sqrt(g)t. Separately track the fixed depth.001m contour. These dedicated gravity/domain/time inputs differ from the historical card, whose values remain unchanged. The .001m mean-depth contour differs from the analytic support edge, which is reported separately. These fixed runs test wetting of initially dry cells. Retreating shorelines, re-drying cycles, real floods, friction and moving fronts over topography are outside scope. The initial100/200/400-cell [-5,5]m attempt passed28 tests and105/109 gates; three retained-dry-cell gates and the .3960m>.25m contour error failed. All original records remain archived; revision2 enlarges/refines the input without changing acceptance. Revision2 then stopped on a binary64 subnormal-tail dry-momentum artifact. Revision3 factors the same HLL update into water packets and adds three regression/equivalence tests; the original28 remain unchanged.
- [Shallow water / dry-bed fan](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dry-bed-en>)
  relation: related-model
  reference_kind: analytic

  Analytic reference Flat bottom; constant g; dry states allowed in the reference only, not the existing FV solver. Retain the historical dry-bed reference gravity/domain/time unchanged. The new g9.81,[-10,10],t.5 computation uses its dedicated Ritter reference.

## Code and validation

- [SWASHES topographic flow: lakes and nonzero steady discharge](<https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en>)
  availability: run

  Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.
- [Dry-bed dam break: actual wetting and dry states](<https://hrkoyama.github.io/numerical-methods-atlas/validation/dry-bed-dam-break/?lang=en>)
  availability: run

  Start the right half at exactly h=q=0 and compare wetting-front advance, conservation and conservative errors with the Ritter analytic solution.
