# 補間・スプライン・Haarの固定対照

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-approximation-controls/

この章に登録された手法・問題・実行例の関連資料です。 節点・表現・丸め、C2連続性と形状保存、境界拡張とシフトをそれぞれ分けた小さな固定例です。

## 手法

- [Chebyshev近似](<https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=ja>)

  第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。
- [スプライン補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=ja>)

  3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。
- [PCHIP単調3次Hermite補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=ja>)

  3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。
- [ウェーブレット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=ja>)

  和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。
- [Chebyshev近似](<https://hrkoyama.github.io/numerical-methods-atlas/methods/chebyshev/?lang=ja>)
- [スプライン補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/splines/?lang=ja>)
- [PCHIP単調3次Hermite補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pchip/?lang=ja>)
- [ウェーブレット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/wavelets/?lang=ja>)

## 方程式

- [格納節点の多項式補間](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja>)

  閉形式重みと丸め節点の表現差、補間誤差と演算丸めを分けます。 無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。
- [3次スプラインと形状保存補間](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja>)

  端点条件を持つC2補間と単調な区分Hermite補間を区別します。 実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。
- [有限長信号の離散Haar変換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja>)

  奇数長の追加標本と切戻しを含む有限写像です。冗長拡張全体の直交性は仮定しません。 奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。
- [格納節点の多項式補間](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#polynomial-interpolation-ja>)

  閉形式重みと丸め節点の表現差、補間誤差と演算丸めを分けます。
- [3次スプラインと形状保存補間](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#cubic-spline-pchip-ja>)

  端点条件を持つC2補間と単調な区分Hermite補間を区別します。
- [有限長信号の離散Haar変換](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#discrete-haar-transform-ja>)

  奇数長の追加標本と切戻しを含む有限写像です。冗長拡張全体の直交性は仮定しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-algorithm>)

  第2重心公式と全係数Clenshaw漸化式を自作。丸め済み節点上の閉形式重みと有限Chebyshev変換をそのまま保存します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-algorithm>)

  3次Bスプラインの配置行列を解きde Boor評価。別経路でPCHIPの調和平均・端点制限とHermite評価を実装します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-algorithm>)

  和差フィルタ・間引き・逆ピラミッドを自作。閾値なし・hard・softの3条件を同じ解析係数から再構成します。

## 問題の図

- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw-preview.png
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls-preview.png
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold-preview.png
- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/runge-barycentric-clenshaw.png
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/spline-shape-controls.png
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/approximation-controls/results/haar-mallat-boundary-threshold.png

## 厳密解・参照解

- [節点・表現・丸めを分けるRunge補間：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/runge-barycentric-clenshaw/?lang=ja#references-ja>)

  格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。
- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。 標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。
- [自然・端点微分指定スプラインとPCHIP：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/spline-shape-controls/?lang=ja#references-ja>)

  正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。 PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。
- [Haar多重解像度の境界・シフト・閾値：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/haar-mallat-boundary-threshold/?lang=ja#references-ja>)

  12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。 Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。
- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja>)
  reference_kind: analytic

  解析解 無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja>)
  reference_kind: analytic

  解析解 実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja>)
  reference_kind: analytic

  解析解 奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。
- [節点・表現・丸めを分けるRunge補間：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja#runge-barycentric-clenshaw-ja-validation>)

  格納値の補間多項式P、閉重み有理式R、格納係数級数C、目標関数fを区別。17点の正確な有理参照・演算別誤差上界・節点一致・固定Runge傾向を照合します。
- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-runge-barycentric-clenshaw-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元区間[-1,1]、次数8・16・32、固定2048中点。節点・データ・重みは実際のbinary64値を対象にします。 標本最大誤差は連続一様ノルムの証明ではありません。丸め節点の閉重み・離散直交性は厳密と見なしません。任意次数・任意点の安定性は保証しません。
- [自然・端点微分指定スプラインとPCHIP：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja#spline-shape-controls-ja-validation>)

  正確な有理2階微分系・有理PCHIP・SciPy 1.14.1を照合。端点15記録は16スカラー出力・13異なる入力。平坦部の負値は実binary64をFraction化した独立式で示します。
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-spline-shape-controls-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 実binary64の節点と値を使用。自然条件は両端2階微分ゼロ、clamped条件は入力端点1階微分です。 PCHIPは通常C1でありC2とは限りません。一般データの最良近似・外挿・ノイズ平滑化は対象外。SciPyは原著完全閲読の代用ではありません。
- [Haar多重解像度の境界・シフト・閾値：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja#haar-mallat-boundary-threshold-ja-validation>)

  12解析・36再構成。独立行列・Fraction/Decimal係数、完全再構成、二乗L2誤差を照合。長さ32のみ直交誤差恒等式を要求し、17点では追加エネルギーを段別保存します。
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-haar-mallat-boundary-threshold-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 奇数長の各段で周期型は先頭、対称型は末尾を1点追加し、再構成時に切り戻します。詳細係数のみ閾値0.2を使用。 Haarに限定し長いフィルタや画像圧縮は対象外。一般の対称拡張に正規直交性を仮定しません。シフト不変性は要求せず、シフト別差を保存します。

## コード・検証

- [節点・表現・丸めを分けるRunge補間](<https://hrkoyama.github.io/numerical-methods-atlas/validation/runge-barycentric-clenshaw/?lang=ja>)
  availability: run

  Runge関数と絶対値関数を等間隔・Lobatto型の固定節点で補間し、Clenshaw評価と比較します。
- [自然・端点微分指定スプラインとPCHIP](<https://hrkoyama.github.io/numerical-methods-atlas/validation/spline-shape-controls/?lang=ja>)
  availability: run

  平坦部を持つ単調データ・3次式・直線の固定3組で、C2連続性と形状保存を比較します。
- [Haar多重解像度の境界・シフト・閾値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/haar-mallat-boundary-threshold/?lang=ja>)
  availability: run

  長さ17・32の小信号に3段Haar分解を適用。1標本シフトと奇数長の境界処理を分けて比較します。
