# True-cold Noh shocks / 真の低温Noh衝撃波

Original educational finite-volume code; edition 2026-11-23-r3. One registered case
`noh-shock` contains planar and cylindrical-radial refinements. It is not two
independent problem discoveries, a Cartesian 2D Euler calculation, or an
independent PDE-engine comparison.

## Run / 実行

Python 3.10+; dependencies are pinned in `requirements.txt`. After installing
them, ordinary execution is offline and needs no ChatGPT/Codex/API key.

```
python -m pip install -r requirements.txt
python -m unittest -v test_noh
python -m pytest -q
python run.py --input inputs.json --output results
```

Rendering saved results additionally needs `requirements-plotting.txt`:

```
python -m pip install -r requirements-plotting.txt
python plot.py --results results/result.json --output results
```

Use a **new output directory**: the runner refuses to overwrite an existing
`results.json`. `results/result.json` is the standard depth-release envelope;
`results/results.json` retains full diagnostics, stage histories and profile
paths. The plotter reads those details without recomputing a numerical solution.
`generate_exactpack_reference.py` is an optional independent-reference generator,
not part of ordinary PDE execution; it needs separately fetched pinned upstream
source, as described in `THIRD_PARTY.md` and its `--help`.

## Fixed physical problem / 固定する物理問題

Dimensionless radius `0 <= r <= 1`; gamma=5/3, rho0=1, u0=-1,
**p0=0 exactly**, final time .6. PDE executions use d=1 (planar) and d=2
(cylindrical-radial), N=64/128/256/512. Angular factors are omitted consistently
from volumes, face areas and all integrals. Cell volumes are
`V=(r_right**d-r_left**d)/d`, areas `A=r**(d-1)` (A=1 for planar).

The center reflects velocity. The outer boundary is prescribed supersonic cold
inflow: rho=(1+t)**(d-1), u=-1, p=0. In cylindrical geometry it is **not** rho=1
held fixed. Its physical inflow flux is imposed at the boundary face and
integrated with the same two SSPRK stages as the state.

C=(gamma+1)/(gamma-1)=4, shock speed=1/3, shock position=.2 at T=.6.
Behind it rho=4**d, u=0, p=4**d/3, specific internal energy=.5. Ahead,
rho=(1+t/r)**(d-1), u=-1, p=0. The jump at the shock is 4 in both geometries;
the amplification relative to initial density is 4 (planar) or 16 (cylindrical).
The cold flow converges inward; the generated shock propagates outward.

## Algorithm and origin treatment / 離散化と原点

Piecewise-constant local Lax–Friedrichs/Rusanov flux, SSPRK2/Heun in time. The
geometric CFL uses `(A_left*a_left+A_right*a_right)/V`, not a Cartesian dx-only
bound. No conservative state or pressure floor, clipping, analytic-array
replacement, or hidden pressure seed is used. Tiny negative internal energy up
to 64 energy-scaled roundoff units is logged rather than repaired; only the
sound-speed square-root argument may use zero at roundoff. Actual cold states
remain exactly cold in the primitive routine.

The radial source is an explicitly documented **interface-stress quadrature**.
For the same numerical flux already used by the update,

```
ubar_f = (u_L+u_R)/2
Pstar_f = Fhat_momentum_f - ubar_f*Fhat_mass_f
S_momentum_i * V_i = (Pstar_left+Pstar_right)/2 * (A_right-A_left)
```

Thus its pressure part simplifies exactly to
`-(A_left+A_right)/2 * (Pstar_right-Pstar_left) / V_i`. This is a consistent
first-order approximation to the pressure gradient, uses the reflection
Riemann stress at the origin, balances static constant pressure exactly, and
vanishes as a geometric source for d=1. For smooth cold constant-velocity
interior flow Pstar=0. The Rusanov numerical stress differs from thermodynamic
cell pressure at finite resolution; it must not be described as exact
integration of p_i or attributed to Noh's original method. No theorem of
positivity or convergence for all radial data is claimed.

## Exact cell means / 厳密セル平均

`noh_reference.py` imports no PDE solver. It analytically splits a cell at the
shock. In cold upstream flow, `rho*r**(d-1)=(r+t)**(d-1)`, so its mass integral
is `((b+t)**d-(a+t)**d)/d`. Momentum comes only from the upstream part. Total
energy is half the total mass in both regions for this input. Integrate these
**conserved quantities** before taking cell means.

`exact_rho`, `exact_momentum`, `exact_total_energy` are true conservative means.
`exact_velocity`, `exact_pressure`, `exact_specific_internal_energy` evaluate
primitives on those conservative means. A shock-crossing cell contains an
unresolved velocity mixture, so `p(mean U)` differs from the physical mean
pressure. The latter is saved separately as `exact_pressure_average`. Profile
comparisons must label that distinction.

LANL ExactPack, independently executed unchanged at commit
`9bacc477eb791e959c9621e771fc7a725db755fa`, cross-checks the analytic reference.
Point samples and Gauss integration split at the shock are saved in
`exactpack-reference-snapshot.json`, with hashes, environment and errors in its
receipt. Geometry-3 analytic checks are **not** a spherical PDE run. ExactPack's
Noh pressure expression is gamma=5/3-specific despite the broader API, so the
independent cross-check is explicitly restricted to gamma=5/3 and rho0=|u0|=1.

## Acceptance and retained failure / 受入条件と初回失敗

`acceptance.json` and `pre-run-contract.json` were written and hashed before the
first numerical execution. All original thresholds are retained. Initial code
used the cell-pressure source p_i*(A_right-A_left). Planar flow passed, but the
area-zero cylindrical origin left constant-velocity cold accumulation and no
stagnation shock. It failed six predeclared gates even though total mass and
energy balanced. That source, inputs, gates and all failed refinement results
are retained under `attempts/attempt-01-cell-pressure/`.

The interface-stress revision was separately executed against **the same**
acceptance file; the revision02 source, receipt and successful result summary
are also retained. Input-schema/output-envelope and finite-input/budget guards
were subsequently added without changing the numerical formula or thresholds.
Final results carry their own complete source hashes.

Full-domain normalized volume-weighted density L1, L2 and Linf are always
reported, as are separate center/shock/plateau masks. Shock location uses the
pressure half-height crossing. Plateau cells lie wholly within .25–.70 times
the exact shock radius. Center cells end at or inside .25 times that radius.
The maximum origin specific internal energy and first-cell values are retained,
with **no accuracy gate that hides persistent center heating**.

At N=512, planar density L1 is approximately .00639 and cylindrical L1 .01868.
Cylindrical plateau density is about 15.36 versus exact 16, shock error about
2.12 cells, and center specific-internal-energy excess about 8.16%. These are
measured finite-grid errors, not claims of exact pointwise behavior or zero
origin error. In particular, unmasked cylindrical density Linf is not
monotonically decreasing in this series (approximately .459 to .579).
The predeclared convergence gate concerns volume-weighted density L1, not
uniform convergence across a discontinuity. All Linf results remain saved.
For this input total mass M(t)=(1+t)**d/d and energy E(t)=M(t)/2;
these analytic inflow totals are checked separately from discrete telescoping
mass/energy balances. Scalar radial momentum includes a geometric source and
is not a conserved Cartesian vector component.

## Provenance / 出典の役割

- W. F. Noh (1987), *Errors for calculations of strong shocks using an artificial
  viscosity and an artificial heat flux*, JCP 72(1), 78–120,
  DOI 10.1016/0021-9991(87)90074-X. Original problem and heating-error analysis;
  publisher metadata/abstract checked, full original text inaccessible (403).
- J. Thrussell and J. M. Ferguson (2023), *ExactPack: A python library of exact
  analytic solutions*, SoftwareX 24, 101560,
  DOI 10.1016/j.softx.2023.101560. Independent reference software, distinct from
  the original Noh problem. Fixed commit and file hashes are in the receipt.

`cases.json` contains bilingual scope/algorithm/validation/limits and the full
bibliographic records. No existing distribution, acceptance tolerance or prior
success record in the Atlas is changed by this new release.
