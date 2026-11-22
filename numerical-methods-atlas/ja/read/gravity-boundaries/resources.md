# 重力核：孤立FFTと周期スラブ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/gravity-boundaries/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [孤立境界の倍格子FFT畳み込み](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=ja>)
- [水平周期スラブGreen関数FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=ja>)
- [孤立境界の倍格子FFT畳み込み](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [水平周期スラブGreen関数FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [水平周期スラブGreen関数FFT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 重力Poisson方程式の孤立境界に対応する密度場の畳み込み問題です。粒子の軟化二体力や全方向周期Poissonの例とは区別し、この図ではゼロ埋めFFTと同じ離散核の非周期直接畳み込みを照合します。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 水平周期・鉛直孤立の重力Poisson問題で、一様平板の零水平モードを扱います。下のPoisson代表式に対し、ここでの右辺は4πGρです。全方向周期境界や軟化粒子系とは区別します。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 水平周期・鉛直孤立の重力Poisson問題で、面密度の非零水平モードと零モードを扱います。Poisson代表式の右辺は4πGρです。全方向周期場や軟化粒子の二体力とは区別します。

## 問題の図

- [孤立FFTと非周期直接畳み込み](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png
- [一様平面スラブの重力](<https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png
- [正弦波状薄層の重力](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/gravity-boundaries.png

## 厳密解・参照解

- [孤立FFTと非周期直接畳み込み：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=ja#references-ja>)

  同じ離散核・セル体積・自己項を使う非周期直接畳み込みと、ゼロ埋めFFTの一致を確認します。連続核の離散化誤差とは別です。
- [一様平面スラブの重力：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/uniform-slab/?lang=ja#references-ja>)

  一様平板のφ=2πz²を定数ゲージ調整後に比較し、加速度-4πzと零水平モードを確認します。
- [正弦波状薄層の重力：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sinusoidal-sheet/?lang=ja#references-ja>)

  正弦状面密度の指数減衰核と一様面の絶対値核を足した解析式で、水平周期・鉛直孤立の場を確認します。

## コード・検証

- [孤立境界の倍格子FFT畳み込み：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hockney/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [水平周期スラブGreen関数FFT：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/slab/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [孤立FFTと非周期直接畳み込み：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-convolution/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
