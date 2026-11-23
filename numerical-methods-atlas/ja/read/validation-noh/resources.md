# Noh衝撃波：厳密解・過熱誤差・格子収束

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-noh/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  全系列でRusanov流束とHeunを使います。平面・円筒は区分定数、球だけ体積重心でのMUSCL/minmodと線形面応力の球殻求積を使用し、同じ105条件で不合格の定数再構築2系列とも比較します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  全系列でRusanov流束とHeunを使います。平面・円筒は区分定数、球だけ体積重心でのMUSCL/minmodと線形面応力の球殻求積を使用し、同じ105条件で不合格の定数再構築2系列とも比較します。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  全系列でRusanov流束とHeunを使います。平面・円筒は区分定数、球だけ体積重心でのMUSCL/minmodと線形面応力の球殻求積を使用し、同じ105条件で不合格の定数再構築2系列とも比較します。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  全系列でRusanov流束とHeunを使います。平面・円筒は区分定数、球だけ体積重心でのMUSCL/minmodと線形面応力の球殻求積を使用し、同じ105条件で不合格の定数再構築2系列とも比較します。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 理想気体Eulerの平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)のNoh流入問題。幾何源、冷たい流入、反射原点、p0=0と境界時間求積は実行例で定義します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-algorithm>)

  Rusanov流束とSSPRK2（Heun）を使用します。平面・円筒は従来の区分定数再構築、球は保存量を体積重心の周りにMUSCL型線形再構築し、内部セルは重心間距離によるminmod傾きを使い、両端の境界セルは傾き0とします。各セル共通の係数θで左右面の全保存量傾きを縮小し、密度と内部エネルギーの面状態を検査します。セル平均の修正・圧力seed・floorは使いません。波速、Rusanov流束、数値応力P*=F_mom−((u_L+u_R)/2)F_massは同じ面状態から計算し、幾何CFLはV/(A_La_L+A_Ra_R)、指定値.35です。球では線形面応力の∫2rP*(r)drを厳密積分、平面・円筒は旧算術平均求積を保持します。反射面は再構築後の面状態を偶奇反転し、外側の冷たい流入は物理流束で与えます。各RK段の有限性・密度・内部エネルギーを検査し、不正なら失敗を記録します。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock-preview.png
- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r5/noh/results/noh-shock.png

## 厳密解・参照解

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/noh/?lang=ja#references-ja>)

  同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
- [Nohの冷たい流入衝撃波：平面・円筒・球対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。 同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。
- [Nohの冷たい流入衝撃波：平面・円筒・球対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。
- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja#noh-shock-ja-validation>)

  旧平面・円筒の受入基準と59判定を保持し、球の追加基準・入力・ソースhashを初回の球PDE実行前に保存します。初回の円筒不合格はソース・全8本の診断ログ・不合格サマリーを保持し、同じ基準で面応力版を再検証した履歴です。厳密保存量セル平均は衝撃をまたぐ積分を分割し、p(平均U)と平均pを分けます。固定版LANL ExactPackの独立解析照合はd=1/2/3を含みます。球の新規PDE系列では全域r²重みL1/L2/L∞、原点を含むr≤.70rsの密度L1、原点・衝撃・plateauを別測定。各段の境界流入による離散保存収支と、連続解析総量との差を分け、M_h−M_exact=Σdt³/6、E_h−E_exact=Σdt³/12というSSPRK2境界求積の恒等式を検査します。 最初の球対称実行は旧算術平均源のまま105条件中2条件で不合格（最細衝撃位置3.923セル、plateau密度誤差11.03%）となり、全結果を保存しました。第2試行は球の面応力求積だけを変更しましたが、同じ2条件が未達（衝撃位置3.919セル、密度誤差11.018%）でした。第3試行はその求積を保ち、球だけMUSCL・minmod再構築を加えて、同じ105条件で比較します。 第3試行は28検査と全12格子計算を完了し、105条件すべてに合格しました。球N=512では全域密度L1=.0114343、衝撃位置誤差1.98856セル、plateau密度誤差5.2533%、原点込みcore密度L1=.0549503です。一方、中心最大比内部エネルギーの相対過剰は20.59%で、第2試行の15.52%より悪化しており、全指標の改善は主張しません。
- [Nohの冷たい流入衝撃波：平面・円筒・球対称](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-noh-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 理想気体Euler、γ=5/3、初期密度1・内向き速度1・圧力0。r∈[0,1]、t=0.6。平面(d=1)・円筒半径対称(d=2)・球半径対称(d=3)の有限体積計算で、圧力の床は使いません。球のカラー図は1次元半径データの中心断面で、Cartesianの3次元計算ではありません。 同じ初期圧力ゼロのNoh問題の連続厳密解です。初期密度からの増幅4^dと、衝撃波そのものの密度比4を区別します。有限体積の比較は保存量の厳密体積平均を使い、p(平均U)と平均pを別に示します。

## コード・検証

- [Noh衝撃波：初期圧力ゼロの平面・円筒・球対称計算](<https://hrkoyama.github.io/numerical-methods-atlas/validation/noh-shock/?lang=ja>)
  availability: run

  初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。
