# Logistic growth: analytic solution and time refinement / ロジスティック増殖：解析解と刻み幅の収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/logistic-growth/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: logistic-growth

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-periodic.json

## ja

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

### scope

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

### assumptions

無次元の単一個体群。RK4を全出力時刻で解析解と比較し、非負性と刻み幅の収束を確認。反応拡散・複数種は対象外。

### units

全変数・係数・時間は入力JSONに定めた無次元値。SIRは人口の割合。

### boundaries

空間境界なし。初期値・時間区間／積分区間・標本数・seedは入力に固定。

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json
Input SHA-256: 17fba8b04671f6d5e28e5d296c221ce90377a0947c0c96a80d5d4c3a81fa07cb
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/logistic-growth.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/solution.csv

### Numerical acceptance

- all-numerical-checks / 入力で定めた全数値条件: /checks; all values = true
- input-provenance / 入力ハッシュ: /input_sha256; value = 17fba8b04671f6d5e28e5d296c221ce90377a0947c0c96a80d5d4c3a81fa07cb
- termination / 固定予算による正常終了: /termination; value = fixed_budget_completed
- finest_max_error-maximum / finest_max_error（固定入力の条件）: /metrics/finest_max_error; value ≤ 2e-06
- observed_orders-minimum / observed_orders（固定入力の条件）: /metrics/observed_orders; value ≥ 3.7

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/biological-models/#01-1838-logistic-population-growth

### References

- 既存の解説章に出典と確認範囲を記載。論文本文は配布しません。: https://doi.org/10.3406/marb.1847.3457

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

### scope

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

### assumptions

One dimensionless population. Compare RK4 with the analytic solution at every output time; check nonnegativity and time refinement. Excludes reaction–diffusion and multispecies models.

### units

Dimensionless variables, coefficients and time as specified in input JSON; SIR uses population fractions.

### boundaries

No spatial boundary. Initial values, time/integration interval, sample counts and seeds are fixed in the input.

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/logistic-growth.json
Input SHA-256: 17fba8b04671f6d5e28e5d296c221ce90377a0947c0c96a80d5d4c3a81fa07cb
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/logistic-growth.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/logistic-growth/solution.csv

### Numerical acceptance

- all-numerical-checks / All numerical conditions fixed by the input: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = 17fba8b04671f6d5e28e5d296c221ce90377a0947c0c96a80d5d4c3a81fa07cb
- termination / Completed fixed computation budget: /termination; value = fixed_budget_completed
- finest_max_error-maximum / finest_max_error (fixed-input criterion): /metrics/finest_max_error; value ≤ 2e-06
- observed_orders-minimum / observed_orders (fixed-input criterion): /metrics/observed_orders; value ≥ 3.7

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/biological-models/#01-1838-logistic-population-growth

### References

- The existing reading chapter documents sources and review depth. Paper text is not redistributed.: https://doi.org/10.3406/marb.1847.3457

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
