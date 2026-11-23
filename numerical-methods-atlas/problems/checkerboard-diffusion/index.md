# 係数ジャンプ拡散：共有流束とMG・AMG / Checkerboard diffusion: shared flux, MG and AMG

https://hrkoyama.github.io/numerical-methods-atlas/problems/checkerboard-diffusion/

## 日本語

[保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/#checkerboard-diffusion) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#checkerboard-diffusion)

### 方程式・問題の定義

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。

#### [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja)

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。

#### 係数ジャンプ拡散：共有流束とMG・AMG

補助実行例 · 実行例の定義・検証式

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

### 厳密解・参照解

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

#### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja#checkerboard-diffusion-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}; T_f=|f|/(d_L/a_L+d_R/a_R)

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。 非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。 係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

#### 係数ジャンプ拡散：共有流束とMG・AMG

非零2材料流束パッチ、残差に整合する収支、直接解の前進/energy誤差、独立三角形P1参照の格子感度。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja)

### 計算法

直交FVの共有面調和平均。幾何MGと座標を受け取らないSA-AMGの対称Galerkin V-cycleを、同じ行列のPCGへ適用。

- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [係数ジャンプ拡散：共有流束とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja)

補助実行例

不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。

単位正方形、零Dirichlet、f=1、対角2象限100/残り1、N16/32/64。参照P1は128/192。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

係数比100の固定例。P1格子差は厳密誤差上界ではなく、特異交点の次数や普遍的なMG/AMG優劣は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

## English

[Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/checkerboard-diffusion-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/#checkerboard-diffusion) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#checkerboard-diffusion-en)

### Equations and problem definitions

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

#### [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en)

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix.

#### Checkerboard diffusion: shared flux, MG and AMG

Supplementary execution example · Example definition or validation formula

$$
-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}
$$

$$
T_f=|f|/(d_L/a_L+d_R/a_R)
$$

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

### Exact and reference solutions

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

#### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en#checkerboard-diffusion-en-measurements)

Finite-grid numerical reference · Reference for the same problem

-\nabla\cdot(a\nabla u)=1,\quad a\in\{1,100\}; T_f=|f|/(d_L/a_L+d_R/a_R)

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

#### Checkerboard diffusion: shared flux, MG and AMG

Nonzero two-material flux patch, residual-aware budget, direct forward/energy errors and independent triangular-P1 grid sensitivity.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en)

### Numerical methods

Orthogonal FV with shared harmonic transmissibility. Symmetric Galerkin geometric and coordinate-free SA cycles precondition PCG on identical matrices.

- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Checkerboard diffusion: shared flux, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=en)

Supplementary execution example

Compare discontinuous-coefficient FV with independent P1 reference fields, separating linear-system residual/forward errors from continuum error.

Unit square, zero Dirichlet, f=1, diagonal quadrants100/others1, N16/32/64; reference P1 meshes128/192.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Fixed contrast100 example. P1 differences are not rigorous error bounds; no singular exponent or universal MG/AMG winner is asserted.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)
