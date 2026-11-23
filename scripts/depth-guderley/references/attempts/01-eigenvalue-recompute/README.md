# Guderley pre-collapse reference

The reference uses actual, unchanged LANL ExactPack code at commit
`9bacc477eb791e959c9621e771fc7a725db755fa`. Selected source files, their original
paths/URLs and SHA-256 receipts are in `exactpack-source.json`; the upstream
BSD-3 license is `EXACTPACK-LICENSE.txt`. The original public wrapper and package
initializer/docstring are archived, but the minimal local package initializer does not
import the unavailable full ExactPack `base` package.

`precollapse.py` calls the unchanged `eexp.eexp(3,1.4)` eigenvalue calculation.
It integrates the unchanged `ramsey.g` ODE once with the original pre-collapse
RK45 tolerances and uses its dense output for shell quadrature. It deliberately
avoids the public wrapper's repeated per-point integrations and unnecessary
post-reflection `B` solve. This is an adapter of ExactPack, not an independent
implementation of the semi-analytic solution. The separate HLL/Heun finite-volume
PDE evolution does not use this ODE as its evolution equation.

The exponent conventions are `lambda` in `x=t/r**lambda` and
`alpha=1/lambda` in the shock trajectory. The spherical gamma1.4 table transcribed
in ExactPack gives lambda1.3943607838; its official regression fixture gives
alpha0.717174501. These table/regression comparisons share the same upstream
provenance and are not independent literature transcriptions.

This example uses Lazarus time `t<0`, `Rs=.6*(-t)**alpha`, rho0=1, gamma1.4,
domain `[0,.75]`, and times `[-1,-.85]`. The upstream is cold gas with exactly
zero pressure and velocity, not a vacuum. ExactPack's public time is
`t_C=.750024322*(t+1)` and its focus is at t_C=.750024322; `ramsey.state` returns
fields in its documented Lazarus-time normalization. The comparison calls use
radius `r/.6`, then scale velocity/sound speed by.6 and pressure by.6².

`cell_means` splits each shell at the known shock, integrates conserved states
with spherical weight r² and divides by shell volume. Pressure is then calculated
from the averaged conserved state. It is neither an analytic closed-form shell
mean nor the average of primitive pressure. A plotted radial cross-section of
these fields is a spherical-symmetry visualization, not a2D Cartesian calculation.

Before any reference computation, `pre-reference-contract.json` fixes the exact
sources, eight checks, tolerances and a60second execution bound. Run from the
distribution root:

```sh
python -W error -m references.qualify_reference --output references/qualification.json
```

The qualifier checks the computed exponent, critical-phase residual, integration
completion, cold upstream, strong-shock jumps, eight calls to the original
unchanged `ramsey.state`, and split Gauss16/32 shell means. Actual execution and
its outcome are recorded separately in `qualification.json`. It performs no PDE
evolution and no reflected-shock eigenvalue solve. The main verification's smooth
Euler-substitution and moving-shock checks further qualify its use.

`citations.json` distinguishes actual source inspection from publisher abstracts
and bibliographic records. The original papers were not all read in full; no
source or author claim is inferred from a repository link alone. The post-focus
branch, singular focus, full collapse/reflection, cylindrical geometry and other
gamma values are outside this fixed educational verification.
