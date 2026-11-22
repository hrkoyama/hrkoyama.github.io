# Periodic electronic structure and k-point sampling / 周期電子状態とk点

Status: educational-example

Connect periodic boundaries, Bloch representations and Brillouin-zone integration.

周期境界、Bloch表現、Brillouin領域の積分をつなぐ。

Limited to a selected local GTH and fixed He cell. Nonlocal/PAW/general-element transferability, metals/smearing, a complete-basis limit and agreement with experiment are unvalidated. BZ quadrature meshes are distinct from band paths.

Other names: k点, Monkhorst–Pack, Bloch, Brillouin zone

Comparison notes: Distinguish metallic occupation/smearing dependence, finite-temperature free energy and zero-temperature energy. Whether Γ-only sampling is adequate depends on the system and cell.

金属の占有とsmearing幅の依存、有限温度の自由エネルギーと零温度エネルギーを区別します。Γ点だけで十分かは系とセルに依存します。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#k-point
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#k-point



- Reference: https://doi.org/10.1103/PhysRevB.13.5188 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

Periodic scope: Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals.

{
  "release": {
    "family": "periodic-dft",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip",
    "sha256": "f331515e3ad419b5435dbf851553c6b853b28b2432801fc13c84109faa362df8",
    "manifest": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/source-manifest.json",
    "manifest_sha256": "1ac7fe2531934a598b7d9b69930c5a8a83f6b5bf2a67ae9f0616f35aa63f34fd",
    "verification": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json",
    "archive_directory": "periodic-dft-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/periodic-dft/2026-11-22/",
  "examples": [
    "periodic-he-dft"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "固定した1原子単純立方Heセルの周期KS-DFT。PySCFを使う教育用ワークフローで、Γ点／k点、Gaussian軌道基底、FFT補助格子、SCF公差を別々に検査し、同じGTHパラメータ・LDA交換＋VWN5相関のDFTK平面波計算と比較。平衡He結晶や一般物質・金属の検証ではありません。",
    "en": "Periodic KS-DFT for one fixed simple-cubic He cell. An educational PySCF workflow separately checks Gamma/k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF tolerances against independent DFTK plane waves with identical GTH parameters and LDA exchange plus VWN5 correlation. Does not validate equilibrium helium solids, general materials or metals."
  },
  "implementation": "Original educational workflow using PySCF; independent reference uses DFTK."
}

Force scope: Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

{
  "release": {
    "family": "periodic-forces",
    "version": "2026-11-22",
    "download": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip",
    "sha256": "137d7981769d503d231b0c4bcc60a2ca61746faaadd0ee39d544dcf4efa07b19",
    "manifest": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/source-manifest.json",
    "manifest_sha256": "57f7180fcaf148dcffa60f2a689e7e39b2938fb4083c642d3ac7cc1813cccbc8",
    "verification": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/verification.json",
    "archive_directory": "periodic-forces-2026-11-22"
  },
  "code_base": "https://hrkoyama.github.io/code/periodic-forces/2026-11-22/",
  "examples": [
    "periodic-he-forces"
  ],
  "run_commands": [
    "python run.py --input inputs.json --output output"
  ],
  "scope": {
    "ja": "非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。",
    "en": "Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated."
  },
  "implementation": "Original PySCF force-validation workflow with independent DFTK reference; BOMD adapter is locally checked, not a validated production trajectory."
}

Common execution records: [{"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}, {"id": "periodic-he-forces", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-forces-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-forces-en"}}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/k-point/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; periodic-he-dft, periodic-he-forces)

#### 問題の図 (`method-problems-ja`)

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) (`periodic-he-dft`)

![固定Heセルの周期LDA：Γ点とkメッシュ、Gaussian軌道基底・FFT格子・SCFを分離。DFTK平面波参照の打切り収束と差も表示。](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#code-ja)

- [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja) (`periodic-he-dft`) · [コードZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

![非対称He₂の解析力をエネルギー有限差分とDFTK参照で比較。力のk点・基底・FFT・SCF収束とBOMDの局所接続確認。](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

- [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja) (`periodic-he-forces`) · [コードZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) (`periodic-he-dft`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) (`periodic-he-forces`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#k-point)
- 独立参照: [独立参照の保存データ](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF (`periodic-he-dft`)

[周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

固定した1原子単純立方Heセル（格子定数4 bohr、価電子2、非偏極LDA_X＋VWN5、局所GTH）。PySCFを使う実行・検証ワークフロー。11設定でk点・Gaussian軌道基底・FFT補助格子・SCFを別々に比較し、Γ／2³は独立DFTK平面波参照と照合。平衡He結晶・完全基底・金属・一般物質は未検証。

##### 周期He₂の原子間力：解析力・有限差分・BOMD接続 (`periodic-he-forces`)

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

非対称な2原子He周期セル・局所GTH・LDA交換＋VWN5。PySCFの解析力（Gaussian基底の微分を含む）を全6座標のエネルギー有限差分とDFTK平面波参照で照合し、力の基底・k点・SCF・FFT収束を分離。BOMDの力供給と短い刻み比較に限定し、長時間NVE・CPMD・一般物質は未検証。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)

###### 関連ソース

- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### 配布版のテスト

- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; periodic-he-dft, periodic-he-forces)

#### Problem figures (`method-problems-en`)

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) (`periodic-he-dft`)

![Periodic LDA for fixed He: separate Gamma/k sampling, Gaussian orbital basis, FFT grid and SCF. Includes independently converged DFTK plane-wave reference differences.](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#code-en)

- [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en) (`periodic-he-dft`) · [Code ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) (`periodic-he-forces`)

![Asymmetric-He₂ analytic forces versus energy finite differences and DFTK reference. Force k-point, basis, FFT and SCF refinement, plus a local BOMD interface check.](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#code-en)

- [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en) (`periodic-he-forces`) · [Code ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) (`periodic-he-dft`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) (`periodic-he-forces`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#k-point)
- Independent reference: [Saved independent-reference data](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/reference-dftk.json)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Periodic-He KS-LDA: Gamma, k meshes, basis and SCF (`periodic-he-dft`)

[Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-dft/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Fixed one-atom simple-cubic He cell (lattice constant 4 bohr, two valence electrons, unpolarized LDA_X plus VWN5, local GTH). A PySCF execution/validation workflow. Eleven settings separately compare k sampling, Gaussian orbital basis, auxiliary FFT grid and SCF; Gamma and 2³ are compared with independent DFTK plane waves. Equilibrium helium, complete-basis, metals and general materials remain unvalidated.

##### Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface (`periodic-he-forces`)

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/periodic-he-forces/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic-forces-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/inputs.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Asymmetric two-He periodic cell with local GTH and LDA exchange plus VWN5. Compare PySCF analytic forces, including Gaussian-basis derivatives, with energy finite differences for all six coordinates and independent DFTK plane waves. Separate force basis, k-point, SCF and FFT refinement. BOMD coverage is a force interface and short step comparison; long NVE, CPMD and general materials remain unvalidated.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

[Related code edition / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)

###### Related source

- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)

###### Package tests

- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python run.py --input inputs.json --output output
```
