# Sod shock tube: Godunov-type update and self-similar reference / Sod衝撃波管：Godunov型更新と自己相似解

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: sod

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

Sod衝撃波管を自己相似Riemann解と比べ、密度誤差の減少・正値性・境界流束を含む収支を確認する。

**使用手法**

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) (`godunov`)
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=ja) (`hllc`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-sod-ja)

x=0.5の不連続、[0,1]の流出境界、t=0.2。Godunov型有限体積更新の数値流束は近似HLLC。参照は別の自己相似Riemann式で、星領域圧力には数値求根を使う。

$$
U_t+F(U)_x=0,\quad U=(\rho,\rho v,E)^{\mathsf T},\quad p=(\gamma-1)\left(E-\frac{\rho v^2}{2}\right)
$$

$$
(\rho,v,p)_L=(1,0,1),\quad(\rho,v,p)_R=(0.125,0,0.1),\quad\gamma=1.4
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

**問題の図**

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja#sod-ja-validation)

細格子160セルの各中心でρ,u,pと同位置・同時刻の参照値を併記。初期値も点サンプルをセル値として与える既存solverを使う。解析的な波構造を使うが、圧力根の数値評価を含み、別コードベースとの独立照合ではない。

- [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja) (`euler-sod`; 関連モデルの参照 · 半解析参照)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。


### scope

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。

### assumptions

理想気体、1次元一様格子、正の密度・圧力、CFL=0.3。名付き標準問題の物理定義はJSONに明示し、異なる定義は拒否する。参照の圧力は既存exact_eulerの区間二分法で評価する。Godunov原報の厳密Riemann一段更新そのものではない。

### units

密度・速度・圧力・長さ・時間は無次元。エネルギーはE=p/(γ−1)+ρu²/2。

### boundaries

両端は端値外挿。波が端へ達しないt≤0.2を対象に、総量変化からT(F_left−F_right)を引く。初速0でも圧力差により全運動量は変化する。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json
Input SHA-256: 45fe724864902d9314398b9a41c7300651a624570390dcbb505295c4cb46141f
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/sod.json --output output-sod
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/solution.csv

細格子160セルの各中心でρ,u,pと同位置・同時刻の参照値を併記。初期値も点サンプルをセル値として与える既存solverを使う。解析的な波構造を使うが、圧力根の数値評価を含み、別コードベースとの独立照合ではない。

### Numerical acceptance

- riemann-error / 自己相似Riemann解に対する密度L1標本誤差が0.035未満（既存Sod検査と同じ基準）。: /metrics/density_l1_error_fine; value ≤ 0.035
- refinement / 80→160セルで密度誤差が15%以上減る（既存検査の基準）。: /metrics/fine_to_coarse_error_ratio; value ≤ 0.85
- positive-density / 最小密度が正である。: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / 最小圧力が正である。: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / 遠方の物理境界流束を差し引いた相対収支誤差。: /metrics/physical_boundary_balance_relative_defect; value ≤ 1e-10
- reached-time / 指定した終端時刻まで進んだ。: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = 45fe724864902d9314398b9a41c7300651a624570390dcbb505295c4cb46141f
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

密度誤差0.035と誤差比0.85は既存Sodテストの80/160セル基準を引き継ぐ。CSVの参照はセル中心で評価した自己相似解との標本比較で、厳密セル平均との誤差ではない。全問題での正値性・エントロピー保証、真空、非理想気体や原報の全計算再現は含まない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/

### References

- 細格子160セルの各中心でρ,u,pと同位置・同時刻の参照値を併記。初期値も点サンプルをセル値として与える既存solverを使う。解析的な波構造を使うが、圧力根の数値評価を含み、別コードベースとの独立照合ではない。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json
- Sod衝撃波管の比較課題の出典。参照は本配布版の理想気体Riemann評価であり、原論文の数値表の転記ではない。: https://doi.org/10.1016/0021-9991(78)90023-2
- HLLCの接触波復元の原報。公開実装ではDavis型外側波速を用いる。: https://doi.org/10.1007/BF01414629

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compare the Sod shock tube with a self-similar Riemann solution; check decreasing density error, positivity and boundary-flux balances.

**Methods used**

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) (`godunov`)
- [HLLC](https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/?lang=en) (`hllc`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-sod-en)

Jump at x=0.5, outflow boundaries on [0,1], t=0.2. Godunov-type finite volumes use approximate HLLC fluxes. The separate self-similar Riemann reference uses numerical root finding for star pressure.

$$
U_t+F(U)_x=0,\quad U=(\rho,\rho v,E)^{\mathsf T},\quad p=(\gamma-1)\left(E-\frac{\rho v^2}{2}\right)
$$

$$
(\rho,v,p)_L=(1,0,1),\quad(\rho,v,p)_R=(0.125,0,0.1),\quad\gamma=1.4
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

**Problem figure**

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en#sod-en-validation)

Each of the 160 fine-grid centers carries ρ,u,p and reference values at the same time/location. The existing solver also initializes its cell values from point samples. Wave structure is analytic but reference pressure requires a numerical root; this is not a cross-check against an independent codebase.

- [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en) (`euler-sod`; Related-model reference · Semi-analytic reference)

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.


### scope

Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.

### assumptions

Perfect gas, one-dimensional uniform grid, positive density/pressure and CFL=0.3. The named benchmark's physical definition is explicit in JSON; incompatible definitions are rejected. Reference pressure is evaluated by the existing exact_euler bracketed bisection. This is not the original exact-Riemann one-step Godunov algorithm.

### units

Density, velocity, pressure, length and time are nondimensional. Energy is E=p/(γ−1)+ρu²/2.

### boundaries

Edge-extrapolated boundaries. For t≤0.2, before the wave fan reaches the ends, subtract T(F_left−F_right) from integral changes. Unequal pressures cause a nonzero total-momentum change despite zero initial velocity.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json
Input SHA-256: 45fe724864902d9314398b9a41c7300651a624570390dcbb505295c4cb46141f
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/sod.json --output output-sod
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/solution.csv

Each of the 160 fine-grid centers carries ρ,u,p and reference values at the same time/location. The existing solver also initializes its cell values from point samples. Wave structure is analytic but reference pressure requires a numerical root; this is not a cross-check against an independent codebase.

### Numerical acceptance

- riemann-error / Density L1 sample error against the self-similar Riemann solution is at most 0.035, matching the existing Sod-test criterion.: /metrics/density_l1_error_fine; value ≤ 0.035
- refinement / Density error decreases by at least 15% from 80 to 160 cells, following the existing test criterion.: /metrics/fine_to_coarse_error_ratio; value ≤ 0.85
- positive-density / Minimum density remains positive.: /metrics/minimum_density; value ≥ 1e-08
- positive-pressure / Minimum gas pressure remains positive.: /metrics/minimum_pressure; value ≥ 1e-08
- boundary-balance / Relative integral balance defect after subtracting physical far-field boundary fluxes.: /metrics/physical_boundary_balance_relative_defect; value ≤ 1e-10
- reached-time / The requested final time is reached.: /metrics/final_time_error; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = 45fe724864902d9314398b9a41c7300651a624570390dcbb505295c4cb46141f
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Density-error 0.035 and error-ratio 0.85 thresholds follow the existing 80/160-cell Sod test. CSV comparisons use the self-similar reference sampled at cell centers, not exact cell-average errors. No all-problem positivity/entropy guarantee, vacuum/nonideal-gas support or reproduction of all original experiments is claimed.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/

### References

- Each of the 160 fine-grid centers carries ρ,u,p and reference values at the same time/location. The existing solver also initializes its cell values from point samples. Wave structure is analytic but reference pressure requires a numerical root; this is not a cross-check against an independent codebase.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/sod/result.json
- Benchmark provenance for the Sod shock tube. The reference uses the edition's ideal-gas Riemann evaluator, not transcribed paper tables.: https://doi.org/10.1016/0021-9991(78)90023-2
- Original HLLC contact-restoration paper; the released implementation uses Davis-type outer speeds.: https://doi.org/10.1007/BF01414629

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
