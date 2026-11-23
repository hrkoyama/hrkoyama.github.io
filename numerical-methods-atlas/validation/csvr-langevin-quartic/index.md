# 非調和CSVRとLangevin：Boltzmann求積との分布比較

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
## 前提・単位・境界

m=kB=T=1、ω=(1,1.7)、λ=0.2、U=Σ(ω²q²/2+λq⁴/4)。正準8192複製、温度摂動4096複製、t=20、τ=0.25/1、h=0.1/0.05、lag=0/0.5/1/2/4。

## 採用した計算法

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

## 比較・検証

座標の正規化・CDF・Uの平均/分散を1D求積、HのCDFをKの指数分布と2D座標Boltzmann密度の畳込み積分で得ます。求積公差2e−10と2e−12の差を保存し、独立棄却集団でもH分布を検査。q,p,K,Hの相関には複製間の標準誤差を併記し、刻み差と標本誤差を混同しません。

## 確認の限界

特定の分離可能な四次2自由度・固定seedだけの小さな例です。Hを調和系のGamma分布と扱いません。全系相関には独立な厳密動力学参照がなく、相関一致や統計誤差に隠れる時間次数を合格主張しません。成熟分子系・輸送係数・量子・第一原理MDの検証ではありません。

## 保存実測値と判定

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

# Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature

Compare CSVR and Langevin distributions, temperature/energy fluctuations and correlations for two weakly quartic modes. Independent Boltzmann quadrature provides equilibrium references.

**Methods used**

- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)
- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-algorithm)

Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=en#csvr-langevin-quartic-en-validation)

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

m=kB=T=1, omega=(1,1.7), lambda=0.2, U=sum(omega²q²/2+lambda q⁴/4). Use 8192 canonical and 4096 heated replicas, t=20, tau=0.25/1, h=0.1/0.05, lags 0/0.5/1/2/4.

## Adopted numerical method

Compare global CSVR and local OU with the same OBABO splitting. Draw initial canonical positions by independent Gaussian-envelope rejection and momenta from Maxwell distributions, and evolve a separate heated initial ensemble.

$$
U(q)=\sum_{i=1}^2\left(\frac{\omega_i^2q_i^2}{2}+\frac{\lambda q_i^4}{4}\right),\quad\rho(q)=Z^{-1}e^{-U(q)/T}
$$

$$
F_H(E)=\int_{U(q)\le E}\rho(q)\left[1-e^{-(E-U(q))/T}\right]dq,\qquad N_f=2
$$

$$
\mathbb E H=\mathbb E K+\mathbb E U,\quad\operatorname{Var}H=\operatorname{Var}K+\operatorname{Var}U
$$

## References and validation

Obtain coordinate normalizers/CDFs and U moments by 1D quadrature, and the H CDF by convolving exponential K with the 2D positional Boltzmann density. Save the difference between quadrature tolerances 2e−10 and 2e−12; a separate rejection ensemble also checks H. Report independent-replica standard errors for q,p,K,H correlations, keeping step differences distinct from sampling noise.

## Limits

A small example for one separable two-mode quartic potential and fixed seeds. H is not treated as harmonic Gamma. No independent exact full-system dynamical reference is claimed, and neither matching correlations nor time order hidden by sampling noise is an acceptance claim. Molecular transport, quantum and ab initio MD are outside scope.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/index.json

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
