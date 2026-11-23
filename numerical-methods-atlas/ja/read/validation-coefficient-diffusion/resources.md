# 係数ジャンプ・回転異方性のMG／AMG

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/

この章に登録された手法・問題・実行例の関連資料です。 同じ行列の幾何MG・SA-AMG・直接解と、連続問題の解析解・別離散参照を分けて比較します。

## 手法

- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)

  直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。
- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja>)

  完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)

  完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)
- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja>)

## 方程式

- [不連続係数・完全テンソル拡散の境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja>)

  スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。 単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。
- [不連続係数・完全テンソル拡散の境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja>)

  スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。 単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。
- [不連続係数・完全テンソル拡散の境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja>)

  スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-algorithm>)

  直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-algorithm>)

  完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

## 問題の図

- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png
- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion.png
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion.png

## 厳密解・参照解

- [係数ジャンプ拡散：共有流束とMG・AMG：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/?lang=ja#references-ja>)

  非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。
- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。 非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。
- [回転異方性拡散：完全テンソルQ1とMG・AMG：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/?lang=ja#references-ja>)

  u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。 u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。
- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。 非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja>)
  reference_kind: manufactured

  製造解 単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。 u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。
- [係数ジャンプ拡散：共有流束とMG・AMG：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-validation>)

  非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。
- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-checkerboard-diffusion-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。 非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。
- [回転異方性拡散：完全テンソルQ1とMG・AMG：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-validation>)

  u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rotated-anisotropic-diffusion-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。 u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

## コード・検証

- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja>)
  availability: run

  不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja>)
  availability: run

  非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。
