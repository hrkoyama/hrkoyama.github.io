# Noh問題：2次元Cartesianと格子方向の誤差

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh-cartesian/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  RusanovとHeunは1D半径例と新2D Cartesian例で使用。MUSCL/minmodは旧球対称系列に限定され、新2D版は区分定数です。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 1D平面・円筒・球の半径対称Euler系と、実際の2D Cartesian Euler系。2D版には幾何源・半径還元・対称境界がなく、全4辺の冷たい流入を与えます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-algorithm>)

  区分定数のRusanov流束をx/y両方向の共有面に置く非分割更新とSSPRK2（Heun）です。CFL=.35を(max a_x+max a_y)/Δxに適用。外辺の冷たい物理流束は面内で解析積分し、時間に一次の流入をHeunの両段で積分します。セル平均の修復・圧力floor・seed・隠れた時間刻み再試行はなく、不正なRK段は配列を保存して失敗にします。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Noh問題：冷たい収束流と外向き衝撃波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d-preview.png
- [Noh問題：実際の2次元Cartesian Euler計算](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/noh-cartesian/results/noh-cartesian-2d.png

## 厳密解・参照解

- [Noh問題：冷たい収束流と外向き衝撃波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja>)

  同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。
- [Nohの冷たい流入衝撃波：平面・円筒・球対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。 別の実2D Cartesian版では[-.5,.5]²の32²/64²/128²格子、2成分運動量と両方向流束を使い、半径還元は行いません。密度参照は衝撃円で分割した64/128点の求積セル平均です。 同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。
- [Noh問題：実際の2次元Cartesian Euler計算：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja#noh-cartesian-2d-ja-validation>)

  実行前に入力・ソース・受入基準をhash保存。19単体検査と3格子・49判定が初回から合格しました。解析密度のセル積分は衝撃円の交差で区間を分割し、x=rs sinθによる64点Gauss求積で評価、128点との差と全質量の解析式で確認します。閉形式の厳密セル平均とは区別します。128²で密度全域L1=.09981、原点込みcore L1=.12231、衝撃位置は軸.968セル・対角1.469セルの誤差。離散収支の最大相対残差は約4.6e-15です。D4の鏡映・座標交換の保存量偶奇性と、連続回転対称性を区別して測ります。
- [Nohの冷たい流入衝撃波：平面・円筒・球対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。 別の実2D Cartesian版では[-.5,.5]²の32²/64²/128²格子、2成分運動量と両方向流束を使い、半径還元は行いません。密度参照は衝撃円で分割した64/128点の求積セル平均です。 同じNoh問題の解析参照。1Dは保存量の厳密体積平均、2Dは衝撃円で分割した密度の求積セル平均を使用します。点値とセル平均、p(平均U)と平均pを区別します。

## コード・検証

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
- [Noh問題：実際の2次元Cartesian Euler計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-cartesian-2d/?lang=ja>)
  availability: run

  正方形の全域で密度・2成分運動量・全エネルギーを更新する、小型の2次元Euler有限体積計算です。32²・64²・128²の3格子で厳密Noh状態からの誤差・保存収支・格子方向の影響を測ります。図は実際の2次元保存配列で、1D半径解の回転表示ではありません。
