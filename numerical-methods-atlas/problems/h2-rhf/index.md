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

閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。

#### [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

#### [最小2電子模型のスピン非制限HF](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja)

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

#### H₂分子RHF：独立参照・SCF・s型基底拡大

共通実行例 · 近似・離散化の式

$$
F(P)C=SC\varepsilon,\quad P=2C_oC_o^T
$$

$$
E_{\rm RHF}=\tfrac12\operatorname{Tr}[P(h+F)]+1/R
$$

孤立2電子RHF・有限s型Gaussian基底。数値収束とRHF近似の誤差は別。

#### 最小基底H2のRHF/UHF/FCI・2固定幾何

補助実行例 · 実行例の定義・検証式

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

### 厳密解・参照解

小さな固定H₂モデルの独立RHF参照とSCF・s型基底の検査を使います。有限基底RHFの一致は完全な電子相関を含む厳密分子解の一致ではありません。

#### [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-measurements)

半解析解 · 同じ問題の参照

F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma;\quad \langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2;\quad H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

#### H₂分子RHF：独立参照・SCF・s型基底拡大

教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。

- [教育用コードをimportしない独立PySCF。同一幾何・同一有限基底のRHFであり、相関を含む厳密解ではありません。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv)
- [保存結果](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja)

#### 最小基底H2のRHF/UHF/FCI・2固定幾何

保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

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

#### [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja)

補助実行例

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

UHFはスピン混入を持ちます。2幾何だけで完全な解離曲線や連続空間の厳密解を保証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

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

Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.

#### [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

#### [Unrestricted HF in a minimal two-electron model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en)

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

#### H₂ molecular RHF: independent reference, SCF and s-basis refinement

Common execution example · Approximation or discretization

$$
F(P)C=SC\varepsilon,\quad P=2C_oC_o^T
$$

$$
E_{\rm RHF}=\tfrac12\operatorname{Tr}[P(h+F)]+1/R
$$

Isolated two-electron RHF in finite s-Gaussian bases. Numerical convergence differs from RHF model error.

#### Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI

Supplementary execution example · Example definition or validation formula

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

### Exact and reference solutions

Use independent RHF references and SCF/s-type-basis checks for a small fixed H₂ model. Agreement in finite-basis RHF is not agreement with a fully correlated exact molecular solution.

#### [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-measurements)

Semi-analytic reference · Reference for the same problem

F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma;\quad \langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2;\quad H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

#### H₂ molecular RHF: independent reference, SCF and s-basis refinement

Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.

- [Independent PySCF imports no educational solver. Same-geometry, same-finite-basis RHF, not an exact correlated solution.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/reference-pyscf.json)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/solution.csv)
- [Saved result](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/scf.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=en)

#### Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI

Check two saved PySCF RHF energies, an analytic paired g/u variational polynomial, the even2x2 FCI block and independent fermion assembly.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

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

#### [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en)

Supplementary execution example

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

Explicit unchanged STO-3G s contraction, R1.4/3.0bohr, finite-basis FCI and broken-spin UHF; not exact continuum chemistry. Distances1.4/3.0bohr and total energies in hartree. Two electrons in2AOs, each an explicitly supplied three-primitive contracted Hs function.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Only two H2 geometries and two contracted s orbitals; no complete-basis dissociation curve. UHF is spin contaminated; FCI exactness is finite-basis only.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

#### [code/molecular-hf/2026-11-22/test_molecular_hf.py](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/test_molecular_hf.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_input_validation`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/molecular-hf-2026-11-22.zip)

Working directory: molecular-hf-2026-11-22/

```sh
python -m pytest -q test_molecular_hf.py -k test_fixed_input_validation
```
