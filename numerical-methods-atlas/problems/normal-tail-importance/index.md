# 正規稀少尾の通常importance sampling / Ordinary importance sampling of a normal rare tail

https://hrkoyama.github.io/numerical-methods-atlas/problems/normal-tail-importance/

## 日本語

[保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/#normal-tail-importance) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#normal-tail-importance)

### 方程式・問題の定義

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。

#### [Gaussian確率測度：尾確率と相関標的](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja)

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。

#### 正規稀少尾の通常importance sampling

補助実行例 · 実行例の定義・検証式

$$
\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}
$$

$$
\mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)
$$

通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。

### 厳密解・参照解

1〜4次モーメントを独立正の積分で資格。既知分散による5SE校正、seed間分散、解析分散低減、重み欠落負例。既知分散normal95%のIS区間の被覆は閾値/prefixごと64反復で別記。

#### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja#normal-tail-importance-ja-measurements)

解析解 · 同じ問題の参照

\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}; \mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。

重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

#### 正規稀少尾の通常importance sampling

1〜4次モーメントを独立正の積分で資格。既知分散による5SE校正、seed間分散、解析分散低減、重み欠落負例。既知分散normal95%のIS区間の被覆は閾値/prefixごと64反復で別記。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja)

### 計算法

Y=1(X>a)exp(-aX+a²/2)の通常平均。ランダムな重み総和で割らず、proposal調整なし。直接MCの無hitは0のまま保存しCP区間を付けます。

- [Monte Carlo積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [正規稀少尾の通常importance sampling](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=ja)

補助実行例

通常の尤度比平均を解析モーメント・独立seed分散・有限被覆診断で確認。

標準正規尾a=3/6、proposal=N(a,1)、64独立seed、N=2048/8192の固定prefix。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

重み付きISへBernoulliの厳密区間を転用しません。64反復は一般95%被覆の証明でなく、nestedprefixを独立反復へ水増ししません。global weightESSと事象ESSは別です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/importance.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/importance.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)

## English

[Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/normal-tail-importance-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/#normal-tail-importance) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#normal-tail-importance-en)

### Equations and problem definitions

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.

#### [Gaussian probability measures: tails and correlated targets](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en)

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim.

#### Ordinary importance sampling of a normal rare tail

Supplementary execution example · Example definition or validation formula

$$
\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}
$$

$$
\mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)
$$

Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.

### Exact and reference solutions

Qualify moments1..4 by independent positive quadrature. Gate known-variance5SE,batch variance,analytic variance reduction and omitted-weight negative control. Report known-variance normal95IScoverage separately for64trials per threshold/prefix.

#### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en#normal-tail-importance-en-measurements)

Analytic reference · Reference for the same problem

\widehat p=N^{-1}\sum_i\mathbf1_{X_i>a}e^{-aX_i+a^2/2}; \mathbb E_q[Y^r]=e^{r(r-1)a^2/2}\overline\Phi(ra)

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.

Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

#### Ordinary importance sampling of a normal rare tail

Qualify moments1..4 by independent positive quadrature. Gate known-variance5SE,batch variance,analytic variance reduction and omitted-weight negative control. Report known-variance normal95IScoverage separately for64trials per threshold/prefix.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en)

### Numerical methods

Ordinary mean ofY=1(X>a)exp(-aX+a²/2),without random weight normalization or proposal tuning. Retain direct zero-hit counts with Clopper-Pearson intervals.

- [Monte Carlo integration](https://hrkoyama.github.io/numerical-methods-atlas/methods/monte-carlo/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Ordinary importance sampling of a normal rare tail](https://hrkoyama.github.io/numerical-methods-atlas/validation/normal-tail-importance/?lang=en)

Supplementary execution example

Check ordinary likelihood-ratio averages with analytic moments,independent batch variance and finite coverage diagnostics.

Standard normal tailsa3/6;proposalN(a,1);64independent seeds;fixedN2048/8192prefixes.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Bernoulli exact intervals are not applied to weighted IS.64trials do not prove general95%coverage;nested prefixes are not extra independent replicates. Global weightESS and eventESS are distinct.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/importance.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/importance.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)
