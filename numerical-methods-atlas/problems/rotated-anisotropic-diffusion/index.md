# 回転異方性拡散：完全テンソルQ1とMG・AMG / Rotated diffusion: full-tensor Q1, MG and AMG

https://hrkoyama.github.io/numerical-methods-atlas/problems/rotated-anisotropic-diffusion/

## 日本語

[保存した2D解・誤差・真の残差・格子感度の検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-coefficient-diffusion/#rotated-anisotropic-diffusion) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#rotated-anisotropic-diffusion)

### 方程式・問題の定義

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。

#### [不連続係数・完全テンソル拡散の境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#tensor-diffusion-ja)

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

スカラー調和流束FVと、非零の交差項を持つ完全テンソルQ1を分けます。MGとAMGは同じ行列を解きます。

#### 回転異方性拡散：完全テンソルQ1とMG・AMG

補助実行例 · 実行例の定義・検証式

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。

### 厳密解・参照解

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

#### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja#rotated-anisotropic-diffusion-ja-measurements)

製造解 · 同じ問題の参照

-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T; f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。 u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。 指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

#### 回転異方性拡散：完全テンソルQ1とMG・AMG

u=xy,f=−2Kxyパッチ、解析流束由来のsource、積分L2/energy誤差と4/6点求積感度、直接解との比較。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja)

### 計算法

完全2×2テンソルQ1とGauss積分。MG/SA-AMGは対称2/2Jacobi、Galerkin粗行列、粗CholeskyでSPDの固定適用。

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [幾何マルチグリッドVサイクル](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [共役勾配法](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [回転異方性拡散：完全テンソルQ1とMG・AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja)

補助実行例

非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。

単位正方形、零Dirichlet、K=R(pi/6)diag(1,.01)Rᵀ、厳密解sin(pi x)sin(pi y)、N16/32/64。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

指定した角度・異方性の限定例。スカラーTPFAを回転テンソルへ転用せず、一般テンソルへの頑健性は保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)

## English

[Saved2D solution, error, true residual and refinement/reference sensitivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/rotated-anisotropic-diffusion-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-coefficient-diffusion/#rotated-anisotropic-diffusion) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#rotated-anisotropic-diffusion-en)

### Equations and problem definitions

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

#### [Discontinuous and full-tensor diffusion BVP](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#tensor-diffusion-en)

$$
-\nabla\cdot(K(\boldsymbol x)\nabla u)=f,\quad u|_{\partial\Omega}=g
$$

$$
K=aI\ (a\in\{1,100\})\quad\mathrm{or}\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

Separate scalar harmonic-flux FV from full-tensor Q1 with nonzero cross terms. MG and AMG solve the same matrix.

#### Rotated diffusion: full-tensor Q1, MG and AMG

Supplementary execution example · Example definition or validation formula

$$
-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T
$$

$$
f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y
$$

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

### Exact and reference solutions

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

#### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en#rotated-anisotropic-diffusion-en-measurements)

Manufactured solution · Reference for the same problem

-\nabla\cdot(K\nabla u)=f,\quad K=R(\pi/6)\operatorname{diag}(1,.01)R^T; f=\pi^2(K_{xx}+K_{yy})\sin\pi x\sin\pi y-2\pi^2K_{xy}\cos\pi x\cos\pi y

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

#### Rotated diffusion: full-tensor Q1, MG and AMG

u=xy,f=-2Kxy patch, analytic-flux source, integrated L2/energy error,4/6point quadrature sensitivity and direct-solve comparison.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en)

### Numerical methods

Full2x2 tensor Q1 and Gauss quadrature. Fixed SPD MG/SA cycles use symmetric2/2Jacobi, Galerkin operators and coarse Cholesky.

- [Q1 FEM for scalar diffusion and mapped vector BVPs](https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Geometric multigrid V-cycle](https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Conjugate gradients](https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Rotated diffusion: full-tensor Q1, MG and AMG](https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=en)

Supplementary execution example

Retain nonzero Kxy in the Q1 weak form and compare analytic refinement with MG/AMG convergence for the same matrix.

Unit square, zero Dirichlet, K=R(pi/6)diag(1,.01)R^T, exact sin(pi x)sin(pi y), N16/32/64.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/atlas-coefficient-diffusion-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One angle/anisotropy only. Scalar TPFA is not extended to rotated tensors; arbitrary-tensor robustness is not established.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/coefficient-diffusion/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/run.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/operators.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/multilevel.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/references/p1.py)
- [/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/coefficient-diffusion/test_diffusion.py)
