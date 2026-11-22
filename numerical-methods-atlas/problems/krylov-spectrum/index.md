# Lanczos・Arnoldi：Ritz値と固有対残差の収束 / Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

https://hrkoyama.github.io/numerical-methods-atlas/problems/krylov-spectrum/

## 日本語

[再直交化Lanczos・ArnoldiのKrylov次元を変え、固有対残差と独立した密行列固有値との差を保存結果から比較。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-foundations/#krylov-eigenvalues) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#krylov-spectrum)

### 方程式・問題の定義

行列固有値問題Av=λvをLanczos・Arnoldiで近似する線形代数の例です。

#### Lanczos・Arnoldi：Ritz値と固有対残差の収束

補助実行例 · 実行例の定義・検証式

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

### 厳密解・参照解

独立固有値参照と、各Ritz値・固有対の残差、直交性と反復収束を確認します。

#### Lanczos・Arnoldi：Ritz値と固有対残差の収束

||Av−λv||₂、独立密行列固有値との差、基底の直交性を保存し、Krylov次元を増やした末尾の改善を確認します。非対称Ritz値の単調収束は仮定しません。恒等行列のhappy breakdown、零初期ベクトル拒否、次元予算不足も検査します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [Krylov固有値解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Lanczos・Arnoldi：Ritz値と固有対残差の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja)

補助実行例

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

対称問題では実対称行列、非対称問題では既知の分離した最大固有値5を持つ実行列を使います。初期ベクトルは固定seedです。非対称Ritz値は複素数を許し、最大実部で選びます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

非再始動・小行列・分離した極端固有対の教材です。内部固有値、クラスタ、巨大な疎行列、強い非正規性、shift-invertやimplicitly restarted Arnoldiは対象外です。小さな固有対残差だけで非正規行列の固有値誤差の厳密上界とはしません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)

## English

[Stored eigenpair residuals and differences from independent dense eigenvalues as reorthogonalized Lanczos/Arnoldi Krylov dimensions increase.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/krylov-eigenvalues.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-foundations/#krylov-eigenvalues) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#krylov-spectrum-en)

### Equations and problem definitions

Linear-algebra example approximating Av=λv with Lanczos/Arnoldi.

#### Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

Supplementary execution example · Example definition or validation formula

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T
$$

$$
H_my=\theta y,\quad v=V_my,\quad r=Av-\theta v
$$

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

### Exact and reference solutions

Check independent eigenvalue references together with Ritz/eigenpair residuals, orthogonality and iterative convergence.

#### Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals

Store ||Av−λv||₂, differences from independently solved dense eigenvalues and basis orthogonality; verify final improvement as Krylov dimension grows. Nonsymmetric Ritz convergence is not assumed monotone. Tests include identity-matrix happy breakdown, zero-start rejection and insufficient dimension budgets.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Krylov eigenvalue solvers](https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Lanczos and Arnoldi: convergence of Ritz values and eigenpair residuals](https://hrkoyama.github.io/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=en)

Supplementary execution example

Original Lanczos and Arnoldi on symmetric/nonsymmetric 32×32 and 48×48 matrices measure convergence of the largest-real-part eigenpair over Krylov dimensions 4, 8 and 16, against independent full-matrix LAPACK references.

The symmetric case is real symmetric; the nonsymmetric case is real with a known separated largest eigenvalue 5. Starting vectors use fixed seeds. Nonsymmetric Ritz values may be complex and are selected by largest real part.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Unrestarted small-matrix educational examples with separated extreme eigenpairs. Interior/clustered eigenvalues, very large sparse matrices, strong nonnormality, shift-invert and implicitly restarted Arnoldi are outside scope. A small eigenpair residual alone is not treated as a rigorous eigenvalue-error bound for nonnormal matrices.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/foundations/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py)
- [/code/validated-examples/2026-11-22/foundations/test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py)
