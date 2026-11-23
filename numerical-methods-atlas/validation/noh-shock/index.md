# Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算

初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。

**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-algorithm)

Rusanov流束とSSPRK2（Heun）を使用します。平面・円筒は従来の区分定数再構築、球は保存量を体積重心の周りにMUSCL型線形再構築し、内部セルは重心間距離によるminmod傾きを使い、両端の境界セルは傾き0とします。各セル共通の係数θで左右面の全保存量傾きを縮小し、密度と内部エネルギーの面状態を検査します。セル平均の修正・圧力seed・floorは使いません。波速、Rusanov流束、数値応力P*=F_mom−((u_L+u_R)/2)F_massは同じ面状態から計算し、幾何CFLはV/(A_La_L+A_Ra_R)、指定値.35です。球では線形面応力の∫2rP*(r)drを厳密積分、平面・円筒は旧算術平均求積を保持します。反射面は再構築後の面状態を偶奇反転し、外側の冷たい流入は物理流束で与えます。各RK段の有限性・密度・内部エネルギーを検査し、不正なら失敗を記録します。

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

理想気体Eulerの平面・円筒・球の半径対称という限定した形です。幾何源・外側流入・初期圧力ゼロの条件は、この実行例の式・固定入力で定義します。


**問題の図**

![Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-validation)

旧平面・円筒の受入基準と59判定を保持し、球の追加基準・入力・ソースhashを初回の球PDE実行前に保存します。初回の円筒不合格はソース・全8本の診断ログ・不合格サマリーを保持し、同じ基準で面応力版を再検証した履歴です。厳密保存量セル平均は衝撃をまたぐ積分を分割し、p(平均U)と平均pを分けます。固定版LANL ExactPackの独立解析照合はd=1/2/3を含みます。球の新規PDE系列では全域r²重みL1/L2/L∞、原点を含むr≤.70rsの密度L1、原点・衝撃・plateauを別測定。各段の境界流入による離散保存収支と、連続解析総量との差を分け、M_h−M_exact=Σdt³/6、E_h−E_exact=Σdt³/12というSSPRK2境界求積の恒等式を検査します。 最初の球対称実行は旧算術平均源のまま105条件中2条件で不合格（最細衝撃位置3.923セル、plateau密度誤差11.03%）となり、全結果を保存しました。第2試行は球の面応力求積だけを変更しましたが、同じ2条件が未達（衝撃位置3.919セル、密度誤差11.018%）でした。第3試行はその求積を保ち、球だけMUSCL・minmod再構築を加えて、同じ105条件で比較します。 第3試行は28検査と全12格子計算を完了し、105条件すべてに合格しました。球N=512では全域密度L1=.0114343、衝撃位置誤差1.98856セル、plateau密度誤差5.2533%、原点込みcore密度L1=.0549503です。一方、中心最大比内部エネルギーの相対過剰は20.59%で、第2試行の15.52%より悪化しており、全指標の改善は主張しません。

- [Nohの冷たい流入衝撃波：平面・円筒・球対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照 · 解析参照)

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
## 前提・単位・境界

無次元r∈[0,1]、γ=5/3、ρ0=1、u0=-1、p0=0、T=.6。平面d=1・円筒半径対称d=2・球半径対称d=3をPDE実行し、衝撃半径は.2。外側密度は(1+t)^(d-1)、原点は反射、体積測度r^(d-1)dr。角度因子をすべての収支から共通に省き、球の解析総量はM=512/375、E=256/375です。球の図は1D半径解の中心断面で、Cartesianの2D/3D計算や角度方向の対称性破れの検証ではありません。

**編集上の補足**

初回不合格の保存物は、実行ソース・入力・全8格子計算の診断ログと、そこから原文のまま抽出した不合格サマリーです。初回の全場CSVが保存されているという意味ではありません。公開する成功版は、別途生成した全断面CSV・履歴・結果とZIP独立展開の再実行記録を備えます。

## 採用した計算法

Rusanov流束とSSPRK2（Heun）を使用します。平面・円筒は従来の区分定数再構築、球は保存量を体積重心の周りにMUSCL型線形再構築し、内部セルは重心間距離によるminmod傾きを使い、両端の境界セルは傾き0とします。各セル共通の係数θで左右面の全保存量傾きを縮小し、密度と内部エネルギーの面状態を検査します。セル平均の修正・圧力seed・floorは使いません。波速、Rusanov流束、数値応力P*=F_mom−((u_L+u_R)/2)F_massは同じ面状態から計算し、幾何CFLはV/(A_La_L+A_Ra_R)、指定値.35です。球では線形面応力の∫2rP*(r)drを厳密積分、平面・円筒は旧算術平均求積を保持します。反射面は再構築後の面状態を偶奇反転し、外側の冷たい流入は物理流束で与えます。各RK段の有限性・密度・内部エネルギーを検査し、不正なら失敗を記録します。

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

## 比較・検証

旧平面・円筒の受入基準と59判定を保持し、球の追加基準・入力・ソースhashを初回の球PDE実行前に保存します。初回の円筒不合格はソース・全8本の診断ログ・不合格サマリーを保持し、同じ基準で面応力版を再検証した履歴です。厳密保存量セル平均は衝撃をまたぐ積分を分割し、p(平均U)と平均pを分けます。固定版LANL ExactPackの独立解析照合はd=1/2/3を含みます。球の新規PDE系列では全域r²重みL1/L2/L∞、原点を含むr≤.70rsの密度L1、原点・衝撃・plateauを別測定。各段の境界流入による離散保存収支と、連続解析総量との差を分け、M_h−M_exact=Σdt³/6、E_h−E_exact=Σdt³/12というSSPRK2境界求積の恒等式を検査します。 最初の球対称実行は旧算術平均源のまま105条件中2条件で不合格（最細衝撃位置3.923セル、plateau密度誤差11.03%）となり、全結果を保存しました。第2試行は球の面応力求積だけを変更しましたが、同じ2条件が未達（衝撃位置3.919セル、密度誤差11.018%）でした。第3試行はその求積を保ち、球だけMUSCL・minmod再構築を加えて、同じ105条件で比較します。 第3試行は28検査と全12格子計算を完了し、105条件すべてに合格しました。球N=512では全域密度L1=.0114343、衝撃位置誤差1.98856セル、plateau密度誤差5.2533%、原点込みcore密度L1=.0549503です。一方、中心最大比内部エネルギーの相対過剰は20.59%で、第2試行の15.52%より悪化しており、全指標の改善は主張しません。

## 確認の限界

平面・円筒は空間一次、球はMUSCL型の制限線形再構築を使う教育用計算です。原点過熱と有限格子のplateau誤差が残り、全域誤差から原点を除外しません。r²重みで中心欠陥が小さく見えるため、原点を含む固定coreの誤差と拡大図も示します。L∞や中心最大誤差のゼロ収束、滑らかな球問題での方式全体の高次精度、幾何源付き全RK段階の一般の正値性保証、Cartesian多次元、任意γの独立照合は検証していません。円筒L∞は旧系列で単調減少せず、球のL2/L∞と過熱も診断値として保持します。球の離散質量・エネルギー収支が丸め誤差でも、解析総量との差は境界時間求積のO(dt²)となります。半径方向の運動量には幾何源があり、保存されるCartesian運動量とは異なります。ExactPackは解析評価器の独立実装で、別の数値PDEエンジンではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "planar_density_l1_finest": 0.006389021550074538,
    "planar_density_l2_finest": 0.035622324219688015,
    "planar_density_linf_finest": 0.2913310649697939,
    "planar_density_l1_order_finest": 1.088972053769089,
    "planar_shock_error_finest": 0.0006243356111319265,
    "planar_center_max_sie_relative_excess_finest": 0.025776017620378955,
    "planar_core_density_l1_finest": 0.006592233446323422,
    "planar_radial_momentum_balance_relative_finest": 1.2490009027033014e-16,
    "planar_mass_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_energy_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_reconstruction_theta_reduced_stage_cells_finest": 0,
    "planar_reconstruction_theta_zero_stage_cells_finest": 0,
    "planar_reconstruction_theta_min_finest": 1.0,
    "cylindrical_density_l1_finest": 0.01868269537157265,
    "cylindrical_density_l2_finest": 0.10813806869356997,
    "cylindrical_density_linf_finest": 0.5794791984687887,
    "cylindrical_density_l1_order_finest": 0.9603991144824785,
    "cylindrical_shock_error_finest": 0.004146970746716938,
    "cylindrical_center_max_sie_relative_excess_finest": 0.08161167421978366,
    "cylindrical_core_density_l1_finest": 0.04533233801997577,
    "cylindrical_radial_momentum_balance_relative_finest": 4.77048955893622e-16,
    "cylindrical_mass_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_energy_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_reconstruction_theta_reduced_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_zero_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_min_finest": 1.0,
    "spherical_density_l1_finest": 0.011434288260693065,
    "spherical_density_l2_finest": 0.12865133541762314,
    "spherical_density_linf_finest": 0.6509628676271373,
    "spherical_density_l1_order_finest": 0.9289091507144915,
    "spherical_shock_error_finest": 0.003883913585905091,
    "spherical_center_max_sie_relative_excess_finest": 0.205922730533584,
    "spherical_core_density_l1_finest": 0.05495030379369082,
    "spherical_radial_momentum_balance_relative_finest": 4.3706899842577265e-16,
    "spherical_mass_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_energy_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_reconstruction_theta_reduced_stage_cells_finest": 1968,
    "spherical_reconstruction_theta_zero_stage_cells_finest": 0,
    "spherical_reconstruction_theta_min_finest": 3.415046023746981e-13
  },
  "checks": {
    "all_runs_reach_final_time": true,
    "planar-n64: finite positive density": true,
    "planar-n64: pressure within roundoff": true,
    "planar-n64: no state floors": true,
    "planar-n64: mass_balance_relative": true,
    "planar-n64: energy_balance_relative": true,
    "planar-n128: finite positive density": true,
    "planar-n128: pressure within roundoff": true,
    "planar-n128: no state floors": true,
    "planar-n128: mass_balance_relative": true,
    "planar-n128: energy_balance_relative": true,
    "planar-n256: finite positive density": true,
    "planar-n256: pressure within roundoff": true,
    "planar-n256: no state floors": true,
    "planar-n256: mass_balance_relative": true,
    "planar-n256: energy_balance_relative": true,
    "planar-n512: finite positive density": true,
    "planar-n512: pressure within roundoff": true,
    "planar-n512: no state floors": true,
    "planar-n512: mass_balance_relative": true,
    "planar-n512: energy_balance_relative": true,
    "cylindrical-n64: finite positive density": true,
    "cylindrical-n64: pressure within roundoff": true,
    "cylindrical-n64: no state floors": true,
    "cylindrical-n64: mass_balance_relative": true,
    "cylindrical-n64: energy_balance_relative": true,
    "cylindrical-n128: finite positive density": true,
    "cylindrical-n128: pressure within roundoff": true,
    "cylindrical-n128: no state floors": true,
    "cylindrical-n128: mass_balance_relative": true,
    "cylindrical-n128: energy_balance_relative": true,
    "cylindrical-n256: finite positive density": true,
    "cylindrical-n256: pressure within roundoff": true,
    "cylindrical-n256: no state floors": true,
    "cylindrical-n256: mass_balance_relative": true,
    "cylindrical-n256: energy_balance_relative": true,
    "cylindrical-n512: finite positive density": true,
    "cylindrical-n512: pressure within roundoff": true,
    "cylindrical-n512: no state floors": true,
    "cylindrical-n512: mass_balance_relative": true,
    "cylindrical-n512: energy_balance_relative": true,
    "spherical-n64: finite positive density": true,
    "spherical-n64: pressure within roundoff": true,
    "spherical-n64: no state floors": true,
    "spherical-n64: mass_balance_relative": true,
    "spherical-n64: energy_balance_relative": true,
    "spherical-n128: finite positive density": true,
    "spherical-n128: pressure within roundoff": true,
    "spherical-n128: no state floors": true,
    "spherical-n128: mass_balance_relative": true,
    "spherical-n128: energy_balance_relative": true,
    "spherical-n256: finite positive density": true,
    "spherical-n256: pressure within roundoff": true,
    "spherical-n256: no state floors": true,
    "spherical-n256: mass_balance_relative": true,
    "spherical-n256: energy_balance_relative": true,
    "spherical-n512: finite positive density": true,
    "spherical-n512: pressure within roundoff": true,
    "spherical-n512: no state floors": true,
    "spherical-n512: mass_balance_relative": true,
    "spherical-n512: energy_balance_relative": true,
    "planar: finest density_l1": true,
    "planar: finest shock_error_in_dx": true,
    "planar: finest plateau_density_relative_error": true,
    "planar: finest plateau_pressure_relative_error": true,
    "planar: finest mass_vs_analytic_relative": true,
    "planar: finest energy_vs_analytic_relative": true,
    "planar: density L1 decreases": true,
    "planar: last-pair L1 order": true,
    "planar: unmasked center heating reported": true,
    "cylindrical: finest density_l1": true,
    "cylindrical: finest shock_error_in_dx": true,
    "cylindrical: finest plateau_density_relative_error": true,
    "cylindrical: finest plateau_pressure_relative_error": true,
    "cylindrical: finest mass_vs_analytic_relative": true,
    "cylindrical: finest energy_vs_analytic_relative": true,
    "cylindrical: density L1 decreases": true,
    "cylindrical: last-pair L1 order": true,
    "cylindrical: unmasked center heating reported": true,
    "spherical: finest density_l1": true,
    "spherical: finest shock_error_in_dx": true,
    "spherical: finest plateau_density_relative_error": true,
    "spherical: finest plateau_pressure_relative_error": true,
    "spherical: finest mass_vs_analytic_relative": true,
    "spherical: finest energy_vs_analytic_relative": true,
    "spherical: density L1 decreases": true,
    "spherical: last-pair L1 order": true,
    "spherical: unmasked center heating reported": true,
    "spherical-n64: radial momentum balance relative": true,
    "spherical-n64: mass temporal bias identity relative": true,
    "spherical-n64: energy temporal bias identity relative": true,
    "spherical-n64: finite center diagnostics": true,
    "spherical-n128: radial momentum balance relative": true,
    "spherical-n128: mass temporal bias identity relative": true,
    "spherical-n128: energy temporal bias identity relative": true,
    "spherical-n128: finite center diagnostics": true,
    "spherical-n256: radial momentum balance relative": true,
    "spherical-n256: mass temporal bias identity relative": true,
    "spherical-n256: energy temporal bias identity relative": true,
    "spherical-n256: finite center diagnostics": true,
    "spherical-n512: radial momentum balance relative": true,
    "spherical-n512: mass temporal bias identity relative": true,
    "spherical-n512: energy temporal bias identity relative": true,
    "spherical-n512: finite center diagnostics": true,
    "spherical: finest core density_l1 (origin included)": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/index.json

![3つの対称性の原点過熱・符号付き密度誤差・全域L1/L2/L∞。原点と衝撃を含む全域誤差を保持します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-errors.png)

3つの対称性の原点過熱・符号付き密度誤差・全域L1/L2/L∞。原点と衝撃を含む全域誤差を保持します。

![球対称の離散保存収支と解析総量との差、境界時間求積のΣdt³予測、原点を含むcore誤差を分けた診断。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-spherical-budget.png)

球対称の離散保存収支と解析総量との差、境界時間求積のΣdt³予測、原点を含むcore誤差を分けた診断。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  出版社書誌・抄録を確認。原著本文の直接取得は403のため全文未読。Noh問題・過熱誤差の原著として引用し、今回の有限体積離散化そのものの出典とは呼びません。
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  LANL公式書誌と固定commit 9bacc477eb791e959c9621e771fc7a725db755faのNohコードを確認・別実行。gamma=5/3,rho0=|u0|=1に限定し、点値と衝撃を分割したGauss積分で参照保存量平均を照合。このd=3解析照合の既存receiptを保持し、本版の球対称PDE系列は別途実行します。
- van Leer, Bram (1979). Towards the ultimate conservative difference scheme. V. A second-order sequel to Godunov's method. https://www.sciencedirect.com/science/article/pii/0021999179901451; review_level=existing-atlas-publisher-record-and-abstract
  既存アトラスの書誌参照。制限線形再構築とlimiterの背景として引用し、原論文の全アルゴリズムや一般の幾何源付き零圧Eulerに対する正値性定理を再現したとは主張しません。
- Sweby, P. K. (1984). High Resolution Schemes Using Flux Limiters for Hyperbolic Conservation Laws. https://epubs.siam.org/doi/10.1137/0721062; review_level=existing-atlas-publisher-record-and-abstract
  既存アトラスの書誌参照。制限線形再構築とlimiterの背景として引用し、原論文の全アルゴリズムや一般の幾何源付き零圧Eulerに対する正値性定理を再現したとは主張しません。
- Mignone, Andrea (2014). High-order conservative reconstruction schemes for finite volume methods in cylindrical and spherical coordinates. https://arxiv.org/abs/1404.0537; review_level=original-arxiv-selected-sections-2.2-3.1-4.2
  原著arXivの§2.2・3.1・4.2を選択確認。体積重心と保存的な線形再構築・幾何源積分の背景です。本実装は限定したminmod/Rusanov/Heunと独自の数値応力源を使い、論文全体の方式の再現とは区別します。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Noh shocks: zero-pressure planar, cylindrical and spherical flow

An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity.

**Methods used**

- [Rusanov / local Lax–Friedrichs flux](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=en) (`rusanov`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-algorithm)

Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`)

The scoped planar, cylindrical-radial and spherical-radial forms of ideal-gas Euler. This example defines the geometric source, outer inflow and exactly zero initial pressure in its formulas and fixed input.


**Problem figure**

![Noh shocks: zero-pressure planar, cylindrical and spherical flow: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Noh shocks: zero-pressure planar, cylindrical and spherical flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en) (`noh`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=en#noh-shock-en-validation)

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

- [Noh cold-inflow shock: planar, cylindrical and spherical symmetry](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-noh-en) (`noh`; Same-problem reference · Analytic reference)

The continuous exact solution of this same zero-pressure Noh problem. Distinguish initial-density amplification4^d from the across-shock ratio4. Finite-volume errors use exact conserved-volume averages, with p(mean U) distinct from mean p.
## Assumptions, units and boundaries

Nondimensional r in [0,1], gamma=5/3, rho0=1, u0=-1, p0=0, T=.6. PDE runs use planar d=1, cylindrical-radial d=2 and spherical-radial d=3, with shock radius .2. Outer density is (1+t)^(d-1), the origin reflects, and the measure is r^(d-1)dr. The same angular factor is omitted throughout; spherical analytic totals are M=512/375 and E=256/375. Its figure is a central section of a 1D radial solution, not a Cartesian 2D/3D calculation or a test of angular symmetry breaking.

**Editorial clarification**

The retained failed attempt includes source, inputs, diagnostic logs for all eight runs and its failed summary recovered verbatim from stdout. It does not contain every failed full-field CSV. The successful release separately supplies all profile CSVs, histories, results and an independently extracted ZIP rerun.

## Adopted numerical method

Rusanov flux with SSPRK2 (Heun). Planar/cylindrical runs retain piecewise-constant reconstruction. Spherical runs reconstruct conserved variables linearly around volume centroids with minmod slopes based on centroid distances in interior cells and zero slopes in the two boundary cells. A single theta per cell scales all conserved slopes at both faces to check face density/internal energy. Cell means are never corrected and no pressure seed/floor is used. Wave speeds, Rusanov flux and numerical stress P*=F_mom-((u_L+u_R)/2)F_mass use the same face states. The geometric CFL V/(A_La_L+A_Ra_R) uses the prescribed .35. Spherical source quadrature exactly integrates the face-linear numerical stress against 2r dr; planar/cylindrical runs keep the old arithmetic rule. Reconstructed reflection faces use even/odd parity, with physical cold inflow at the outer face. Every RK stage is checked and invalid states cause a retained failure.

$$
\partial_tU+r^{1-d}\partial_r(r^{d-1}F(U))=(0,(d-1)p/r,0)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
C=(\gamma+1)/(\gamma-1),\quad r_s=|u_0|(\gamma-1)t/2,\quad \rho_2=\rho_0C^d,\quad p_2=(\gamma-1)\rho_2u_0^2/2
$$

$$
\rho_1(r,t)=\rho_0(1+|u_0|t/r)^{d-1},\quad u_1=u_0,\quad p_1=0
$$

$$
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad \text{arithmetic-face option: }S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

$$
d=3,\ \rho_0=|u_0|=1:\quad M_h-M_{\rm exact}=\frac16\sum_n\Delta t_n^3,\qquad E_h-E_{\rm exact}=\frac1{12}\sum_n\Delta t_n^3
$$

$$
\mathcal E_{\rm core}=\frac{\sum_{r_{i+1/2}\le0.70r_s}V_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_{r_{i+1/2}\le0.70r_s}V_i\bar\rho_i^{\rm exact}},\qquad V_i=\frac{r_{i+1/2}^3-r_{i-1/2}^3}{3}
$$

$$
d=3:\quad \int_a^b2rP^*(r)\,dr=\frac{b-a}{3}\big[(b+2a)P_L^*+(2b+a)P_R^*\big]
$$

$$
\bar r_i=\frac{d}{d+1}\frac{r_{i+1/2}^{d+1}-r_{i-1/2}^{d+1}}{r_{i+1/2}^{d}-r_{i-1/2}^{d}},\qquad U_i(r)=\bar U_i+\theta_i\sigma_i(r-\bar r_i)
$$

$$
\sigma_i=\operatorname{minmod}\left(\frac{\bar U_i-\bar U_{i-1}}{\bar r_i-\bar r_{i-1}},\frac{\bar U_{i+1}-\bar U_i}{\bar r_{i+1}-\bar r_i}\right),\quad 0\le\theta_i\le1\quad \text{interior cells; boundary slopes }\sigma_0=\sigma_{N-1}=0
$$

## References and validation

Retain the planar/cylindrical acceptance file and all 59 original decisions, and save spherical criteria, inputs and source hashes before the first spherical PDE run. The initial cylindrical failure retains its source, all eight diagnostic logs and failed summary; the face-stress revision was tested against the same gates. Analytic conserved means split shock-crossing integrals and distinguish p(mean U) from mean p. The pinned independent LANL ExactPack analytic comparison includes d=1/2/3. New spherical PDE refinements separately measure full-domain r^2-weighted L1/L2/Linf, density L1 in r<=.70rs including the origin, and center/shock/plateau diagnostics. Discrete stage-weighted inflow budgets are distinct from continuous analytic totals; SSPRK2 boundary quadrature is checked through M_h-M_exact=sum(dt^3)/6 and E_h-E_exact=sum(dt^3)/12. The first spherical run retained arithmetic source quadrature and failed two of 105 gates (finest shock-position error 3.923 cells, plateau-density error 11.03%); all results are retained. A second attempt changed only spherical stress quadrature, but still failed the same two gates (3.919 cells and 11.018% density error). A third attempt retains that quadrature and adds MUSCL/minmod reconstruction only for spherical runs, against the same 105 criteria. The third attempt completed 28 tests and all 12 grid runs, passing all 105 gates. At spherical N=512 the whole-domain density L1 is .0114343, shock error 1.98856 cells, plateau-density error 5.2533%, and origin-inclusive core-density L1 .0549503. Maximum center specific-internal-energy excess is 20.59%, worse than the second attempt's 15.52%; not every diagnostic improves.

## Limits

An educational calculation: first-order space in planar/cylindrical flow and MUSCL-type limited linear reconstruction in spherical flow. Origin heating and finite-grid plateau errors remain; the center is never removed from whole-domain error. Because r^2 weighting can make central defects appear small, an origin-inclusive fixed-core norm and enlarged view are also shown. Vanishing Linf/center maximum error, high order for the complete method on smooth spherical problems, general stage positivity with the geometric source, Cartesian multidimensional flow and independent arbitrary-gamma validation are not established. Cylindrical Linf was not monotone in the old series; spherical L2/Linf and heating are retained as diagnostics. Roundoff-scale discrete mass/energy balance coexists with O(dt^2) spherical boundary-time-quadrature error against analytic totals. Radial momentum has a geometric source and is not a conserved Cartesian momentum component. ExactPack independently implements the analytic evaluator, not another numerical PDE engine.

## Stored measurements and decisions

```json
{
  "metrics": {
    "planar_density_l1_finest": 0.006389021550074538,
    "planar_density_l2_finest": 0.035622324219688015,
    "planar_density_linf_finest": 0.2913310649697939,
    "planar_density_l1_order_finest": 1.088972053769089,
    "planar_shock_error_finest": 0.0006243356111319265,
    "planar_center_max_sie_relative_excess_finest": 0.025776017620378955,
    "planar_core_density_l1_finest": 0.006592233446323422,
    "planar_radial_momentum_balance_relative_finest": 1.2490009027033014e-16,
    "planar_mass_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_energy_temporal_bias_residual_relative_finest": 6.938893903907228e-16,
    "planar_reconstruction_theta_reduced_stage_cells_finest": 0,
    "planar_reconstruction_theta_zero_stage_cells_finest": 0,
    "planar_reconstruction_theta_min_finest": 1.0,
    "cylindrical_density_l1_finest": 0.01868269537157265,
    "cylindrical_density_l2_finest": 0.10813806869356997,
    "cylindrical_density_linf_finest": 0.5794791984687887,
    "cylindrical_density_l1_order_finest": 0.9603991144824785,
    "cylindrical_shock_error_finest": 0.004146970746716938,
    "cylindrical_center_max_sie_relative_excess_finest": 0.08161167421978366,
    "cylindrical_core_density_l1_finest": 0.04533233801997577,
    "cylindrical_radial_momentum_balance_relative_finest": 4.77048955893622e-16,
    "cylindrical_mass_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_energy_temporal_bias_residual_relative_finest": 0.0,
    "cylindrical_reconstruction_theta_reduced_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_zero_stage_cells_finest": 0,
    "cylindrical_reconstruction_theta_min_finest": 1.0,
    "spherical_density_l1_finest": 0.011434288260693065,
    "spherical_density_l2_finest": 0.12865133541762314,
    "spherical_density_linf_finest": 0.6509628676271373,
    "spherical_density_l1_order_finest": 0.9289091507144915,
    "spherical_shock_error_finest": 0.003883913585905091,
    "spherical_center_max_sie_relative_excess_finest": 0.205922730533584,
    "spherical_core_density_l1_finest": 0.05495030379369082,
    "spherical_radial_momentum_balance_relative_finest": 4.3706899842577265e-16,
    "spherical_mass_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_energy_temporal_bias_residual_relative_finest": 6.154895124725433e-16,
    "spherical_reconstruction_theta_reduced_stage_cells_finest": 1968,
    "spherical_reconstruction_theta_zero_stage_cells_finest": 0,
    "spherical_reconstruction_theta_min_finest": 3.415046023746981e-13
  },
  "checks": {
    "all_runs_reach_final_time": true,
    "planar-n64: finite positive density": true,
    "planar-n64: pressure within roundoff": true,
    "planar-n64: no state floors": true,
    "planar-n64: mass_balance_relative": true,
    "planar-n64: energy_balance_relative": true,
    "planar-n128: finite positive density": true,
    "planar-n128: pressure within roundoff": true,
    "planar-n128: no state floors": true,
    "planar-n128: mass_balance_relative": true,
    "planar-n128: energy_balance_relative": true,
    "planar-n256: finite positive density": true,
    "planar-n256: pressure within roundoff": true,
    "planar-n256: no state floors": true,
    "planar-n256: mass_balance_relative": true,
    "planar-n256: energy_balance_relative": true,
    "planar-n512: finite positive density": true,
    "planar-n512: pressure within roundoff": true,
    "planar-n512: no state floors": true,
    "planar-n512: mass_balance_relative": true,
    "planar-n512: energy_balance_relative": true,
    "cylindrical-n64: finite positive density": true,
    "cylindrical-n64: pressure within roundoff": true,
    "cylindrical-n64: no state floors": true,
    "cylindrical-n64: mass_balance_relative": true,
    "cylindrical-n64: energy_balance_relative": true,
    "cylindrical-n128: finite positive density": true,
    "cylindrical-n128: pressure within roundoff": true,
    "cylindrical-n128: no state floors": true,
    "cylindrical-n128: mass_balance_relative": true,
    "cylindrical-n128: energy_balance_relative": true,
    "cylindrical-n256: finite positive density": true,
    "cylindrical-n256: pressure within roundoff": true,
    "cylindrical-n256: no state floors": true,
    "cylindrical-n256: mass_balance_relative": true,
    "cylindrical-n256: energy_balance_relative": true,
    "cylindrical-n512: finite positive density": true,
    "cylindrical-n512: pressure within roundoff": true,
    "cylindrical-n512: no state floors": true,
    "cylindrical-n512: mass_balance_relative": true,
    "cylindrical-n512: energy_balance_relative": true,
    "spherical-n64: finite positive density": true,
    "spherical-n64: pressure within roundoff": true,
    "spherical-n64: no state floors": true,
    "spherical-n64: mass_balance_relative": true,
    "spherical-n64: energy_balance_relative": true,
    "spherical-n128: finite positive density": true,
    "spherical-n128: pressure within roundoff": true,
    "spherical-n128: no state floors": true,
    "spherical-n128: mass_balance_relative": true,
    "spherical-n128: energy_balance_relative": true,
    "spherical-n256: finite positive density": true,
    "spherical-n256: pressure within roundoff": true,
    "spherical-n256: no state floors": true,
    "spherical-n256: mass_balance_relative": true,
    "spherical-n256: energy_balance_relative": true,
    "spherical-n512: finite positive density": true,
    "spherical-n512: pressure within roundoff": true,
    "spherical-n512: no state floors": true,
    "spherical-n512: mass_balance_relative": true,
    "spherical-n512: energy_balance_relative": true,
    "planar: finest density_l1": true,
    "planar: finest shock_error_in_dx": true,
    "planar: finest plateau_density_relative_error": true,
    "planar: finest plateau_pressure_relative_error": true,
    "planar: finest mass_vs_analytic_relative": true,
    "planar: finest energy_vs_analytic_relative": true,
    "planar: density L1 decreases": true,
    "planar: last-pair L1 order": true,
    "planar: unmasked center heating reported": true,
    "cylindrical: finest density_l1": true,
    "cylindrical: finest shock_error_in_dx": true,
    "cylindrical: finest plateau_density_relative_error": true,
    "cylindrical: finest plateau_pressure_relative_error": true,
    "cylindrical: finest mass_vs_analytic_relative": true,
    "cylindrical: finest energy_vs_analytic_relative": true,
    "cylindrical: density L1 decreases": true,
    "cylindrical: last-pair L1 order": true,
    "cylindrical: unmasked center heating reported": true,
    "spherical: finest density_l1": true,
    "spherical: finest shock_error_in_dx": true,
    "spherical: finest plateau_density_relative_error": true,
    "spherical: finest plateau_pressure_relative_error": true,
    "spherical: finest mass_vs_analytic_relative": true,
    "spherical: finest energy_vs_analytic_relative": true,
    "spherical: density L1 decreases": true,
    "spherical: last-pair L1 order": true,
    "spherical: unmasked center heating reported": true,
    "spherical-n64: radial momentum balance relative": true,
    "spherical-n64: mass temporal bias identity relative": true,
    "spherical-n64: energy temporal bias identity relative": true,
    "spherical-n64: finite center diagnostics": true,
    "spherical-n128: radial momentum balance relative": true,
    "spherical-n128: mass temporal bias identity relative": true,
    "spherical-n128: energy temporal bias identity relative": true,
    "spherical-n128: finite center diagnostics": true,
    "spherical-n256: radial momentum balance relative": true,
    "spherical-n256: mass temporal bias identity relative": true,
    "spherical-n256: energy temporal bias identity relative": true,
    "spherical-n256: finite center diagnostics": true,
    "spherical-n512: radial momentum balance relative": true,
    "spherical-n512: mass temporal bias identity relative": true,
    "spherical-n512: energy temporal bias identity relative": true,
    "spherical-n512: finite center diagnostics": true,
    "spherical: finest core density_l1 (origin included)": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/index.json

![Origin heating, signed density error and whole-domain L1/L2/Linf for all three symmetries. Full-domain norms retain the origin and shock.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-errors.png)

Origin heating, signed density error and whole-domain L1/L2/Linf for all three symmetries. Full-domain norms retain the origin and shock.

![Spherical diagnostics separate discrete budgets, differences from analytic totals, the sum(dt^3) boundary-quadrature prediction and origin-inclusive core error.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-spherical-budget.png)

Spherical diagnostics separate discrete budgets, differences from analytic totals, the sum(dt^3) boundary-quadrature prediction and origin-inclusive core error.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/atlas-noh-2026-11-23-r5.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  Publisher metadata and abstract checked; full original text was not accessed (403). Cited for the problem and heating-error analysis, not as the source of this particular finite-volume discretization.
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  Checked the LANL software record and separately executed unmodified Noh code at commit 9bacc477eb791e959c9621e771fc7a725db755fa. Cross-checks use only gamma=5/3 and rho0=|u0|=1: points and shock-split Gauss integration of conservative means. Retain that d=3 analytic-comparison receipt; this edition separately executes its spherical PDE series.
- van Leer, Bram (1979). Towards the ultimate conservative difference scheme. V. A second-order sequel to Godunov's method. https://www.sciencedirect.com/science/article/pii/0021999179901451; review_level=existing-atlas-publisher-record-and-abstract
  Existing Atlas bibliography record. Background for limited linear reconstruction and limiters, not a claim to reproduce the full original algorithm or a general positivity theorem for geometric-source zero-pressure Euler.
- Sweby, P. K. (1984). High Resolution Schemes Using Flux Limiters for Hyperbolic Conservation Laws. https://epubs.siam.org/doi/10.1137/0721062; review_level=existing-atlas-publisher-record-and-abstract
  Existing Atlas bibliography record. Background for limited linear reconstruction and limiters, not a claim to reproduce the full original algorithm or a general positivity theorem for geometric-source zero-pressure Euler.
- Mignone, Andrea (2014). High-order conservative reconstruction schemes for finite volume methods in cylindrical and spherical coordinates. https://arxiv.org/abs/1404.0537; review_level=original-arxiv-selected-sections-2.2-3.1-4.2
  Selected original arXiv sections 2.2, 3.1 and 4.2 checked for volume centroids, conservative linear reconstruction and source integration. The restricted minmod/Rusanov/Heun and numerical-stress source are Atlas choices, distinct from reproducing the full paper scheme.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
