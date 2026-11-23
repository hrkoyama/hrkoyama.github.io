# WENO5 critical points and epsilon

This educational finite-volume supplement compares Jiang–Shu weights with WENO-Z weights (power **2**) using exactly the same five cell averages, candidate polynomials and upwind flux. It connects to the existing smooth scalar-advection family; parameter choices are not new physical problems.

Run with Python 3.10+, in a fresh output directory:

```
python -m pip install -r requirements.txt
python -W error -m pytest -q
python -W error run.py --input inputs.json --output output
python -m pip install -r requirements-plotting.txt
python plot.py --results output/result.json --output output
```

The reviewed direct numerical dependencies are NumPy2.0.2, SciPy1.14.1 and pytest8.3.5. SciPy is pinned for compatibility with the public verifier, though this solver/reference uses NumPy only. Matplotlib3.9.4 is a separate plotting dependency. No network, private source, reference PDE engine or heavy parameter scan is needed. The shared pytest plus main runner budget is120 seconds. A4GiB free-space start and2.5GiB running floor are enforced by the runner.

`pre-run-contract.json` binds the exact input, acceptance, solver, analytic reference and tests before the first scientific run. Editing a frozen file is rejected. Failed attempts must be retained with the original contract; numerical tolerances are not fitted to results.

The local study uses three polynomials at cell center x=0: regular x+x²+x³+x⁴+x⁵, first-critical x²+x³+x⁴+x⁵, and second-critical x³+x⁴+x⁵. Analytic means over cells centered at −2h,…,2h are reconstructed at the right interface h/2. Grids64/128/256/512 and epsilon10⁻⁴⁰,10⁻⁶,h² give72 local records. First-critical reconstruction has explicit monotonicity/order/comparison gates. The second-critical class remains a diagnostic; a fifth-order guarantee there is not claimed.

The transport is a genuine periodic finite-volume evolution of q_t+q_x=0 on[0,1], with q₀=cos(2πx)+.1sin³(2πx), unit speed, T=1 and32/64/128 cells. Both schemes use classical RK4 with Courant .1. Six additional finest-grid runs halve dt. Five intermediate/final snapshots test direction and accuracy separately from the full-period return. The exact reference consists of Fourier-antiderivative cell averages, independently checked by Gauss12 integration of the point function. These references are analytic, not independent PDE-software runs. Every RK stage is checked finite; mass histories, stage ranges and shared-flux balance are saved. There is no clipping, positivity correction, retry or universal TVD/SSP claim for RK4/WENO.

`reconstruction.npz` retains every stencil mean, candidate, beta and normalized weight in CSV/result record order. Each transport NPZ contains initial/final/reference fields, all five snapshot fields/references and every step's diagnostics. CSVs, result.json and source/file SHA256 hashes accompany the arrays. `plot.py` verifies these hashes and renders actual saved fields into PNG, SVG and PDF plus a gallery preview.

Borges2008 was checked through the author institution's abstract/bibliography; publisher full text was inaccessible. We do **not** claim a full Borges paper review, its original numerical experiments, or its power-one variant were reproduced. The NASA-hosted Jiang–Shu preprint selected sections1–3 was inspected for candidates, weights, indicators and the distinction between point-value finite differences and cell-mean reconstruction. The finite-volume formulas and Z power parameter were additionally checked in van Lith et al.'s institution-hosted accepted manuscript, section2 equations(2)–(15) and selected section4.2. Only baseline JS/Z are implemented, not that paper's new embedded schemes. No third-party PDF or code is redistributed. See references/source-review.json for the exact source roles and limits.

コードはMIT。新たに生成した入力・数値配列・CSV・図・説明はCC BY4.0。第三者論文は各権利者の条件に従い、本配布へ含めません。小規模な固定入力例であり、Euler/MHD、衝撃波、一般の高次臨界点の精度・安定性を保証しません。
