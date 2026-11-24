# Implicit midpoint / 陰的中点則

Status: educational-example

Read about Implicit midpoint, follow the original references and inspect related educational code and checks. Additional fixed examples: Oblique s/p incidence on a Lorentz-dispersive slab. See each release for assumptions and checked scope. Additional fixed examples: Long-time grazing PML in a dispersive medium. See each release for assumptions and checked scope.

「陰的中点則」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：Lorentz分散板へのs/p斜め入射。条件と検証範囲は各配布版で確認してください。 追加固定例：分散媒質の浅い入射角と長時間PML。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed. Additional fixed examples: The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

Other names: 陰的中点法, implicit midpoint rule

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

- Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/
- Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json

- Oblique s/p incidence on a Lorentz-dispersive slab: https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/result.json

- Long-time grazing PML in a dispersive medium: https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json

Common execution records: [{"id": "schnakenberg-nonlinear", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-pattern", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lorentz-oblique-sp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "dispersive-grazing-pml", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; quartic-oscillator)
- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)
- [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja) (`maxwell-lorentz`; lorentz-oblique-sp, dispersive-grazing-pml)

#### 問題の図 (`method-problems-ja`)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja) (`quartic-oscillator`)

![保存済みのt≤10の正準位相軌道。手法違いは同一問題の比較。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja) (`schnakenberg-nonlinear`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

- [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja) (`schnakenberg-pattern`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`)

![保存したp偏光の実電場をky=4の周期y方向へ再構成した場。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

単一ky Yee空間演算と局所の陰的中点Lorentz ADE。p偏光の両電場に分極を結合し、同格子の真空波束で入射・伝播位相を除きます。直接Ohmic・物質減衰仕事と修正エネルギーを別々に集計します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#code-ja)

- [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) (`lorentz-oblique-sp`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`)

![保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#code-ja)

- [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。


#### 厳密解・参照解 (`method-references-ja`)

##### [4次ポテンシャルの非線形振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=ja#references-ja) (`quartic-oscillator`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja#references-ja) (`lorentz-oblique-sp`)

- [斜め入射の複素Fresnel係数とLorentz板の直接散逸](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lorentz-oblique-sp-ja) (`lorentz-oblique-sp`; 同じ問題の参照; 解析参照)

任意の横方向分布ではなく単一kyの実空間制限です。1つの受動Lorentz極と有限帯域・有限窓のみ。Gaussian尾は厳密には非零で、窓診断と参照誤差を別記します。 全周波数で厳密にcap反射が未到達という証明ではありません。

[既存の参照図](/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja#lorentz-oblique-sp-ja-measurements)

##### [分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#references-ja) (`dispersive-grazing-pml`)

- [浅角度分散波束の長時間・同格子孤立境界参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja) (`dispersive-grazing-pml`; 同じ問題の参照; 有限格子の数値参照)

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

[既存の参照図](/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

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

##### Lorentz分散板へのs/p斜め入射 (`lorentz-oblique-sp`)

[Lorentz分散板へのs/p斜め入射](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

有限波束の実進行から複素r/t・R/T・直接散逸を求め、複素Fresnel参照と比較します。

##### 分散媒質の浅い入射角と長時間PML (`dispersive-grazing-pml`)

[分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; quartic-oscillator)
- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)
- [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en) (`maxwell-lorentz`; lorentz-oblique-sp, dispersive-grazing-pml)

#### Problem figures (`method-problems-en`)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en) (`quartic-oscillator`)

![Stored canonical phase orbits for t≤10; methods remain variants of one problem.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/quartic-oscillator.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en) (`schnakenberg-nonlinear`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

- [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en) (`schnakenberg-pattern`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip)

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`)

![Actual saved p-polarized electric field reconstructed over the periodic y direction at ky=4. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/results/lorentz-oblique-sp-preview.png)

Use the single-ky Yee spatial operator and local implicit-midpoint Lorentz ADE. Couple both p-polarized electric components to polarization, and remove incident propagation with a matched vacuum pulse on the same grid. Accumulate direct Ohmic and material-damping work separately from modified energy.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#code-en)

- [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) (`lorentz-oblique-sp`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`)

![Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#code-en)

- [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.


#### Exact / reference solutions (`method-references-en`)

##### [Nonlinear quartic-potential oscillator](https://hrkoyama.github.io/numerical-methods-atlas/problems/quartic-oscillator/?lang=en#references-en) (`quartic-oscillator`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en#references-en) (`lorentz-oblique-sp`)

- [Complex oblique Fresnel coefficients and direct Lorentz-slab loss](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lorentz-oblique-sp-en) (`lorentz-oblique-sp`; Same-problem reference; Analytic reference)

This is a genuine single-ky restriction rather than arbitrary transverse data. It covers one passive Lorentz pole and a fixed finite band/window. Gaussian tails are nonzero; window diagnostics and reference errors are reported separately. No strict all-frequency no-return proof is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en#lorentz-oblique-sp-en-measurements)

##### [Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#references-en) (`dispersive-grazing-pml`)

- [Isolated same-grid reference for a long grazing dispersive packet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en) (`dispersive-grazing-pml`; Same-problem reference; Finite-grid numerical reference)

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

[Existing reference profile](/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

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

##### Oblique s/p incidence on a Lorentz-dispersive slab (`lorentz-oblique-sp`)

[Oblique s/p incidence on a Lorentz-dispersive slab](https://hrkoyama.github.io/numerical-methods-atlas/problems/lorentz-oblique-sp/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lorentz-oblique-sp/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/atlas-maxwell-lorentz-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/verification.json)

Measure complex r/t, power fractions and direct dissipation from actual finite-pulse evolutions and compare them with complex Fresnel slab references.

##### Long-time grazing PML in a dispersive medium (`dispersive-grazing-pml`)

[Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json)

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/reference_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/slab_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/run.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/references/isolated_reference.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/centered_pml.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/modal_yee_draft.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/pml_evolution.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/specifications.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-lorentz/test_lorentz.py)
- [/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/test_grazing.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
