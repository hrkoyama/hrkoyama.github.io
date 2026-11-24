# Lorentz分散板へのs/p斜め入射

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-maxwell-lorentz/

この章に登録された手法・問題・実行例の関連資料です。 有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

## 手法

- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)

  単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)

  単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

  単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。
- [Yee FDTD](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja>)
- [2ステップleapfrog法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja>)
- [陰的中点則](<https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja>)

## 方程式

- [受動Lorentz・Ohmic分散Maxwell場](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja>)

  正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。 周期y方向のky=4に制限した2D場、c=1。板[4,5]のε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。外側は真空、PEC端は[-24,36]、T=60です。
- [受動Lorentz・Ohmic分散Maxwell場](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja>)

  正の物質エネルギーと直接Ohmic/γ仕事を持つ単一受動Lorentz極。代表式は3Dですが、実装は周期y単一kyの2D s/p成分制限です。PML数値仕事は物理散逸と同一視しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-algorithm>)

  単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

## 問題の図

- [Lorentz分散板へのs/p斜め入射](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png
- [Lorentz分散板へのs/p斜め入射](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp.png

## 厳密解・参照解

- [Lorentz分散板へのs/p斜め入射：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#references-ja>)

  s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。
- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 外側真空、ky=4、板[4,5]、ε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。s=Ezとp=Hzをω=5.1/6/6.9で比較します。 任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。
- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja>)
  reference_kind: analytic

  解析解 外側真空、ky=4、板[4,5]、ε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。s=Ezとp=Hzをω=5.1/6/6.9で比較します。
- [Lorentz分散板へのs/p斜め入射：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-validation>)

  s/p各3解像度の物質・真空12進行からω=5.1/6/6.9を測定。独立な有限窓の真空幾何級数、複素Fresnel係数、直接体積散逸、全stepのPEC収支と末尾を検査します。
- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 外側真空、ky=4、板[4,5]、ε∞=1.5、Δε=0.75、ω0=9、γ=0.5、σ=0.04。s=Ezとp=Hzをω=5.1/6/6.9で比較します。 任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

## コード・検証

- [Lorentz分散板へのs/p斜め入射](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja>)
  availability: run

  有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。
