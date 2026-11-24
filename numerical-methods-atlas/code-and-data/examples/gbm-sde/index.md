# Itô SDE: strong convergence with coupled Brownian paths / Itô SDE：共有Brown運動による強収束

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: gbm-sde

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

**使用手法**

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) (`sde`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-gbm-sde-ja)

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja) (`gbm-sde`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja#gbm-sde-ja-validation)

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-weak-moments-ja) (`gbm-weak-moments`; 関連モデルの参照 · 解析参照)

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

- [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gbm-milstein-strong-ja) (`gbm-milstein-strong`; 関連モデルの参照 · 解析参照)

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。


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

**Methods used**

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) (`sde`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-gbm-sde-en)

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en) (`gbm-sde`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en#gbm-sde-en-validation)

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-weak-moments-en) (`gbm-weak-moments`; Related-model reference · Analytic reference)

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

- [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-gbm-milstein-strong-en) (`gbm-milstein-strong`; Related-model reference · Analytic reference)

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.


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
