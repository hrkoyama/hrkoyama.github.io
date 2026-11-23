# CSVRとLangevin：調和2自由度の分布・揺らぎ・相関

異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。

**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-algorithm)

両方式とも厳密な浴O(h/2)–velocity-Verlet–O(h/2)（OBABO）。CSVRは全運動量に同じ係数、Langevinは各成分に独立OU雑音を作用。γ=1/(2τ)で自由浴のK緩和時間をそろえます。以前のBAOAB例は変更せず別の分割として残します。

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

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![CSVRとLangevin：調和2自由度の分布・揺らぎ・相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja#csvr-langevin-harmonic-ja-validation)

正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

m=kB=T=1、ω=(1,1.7)、Nf=2。τ=0.25/1、h=0.1/0.05。正準初期8192複製とq,pを1.4倍した4096複製を別にt=20まで進めます。相関lagは0/0.5/1/2/4。

## 採用した計算法

両方式とも厳密な浴O(h/2)–velocity-Verlet–O(h/2)（OBABO）。CSVRは全運動量に同じ係数、Langevinは各成分に独立OU雑音を作用。γ=1/(2τ)で自由浴のK緩和時間をそろえます。以前のBAOAB例は変更せず別の分割として残します。

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

## 比較・検証

正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。

## 確認の限界

global CSVRとlocal Langevinの運動相関が等しいとは要求しません。CDF差は指定5点の最大であり全実数上のKS距離ではありません。正準初期分布の保存と温度摂動からの有限時間確認は一般のエルゴード性証明ではなく、軸上の励起されない自由度が残る反例もテストします。分子・拘束・BOMDには外挿しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_canonical_cdf": 0.015625,
    "maximum_canonical_mean": 0.013405172680857502,
    "maximum_canonical_variance": 0.05977288750654294,
    "maximum_heated_cdf": 0.01733397470983844,
    "maximum_heated_mean": 0.026796700361769732,
    "maximum_heated_variance": 0.11505796375558419,
    "maximum_acf_standard_error": 0.03519420852454281,
    "maximum_langevin_acf_absolute_error": 0.05177769481005279,
    "maximum_langevin_acf_z": 2.526881902370831,
    "quadrature_refinement_error": 4.440892098500626e-16,
    "minimum_shadow_bias_order": 2.0078530846410816,
    "maximum_shadow_covariance_error": 2.4424906541753444e-15,
    "finest_shadow_position_bias": 0.0006261309490266931
  },
  "checks": {
    "canonical_position_momentum_energy_cdfs": true,
    "canonical_energy_means": true,
    "canonical_energy_fluctuations": true,
    "heated_start_cdfs": true,
    "heated_start_energy_means": true,
    "heated_start_energy_fluctuations": true,
    "quadrature_reference_refined": true,
    "independent_replica_correlation_uncertainty": true,
    "langevin_independent_discrete_correlation": true,
    "shadow_covariance_identity": true,
    "deterministic_second_order_bias": true,
    "finest_shadow_bias": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/index.json

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

# CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes

Compare global CSVR with local Langevin on two nondegenerate modes using the same OBABO splitting. Record position, momentum, temperature and total-energy distributions, fluctuations and correlations.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-algorithm)

Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.

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

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![CSVR versus Langevin: distributions, fluctuations and correlations of two harmonic modes: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-harmonic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Langevin thermostat: canonical distributions, timestep bias and correlation](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en) (`langevin-harmonic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=en#csvr-langevin-harmonic-en-validation)

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

m=kB=T=1, omega=(1,1.7), Nf=2. tau=0.25/1, h=0.1/0.05. Evolve 8192 canonically initialized replicas and a separate 4096-replica ensemble with q,p scaled by 1.4 to t=20. Correlation lags are 0/0.5/1/2/4.

## Adopted numerical method

Both use exact O(h/2)–velocity-Verlet–O(h/2), or OBABO. CSVR applies one factor to all momenta; Langevin uses independent component-wise OU noise. gamma=1/(2 tau) matches bath-only K relaxation. The earlier BAOAB release is retained as a different splitting.

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

## References and validation

Check canonical Gaussian/Gamma distributions and K/U/H means/variances. For finite steps, compare the Verlet-shadow position variance T/[omega²(1−h² omega²/4)] and momentum variance T against a separately constructed Lyapunov solution. Deterministic biases at h=0.2/0.1/0.05 establish second order. Check Langevin q,p,K,H correlations against independent discrete propagation; report CSVR correlations with independent-replica standard errors and tau/h dependence.

## Limits

Global-CSVR and local-Langevin dynamical correlations are not required to agree. CDF errors are maxima over five declared points, not whole-line KS distances. Canonical-start preservation and the heated-start finite-time check do not prove ergodicity; tests retain an invariant unexcited-axis counterexample. No extrapolation to molecules, constraints or BOMD.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_canonical_cdf": 0.015625,
    "maximum_canonical_mean": 0.013405172680857502,
    "maximum_canonical_variance": 0.05977288750654294,
    "maximum_heated_cdf": 0.01733397470983844,
    "maximum_heated_mean": 0.026796700361769732,
    "maximum_heated_variance": 0.11505796375558419,
    "maximum_acf_standard_error": 0.03519420852454281,
    "maximum_langevin_acf_absolute_error": 0.05177769481005279,
    "maximum_langevin_acf_z": 2.526881902370831,
    "quadrature_refinement_error": 4.440892098500626e-16,
    "minimum_shadow_bias_order": 2.0078530846410816,
    "maximum_shadow_covariance_error": 2.4424906541753444e-15,
    "finest_shadow_position_bias": 0.0006261309490266931
  },
  "checks": {
    "canonical_position_momentum_energy_cdfs": true,
    "canonical_energy_means": true,
    "canonical_energy_fluctuations": true,
    "heated_start_cdfs": true,
    "heated_start_energy_means": true,
    "heated_start_energy_fluctuations": true,
    "quadrature_reference_refined": true,
    "independent_replica_correlation_uncertainty": true,
    "langevin_independent_discrete_correlation": true,
    "shadow_covariance_identity": true,
    "deterministic_second_order_bias": true,
    "finest_shadow_bias": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/index.json

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
