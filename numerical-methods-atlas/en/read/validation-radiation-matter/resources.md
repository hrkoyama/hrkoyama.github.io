# Non-equilibrium radiation: distinct diffusion and transport

Resources for this chapter

https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/

Resources explicitly registered to the methods, problems and executions of this chapter. Separate Su-Olson diffusion and transport by normalization,boundaries and sources,with an additional matched periodic Fourier control for the resolved diffusion limit.

## Methods

- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)

  Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)

  Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)

  Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

  Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.
- [Radiation transport and moment methods](<https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en>)
- [Backward Euler](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en>)
- [Upwind finite differences](<https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en>)
- [Heun / SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en>)

## Equations

- [Su–Olson1996 non-equilibrium diffusion and material exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en>)

  x=sqrt(3)kappa*z,distinct from x=kappa*z in1997 transport. Boundary data and references remain separate; non-unit-epsilon closed cells are separate controls. Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.
- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa. The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries. The main benchmark uses1997-type radiation/material transport. The heat equation is a limiting companion for separate periodic Fourier controls with E approximately V and diffusivity1/[3kappa(epsilon+1)],not the1996Marshak boundary problem or an exact solution of full transport.
- [Static grey radiative transfer,scattering and linear exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-transfer-en>)

  Use a normalized angular mean. Material exchange is evolved in the1997 transport example and periodic Fourier controls. The1997 optical coordinates give a unit exchange coefficient; physical-coordinate controls multiply both exchange terms by kappa.
- [Su–Olson1996 non-equilibrium diffusion and material exchange](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en>)

  x=sqrt(3)kappa*z,distinct from x=kappa*z in1997 transport. Boundary data and references remain separate; non-unit-epsilon closed cells are separate controls.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-algorithm>)

  Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.
- [This execution’s formulation and conditions](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-algorithm>)

  Full signed-angle upwind FV/SSPRK2 advancesIandV. WithI=2U,E=halfangularintegral,the weightedbudgetisepsilonE+V;nodiffusionsubstitution. Only the thick-limit control constructs the same upwind operator from actual real cos/sin responses and evolves one Fourier mode by an exact-time matrix exponential.
- [Heat / diffusion equation](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en>)

  A representative constant-diffusivity form: mode decay, time integration and boundaries.

## Problem figures

- [Su–Olson1996 non-equilibrium diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png
- [Su–Olson transport with an independently published analytical table](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en>)

  Representative test-problem figure; the problem page records conditions and provenance.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997-preview.png
- [Su–Olson1996 non-equilibrium diffusion](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996.png
- [Su–Olson transport with an independently published analytical table](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png>)

  The saved validation figure for this execution itself.

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-transport1997.png

## Exact / reference solutions

- [Su–Olson1996 non-equilibrium diffusion — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#references-en>)

  The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.
- [Su–Olson1996 diffusion: pinned independent integral evaluator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Half-space Marshak diffusion with zero initial radiation/material variables and epsilon1. Direct dimensionless evaluator; no ambiguous physical mass-opacity wrapper convention. This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.
- [Su–Olson transport with an independently published analytical table — references and comparison conditions](<https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-transport1997/?lang=en#references-en>)

  Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.
- [Su–Olson transport: primary2023author-provided analytical benchmark data](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Infinite symmetric1D angular transport/material exchange,epsilon1,no elastic scattering,cold initial state. Source Q1 for |x|<.5 and0<tau<10. Primary half-domain uses reflecting left and distant incoming-vacuum right; comparison times precede boundary influence. A separate matched periodic cell-mean companion uses physical x in [0,2*pi), c=epsilon=1, kappa4/8/16, N128/512/2048, Q0, initial I=V=1+.1cos(x), and t=kappa*s for s=0,.0625,.125,.25. Its IC/BC/source differ from the source-driven1997 benchmark; the FV, continuum-angular and diffusion comparisons within this companion use matched inputs. No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.
- [Su–Olson1996 diffusion: pinned independent integral evaluator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en>)
  reference_kind: semi-analytic

  Semi-analytic reference Half-space Marshak diffusion with zero initial radiation/material variables and epsilon1. Direct dimensionless evaluator; no ambiguous physical mass-opacity wrapper convention.
- [Su–Olson transport: primary2023author-provided analytical benchmark data](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en>)
  reference_kind: numerical-reference

  Finite-grid numerical reference Infinite symmetric1D angular transport/material exchange,epsilon1,no elastic scattering,cold initial state. Source Q1 for |x|<.5 and0<tau<10. Primary half-domain uses reflecting left and distant incoming-vacuum right; comparison times precede boundary influence. A separate matched periodic cell-mean companion uses physical x in [0,2*pi), c=epsilon=1, kappa4/8/16, N128/512/2048, Q0, initial I=V=1+.1cos(x), and t=kappa*s for s=0,.0625,.125,.25. Its IC/BC/source differ from the source-driven1997 benchmark; the FV, continuum-angular and diffusion comparisons within this companion use matched inputs.
- [Su–Olson1996 non-equilibrium diffusion — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-validation>)

  The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.
- [Su–Olson1996 diffusion: pinned independent integral evaluator](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en>)
  relation: same-problem
  reference_kind: semi-analytic

  Semi-analytic reference Half-space Marshak diffusion with zero initial radiation/material variables and epsilon1. Direct dimensionless evaluator; no ambiguous physical mass-opacity wrapper convention. This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.
- [Su–Olson transport with an independently published analytical table — references and checks](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en#su-olson-transport1997-en-validation>)

  Fiveprimaryrunsseparatespace,32/64angles,timeandindependentW/Verrors. Finite/causalzero/homogeneousanalyticsource normalization oftheprovidedtableswerequalifiedbeforemain. A matched-IC/BC/source control separates FV-space,angular and continuum-limit errors against independent continuum angular matrices and analytic diffusion;141 reference checks use GL64/128,exact nonunit-capacity k0 exchange and independent DOP853 before primary mode evaluation.
- [Su–Olson transport: primary2023author-provided analytical benchmark data](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-transport1997-en>)
  relation: same-problem
  reference_kind: numerical-reference

  Finite-grid numerical reference Infinite symmetric1D angular transport/material exchange,epsilon1,no elastic scattering,cold initial state. Source Q1 for |x|<.5 and0<tau<10. Primary half-domain uses reflecting left and distant incoming-vacuum right; comparison times precede boundary influence. A separate matched periodic cell-mean companion uses physical x in [0,2*pi), c=epsilon=1, kappa4/8/16, N128/512/2048, Q0, initial I=V=1+.1cos(x), and t=kappa*s for s=0,.0625,.125,.25. Its IC/BC/source differ from the source-driven1997 benchmark; the FV, continuum-angular and diffusion comparisons within this companion use matched inputs. No direct original1997fulltext/tablecomparison claim. TheauthorREADMEdoesnotstate transcriptionversusregeneration. Source-offprofiles,generalscattering,globalcontinuumerrorandangularorderarenotcertified. The addition is a resolved N~kappa^2 semidiscrete periodic control,not fixed-grid AP or an SSPRK2 diffusion-time order certificate. Initial F0 versus nonzero Fick flux is retained;limit gates use final s=.25 only. SciPy sparse expm_multiply is shared;DOP853 qualifies the reference propagator.

## Code and validation

- [Su–Olson1996 non-equilibrium diffusion](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en>)
  availability: run

  Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.
- [Su–Olson transport with an independently published analytical table](<https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-transport1997/?lang=en>)
  availability: run

  Evolve actual signed-angle transport/material exchange and compare with pinned analytical benchmark tables provided by the2023primary author.
