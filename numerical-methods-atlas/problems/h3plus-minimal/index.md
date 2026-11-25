# 3中心H3+の小RHF/MP2/FCI模型 / A tiny three-center H3+ RHF / MP2 / FCI example

https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/

## 日本語

[固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/#h3plus-mp2-fci) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#h3plus-minimal)

### 方程式・問題の定義

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

#### [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

#### [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

閉殻RHFの占有空間軌道の式で、非局所交換を含む。既存のHe局所還元とH2のRHF例を保持する。追加は固定H2/H3+の最小2電子模型で、UHF式は別の対応模型に明示する。一般多中心分子、開殻の大域安定性、完全基底や一般相関法の保証ではない。

#### 3中心H3+の小RHF/MP2/FCI模型

補助実行例 · 実行例の定義・検証式

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

### 厳密解・参照解

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

#### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs);\quad E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

#### 3中心H3+の小RHF/MP2/FCI模型

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja)

### 計算法

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MP2摂動論](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja)

補助実行例

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

一般分子DFT・CC・一般多参照法は未実装です。MP2は変分的でなく、外部独立エンジンの新参照値も生成しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

## English

[Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/#h3plus-mp2-fci) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#h3plus-minimal-en)

### Equations and problem definitions

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

#### [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

#### [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

Closed-shell occupied-orbital RHF equations include nonlocal exchange. Preserve existing He local-reduction and H2RHF examples. New calculations cover only fixed minimal two-electron H2/H3+ models; UHF equations have their own mapped model. No general multicenter molecules, global open-shell stability, complete-basis or general correlated-method guarantee.

#### A tiny three-center H3+ RHF / MP2 / FCI example

Supplementary execution example · Example definition or validation formula

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

### Exact and reference solutions

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

#### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-measurements)

Finite-grid numerical reference · Reference for the same problem

H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs);\quad E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

#### A tiny three-center H3+ RHF / MP2 / FCI example

Check independent signed-fermion assembly, determinant perturbation MP2, electron number, SCF stationarity and FCI variational ordering.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en)

### Numerical methods

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MP2 perturbation theory](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Configuration interaction / CI](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en)

Supplementary execution example

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

Two electrons/3 explicit s orbitals, one fixed non-symmetric triangle. Molecular DFT, CC and general multireference/large molecules remain unimplemented tails. One H3+ geometry[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr, charge+1,2electrons/3s orbitals; energies in hartree.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

General molecular DFT, CC, large bases and general multireference methods remain unimplemented. Independent operator assembly is not an independent external chemistry-engine scalar reference.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
