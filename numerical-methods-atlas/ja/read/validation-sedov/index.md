# Sedov–Taylor点爆発：球対称の軽量検証

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Sedov–Taylor点爆発：球対称の軽量検証

球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。

**使用手法**

- [Rusanov／局所Lax–Friedrichs流束](https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja) (`rusanov`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-algorithm)

球殻体積と面積を用いる区分定数Rusanov流束＋SSPRK2（Heun）です。半径運動量の幾何源p(A右−A左)/Vを同じRK段で積分し、静止した一様圧力との釣り合いも検査します。CFL=.4は各セルのV/(A左+A右)/(|u|+c)の最小値を使います。圧力seed・floor・セル平均修復・隠れた刻み再試行はなく、不正な段は生の保存量と履歴を保存して失敗とします。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`)

理想気体Eulerの1次元球半径対称形。原点反射、幾何源、有限半径へのエネルギー投入と外側境界は、この例の固定入力で定義します。


**問題の図**

![Sedov–Taylor点爆発：球対称の軽量検証：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Sedov–Taylorの点爆発](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja) (`sedov`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-validation)

入力・数値ソース・受入基準・22テストを初回計算前にhash固定し、22単体検査と全4計算・48判定が初回から合格しました。参照は独立な相似ODEのDOP853積分、エネルギー規格化、中心ξ<.001の正則漸近形と衝撃位置で分割する殻求積です。16/32点求積・中心cutoff/ODE公差を別々に確認。固定commitの未改変ExactPackを6001/12001点で別実行し、中心とジャンプから離れた点を事前基準5e-4で照合しました。β=1.15166641793、Rs(.05)=.34746791233。原点・衝撃波を含むr≤1.2Rsの体積重み密度L1は.17257/.12785/.07458、圧力L1は.18148/.13939/.07615。512セルの衝撃位置誤差は1.096セル、最大離散収支残差は約1.34e-15です。

- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja) (`sedov`; 同じ問題の参照 · 半解析参照)

エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。
### 前提・単位・境界

無次元、γ=5/3、初期密度1・速度0・背景圧力0、半径[0,1]、総注入エネルギー1、T=.05。球内一様の熱エネルギーを各殻の切断体積で正確に配分します。注入半径0.03を3格子で共通にし、512セルでは半径0.015の別実行も保存します。原点は鏡映、外端は流出境界で、実際の境界流束を収支へ含めます。

**編集上の補足**

固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

### 採用した計算法

球殻体積と面積を用いる区分定数Rusanov流束＋SSPRK2（Heun）です。半径運動量の幾何源p(A右−A左)/Vを同じRK段で積分し、静止した一様圧力との釣り合いも検査します。CFL=.4は各セルのV/(A左+A右)/(|u|+c)の最小値を使います。圧力seed・floor・セル平均修復・隠れた刻み再試行はなく、不正な段は生の保存量と履歴を保存して失敗とします。

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2F)=\left(0,2p/r,0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=\beta(E_0t^2/\rho_0)^{1/5},\quad\beta\simeq1.15166641793,\quad\dot R_s=2R_s/(5t)
$$

$$
\rho=\rho_0G(\xi),\quad u=\dot R_sV(\xi),\quad p=\rho_0\dot R_s^2P(\xi),\quad\xi=r/R_s
$$

$$
E_0=4\pi\int_0^\infty\left(\frac{p}{\gamma-1}+\frac{\rho u^2}{2}\right)r^2\,dr=1
$$

$$
\bar U_i=\frac{3}{r_{i+1/2}^3-r_{i-1/2}^3}\int_{r_{i-1/2}}^{r_{i+1/2}}U(r)r^2\,dr
$$

### 比較・検証

入力・数値ソース・受入基準・22テストを初回計算前にhash固定し、22単体検査と全4計算・48判定が初回から合格しました。参照は独立な相似ODEのDOP853積分、エネルギー規格化、中心ξ<.001の正則漸近形と衝撃位置で分割する殻求積です。16/32点求積・中心cutoff/ODE公差を別々に確認。固定commitの未改変ExactPackを6001/12001点で別実行し、中心とジャンプから離れた点を事前基準5e-4で照合しました。β=1.15166641793、Rs(.05)=.34746791233。原点・衝撃波を含むr≤1.2Rsの体積重み密度L1は.17257/.12785/.07458、圧力L1は.18148/.13939/.07615。512セルの衝撃位置誤差は1.096セル、最大離散収支残差は約1.34e-15です。

### 確認の限界

有限の注入球と理想点爆発は初期条件が異なり、報告誤差には注入モデルと離散化の両方が含まれます。傾きは純粋な空間精度次数ではありません。同じ512セルで注入半径を半分にした密度差は約.000451、圧力差は約.000619ですが、点爆発参照への誤差は僅かに悪化し、改善や点源極限の証明とは扱いません。圧力誤差は数値p(保存量のセル平均)と参照の物理圧力平均を比較し、参照平均保存量からの圧力と区別します。中心密度・圧力・最大誤差を除外せず保存します。最細密度ピークは約2.918で厳密ジャンプ4を解像しきりません。冷たい裾の極小波速では局所CFL比が浮動小数点overflowで∞になりますが、制限しない比として扱い、選ばれる全体刻みの有限性・正値性を検査します。原点漸近部は近似で、ExactPack点照合もξ<.15を除きます。2D/3D Cartesian、一般摂動・非球対称性、高次精度は未検証です。

### 保存実測値と判定

```json
{
  "metrics": {
    "n": 512,
    "deposit_radius": 0.03,
    "time": 0.05,
    "steps": 4009,
    "density_l1": 0.005369634041936693,
    "active_density_l1": 0.0745788634711047,
    "active_pressure_l1": 0.07615237367293834,
    "density_l2": 0.058313703526242607,
    "density_linf": 0.3892475533701589,
    "density_min": 0.014842231748925943,
    "density_max": 2.918215810146801,
    "pressure_min": 0.0,
    "pressure_max": 4.8023695991464725,
    "maximum_speed": 2.007592026879321,
    "center_density": 0.014842231748925943,
    "center_pressure": 1.641701683913197,
    "center_reference_density": 4.1043889913677827e-11,
    "center_reference_pressure": 1.7744715646691345,
    "shock_radius": 0.349609375,
    "reference_shock_radius": 0.3474679123327071,
    "shock_error_cells": 1.0964288856539781,
    "minimum_density_all_stages": 0.014842231581750319,
    "minimum_pressure_all_stages": 0.0,
    "minimum_internal_roundoff_units": 0.0,
    "state_floor_count": 0,
    "reference_quadrature_density_l1": 1.1766085003791174e-16,
    "reference_quadrature_pressure_l1": 1.1717338251963657e-16,
    "initial_energy_error": 0.0
  },
  "checks": {
    "three fixed-radius refinements complete": true,
    "paired smaller-radius run completes": true,
    "n128: strictly positive density all stages": true,
    "n128: internal energy within roundoff": true,
    "n128: no state floor or repair": true,
    "n128: unit deposited energy": true,
    "n128: mass discrete balance": true,
    "n128: radial momentum including geometric source discrete balance": true,
    "n128: energy discrete balance": true,
    "n128: reference_quadrature_density_l1": true,
    "n128: reference_quadrature_pressure_l1": true,
    "n128: origin and maximum diagnostics retained": true,
    "n256: strictly positive density all stages": true,
    "n256: internal energy within roundoff": true,
    "n256: no state floor or repair": true,
    "n256: unit deposited energy": true,
    "n256: mass discrete balance": true,
    "n256: radial momentum including geometric source discrete balance": true,
    "n256: energy discrete balance": true,
    "n256: reference_quadrature_density_l1": true,
    "n256: reference_quadrature_pressure_l1": true,
    "n256: origin and maximum diagnostics retained": true,
    "n512: strictly positive density all stages": true,
    "n512: internal energy within roundoff": true,
    "n512: no state floor or repair": true,
    "n512: unit deposited energy": true,
    "n512: mass discrete balance": true,
    "n512: radial momentum including geometric source discrete balance": true,
    "n512: energy discrete balance": true,
    "n512: reference_quadrature_density_l1": true,
    "n512: reference_quadrature_pressure_l1": true,
    "n512: origin and maximum diagnostics retained": true,
    "sensitivity: strictly positive density all stages": true,
    "sensitivity: internal energy within roundoff": true,
    "sensitivity: no state floor or repair": true,
    "sensitivity: unit deposited energy": true,
    "sensitivity: mass discrete balance": true,
    "sensitivity: radial momentum including geometric source discrete balance": true,
    "sensitivity: energy discrete balance": true,
    "sensitivity: reference_quadrature_density_l1": true,
    "sensitivity: reference_quadrature_pressure_l1": true,
    "sensitivity: origin and maximum diagnostics retained": true,
    "finest active_density_l1": true,
    "finest active_pressure_l1": true,
    "finest shock_error_cells": true,
    "fixed-source active density L1 decreases": true,
    "last fixed-source density L1 order": true,
    "source-radius effects separately retained": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/atlas-sedov-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

### 出典と確認範囲

- G. I. Taylor (1950). The formation of a blast wave by a very intense explosion I. Theoretical discussion. https://doi.org/10.1098/rspa.1950.0049; review_level=selected-original-pages
  大学公開の原著スキャンpp159–167で相似仮定・Euler縮約・強衝撃条件・エネルギー規格化・中心指数を選択確認。出版社は403で、全文読了やPDF再配布を主張しません。
- J. Thrussell and J. M. Ferguson (2023). ExactPack: A python library of exact analytic solutions. https://doi.org/10.1016/j.softx.2023.101560; review_level=official-record-and-selected-pinned-code-execution
  固定commitの未改変Sedov評価器を6001/12001点で実行。ソースhash・パラメータ・点値・照合判定・BSD-3-Clauseを保存。別のEuler数値ソルバーや全ライブラリ検査ではありません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
