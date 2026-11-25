# Configuration interaction / CI / 配置間相互作用（CI）

Status: educational-example

Explain many-electron configuration expansions and truncation.

多電子配置の展開と打切りの意味を整理する。

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

Other names: CI, CISD, FCI, 配置間相互作用

Comparison notes: Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#configuration-interaction
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#configuration-interaction



- Reference: https://doi.org/10.1016/0009-2614(84)85513-X — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

## Small fixed-input validation supplements

Restricted fixed examples: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI, A tiny three-center H3+ RHF / MP2 / FCI example. Saved-reference audits are not new electronic calculations.

固定した小規模例に限定：最小基底H2のRHF/UHF/FCI・2固定幾何、3中心H3+の小RHF/MP2/FCI模型。保存参照監査は新しい電子計算ではありません。

- Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI: https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/
- A tiny three-center H3+ RHF / MP2 / FCI example: https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "h2-rhf-uhf-fci", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "h3plus-mp2-fci", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain these fixed educational examples; broader extensions require a separately specified need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; h2-rhf, h3plus-minimal)
- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; h2-rhf, h3plus-minimal)
- [最小2電子模型のスピン非制限HF](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja) (`unrestricted-hartree-fock-model`; h2-rhf)

#### 問題の図 (`method-problems-ja`)

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

![固定入力のH₂ RHF：核間距離・s型基底系列・SCF公差を分けて比較。PySCFとの差、反復履歴と有限基底の残る制約を解説。](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

- [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja) (`h2-rhf-uhf-fci`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

![固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) (`h3plus-mp2-fci`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。


#### 厳密解・参照解 (`method-references-ja`)

##### [H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#references-ja) (`h2-rhf`)

- [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja) (`h2-rhf-uhf-fci`; 同じ問題の参照; 半解析参照)

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

[既存の参照図](/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-measurements)

##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#references-ja) (`h3plus-minimal`)

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja) (`h3plus-mp2-fci`; 同じ問題の参照; 有限格子の数値参照)

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#configuration-interaction)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 最小基底H2のRHF/UHF/FCI・2固定幾何 (`h2-rhf-uhf-fci`)

[H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

##### 3中心H3+の小RHF/MP2/FCI模型 (`h3plus-mp2-fci`)

[3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した小規模例に限定：最小基底H2のRHF/UHF/FCI・2固定幾何、3中心H3+の小RHF/MP2/FCI模型。保存参照監査は新しい電子計算ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; h2-rhf, h3plus-minimal)
- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; h2-rhf, h3plus-minimal)
- [Unrestricted HF in a minimal two-electron model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#unrestricted-hartree-fock-model-en) (`unrestricted-hartree-fock-model`; h2-rhf)

#### Problem figures (`method-problems-en`)

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) (`h2-rhf`)

![Fixed-input H₂ RHF: separate geometry, s-basis sequence and SCF-tolerance comparisons. Reading states PySCF differences, histories and remaining finite-basis limits.](https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/preview.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#code-en)

- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en) (`h2-rhf-uhf-fci`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

![Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) (`h3plus-mp2-fci`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.


#### Exact / reference solutions (`method-references-en`)

##### [H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en#references-en) (`h2-rhf`)

- [Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h2-rhf-uhf-fci-en) (`h2-rhf-uhf-fci`; Same-problem reference; Semi-analytic reference)

Only2fixed distances. Finite-basis FCI is not continuum exactness, and UHF stationarity is not a general global-minimum guarantee. Angular/complete-basis convergence and a broad dissociation curve remain untested.

[Existing reference profile](/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en#h2-rhf-uhf-fci-en-measurements)

##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#references-en) (`h3plus-minimal`)

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en) (`h3plus-mp2-fci`; Same-problem reference; Finite-grid numerical reference)

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

[Existing reference profile](/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#configuration-interaction)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI (`h2-rhf-uhf-fci`)

[H₂ molecular RHF: independent reference, SCF and s-basis refinement](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Compare RHF, broken-spin UHF and finite-basis FCI for H2 at two fixed geometries in the same minimal basis.

##### A tiny three-center H3+ RHF / MP2 / FCI example (`h3plus-mp2-fci`)

[A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Restricted fixed examples: Minimal-basis H2: RHF, broken-spin UHF and finite-basis FCI, A tiny three-center H3+ RHF / MP2 / FCI example. Saved-reference audits are not new electronic calculations.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/molecules.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/molecules.py)
- [/code/validated-examples/2026-11-25/quantum-small/coupled_md.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/coupled_md.py)
- [/code/validated-examples/2026-11-25/quantum-small/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/io_utils.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/periodic_projector.py)
- [/code/validated-examples/2026-11-25/quantum-small/plot_results.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/plot_results.py)

###### Package tests

- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
