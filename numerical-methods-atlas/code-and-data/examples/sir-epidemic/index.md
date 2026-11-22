# SIR: independent DOP853 reference, conservation and convergence / SIR：独立DOP853参照・人口保存・収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: sir-epidemic

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-sir-epidemic-ja)

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

$$
\dot S=-\beta SI,\quad\dot I=\beta SI-\gamma I,\quad\dot R=\gamma I
$$

$$
S+I+R=1
$$

- [SIR・SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-sir-ja) (`bio-sir`)

**問題の図**

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[SIR：独立DOP853参照・人口保存・収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja) (`sir-epidemic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=ja#sir-epidemic-ja-validation)

別実装DOP853と2段階許容誤差の比較。解析解ではありません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。


### scope

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

### assumptions

閉鎖・均質な人口割合SIR。RK4と別実装のSciPy DOP853を比較。人口保存・非負性・時間収束を確認。SEIR・空間伝播・実データ較正は対象外。

### units

全変数・係数・時間は入力JSONに定めた無次元値。SIRは人口の割合。

### boundaries

空間境界なし。初期値・時間区間／積分区間・標本数・seedは入力に固定。

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json
Input SHA-256: bff023a3ec9c4cfc6788a6a78279ee68e851cca0b6080d35d92d3208f6c52327
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/sir-epidemic.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/solution.csv

### Numerical acceptance

- all-numerical-checks / 入力で定めた全数値条件: /checks; all values = true
- input-provenance / 入力ハッシュ: /input_sha256; value = bff023a3ec9c4cfc6788a6a78279ee68e851cca0b6080d35d92d3208f6c52327
- termination / 固定予算による正常終了: /termination; value = fixed_budget_completed
- finest_max_error-maximum / finest_max_error（固定入力の条件）: /metrics/finest_max_error; value ≤ 2e-06
- observed_orders-minimum / observed_orders（固定入力の条件）: /metrics/observed_orders; value ≥ 3.7
- mass_balance_max-maximum / mass_balance_max（固定入力の条件）: /metrics/mass_balance_max; value ≤ 2e-13

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#05-1927-sir-and-seir-compartment-models

### References

- 既存の解説章に出典と確認範囲を記載。論文本文は配布しません。: https://doi.org/10.1098/rspa.1927.0118
- 別実装DOP853と2段階許容誤差の比較。解析解ではありません。: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/references/sir.json

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-sir-epidemic-en)

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

$$
\dot S=-\beta SI,\quad\dot I=\beta SI-\gamma I,\quad\dot R=\gamma I
$$

$$
S+I+R=1
$$

- [SIR and SEIR compartment models](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-sir-en) (`bio-sir`)

**Problem figure**

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/preview.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[SIR: independent DOP853 reference, conservation and convergence](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en) (`sir-epidemic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sir-epidemic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sir-epidemic/?lang=en#sir-epidemic-en-validation)

Separately implemented DOP853 with two-tolerance agreement; not an analytic solution.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.


### scope

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

### assumptions

Closed homogeneous population-fraction SIR. Compare RK4 with independently implemented SciPy DOP853; check conservation, nonnegativity and time convergence. Excludes SEIR, spatial spread and calibration to observations.

### units

Dimensionless variables, coefficients and time as specified in input JSON; SIR uses population fractions.

### boundaries

No spatial boundary. Initial values, time/integration interval, sample counts and seeds are fixed in the input.

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/sir-epidemic.json
Input SHA-256: bff023a3ec9c4cfc6788a6a78279ee68e851cca0b6080d35d92d3208f6c52327
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/sir-epidemic.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/sir-epidemic/solution.csv

### Numerical acceptance

- all-numerical-checks / All numerical conditions fixed by the input: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = bff023a3ec9c4cfc6788a6a78279ee68e851cca0b6080d35d92d3208f6c52327
- termination / Completed fixed computation budget: /termination; value = fixed_budget_completed
- finest_max_error-maximum / finest_max_error (fixed-input criterion): /metrics/finest_max_error; value ≤ 2e-06
- observed_orders-minimum / observed_orders (fixed-input criterion): /metrics/observed_orders; value ≥ 3.7
- mass_balance_max-maximum / mass_balance_max (fixed-input criterion): /metrics/mass_balance_max; value ≤ 2e-13

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#05-1927-sir-and-seir-compartment-models

### References

- The existing reading chapter documents sources and review depth. Paper text is not redistributed.: https://doi.org/10.1098/rspa.1927.0118
- Separately implemented DOP853 with two-tolerance agreement; not an analytic solution.: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/references/sir.json

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
