# CSVRとLangevin：分布・揺らぎ・相関

小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## CSVRの厳密浴：条件付き分布・揺らぎ・運動エネルギー相関

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
### 前提・単位・境界

kB=1、T=1.3、τ=0.5、h=0.2、65536独立複製。3初期Kと3自由度で条件付き分布を測定。Hamiltonianの力・座標・拘束・COM除去は含みません。

### 採用した計算法

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

### 比較・検証

条件付き平均・分散は独立なCIR式、CDFの3確率点はSciPyの非心χ²分位点、定常KはGamma分布、浴単独ACFはexp(−t/τ)と照合。無雑音の平均緩和は分散を失う対照として別表示します。

### 確認の限界

浴の診断用ケースで独立した物理問題数へ加算しません。浴がKを正しく分布させてもglobal rescalingだけでは方向を熱化しません。exp(−t/τ)を力付きMDのK相関へ流用しません。固定seedと予算に対する統計判定で、一般の混合保証ではありません。

### 保存実測値と判定

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

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
  2007年原著の著者稿arXiv:0803.4060v1（2008年掲示）のII.1–II.3、Appendix Aの厳密運動エネルギー更新を確認。SISSAの出版社PDFは取得できず、原著の分子系を再現したものではありません。χ²は直接生成し、著者が後に指摘したΓ生成手順のtypoを写しません。
- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
  著者稿のI・II節、式(8)の有限刻み更新、式(9)のα符号、同じGaussianの使用、Nf=1のLangevin同値、τ=1/(2γ)を確認。原著Lennard-Jonesの長時間輸送係数は再現していません。
- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
  著者の公式アルゴリズム頁にある2007年論文のGaussian二乗和をΓ分布で生成する記述のtypo注記を確認。年は確認年。配布コードの転載ではなく独自実装です。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## CSVRとLangevin：調和2自由度の分布・揺らぎ・相関

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
### 前提・単位・境界

m=kB=T=1、ω=(1,1.7)、Nf=2。τ=0.25/1、h=0.1/0.05。正準初期8192複製とq,pを1.4倍した4096複製を別にt=20まで進めます。相関lagは0/0.5/1/2/4。

### 採用した計算法

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

### 比較・検証

正準Gaussian・Gamma分布とK/U/Hの平均・分散を照合。有限刻みではVerletのshadow二次形式を使い、位置分散T/[ω²(1−h²ω²/4)]、運動量分散Tを別導出したLyapunov解と比較します。h=0.2/0.1/0.05の決定論的偏りで2次性を確認。Langevinのq,p,K,H相関は独立の離散伝播と照合し、CSVRの相関は独立複製の標準誤差とτ・h依存を表示します。

### 確認の限界

global CSVRとlocal Langevinの運動相関が等しいとは要求しません。CDF差は指定5点の最大であり全実数上のKS距離ではありません。正準初期分布の保存と温度摂動からの有限時間確認は一般のエルゴード性証明ではなく、軸上の励起されない自由度が残る反例もテストします。分子・拘束・BOMDには外挿しません。

### 保存実測値と判定

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

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
  2007年原著の著者稿arXiv:0803.4060v1（2008年掲示）のII.1–II.3、Appendix Aの厳密運動エネルギー更新を確認。SISSAの出版社PDFは取得できず、原著の分子系を再現したものではありません。χ²は直接生成し、著者が後に指摘したΓ生成手順のtypoを写しません。
- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
  著者稿のI・II節、式(8)の有限刻み更新、式(9)のα符号、同じGaussianの使用、Nf=1のLangevin同値、τ=1/(2γ)を確認。原著Lennard-Jonesの長時間輸送係数は再現していません。
- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
  著者の公式アルゴリズム頁にある2007年論文のGaussian二乗和をΓ分布で生成する記述のtypo注記を確認。年は確認年。配布コードの転載ではなく独自実装です。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 非調和CSVRとLangevin：Boltzmann求積との分布比較

弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。

**使用手法**

- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-algorithm)

同じOBABO分割でglobal CSVRとlocal OUを比較。正準初期座標はGaussianを包絡にした独立棄却法、運動量はMaxwell分布から生成し、別の温度摂動初期集団も進めます。

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![非調和CSVRとLangevin：Boltzmann求積との分布比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja#csvr-langevin-quartic-ja-validation)

座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

m=kB=T=1、ω=(1,1.7)、λ=0.2、U=Σ(ω²q²/2+λq⁴/4)。正準8192複製、温度摂動4096複製、t=20、τ=0.25/1、h=0.1/0.05、lag=0/0.5/1/2/4。

### 採用した計算法

同じOBABO分割でglobal CSVRとlocal OUを比較。正準初期座標はGaussianを包絡にした独立棄却法、運動量はMaxwell分布から生成し、別の温度摂動初期集団も進めます。

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

### 比較・検証

座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

### 確認の限界

特定の分離可能な四次2自由度・固定seedだけの小さな例です。Hを調和系のGamma分布と扱いません。全系相関には独立な厳密動力学参照がなく、相関一致や統計誤差に隠れる時間次数を合格主張しません。成熟分子系・輸送係数・量子・第一原理MDの検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_canonical_cdf": 0.009973613306457074,
    "maximum_canonical_mean": 0.02768676262778527,
    "maximum_canonical_variance": 0.06550451883072274,
    "maximum_heated_cdf": 0.02028342990986376,
    "maximum_heated_mean": 0.037081739382698875,
    "maximum_heated_variance": 0.08740949912634027,
    "maximum_acf_standard_error": 0.033097037653465056,
    "quadrature_refinement_error": 2.1561918917001321e-13
  },
  "checks": {
    "canonical_position_momentum_energy_cdfs": true,
    "canonical_energy_means": true,
    "canonical_energy_fluctuations": true,
    "heated_start_cdfs": true,
    "heated_start_energy_means": true,
    "heated_start_energy_fluctuations": true,
    "quadrature_reference_refined": true,
    "independent_replica_correlation_uncertainty": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/atlas-thermostats-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. Bussi, D. Donadio and M. Parrinello (2007). Canonical sampling through velocity rescaling. https://arxiv.org/html/0803.4060v1; review_level=author-manuscript-selected-theory-and-appendix
  2007年原著の著者稿arXiv:0803.4060v1（2008年掲示）のII.1–II.3、Appendix Aの厳密運動エネルギー更新を確認。SISSAの出版社PDFは取得できず、原著の分子系を再現したものではありません。χ²は直接生成し、著者が後に指摘したΓ生成手順のtypoを写しません。
- G. Bussi and M. Parrinello (2008). Stochastic thermostats: comparison of local and global schemes. https://arxiv.org/html/0803.4397v1; review_level=author-manuscript-selected-equations-and-algorithm
  著者稿のI・II節、式(8)の有限刻み更新、式(9)のα符号、同じGaussianの使用、Nf=1のLangevin同値、τ=1/(2γ)を確認。原著Lennard-Jonesの長時間輸送係数は再現していません。
- Giovanni Bussi (2026). Research algorithms: stochastic velocity rescaling. https://sites.google.com/site/giovannibussi/Research/algorithms; review_level=author-official-algorithm-note
  著者の公式アルゴリズム頁にある2007年論文のGaussian二乗和をΓ分布で生成する記述のtypo注記を確認。年は確認年。配布コードの転載ではなく独自実装です。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
