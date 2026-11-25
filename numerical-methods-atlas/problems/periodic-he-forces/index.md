# 周期He₂の原子間力：解析力・有限差分・BOMD接続 / Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface

https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/

## 日本語

[非対称He₂の解析力をエネルギー有限差分とDFTK参照で比較。力のk点・基底・FFT・SCF収束とBOMDの局所接続確認。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/periodic-forces/#measured-results) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#periodic-he-forces)

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

#### 周期He₂の原子間力：解析力・有限差分・BOMD接続

共通実行例 · 診断量の定義

$$
F_{I\alpha}=-\frac{\partial E_{\rm BO}}{\partial R_{I\alpha}}
$$

$$
F^{\rm FD}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

#### 保存周期Heエネルギー・力の参照台帳

補助実行例 · 実行例の定義・検証式

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

### 厳密解・参照解

固定He₂配置のエネルギー有限差分と解析力、独立DFTK参照と保存された収束検査を区別します。長時間の第一原理MD精度を認定するものではありません。

#### [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

#### 周期He₂の原子間力：解析力・有限差分・BOMD接続

独立DFTK平面波計算：Γ／2³の解析力、8カットオフ設定、全6座標のエネルギー有限差分。共通Libxcと異なる有限基底の制約を明記。

- [独立DFTK平面波計算：Γ／2³の解析力、8カットオフ設定、全6座標のエネルギー有限差分。共通Libxcと異なる有限基底の制約を明記。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/reference-dftk.json)
- [保存結果](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json)
- [保存結果](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/solution.csv)
- [保存結果](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/scf.csv)
- [保存結果](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/finite-difference.csv)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja)

#### 保存周期Heエネルギー・力の参照台帳

元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja)

### 計算法

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [電子状態計算の基底](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [LDA・GGA・hybrid汎関数](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [周期電子状態とk点](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja)

共通実行例

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

固定した非対称2原子Heセル（5 bohr立方、4価電子、非偏極・整数占有、局所GTH、LDA_X＋VWN5）。PySCFライブラリを使う検証ドライバー。物理的な平衡He物質や長時間MDではありません。

[コード / ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[固定入力](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_periodic_forces.py
```

不正モデル・非有限値・参照の改変・SCF未収束・力/収束公差不達を拒否。未収束の力をBOMDへ渡さない。短い刻み比較は長時間NVEを保証しない。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

#### [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja)

補助実行例

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

新電子計算や基底・k点・cutoff走査は0回です。局所Heの成功を非局所擬ポテンシャルへ拡張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

#### [code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_saved_full_run_passes`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

作業フォルダ：periodic-forces-2026-11-22/

```sh
python -m pytest -q test_periodic_forces.py -k test_saved_full_run_passes
```

## English

[Asymmetric-He₂ analytic forces versus energy finite differences and DFTK reference. Force k-point, basis, FFT and SCF refinement, plus a local BOMD interface check.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/periodic-forces/#measured-results) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#periodic-he-forces-en)

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

#### Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface

Common execution example · Diagnostic definition

$$
F_{I\alpha}=-\frac{\partial E_{\rm BO}}{\partial R_{I\alpha}}
$$

$$
F^{\rm FD}_{I\alpha}(h)=-\frac{E(\mathbf R+h\mathbf e_{I\alpha})-E(\mathbf R-h\mathbf e_{I\alpha})}{2h}
$$

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

#### Immutable periodic-helium energy and force reference audit

Supplementary execution example · Example definition or validation formula

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

### Exact and reference solutions

Distinguish energy finite differences versus analytic forces, independent DFTK references and stored convergence checks for fixed He₂ configurations. This certifies no long-time first-principles MD accuracy.

#### [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-measurements)

Finite-grid numerical reference · Reference for the same problem

F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

#### Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface

Independent DFTK plane waves: Gamma/2³ analytic forces, eight cutoff settings and all-six-coordinate energy finite differences. State shared Libxc formulas and different finite-basis limits.

- [Independent DFTK plane waves: Gamma/2³ analytic forces, eight cutoff settings and all-six-coordinate energy finite differences. State shared Libxc formulas and different finite-basis limits.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/reference-dftk.json)
- [Saved result](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/result.json)
- [Saved result](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/solution.csv)
- [Saved result](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/scf.csv)
- [Saved result](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/finite-difference.csv)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en)

#### Immutable periodic-helium energy and force reference audit

Run zero electronic calculations. Preserve cell, units, local-only GTH, XC, electron counts and engine-version provenance; identify shared Libxc formulas.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en)

### Numerical methods

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

- [Kohn–Sham density functional theory / DFT](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Electronic-structure basis sets](https://hrkoyama.github.io/numerical-methods-atlas/methods/electronic-bases/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Self-consistent field iteration / SCF](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [LDA, GGA and hybrid functionals](https://hrkoyama.github.io/numerical-methods-atlas/methods/xc-functionals/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Pseudopotentials and PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Periodic electronic structure and k-point sampling](https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en)

Common execution example

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

Fixed asymmetric two-He cell (5-bohr cubic lattice, four valence electrons, unpolarized integer occupations, local GTH and LDA_X plus VWN5). A library-backed PySCF validation driver; not physical equilibrium helium or long-time MD.

[Code / ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[Fixed input](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python run.py --input inputs.json --output output
python -m pytest -q test_periodic_forces.py
```

Reject invalid models, nonfinite values, altered references, SCF nonconvergence and missed force/refinement criteria. Do not pass unconverged forces to BOMD. A short step comparison does not establish long-time NVE conservation.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

#### [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en)

Supplementary execution example

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

Audit saved six-coordinate FD and Gaussian/PW comparisons; source versions, local-only He GTH, XC/units/cell/electron count fixed. No new k/basis/cutoff scans. Artificial He2,4electrons,5bohr cell. Stored geometry/localGTH version/LDA_X+VWN/Libxc/PySCF/DFTK versions remain fixed in saved-data/periodic-he-reference.json. Energy hartree; force hartree/bohr.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No new SCF/DFTK/PySCF run, no basis/k/cutoff scans; preserve all old values and criteria. The He GTH is local-only, so its saved success does not test nonlocal projectors.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

#### [code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_saved_full_run_passes`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

Working directory: periodic-forces-2026-11-22/

```sh
python -m pytest -q test_periodic_forces.py -k test_saved_full_run_passes
```
