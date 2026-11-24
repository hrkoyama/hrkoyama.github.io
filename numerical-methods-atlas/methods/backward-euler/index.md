# Backward Euler / 後退Euler法

Status: educational-example

Read about Backward Euler, follow the original references and inspect related educational code and checks. Additional fixed examples: Su–Olson1996 non-equilibrium diffusion. See each release for assumptions and checked scope. Additional fixed examples: Discrete diffusion adjoint and checkpoint replay. See each release for assumptions and checked scope.

「後退Euler法」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：Su–Olson1996非平衡拡散。条件と検証範囲は各配布版で確認してください。 追加固定例：時間離散拡散の随伴とcheckpoint。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units. The preceding limitations describe earlier editions. This additional release: Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

Other names: 後退オイラー法, 陰的Euler法, 陰的オイラー法, implicit Euler, backward Euler method

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional fixed examples: Su–Olson1996 non-equilibrium diffusion. See each release for assumptions and checked scope. This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

追加固定例：Su–Olson1996非平衡拡散。条件と検証範囲は各配布版で確認してください。 1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

- Su–Olson1996 non-equilibrium diffusion: https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json

- Discrete diffusion adjoint and checkpoint replay: https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json

Common execution records: [{"id": "su-olson-diffusion1996", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "diffusion-discrete-adjoint", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; heat-dirichlet, diffusion-discrete-adjoint)
- [Su–Olson1996の非平衡拡散・物質交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja) (`non-equilibrium-diffusion-exchange`; su-olson-diffusion1996)

#### 問題の図 (`method-problems-ja`)

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja) (`heat-dirichlet`)

![共有図の左パネル：Dirichlet境界の熱拡散。右パネルは別のPoisson境界問題。](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja) (`nonlinear-rational-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

公開検査に後退Euler・BDF2・SDIRK2・IMEX Eulerがあり、保存プレビューはSDIRK2です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`)

![保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

保存的FVと後退Euler。放射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#code-ja)

- [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) (`su-olson-diffusion1996`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

実際の放射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

##### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`)

![時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#code-ja)

- [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Dirichlet境界の熱拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja) (`heat-dirichlet`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [有理関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=ja#references-ja) (`nonlinear-rational-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja#references-ja) (`su-olson-diffusion1996`)

- [Su–Olson1996拡散：固定版の独立積分評価関数](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-su-olson-diffusion1996-ja) (`su-olson-diffusion1996`; 同じ問題の参照; 半解析参照)

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

[既存の参照図](/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-measurements)

##### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#references-ja) (`diffusion-discrete-adjoint`)

- [後退Euler離散モードと時間厳密半離散拡散の参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja) (`diffusion-discrete-adjoint`; 同じ問題の参照; 解析参照)

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

[既存の参照図](/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Su–Olson1996非平衡拡散 (`su-olson-diffusion1996`)

[Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

実際の放射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

##### 時間離散拡散の随伴とcheckpoint (`diffusion-discrete-adjoint`)

[時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：Su–Olson1996非平衡拡散。条件と検証範囲は各配布版で確認してください。 1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; heat-dirichlet, diffusion-discrete-adjoint)
- [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en) (`non-equilibrium-diffusion-exchange`; su-olson-diffusion1996)

#### Problem figures (`method-problems-en`)

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en) (`heat-dirichlet`)

![Shared figure, left: Dirichlet heat decay. Right: separate Poisson boundary problems.](https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en) (`nonlinear-rational-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-ode.png)

Public checks include backward Euler, BDF2, SDIRK2 and IMEX Euler; the saved preview uses SDIRK2.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`)

![Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#code-en)

- [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) (`su-olson-diffusion1996`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

##### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`)

![Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#code-en)

- [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.


#### Exact / reference solutions (`method-references-en`)

##### [Heat decay with Dirichlet boundaries](https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=en#references-en) (`heat-dirichlet`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

This test has zero Dirichlet endpoints and sin(πx); the card has periodic boundaries, 1+0.25sin(2πx) and ν=0.02.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Nonlinear nonautonomous ODE with rational exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-ode/?lang=en#references-en) (`nonlinear-rational-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en#references-en) (`su-olson-diffusion1996`)

- [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-su-olson-diffusion1996-en) (`su-olson-diffusion1996`; Same-problem reference; Semi-analytic reference)

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

[Existing reference profile](/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-measurements)

##### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#references-en) (`diffusion-discrete-adjoint`)

- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en) (`diffusion-discrete-adjoint`; Same-problem reference; Analytic reference)

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

[Existing reference profile](/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Su–Olson1996 non-equilibrium diffusion (`su-olson-diffusion1996`)

[Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

##### Discrete diffusion adjoint and checkpoint replay (`diffusion-discrete-adjoint`)

[Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: Su–Olson1996 non-equilibrium diffusion. See each release for assumptions and checked scope. This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/transport.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/thick_limit.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/thick_reference.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/analytic.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/references/qualify_thick.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
