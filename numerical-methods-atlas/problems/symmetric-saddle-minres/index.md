# 対称不定値鞍点系とSchur前処理 / Symmetric saddle systems and Schur preconditioning

https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/

## 日本語

[速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/#symmetric-saddle-minres) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#symmetric-saddle-minres)

### 方程式・問題の定義

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。

#### [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。

#### 対称不定値鞍点系とSchur前処理

補助実行例 · 実行例の定義・検証式

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

### 厳密解・参照解

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

#### [対称不定値鞍点系：独立dense解と理想Schurスペクトル](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

S=B H^{-1} B^T; P=diag(H,S); spectrum(L^{-1} A L^{-T})={1,(1-sqrt(5))/2,(1+sqrt(5))/2}; x_ref=LAPACK_solve(A,b)

A=[[H,Bᵀ],[B,0]]、速度サイズ12/24、圧力行数5/11の代数問題。SPD理想Schurは全行列を小さく直接構成し、元の真残差とdense参照解誤差を別に判定。実Stokes境界値問題ではありません。

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

#### 対称不定値鞍点系とSchur前処理

LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja)

### 計算法

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

- [対称不定値系の教育用MINRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja)

補助実行例

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

## English

[The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/#symmetric-saddle-minres) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#symmetric-saddle-minres-en)

### Equations and problem definitions

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.

#### [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en)

$$
A x=b
$$

$$
P A=L U
$$

$$
A=L L^\top\quad(A=A^\top>0)
$$

$$
r=b-Ax
$$

Finite matrices A and right-hand sides b define algebraic problems. Fixed LU, Cholesky, refinement and symmetric-indefinite saddle controls are distinct from continuum PDE solutions.

#### Symmetric saddle systems and Schur preconditioning

Supplementary execution example · Example definition or validation formula

$$
A=[[H,B^T],[B,0]]
$$

$$
P=diag(H,BH^-1B^T)
$$

$$
A_tilde=L^-1 A L^-T
$$

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

### Exact and reference solutions

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

#### [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-measurements)

Finite-grid numerical reference · Reference for the same problem

S=B H^{-1} B^T; P=diag(H,S); spectrum(L^{-1} A L^{-T})={1,(1-sqrt(5))/2,(1+sqrt(5))/2}; x_ref=LAPACK_solve(A,b)

Algebraic saddles A=[[H,B^T],[B,0]] use velocity sizes 12 and 24 and pressure sizes 5 and 11. Explicit dense SPD ideal-Schur controls compare the original residual separately with dense-solution error. This is not a Stokes boundary-value PDE.

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

#### Symmetric saddle systems and Schur preconditioning

Global LAPACK solutions, the analytic ideal-Schur spectrum and an explicit negative-curvature control for CG.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en)

### Numerical methods

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

- [Educational MINRES for symmetric-indefinite systems](https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Restarted GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en)

Supplementary execution example

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

Algebraic mixed-Poisson/Stokes-type blocks with velocity sizes 12 and 24 and pressure sizes 5 and 11. The common original-system residual tolerance is 1e-9.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
