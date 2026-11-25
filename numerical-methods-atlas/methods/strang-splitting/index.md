# Strang splitting / Strang分割

Status: educational-example

Second-order integration using a symmetric half/full/half composition. Compare Lie–Trotter, subsolver order, boundaries and stability, with links to existing reaction–diffusion runs. Dedicated code, fixed inputs and rerun evidence compare the same 32-point Schnakenberg problem. Additional fixed examples: Strang splitting: Dirichlet boundary order reduction and correction. See each release for assumptions and checked scope. Additional fixed examples: Coupled frequencies and finite-window resonance. See each release for assumptions and checked scope.

半刻み・全刻み・半刻みの対称合成による2次の時間積分法。Lie–Trotterとの違い、部分ソルバーの次数、境界条件と安定性、既存の反応拡散の実行例を解説する。 同じ32格子のSchnakenberg問題を比較する専用コード・固定入力・追試記録があります。 追加固定例：Dirichlet境界でのStrang次数低下と補正。条件と検証範囲は各配布版で確認してください。 追加固定例：結合した2周波数系と共鳴の有限窓。条件と検証範囲は各配布版で確認してください。

This measures temporal error of the adopted compositions at fixed space, including splitting and midpoint-reaction discretization errors. It is not an exact continuum solution, spatial convergence check or independent PDE-engine comparison. Reactions do not conserve u+v; positivity is observed only for the fixed input. Work is reported as actual subflow calls, without runtime rankings or universal Strang superiority. This additional comparison of the existing Schnakenberg problem changes neither physical-problem counts, the common 22 examples, old release criteria nor success history. Long-time patterns, 2D and general boundaries are outside scope. The preceding limitations describe earlier editions. This additional release: This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately. The preceding limitations describe earlier editions. This additional release: The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

Other names: Strang splitting, Strang splitting method, Strang分割法, ストラング分割, ストラング分割法, symmetric Strang splitting, Strang–Marchuk splitting, 2次作用素分割

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/



- Reference: https://doi.org/10.1137/0705041 — Publisher bibliography checked for this addition. The original symmetric splitting reference is distinct from the Hairer lecture consulted for compositions and order. No fresh full-paper audit.
- Reference: https://www.unige.ch/~hairer/poly_geoint/week2.pdf — Author-hosted Lecture 2, section 5, printed pp.12–14, equations (23)–(27), and exact versus numerical subflows: Lie–Trotter, symmetric second-order composition and separable Hamiltonians. Selected passages, not a full-lecture audit.

## Small fixed-input validation supplements

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

- Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input: https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json

- Strang splitting: Dirichlet boundary order reduction and correction: https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json

- Coupled frequencies and finite-window resonance: https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json

- Schnakenberg:2D boundaries and initial modes: https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json

Common execution records: [{"id": "reaction-diffusion-splitting", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "strang-boundary-order-reduction", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "multifrequency-resonance", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "schnakenberg-2d-boundary-modes", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg, schnakenberg-2d-boundary-modes)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)
- [非同次境界を持つ線形反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja) (`inhomogeneous-reaction-diffusion`; strang-boundary-order-reduction)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; strang-boundary-order-reduction)
- [二周波数の結合調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja) (`coupled-harmonic-oscillators`; multifrequency-resonance)
- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`; multifrequency-resonance)

#### 問題の図 (`method-problems-ja`)

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) (`reaction-diffusion-splitting`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

##### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`)

![実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#code-ja)

- [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

##### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`)

![2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。 短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#code-ja)

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#references-ja) (`strang-boundary-order-reduction`)

- [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja) (`strang-boundary-order-reduction`; 同じ問題の参照; 半解析参照)

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

[既存の参照図](/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-measurements)

##### [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#references-ja) (`multifrequency-resonance`)

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja) (`multifrequency-resonance`; 同じ問題の参照; 半解析参照)

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-measurements)

##### [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#references-ja) (`schnakenberg-2d-boundary-modes`)

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja) (`schnakenberg-2d-boundary-modes`; 同じ問題の参照; 有限格子の数値参照)

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

[既存の参照図](/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/operator-splitting/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 同じ非線形反応拡散でLie–TrotterとStrangを比較する (`reaction-diffusion-splitting`)

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

##### Dirichlet境界でのStrang次数低下と補正 (`strang-boundary-order-reduction`)

[Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

##### 結合した2周波数系と共鳴の有限窓 (`multifrequency-resonance`)

[結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

##### Schnakenberg：2D境界と初期モード (`schnakenberg-2d-boundary-modes`)

[Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-22/splitting/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py)
- [/code/validated-examples/2026-11-22/splitting/splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py)
- [/code/validated-examples/2026-11-22/splitting/reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg, schnakenberg-2d-boundary-modes)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)
- [Linear reaction-diffusion with inhomogeneous boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en) (`inhomogeneous-reaction-diffusion`; strang-boundary-order-reduction)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; strang-boundary-order-reduction)
- [Coupled two-frequency harmonic oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coupled-harmonic-oscillators-en) (`coupled-harmonic-oscillators`; multifrequency-resonance)
- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`; multifrequency-resonance)

#### Problem figures (`method-problems-en`)

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) (`reaction-diffusion-splitting`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

##### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`)

![Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#code-en)

- [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) (`multifrequency-resonance`)

![Saved q1–q2 coordinates of the finest impulse trajectory, colored by physical time. This is one coupled trajectory, not a scanned phase diagram. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

Full-potential Verlet and a Strang impulse composition: half B kick, exact A flow, half B kick. A contains the fast oscillator and slow free drift; B contains the slow potential and the coupling.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#code-en)

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) (`multifrequency-resonance`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

##### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`)

![Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references. This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

Strang-split cell-averageCN diffusion and local implicit-midpoint reactions. Independent orthonormal sine/cosine Galerkin references retain four K12/18,Q96/192,tolerance rows for every initial condition. The original Dirichlet K12/18 reference failed its first relative qualification. Preserve that failure and add four D-only K24/32,Q128/192 reference actions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#code-en)

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en) (`schnakenberg-2d-boundary-modes`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.


#### Exact / reference solutions (`method-references-en`)

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#references-en) (`strang-boundary-order-reduction`)

- [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en) (`strang-boundary-order-reduction`; Same-problem reference; Semi-analytic reference)

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

[Existing reference profile](/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-measurements)

##### [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en#references-en) (`multifrequency-resonance`)

- [Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-multifrequency-resonance-en) (`multifrequency-resonance`; Same-problem reference; Semi-analytic reference)

The central actual floating map remains unresolved; ideal-pi Jordan structure is not transferred to it. Results concern 64-step amplification and small fixed inputs, not a scanned resonance diagram, general stability or a universal long-time error theorem.

[Existing reference profile](/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en#multifrequency-resonance-en-measurements)

##### [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en#references-en) (`schnakenberg-2d-boundary-modes`)

- [Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-schnakenberg-2d-boundary-modes-en) (`schnakenberg-2d-boundary-modes`; Same-problem reference; Finite-grid numerical reference)

This short small-amplitude study does not establish general pattern selection, mature patterns or reproduction of original figures. Finite reference differences are not rigorous continuum error bounds.

[Existing reference profile](/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en#schnakenberg-2d-boundary-modes-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/operator-splitting/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input (`reaction-diffusion-splitting`)

[Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

##### Strang splitting: Dirichlet boundary order reduction and correction (`strang-boundary-order-reduction`)

[Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

##### Coupled frequencies and finite-window resonance (`multifrequency-resonance`)

[Coupled frequencies and finite-window resonance](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json)

A genuinely coupled two-degree-of-freedom system uses twelve 64-step probes and six accuracy trajectories to separate normal modes, coordinate exchange, discrete maps and roundoff.

##### Schnakenberg:2D boundaries and initial modes (`schnakenberg-2d-boundary-modes`)

[Schnakenberg:2D boundaries and initial modes](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Compare two Neumann perturbations and a Dirichlet perturbation against nonlinear Galerkin references.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

###### Related source

- [/code/validated-examples/2026-11-22/splitting/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py)
- [/code/validated-examples/2026-11-22/splitting/splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py)
- [/code/validated-examples/2026-11-22/splitting/reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/tableau.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/boundary_reference.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/coefficient_exact.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/references/reference_models.py)
- [/code/validated-examples/2026-11-24/geometric-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/run.py)
- [/code/validated-examples/2026-11-24/geometric-controls/physics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/physics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/diagnostics.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/analytic.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/discrete.py)
- [/code/validated-examples/2026-11-24/geometric-controls/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/io_utils.py)
- [/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/references/qualify.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)

###### Package tests

- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
- [/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/test_geometry.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
