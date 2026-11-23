# Noh衝撃波：厳密解・過熱誤差・格子収束

初期圧力ゼロの平面・円筒対称Noh問題を小さな有限体積コードで解きます。原著と固定版ExactPackを引用し、厳密解・体積平均・原点過熱・保存収支と、残る誤差を一緒に確認します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Noh衝撃波：初期圧力ゼロの平面・円筒対称計算

圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。

**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-algorithm)

区分定数再構築のlocal Lax–Friedrichs/Rusanov流束とSSPRK2（Heun）。幾何CFLはV/(A_L a_L+A_R a_R)に基づきます。運動量の幾何源は面の数値法線応力P*=F_mom−((u_L+u_R)/2)F_massを左右平均しΔAで積分する独自の整合的一次求積です。静止定圧では厳密相殺、d=1では源がゼロ。反射面の数値応力を原点セルへ伝え、cold流の特異な蓄積を避けます。保存量・圧力のfloor、クリッピング、厳密解への置換はありません。丸め誤差内の負内部エネルギーは記録し、音速の平方根引数だけゼロを使います。

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

理想気体Eulerの平面・円筒半径対称という限定した形です。幾何源と初期圧力ゼロの条件は、この実行例の式・固定入力で定義します。


**問題の図**

![Noh衝撃波：初期圧力ゼロの平面・円筒対称計算：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja) (`noh`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-validation)

入力・受入基準・hashを初回実行前に保存。セル平均圧力p_iΔAを使った初回は平面のみ合格し、円筒はshock不形成で不合格。そのソース・全系列結果を保持し、同じ閾値でinterface-stress版を再実行しました。厳密保存量セル平均は衝撃をまたぐ積分を解析的に分割し、p(U平均)と圧力の体積平均を別列に保存。独立LANL ExactPack固定版から点値・分割求積平均を別実行して照合。全域の相対体積重みL1/L2/Linfと、原点・衝撃・plateauのマスク別診断、shock半値位置、密度増幅4^d（衝撃自体の跳躍は4）、SSPRK2各段の境界流入を積算した保存収支を検査します。

- [Nohの冷たい流入衝撃波：平面・円筒対称](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja) (`noh`; 同じ問題の参照 · 解析参照)

同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
### 前提・単位・境界

無次元r∈[0,1]、gamma=5/3、rho0=1、u0=-1、p0=0、T=.6。平面d=1と円筒半径対称d=2だけをPDE実行し、衝撃半径は.2。外側はrho(1,t)=1+tの円筒低温流入（平面は1）。原点は反射、体積測度r^(d-1)dr、角度因子は全ての収支から共通に省きます。球対称の解析参照検査とCartesian 2D Euler計算を混同しません。

**編集上の補足**

初回不合格の保存物は、実行ソース・入力・全8格子計算の診断ログと、そこから原文のまま抽出した不合格サマリーです。初回の全場CSVが保存されているという意味ではありません。公開する成功版は、別途生成した全断面CSV・履歴・結果とZIP独立展開の再実行記録を備えます。

### 採用した計算法

区分定数再構築のlocal Lax–Friedrichs/Rusanov流束とSSPRK2（Heun）。幾何CFLはV/(A_L a_L+A_R a_R)に基づきます。運動量の幾何源は面の数値法線応力P*=F_mom−((u_L+u_R)/2)F_massを左右平均しΔAで積分する独自の整合的一次求積です。静止定圧では厳密相殺、d=1では源がゼロ。反射面の数値応力を原点セルへ伝え、cold流の特異な蓄積を避けます。保存量・圧力のfloor、クリッピング、厳密解への置換はありません。丸め誤差内の負内部エネルギーは記録し、音速の平方根引数だけゼロを使います。

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
V_i=(r_{i+1/2}^d-r_{i-1/2}^d)/d,\quad P_f^*=\widehat F_{m,f}-\bar u_f\widehat F_{\rho,f},\quad S_{m,i}V_i=\tfrac12(P_{i-1/2}^*+P_{i+1/2}^*)(A_{i+1/2}-A_{i-1/2})
$$

$$
\mathcal E_1=\frac{\sum_iV_i|\bar\rho_i-\bar\rho_i^{\rm exact}|}{\sum_iV_i\bar\rho_i^{\rm exact}},\quad M(t)=\rho_0(R+|u_0|t)^d/d,\quad E_{\rm tot}(t)=u_0^2M(t)/2
$$

### 比較・検証

入力・受入基準・hashを初回実行前に保存。セル平均圧力p_iΔAを使った初回は平面のみ合格し、円筒はshock不形成で不合格。そのソース・全系列結果を保持し、同じ閾値でinterface-stress版を再実行しました。厳密保存量セル平均は衝撃をまたぐ積分を解析的に分割し、p(U平均)と圧力の体積平均を別列に保存。独立LANL ExactPack固定版から点値・分割求積平均を別実行して照合。全域の相対体積重みL1/L2/Linfと、原点・衝撃・plateauのマスク別診断、shock半値位置、密度増幅4^d（衝撃自体の跳躍は4）、SSPRK2各段の境界流入を積算した保存収支を検査します。

### 確認の限界

空間一次・衝撃捕獲の教育用ソルバーです。最細円筒でもplateau密度誤差と原点過熱が残り、中心最大誤差のゼロ収束・正値性の一般証明・高次精度・Cartesian多次元・球対称PDE・任意gammaの独立照合を主張しません。全域誤差から原点を除外せず、中心過熱を合格のために隠しません。質量/エネルギー収支だけでは解の正しさを証明できないことを初回失敗で示します。ExactPackは解析参照の独立実装であり、独立PDEエンジンではありません。 円筒の全域密度L∞はこの系列では単調減少しません。収束の合格判定は事前に指定した体積重みL1で行い、L∞も隠さず保存します。

### 保存実測値と判定

```json
{
  "metrics": {
    "planar_density_l1_finest": 0.006389021550074538,
    "planar_density_l2_finest": 0.035622324219688015,
    "planar_density_linf_finest": 0.2913310649697939,
    "planar_density_l1_order_finest": 1.088972053769089,
    "planar_shock_error_finest": 0.0006243356111319265,
    "planar_center_max_sie_relative_excess_finest": 0.025776017620378955,
    "cylindrical_density_l1_finest": 0.01868269537157265,
    "cylindrical_density_l2_finest": 0.10813806869356997,
    "cylindrical_density_linf_finest": 0.5794791984687887,
    "cylindrical_density_l1_order_finest": 0.9603991144824785,
    "cylindrical_shock_error_finest": 0.004146970746716938,
    "cylindrical_center_max_sie_relative_excess_finest": 0.08161167421978366
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
    "cylindrical: unmasked center heating reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/atlas-noh-2026-11-23-r3.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- W. F. Noh (1987). Errors for calculations of strong shocks using an artificial viscosity and an artificial heat flux. https://www.sciencedirect.com/science/article/pii/002199918790074X; review_level=publisher-metadata-and-abstract
  出版社書誌・抄録を確認。原著本文の直接取得は403のため全文未読。Noh問題・過熱誤差の原著として引用し、今回の有限体積離散化そのものの出典とは呼びません。
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-unmodified-pinned-code-execution
  LANL公式書誌と固定commit 9bacc477eb791e959c9621e771fc7a725db755faのNohコードを確認・別実行。gamma=5/3,rho0=|u0|=1に限定し、点値と衝撃を分割したGauss積分で参照保存量平均を照合。3次元の解析参照検査は球対称PDEの実行を意味しません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
