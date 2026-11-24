# Educational MINRES for symmetric-indefinite systems / 対称不定値系の教育用MINRES

Status: educational-example

Stored-basis, fully reorthogonalized Lanczos least squares solves algebraic saddle controls, checking the original residual against GMRES and the ideal-Schur spectrum.

全再直交化のLanczos最小二乗で代数鞍点系を解き、GMRESと同じ元残差および理想Schurの三点スペクトルを検査します。

This is not compact production Paige–Saunders MINRES, MINRES-QLP, a singular minimum-norm solver, or a full Stokes PDE solver.

Other names: MINRES法, 最小残差法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/



- Reference: https://web.stanford.edu/group/SOL/software/minres/ — Selected author discussion of symmetry, indefinite A, SPD preconditioning, Lanczos and the original residual was read. The original 1975 paper was not read.

## Small fixed-input validation supplements

Stored-basis, fully reorthogonalized Lanczos least squares solves algebraic saddle controls, checking the original residual against GMRES and the ideal-Schur spectrum.

全再直交化のLanczos最小二乗で代数鞍点系を解き、GMRESと同じ元残差および理想Schurの三点スペクトルを検査します。

- Symmetric saddle systems and Schur preconditioning: https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json

Common execution records: [{"id": "symmetric-saddle-minres", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`; symmetric-saddle-minres)

#### 問題の図 (`method-problems-ja`)

##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

- [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#references-ja) (`symmetric-saddle-minres`)

- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja) (`symmetric-saddle-minres`; 同じ問題の参照; 有限格子の数値参照)

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

[既存の参照図](/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 対称不定値鞍点系とSchur前処理 (`symmetric-saddle-minres`)

[対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

全再直交化のLanczos最小二乗で代数鞍点系を解き、GMRESと同じ元残差および理想Schurの三点スペクトルを検査します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`; symmetric-saddle-minres)

#### Problem figures (`method-problems-en`)

##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

- [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.


#### Exact / reference solutions (`method-references-en`)

##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#references-en) (`symmetric-saddle-minres`)

- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en) (`symmetric-saddle-minres`; Same-problem reference; Finite-grid numerical reference)

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

[Existing reference profile](/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Symmetric saddle systems and Schur preconditioning (`symmetric-saddle-minres`)

[Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Stored-basis, fully reorthogonalized Lanczos least squares solves algebraic saddle controls, checking the original residual against GMRES and the ideal-Schur spectrum.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

###### Related source

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### Package tests

- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
