# moving-waves fixed lightweight PDE cases

Run Python3.10+ with the exact3pins in requirements.txt.

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

Tests and all fixed inputs share one120second group budget. No network/private source is required. The runner rejects changed frozen sources and nonempty output. plot.py reads only saved arrays; it needs Matplotlib3.9.4. NPZ files retain actual grid/fields/reference and stage or face budgets; CSV/result.json retain every decision. PNG/SVG/PDF and preview PNGs are generated from those arrays.

The bilingual cases.json is the detailed model/input/algorithm/reference/limits specification. Selected primary/official source review scopes are under references/. All MMS and numerical code are newly implemented, without copied third-party code. An analytic qualification or same-matrix alternative solve is not an independent PDE engine.

Current cases:
- ale-nonuniform-transport: Periodic unit interval, speed.7,q0=1+.2sin(2pi x), grid speed .2sin(2pi xi)cos(2pi t),N40/80/160,T1. Separate N40,T.25 time series32/64/128steps. First-stage1D prescribed mesh motion. The x–t image is not2D physics; Euler Lagrange/remap and Saltzman piston remain future work.
- cgrid-rotating-wave: Linear f-plane,g=H=f=1, periodic unit square, mode(1,2),height amplitude.01,N16/32/64,T.5. Separate N16 time refinement, zero-mode and discrete geostrophic probes. Linear planar periodic square only. Nonlinear SWE,PV,spherical dynamics and Williamson tests remain future work.

No original acceptance values or existing releases are changed. MIT applies only to original implementation code; site rights apply separately to prose/inputs/figures.

Executed frozen revision2 once:19/19 pytest and98/98 numerical gates across15 actual evolutions passed within1.527seconds combined. The independent review and execution receipts are retained. The plot-only warnings-as-errors import attempt is separately recorded; plotting then used the documented command. No scientific rerun or acceptance change was needed.
