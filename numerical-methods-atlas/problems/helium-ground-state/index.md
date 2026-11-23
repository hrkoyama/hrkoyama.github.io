# He基底状態：閉殻HF・交換のみLDA / Helium ground state: closed-shell HF and exchange-only LDA

https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/

## 日本語

[公開した原子計算コードの固定入力から計算。条件・CSV・収束検査・独立参照を解説先に保存。](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-atoms/#helium) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#helium-ground-state)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

閉殻RHFの占有空間軌道の式で、一般に非局所な交換を含みます。公開例は、球対称1s² Heの局所還元と、別の分子積分実装による固定入力のH₂ RHFです。原子例と分子例では基底・離散化・参照が異なります。各例の範囲は下の固定入力・検証記録で確認してください。一般多中心分子・開殻・相関を含む解法の検証ではありません。

#### [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja)

$$
E[n]=T_s[n]+\int v_{\rm ext}n\,d\mathbf r+E_H[n]+E_{\rm xc}[n]+E_{NN}
$$

$$
[-\tfrac12\nabla^2+v_{\rm ext}+v_H+v_{\rm xc}]\phi_i=\varepsilon_i\phi_i
$$

$$
n(\mathbf r)=\sum_i f_i|\phi_i(\mathbf r)|^2,\quad \int n\,d\mathbf r=N,\quad v_{\rm xc}=\frac{\delta E_{\rm xc}}{\delta n}
$$

密度汎関数の局所KS代表形です。公開例は、球対称Heのスピン非偏極・Dirac交換のみLDAと、固定した周期He／He₂セルのLDA交換＋VWN5相関です。原子の動径実装と周期PySCFワークフローは別系列で、基底・境界条件・参照も異なります。各例の範囲は下の固定入力・検証記録で確認してください。GGA・hybrid・一般物質・励起状態まで検証した意味ではありません。

#### He：閉殻HF・交換のみLDA

共通実行例 · 近似・離散化の式

$$
\left[\hat h_r+\frac12v_H[n]\right]u=\varepsilon u\quad(\mathrm{He}\;1s^2\ \mathrm{RHF})
$$

$$
\left[\hat h_r+v_H[n]+v_x^{\rm LDA}(n)\right]u=\varepsilon u,\qquad v_x^{\rm LDA}=-\left(\frac{3n}{\pi}\right)^{1/3}
$$

$$
\hat h_r=-\frac12\frac{d^2}{dr^2}-\frac2r,\qquad n(r)=\frac{2|u(r)|^2}{4\pi r^2}
$$

孤立・球対称・閉殻1s²に限定した原子単位の動径式。RHFのvH/2は2電子同一空間軌道に特有。LDAは交換のみで相関なし。UHF、GGA、hybrid、一般分子・周期DFTの実行例ではない。

### 厳密解・参照解

閉殻HF・交換のみLDAの独立参照、SCF残差・電子数・格子収束を確認します。近似汎関数の解を厳密なHe多体解とは呼びません。

#### He：閉殻HF・交換のみLDA

PySCF 2.11.0 / LibxcのGaussian基底参照。外挿値・有限格子値・参照を区別。参照scriptの再実行は今回の共通runnerの測定に含まない。

- [PySCF 2.11.0 / LibxcのGaussian基底参照。外挿値・有限格子値・参照を区別。参照scriptの再実行は今回の共通runnerの測定に含まない。](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-hf.csv)
- [保存結果](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-lda_x.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Coulomb・Hartreeポテンシャル](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [He：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=ja)

共通実行例

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

非相対論・無限質量の点核、2電子が単一1s空間軌道を二重占有。2次中心差分と線形密度混合。HF交換の局所還元はこの2電子問題に限定。

[コード / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
python -m pytest -q
```

Heの球対称1s²・閉殻HFとスピン非偏極Dirac交換のみLDAを比較します。電子相関・分子・周期系は含みません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

#### [code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_helium_scf_and_independent_reference`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

作業フォルダ：quantum-atoms-2026-11-21/

```sh
python -m pytest -q test_atomic_radial.py -k test_helium_scf_and_independent_reference
```

## English

[Computed from the public atomic-code fixed inputs, with conditions, CSV profiles, convergence checks and independent references linked in the reading.](https://hrkoyama.github.io/numerical-methods-atlas/assets/quantum-atoms/helium.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-atoms/#helium) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#helium-ground-state-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en)

$$
\hat F=\hat h+\sum_{j\in\mathrm{occ}}(2\hat J_j-\hat K_j),\qquad \hat F\phi_i=\varepsilon_i\phi_i
$$

$$
\mathbf F\mathbf C=\mathbf S\mathbf C\boldsymbol\varepsilon,\qquad \mathbf C^\dagger\mathbf S\mathbf C=\mathbf I
$$

Closed-shell RHF equations for occupied spatial orbitals generally include nonlocal exchange. Published examples cover the spherical 1s²-helium local reduction and fixed-input H₂ RHF using a separate molecular-integral implementation. Their bases, discretizations and references differ; inspect each input and validation record below. These examples do not validate general multicenter molecules, open shells or correlated methods.

#### [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en)

$$
E[n]=T_s[n]+\int v_{\rm ext}n\,d\mathbf r+E_H[n]+E_{\rm xc}[n]+E_{NN}
$$

$$
[-\tfrac12\nabla^2+v_{\rm ext}+v_H+v_{\rm xc}]\phi_i=\varepsilon_i\phi_i
$$

$$
n(\mathbf r)=\sum_i f_i|\phi_i(\mathbf r)|^2,\quad \int n\,d\mathbf r=N,\quad v_{\rm xc}=\frac{\delta E_{\rm xc}}{\delta n}
$$

Representative local Kohn–Sham equations. Published examples cover spin-unpolarized exchange-only Dirac LDA for spherical helium and LDA exchange plus VWN5 correlation for fixed periodic He/He₂ cells. The radial atomic implementation and periodic PySCF workflows are separate series with different bases, boundaries and references. Inspect each input and validation record below; these examples do not validate GGA, hybrids, general materials or excited states.

#### Helium: closed-shell HF and exchange-only LDA

Common execution example · Approximation or discretization

$$
\left[\hat h_r+\frac12v_H[n]\right]u=\varepsilon u\quad(\mathrm{He}\;1s^2\ \mathrm{RHF})
$$

$$
\left[\hat h_r+v_H[n]+v_x^{\rm LDA}(n)\right]u=\varepsilon u,\qquad v_x^{\rm LDA}=-\left(\frac{3n}{\pi}\right)^{1/3}
$$

$$
\hat h_r=-\frac12\frac{d^2}{dr^2}-\frac2r,\qquad n(r)=\frac{2|u(r)|^2}{4\pi r^2}
$$

Atomic-unit radial equations restricted to isolated spherical closed-shell 1s² helium. The RHF vH/2 form is specific to two electrons sharing one spatial orbital. LDA is exchange-only, without correlation; no UHF, GGA, hybrid, general molecular or periodic-DFT example.

### Exact and reference solutions

Check independent closed-shell HF/exchange-only LDA references, SCF residuals, electron number and mesh refinement. Approximate-functional solutions are not labeled exact many-body helium solutions.

#### Helium: closed-shell HF and exchange-only LDA

PySCF 2.11.0 / Libxc finite-Gaussian references. Distinguish extrapolation, finite-grid values and references. Regenerating the independent reference is outside this measured runner.

- [PySCF 2.11.0 / Libxc finite-Gaussian references. Distinguish extrapolation, finite-grid values and references. Regenerating the independent reference is outside this measured runner.](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/reference-pyscf.json)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/results.json)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-hf.csv)
- [Saved result](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/results/profiles/helium-lda_x.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Hartree–Fock](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Coulomb and Hartree potentials](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-poisson/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Helium: closed-shell HF and exchange-only LDA](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/helium-ground-state/?lang=en)

Common execution example

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

Nonrelativistic infinite-mass point nucleus, two electrons doubly occupying a single 1s spatial orbital. Second-order central differences and linear density mixing. Local HF exchange reduction is specific to this two-electron problem.

[Code / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements-dev.txt
python run.py --input inputs.json --reference reference-pyscf.json --output output --figures
python -m pytest -q
```

Compare spherical 1s² closed-shell helium HF and spin-unpolarized Dirac exchange-only LDA. No electron correlation, molecules or periodic systems.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/quantum-atoms/2026-11-21/run.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/run.py)

#### [code/quantum-atoms/2026-11-21/test_atomic_radial.py](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/test_atomic_radial.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_helium_scf_and_independent_reference`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/quantum-atoms/2026-11-21/quantum-atoms-2026-11-21.zip)

Working directory: quantum-atoms-2026-11-21/

```sh
python -m pytest -q test_atomic_radial.py -k test_helium_scf_and_independent_reference
```
