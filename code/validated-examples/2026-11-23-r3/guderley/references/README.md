# Guderley pre-collapse reference

The reference uses actual, unchanged LANL ExactPack code at commit
`9bacc477eb791e959c9621e771fc7a725db755fa`. Selected source files, their original
paths/URLs and SHA-256 receipts are in `exactpack-source.json`; the upstream
BSD-3 license is `EXACTPACK-LICENSE.txt`. The original public wrapper and package
initializer/docstring are archived, but the minimal local package initializer does not
import the unavailable full ExactPack `base` package.

`precollapse.py` normally reuses the exponent that was actually computed by
unchanged `eexp.eexp(3,1.4)` in the retained original qualification. The cache
`eigenvalue-cache.json` has a literal SHA binding in the adapter. Its loader
checks the original qualification, its pre-execution contract, all twelve
archived source files, fixed geometry/gamma/normalization, and ten unchanged
live upstream/provenance files. The adapter still freshly integrates unchanged
`ramsey.g` with the original pre-collapse RK45 tolerances for dense shell
quadrature. Reusing the exponent does not reuse the finite-volume PDE result.

Full nonlinear exponent shooting was repeated in both pytest and main execution
in the original release. The Linux33-test phase passed but took96.34seconds,
leaving insufficient time for the main run under the unchanged combined120second
group limit. That failed timing record and original source are retained. The
runtime revision reuses completed, hash-qualified eigenvalue work; it changes no
physical input or numerical acceptance threshold. One fresh `critical_phase_residual()`
check uses the original `Cdiff` at the saved alpha, without a root search.

This is an adapter of ExactPack, not an independent implementation of the
semi-analytic solution. The separate HLL/Heun finite-volume PDE evolution does
not use the similarity ODE as its evolution equation. No reflected-shock `B`
solve is required for this pre-collapse branch.

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

The original full-shooting qualification and its unchanged source/contract are
preserved under `attempts/01-eigenvalue-recompute/`. The original eight checks
included eight actual calls to unchanged `ramsey.state`; those successful calls
are historical evidence and are not claimed as new cached-run work.

`cache-contract.json` preregisters the fresh lightweight cache qualification:
receipt/source checks, one actual critical-phase evaluation, fresh dense ODE,
eight comparisons against the archived original state values, and fresh
Gauss16/32 shell integration. Its result is `cache-qualification.json`:

```sh
python -W error -m references.qualify_cached_reference --output references/cache-qualification.json
```

The original root-shooting path remains available as a separate explicit
regeneration command; it is not called by routine pytest or PDE execution:

```sh
python -W error -m references.qualify_reference --recompute-eigenvalue --output new-full-reference-qualification.json
```

This command recomputes the exponent and repeats the original eight state calls.
It belongs to separate reference regeneration, outside the routine combined
120second group verification. The original contract/time receipts describe the
actual earlier run and are not rewritten to claim the full work was repeated.

`citations.json` distinguishes actual source inspection from publisher abstracts
and bibliographic records. The original papers were not all read in full; no
source or author claim is inferred from a repository link alone. The post-focus
branch, singular focus, full collapse/reflection, cylindrical geometry and other
gamma values are outside this fixed educational verification.
