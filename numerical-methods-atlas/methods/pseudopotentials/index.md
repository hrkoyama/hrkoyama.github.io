# Pseudopotentials and PAW / 擬ポテンシャル・PAW

Status: educational-example

Map core-electron treatments and effective electronic representations.

内殻の扱いと有効な電子状態表現の位置付けを示す。

Limited to a selected local GTH and fixed He cell. Nonlocal/PAW/general-element transferability, metals/smearing, a complete-basis limit and agreement with experiment are unvalidated. BZ quadrature meshes are distinct from band paths.

Other names: 擬ポテンシャル, PAW, norm-conserving, ultrasoft

Comparison notes: Do not compare absolute energy zeroes across different pseudopotentials without alignment. Cutoff convergence alone does not establish transferability.

異なる擬ポテンシャルの全エネルギーの零点を無条件に比較しません。平面波カットオフの収束だけで移植性が証明されるわけではありません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#pseudopotentials
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#pseudopotentials



- Reference: https://doi.org/10.1103/PhysRevLett.43.1494 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.
- Reference: https://doi.org/10.1103/PhysRevB.41.7892 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.
- Reference: https://doi.org/10.1103/PhysRevB.50.17953 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

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

## Small fixed-input validation supplements

Restricted fixed examples: Immutable periodic-helium energy and force reference audit, A three-wave periodic projector and Fermi-occupation model. Saved-reference audits are not new electronic calculations. No new SCF/DFTK/PySCF run, no basis/k/cutoff scans; preserve all old values and criteria. The He GTH is local-only, so its saved success does not test nonlocal projectors. The authored rank-one kernel is not an element-fitted norm-conserving pseudopotential. No self-consistent Hartree/XC, real metal, general material or long-time MD success.

固定した小規模例に限定：保存周期Heエネルギー・力の参照台帳、3平面波の非局所projectorと有限温度占有。保存参照監査は新しい電子計算ではありません。 新電子計算や基底・k点・cutoff走査は0回です。局所Heの成功を非局所擬ポテンシャルへ拡張しません。 元素に合わせたノルム保存擬ポテンシャルではありません。実金属、自己無撞着Hartree/XC、一般材料や長時間MDは未検証です。

- Immutable periodic-helium energy and force reference audit: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/
- A three-wave periodic projector and Fermi-occupation model: https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "periodic-he-dft", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-dft-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-dft-en"}}, {"id": "periodic-he-forces", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#periodic-he-forces-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#periodic-he-forces-en"}}, {"id": "periodic-he-reference-cards", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "periodic-projector-occupations", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain fixed inputs, saved references and release integrity for the existing small examples; rerun a few representative cases when needed. Large basis/k-point sweeps, expensive independent-reference regeneration and long BOMD/CPMD trajectories are considered separately only on explicit need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`; periodic-he-dft, periodic-he-forces)
- [3平面波・非局所核と平均Fermi占有](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja) (`finite-projector-fermi-model`; finite-projector-fermi)

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

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja) (`periodic-he-reference-cards`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

##### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) (`finite-projector-fermi`)

![3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。 自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#code-ja)

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja) (`periodic-projector-occupations`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期HeのKS-LDA：Γ点・kメッシュ・基底・SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=ja#references-ja) (`periodic-he-dft`)

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

[既存の参照図](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-measurements)

##### [周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#references-ja) (`periodic-he-forces`)

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照; 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

[既存の参照図](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-measurements)

##### [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#references-ja) (`finite-projector-fermi`)

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja) (`periodic-projector-occupations`; 同じ問題の参照; 半解析参照)

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

[既存の参照図](/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#pseudopotentials)
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

##### 保存周期Heエネルギー・力の参照台帳 (`periodic-he-reference-cards`)

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

##### 3平面波の非局所projectorと有限温度占有 (`periodic-projector-occupations`)

[3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)

###### 関連ソース

- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### 配布版のテスト

- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Local Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#kohn-sham-model-en) (`kohn-sham-model`; periodic-he-dft, periodic-he-forces)
- [Three-wave nonlocal kernel and mean Fermi occupations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-projector-fermi-model-en) (`finite-projector-fermi-model`; finite-projector-fermi)

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

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en) (`periodic-he-reference-cards`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

##### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) (`finite-projector-fermi`)

![Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model. Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

Solve3x3 Hermitian blocks, determine fixed-N Fermi occupations and differentiate Helmholtz free energy including entropy.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#code-en)

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en) (`periodic-projector-occupations`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic-He KS-LDA: Gamma, k meshes, basis and SCF](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-dft/?lang=en#references-en) (`periodic-he-dft`)

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-measurements)

##### [Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en#references-en) (`periodic-he-forces`)

- [Immutable periodic-helium energy and force reference audit](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-he-reference-cards-en) (`periodic-he-reference-cards`; Same-problem reference; Finite-grid numerical reference)

Audit of stored6force components, energy differences and Gaussian/PW comparisons; zero new electronic solves. No new basis/k/cutoff scans, materials, metals or longMD claim.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en#periodic-he-reference-cards-en-measurements)

##### [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en#references-en) (`finite-projector-fermi`)

- [A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-periodic-projector-occupations-en) (`periodic-projector-occupations`; Same-problem reference; Semi-analytic reference)

Authored linear3-wave Hamiltonian with independent-particle mean Fermi occupations, not an integer-particle canonical many-body ensemble. No self-consistent Hartree/XC, element-fitted norm-conserving PSP, real metal, general material or longMD validation.

[Existing reference profile](/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en#periodic-projector-occupations-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#pseudopotentials)
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

##### Immutable periodic-helium energy and force reference audit (`periodic-he-reference-cards`)

[Periodic-He₂ forces: analytic derivatives, finite differences and BOMD interface](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Map saved periodic-He energies and six-coordinate forces to unchanged independent references and criteria.

##### A three-wave periodic projector and Fermi-occupation model (`periodic-projector-occupations`)

[A three-wave periodic projector and Fermi-occupation model](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Show a genuine rank-one nonlocal kernel and finite-temperature occupations in a three-wave periodic educational model.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic-dft-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/verification.json)

###### Related source

- [/code/periodic-dft/2026-11-22/periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/periodic_dft.py)
- [/code/periodic-dft/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/run.py)
- [/code/periodic-forces/2026-11-22/periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/periodic_forces.py)
- [/code/periodic-forces/2026-11-22/bomd.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/bomd.py)
- [/code/periodic-forces/2026-11-22/run.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### Package tests

- [/code/periodic-dft/2026-11-22/test_periodic_dft.py](https://hrkoyama.github.io/code/periodic-dft/2026-11-22/test_periodic_dft.py)
- [/code/periodic-forces/2026-11-22/test_periodic_forces.py](https://hrkoyama.github.io/code/periodic-forces/2026-11-22/test_periodic_forces.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python run.py --input inputs.json --output output
```
