# Variable Eddington controls / 可変エディントン法の固定検証

Two small steady grey periodic controls couple an angular formal solution to independently discretized moment equations: a1D scalar factor and a spatial2D/full-S2 tensor. The prescribed positive sources have independently derived Fourier references. The1D intensity plot uses position and angular cosine, not two spatial coordinates.

小さな定常・灰色の周期問題で、角度輸送と独立なモーメント方程式を反復結合します。1Dは可変因子、空間2Dは全S²角度の3×3テンソルです。参照解を主計算の閉包へ注入しません。

## Fixed scope

Each case has three variable-source rows (two spatial grids and one separate angular probe) and one N=9 constant-source control: eight saved rows total, two scientific cases. Inputs and criteria are declared in `inputs.json`, `acceptance.json` and `PROTOCOL.md`; `freeze.json` binds their reviewed source. Current measured success, versions and timing belong to `results/result.json` and `verification.json`, not this description.

Point values are at i/N; faces are at (i+1/2)/N. Total, scattering and absorption coefficients are4,3,1 in dimensionless units, and c=1. Angle averages are normalized to1. The2D spatial case retains Dzz, although derivatives involve only x,y. Different HO/LO discretizations need not agree exactly at a fixed mesh.

## Reproduce

Use Python3.12 with the exact package versions in `requirements.txt`; plotting additionally uses `requirements-plotting.txt`. A supplied public archive contains its pinned inputs, acceptance criteria and source. From that source directory:

```sh
python -W error -m pytest -q --junitxml=pytest.xml
python -W error run.py --input inputs.json --output results-new
python plot.py --results results-new/result.json --output results-new
```

Use a fresh output directory and single-thread numerical libraries. The fixed cooperative runner limit is90s, owned runner/pytest limits120s and plotting limit45s. An exceeded limit or failed criterion remains a failure; thresholds, seeds and rows are not adjusted automatically. Plotting reads saved NPZ fields and result records only and does not call the solver or reference evaluator.

## Saved evidence and figures

`result.json` contains exact case-ID checks, metrics, fixed-row records and a termination reason; `measurements.csv` provides finite measured values. Each row points to `{caseid}--{rowid}.npz`, preserving angular intensity, moments, tensor, shared face fluxes, references and iteration history. Constant-source rows remain separate from variable-closure rows.

Each case produces `<caseid>.png` plus a distinct `<caseid>-diagnostics.png`. The main1D figure prioritizes actual I(x,mu) and f(x). The main2D figure shows actual E(x,y), explicitly scaled flux arrows and Dxy. Diagnostic plots show saved reference errors, spatial/angular comparisons and iteration history; they do not simulate new rows.

## Limits and references

These are static, homogeneous, steady grey fixed-source controls with periodic boundaries. They do not validate inflow boundary factors, radiation time integration, material/gas coupling, relativistic or moving media, nonlinear FLD, Athena, high-order FEM, universal AP behavior or performance speedup. A pointwise M1 tensor comparison is not an M1 PDE run. The analytic periodic problems are authored controls, not reproductions of paper benchmark tables. `source-reading.json` records selected primary passages and unread limits; the1970 paper was read only at publisher-abstract/bibliography level. Original software is MIT licensed; cited papers retain their own rights.
