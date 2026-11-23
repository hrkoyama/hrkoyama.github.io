# Euler再構成：PPM・特性変数・WENO-Z・AUSM

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Eulerの特性変数再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=ja>)
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [制限付きPPM再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ppm/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [WENO5-JS](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-js/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [有限差分WENO5-Z](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Eulerの特性変数再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [HLL](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [MUSCL再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Minmod](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [単調中心勾配制限／MC](<https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-shu-osher-ja>)

  初期不連続x=−4、左状態は固定入力を参照。特性有限差分WENO5-Zの点値を比較する。800点参照は同一方式の数値解であり、厳密解・独立ソルバーではない。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

## 問題の図

- [Shu–Osher衝撃波・エントロピー波干渉](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png
- [移動接触不連続](<https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png
- [2次元の滑らかなEulerエントロピー波](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/comparisons/smooth-refinement.png

## 厳密解・参照解

- [Shu–Osher衝撃波・エントロピー波干渉：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#references-ja>)

  保存された高解像度WENO-Z数値参照と、別配布の独立Athena++参照を区別します。どちらもこの衝撃波・密度波相互作用の厳密解という主張ではありません。
- [移動接触不連続：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#references-ja>)

  一定圧力・速度の周期接触不連続の解析的な平行移動が基準です。Sodの波構造全体を代用しません。
- [2次元の滑らかなEulerエントロピー波：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#references-ja>)

  速度(0.7,0.3)・圧力一定の2次元周期正弦密度波について、解析的な保存変数セル平均と格子収束を確認します。
- [Shu–Osher：特性WENO-Zと高解像度参照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja#shu-osher-ja-validation>)

  高解像度の保存変数の点値を各100/200点の格子中心へ線形補間する。誤差はそれぞれ同じ場所・t=1.8で平均する。CSVは200点の計算・参照を並べる。近似収支の許容値0.2%は固定境界の離散化誤差を許すためであり、密度誤差0.15の判定とは別。

## コード・検証

- [WENO-JS／Z：臨界点とεの固定比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja>)
  availability: run

  同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。
- [Shu–Osher：特性WENO-Zと高解像度参照](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja>)
  availability: run

  [-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。
- [Shu–Osher：独立参照と格子収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja>)
  availability: run

  衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。
- [Eulerの特性変数再構成：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/characteristic-reconstruction/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [有限差分WENO5-Z：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [2次元の滑らかなEulerエントロピー波：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/entropy-2d/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
