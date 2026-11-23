# Shallow-water fixed educational benchmarks

This group contains two independently described cases: `swashes-topography`
(two lake equilibria and one nonzero-discharge steady family) and
`dry-bed-dam-break` (Ritter wetting of an exactly dry downstream bed).
Only these eight 1D fixed calculations and 28 small tests are required.

Use Python 3.10 or newer with the three exact pins in `requirements.txt`:

```sh
python -W error -m pytest -q -p no:cacheprovider
python -W error run.py --input inputs.json --output fresh-results
python plot.py --results fresh-results/result.json --output fresh-results
```

The numerical and test steps share a 120-second group budget in the recorded
execution. Plotting additionally uses Matplotlib 3.9.4. No network or private
checkout is needed. The runner rejects changed scientific files and existing
nonempty output directories. Inputs/acceptance and scientific sources were
hash-frozen before execution in `pre-run-contract.json`; the review describes
what was inspected rather than claiming unexecuted checks have passed.

The equations are h_t+q_x=0 and
q_t+(q²/h+gh²/2)_x=−gh z_x, with q=hu. A shared HLL flux handles dry states
directly. Hydrostatic face reconstruction and side-specific pressure corrections
discretize the bed. Face depth max(0,h+z−z*) is part of this method; the evolved
cell states are never clipped, floored or repaired. Forward Euler at face CFL .4
retains every-step minima and boundary/source impulses.

The 25m SWASHES bump is z=.2−.05(x−10)² on8<x<12 and zero elsewhere. The
represented bed is its Gauss8 cell mean. Lakes at surface .5/.1m use200 cells
and reflecting walls; lake balance is exact for this piecewise-constant bed.
The q=4.42m²/s, downstream h=2m subcritical branch uses100/200/400 cells to2s,
initialized from its exact steady conservative means. At the left boundary
impose q and extrapolate h; at the right impose h and extrapolate q. This
tests finite-time preservation/convergence of moving steady flow; it is not
the paper's rest-to-steady initialization, nor an exact moving-water-balanced
scheme.

The flat dry-bed case uses[−10,10]m, hL=1m/hR=0, x0=0, initially zero velocity,
g=9.81m/s², T=.5s and800/1600/3200 cells with transmissive boundaries. These
explicitly rescaled inputs differ from SWASHES's .005m/6s example. Ritter's
fan edges are−cL t and2cL t. Split Gauss8 h/hu means are compared with
Gauss16, total mass and a finite-difference PDE residual. Numerical front
position means the rightmost cell CENTER with mean h≥.001m; compare against
the analytic .001m contour and retain the analytic zero-depth support edge
separately. No positive thin layer is added. Initially dry cells become wet;
retreating/re-drying shoreline cycles are not part of this test.

Each `field-*.npz` saves edges, represented bed, initial/final/reference states,
five equally spaced time snapshots and reference snapshots, every FE stage's
budget diagnostics and their column names. `result.json` retains every
measurement, every frozen numerical decision, hashes and reference qualification.
The two CSV files provide compact per-grid metrics. `plot.py` reads only these
saved arrays/measurements to make PNG/SVG/PDF and preview PNG outputs.

Limits: first-order 1D inviscid flow, selected fixed inputs; no friction, rain,
infiltration, hydraulic jump, 2D flood validation or fully discrete entropy
claim. New analytic references import no FV code. Neither SWASHES nor FullSWOF
was run and no third-party source was copied. Review scope/URLs and the failed
retrieval of the original HR PDF are recorded under `references/`. Original
software is MIT; prose/data/figures retain the site's separate conditions.

日本語: 地形上の静水2例と非零流量の亜臨界定常流、厳密に乾いた河床への
Ritterダム破壊を分けて検証します。静水の厳密釣合いは表現したセル地形に
対する性質です。動く定常流には有限時刻の誤差が残ります。全更新後の水深、
共有境界流束と地形による運動量の収支、3格子の保存量セル平均誤差を保存し、
状態の切上げや失敗後の許容条件緩和を行いません。前線の.001m診断と厳密な
支持端を区別します。実地洪水・後退汀線・再乾燥周期の検証ではありません。

Initial attempt: 28 tests passed and105/109 numerical gates passed. With the original[-5,5]m domain and100/200/400 grids, arbitrarily tiny positive conservative-stencil tails removed all final exact-zero dry cells, and the finest .001m contour error was0.3960237865001921m against the frozen .25m limit. All original sources, arrays, gates, JUnit and logs are retained under attempts/01, with the archived test filename mapped to prevent duplicate collection. Revision2 uses[-10,10]m and dedicated Ritter800/1600/3200 grids; topography/lakes, acceptance, solver, analytic reference and28tests remain byte-identical. See protocol-history.json and the linked contracts.
