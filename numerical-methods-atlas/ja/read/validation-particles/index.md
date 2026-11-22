# 粒子・静電場・運動論・放射輸送

小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 中性周期セルのEwald和と独立theta積分

3次元周期Coulomb相互作用の実空間和・逆空間和・自己項を実装し、分割パラメータと打切りを変えて検証します。

### 前提・単位・境界

立方セル・全電荷ゼロ・Coulomb定数1・導体境界（tin foil）。主例は非対称な8点電荷で、NaClの8イオン配置は別の解析照合用です。

### 採用した計算法

erfcで減衰する実空間和、Gaussian係数を持つ構造因子の逆格子和、−alpha/sqrt(pi) sum(q²)を加えます。力は各項の位置微分から求め、24成分を中心エネルギー差分と比較します。

$$
E=\frac12\sum_{ij\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2
$$

$$
M_{\rm NaCl}=\frac2{\sqrt\pi}\int_0^\infty[1-\vartheta_4(0,e^{-u^2})^3]du
$$

### 比較・検証

分割alphaを3点、実空間打切りを3点、逆空間打切りを4点で確認。NaClのMadelung定数は3次元和を呼ばない独立な1次元Jacobi-theta積分と照合し、求積の誤差推定も保存します。

### 確認の限界

非中性セル、背景補正、非直交セル、誘電率が有限の表面項、スラブ補正、応力、物質固有の力場は扱いません。

### 保存実測値と判定

```json
{
  "metrics": {
    "madelung_constant": 1.7475645946331826,
    "theta_reference": 1.7475645946331821,
    "theta_quadrature_error": 1.27151293921409e-13,
    "real_cutoff_force_last_change": 0.0,
    "madelung_error": 4.440892098500626e-16,
    "splitting_energy_difference": 5.329070518200751e-15,
    "splitting_force_difference": 3.8191672047105385e-14,
    "finite_difference_error": 1.7360424209300618e-09,
    "cutoff_force_last_change": 0.0,
    "net_force": 1.1546319456101628e-14
  },
  "checks": {
    "madelung_error": true,
    "splitting_energy_difference": true,
    "splitting_force_difference": true,
    "finite_difference_error": true,
    "cutoff_force_last_change": true,
    "net_force": true,
    "nonzero_forces": true,
    "real_cutoff_refines": true,
    "theta_reference_error_bound": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  出版社が返した書誌と原著の節見出しを確認。原著全文の監査はしていません。
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Jacobi thetaの格子パラメータ変換式を公式資料で確認。年は確認年。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Bスプラインsmooth PMEの格子・次数収束

電荷をBスプラインで格子へ割り当て、FFTでEwald逆空間項を評価するsmooth PME（SPME）の小規模例です。

### 前提・単位・境界

Ewaldと同じ中性立方セルと実空間項を使います。PME族のうちEssmannらのBスプライン変種を採用し、Dardenらの原法のLagrange補間とは区別します。

### 採用した計算法

4次または6次のcardinal Bスプラインのテンソル積で電荷を格子化し、節点スプラインの離散構造因子補正、Gaussian Green関数、3次元FFTを組み合わせます。格子エネルギーを重みの位置微分で解析的に微分します。

$$
Q_{\mathbf j}=\sum_iq_i\prod_{a=1}^3M_p(u_{ia}-j_a+p/2)
$$

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

### 比較・検証

16³・24³・40³格子と2つの次数で、直接Ewald逆空間和との差を記録します。Ewaldと実空間項・自己項を共有する部分も明示。最細格子の力はエネルギー差分とも比較し、全電荷の保持を確認します。

### 確認の限界

有限格子のaliasingにより、エネルギー勾配型の合力は厳密にはゼロでなく、その診断量を保存します。運動量保存・長時間MD・原法PME・最適化P³M・スラブ補正の検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "force_error": 7.855116843202836e-06,
    "energy_error": 8.183940956030256e-07,
    "finest_to_coarsest_force_ratio": 0.0062278365701822136,
    "charge_error": 2.1871393585115584e-14,
    "finite_difference_error": 2.6557447796449196e-08,
    "net_force": 1.919342197087559e-05
  },
  "checks": {
    "force_error": true,
    "energy_error": true,
    "finest_to_coarsest_force_ratio": true,
    "charge_error": true,
    "finite_difference_error": true,
    "both_orders_refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spme/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  原著PDFの冒頭と抄録を確認。歴史的なPME原法であり、実装したBスプライン変種とは区別。
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  原著PDFのBスプライン構造因子・FFT・解析勾配に関わる部分と抄録を確認。全ベンチマークの再現ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 2次元対数核のM2M・M2L・L2Lを持つFMM

自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。

### 前提・単位・境界

単位正方形内の有限点電荷ですが、境界は壁でなく木を作る包囲領域です。核はphi=−sum(q log r)、電場は−grad(phi)。自己項を除外し、周期像はありません。

### 採用した計算法

葉でP2M、上向きのM2M、相互作用リスト上のM2L、下向きのL2L、局所多項式の評価と近接P2Pを実装します。遠方を粒子ごとに開くBarnes–Hutへ置き換えず、移動演算回数と近接対数を記録します。

$$
M_k(c)=\sum_jq_j(z_j-c)^k
$$

$$
f(z)=M_0\log(z-c)-\sum_{k=1}^p\frac{M_k}{k(z-c)^k},\qquad\phi=-\Re f
$$

### 比較・検証

固定seedの128粒子で次数2・4・8・12を走査し、別の全対直接和とポテンシャル・電場の全成分を照合します。2点の符号、順序不変性、ポテンシャル微分も検査します。

### 確認の限界

3次元1/r核、適応木、周期FMM、特異積分、実測の計算量スケーリングは未検証です。2次元自由空間の教育用実装として表示します。

### 保存実測値と判定

```json
{
  "metrics": {
    "potential_max_error": 5.953093840105339e-07,
    "field_max_error": 6.36492158818669e-05,
    "finest_to_coarsest_ratio": 3.419465787735687e-05
  },
  "checks": {
    "potential_max_error": true,
    "field_max_error": true,
    "finest_to_coarsest_ratio": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_field_is_subset": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  著者所属機関の再録PDFで対数核、モーメント、3つの移動演算、上下走査を確認。再録版の掲載年1997と原著1987を区別。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## CIC静電PICの冷たいプラズマ振動

1次元周期セルの電子をCICで格子と結び、Poisson方程式と粒子運動を自洽に進めます。

### 前提・単位・境界

長さ2pi、電子の電荷質量比−1、静止イオン背景密度1、plasma frequency=1の無次元系。quiet startから振幅0.001の微小正弦変位を与えます。

### 採用した計算法

CIC電荷割当てと同じ重みの場補間、ゼロ平均のスペクトルPoisson解、速度Verletを組み合わせます。実数の奇微分の規約により、電場のNyquistモードはゼロにします。

$$
\dot x_i=v_i,\quad\dot v_i=-E_h(x_i),\quad-\phi_{xx}=\rho,\quad E=-\phi_x
$$

$$
A(t)/A(0)\simeq\cos(\omega_pt),\qquad\omega_p=1
$$

### 比較・検証

32・64・128格子の系列と、別の512格子上の時間刻み系列を分けます。変位モードを連続線形理論のcos(t)と比較し、全電荷・Poissonポテンシャル残差・単一粒子の自己力を検査します。

### 確認の限界

有限振幅・有限粒子数の誤差床があります。非線形不安定性、Landau減衰、衝突、電磁PIC、相対論粒子、境界流入出の検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "mode_error": 0.0008867237363958114,
    "time_mode_error": 0.0004385575782555884,
    "charge_error": 1.743934249004316e-16,
    "poisson_residual": 1.0587911840678754e-22,
    "self_force": 3.3306690738754696e-16,
    "grid_refinement_ratio": 0.05753235309401034,
    "time_refinement_ratio": 0.014260976320524699
  },
  "checks": {
    "mode_error": true,
    "charge_error": true,
    "poisson_residual": true,
    "self_force": true,
    "time_error": true,
    "grid_refines": true,
    "time_refines": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pic/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  出版社配布プレビューの書誌・粒子モデルの導入と目次を確認。CICや冷たいプラズマの歴史的出典とし、全書の監査は主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 等質DSMC衝突成分の保存則・Maxwell分布

等質なMaxwell分子のランダム二体衝突で、保存則と平衡分布への緩和を検証します。

### 前提・単位・境界

等質・等質量・等方散乱・一定衝突率。各roundで全粒子を一度ずつランダムに組み合わせます。初期は±sqrt(3)の二つのビームで、温度の目標は1です。 各seedは総運動量0・総エネルギー固定のmicrocanonical系で、Maxwell/Gammaは大粒子数極限の参照です。

### 採用した計算法

対の重心速度と相対速度の大きさを保持し、相対速度の方向を球面上で一様に選びます。roundは物理時刻ではなく衝突演算の回数です。 D=<vx²−(vy²+vz²)/2>と置くと、ランダムな相方の平均で重心の異方性が(N−2)/(2(N−1))倍になり、散乱後の相対方向の異方性期待値はゼロになるため、保存した期待減衰率が得られます。

$$
\mathbf v_{1,2}^{\prime}=\mathbf V\pm\frac{|\mathbf g|}{2}\mathbf n,\qquad|\mathbf n|=1
$$

$$
\mathbb E[D_{r+1}]=\frac{N-2}{2(N-1)}\mathbb E[D_r]
$$

### 比較・検証

粒子512・2048・8192、16 seedで、運動量・運動エネルギー、Maxwellの2次/4次モーメント、Gamma(3/2,1)のエネルギーCDFを比較。異方性の期待減衰率(N−2)/(2(N−1))も独立に照合します。 有限Nの成分4次モーメントは3−6/(3N−1)であり、Maxwell値3との有限N偏りとseed間の標本誤差を区別します。

### 確認の限界

DSMCの衝突部分の教育例です。空間輸送、衝突セル、剛体球の速度依存の衝突選択、実際の輸送係数・流れ場・全seedでの保証は含みません。Bird原著の剛体球条件を再現したとは主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "momentum_error": 1.2923689896027213e-16,
    "energy_error": 2.9605947323337516e-16,
    "variance_error": 0.008371767231336591,
    "fourth_moment_error": 0.06631754023150327,
    "energy_cdf_ks": 0.0017215082600027798,
    "anisotropy_error": 0.011017100788060268,
    "finest_particle_count": 8192,
    "seeds": 16
  },
  "checks": {
    "momentum_error": true,
    "energy_error": true,
    "variance_error": true,
    "fourth_moment_error": true,
    "energy_cdf_ks": true,
    "anisotropy_error": true,
    "sampling_uncertainty_decreases": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
  Sandiaの公式DSMC記念文書とDOI書誌を確認。出版社本文は取得できず、原著の剛体球モデルを再現したとは主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 純吸収平板の離散座標放射輸送

純吸収の定常放射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

### 前提・単位・境界

光学的厚さ0.7の一様平板。正の半球から単位強度が入射し、逆向きの入射・散乱・内部放射はゼロです。

### 採用した計算法

正のGauss–Legendre離散方向と1次風上有限体積の空間行進を使います。角度誤差だけを分ける系列では、一定セル内を指数関数で正確に伝播します。

$$
\mu\frac{dI}{d\tau}+I=0,\qquad I(\tau,\mu)=e^{-\tau/\mu}
$$

$$
F_{\rm out}=2\pi\int_0^1\mu e^{-\tau/\mu}d\mu=2\pi E_3(\tau)
$$

### 比較・検証

32〜512セルで全方向の強度誤差・空間フラックス誤差・正値性・離散吸収収支を確認。4〜32方向の別系列は、出射フラックス2pi E3(tau)の解析表示と比較します。

### 確認の限界

多重散乱、熱放射、周波数再分配、動的媒質、放射流体連成は未実装です。StamnesらのDISORTの全機能・安定化を再現したとは表示しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "ray_max_error": 0.012314628761692092,
    "spatial_flux_error": 0.0011230547235325794,
    "angular_flux_error": 4.558353694505968e-12,
    "balance_error": 9.769962616701378e-15,
    "refinement_ratio": 0.06309366514102617
  },
  "checks": {
    "ray_max_error": true,
    "spatial_flux_error": true,
    "angular_flux_error": true,
    "balance_error": true,
    "refinement_ratio": true,
    "positive_bounded_intensity": true,
    "angular_refines": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-transport/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
  出版社HTMLの書誌・抄録と基本の輸送式を確認。離散座標の背景として引用し、本例はDISORT全機能の実装ではありません。
- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
  一般化指数積分の積分表示を公式資料で確認。年は確認年。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
