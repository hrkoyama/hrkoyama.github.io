# Strang splitting / Strang分割

Status: educational-example

Second-order integration using a symmetric half/full/half composition. Compare Lie–Trotter, subsolver order, boundaries and stability, with links to existing reaction–diffusion runs. Dedicated code, fixed inputs and rerun evidence compare the same 32-point Schnakenberg problem.

半刻み・全刻み・半刻みの対称合成による2次の時間積分法。Lie–Trotterとの違い、部分ソルバーの次数、境界条件と安定性、既存の反応拡散の実行例を解説する。 同じ32格子のSchnakenberg問題を比較する専用コード・固定入力・追試記録があります。

This measures temporal error of the adopted compositions at fixed space, including splitting and midpoint-reaction discretization errors. It is not an exact continuum solution, spatial convergence check or independent PDE-engine comparison. Reactions do not conserve u+v; positivity is observed only for the fixed input. Work is reported as actual subflow calls, without runtime rankings or universal Strang superiority. This additional comparison of the existing Schnakenberg problem changes neither physical-problem counts, the common 22 examples, old release criteria nor success history. Long-time patterns, 2D and general boundaries are outside scope.

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

Common execution records: [{"id": "reaction-diffusion-splitting", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja) (`bio-turing`; turing-schnakenberg)

#### 問題の図 (`method-problems-ja`)

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

![a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

- [同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja) (`reaction-diffusion-splitting`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。


#### 厳密解・参照解 (`method-references-ja`)

##### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#references-ja) (`turing-schnakenberg`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

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

###### 配布版のテスト

- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en) (`bio-schnakenberg`; turing-schnakenberg)
- [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en) (`bio-turing`; turing-schnakenberg)

#### Problem figures (`method-problems-en`)

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en) (`turing-schnakenberg`)

![Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#code-en)

- [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en) (`reaction-diffusion-splitting`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip)

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.


#### Exact / reference solutions (`method-references-en`)

##### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=en#references-en) (`turing-schnakenberg`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

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

###### Package tests

- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
