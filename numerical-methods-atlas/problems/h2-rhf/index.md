# H₂分子RHF：独立参照・SCF・s型基底拡大 / H₂ molecular RHF: independent reference, SCF and s-basis refinement

https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/

## 日本語

[固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/h2-hf/#measured-results) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#h2-rhf)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

閉殻RHFの占有空間軌道の式。一般に非局所な交換を含む。実行例は球対称1s² Heの局所還元に限定し、一般の分子・多電子のFock行列構築は未実装。

#### [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子多体固有値問題。核間反発は電子Hamiltonianの外に加える。実行例は1電子の孤立水素型原子に限定。一般の多電子直接解法は未実装。

#### H₂分子RHF：独立参照・SCF・s型基底拡大

共通実行例 · 近似・離散化の式

$$
F(P)C=SC\varepsilon,\quad P=2C_oC_o^T
$$

$$
E_{\rm RHF}=\tfrac12\operatorname{Tr}[P(h+F)]+1/R
$$

孤立2電子RHF・有限s型Gaussian基底。数値収束とRHF近似の誤差は別。

### 厳密解・参照解

小さな固定H₂モデルの独立RHF参照とSCF・s型基底の検査を使います。有限基底RHFの一致は完全な電子相関を含む厳密分子解の一致ではありません。

#### H₂分子RHF：独立参照・SCF・s型基底拡大

教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。

- [教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja)

共通実行例

孤立・Born–Oppenheimer・非相対論・2電子閉殻H₂。3核間距離でSTO-3Gと入れ子s型Gaussian基底を比較。RHFの数値検証であり、分子DFT・周期系・完全基底極限や正しい解離を検証しない。

固定核・一重項の制限HF、1空間軌道の二重占有。自作Gaussian積分と別実装PySCFで同じ幾何・基底を使用。

[コード / ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_molecular_hf.py
```

最大反復・特異な重なり・不適切入力は失敗として扱う。SCF停止と基底公差、物理近似の妥当性を区別する。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

#### [code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_fixed_input_validation`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

作業フォルダ：molecular-hf-2026-11-22/

```sh
python -m pytest -q test_molecular_hf.py -k test_fixed_input_validation
```

## English

[Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/h2-hf/#measured-results) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#h2-rhf-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

Closed-shell RHF spatial-orbital equations, generally with nonlocal exchange. Runnable code is restricted to the spherical 1s² helium local reduction; general molecular/many-electron Fock-matrix construction is not implemented.

#### [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic many-body eigenproblem; add nuclear repulsion separately. Runnable examples cover only isolated one-electron hydrogenic atoms, not direct general many-electron solutions.

#### H₂ molecular RHF: independent reference, SCF and s-basis refinement

Common execution example · Approximation or discretization

$$
F(P)C=SC\varepsilon,\quad P=2C_oC_o^T
$$

$$
E_{\rm RHF}=\tfrac12\operatorname{Tr}[P(h+F)]+1/R
$$

Isolated two-electron RHF in finite s-Gaussian bases. Numerical convergence differs from RHF model error.

### Exact and reference solutions

Use independent RHF references and SCF/s-type-basis checks for a small fixed H₂ model. Agreement in finite-basis RHF is not agreement with a fully correlated exact molecular solution.

#### H₂ molecular RHF: independent reference, SCF and s-basis refinement

Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.

- [Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en)

Common execution example

Isolated Born–Oppenheimer nonrelativistic two-electron closed-shell H₂. Compare STO-3G and nested s-Gaussian spaces at three separations. Numerical RHF validation, not molecular DFT, periodic, complete-basis or correct-dissociation validation.

Fixed nuclei, singlet restricted HF, one doubly occupied spatial orbital. Original Gaussian integrals and independent PySCF use identical geometries and bases.

[Code / ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_molecular_hf.py
```

Iteration limits, singular overlap and invalid inputs fail explicitly. SCF stopping, basis tolerance and physical adequacy remain distinct.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/molecular-hf/2026-11-22/run.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/run.py)
- [/code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

#### [code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_input_validation`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Working directory: molecular-hf-2026-11-22/

```sh
python -m pytest -q test_molecular_hf.py -k test_fixed_input_validation
```
