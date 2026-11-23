# Noh衝撃波：厳密解・過熱誤差・格子収束

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  新しい専用配布版は区分定数Rusanov流束とSSPRK2/Heunを使用します。旧Eulerモジュールを圧力床で変更したものではなく、半径方向の面応力を用いる独自の整合的一次源項を検証します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  新しい専用配布版は区分定数Rusanov流束とSSPRK2/Heunを使用します。旧Eulerモジュールを圧力床で変更したものではなく、半径方向の面応力を用いる独自の整合的一次源項を検証します。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 理想気体Eulerの平面(d=1)・円筒対称半径方向(d=2)のNoh流入問題。幾何源・冷たい外境界・反射原点と真のp0=0の扱いは実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-algorithm>)

  区分定数再構築のlocal Lax–Friedrichs/Rusanov流束とSSPRK2（Heun）。幾何CFLはV/(A_L a_L+A_R a_R)に基づきます。運動量の幾何源は面の数値法線応力P*=F_mom−((u_L+u_R)/2)F_massを左右平均しΔAで積分する独自の整合的一次求積です。静止定圧では厳密相殺、d=1では源がゼロ。反射面の数値応力を原点セルへ伝え、cold流の特異な蓄積を避けます。保存量・圧力のfloor、クリッピング、厳密解への置換はありません。丸め誤差内の負内部エネルギーは記録し、音速の平方根引数だけゼロを使います。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock-preview.png
- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/noh/results/noh-shock.png

## 厳密解・参照解

- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja>)

  同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
- [Nohの冷たい流入衝撃波：平面・円筒対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)と円筒対称の半径方向(d=2)の有限体積計算で、圧力の床は使いません。カラー図は1次元の半径方向解を回転表示したもので、Cartesianの2次元計算ではありません。 同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
- [Nohの冷たい流入衝撃波：平面・円筒対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)と円筒対称の半径方向(d=2)の有限体積計算で、圧力の床は使いません。カラー図は1次元の半径方向解を回転表示したもので、Cartesianの2次元計算ではありません。
- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-validation>)

  入力・受入基準・hashを初回実行前に保存。セル平均圧力p_iΔAを使った初回は平面のみ合格し、円筒はshock不形成で不合格。そのソース・全系列結果を保持し、同じ閾値でinterface-stress版を再実行しました。厳密保存量セル平均は衝撃をまたぐ積分を解析的に分割し、p(U平均)と圧力の体積平均を別列に保存。独立LANL ExactPack固定版から点値・分割求積平均を別実行して照合。全域の相対体積重みL1/L2/Linfと、原点・衝撃・plateauのマスク別診断、shock半値位置、密度増幅4^d（衝撃自体の跳躍は4）、SSPRK2各段の境界流入を積算した保存収支を検査します。
- [Nohの冷たい流入衝撃波：平面・円筒対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)と円筒対称の半径方向(d=2)の有限体積計算で、圧力の床は使いません。カラー図は1次元の半径方向解を回転表示したもので、Cartesianの2次元計算ではありません。 同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

## コード・検証

- [Noh衝撃波：初期圧力ゼロの平面・円筒対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  圧力をゼロから始めるNoh問題を、独自の小型1D有限体積ソルバーで平面・円筒半径対称に計算します。64/128/256/512格子で体積重み誤差、衝撃位置、密度増幅、原点過熱、外側流入を含む質量・全エネルギー収支を別々に測ります。
