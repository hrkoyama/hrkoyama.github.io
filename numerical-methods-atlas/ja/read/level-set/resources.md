# レベルセット法：動く界面とVOFとの比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/level-set/

この章に登録された手法・問題・実行例の関連資料です。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

## 手法

- [レベルセット法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja>)
- [VOF法／体積率による界面捕獲](<https://hrkoyama.github.io/numerical-methods-atlas/methods/vof/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja>)
- [レベルセット法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja>)

  専用の2D ENO2／Heunレベルセット移流。任意選択の単純なGodunov再初期化による面積変化も保存し、VOF実装を割り当てません。

## 方程式

- [レベルセット界面の移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja>)

  ゼロ等値線で界面を表す非保存形の移流式。円の平行移動・剛体回転を検証し、VOFの体積率輸送と区別します。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [レベルセット界面の移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#level-set-advection-ja>)

  ゼロ等値線で界面を表す非保存形の移流式。円の平行移動・剛体回転を検証し、VOFの体積率輸送と区別します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-algorithm>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-algorithm>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 移流は両モードで同じ2次ENO片側微分とHeun RK2。2階差分の絶対値でステンシルを選択します。再初期化ありでは物理時刻.1ごとに、呼出し開始時の平滑符号を固定した1次Godunov法をΔτ=.3Δxで5回実行。体積補正、界面への投影、φのclip、隠れたretry、内部の解析解への置換を行いません。

## 問題の図

- [レベルセットで表した円の移流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-overview.png
- [レベルセット円の2D平行移動：界面・面積・再初期化](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-translation.png
- [偏心したレベルセット円の2D剛体回転](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/level-set/results/level-set-rotation.png

## 厳密解・参照解

- [レベルセットで表した円の移流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/level-set-circle/?lang=ja#references-ja>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja>)
  reference_kind: analytic

  解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。
- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja>)
  reference_kind: analytic

  解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。
- [レベルセット円の2D平行移動：界面・面積・再初期化：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja#level-set-translation-ja-validation>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。
- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja>)
  relation: same-problem
  reference_kind: analytic

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja>)
  relation: same-problem
  reference_kind: analytic

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [偏心したレベルセット円の2D剛体回転：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja#level-set-rotation-ja-validation>)

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析的な円の中心運動と符号付き距離を参照し、4つの正の共通時刻の最悪値を測定します。界面位置は格子辺上で線形補間したφ=0点の半径誤差、面積は格子中心間を三角形に分けた区分線形φの負領域から計算。初期の幾何学的な面積偏りも残します。|φ厳密|≤2Δx帯のφ誤差と距離勾配、各再初期化による面積変化、N64でのCourant半減も別記録。
- [レベルセット円の2D平行移動：界面・面積・再初期化：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-translation-ja>)
  relation: same-problem
  reference_kind: analytic

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。
- [偏心したレベルセット円の2D剛体回転：解析的符号付き距離参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-level-set-rotation-ja>)
  relation: same-problem
  reference_kind: analytic

  円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。 解析解 全て無次元、領域[0,1]²、内部φ<0。与えた非圧縮の剛体運動だけを解き、円は境界から離れます。外側2層のゴースト値は各RK段階で解析解を指定します。周期境界ではなく、内部のφは数値更新します。出力時刻0/.25/.5/.75/1、物理Courant数max(|u|+|v|)Δt/Δx≤.35。 円の平行移動と偏心した剛体回転の解析的な中心運動・符号付き距離が参照です。2モードの面積・界面誤差を測り、VOFや二相流の実行とは区別します。

## コード・検証

- [レベルセット円の2D平行移動：界面・面積・再初期化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-translation/?lang=ja>)
  availability: run

  中心(.3,.35)の半径.15の円を速度(.2,.1)でT=1まで平行移動します。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。
- [偏心したレベルセット円の2D剛体回転](<https://hrkoyama.github.io/numerical-methods-atlas/validation/level-set-rotation/?lang=ja>)
  availability: run

  中心(.68,.5)の半径.15の円を(.5,.5)周りに角速度2πで1周回転させます。32²/64²/128²のENO2＋Heunを用い、再初期化の有無、途中の界面位置、面積誤差と格子・刻みの細分化を比べます。
- [レベルセット法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/level-set/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
