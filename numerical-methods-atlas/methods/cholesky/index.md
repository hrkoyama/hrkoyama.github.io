# Cholesky factorization and triangular solves / Cholesky分解と三角代入

Status: educational-example

Original lower Cholesky factorization and substitution are checked on fixed real SPD systems, then used for refinement and exact stiffness inversion in the small string example.

自作の下三角Choleskyと代入を実SPD固定例で検査し、混合精度改良と小弦の厳密剛性逆に使います。

No indefinite or complex systems, pivoted Cholesky, or arbitrary extreme-scaling capability is claimed.

Other names: コレスキー分解, 平方根法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/



- Reference: https://netlib.org/lapack/lug/node38.html — Selected official LU, Cholesky, conditioning and refinement paragraphs were read. LAPACK writes A=PLU; this source records PA=LU. The implemented mixed-precision refinement differs from the selected same-precision RFS description.

## Small fixed-input validation supplements

Original lower Cholesky factorization and substitution are checked on fixed real SPD systems, then used for refinement and exact stiffness inversion in the small string example.

自作の下三角Choleskyと代入を実SPD固定例で検査し、混合精度改良と小弦の厳密剛性逆に使います。

- Pivoted LU, Cholesky and iterative refinement: https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json

Common execution records: [{"id": "pivoted-direct-refinement", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`; pivoted-direct-refinement)

#### 問題の図 (`method-problems-ja`)

##### [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`)

![保存した12×12 SPD行列。反復改良の固定例に使います。 別の全図に示す誤差は厳密有理数解をbinary64へ丸めた参照との差です。対数表示だけ、厳密なゼロ誤差をfloat64.tinyに置いて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

手書き部分ピボットLU・下三角Cholesky・前後代入。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#code-ja)

- [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja) (`pivoted-direct-refinement`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。


#### 厳密解・参照解 (`method-references-ja`)

##### [部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#references-ja) (`pivoted-direct-refinement`)

- [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pivoted-direct-refinement-ja) (`pivoted-direct-refinement`; 同じ問題の参照; 解析参照)

小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。

[既存の参照図](/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 部分ピボットLU・Choleskyと反復改良 (`pivoted-direct-refinement`)

[部分ピボットLU・Choleskyと反復改良](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

自作の下三角Choleskyと代入を実SPD固定例で検査し、混合精度改良と小弦の厳密剛性逆に使います。

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

- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`; pivoted-direct-refinement)

#### Problem figures (`method-problems-en`)

##### [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`)

![The saved 12 x 12 SPD matrix used in the refinement examples. In the companion full figure, errors are measured against the exact-rational solution rounded to binary64; exact zeros are shown at float64.tiny for logarithmic display only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png)

Original implementations of LU with partial pivoting, lower Cholesky factorization and triangular substitution.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#code-en)

- [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en) (`pivoted-direct-refinement`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.


#### Exact / reference solutions (`method-references-en`)

##### [Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en#references-en) (`pivoted-direct-refinement`)

- [Pivoted LU and Cholesky: exact-rational references for actual binary input](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pivoted-direct-refinement-en) (`pivoted-direct-refinement`; Same-problem reference; Analytic reference)

Small fixed examples only; convergence of mixed-precision refinement is not guaranteed for arbitrary matrices.

[Existing reference profile](/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en#pivoted-direct-refinement-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-linear-algebra-spectral/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Pivoted LU, Cholesky and iterative refinement (`pivoted-direct-refinement`)

[Pivoted LU, Cholesky and iterative refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

Exact-rational comparisons separate conditioning, forward and backward error, and pivot growth.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Original lower Cholesky factorization and substitution are checked on fixed real SPD systems, then used for refinement and exact stiffness inversion in the small string example.

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
