# Restricted SRHD collision and nonlinear SRMHD Alfvén wave

Two small one-dimensional examples share a real seven-variable ideal-RMHD finite
volume solver. U=(D,Sx,Sy,Sz,E,By,Bz), with fixed normal Bx and E including rest mass.
The B=0 specialization is relativistic hydrodynamics. The nonzero-B case evolves
the complete magnetic stress, momentum, energy and induction; it is not passive
transport. Units are c=4π=1 and the gamma-law EOS is used.

The method uses primitive MUSCL reconstruction with componentwise minmod slopes,
the HLL flux with conservative causal bounds −1,+1, and SSPRK(3,3), CFL.35. These
bounds are intentionally diffusive. A safeguarded scalar Z=rho h W² Newton root
recovers primitives, checked by the physical residual and full conserved-state
roundtrip. Safeguarding changes algebraic root trials only. No density/pressure
floor, evolved-state clipping, rejected step or PDE retry is implemented.

Fixed inputs are three collision grids96/192/384 to t=.3 and three periodic-wave
grids32/64/128 to one period. The collision is a custom mild rho1,p.1,v±.3, gamma5/3
two-shock case, with matching resting star states. The wave follows the exact
finite-amplitude ECHO §4.1 family rho=p=B0=eta1, gamma4/3, rescaled to a unit period.
Neither example validates a generic RMHD Riemann solver, arbitrary EOS, extreme
Lorentz factors, general relativity, divergence control in multiple dimensions,
or interacting transverse shocks.

`inputs.json`, `acceptance.json`, the independent reference, solver, driver and
25 tests are hashed in `pre-run-contract.json` before their first execution.
The group has six fixed FV runs and 110 case acceptance gates, plus six analytic
reference qualifiers. The pytest and main runner share a measured 120-second
deadline. Plotting is separate. Full logs and the combined timing receipt record
what was actually rerun; this paragraph is a protocol, not a claim of an unrun pass.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output results
python -m pip install -r requirements-plot.txt
python plot.py --results results
```

Each run stores initial/final conserved states, exact reference means, five
numerical/reference snapshots, cell centers/edges, every SSP-stage admissibility
and recovery record, and all-seven-component integrated boundary budgets. There
are three operator-stage records and one completed-state record per step; face
diagnostics in that last record repeat the third operator's reconstructed faces.
They do not pretend to be an extra reconstruction. The collision uses constant
extrapolation endpoints before its shocks arrive and measures the resulting
nonzero boundary mass/energy influx. The periodic wave conserves all seven totals.
Bx is a fixed one-dimensional parameter, so ∂xBx=0 structurally; this is not a
multidimensional magnetic-divergence benchmark.

Main PNG/SVG/PDF figures show actual x–t fields from five saved times, final exact
cell-mean overlays, refinement errors and stage diagnostics. Gallery previews are
explicitly labeled one-dimensional x–t diagrams. See `references/README.md` for
primary-source reading scope, normalization and independent checks.
