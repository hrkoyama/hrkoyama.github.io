# 相関2変量Gaussianのjoint標的とMCSE / Joint target and MCSE for a correlated bivariate Gaussian

https://hrkoyama.github.io/numerical-methods-atlas/problems/correlated-gaussian-mcmc/

## 日本語

[保存した実データ由来の分布・誤差診断。空間次元と標本/時間軸を区別します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-stochastic-estimation/#correlated-gaussian-mcmc) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#correlated-gaussian-mcmc)

### 方程式・問題の定義

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。

#### [Gaussian確率測度：尾確率と相関標的](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#gaussian-probability-model-ja)

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

確率密度と積分のモデル。通常の重要度重みと既知分散の区間、2D相関Gaussianの量別診断を区別し、物理時間発展や一般のMCMC収束保証とは扱いません。

#### 相関2変量Gaussianのjoint標的とMCSE

補助実行例 · 実行例の定義・検証式

$$
\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]
$$

$$
\operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}
$$

実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。

### 厳密解・参照解

4つのpreconditioned最終prefix全観測量にRhat/ESS/MCSE/既知moment条件。同じ128scalararrayを別ArviZ0.20過程へ渡した640値資格と全データSHAで照合。標的は解析Gaussianモーメントで別検査。 640比較は不変な同一データfixture上で行い、別に生成する8組のfresh軌道で物理・混合判定を行います。環境を跨ぐ生成配列のbit一致は要求しません。

#### [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja#correlated-gaussian-mcmc-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]; \operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。

診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。

#### 相関2変量Gaussianのjoint標的とMCSE

4つのpreconditioned最終prefix全観測量にRhat/ESS/MCSE/既知moment条件。同じ128scalararrayを別ArviZ0.20過程へ渡した640値資格と全データSHAで照合。標的は解析Gaussianモーメントで別検査。 640比較は不変な同一データfixture上で行い、別に生成する8組のfresh軌道で物理・混合判定を行います。環境を跨ぐ生成配列のbit一致は要求しません。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja)

### 計算法

対称random-walk MH、拒否状態も保持。8観測量それぞれのoriginal-scale meanESS/MCSEを計算し、rankbulkESSを流用しません。

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [相関2変量Gaussianのjoint標的とMCSE](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=ja)

補助実行例

実2D MH軌道を既知のjointモーメントと同一データArviZ診断で検査。

平均(1,-1)、相関.95・対角分散1。4独立chainset×4chain、burn1024/draw8192、prefix2048/8192。固定.9Lzと.25z、適応なし。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

診断engineの独立性とsamplerの独立参照を混同しません。Rhat等は大域収束・被覆の証明ではありません。isotropicは固定比較で失敗を要求せず、banana/funnel/HMC/NUTSは未実装です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)

## English

[Distribution and error diagnostics from actual saved data;sample/time axes are distinguished from spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/correlated-gaussian-mcmc-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-stochastic-estimation/#correlated-gaussian-mcmc) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#correlated-gaussian-mcmc-en)

### Equations and problem definitions

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.

#### [Gaussian probability measures: tails and correlated targets](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#gaussian-probability-model-en)

$$
\pi_d(x)=\frac{\exp[-(x-\mu)^T\Sigma^{-1}(x-\mu)/2]}{\sqrt{(2\pi)^d\det\Sigma}}
$$

$$
p_a=\int_a^\infty\phi(z)\,\mathrm dz,\quad\mathbb E_\pi[g]=\mathbb E_q[g(X)\pi(X)/q(X)]
$$

A probability-density/integration model. Separate ordinary importance weights/known-variance intervals and observable-specific2D Gaussian diagnostics; no physical-time or universal MCMC-convergence claim.

#### Joint target and MCSE for a correlated bivariate Gaussian

Supplementary execution example · Example definition or validation formula

$$
\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]
$$

$$
\operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}
$$

Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.

### Exact and reference solutions

Gate all full-prefix observables in4preconditioned chainsets by Rhat/ESS/MCSE/knownmoments. Match exact dataSHAand640values from128scalar arrays in a separateArviZ0.20process. Target law is separately checked by analytic Gaussian moments. All640comparisons use the immutable same-data fixture;8freshchainsets independently receive the unchanged physical/mixing gates. No portable generated-byte-identity claim.

#### [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en#correlated-gaussian-mcmc-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\pi(x)\propto\exp[-\tfrac12(x-m)^\top\Sigma^{-1}(x-m)]; \operatorname{MCSE}(g)=s_g/\sqrt{\operatorname{ESS}_{\mathrm{mean}}(g)}

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.

Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.

#### Joint target and MCSE for a correlated bivariate Gaussian

Gate all full-prefix observables in4preconditioned chainsets by Rhat/ESS/MCSE/knownmoments. Match exact dataSHAand640values from128scalar arrays in a separateArviZ0.20process. Target law is separately checked by analytic Gaussian moments. All640comparisons use the immutable same-data fixture;8freshchainsets independently receive the unchanged physical/mixing gates. No portable generated-byte-identity claim.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en)

### Numerical methods

Symmetric random-walk MH retains rejected states. Compute original-scale meanESS/MCSE separately for8observables;rank bulkESS is not substituted.

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Joint target and MCSE for a correlated bivariate Gaussian](https://hrkoyama.github.io/numerical-methods-atlas/validation/correlated-gaussian-mcmc/?lang=en)

Supplementary execution example

Test actual2D MH paths against known joint moments and same-data ArviZ diagnostics.

Mean(1,-1),unit marginal variances,rho.95;4independent chainsets×4chains;burn1024/draw8192;prefix2048/8192. Fixed.9Lzand.25z,no adaptation.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/atlas-stochastic-estimation-2026-11-24.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Diagnostic-engine independence is not an independent sampler. Rhat/ESS/MCSE do not prove global convergence/coverage. Isotropic is descriptive with no required failure;banana/funnel/HMC/NUTSremain unimplemented.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24/stochastic-estimation/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/run.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/sampler.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/diagnostics.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_driver_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_estimators.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_fixture_contract.py)
- [/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/stochastic-estimation/test_tail_quantiles.py)
