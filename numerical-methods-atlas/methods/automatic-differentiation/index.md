# Automatic differentiation / 自動微分

Status: educational-example

A shared foundation for the chain rule, forward/reverse modes and JVPs, with analytic, finite-difference and forward-AD verification on the same Bratu equation. Additional fixed examples: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products. See each release for assumptions and checked scope.

共通基盤として連鎖律・前進／逆モード・JVPを学び、同じBratu方程式で解析微分・有限差分・前進モード自動微分を検証する。 追加固定例：解析・中央差分・方向ADによるJacobian不要Newton–Krylov。条件と検証範囲は各配布版で確認してください。

Limited to educational real forward mode and small dense-Newton Bratu comparisons. Reverse mode, HVPs and matrix-free Newton–Krylov remain explanatory only. A separate dedicated supplement verifies implicit sensitivities and discrete adjoints. Additional fixed examples: An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

Other names: AD, 自動微分法, automatic differentiation, アルゴリズム微分, Bratu, JVP, forward mode, 前進モード, 双対数

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/



- Reference: https://doi.org/10.1145/355586.364791 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/bf01931367 — Method-specific source; see the detailed reading for source role and actual review depth.

Forward-mode AD supplement: analytic/finite-difference/AD Bratu derivatives, Newton convergence and spatial refinement. Reverse-mode execution and implicit sensitivities are not implemented in this edition. The separate Bratu sensitivity edition is linked from /numerical-methods-atlas/en/read/adjoint/.

- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/autodiff/2026-11-22/scripts/build_autodiff.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py

- Tests: https://hrkoyama.github.io/code/autodiff/2026-11-22/tests/test_autodiff.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py

Download: https://hrkoyama.github.io/code/autodiff/2026-11-22/autodiff-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/autodiff/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/autodiff/2026-11-22/docs/figures/autodiff-bratu.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_autodiff.py
python scripts/build_autodiff.py
```

## Small fixed-input validation supplements

Additional fixed examples: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products. See each release for assumptions and checked scope. An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

追加固定例：解析・中央差分・方向ADによるJacobian不要Newton–Krylov。条件と検証範囲は各配布版で確認してください。 小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

- Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json

Common execution records: [{"id": "bratu-matrix-free-jfnk", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Separate executable checks for reverse mode and Hessian-vector products. Implicit differentiation and adjoints now have a separate Bratu sensitivity chapter.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu, bratu-matrix-free-jfnk)

#### 問題の図 (`method-problems-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) (`bratu-matrix-free-jfnk`)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja) (`bratu-matrix-free-jfnk`; 同じ問題の参照; 解析参照)

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/automatic-differentiation/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/autodiff/2026-11-22/docs/figures/autodiff-bratu.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov (`bratu-matrix-free-jfnk`)

[解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/autodiff/2026-11-22/autodiff-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json)

###### 関連ソース

- [/code/autodiff/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/autodiff.py)
- [/code/autodiff/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/krylov.py)
- [/code/autodiff/2026-11-22/scripts/build_autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/scripts/build_autodiff.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)

###### 配布版のテスト

- [/code/autodiff/2026-11-22/tests/test_autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/tests/test_autodiff.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_autodiff.py
python scripts/build_autodiff.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu, bratu-matrix-free-jfnk)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) (`bratu-matrix-free-jfnk`)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en) (`bratu-matrix-free-jfnk`; Same-problem reference; Analytic reference)

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/automatic-differentiation/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/autodiff/2026-11-22/docs/figures/autodiff-bratu.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products (`bratu-matrix-free-jfnk`)

[Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/autodiff/2026-11-22/autodiff-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/autodiff/2026-11-22/verification.json)

###### Related source

- [/code/autodiff/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/autodiff.py)
- [/code/autodiff/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/numart/krylov.py)
- [/code/autodiff/2026-11-22/scripts/build_autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/scripts/build_autodiff.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)

###### Package tests

- [/code/autodiff/2026-11-22/tests/test_autodiff.py](https://hrkoyama.github.io/code/autodiff/2026-11-22/tests/test_autodiff.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_autodiff.py
python scripts/build_autodiff.py
```
