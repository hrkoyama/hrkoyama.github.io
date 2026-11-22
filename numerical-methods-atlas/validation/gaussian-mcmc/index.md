# Gaussian標的のMCMC：分布・自己相関・ESS

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

**使用手法**

- [Markov連鎖Monte Carlo](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=ja) (`mcmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-algorithm)

log受理比でMetropolis更新。FFTによる連鎖内自己共分散を平均し、Geyerのgamma0+gamma1から始まる初期正ペア和から平均観測量のESSを求めます。古典的split-Rhatも併記します。

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Gaussian標的のMCMC：分布・自己相関・ESS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Gaussian標的のMCMC：分布・自己相関・ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja) (`gaussian-mcmc`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja#gaussian-mcmc-ja-validation)

正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

無次元1変数、対称Gaussianランダムウォーク提案幅1.5。固定master seedから32の別PCG64ストリームを生成し、1024回のburn-in後に各8192標本を保持します。

## 採用した計算法

log受理比でMetropolis更新。FFTによる連鎖内自己共分散を平均し、Geyerのgamma0+gamma1から始まる初期正ペア和から平均観測量のESSを求めます。古典的split-Rhatも併記します。

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

## 比較・検証

正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。

## 確認の限界

固定seed・予算での統計検査です。ESSは平均という観測量だけ、Rhatはrank正規化版ではありません。多峰性・高次元・任意のseedでの混合や所定の偽陽性率は保証しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "mean_error": 0.010631777843262634,
    "variance_error": 0.002245617179238435,
    "cdf_max_error": 0.0032519421134648008,
    "acceptance": 0.5894775390625,
    "tau": 5.380318100624768,
    "ess": 48722.769750279185,
    "split_rhat": 1.0004379739161546,
    "acf_lag1": 0.6804539280760109,
    "ar1_exact_tau": 9.000000000000002,
    "ar1_series_tau_error": 1.7763568394002505e-15,
    "ar1_empirical_tau_relative_error": 0.012439210859068739,
    "budget_mean_rmse_ratio": 2.949230534359497
  },
  "checks": {
    "finite": true,
    "mean": true,
    "variance": true,
    "cdf": true,
    "split_rhat": true,
    "ess": true,
    "acceptance": true,
    "ar1_exact_sequence": true,
    "ar1_sampling_diagnostic": true,
    "sample_budget": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
  出版社の書誌・抄録を確認。対称提案のMetropolis受理の原著として引用し、硬い球の原著計算を再現したとは扱いません。
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
  大学で公開された原著の書誌・要約と冒頭を確認。出版社DOIの通常取得はアクセスできませんでした。今回は対称Gaussian提案なので一般の非対称提案比は実装しません。
- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://projecteuclid.org/journals/statistical-science/volume-7/issue-4/Practical-Markov-Chain-Monte-Carlo/10.1214/ss/1177011137.full; review_level=publisher-abstract-and-selected-original-section
  出版社側の抄録・書誌と大学公開原著の初期正列・AR(1)に関する検索返却箇所を確認。全文監査や任意の連鎖の収束証明を主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Gaussian-target MCMC: distribution, autocorrelation and ESS

Check 32 Metropolis chains against a known standard-normal target; record mean, variance, CDF, autocorrelation time, ESS and sample-budget dependence.

**Methods used**

- [Markov-chain Monte Carlo / MCMC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mcmc/?lang=en) (`mcmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-algorithm)

Use a log-acceptance Metropolis update. Pool FFT within-chain autocovariances and obtain mean-observable ESS from Geyer initial-positive pairs starting at gamma0+gamma1. Also report classical split-Rhat.

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Gaussian-target MCMC: distribution, autocorrelation and ESS: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/gaussian-mcmc.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Gaussian-target MCMC: distribution, autocorrelation and ESS](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en) (`gaussian-mcmc`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/gaussian-mcmc/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/?lang=en#gaussian-mcmc-en-validation)

Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

One dimensionless variable and symmetric Gaussian random-walk width1.5. Spawn 32 separate PCG64 streams from a fixed master seed; retain 8192 samples per chain after 1024 burn-in steps.

## Adopted numerical method

Use a log-acceptance Metropolis update. Pool FFT within-chain autocovariances and obtain mean-observable ESS from Geyer initial-positive pairs starting at gamma0+gamma1. Also report classical split-Rhat.

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

## References and validation

Use the normal CDF as an independent analytic reference and compare chain-mean RMSE at 1024/2048/8192 retained samples. A separate stationary AR(1) sequence and exact tau=(1+rho)/(1-rho) check the diagnostic. Acceptance is predeclared in fixed inputs.

## Limits

Statistical checks apply to fixed seeds and budgets. ESS concerns the mean only; Rhat is not rank-normalized. No guarantee covers multimodality, high dimensions, every seed, mixing or a specified false-positive rate.

## Stored measurements and decisions

```json
{
  "metrics": {
    "mean_error": 0.010631777843262634,
    "variance_error": 0.002245617179238435,
    "cdf_max_error": 0.0032519421134648008,
    "acceptance": 0.5894775390625,
    "tau": 5.380318100624768,
    "ess": 48722.769750279185,
    "split_rhat": 1.0004379739161546,
    "acf_lag1": 0.6804539280760109,
    "ar1_exact_tau": 9.000000000000002,
    "ar1_series_tau_error": 1.7763568394002505e-15,
    "ar1_empirical_tau_relative_error": 0.012439210859068739,
    "budget_mean_rmse_ratio": 2.949230534359497
  },
  "checks": {
    "finite": true,
    "mean": true,
    "variance": true,
    "cdf": true,
    "split_rhat": true,
    "ess": true,
    "acceptance": true,
    "ar1_exact_sequence": true,
    "ar1_sampling_diagnostic": true,
    "sample_budget": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gaussian-mcmc/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
  Publisher bibliography and abstract checked. Cited for symmetric-proposal Metropolis acceptance; no reproduction of the original hard-sphere experiment is claimed.
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
  Bibliography, summary and opening excerpt of the original paper hosted by a university checked; the publisher DOI could not be opened. This example uses symmetric Gaussian proposals and does not implement a general asymmetric proposal ratio.
- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://projecteuclid.org/journals/statistical-science/volume-7/issue-4/Practical-Markov-Chain-Monte-Carlo/10.1214/ss/1177011137.full; review_level=publisher-abstract-and-selected-original-section
  Publisher-side abstract/metadata and returned original-paper excerpts on initial-positive sequences and AR(1), from a university-hosted copy, checked. No full-text audit or convergence certificate for arbitrary chains is claimed.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
