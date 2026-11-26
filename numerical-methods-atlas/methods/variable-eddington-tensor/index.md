# Variable Eddington tensor (VET) / 可変Eddingtonテンソル（VET）

Status: educational-example

Use the tensor form of the VEF closure. Retain the full three-dimensional angular measure in two-dimensional space and check off-diagonal pressure and flux.

VEFの多次元でのテンソル閉包を用います。2D空間でも3D角度測度を保ち、非対角成分を含む圧力と流束を確認します。

Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

Other names: VET, variable Eddington tensor, 可変エディントンテンソル, transport-derived closure

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/



- Reference: https://arxiv.org/pdf/1201.2223 — Section3.1 algorithmStep1; Section3.4 PDFp8, equations22–23 and discussion; Section6.5 shadow-test scope description read. Limits: Not a reproduction of Athena, mixed-frameRHD, gas coupling, shocks or the paper shadow/cloud-ablation test.
- Reference: https://arxiv.org/pdf/1201.2222 — Equations8–16 source/opacity/moment conventions, Section3.2 angular quadrature Eq17–19 and two-stream warning; Section3.3 Eq20 formal solution and Section3.5 boundary scope read. Limits: Proposed Fourier formal solver is not their short-characteristics/interpolation algorithm. No multifrequency, ALI, stellar atmosphere or timing reproduction claim.
- Reference: https://arxiv.org/pdf/2301.04758 — Section2, PDFpp3–4: transport Eq1, moment equations Eq2, angular tensor and boundary factor Eq3, fixed-point steps. Introduction on independent spatial discretizations also read. Limits: No claim of full59page reading, high-order mixedFEM reproduction, curved-mesh, multigrid or scalability validation.
- Reference: https://arxiv.org/pdf/1306.0010 — Section2.3 PDFp5, equations11–17: localM1 tensor, trace/covariance constraints and chi(reducedflux). Introduction distinction from formalVET also read. Limits: No Hyperion/RHD solver or reduced-light-speed/timing validation. InstitutionalPDF endpoint returned401; arXiv original-author copy was read.

## Small fixed-input validation supplements

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

- Variable Eddington tensor: a periodic 2D nonparallel-source control: https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json

Common execution records: [{"id": "vet-fourier-source2d", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/variable-eddington-tensor/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [静止灰色輻射のVEF・VETモーメント閉包](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#static-grey-variable-eddington-moments-ja) (`static-grey-variable-eddington-moments`; vet-fourier-source2d)

#### 問題の図 (`method-problems-ja`)

##### [可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`)

![非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#code-ja)

- [可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja) (`vet-fourier-source2d`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja#references-ja) (`vet-fourier-source2d`)

- [本例のために導出した周期2D VETの連続Fourier応答](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-vet-fourier-source2d-ja) (`vet-fourier-source2d`; 同じ問題の参照; 解析参照)

正の指定等方輻射源に対する連続角度Fourier応答が、同じ固定問題の解析参照です。点値・面位置・複素位相を区別し、異なるHO/LO離散化の差は保存します。 局所M1との比較は閉包の点ごとの診断だけで、M1方程式は解きません。Athena・短い特性線法・影・交差ビーム・RHD・境界閉包の再現でもなく、固定格子でHO/LOの厳密一致や普遍的な収束率を主張しません。

[既存の参照図](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja#vet-fourier-source2d-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/variable-eddington/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 可変エディントンテンソル：周期2D非平行源の固定検証 (`vet-fourier-source2d`)

[可変エディントンテンソル：周期2D非平行源の固定検証](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

非平行な2つの源モードから全S²角度分布と3×3テンソルを求め、Dxyを含む保存的モーメント式と閉形式参照を比較します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Static grey VEF/VET moment closure](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#static-grey-variable-eddington-moments-en) (`static-grey-variable-eddington-moments`; vet-fourier-source2d)

#### Problem figures (`method-problems-en`)

##### [Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`)

![Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/vet-fourier-source2d.png)

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#code-en)

- [Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en) (`vet-fourier-source2d`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.


#### Exact / reference solutions (`method-references-en`)

##### [Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en#references-en) (`vet-fourier-source2d`)

- [Authored continuum Fourier response for periodic 2D VET](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-vet-fourier-source2d-en) (`vet-fourier-source2d`; Same-problem reference; Analytic reference)

The continuum-angle Fourier response to the prescribed positive isotropic source is an analytic reference for this same fixed problem. Keep point/face locations and complex phase distinct, retaining the independent HO/LO discretization gap. Pointwise M1 comparison is a closure diagnostic; no M1 PDE is solved. This is not a reproduction of Athena, short characteristics, shadows, crossing beams, RHD or boundary closures, and does not claim exact fixed-grid HO/LO agreement or universal convergence rates.

[Existing reference profile](/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en#vet-fourier-source2d-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/variable-eddington/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Variable Eddington tensor: a periodic 2D nonparallel-source control (`vet-fourier-source2d`)

[Variable Eddington tensor: a periodic 2D nonparallel-source control](https://hrkoyama.github.io/numerical-methods-atlas/problems/vet-fourier-source2d/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/vet-fourier-source2d/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Use two nonparallel source modes to compute full-S2 angular moments and a3x3 tensor, then compare conservative moment equations including Dxy with a closed-form reference.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/atlas-variable-eddington-controls-2026-11-26.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/verification.json)

###### Related source

- [/code/validated-examples/2026-11-26/variable-eddington-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/run.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/primary.py)
- [/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/analytic_reference.py)

###### Package tests

- [/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py](https://hrkoyama.github.io/code/validated-examples/2026-11-26/variable-eddington-controls/test_cases.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
