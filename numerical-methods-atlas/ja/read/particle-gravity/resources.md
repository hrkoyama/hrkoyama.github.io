# 粒子重力：PM、P³M、ツリー、多重極、マルチグリッド

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/particle-gravity/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)
- [FFT粒子格子力](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja>)
- [Barnes–Hut八分木](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja>)
- [単極と2次モーメント展開](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multipole/?lang=ja>)
- [P³M短距離補正](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p3m/?lang=ja>)
- [TreePM力分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/treepm/?lang=ja>)
- [高速多重極法の移動演算](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja>)
- [Fourier微分と時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [FFT粒子格子力](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Barnes–Hut八分木](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [Cloud-in-cellの割当てと補間](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。
- [FFT粒子格子力](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [重力粒子モデル](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja>)

  孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-periodic-particles-ja>)

  3次元周期箱L=1、24³格子、同じCIC配置・補間と連続k²のFourier記号。孤立直接和・Ewald・PME・SPMEではない。正弦密度の解析格子解は粒子近接力全体の精度保証ではない。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

## 問題の図

- [3次元周期Poisson・Fourier製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-poisson-3d.png
- [孤立粒子群の軟化重力（ツリー・直接和）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isolated-particles.png
- [周期PM粒子群の質量・内力](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/particle-gravity.png

## 厳密解・参照解

- [3次元周期Poisson・Fourier製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-3d-periodic/?lang=ja#references-ja>)

  平均密度を除いた周期Poissonの単一Fourier製造モードと比較します。格子場の検証であり、周期粒子の直接和の検証とは別です。
- [孤立粒子群の軟化重力（ツリー・直接和）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/isolated-particles/?lang=ja#references-ja>)

  同一粒子・同一Plummer軟化の直接対和が数値基準です。ツリー開き角と多重極次数ごとの力誤差を比較します。
- [周期PM粒子群の質量・内力：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#references-ja>)

  質量保存・質量重み付き内力と、格子PoissonのFourier製造解を確認します。一般の周期粒子直接和との力比較を行ったという意味ではありません。
- [周期PM粒子群：質量・内力・格子場：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja#periodic-particles-ja-validation>)

  CSVは粒子ごとの座標・質量・加速度・力。正弦密度の独立解析場検査はJSONの集計値に保存。PM格子細分化を粒子力の解析誤差として誤表示しない。

## コード・検証

- [周期PM粒子群：質量・内力・格子場](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-particles/?lang=ja>)
  availability: run

  入力JSONに保存した19粒子の周期CIC–FFT–CIC計算。質量、内力和、単粒子自己力、整数箱長移動を確認し、別の正弦密度の解析的周期Poisson場と照合。
- [PIC空間演算の独立実装照合](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja>)
  availability: run

  ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。
- [温かいPICの線形Landau減衰](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-landau-damping/?lang=ja>)
  availability: run

  熱速度1のMaxwell分布を自己無撞着に動かし、減衰率・周波数・符号付き場の履歴を独立した線形参照で調べます。
- [温かいPICの二流初期成長](<https://hrkoyama.github.io/numerical-methods-atlas/validation/thermal-two-stream/?lang=ja>)
  availability: run

  温度を持つ対向Maxwell二流を時間発展し、固定した線形窓の成長率と過渡を分散式・Volterra参照から分けて検査します。
- [Barnes–Hut：192粒子と直接和の比較](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/barnes-hut/?lang=ja>)
  availability: run

  孤立・軟化重力の静的な力の比較。軌道計算・周期系・実行速度の比較ではありません。
- [冷たいPlummer密度由来32粒子の短時間力学](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gravity-plummer-short/?lang=ja>)
  availability: run

  同じ軟化有限N ODEで時間誤差と木近似誤差を分け、独立DOP853・直接力と収支を比較。
- [2次元対数核のM2M・M2L・L2Lを持つFMM](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm/?lang=ja>)
  availability: run

  自由空間の対数ポテンシャルを一様四分木の多重極・局所展開で評価し、直接和と比較します。
- [FMM：直接和・解析配置と展開次数・木の深さ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm-convergence/?lang=ja>)
  availability: run

  96粒子の2次元対数核を別の全対直接和と照合し、展開次数・木の深さ、回転・平行移動、合力の近似誤差を測ります。
- [真3D 1/r FMM：多段変換・力・適応所有権](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja>)
  availability: run

  非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。
- [Cloud-in-cellの割当てと補間：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [FFT粒子格子力：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pm/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Barnes–Hut八分木：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/barnes-hut/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [単極と2次モーメント展開：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multipole/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [高速多重極法の移動演算：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [周期PM粒子群の質量・内力：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-particles/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
