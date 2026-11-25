# MP2 perturbation theory / MP2摂動論

Status: educational-example

Locate perturbative electron correlation beyond mean field.

平均場から電子相関を加える摂動的な方法を位置付ける。

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

Other names: Møller–Plesset, メラー・プレセット

Comparison notes: Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#mp2
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#mp2



- Reference: https://doi.org/10.1103/PhysRev.46.618 — Primary publication entry point for the quantum-chemistry overview. Bibliographic/introductory review only; full-paper equations and numerical results have not been reproduced.

## Small fixed-input validation supplements

Restricted fixed examples: A tiny three-center H3+ RHF / MP2 / FCI example. Saved-reference audits are not new electronic calculations.

固定した小規模例に限定：3中心H3+の小RHF/MP2/FCI模型。保存参照監査は新しい電子計算ではありません。

- A tiny three-center H3+ RHF / MP2 / FCI example: https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json

Common execution records: [{"id": "h3plus-mp2-fci", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Maintain these fixed educational examples; broader extensions require a separately specified need.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`; h3plus-minimal)
- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`; h3plus-minimal)

#### 問題の図 (`method-problems-ja`)

##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

![固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。 独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) (`h3plus-mp2-fci`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。


#### 厳密解・参照解 (`method-references-ja`)

##### [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#references-ja) (`h3plus-minimal`)

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja) (`h3plus-mp2-fci`; 同じ問題の参照; 有限格子の数値参照)

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/quantum-chemistry/#mp2)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 3中心H3+の小RHF/MP2/FCI模型 (`h3plus-mp2-fci`)

[3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した小規模例に限定：3中心H3+の小RHF/MP2/FCI模型。保存参照監査は新しい電子計算ではありません。

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

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`; h3plus-minimal)
- [Closed-shell Hartree–Fock equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hartree-fock-model-en) (`hartree-fock-model`; h3plus-minimal)

#### Problem figures (`method-problems-en`)

##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) (`h3plus-minimal`)

![Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule. Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

Canonicalize RHF, evaluate the two-electron MP2 correction and9x9 FCI, and render the saved occupied-orbital density slice.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#code-en)

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) (`h3plus-mp2-fci`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.


#### Exact / reference solutions (`method-references-en`)

##### [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en#references-en) (`h3plus-minimal`)

- [A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-h3plus-mp2-fci-en) (`h3plus-mp2-fci`; Same-problem reference; Finite-grid numerical reference)

Independent operator assembly and two-electron RS2 identity qualify this fixed toy. No fresh external PySCF scalar. General molecular DFT, CC, multireference methods, precision energetics, geometry optimization and chemical accuracy remain unimplemented/unverified. MP2 is not variational.

[Existing reference profile](/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en#h3plus-mp2-fci-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/quantum-chemistry/#mp2)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### A tiny three-center H3+ RHF / MP2 / FCI example (`h3plus-mp2-fci`)

[A tiny three-center H3+ RHF / MP2 / FCI example](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

Demonstrate RHF, MP2 and finite-basis FCI for a tiny fixed three-center H3+ molecule.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Restricted fixed examples: A tiny three-center H3+ RHF / MP2 / FCI example. Saved-reference audits are not new electronic calculations.

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
