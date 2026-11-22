# Monte Carlo: integral errors and interval coverage across 256 seeds / Monte Carlo：256 seedの積分誤差と区間被覆

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/mc-integral/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: mc-integral

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-h2.json

## ja

U[0,1]でx²を積分。256の独立seedで解析積分・分散と比較し、Nの平方根に反比例するRMS誤差と区間被覆を確認。MCMC・希少事象は対象外。

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
