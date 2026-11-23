# Double Mach反射：多格子の軽量検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-double-mach/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Godunov型有限体積法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja>)

  既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 同じMach10設定・γ=1.4の圧縮性Euler系を、長方形[0,4]×[0,1]の全域で更新します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-algorithm>)

  既存Numartの区分定数HLL流束と非分割x/y発散、Heun/SSPRK(2,2)を独立した小型配布物にし、両段の境界流束・状態確認を追加しました。CFL=.4を各方向の最大音響速度の和に適用し、上辺は各RK段の実時刻で更新します。状態floor、セル修復、隠れた刻み再試行はなく、不正段の生配列と履歴を残して失敗します。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [二重Mach反射](<https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png
- [Double Mach反射：多格子の軽量検証](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection.png

## 厳密解・参照解

- [二重Mach反射：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja>)

  公開済みの低解像度HLL像を保持し、別の有限体積コードの保存参照との比較を追加します。参照も有限格子の数値解であり、全場の厳密解や誤差上界ではありません。
- [Double Mach反射：保存済み独立有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 領域[0,4]×[0,1]の2次元理想気体Euler、γ=1.4、Mach10・角度60度の入射衝撃波、初期の衝撃脚x=1/6、最終時刻T=.2。保存参照は別実装の非分割primitive MUSCL/HLL/Heun有限体積法（勾配制限はgeneralized minmodのθ=1.5、MC型であり標準MCのθ=2とは異なる）で、256×64と512×128セルです。主計算とHLLという流束族・Heun時間積分の数式を共有しますが、空間再構成と実装は別です。保存量を保つ制限で比較用セル平均を得ます。不変のRKDG2Dキットで以前に実行したソース・配列・記録を再利用し、今回の参照PDE・Athena・LAVAの新規実行ではありません。参照の格子差も有限分解能の感度指標で、厳密な誤差上界ではありません。厳密2D解でも細いwall jet・渦構造の収束検証でもありません。 入射不連続面の初期化はセル中心での状態判定であり、衝撃面で切られたセルの厳密平均からの初期化ではありません。 以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。
- [Double Mach反射：保存済み独立有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 領域[0,4]×[0,1]の2次元理想気体Euler、γ=1.4、Mach10・角度60度の入射衝撃波、初期の衝撃脚x=1/6、最終時刻T=.2。保存参照は別実装の非分割primitive MUSCL/HLL/Heun有限体積法（勾配制限はgeneralized minmodのθ=1.5、MC型であり標準MCのθ=2とは異なる）で、256×64と512×128セルです。主計算とHLLという流束族・Heun時間積分の数式を共有しますが、空間再構成と実装は別です。保存量を保つ制限で比較用セル平均を得ます。不変のRKDG2Dキットで以前に実行したソース・配列・記録を再利用し、今回の参照PDE・Athena・LAVAの新規実行ではありません。参照の格子差も有限分解能の感度指標で、厳密な誤差上界ではありません。厳密2D解でも細いwall jet・渦構造の収束検証でもありません。 入射不連続面の初期化はセル中心での状態判定であり、衝撃面で切られたセルの厳密平均からの初期化ではありません。
- [Double Mach反射：多格子の軽量検証：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-validation>)

  初回事前契約の20単体検査は合格。全3格子の実行前の読み取りレビューで、衝撃探索窓に前線が無い場合を拒否する診断ガードと1検査を追加し、旧契約・ソースを保持して改訂契約を固定しました。その21検査と全3計算・40判定が-W errorで合格しました。参照はRKDGキットで既に独立実行済みの、別実装primitive MUSCL/generalized-minmod θ=1.5/HLL/HeunのNy64/128データを再利用し、今回は参照PDEを再実行していません。Ny128保存量を保守的に制限して比較した密度L1は.08431/.05802/.03503、圧力L1は.09556/.06798/.04156。参照64/128増分は.00955/.01250で、最細主計算差の約.273/.301です。4保存量の境界収支の最大相対残差は約4.60e-13でした。
- [Double Mach反射：保存済み独立有限格子数値参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 領域[0,4]×[0,1]の2次元理想気体Euler、γ=1.4、Mach10・角度60度の入射衝撃波、初期の衝撃脚x=1/6、最終時刻T=.2。保存参照は別実装の非分割primitive MUSCL/HLL/Heun有限体積法（勾配制限はgeneralized minmodのθ=1.5、MC型であり標準MCのθ=2とは異なる）で、256×64と512×128セルです。主計算とHLLという流束族・Heun時間積分の数式を共有しますが、空間再構成と実装は別です。保存量を保つ制限で比較用セル平均を得ます。不変のRKDG2Dキットで以前に実行したソース・配列・記録を再利用し、今回の参照PDE・Athena・LAVAの新規実行ではありません。参照の格子差も有限分解能の感度指標で、厳密な誤差上界ではありません。厳密2D解でも細いwall jet・渦構造の収束検証でもありません。 入射不連続面の初期化はセル中心での状態判定であり、衝撃面で切られたセルの厳密平均からの初期化ではありません。 以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

## コード・検証

- [Double Mach反射：多格子の軽量検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja>)
  availability: run

  既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。
