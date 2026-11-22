# Gaussian標的のMCMC：分布・自己相関・ESS / Gaussian-target MCMC: distribution, autocorrelation and ESS

https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/

## 日本語

[標準正規標的・固定seedの32連鎖。保存したCDF検査点、標本予算ごとの連鎖平均RMSE・平均観測量のESSを表示。全seedの保証ではない。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#gaussian-mcmc) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#gaussian-mcmc)

### 方程式・問題の定義

Gaussian標的分布を不変分布とするMarkov連鎖の標本化問題です。既存の物理方程式一覧に専用項目はありません。

#### Gaussian標的のMCMC：分布・自己相関・ESS

補助実行例 · 実行例の定義・検証式

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

### 厳密解・参照解

既知のGaussian標的分布・モーメントを基準に、標本分布・自己相関・ESSを確認します。18件の参照解一覧にMCMC軌道の厳密解カードはありません。

#### Gaussian標的のMCMC：分布・自己相関・ESS

正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja)

補助実行例

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

無次元1変数、対称Gaussianランダムウォーク提案幅1.5。固定master seedから32の別PCG64ストリームを生成し、1024回のburn-in後に各8192標本を保持します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定seed・予算での統計検査です。ESSは平均という観測量だけ、Rhatはrank正規化版ではありません。多峰性・高次元・任意のseedでの混合や所定の偽陽性率は保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

## English

[Standard-normal target and 32 fixed-seed chains: stored CDF checkpoints, chain-mean RMSE and mean-observable ESS by sample budget. Not an every-seed guarantee.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#gaussian-mcmc) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#gaussian-mcmc-en)

### Equations and problem definitions

Markov-chain sampling with a Gaussian invariant target; the physical-equation registry has no dedicated entry.

#### Gaussian-target MCMC: distribution, autocorrelation and ESS

Supplementary execution example · Example definition or validation formula

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

### Exact and reference solutions

Use the known Gaussian target and moments to check sampled distributions, autocorrelation and ESS. The 18-case reference library has no exact MCMC-trajectory card.

#### Gaussian-target MCMC: distribution, autocorrelation and ESS

Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en)

Supplementary execution example

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

One dimensionless variable and symmetric Gaussian random-walk width1.5. Spawn 32 separate PCG64 streams from a fixed master seed; retain 8192 samples per chain after 1024 burn-in steps.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
