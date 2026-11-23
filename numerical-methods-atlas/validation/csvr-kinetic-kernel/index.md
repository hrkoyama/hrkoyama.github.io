# CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関

自由度1・2・6のCSVR浴だけを実装し、厳密な条件付きモーメントと非心χ²分布、正準Gamma分布と運動エネルギー相関を照合します。

**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-algorithm)

平方完成した厳密CIR遷移を、標準正規Rと独立χ²(Nf−1)のSから作ります。同じRでglobal αの符号を決め、Nf=1ではS=0。単位方向と新しい半径からpを再構成し、極小KでKnew/Kを作りません。K=0は方向が未定義として拒否します。

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=ja#csvr-kinetic-kernel-ja-validation)

条件付き平均・分散は独立なCIR式、CDFの3確率点はSciPyの非心χ²分位点、定常KはGamma分布、浴単独ACFはexp(−t/τ)と照合。無雑音の平均緩和は分散を失う対照として別表示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

kB=1、T=1.3、τ=0.5、h=0.2、65536独立複製。3初期Kと3自由度で条件付き分布を測定。Hamiltonianの力・座標・拘束・COM除去は含みません。

## 採用した計算法

平方完成した厳密CIR遷移を、標準正規Rと独立χ²(Nf−1)のSから作ります。同じRでglobal αの符号を決め、Nf=1ではS=0。単位方向と新しい半径からpを再構成し、極小KでKnew/Kを作りません。K=0は方向が未定義として拒否します。

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

## 比較・検証

条件付き平均・分散は独立なCIR式、CDFの3確率点はSciPyの非心χ²分位点、定常KはGamma分布、浴単独ACFはexp(−t/τ)と照合。無雑音の平均緩和は分散を失う対照として別表示します。

## 確認の限界

浴の診断用ケースで独立した物理問題数へ加算しません。浴がKを正しく分布させてもglobal rescalingだけでは方向を熱化しません。exp(−t/τ)を力付きMDのK相関へ流用しません。固定seedと予算に対する統計判定で、一般の混合保証ではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_conditional_mean_z": 1.3654493943919508,
    "maximum_conditional_variance_relative_error": 0.01524939112434133,
    "maximum_cdf_error": 0.0039733886718749944,
    "maximum_stationary_mean_relative_error": 0.014118871247168655,
    "maximum_stationary_variance_relative_error": 0.029724570745614808,
    "maximum_kinetic_acf_error": 0.011721962477943104,
    "noiseless_variance_fraction": 2.0403637334495363e-09
  },
  "checks": {
    "conditional_mean": true,
    "conditional_variance": true,
    "transition_and_stationary_cdf": true,
    "stationary_mean": true,
    "stationary_fluctuations": true,
    "kinetic_correlation": true,
    "noiseless_control_loses_fluctuations": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
2007年原著の著者稿arXiv:0803.4060v1（2008年掲示）のII.1–II.3、Appendix Aの厳密運動エネルギー更新を確認。SISSAの出版社PDFは取得できず、原著の分子系を再現したものではありません。χ²は直接生成し、著者が後に指摘したΓ生成手順のtypoを写しません。

- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
著者稿のI・II節、式(8)の有限刻み更新、式(9)のα符号、同じGaussianの使用、Nf=1のLangevin同値、τ=1/(2γ)を確認。原著Lennard-Jonesの長時間輸送係数は再現していません。

- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
著者の公式アルゴリズム頁にある2007年論文のGaussian二乗和をΓ分布で生成する記述のtypo注記を確認。年は確認年。配布コードの転載ではなく独自実装です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Exact CSVR bath: conditional laws, fluctuations and kinetic correlation

Implement the bath-only CSVR update for 1, 2 and 6 degrees of freedom; compare exact conditional moments/noncentral-chi-square laws, canonical Gamma fluctuations and kinetic correlations.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-algorithm)

Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Exact CSVR bath: conditional laws, fluctuations and kinetic correlation: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-kinetic-kernel.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/?lang=en#csvr-kinetic-kernel-en-validation)

Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

kB=1, T=1.3, tau=0.5, h=0.2, 65536 independent replicas. Test three initial energies at each of three degree counts. No Hamiltonian force, positions, constraints or center-of-mass removal.

## Adopted numerical method

Use the completed-square exact CIR transition with normal R and independent chi-square(Nf−1) S. The same R sets the sign of global alpha; S=0 for Nf=1. Reconstruct momentum from its unit direction and new radius without a tiny-K energy ratio. Reject K=0 because its direction is undefined.

$$
\bar K=\frac{N_fT}{2},\quad c=e^{-h/\tau},\quad A=\frac{T(1-c)}2,\quad R\sim N(0,1),\ S\sim\chi^2_{N_f-1}
$$

$$
K^\prime=(\sqrt{cK}+\sqrt A R)^2+AS,\quad \operatorname{sign}\alpha=\operatorname{sign}(\sqrt{cK}+\sqrt A R)
$$

$$
\mathbb E[K^\prime\mid K]=cK+(1-c)\bar K,\quad\operatorname{Var}(K^\prime\mid K)=2TKc(1-c)+\frac{N_fT^2}{2}(1-c)^2
$$

$$
K\sim\operatorname{Gamma}(N_f/2,T),\quad\operatorname{Var}(T_{\rm inst})=\frac{2T^2}{N_f},\quad C_K^{\rm bath}(t)=e^{-t/\tau}
$$

## References and validation

Compare with separate CIR conditional moments, three SciPy noncentral-chi-square quantile probabilities, stationary Gamma K and bath-only exp(−t/tau) correlation. A separate noiseless mean-relaxation control demonstrates loss of fluctuations.

## Limits

A bath diagnostic, not another independent physical problem. Correct K sampling does not thermalize momentum directions by global scaling alone. The bath-only exp(−t/tau) identity is not a full-MD kinetic ACF. Statistical decisions apply to fixed seeds/budgets, not general mixing guarantees.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_conditional_mean_z": 1.3654493943919508,
    "maximum_conditional_variance_relative_error": 0.01524939112434133,
    "maximum_cdf_error": 0.0039733886718749944,
    "maximum_stationary_mean_relative_error": 0.014118871247168655,
    "maximum_stationary_variance_relative_error": 0.029724570745614808,
    "maximum_kinetic_acf_error": 0.011721962477943104,
    "noiseless_variance_fraction": 2.0403637334495363e-09
  },
  "checks": {
    "conditional_mean": true,
    "conditional_variance": true,
    "transition_and_stationary_cdf": true,
    "stationary_mean": true,
    "stationary_fluctuations": true,
    "kinetic_correlation": true,
    "noiseless_control_loses_fluctuations": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-kinetic-kernel/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
Checked theory II.1–II.3 and the exact kinetic-energy propagator in Appendix A of the author manuscript arXiv:0803.4060v1 (posted 2008 for the 2007 article). The SISSA publisher PDF was unavailable. Original molecular applications are not reproduced. Direct chi-square sampling avoids copying the gamma-generation typo later noted by the author.

- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
Checked sections I–II, finite-step update Eq. (8), the sign of alpha in Eq. (9) using the same Gaussian, the Nf=1 Langevin limit and tau=1/(2 gamma). The original long Lennard-Jones transport calculations are not reproduced.

- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
Checked the author’s official note identifying a typo in the 2007 paper’s gamma-based generation of Gaussian-square sums. Year is access year. This is an original implementation, not a reproduction of the downloadable code.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
