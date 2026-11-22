# 西川の双曲型拡散法：1階系を反復する

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/hyperbolic-diffusion/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [1次の双曲型拡散ベースライン](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hyperbolic-diffusion/?lang=ja>)
- [1次の双曲型拡散ベースライン](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hyperbolic-diffusion/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [補助的な双曲型拡散系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hyperbolic-diffusion-ja>)

  τは擬似時間、Trは緩和時間。定常でp=uₓ、−νuₓₓ=fを回復します。物理時間の熱拡散とは区別します。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [補助的な双曲型拡散系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hyperbolic-diffusion-ja>)

  τは擬似時間、Trは緩和時間。定常でp=uₓ、−νuₓₓ=fを回復します。物理時間の熱拡散とは区別します。

## 問題の図

- [1次元周期Poisson・擬似時間による定常解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-periodic.png

## 厳密解・参照解

- [1次元周期Poisson・擬似時間による定常解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja#references-ja>)

  周期正弦製造解に向かう補助双曲系の擬似時間残差、零平均と格子収束を確認します。

## コード・検証

- [1次の双曲型拡散ベースライン：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/hyperbolic-diffusion/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [1次元周期Poisson・擬似時間による定常解：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-periodic/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
