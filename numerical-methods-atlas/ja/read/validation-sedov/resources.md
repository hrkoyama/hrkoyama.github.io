# Sedov–Taylor点爆発：球対称の軽量検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-sedov/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  区分定数のRusanov有限体積流束とSSPRK2/Heunを使う限定した球半径例です。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  区分定数のRusanov有限体積流束とSSPRK2/Heunを使う限定した球半径例です。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 無次元の球半径対称Euler系。1D半径方向の密度・運動量・全エネルギーを体積重み付きで発展させます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-algorithm>)

  球殻体積と面積を用いる区分定数Rusanov流束＋SSPRK2（Heun）です。半径運動量の幾何源p(A右−A左)/Vを同じRK段で積分し、静止した一様圧力との釣り合いも検査します。CFL=.4は各セルのV/(A左+A右)/(|u|+c)の最小値を使います。圧力seed・floor・セル平均修復・隠れた刻み再試行はなく、不正な段は生の保存量と履歴を保存して失敗とします。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Sedov–Taylorの点爆発](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast-preview.png
- [Sedov–Taylor点爆発：球対称の軽量検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sedov/results/sedov-blast.png

## 厳密解・参照解

- [Sedov–Taylorの点爆発：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sedov/?lang=ja#references-ja>)

  エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。
- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=5/3、周囲密度1・圧力0、爆発エネルギー1、r∈[0,1]、t=0.05。自己相似参照は瞬間的な理想点源を表しますが、有限体積計算は半径0.03の内部へ投入し、同じ最細格子で半径0.015も比較します。参照は相似ODEの数値積分、小さな中心域の正則漸近形、衝撃位置で分割する球殻求積を含む半解析解であり、閉形式の厳密セル平均ではありません。ギャラリー図は1次元球半径データの中心断面で、2D Cartesian計算ではありません。固定投入半径での誤差には点源とのモデル差が含まれ、その傾きは純粋な空間収束次数ではなく、投入半径の変更も感度診断に留まります。 エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。
- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja>)
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=5/3、周囲密度1・圧力0、爆発エネルギー1、r∈[0,1]、t=0.05。自己相似参照は瞬間的な理想点源を表しますが、有限体積計算は半径0.03の内部へ投入し、同じ最細格子で半径0.015も比較します。参照は相似ODEの数値積分、小さな中心域の正則漸近形、衝撃位置で分割する球殻求積を含む半解析解であり、閉形式の厳密セル平均ではありません。ギャラリー図は1次元球半径データの中心断面で、2D Cartesian計算ではありません。固定投入半径での誤差には点源とのモデル差が含まれ、その傾きは純粋な空間収束次数ではなく、投入半径の変更も感度診断に留まります。
- [Sedov–Taylor点爆発：球対称の軽量検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja#sedov-blast-ja-validation>)

  入力・数値ソース・受入基準・22テストを初回計算前にhash固定し、22単体検査と全4計算・48判定が初回から合格しました。参照は独立な相似ODEのDOP853積分、エネルギー規格化、中心ξ<.001の正則漸近形と衝撃位置で分割する殻求積です。16/32点求積・中心cutoff/ODE公差を別々に確認。固定commitの未改変ExactPackを6001/12001点で別実行し、中心とジャンプから離れた点を事前基準5e-4で照合しました。β=1.15166641793、Rs(.05)=.34746791233。原点・衝撃波を含むr≤1.2Rsの体積重み密度L1は.17257/.12785/.07458、圧力L1は.18148/.13939/.07615。512セルの衝撃位置誤差は1.096セル、最大離散収支残差は約1.34e-15です。
- [Sedov–Taylorの点爆発：エネルギー正規化した球対称自己相似解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sedov-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 理想気体Eulerの球半径対称、γ=5/3、周囲密度1・圧力0、爆発エネルギー1、r∈[0,1]、t=0.05。自己相似参照は瞬間的な理想点源を表しますが、有限体積計算は半径0.03の内部へ投入し、同じ最細格子で半径0.015も比較します。参照は相似ODEの数値積分、小さな中心域の正則漸近形、衝撃位置で分割する球殻求積を含む半解析解であり、閉形式の厳密セル平均ではありません。ギャラリー図は1次元球半径データの中心断面で、2D Cartesian計算ではありません。固定投入半径での誤差には点源とのモデル差が含まれ、その傾きは純粋な空間収束次数ではなく、投入半径の変更も感度診断に留まります。 エネルギー正規化した球対称の自己相似参照。相似ODEの数値積分・球殻平均の求積を含む半解析解で、閉形式の厳密セル平均とは区別します。有限半径の投入初期値は理想点爆発の特異初期値と一致しません。 固定した有限の投入半径で点源の自己相似参照と比べるため、誤差曲線には投入モデルの差も含まれ、純粋な空間精度の収束次数ではありません。同じ最細格子で投入半径を変える比較は感度診断であり、連続極限の投入誤差とPDE離散化誤差を完全に分離する検証ではありません。

## コード・検証

- [Sedov–Taylor点爆発：球対称の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sedov-blast/?lang=ja>)
  availability: run

  球対称Euler方程式を半径方向の有限体積法で解く軽量例です。固定した半径0.03の領域に総エネルギー1を与え、128・256・512セルで点爆発の相似参照からの差と保存収支を測ります。図は1次元球対称データの断面表示で、2次元Cartesian計算ではありません。
