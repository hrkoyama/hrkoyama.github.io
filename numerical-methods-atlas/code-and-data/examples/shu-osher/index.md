# Shu–Osher: characteristic WENO-Z and a numerical reference / Shu–Osher：特性WENO-Zと高解像度参照

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: shu-osher

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

衝撃波と密度波の相互作用を計算し、100/200点解と800点の同一手法による数値参照との差を確認する。

**使用手法**

- [有限差分WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja) (`weno-z`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-shu-osher-ja)

初期不連続x=−4、左状態は固定入力を参照。特性有限差分WENO5-Zの点値を比較する。800点参照は同一方式の数値解であり、厳密解・独立ソルバーではない。

$$
U_t+F(U)_x=0,\qquad \gamma=1.4,\qquad -5\leq x\leq5
$$

$$
\rho_R(x,0)=1+0.2\sin(5x),\quad v_R=0,\quad p_R=1,\qquad t_{\rm final}=1.8
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

**問題の図**

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja#shu-osher-ja-validation)

高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。


### scope

[-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。

### assumptions

γ=1.4、初期不連続x=−4、左(ρ,u,p)=(3.857143,2.629369,10.33333)、右ρ=1+0.2sin(5x),u=0,p=1。初期不連続を各格子の界面へ合わせる。点値FD、大域LF分割、界面固定Roe特性基底、WENO-Z指数2、ε=10^-6、SSPRK3、CFL=0.3。

### units

長さ・時間・Euler変数は無次元。固定εはこの無次元流束の尺度に対する値で、任意単位系へ自動転用しない。

### boundaries

端点初期値を固定したゴースト値。連続の遠方流束を差し引いた収支には、静止した非一様密度を固定ゴーストで扱うFD境界離散化誤差が残る。丸め誤差保存とは区別する。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json
Input SHA-256: 302a761bb5cd20d049999da230eda0b873daaed9cafefafc7779374b6210accf
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/shu-osher.json --output output-shu-osher
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/solution.csv

高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。

### Numerical acceptance

- numerical-reference-error / 800点の同一手法の数値参照に対する平均密度差が0.15以下。厳密解誤差ではない。: /metrics/density_l1_error_fine; value ≤ 0.15
- empirical-refinement / 100→200点で高解像度参照との差が減る。収束次数は主張しない。: /metrics/fine_to_coarse_error_ratio; value ≤ 0.95
- positive-density / 最小密度が正である。: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / 最小圧力が正である。: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / 物理境界流束に対する近似収支を0.2%以内にする。固定ゴーストのFD境界離散化誤差を含み、丸め誤差保存を主張しない。: /metrics/physical_boundary_balance_relative_defect; value ≤ 0.002
- reached-time / 指定した終端時刻まで進んだ。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 302a761bb5cd20d049999da230eda0b873daaed9cafefafc7779374b6210accf
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

800点は同一手法の数値参照で、厳密解や独立solverではない。0.15の平均密度差は構造の再現を見る教材用の解像度基準であり、高精度認証ではない。格子倍増で差が減ることだけを判定し、形式次数は付与しない。正の出力と棄却回数を記録しても、全入力の正値性定理にはならない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/

### References

- 高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json
- Shu–Osher干渉問題の歴史的な原報。原図のデジタイズや厳密解の再現を主張しない。: https://doi.org/10.1016/0021-9991(89)90222-2
- 既存台帳で採用している初期値の参照先（§3.1.5）。quokkaコードやAMR機構は利用しない。: https://doi.org/10.1093/mnras/stac439
- WENO-Zの原報。局所実装のp=2、ε、流束分割・基底・時間積分は別に明示する。: https://doi.org/10.1016/j.jcp.2007.11.038

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compute shock–density-wave interaction and compare 100/200-point solutions with an 800-point same-method numerical reference.

**Methods used**

- [FD WENO5-Z](https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=en) (`weno-z`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-shu-osher-en)

Initial jump at x=−4; see the fixed input for the left state. Compares characteristic finite-difference WENO5-Z point values. The 800-point reference is neither exact nor an independent solver.

$$
U_t+F(U)_x=0,\qquad \gamma=1.4,\qquad -5\leq x\leq5
$$

$$
\rho_R(x,0)=1+0.2\sin(5x),\quad v_R=0,\quad p_R=1,\qquad t_{\rm final}=1.8
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

**Problem figure**

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en#shu-osher-en-validation)

Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.


### scope

Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.

### assumptions

γ=1.4, initial jump x=−4, left (ρ,u,p)=(3.857143,2.629369,10.33333), and right ρ=1+0.2sin(5x), u=0, p=1. The initial jump aligns with a face on every grid. Pointwise FD, global LF splitting, face-frozen Roe characteristics, WENO-Z exponent 2, ε=10^-6, SSPRK3 and CFL=0.3 are used.

### units

Length, time and Euler variables are nondimensional. Fixed ε refers to this nondimensional flux scaling and is not automatically transferable to arbitrary units.

### boundaries

Ghost values are fixed to initial endpoint states. Balance against continuous far-field fluxes retains FD boundary discretization error for the nonuniform stationary density with fixed ghosts; this is distinct from roundoff conservation.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json
Input SHA-256: 302a761bb5cd20d049999da230eda0b873daaed9cafefafc7779374b6210accf
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/shu-osher.json --output output-shu-osher
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/solution.csv

Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.

### Numerical acceptance

- numerical-reference-error / Mean density disagreement with the same-method 800-point numerical reference is at most 0.15; this is not exact-solution error.: /metrics/density_l1_error_fine; value ≤ 0.15
- empirical-refinement / The discrepancy with the higher-resolution reference decreases from 100 to 200 points; no convergence order is claimed.: /metrics/fine_to_coarse_error_ratio; value ≤ 0.95
- positive-density / Minimum density remains positive.: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / Minimum gas pressure remains positive.: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / Approximate physical-flux balance remains within 0.2%; fixed-ghost FD boundary discretization error is included, so roundoff conservation is not claimed.: /metrics/physical_boundary_balance_relative_defect; value ≤ 0.002
- reached-time / The requested final time is reached.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 302a761bb5cd20d049999da230eda0b873daaed9cafefafc7779374b6210accf
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

The 800-point solution is a same-method numerical reference, not an exact solution or independent solver. The mean-density difference bound of 0.15 is an educational structure-resolution criterion, not a high-accuracy certification. Only decreasing discrepancy under grid doubling is tested; no formal order is assigned. Positive outputs and counted rejections do not establish positivity for every input.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/

### References

- Higher-resolution conserved point values are linearly interpolated to each 100/200-point grid's centers. Errors are averaged at matching locations and t=1.8; CSV pairs the 200-point solution and reference. The 0.2% approximate-balance allowance accommodates fixed-boundary discretization and is separate from the density-error bound of 0.15.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/shu-osher/result.json
- Historical source for the Shu–Osher interaction problem; no original-figure digitization or exact-solution reproduction is claimed.: https://doi.org/10.1016/0021-9991(89)90222-2
- Existing catalog's adopted initial-condition source (§3.1.5); neither the quokka code nor its AMR machinery is used.: https://doi.org/10.1093/mnras/stac439
- Original WENO-Z paper; local p=2, ε, splitting, basis and time integration are stated separately.: https://doi.org/10.1016/j.jcp.2007.11.038

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
