# Langevin温度制御：正準分布・刻み偏り・時間相関 / Langevin thermostat: canonical distributions, timestep bias and correlation

https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/

## 日本語

[調和振動子BAOABの刻み0.4/0.2/0.1。離散定常共分散の偏り、有限標本誤差、正準CDF誤差とlag2の位置相関を保存値から分離表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#langevin-harmonic) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#langevin-harmonic)

### 方程式・問題の定義

Hamilton系へのリンクは調和ポテンシャルの力学部分です。計算には摩擦・雑音またはCSVRの温度浴が追加されます。

#### [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

#### [スカラーItô拡散：GBMとOU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#scalar-ito-diffusion-ja)

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

決定論的初期値のスカラーSDE。平均・二次モーメントの弱誤差、共有Brown運動での強誤差、有限標本のMCSEを分けます。OUは調和Langevin系の浴成分に関連する追加検査です。

#### Langevin温度制御：正準分布・刻み偏り・時間相関

補助実行例 · 実行例の定義・検証式

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

#### CSVRとLangevin：調和2自由度の分布・揺らぎ・相関

補助実行例 · 実行例の定義・検証式

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

#### OUのweakモーメントと同時Brownian結合

補助実行例 · 実行例の定義・検証式

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

### 厳密解・参照解

調和ポテンシャルの正準分布・モーメントと相関の解析基準を使い、刻み幅バイアスを確認します。摩擦・雑音を持たない調和軌道とは区別します。

#### [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja#ou-weak-moments-ja-measurements)

解析解 · 関連モデルの参照

dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

#### Langevin温度制御：正準分布・刻み偏り・時間相関

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja)

#### CSVRとLangevin：調和2自由度の分布・揺らぎ・相関

正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja)

#### OUのweakモーメントと同時Brownian結合

軌道前にDecimal80/120・独立GH/OU共分散積分とpaired分散による標本解像を資格。各モーメントの5MCSE校正、MCSE精度、固定3段weak率、最後2段の3SE解像を判定。区間の被覆は離散真値に対する有限32反復の記述値。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [確率微分方程式](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja)

補助実行例

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

質量・Boltzmann定数・角振動数・摩擦・温度は1。独立32768複製、burn時間20、刻み0.4/0.2/0.1、相関lag時間2。h*omega<2を要求します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

調和ポテンシャル・固定seedの分布検証です。位置分散が正確でも運動量には有限刻み偏りがあります。他のサーモスタット、一般分子系、長時間の第一原理MDへ検証を移しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

#### [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja)

補助実行例

異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

m=kB=T=1、ω=(1,1.7)、Nf=2。τ=0.25/1、h=0.1/0.05。正準初期8192複製とq,pを1.4倍した4096複製を別にt=20まで進めます。相関lagは0/0.5/1/2/4。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

global CSVRとlocal Langevinの運動相関が等しいとは要求しません。CDF差は指定5点の最大であり全実数上のKS距離ではありません。正準初期分布の保存と温度摂動からの有限時間確認は一般のエルゴード性証明ではなく、軸上の励起されない自由度が残る反例もテストします。分子・拘束・BOMDには外挿しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)

#### [OUのweakモーメントと同時Brownian結合](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=ja)

補助実行例

連続真値、離散EM期待値、同一経路差とMCSEを分離する固定入力です。

dX=1.5(.2-X)dt+.8dW,X0=.7。無次元T=1、8/16/32/64刻み、独立32seed×1024経路。状態軸に境界・clipなし。

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

## English

[Stored harmonic-BAOAB steps 0.4/0.2/0.1 separate discrete stationary-covariance bias, sampling error, canonical-CDF errors and position correlation at lag 2.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#langevin-harmonic) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#langevin-harmonic-en)

### Equations and problem definitions

The Hamiltonian link identifies the harmonic mechanical part; the calculations add friction/noise or a CSVR heat bath.

#### [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en)

$$
\dot q=\frac{\partial H}{\partial p},\qquad\dot p=-\frac{\partial H}{\partial q}
$$

$$
H=\frac{p^2}{2}+V(q)
$$

Canonical equations and a representative separable Hamiltonian. Harmonic and quartic oscillators distinguish energy error from symplecticity.

#### [Scalar Ito diffusion: GBM and OU](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#scalar-ito-diffusion-en)

$$
\mathrm dX_t=a(X_t,t)\,\mathrm dt+b(X_t,t)\,\mathrm dW_t
$$

$$
\mathrm{GBM}:\ a=\mu X,\ b=\sigma X;\quad\mathrm{OU}:\ a=\kappa(\theta-X),\ b=\sigma
$$

Scalar SDEs with deterministic initial states. Separate weak moment bias,strong errors on shared Brownian paths and finite-sample MCSE. OU is a related bath-component check,not the full harmonic Langevin system.

#### Langevin thermostat: canonical distributions, timestep bias and correlation

Supplementary execution example · Example definition or validation formula

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

#### CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes

Supplementary execution example · Example definition or validation formula

$$
U(q)=\frac12\sum_{i=1}^2\omega_i^2q_i^2,\quad H=K+U,\quad\gamma=\frac1{2\tau}
$$

$$
\Sigma_{h,i}=\operatorname{diag}\left(\frac{T}{\omega_i^2(1-h^2\omega_i^2/4)},T\right),\quad\Sigma_h=M\Sigma_hM^T+Q
$$

$$
K\sim\operatorname{Gamma}(1,T),\quad H\sim\operatorname{Gamma}(2,T),\quad\operatorname{Var}K=T^2,\quad\operatorname{Var}H=2T^2
$$

$$
C_X(t)=\frac{\mathbb E[(X_t-\mu_X)(X_0-\mu_X)]}{\sigma_X^2},\quad\operatorname{SE}(\widehat C_X)=\frac{s_{\rm products}}{\sqrt{N_{\rm replicas}}}
$$

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

#### OU weak moments with joint Brownian coupling

Supplementary execution example · Example definition or validation formula

$$
dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t
$$

$$
b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2
$$

$$
\operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa
$$

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

### Exact and reference solutions

Use analytic canonical-distribution, moment and correlation standards for the harmonic potential to check timestep bias, separately from frictionless, noiseless harmonic trajectories.

#### [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en#ou-weak-moments-en-measurements)

Analytic reference · Related-model reference

dX_t=\kappa(\theta-X_t)\,dt+\sigma\,dW_t; b_p(h)=\mathbb E[X_h(T)^p]-\mathbb E[X(T)^p],\quad p=1,2; \operatorname{Cov}(J_h,\Delta W)=(1-e^{-\kappa h})/\kappa

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

#### Langevin thermostat: canonical distributions, timestep bias and correlation

Check against a SciPy discrete-Lyapunov solve and explicit harmonic covariance diag(T/omega²,T(1-h²omega²/4)). Separate second-order momentum bias from sampling error and evaluate burn transients from the map. A separate matrix exponential gives continuous correlation.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en)

#### CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en)

#### OU weak moments with joint Brownian coupling

Before paths qualify Decimal80/120,independent GH/OUcovariance integrals and paired-variance allocation. Gate5MCSE calibration,MCSE precision,fixed three-level weak rate and final-two-level3SE resolution. Coverage is descriptive over32batches against discrete truth.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-accuracy/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Stochastic differential equations](https://hrkoyama.github.io/numerical-methods-atlas/methods/sde/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=en)

Supplementary execution example

Compare harmonic BAOAB with canonical and discrete-Lyapunov stationary distributions, and with continuous/discrete time correlations.

Mass, Boltzmann constant, frequency, friction and temperature are one. Use 32768 replicas, burn time 20, steps 0.4/0.2/0.1 and correlation lag 2; require h*omega<2.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Distribution checks use a harmonic potential and fixed seeds. Exact position variance does not remove finite-step momentum bias. Evidence does not transfer to other thermostats, general molecules or long ab initio MD.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

#### [CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en)

Supplementary execution example

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

m=kB=T=1, omega=(1,1.7), Nf=2. tau=0.25/1, h=0.1/0.05. Evolve 8192 canonically initialized replicas and a separate 4096-replica ensemble with q,p scaled by 1.4 to t=20. Correlation lags are 0/0.5/1/2/4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/thermostats/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/run.py)
- [/code/validated-examples/2026-11-22/thermostats/thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/thermostats.py)
- [/code/validated-examples/2026-11-22/thermostats/test_thermostats.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/test_thermostats.py)

#### [OU weak moments with joint Brownian coupling](https://hrkoyama.github.io/numerical-methods-atlas/validation/ou-weak-moments/?lang=en)

Supplementary execution example

Separate continuous truth,exact discrete EM expectation,paired-path weak difference and MCSE.

dX=1.5(.2-X)dt+.8dW,X0=.7;dimensionlessT1;8/16/32/64steps;32independent seeds×1024paths. Unbounded state,no clipping.

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
