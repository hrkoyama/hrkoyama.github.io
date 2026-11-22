# Monte Carlo: integral errors and interval coverage across 256 seeds / Monte Carlo：256 seedの積分誤差と区間被覆

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: mc-integral

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

**使用手法**

- [Monte Carlo積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja) (`monte-carlo`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-mc-integral-ja)

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

$$
\int_0^1 x^2\,dx=\tfrac13,\qquad\operatorname{Var}(U^2)=\tfrac4{45}
$$

$$
\operatorname{RMS}(\hat I_N)=\sqrt{4/(45N)}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[Monte Carlo：256 seedの積分誤差と区間被覆](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja) (`mc-integral`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=ja#mc-integral-ja-validation)

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。


### scope

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

### assumptions

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

### units

全変数・係数・時間は入力JSONに定めた無次元値。SIRは人口の割合。

### boundaries

空間境界なし。初期値・時間区間／積分区間・標本数・seedは入力に固定。

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json
Input SHA-256: a4a88a51f4b89bc972cd6f9fb81662333ab992647b6355c5e705c966d4c3042f
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/mc-integral.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/solution.csv

### Numerical acceptance

- all-numerical-checks / 入力で定めた全数値条件: /checks; all values = true
- input-provenance / 入力ハッシュ: /input_sha256; value = a4a88a51f4b89bc972cd6f9fb81662333ab992647b6355c5e705c966d4c3042f
- termination / 固定予算による正常終了: /termination; value = fixed_budget_completed
- rms_over_theory-minimum / rms_over_theory（固定入力の条件）: /metrics/rms_over_theory; value ≥ 0.75
- rms_over_theory-maximum / rms_over_theory（固定入力の条件）: /metrics/rms_over_theory; value ≤ 1.3
- coverage_95-minimum / coverage_95（固定入力の条件）: /metrics/coverage_95; value ≥ 0.89
- coverage_95-maximum / coverage_95（固定入力の条件）: /metrics/coverage_95; value ≤ 0.995

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/monte-carlo/

### References

- 既存の解説章に出典と確認範囲を記載。論文本文は配布しません。: https://doi.org/10.1080/01621459.1949.10483310

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

**Methods used**

- [Monte Carlo integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en) (`monte-carlo`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-mc-integral-en)

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

$$
\int_0^1 x^2\,dx=\tfrac13,\qquad\operatorname{Var}(U^2)=\tfrac4{45}
$$

$$
\operatorname{RMS}(\hat I_N)=\sqrt{4/(45N)}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/preview.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Monte Carlo: integral errors and interval coverage across 256 seeds](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en) (`mc-integral`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/mc-integral/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/?lang=en#mc-integral-en-validation)

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.


### scope

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

### assumptions

Integrate x² under U[0,1]. Compare 256 independent seeds with analytic integral and variance, checking N^-1/2 RMS scaling and interval coverage. Excludes MCMC and rare events.

### units

Dimensionless variables, coefficients and time as specified in input JSON; SIR uses population fractions.

### boundaries

No spatial boundary. Initial values, time/integration interval, sample counts and seeds are fixed in the input.

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/mc-integral.json
Input SHA-256: a4a88a51f4b89bc972cd6f9fb81662333ab992647b6355c5e705c966d4c3042f
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/mc-integral.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/mc-integral/solution.csv

### Numerical acceptance

- all-numerical-checks / All numerical conditions fixed by the input: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = a4a88a51f4b89bc972cd6f9fb81662333ab992647b6355c5e705c966d4c3042f
- termination / Completed fixed computation budget: /termination; value = fixed_budget_completed
- rms_over_theory-minimum / rms_over_theory (fixed-input criterion): /metrics/rms_over_theory; value ≥ 0.75
- rms_over_theory-maximum / rms_over_theory (fixed-input criterion): /metrics/rms_over_theory; value ≤ 1.3
- coverage_95-minimum / coverage_95 (fixed-input criterion): /metrics/coverage_95; value ≥ 0.89
- coverage_95-maximum / coverage_95 (fixed-input criterion): /metrics/coverage_95; value ≤ 0.995

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/monte-carlo/

### References

- The existing reading chapter documents sources and review depth. Paper text is not redistributed.: https://doi.org/10.1080/01621459.1949.10483310

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
