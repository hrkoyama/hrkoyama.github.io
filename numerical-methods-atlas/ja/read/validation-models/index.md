# MCMC・温度制御・生物モデル

小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Gaussian標的のMCMC：分布・自己相関・ESS

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
### 前提・単位・境界

無次元1変数、対称Gaussianランダムウォーク提案幅1.5。固定master seedから32の別PCG64ストリームを生成し、1024回のburn-in後に各8192標本を保持します。

### 採用した計算法

log受理比でMetropolis更新。FFTによる連鎖内自己共分散を平均し、Geyerのgamma0+gamma1から始まる初期正ペア和から平均観測量のESSを求めます。古典的split-Rhatも併記します。

$$
\pi(x)=(2\pi)^{-1/2}e^{-x^2/2},\quad \alpha=\min(1,e^{-(y^2-x^2)/2})
$$

$$
\tau=-1+2\sum_{k=0}^{K}(\rho_{2k}+\rho_{2k+1}),\qquad N_{\rm eff}=MN/\max(1,\tau)
$$

### 比較・検証

正規CDFを独立参照とし、標本数1024/2048/8192の連鎖平均RMSEを比較。別の定常AR(1)系列と厳密tau=(1+rho)/(1-rho)で診断量を照合します。公差は固定入力で事前指定します。

### 確認の限界

固定seed・予算での統計検査です。ESSは平均という観測量だけ、Rhatはrank正規化版ではありません。多峰性・高次元・任意のseedでの混合や所定の偽陽性率は保証しません。

### 保存実測値と判定

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

### 取得・実行

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

### 出典と確認範囲

- N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114; review_level=publisher-abstract-and-metadata
  出版社の書誌・抄録を確認。対称提案のMetropolis受理の原著として引用し、硬い球の原著計算を再現したとは扱いません。
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://probability.ca/hastings/hastings.pdf; review_level=original-paper-excerpt-and-metadata
  大学で公開された原著の書誌・要約と冒頭を確認。出版社DOIの通常取得はアクセスできませんでした。今回は対称Gaussian提案なので一般の非対称提案比は実装しません。
- C. J. Geyer (1992). Practical Markov Chain Monte Carlo. https://projecteuclid.org/journals/statistical-science/volume-7/issue-4/Practical-Markov-Chain-Monte-Carlo/10.1214/ss/1177011137.full; review_level=publisher-abstract-and-selected-original-section
  出版社側の抄録・書誌と大学公開原著の初期正列・AR(1)に関する検索返却箇所を確認。全文監査や任意の連鎖の収束証明を主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Langevin温度制御：正準分布・刻み偏り・時間相関

調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。

**使用手法**

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-algorithm)

力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Langevin温度制御：正準分布・刻み偏り・時間相関：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/langevin-harmonic.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Langevin温度制御：正準分布・刻み偏り・時間相関](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja) (`langevin-harmonic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/langevin-harmonic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja#langevin-harmonic-ja-validation)

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

質量・Boltzmann定数・角振動数・摩擦・温度は1。独立32768複製、burn時間20、刻み0.4/0.2/0.1、相関lag時間2。h*omega<2を要求します。

### 採用した計算法

力B・ドリフトAの半ステップと厳密OUノイズ更新OをB-A-O-A-Bで合成。サンプルの共分散・3種のCDF・エネルギー平均/分散・位置相関を記録します。

$$
dq=p\,dt,\qquad dp=-\omega^2q\,dt-\gamma p\,dt+\sqrt{2\gamma T}\,dW
$$

$$
\Sigma=M\Sigma M^T+Q,\qquad \Sigma_{h}=\operatorname{diag}(T/\omega^2,T(1-h^2\omega^2/4))
$$

### 比較・検証

SciPy離散Lyapunov解および調和系の明示共分散diag(T/omega²,T(1-h²omega²/4))で照合。運動量の刻み2次偏りと有限標本誤差を分離し、burn過渡を写像で評価。連続相関は別の行列指数で算出します。

### 確認の限界

調和ポテンシャル・固定seedの分布検証です。位置分散が正確でも運動量には有限刻み偏りがあります。他のサーモスタット、一般分子系、長時間の第一原理MDへ検証を移しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "maximum_covariance_sampling_error": 0.010793938239005096,
    "maximum_correlation_sampling_error": 0.007859497657203701,
    "maximum_lyapunov_residual": 1.1102230246251565e-16,
    "maximum_burn_transient_covariance_error": 3.9116795872649285e-09,
    "minimum_covariance_bias_order": 1.9999999999999882,
    "finest_covariance_bias": 0.0024999999999999467,
    "energy_cdf_error": 0.004375986814703525,
    "position_cdf_error": 0.005928788756380088,
    "momentum_cdf_error": 0.0068938107115509295,
    "energy_mean_error": 0.009281722112660762,
    "energy_variance_error": 0.03054847700744423
  },
  "checks": {
    "finite": true,
    "stationary_reference": true,
    "burn_transient": true,
    "covariance_sampling": true,
    "correlation_sampling": true,
    "bias_refinement": true,
    "finest_bias": true,
    "canonical_energy_cdf": true,
    "canonical_position_cdf": true,
    "canonical_momentum_cdf": true,
    "canonical_energy_mean": true,
    "canonical_energy_variance": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/index.json

### 取得・実行

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

### 出典と確認範囲

- B. Leimkuhler and C. Matthews (2013). Rational Construction of Stochastic Numerical Methods for Molecular Sampling. https://arxiv.org/abs/1203.5428; review_level=author-manuscript-selected-appendix
  著者稿の抄録、Langevin式、付録のBAOAB更新式（印刷22ページ）を確認。一般分子の超収束や原著の長時間計算を再現したとは主張しません。
- The SciPy community (2024). SciPy1.14.1 solve_discrete_lyapunov reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.solve_discrete_lyapunov.html; review_level=official-api-documentation
  公式の離散Lyapunov方程式AXA^H-X+Q=0の符号と返却仕様を確認。
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 反応拡散：空間2次と時間4次を分けて測る

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-algorithm)

周期中心2階差分と独自RK4で進めます。空間系列は小さな同一時間刻み、時間系列は同じ空間演算子を用います。

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![反応拡散：空間2次と時間4次を分けて測る：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja#reaction-diffusion-fourier-ja-validation)

連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

周期区間[0,2pi)、D=0.1、r=0.1、初期cos(2x)、終了t=2。格子16/32/64と、別の固定格子で刻み0.5/0.25/0.125を用います。

### 採用した計算法

周期中心2階差分と独自RK4で進めます。空間系列は小さな同一時間刻み、時間系列は同じ空間演算子を用います。

$$
u_t=D u_{xx}+r u,\qquad u(x,t)=e^{(r-Dk^2)t}\cos(kx)
$$

$$
\lambda_h=r-\frac{4D}{\Delta x^2}\sin^2(k\Delta x/2)
$$

### 比較・検証

連続固有値r-Dk²への最大誤差で空間次数、半離散固有値r-4Dsin²(kdx/2)/dx²への最大誤差で時間次数を測ります。独立した解析参照であり同じ実装の細格子値を参照にしません。

### 確認の限界

線形・周期・滑らかな単一モードだけを検証します。非線形のFisher前線、複雑境界、空間生態系や一般の反応ネットワークの検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "spatial_finest_error": 0.0014105590121191725,
    "spatial_minimum_order": 1.9995467358065582,
    "temporal_finest_error": 4.109141582553377e-09,
    "temporal_minimum_order": 4.0421093675761
  },
  "checks": {
    "space_error": true,
    "space_order": true,
    "time_error": true,
    "time_order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/index.json

### 取得・実行

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

### 出典と確認範囲

- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Turing不安定性：線形成長率と小振幅パターン

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-algorithm)

独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Turing不安定性：線形成長率と小振幅パターン：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja#turing-schnakenberg-ja-validation)

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

無次元a=0.1,b=0.9、平衡(1,0.9)、拡散係数(0.01,1)、周期k=2、初期振幅1e-4。線形t=1と非線形t=4の短い計算に限定します。

### 採用した計算法

独自の中心差分・RK4で線形化PDEと短い非線形PDEを進めます。3格子でのモード振幅と成長率、非線形の濃度最小値・初期パターン増幅を記録します。

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

### 比較・検証

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

### 確認の限界

1つの平衡近傍の発生段階です。原著係数や原著実験の再現、成熟模様、ランダム擾乱からの波数選択、実生物の較正は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "homogeneous_max_real_eigenvalue": -0.10000000000000003,
    "continuum_mode_growth_rate": 0.42841126979143596,
    "linear_finest_relative_error": 0.00024726924944451685,
    "linear_minimum_spatial_order": 2.000750498056138,
    "linear_finest_growth_rate_error": 7.301377900481576e-05,
    "nonlinear_minimum_concentration": 0.8998159771334997,
    "nonlinear_early_linear_relative_error": 0.00016918909911058558,
    "pattern_amplitude_growth": 5.535462628423193
  },
  "checks": {
    "homogeneous_stable": true,
    "diffusion_mode_unstable": true,
    "linear_space_error": true,
    "linear_space_order": true,
    "growth_rate": true,
    "nonlinear_finite_positive": true,
    "early_linear_agreement": true,
    "growing_spatial_pattern": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/index.json

### 取得・実行

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

### 出典と確認範囲

- A. M. Turing (1952). The Chemical Basis of Morphogenesis. https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012; review_level=publisher-archive-and-original-first-page-metadata
  Royal Societyの原稿審査記録と大学公開の原著第1ページの書誌を確認。出版社本文は403でした。拡散誘起不安定性の歴史的原著で、採用したSchnakenberg数値例の出典とは区別します。
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliographic-metadata
  PubMedの書誌・DOIを確認（抄録なし）。反応系の原典として引用し、採用係数a=0.1,b=0.9や今回の空間パターンを原著から転記したとは扱いません。
- The SciPy community (2024). SciPy1.14.1 expm reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.linalg.expm.html; review_level=official-api-documentation
  公式の行列指数APIとPadé/scaling-and-squaring法の記載を確認。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照

2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-algorithm)

独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/fitzhugh-nagumo.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja) (`fitzhugh-nagumo`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fitzhugh-nagumo/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/?lang=ja#fitzhugh-nagumo-ja-validation)

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

無次元a=0.7,b=0.8,tau=12.5。I=0の休止平衡からt=10〜20だけI=0.8を与え、t=80まで進めます。生理学的な物理単位への較正はしません。

### 採用した計算法

独自RK4を刻み0.1/0.05/0.025で使用し、パルスの不連続点で時間区間を厳密に分割します。出力刻み0.1でピークと休止状態からの距離も測定します。

$$
\dot v=v-v^3/3-w+I(t),\qquad \dot w=(v+a-bw)/\tau
$$

### 比較・検証

別実装SciPy DOP853のrtol1e-11と1e-13を比較して参照の感度を確認し、厳しい参照への最大解誤差と時間次数を評価します。ピーク時刻は出力格子上の精度です。

### 確認の限界

FHN/BVP型の縮約ODEの限定検証です。HH全イオンチャネル、空間軸索、患者データ、実測電気生理の再現を含みません。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_tolerance_difference": 1.673639005161931e-10,
    "finest_max_error": 6.469538016418142e-08,
    "minimum_temporal_order": 4.06818366368244,
    "peak_v": 2.099845449002621,
    "peak_v_error": 2.613303262677391e-08,
    "peak_time_error": 0.0,
    "recovery_distance": 2.3590633279280127e-05
  },
  "checks": {
    "reference_tolerance": true,
    "solution_error": true,
    "time_order": true,
    "excitation": true,
    "peak_voltage": true,
    "peak_time": true,
    "recovery": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fitzhugh-nagumo/index.json

### 取得・実行

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

### 出典と確認範囲

- R. FitzHugh (1961). Impulses and Physiological States in Theoretical Models of Nerve Membrane. https://pubmed.ncbi.nlm.nih.gov/19431309/; review_level=official-abstract-and-metadata
  PubMedの原著抄録・書誌を確認。2変数の興奮・不応期の縮約という役割を参照し、HH全系や実測膜電位の再現とは区別します。
- J. Nagumo, S. Arimoto and S. Yoshizawa (1962). An Active Pulse Transmission Line Simulating Nerve Axon. https://ieeexplore.ieee.org/abstract/document/4066548; review_level=publisher-abstract-and-metadata
  IEEE出版社の抄録・巻号・頁・DOIを確認。縮約した膜興奮と回路の歴史的な原著として参照し、空間的な伝送線路や回路実験を今回再現したとは扱いません。
- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-api-documentation
  公式のDOP853、dense_output、許容誤差、successの仕様を確認。独立数値参照の実装資料です。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
