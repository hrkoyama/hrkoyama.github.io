# Centered spatial difference / 空間中心差分

Status: educational-example

Read about Centered spatial difference, follow the original references and inspect related educational code and checks.

「空間中心差分」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: 中心差分, 中心差分法, 中央差分, central difference, central finite difference

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://doi.org/10.1007/BF01448839 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1002/cpa.3160070112 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1002/cpa.3160130205 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

- Reaction-diffusion: separate second-order space and fourth-order time: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/
- Turing instability: linear growth and small-amplitude patterns: https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json

- Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/
- Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json

Common execution records: [{"id": "reaction-diffusion-fourier", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "turing-schnakenberg", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-nonlinear", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-pattern", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; heat-periodic, heat-dirichlet, reaction-diffusion-fourier)
- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)

#### 問題の図 (`method-problems-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`)

![周期Fourierモードの線形反応拡散。16/32/64格子の連続解誤差と、固定格子での半離散厳密解に対する時間誤差を分けた保存収束図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#code-ja)

- [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) (`reaction-diffusion-fourier`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) (`schnakenberg-nonlinear`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) (`schnakenberg-pattern`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) (`heat-periodic`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) (`heat-dirichlet`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja#references-ja) (`reaction-diffusion-fourier`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/stability/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 反応拡散：空間2次と時間4次を分けて測る (`reaction-diffusion-fourier`)

[反応拡散：空間2次と時間4次を分けて測る](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。

##### Turing不安定性：線形成長率と小振幅パターン (`turing-schnakenberg`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

##### Schnakenberg有限振幅過渡：非線形性と独立参照 (`schnakenberg-nonlinear`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

##### Schnakenberg飽和パターン：近定常性と格子・時間収束 (`schnakenberg-pattern`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; heat-periodic, heat-dirichlet, reaction-diffusion-fourier)
- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)

#### Problem figures (`method-problems-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`)

![Stored linear periodic Fourier reaction–diffusion refinement separates continuum errors on 16/32/64 grids from temporal errors against a fixed-grid semidiscrete exact solution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/reaction-diffusion-fourier.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#code-en)

- [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) (`reaction-diffusion-fourier`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) (`turing-schnakenberg`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) (`schnakenberg-nonlinear`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) (`schnakenberg-pattern`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) (`heat-periodic`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) (`heat-dirichlet`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en#references-en) (`reaction-diffusion-fourier`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/stability/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Reaction-diffusion: separate second-order space and fourth-order time (`reaction-diffusion-fourier`)

[Reaction-diffusion: separate second-order space and fourth-order time](https://hrkoyama.github.io/numerical-methods-atlas/problems/reaction-diffusion-fourier/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-fourier/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions.

##### Turing instability: linear growth and small-amplitude patterns (`turing-schnakenberg`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

##### Finite-amplitude Schnakenberg transient: nonlinearity and independent reference (`schnakenberg-nonlinear`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

##### Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence (`schnakenberg-pattern`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)
- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_numerics.py
```
