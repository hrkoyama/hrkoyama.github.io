# 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF / Periodic-He KS-LDA: Gamma, k meshes, basis and SCF

https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/

## 日本語

[固定Heセルの周期LDA：Γ点とkメッシュ、Gaussian軌道基底・FFT格子・SCFを分離。DFTK平面波参照の打切り収束と差も表示。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-dft/#measured-results) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#periodic-he-dft)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

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

#### 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF

共通実行例 · 近似・離散化の式

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)
$$

$$
n(\mathbf r)=2\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k}|\psi_{n\mathbf k}(\mathbf r)|^2
$$

3次元周期・固定HeセルのKS-LDA。BZ積分メッシュとバンド経路、数値収束と物理近似を区別。

### 厳密解・参照解

固定した小周期Heセルの独立DFTK参照・SCF・基底・k点の保存検査を使います。擬ポテンシャルと交換のみLDAのモデル範囲に限定します。

#### 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF

別実行のDFTK平面波KS-LDA。Γ／2³で同一モデルを比較し、平面波打切り収束を保存。異なる有限軌道基底のため機械精度一致は要求しない。

- [別実行のDFTK平面波KS-LDA。Γ／2³で同一モデルを比較し、平面波打切り収束を保存。異なる有限軌道基底のため機械精度一致は要求しない。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json)
- [保存結果](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json)
- [保存結果](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/solution.csv)
- [保存結果](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/scf.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [周期電子状態とk点](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja)

共通実行例

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

固定中性セル・2電子閉殻、整数占有。Γ中心の分率k座標と一様重みを保存。同一のGTH係数・Libxc汎関数で独立DFTKと比較し、エネルギー原点のフィットはしない。

[コード / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_periodic_dft.py
```

不正入力・重なり行列の悪条件・SCF未収束・公差不達を明示して失敗。低い残差だけでk点／基底収束や物理モデルを保証しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)

#### [code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_fixed_input_validation`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

作業フォルダ：periodic-dft-2026-11-22/

```sh
python -m pytest -q test_periodic_dft.py -k test_fixed_input_validation
```

## English

[Periodic LDA for fixed He: separate Gamma/k sampling, Gaussian orbital basis, FFT grid and SCF. Includes independently converged DFTK plane-wave reference differences.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-dft/#measured-results) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#periodic-he-dft-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

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

#### Periodic-He KS-LDA: Gamma, k meshes, basis and SCF

Common execution example · Approximation or discretization

$$
\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)
$$

$$
n(\mathbf r)=2\sum_{n\mathbf k}w_{\mathbf k}f_{n\mathbf k}|\psi_{n\mathbf k}(\mathbf r)|^2
$$

KS-LDA for a fixed 3D periodic He cell. BZ integration meshes differ from band paths; numerical convergence differs from physical-model accuracy.

### Exact and reference solutions

Use stored independent DFTK, SCF, basis and k-point checks for a fixed small periodic He cell, limited to the pseudopotential and exchange-only LDA model.

#### Periodic-He KS-LDA: Gamma, k meshes, basis and SCF

Separately executed DFTK plane-wave KS-LDA at Gamma and 2³ for the same model, with cutoff convergence saved. Different finite orbital bases are compared within a stated tolerance, without machine-precision claims.

- [Separately executed DFTK plane-wave KS-LDA at Gamma and 2³ for the same model, with cutoff convergence saved. Different finite orbital bases are compared within a stated tolerance, without machine-precision claims.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json)
- [Saved result](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json)
- [Saved result](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/solution.csv)
- [Saved result](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/scf.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Periodic electronic structure and k-point sampling](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en)

Common execution example

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

Fixed neutral two-electron closed-shell cell with integer occupations. Explicit Gamma-centered fractional k coordinates and equal weights. Independent DFTK uses identical GTH coefficients and Libxc functionals; no fitted energy shifts.

[Code / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_periodic_dft.py
```

Invalid inputs, excessive overlap conditioning, SCF nonconvergence and missed tolerances fail explicitly. Small residuals alone do not establish k/basis convergence or physical-model accuracy.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)

#### [code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_fixed_input_validation`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

Working directory: periodic-dft-2026-11-22/

```sh
python -m pytest -q test_periodic_dft.py -k test_fixed_input_validation
```
