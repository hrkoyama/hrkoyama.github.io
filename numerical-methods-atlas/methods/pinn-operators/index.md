# PINNs and neural operators / PINN・ニューラル演算子

Status: educational-example

Map learned solutions/operators, error and generalization. Fixed educational executions: Poisson PINN: independent grid error, Tiny FNO on held-out heat problems.

学習した解・演算子の位置付けと誤差・汎化を整理する。 固定した教育用実行例：1D Poisson PINNと独立格子誤差、小型FNOの問題単位検証。

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible. This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

Other names: PINN, PINN法, physics informed neural network, 物理情報ニューラルネットワーク, neural operator, ニューラルオペレーター

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pinn-operators/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/pinn-operators/



- Reference: https://doi.org/10.1016/j.jcp.2018.10.045 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://openreview.net/forum?id=c8P9NQVtmnO — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://arxiv.org/pdf/1711.10561 — Extracted PDF text selected pp.4–6, §2 continuous-time residual, Eq(2)–(4), Burgers setup and loss/optimizer discussion; not all 22 pages and not visual PDF audit.
- Reference: https://arxiv.org/html/2010.08895v3 — Selected HTML §2 learning operators; §3 Eq(2); §4 Eq(4)–(5), FFT/truncation/reality; §5 setup and §5.1 Burgers. PDF header/edition only; not full paper or appendix audit.

## Small fixed-input validation supplements

Fixed educational executions: Poisson PINN: independent grid error, Tiny FNO on held-out heat problems.

固定した教育用実行例：1D Poisson PINNと独立格子誤差、小型FNOの問題単位検証。

- Poisson PINN: independent grid error: https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/
- Tiny FNO on held-out heat problems: https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json

Common execution records: [{"id": "pinn-poisson", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fno-periodic-heat", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Preserve the fixed scope and qualify extensions separately.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; heat-periodic)
- [Poisson・Laplace方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja) (`poisson-laplace`; poisson-1d-dirichlet)

#### 問題の図 (`method-problems-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) (`heat-periodic`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。 入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja)

- [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja) (`fno-periodic-heat`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

同じ重みで32/64点・未見関数・OODを分けて評価します。

##### [1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) (`poisson-1d-dirichlet`)

![保存済み1次元Dirichlet製造解の誤差と格子数。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja)

- [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja) (`pinn-poisson`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

3固定seedの49パラメータPINNを解析解・FDと比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja) (`heat-periodic`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

- [小型FNOの問題単位検証](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja) (`fno-periodic-heat`; 関連モデルの参照; 解析参照)

固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。

[既存の参照図](/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja#fno-periodic-heat-ja-measurements)

##### [1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#references-ja) (`poisson-1d-dirichlet`)

- [Poisson／正弦波の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja) (`poisson-manufactured`; 関連モデルの参照; 製造解)

単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poisson-manufactured)

- [1D Poisson PINNと独立格子誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja) (`pinn-poisson`; 関連モデルの参照; 製造解)

1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

[既存の参照図](/numerical-methods-atlas/validation/pinn-poisson/?lang=ja#pinn-poisson-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/pinn-operators/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 小型FNOの問題単位検証 (`fno-periodic-heat`)

[周期Fourierモードの熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

同じ重みで32/64点・未見関数・OODを分けて評価します。

##### 1D Poisson PINNと独立格子誤差 (`pinn-poisson`)

[1次元Poisson・Dirichlet製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

3固定seedの49パラメータPINNを解析解・FDと比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

固定した教育用実行例：1D Poisson PINNと独立格子誤差、小型FNOの問題単位検証。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

###### 関連ソース

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### 配布版のテスト

- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; heat-periodic)
- [Poisson / Laplace equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#poisson-laplace-en) (`poisson-laplace`; poisson-1d-dirichlet)

#### Problem figures (`method-problems-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) (`heat-periodic`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability. Lift (u₀,ν) to width two and apply two blocks containing a local linear map, real DC and complex Fourier modes 1–4, then tanh. Train with a fixed L-BFGS-B budget and evaluate the same weights at N=32 and 64. Nonlinear terms are evaluated on each native grid without dealiasing.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#code-en)

- [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en) (`fno-periodic-heat`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

##### [1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) (`poisson-1d-dirichlet`)

![Stored error versus resolution for the 1D Dirichlet manufactured solution.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Train a hard-boundary tanh ansatz with trust-region reflective least squares and an analytic parameter Jacobian. Retain every returned model under the fixed budget. Also solve second-order finite differences with 31, 63 and 127 unknowns using the Thomas algorithm.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#code-en)

- [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en) (`pinn-poisson`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en#references-en) (`heat-periodic`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

- [Tiny FNO on held-out heat problems](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fno-periodic-heat-en) (`fno-periodic-heat`; Related-model reference; Analytic reference)

This comparison concerns a fixed tiny discrete operator, without arbitrary-resolution, distributional or OOD guarantees. The N=64-to-32 discrepancy includes nonlinear aliasing and is not a continuum discretization error. Optimizer convergence is distinct from normal budget termination.

[Existing reference profile](/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en#fno-periodic-heat-en-measurements)

##### [1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en#references-en) (`poisson-1d-dirichlet`)

- [Poisson / manufactured sine](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poisson-manufactured-en) (`poisson-manufactured`; Related-model reference; Manufactured solution)

It matches the single-sine common fixed input, but saved comparisons also contain composite-sine manufactured forcing. Zero Dirichlet boundaries do not make all sources identical.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poisson-manufactured)

- [Poisson PINN: independent grid error](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-pinn-poisson-en) (`pinn-poisson`; Related-model reference; Manufactured solution)

This fixed-budget study covers one smooth Poisson problem and three seeds. A small training loss does not establish independent-point accuracy or general PINN training success. Unmet goals remain visible.

[Existing reference profile](/numerical-methods-atlas/validation/pinn-poisson/?lang=en#pinn-poisson-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/pinn-operators/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Tiny FNO on held-out heat problems (`fno-periodic-heat`)

[Periodic Fourier-mode heat decay](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

Evaluate the same learned weights on 32/64-point grids, held-out functions and separate OOD inputs.

##### Poisson PINN: independent grid error (`pinn-poisson`)

[1D Poisson / smooth Dirichlet manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

Compare a 49-parameter PINN for three fixed seeds with analytic and finite-difference solutions.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Fixed educational executions: Poisson PINN: independent grid error, Tiny FNO on held-out heat problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json)

###### Related source

- [/code/validated-examples/2026-11-25/small-models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/run.py)
- [/code/validated-examples/2026-11-25/small-models/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/experiments.py)
- [/code/validated-examples/2026-11-25/small-models/io_utils.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/io_utils.py)
- [/code/validated-examples/2026-11-25/small-models/pinn.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/pinn.py)
- [/code/validated-examples/2026-11-25/small-models/fno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/fno.py)
- [/code/validated-examples/2026-11-25/small-models/data_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/data_family.py)
- [/code/validated-examples/2026-11-25/small-models/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/biology.py)
- [/code/validated-examples/2026-11-25/small-models/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/oracles.py)
- [/code/validated-examples/2026-11-25/small-models/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/qualify.py)
- [/code/validated-examples/2026-11-25/small-models/references/reference_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/references/reference_models.py)

###### Package tests

- [/code/validated-examples/2026-11-25/small-models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q
python run.py --input inputs.json --output output
```
