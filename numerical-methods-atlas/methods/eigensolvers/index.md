# Krylov eigenvalue solvers / Krylov固有値解法

Status: educational-example

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace. Additional fixed examples: Explicitly restarted Krylov and interior eigenvalues, Consistent-mass FEM string eigenpairs. See each release for assumptions and checked scope.

Lanczos・Arnoldi：Ritz値と固有対残差の収束: 32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。 Krylov固有値：クラスター部分空間と非正規感度: 48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。 追加固定例：明示的再始動Krylovと内部固有値、整合質量FEM弦の一般化固有値。条件と検証範囲は各配布版で確認してください。

Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals: Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices. Krylov eigenvalues: cluster subspaces and nonnormal sensitivity: NumPy projected solves and SciPy dense references may share LAPACK infrastructure and are not claimed fully independent backends. Analytic eigenvalues and constructed controls provide additional checks. Restarting, interior eigenvalues, large sparse systems and universal monotonic convergence are outside scope. Additional fixed examples: One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed. A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

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

- Explicitly restarted Krylov and interior eigenvalues: https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/
- Consistent-mass FEM string eigenpairs: https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json

Common execution records: [{"id": "krylov-eigenvalues", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "krylov-eigen-conditioning", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "restarted-shift-invert", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fem-mass-eigen", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the published fixed-input scope; validate conditions, references and criteria separately for extensions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [有限次元の行列固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-eigenproblem-ja) (`finite-dimensional-eigenproblem`; restarted-shift-invert)
- [固定端弦の固有値と整合質量FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja) (`dirichlet-string-eigenproblem`; fem-mass-eigen)

#### 問題の図 (`method-problems-ja`)

##### [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja) (`krylov-spectrum`)

![再直交化Lanczos・ArnoldiのKrylov次元を変え、固有対残差と独立した密行列固有値との差を保存結果から比較。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#code-ja)

- [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja) (`krylov-eigenvalues`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

- [Krylov固有値：クラスター部分空間と非正規感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja) (`krylov-eigen-conditioning`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

##### [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`)

![固有値比較に使う、保存した31×31 Dirichlet Laplacian。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#code-ja)

- [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja) (`restarted-shift-invert`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`)

![内部63点で計算した、M正規化された最低3モード。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#code-ja)

- [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) (`fem-mass-eigen`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=ja#references-ja) (`krylov-spectrum`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#references-ja) (`restarted-shift-invert`)

- [再始動/shift-invert：固定離散行列の閉スペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-restarted-shift-invert-ja) (`restarted-shift-invert`; 同じ問題の参照; 解析参照)

単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。

[既存の参照図](/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-measurements)

##### [整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#references-ja) (`fem-mass-eigen`)

- [P1整合質量弦：閉離散固有値と連続体固有値](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja) (`fem-mass-eigen`; 同じ問題の参照; 解析参照)

小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

[既存の参照図](/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-measurements)

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

##### 明示的再始動Krylovと内部固有値 (`restarted-shift-invert`)

[明示的再始動Krylovと内部固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。

##### 整合質量FEM弦の一般化固有値 (`fem-mass-eigen`)

[整合質量FEM弦の一般化固有値](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。

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
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
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

- [Finite-dimensional matrix eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-eigenproblem-en) (`finite-dimensional-eigenproblem`; restarted-shift-invert)
- [Fixed-end string eigenvalues and consistent-mass FEM](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#dirichlet-string-eigenproblem-en) (`dirichlet-string-eigenproblem`; fem-mass-eigen)

#### Problem figures (`method-problems-en`)

##### [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en) (`krylov-spectrum`)

![Stored eigenpair residuals and differences from independent dense eigenvalues as reorthogonalized Lanczos/Arnoldi Krylov dimensions increase.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#code-en)

- [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en) (`krylov-eigenvalues`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip)

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

- [Krylov eigenvalues: cluster subspaces and nonnormal sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=en) (`krylov-eigen-conditioning`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip)

Measure Lanczos and Arnoldi with dimensions4/8/16/32 on 48-dimensional clustered symmetric and strongly nonnormal triangular matrices. Distinguish residual, forward error, eigenvalue condition number and invariant subspace.

##### [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) (`restarted-shift-invert`)

![The saved 31 x 31 Dirichlet Laplacian used in the eigenvalue comparisons.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png)

Two-pass Arnoldi is explicitly restarted from one Ritz vector. Original LU routines perform the shifted solves, and stopping uses the original eigenproblem.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#code-en)

- [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en) (`restarted-shift-invert`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) (`fem-mass-eigen`)

![The first three M-normalized modes computed on the 63-node interior grid.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png)

Elementwise K and M assembly, M-inner-product Krylov iteration on K^-1 M, and actual SciPy LOBPCG with a small exact-K-inverse preconditioner. LOBPCG starts from {1, x^3, x^6}; degree-plus-two images avoid the structural rank defect of {1, x, x^2}. The same M is applied through a qualified einsum LinearOperator, avoiding the dense-B adapter. The eigensolver itself remains SciPy LOBPCG.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#code-en)

- [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) (`fem-mass-eigen`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.


#### Exact / reference solutions (`method-references-en`)

##### [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/?lang=en#references-en) (`krylov-spectrum`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en#references-en) (`restarted-shift-invert`)

- [Restarting and shift-invert: the closed spectrum of a fixed discrete matrix](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-restarted-shift-invert-en) (`restarted-shift-invert`; Same-problem reference; Analytic reference)

One eigenpair of a real symmetric matrix only. No implicit restarting, Krylov-Schur, locking, or general nonnormal or clustered-spectrum capability is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en#restarted-shift-invert-en-measurements)

##### [Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en#references-en) (`fem-mass-eigen`)

- [Consistent-mass P1 string: closed discrete and continuum eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fem-mass-eigen-en) (`fem-mass-eigen`; Same-problem reference; Analytic reference)

A small 1D string only. If SciPy raises before returning, inputs are retained; unreturned internal iterates are not claimed to be saved. The 35 component checks do not replace the four full scientific cases.

[Existing reference profile](/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en#fem-mass-eigen-en-measurements)

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

##### Explicitly restarted Krylov and interior eigenvalues (`restarted-shift-invert`)

[Explicitly restarted Krylov and interior eigenvalues](https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

Explicit restarting and shift-invert are compared using original eigenproblem residuals and counted operator actions.

##### Consistent-mass FEM string eigenpairs (`fem-mass-eigen`)

[Consistent-mass FEM string eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

Consistent-mass P1 string eigenpairs compare an M-inner-product Krylov method and actual SciPy LOBPCG with an independent discrete spectrum.

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
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)

###### Package tests

- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
- [/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
