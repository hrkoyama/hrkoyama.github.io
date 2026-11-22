# Itô SDE：共有Brown運動による強収束 / Itô SDE: strong convergence with coupled Brownian paths

https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/

## 日本語

[公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/#publication-scope) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gbm-sde)

### 方程式・問題の定義

幾何Brown運動のItô SDE dX=μXdt+σXdW。既存46式にはSDEの専用項目がありません。

#### Itô SDE：共有Brown運動による強収束

共通実行例 · 問題の式

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

### 厳密解・参照解

幾何Brown運動の解析的なItô解を同じBrown増分で結び、強収束とモーメントを確認します。決定論ODEの厳密解とは区別します。

#### Itô SDE：共有Brown運動による強収束

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Itô SDE：共有Brown運動による強収束](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja)

共通実行例

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

[コード / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/gbm-sde.json --output output
python -m pytest -q test_models.py
```

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

#### [code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_fixed_case`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

作業フォルダ：model-benchmarks-2026-11-22/

```sh
python -m pytest -q test_models.py -k test_fixed_case
```

## English

[The same public fixed-input calculation. Shows solutions, analytic/independent references or errors; numerical criteria and CSV are linked in the execution entry.](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sde/#publication-scope) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gbm-sde-en)

### Equations and problem definitions

Geometric-Brownian Itô SDE dX=μXdt+σXdW; no SDE-specific entry exists among the 46 equations.

#### Itô SDE: strong convergence with coupled Brownian paths

Common execution example · Problem definition

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

### Exact and reference solutions

Couple geometric Brownian motion to its analytic Itô solution using the same Brownian increments to check strong convergence and moments, separately from deterministic ODE exactness.

#### Itô SDE: strong convergence with coupled Brownian paths

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Itô SDE: strong convergence with coupled Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en)

Common execution example

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

[Code / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/inputs/gbm-sde.json)

[File manifest and hashes](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs/gbm-sde.json --output output
python -m pytest -q test_models.py
```

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/model-benchmarks/2026-11-22/run.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/run.py)
- [/code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

#### [code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_case`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Working directory: model-benchmarks-2026-11-22/

```sh
python -m pytest -q test_models.py -k test_fixed_case
```
