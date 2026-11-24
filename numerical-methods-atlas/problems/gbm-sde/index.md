# Itô SDE：共有Brown運動による強収束 / Itô SDE: strong convergence with coupled Brownian paths

https://hrkoyama.github.io/numerical-methods-atlas/problems/gbm-sde/

## 日本語

[公開した固定入力と同じ計算結果。解・解析参照または独立参照・誤差を図示。数値条件とCSVを実行ページに保存。](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sde/#publication-scope) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gbm-sde)

### 方程式・問題の定義

幾何Brown運動のItô SDE dX=μXdt+σXdW。既存46式にはSDEの専用項目がありません。

#### [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja)

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。

#### Itô SDE：共有Brown運動による強収束

共通実行例 · 問題の式

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

#### GBMのweak誤差とMonte Carlo標準誤差

補助実行例 · 実行例の定義・検証式

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

#### 同じBrownian経路のMilstein・EM strong比較

補助実行例 · 実行例の定義・検証式

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。

### 厳密解・参照解

幾何Brown運動の解析的なItô解を同じBrown増分で結び、強収束とモーメントを確認します。決定論ODEの厳密解とは区別します。

#### [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja#gbm-weak-moments-ja-measurements)

解析解 · 関連モデルの参照

dX_t=\mu X_t\,dt+\sigma X_t\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \mathbb E[X_h(T)]=X_0(1+\mu h)^n

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

#### [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja#gbm-milstein-strong-ja-measurements)

解析解 · 関連モデルの参照

X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]; \mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

#### Itô SDE：共有Brown運動による強収束

スカラー幾何Brown運動のEuler–Maruyama。粗細刻みと解析解で同じBrown運動を共有し、4096経路で強RMS誤差を測定。一般SDE・MCMC・弱収束次数は検証しない。

- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json)
- [保存結果](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=ja)

#### GBMのweak誤差とMonte Carlo標準誤差

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja)

#### 同じBrownian経路のMilstein・EM strong比較

相殺を含む解析MSEをDecimal80/120と独立1step GHで資格。二乗誤差の5SE校正、固定3段RMS率、最細段の優位性を判定。相関を保つ64pathblock jackknifeで率の不確実性を記述。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja)

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

#### [GBMのweak誤差とMonte Carlo標準誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=ja)

補助実行例

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

dX=.5Xdt+.4XdW,X0=1。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

弱誤差は期待値の差です。3SEや区間を真の誤差上界・一般被覆保証としません。1D状態×時間の保存例であり2D物理流れではありません。GBMやOU浴成分を新しい物理問題として重複計数しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

#### [同じBrownian経路のMilstein・EM strong比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=ja)

補助実行例

補償項を持つMilsteinとEMの終端L2 RMSを、厳密端点と有限モーメントから検査。

既存GBMと同じμ=.15,σ=.4,X0=T=1。4seed×8192経路、16/32/64/128刻み。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

L2終端誤差を扱い、原著のL1定義と区別。GBM以外の非Lipschitz系・正値性の一般保証はしません。既存gbm-sdeへの手法追加です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

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

#### [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en)

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

Scalar SDEs with deterministic initial states. Separate weak moment bias,strong errors on shared Brownian paths and finite-sample MCSE. OU is a related bath-component check,not the full harmonic Langevin system.

#### Itô SDE: strong convergence with coupled Brownian paths

Common execution example · Problem definition

$$
dX=\mu X\,dt+\sigma X\,dW
$$

$$
X(T)=X_0\exp[(\mu-\sigma^2/2)T+\sigma W(T)]
$$

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

#### GBM weak bias and Monte Carlo error

Supplementary execution example · Example definition or validation formula

$$
dX_t=\mu X_t\,dt+\sigma X_t\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\mathbb E[X_h(T)]=X_0(1+\mu h)^n
$$

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

#### Milstein and EM on identical Brownian paths

Supplementary execution example · Example definition or validation formula

$$
X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]
$$

$$
\mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]
$$

Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.

### Exact and reference solutions

Couple geometric Brownian motion to its analytic Itô solution using the same Brownian increments to check strong convergence and moments, separately from deterministic ODE exactness.

#### [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en#gbm-weak-moments-en-measurements)

Analytic reference · Related-model reference

dX_t=\mu X_t\,dt+\sigma X_t\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \mathbb E[X_h(T)]=X_0(1+\mu h)^n

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

#### [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en#gbm-milstein-strong-en-measurements)

Analytic reference · Related-model reference

X_{j+1}=X_j[1+\mu h+\sigma\Delta W_j+\tfrac12\sigma^2((\Delta W_j)^2-h)]; \mathbb E[(X_n-X(T))^2]=X_0^2[A^n+e^{(2\mu+\sigma^2)T}-2K^n]

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

#### Itô SDE: strong convergence with coupled Brownian paths

Euler–Maruyama for scalar geometric Brownian motion. Coarse/fine steps and analytic endpoints share the same Brownian paths; measure strong RMS error across 4096 paths. Does not validate general SDEs, MCMC or weak convergence order.

- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/result.json)
- [Saved result](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/results/gbm-sde/solution.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/gbm-sde/?lang=en)

#### GBM weak bias and Monte Carlo error

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en)

#### Milstein and EM on identical Brownian paths

Qualify cancellation-prone analytic MSE by Decimal80/120and independent one-step GH. Gate squared-error5SE calibration,fixed-three-level RMS rates and finest advantage.64paired path-block jackknife describes slope uncertainty.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en)

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

#### [GBM weak bias and Monte Carlo error](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-weak-moments/?lang=en)

Supplementary execution example

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

dX=.5Xdt+.4XdW,X0=1;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Weak error is a difference of expectations. SE/intervals are not true-error bounds or general coverage guarantees. State×time examples are not2Dphysical flow. Existing GBM/OUbath physical families are reused.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

#### [Milstein and EM on identical Brownian paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/gbm-milstein-strong/?lang=en)

Supplementary execution example

Compare compensated Milstein and EM endpoint L2RMS against exact endpoints and finite-moment identities.

ExistingGBMparametersmu.15,sigma.4,X0=T1;4seeds×8192paths;16/32/64/128steps.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/atlas-stochastic-accuracy-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

EndpointL2error is distinct from the selected paper L1definition. No general non-Lipschitz/positivity guarantee. This extends existinggbm-sde rather than adding a physical problem.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/stochastic-accuracy/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/run.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/paths.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/references/analytic.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/test_paths.py)

#### [code/model-benchmarks/2026-11-22/test_models.py](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/test_models.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_case`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/model-benchmarks/2026-11-22/model-benchmarks-2026-11-22.zip)

Working directory: model-benchmarks-2026-11-22/

```sh
python -m pytest -q test_models.py -k test_fixed_case
```
