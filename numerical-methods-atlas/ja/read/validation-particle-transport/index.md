# 粒子・輸送：独立参照・保存則・統計誤差

周期力、FMM、PIC、衝突、放射輸送の既存問題を別版で検証します。決定論的な離散誤差、保存則、有限粒子数の偏りと統計誤差を分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Ewald：非対称周期セルのエネルギー・力と独立theta積分

中性8電荷の全エネルギーと24力成分を、別実装のGaussian/theta積分と比較。分割・実空間・逆空間の打切り、保存則と不変性を分けて測定します。

### 前提・単位・境界

Coulomb定数1、単位立方体の3次元周期、全電荷0、tin-foil境界。旧版と同じ非対称配置です。独立参照も同じ零モードと自己項の規約を使います。

**編集上の補足**

非対称な中性立方セルの全エネルギー・全24力成分を、別実装のGaussian/theta積分と比較します。積分・打切り・上限の感度は、この固定配置での確認です。

### 採用した計算法

erfcと逆空間和による主計算とは別に、1/rのGaussian積分と1次元theta関数の積を数値積分します。小さい積分変数ではPoisson変換と中性条件、大きい側では自己項を引いた像和を使い、力はthetaの解析微分から積分します。

$$
E=\frac{1}{\sqrt\pi}\int_0^\infty\left[\sum_{ij}q_iq_j\Theta(\mathbf r_i-\mathbf r_j,u)-\sum_iq_i^2\right]du
$$

$$
\mathbf F_i=-\nabla_iE
$$

### 比較・検証

参照の求積・theta/像の打切り・切替点をまとめて精密化し、上限32→40の感度を別に記録します。alpha3点、実空間4点・逆空間5点、平行移動・並べ替え、合力、エネルギー差分の3成分を比較。粗い打切りの不正確さを検出する対照も残します。

### 確認の限界

固定した中性立方セルだけです。上限感度は厳密な全配置の裾誤差保証ではありません。theta参照は別定式化の自作実装であり、第三者計算パッケージや公表された参照数表ではありません。非中性・非直交・スラブ・応力・長時間MDは対象外です。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_energy": -8.407406514350587,
    "reference_energy_refinement": 0.0,
    "reference_force_refinement": 1.7763568394002505e-15,
    "reference_tail_energy": 0.0,
    "reference_tail_force": 1.7763568394002505e-15,
    "reference_quadrature_estimate": 9.6957684120808e-13,
    "energy_error": 3.552713678800501e-15,
    "force_error": 1.2434497875801753e-14,
    "splitting_energy_spread": 3.552713678800501e-15,
    "splitting_force_spread": 7.105427357601002e-14,
    "real_refinement_ratio": 1.520413841404234e-14,
    "reciprocal_refinement_ratio": 4.647403985774097e-13,
    "translation_energy": 3.552713678800501e-15,
    "translation_force": 4.440892098500626e-15,
    "permutation_force": 1.7763568394002505e-15,
    "net_force": 2.842170943040401e-14,
    "gradient_error": 6.119158513229195e-10,
    "control_force_error": 0.8224115526909029
  },
  "checks": {
    "reference_energy_refinement": true,
    "reference_force_refinement": true,
    "reference_tail_energy": true,
    "reference_tail_force": true,
    "reference_quadrature_estimate": true,
    "energy_error": true,
    "force_error": true,
    "splitting_energy_spread": true,
    "splitting_force_spread": true,
    "translation_energy": true,
    "translation_force": true,
    "permutation_force": true,
    "net_force": true,
    "gradient_error": true,
    "real_refinement_ratio": true,
    "reciprocal_refinement_ratio": true,
    "truncation_control_detected": true,
    "asymmetric_forces_nonzero": true,
    "reference_quadrature_converged": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ewald-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- P. P. Ewald (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304; review_level=abstract-and-metadata
  出版社が返した書誌と原著の節見出しを確認。原著全文の監査はしていません。
- NIST Digital Library of Mathematical Functions (2026). §20.7(viii) Transformations of Lattice Parameter. https://dlmf.nist.gov/20.7#viii; review_level=official-documentation
  Jacobi thetaの格子パラメータ変換式を公式資料で確認。年は確認年。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## SPME：格子・補間次数・格子位相と保存則

BスプラインSPMEを同じ独立theta参照へ照合し、格子・次数・位相への依存、電荷の保持、エネルギー勾配と合力を測ります。

### 前提・単位・境界

同じ中性周期8電荷、alpha=5.6、実空間像3。PME族のEssmann型SPMEであり、1993年のLagrange補間の原法とは区別します。

**編集上の補足**

PME族のうちBスプラインSPMEのエネルギー勾配型を採用します。格子位相の依存と有限格子の合力を測り、厳密な運動量保存や原法Lagrange PMEの再現とはしません。

### 採用した計算法

16³/24³/40³格子と4/6次Bスプライン、3つの平行移動位相を用います。FFT逆空間エネルギーを割当て重みで位置微分し、実空間・自己項はEwald主計算と共有します。

$$
\mathbf F_i=-\partial E_h/\partial\mathbf r_i
$$

$$
\sum_j M_p(u-j)=1,\qquad\sum_j M_p^{\prime}(u-j)=0
$$

### 比較・検証

独立thetaエネルギー・全力との差と、共有Ewald経路自体の誤差を明記します。分配の総和・導関数総和、電荷、エネルギー差分3成分、位相間の幅、有限格子の合力と粗い格子の対照を保存します。

### 確認の限界

エネルギー勾配型では有限格子のaliasingにより合力は一般にゼロではありません。厳密な運動量保存や任意配置での同じ誤差、長時間MD、原法PME、SPME全変種の検証とはしません。

### 保存実測値と判定

```json
{
  "metrics": {
    "fine_energy_error": 8.630229899608821e-07,
    "fine_force_error": 7.855116843202836e-06,
    "force_refinement_ratio": 0.005861182985296622,
    "phase_energy_spread": 1.1496225127416437e-07,
    "phase_force_spread": 1.447734647719301e-05,
    "charge_error": 2.4202861936828413e-14,
    "fine_net_force": 1.919342197087559e-05,
    "maximum_net_force_all_meshes": 0.15409275755368146,
    "shared_ewald_energy_error": 0.0,
    "shared_ewald_force_error": 3.197442310920451e-14,
    "partition_error": 2.8199664825478976e-14,
    "partition_derivative_error": 3.268496584496461e-13,
    "gradient_error": 2.401151921738176e-08,
    "coarse_control_force_error": 0.03526113281182308
  },
  "checks": {
    "fine_energy_error": true,
    "fine_force_error": true,
    "force_refinement_ratio": true,
    "phase_energy_spread": true,
    "phase_force_spread": true,
    "charge_error": true,
    "partition_error": true,
    "partition_derivative_error": true,
    "gradient_error": true,
    "shared_ewald_energy_error": true,
    "shared_ewald_force_error": true,
    "fine_net_force": true,
    "coarse_control_detected": true,
    "both_orders_refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/spme-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- T. Darden, D. York and L. Pedersen (1993). Particle mesh Ewald: An N·log(N) method for Ewald sums in large systems. https://doi.org/10.1063/1.464397; review_level=abstract-and-metadata
  原著PDFの冒頭と抄録を確認。歴史的なPME原法であり、実装したBスプライン変種とは区別。
- U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee and L. G. Pedersen (1995). A smooth particle mesh Ewald method. https://doi.org/10.1063/1.470117; review_level=selected-full-text
  原著PDFのBスプライン構造因子・FFT・解析勾配に関わる部分と抄録を確認。全ベンチマークの再現ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## FMM：直接和・解析配置と展開次数・木の深さ

96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。

### 前提・単位・境界

自由空間のphi=−sum(q log r)、自己項なし。単位正方形は木の包囲領域で、壁・周期境界ではありません。3次元Coulomb核とは別です。

**編集上の補足**

自由空間2次元対数核の展開次数・木の深さ・回転平行移動の影響を測ります。深さで単調に改善するとは仮定せず、3次元Coulomb核や最適計算量へ広げません。

### 採用した計算法

P2M/M2M/M2L/L2Lと近接P2Pを保ち、次数2/4/8/12、深さ2/3を比較します。別のCartesian直接和、二点電荷の閉形式、正多角形の中心力と遠方ポテンシャルを参照にします。

$$
\phi_i=-\sum_{j\ne i}q_j\log|z_i-z_j|,\qquad\mathbf F_i=q_i\mathbf E_i
$$

$$
\epsilon_E=\max_i\|\mathbf E_i^{\rm FMM}-\mathbf E_i^{\rm direct}\|_{\infty}
$$

### 比較・検証

ポテンシャル・場の最大絶対誤差、実際の遠方移動演算、回転・平行移動誤差、電荷を掛けた力の合計を測ります。粗い展開の失敗対照も確認します。

### 確認の限界

木の深さによる相互作用の分割は変わるので、一定次数で深さに対する単調収束は要求しません。対象粒子ごとの展開は厳密な作用反作用を保証せず、3次元・適応木・周期FMM・計算量スケーリングは未検証です。

### 保存実測値と判定

```json
{
  "metrics": {
    "fine_potential_error": 1.6153974611299304e-06,
    "fine_field_error": 0.00013124381103546412,
    "order_refinement_ratio": 7.213976104507879e-05,
    "depth2_field_error": 0.00010463275822658602,
    "net_force_relative": 8.766244233276265e-08,
    "net_force_absolute": 0.00011622325026383606,
    "direct_net_force": 7.283063041541027e-14,
    "coarse_control_field_error": 1.8192992204874692,
    "translation_potential_error": 1.612941820106073e-06,
    "translation_field_error": 0.0004069109892306244,
    "rotation_potential_error": 1.614394697035948e-06,
    "rotation_field_error": 0.00015204244904776232,
    "analytic_direct_potential_error": 0.0,
    "analytic_direct_field_error": 0.0,
    "symmetric_field_error": 6.770015090751258e-06,
    "multipole_potential_error": 1.3839596135767351e-11,
    "multipole_field_error": 1.0251124393789723e-09
  },
  "checks": {
    "fine_potential_error": true,
    "fine_field_error": true,
    "order_refinement_ratio": true,
    "depth2_field_error": true,
    "translation_potential_error": true,
    "translation_field_error": true,
    "rotation_potential_error": true,
    "rotation_field_error": true,
    "net_force_relative": true,
    "analytic_direct_potential_error": true,
    "analytic_direct_field_error": true,
    "symmetric_field_error": true,
    "multipole_potential_error": true,
    "multipole_field_error": true,
    "coarse_control_detected": true,
    "actual_m2l": true,
    "actual_l2l": true,
    "near_pairs_subset": true,
    "multipole_probe_has_far_translation": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- L. Greengard and V. Rokhlin (1987). A fast algorithm for particle simulations. https://doi.org/10.1016/0021-9991(87)90140-9; review_level=selected-full-text
  著者所属機関の再録PDFで対数核、モーメント、3つの移動演算、上下走査を確認。再録版の掲載年1997と原著1987を区別。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## PIC：格子・時間収束、保存量と粒子雑音

冷たい1次元周期プラズマのquiet-start収束と、独立seedでの初期粒子雑音を分け、電荷・運動量・Gauss則・エネルギー誤差を保存します。

### 前提・単位・境界

長さ2pi、静止イオン密度1、電子q/m=−1、plasma frequency=1、微小正弦変位0.001、最終時刻1.6。格子系列は同じ2048粒子を使い、時間系列は同じ32格子・256粒子を使います。 w=2pi/Nは粒子重み、nは格子数です。

**編集上の補足**

DOP853参照は同じ粒子格子RHSを積分し、時間積分に限る独立参照です。quiet startの収束と時刻0のランダム粒子雑音を分け、エネルギーの厳密保存は主張しません。

### 採用した計算法

CIC割当て・同じ重みの場補間・スペクトルPoisson・速度Verlet。独立な時間積分法DOP853は同じ粒子格子RHSを積分し、参照自身の最大刻み感度を検査します。

$$
\mathbb E[|\widehat\rho_1/n|^2]=\frac{2+\cos(2\pi/n)}{3N}
$$

$$
H_h=\frac{w}{2}\sum_iv_i^2+\frac{\Delta x}{2}\sum_jE_j^2
$$

### 比較・検証

16/32/64格子とdt=.2/.1/.05を別に精密化し、線形cos(t)と時間参照の誤差を分離します。実数奇微分のNyquist零モードはGauss残差から分けて記録。時刻0の64seed・N=256/1024/4096のCICモード電力を解析期待値と比較します。

### 確認の限界

DOP853は独立PIC空間実装ではありません。電荷・運動量の保持とエネルギーの近似保存を区別し、初期雑音のNスケーリングを時間発展した熱プラズマの保証としません。Landau減衰・電磁PIC・相対論・衝突は未検証です。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_mesh_mode_error": 0.0012829885842868122,
    "minimum_mesh_error_ratio": 3.982691594959013,
    "minimum_time_order": 2.0012021519229015,
    "finest_time_mode_error": 0.0001650650068896753,
    "reference_sensitivity": 6.217248937900877e-12,
    "charge_error": 7.847704120519421e-16,
    "momentum_error": 6.812243160173109e-19,
    "resolved_gauss_error": 2.58493941422823e-26,
    "nyquist_charge": 2.725250580759564e-15,
    "relative_energy_drift": 0.00997018843320538,
    "minimum_shot_scaled_power": 0.9441284361820317,
    "maximum_shot_scaled_power": 1.3013624563118524,
    "minimum_shot_rms_reduction": 1.7035241144134314
  },
  "checks": {
    "continuum_reference": true,
    "mesh_convergence": true,
    "time_convergence": true,
    "independent_time_reference": true,
    "charge": true,
    "momentum": true,
    "resolved_gauss": true,
    "nyquist_charge": true,
    "measured_energy_drift": true,
    "shot_noise_power": true,
    "shot_noise_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-conservation/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- R. W. Hockney and J. W. Eastwood (1988). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934; review_level=publisher-preview-and-metadata
  出版社配布プレビューの書誌・粒子モデルの導入と目次を確認。CICや冷たいプラズマの歴史的出典とし、全書の監査は主張しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## DSMC衝突成分：有限N平衡・保存則・統計誤差

有限粒子数の平衡をMaxwell極限と区別し、独立な球面標本、解析的異方性減衰、seed間誤差と比較します。

### 前提・単位・境界

等質・等質量・等方散乱のMaxwell分子、N=16/64/256、独立64seed、運動量0、sum|v|²=3N。二つのビームから24round衝突させ、roundは物理時間へ換算しません。

**編集上の補足**

保存量を固定した有限N平衡のBeta分布と独立な球面標本を使います。粒子間相関があるので独立seed間の誤差を測り、衝突roundを物理時刻や剛体球輸送へ読み替えません。

### 採用した計算法

ランダムな完全対合と球面一様の散乱で、各対の運動量・エネルギーを保持します。別の標本生成ではGaussianを重心ゼロ部分空間へ射影し、半径を固定します。

$$
\frac{e_i}{3(N-1)/2}\sim\mathrm{Beta}\!\left(\frac32,\frac{3(N-2)}2\right)
$$

$$
\mathbb E[v_x^4]=\frac{9(N-1)}{3N-1},\qquad\mathbb E[D_r]=3\left[\frac{N-2}{2(N-1)}\right]^r
$$

$$
e_i=|\mathbf v_i|^2/2,\qquad D_r=\langle v_x^2-(v_y^2+v_z^2)/2\rangle_r
$$

### 比較・検証

全roundの運動量・エネルギーの最大保存誤差は決定論的な許容値で検査します。最初の6roundの異方性、4点のエネルギーCDF、4次モーメントと有限NのBeta参照との差は、独立seed間の標準誤差で測ります。NによるCDF標準誤差の減少と、有限NからMaxwellへの偏りを分けます。

### 確認の限界

固定した64seedの統計的診断であり、全seedの保証ではありません。同一seed内の粒子は保存量で相関し、IIDのKS p値へ読み替えません。空間輸送、衝突セル、剛体球の速度依存衝突選択・輸送係数は含みません。

### 保存実測値と判定

```json
{
  "metrics": {
    "momentum_error": 2.983724378680108e-16,
    "relative_energy_error": 7.401486830834378e-16,
    "anisotropy_standard_errors": 1.6562460503431053,
    "cdf_standard_errors": 2.244491479985008,
    "independent_equilibrium_standard_errors": 1.7114389804398267,
    "fourth_standard_errors": 1.4292752287239299,
    "maximum_finite_n_maxwell_cdf_bias": 0.01377529224707158,
    "cdf_seed_standard_error_reduction": 3.996517498915623
  },
  "checks": {
    "momentum": true,
    "energy": true,
    "analytic_anisotropy": true,
    "exact_finite_n_cdf": true,
    "independent_equilibrium": true,
    "finite_n_fourth_moment": true,
    "finite_n_distinct_from_maxwell": true,
    "statistical_error_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-statistics/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- G. A. Bird (1963). Approach to Translational Equilibrium in a Rigid Sphere Gas. https://doi.org/10.1063/1.1710976; review_level=metadata-only
  Sandiaの公式DSMC記念文書とDOI書誌を確認。出版社本文は取得できず、原著の剛体球モデルを再現したとは主張しません。
- E. Scalas, A. T. Gabriel, E. Martin and G. Germano (2015). Velocity and energy distributions in microcanonical ensembles of hard spheres. https://arxiv.org/abs/1207.3505; review_level=primary-abstract-and-selected-theory; separate center-of-mass sphere derivation
  初期設計は原著抄録を確認し、その後の追加レビューで有限系分布の理論の一部を参照。ここでの運動量0の球面・周辺Beta則は明示的に導出し、原著の分子動力学データを再利用したとはしません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 放射輸送：空間・角度収束と光子統計

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

### 前提・単位・境界

定常一様平板、光学的厚さ.1/.7/3、正の半球から単位強度、逆入射・散乱・内部放射0。フラックス基準の光子入射方向はpdf=2muです。

**編集上の補足**

純吸収平板の空間・角度誤差を分離し、特性解・適応求積・光子生存率を照合します。有限seedの区間被覆を全seed保証とせず、散乱や放射流体連成は未検証です。

### 採用した計算法

1次風上有限体積の空間更新とGauss–Legendre方向を使い、角度系列は正確な指数伝播で空間誤差を除きます。MCはmu=sqrt(U)と指数光学距離から生存・吸収を独立に判定します。

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

### 比較・検証

16〜256セル・4〜64方向を別に収束させ、QUADPACK積分とE3を照合。64seed・1024/4096/16384光子で平均誤差、RMSE、二項標準偏差と95% Clopper–Pearson区間の実測被覆を記録します。全光子の出射＋吸収、正値性と離散フラックス収支を確認します。

### 確認の限界

区間被覆は有限の固定seedでの観測で、ちょうど95%の実測値や全seedの成功を保証しません。決定論的求積誤差を統計誤差へ含めず、多重散乱・周波数依存・熱放射・放射流体連成は未検証です。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_difference": 8.881784197001252e-16,
    "quad_reported_error": 4.357392576641327e-12,
    "minimum_spatial_order": 0.9856180164488282,
    "finest_spatial_flux_error": 0.0022447377157130965,
    "finest_angular_flux_error": 9.019895941264622e-12,
    "minimum_angular_reduction": 291718065.1011767,
    "balance_error": 7.771561172376096e-16,
    "minimum_intensity": 1.9515912759331092e-130,
    "maximum_intensity": 1.0,
    "mc_mean_standard_errors": 1.2889293439083243,
    "minimum_mc_rmse_ratio": 0.8350073934277391,
    "maximum_mc_rmse_ratio": 1.0858116678301433,
    "minimum_measured_coverage": 0.9375,
    "minimum_mc_rmse_reduction": 1.6796261124956355
  },
  "checks": {
    "independent_characteristic_reference": true,
    "reference_quadrature_error": true,
    "spatial_convergence": true,
    "spatial_accuracy": true,
    "angular_accuracy": true,
    "angular_convergence": true,
    "balance": true,
    "positivity": true,
    "mc_mean": true,
    "mc_binomial_error": true,
    "mc_coverage": true,
    "mc_statistical_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

### 出典と確認範囲

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
  出版社HTMLの書誌・抄録と基本の輸送式を確認。離散座標の背景として引用し、本例はDISORT全機能の実装ではありません。
- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
  一般化指数積分の積分表示を公式資料で確認。年は確認年。
- SciPy developers (2024). SciPy 1.14.1: BinomTestResult.proportion_ci. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html; review_level=official-versioned-documentation
  公式資料でexactがClopper–Pearson法を使うことと区間APIを確認。1934年原著本文は取得できず、本文閲覧とはしません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
