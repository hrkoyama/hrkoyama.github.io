# Itô SDE: strong convergence with coupled Brownian paths / Itô SDE：共有Brown運動による強収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: gbm-sde

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-h2.json

## ja

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

### scope

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

### assumptions

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

### units

全変数・係数・時間は入力JSONに定めた無次元値。SIRは人口の割合。

### boundaries

空間境界なし。初期値・時間区間／積分区間・標本数・seedは入力に固定。

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json
Input SHA-256: 5ecd024be23c56e943bae1d33a0b9ea335b27de994fad86bb03df8caff0152bc
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/gbm-sde.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv

### Numerical acceptance

- all-numerical-checks / 入力で定めた全数値条件: /checks; all values = true
- input-provenance / 入力ハッシュ: /input_sha256; value = 5ecd024be23c56e943bae1d33a0b9ea335b27de994fad86bb03df8caff0152bc
- termination / 固定予算による正常終了: /termination; value = fixed_budget_completed
- finest_rms_error-maximum / finest_rms_error（固定入力の条件）: /metrics/finest_rms_error; value ≤ 0.02
- observed_orders-minimum / observed_orders（固定入力の条件）: /metrics/observed_orders; value ≥ 0.35
- observed_orders-maximum / observed_orders（固定入力の条件）: /metrics/observed_orders; value ≤ 0.7
- exact_sample_mean_z-maximum / exact_sample_mean_z（固定入力の条件）: /metrics/exact_sample_mean_z; value ≤ 4.0

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/

### References

- 既存の解説章に出典と確認範囲を記載。論文本文は配布しません。: https://doi.org/10.1007/bf02846028

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

### scope

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

### assumptions

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

### units

Dimensionless variables, coefficients and time as specified in input JSON; SIR uses population fractions.

### boundaries

No spatial boundary. Initial values, time/integration interval, sample counts and seeds are fixed in the input.

### Input and run

Input: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json
Input SHA-256: 5ecd024be23c56e943bae1d33a0b9ea335b27de994fad86bb03df8caff0152bc
ZIP: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip
Run from: model-benchmarks-2026-11-22

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/gbm-sde.json --output output
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv

### Numerical acceptance

- all-numerical-checks / All numerical conditions fixed by the input: /checks; all values = true
- input-provenance / Input SHA-256: /input_sha256; value = 5ecd024be23c56e943bae1d33a0b9ea335b27de994fad86bb03df8caff0152bc
- termination / Completed fixed computation budget: /termination; value = fixed_budget_completed
- finest_rms_error-maximum / finest_rms_error (fixed-input criterion): /metrics/finest_rms_error; value ≤ 0.02
- observed_orders-minimum / observed_orders (fixed-input criterion): /metrics/observed_orders; value ≥ 0.35
- observed_orders-maximum / observed_orders (fixed-input criterion): /metrics/observed_orders; value ≤ 0.7
- exact_sample_mean_z-maximum / exact_sample_mean_z (fixed-input criterion): /metrics/exact_sample_mean_z; value ≤ 4.0

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/

### References

- The existing reading chapter documents sources and review depth. Paper text is not redistributed.: https://doi.org/10.1007/bf02846028

Code license: https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
