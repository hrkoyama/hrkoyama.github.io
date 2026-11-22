# Krylov eigenvalue solvers / Krylov固有値解法

Status: educational-example

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope.

Other names: 固有値解法, eigenvalue solver, Krylov eigensolver, クリロフ固有値法

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/



- Reference: https://doi.org/10.1090/qam/42792 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.6028/jres.045.026 — Method-specific source; see the detailed reading for source role and actual review depth.

## Small fixed-input validation supplements

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

- Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json

- Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json

Common execution records: [{"id": "krylov-eigenvalues", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "krylov-eigen-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

対応する方程式一覧の項目は未登録です。

#### 問題の図 (`method-problems-ja`)

##### [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

![再直交化Lanczos・ArnoldiのKrylov次元を変え、固有対残差と独立した密行列固有値との差を保存結果から比較。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja) (`krylov-eigenvalues`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

- [Krylov固有値：クラスター部分空間と非正規感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja) (`krylov-eigen-conditioning`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。


#### 厳密解・参照解 (`method-references-ja`)

##### [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#references-ja) (`krylov-spectrum`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/eigensolvers/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Lanczos・Arnoldi：Ritz値と固有対残差の収束 (`krylov-eigenvalues`)

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

##### Krylov固有値：クラスター部分空間と非正規感度 (`krylov-eigen-conditioning`)

[Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

No corresponding equation-registry entry is registered.

#### Problem figures (`method-problems-en`)

##### [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

![Stored eigenpair residuals and differences from independent dense eigenvalues as reorthogonalized Lanczos/Arnoldi Krylov dimensions increase.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en) (`krylov-eigenvalues`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en) (`krylov-eigen-conditioning`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.


#### Exact / reference solutions (`method-references-en`)

##### [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#references-en) (`krylov-spectrum`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/eigensolvers/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals (`krylov-eigenvalues`)

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

##### Krylov eigenvalues: cluster subspaces and nonnormal sensitivity (`krylov-eigen-conditioning`)

[Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
