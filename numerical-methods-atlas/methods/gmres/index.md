# Restarted GMRES / 再始動GMRES

Status: educational-example

Read about Restarted GMRES, follow the original references and inspect related educational code and checks. Additional fixed examples: Symmetric saddle systems and Schur preconditioning. See each release for assumptions and checked scope. Additional fixed examples: Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products. See each release for assumptions and checked scope. Additional fixed examples: Bratu sensitivity near the discrete fold, Matrix-free VJP for distributed Bratu coefficients. See each release for assumptions and checked scope.

「再始動GMRES」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：対称不定値鞍点系とSchur前処理。条件と検証範囲は各配布版で確認してください。 追加固定例：解析・中央差分・方向ADによるJacobian不要Newton–Krylov。条件と検証範囲は各配布版で確認してください。 追加固定例：離散fold近傍のBratu感度、分布係数Bratuの行列非形成VJP。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner. Additional fixed examples: An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee. The preceding limitations describe earlier editions. This additional release: The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

Other names: GMRES法, 一般化最小残差法, generalized minimal residual, restarted GMRES

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py

- Reference: https://doi.org/10.1137/0907058 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1137/0913035 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional fixed examples: Symmetric saddle systems and Schur preconditioning. See each release for assumptions and checked scope. A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

追加固定例：対称不定値鞍点系とSchur前処理。条件と検証範囲は各配布版で確認してください。 理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

- Symmetric saddle systems and Schur preconditioning: https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/result.json

- Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json

- Bratu sensitivity near the discrete fold: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/
- Matrix-free VJP for distributed Bratu coefficients: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json

Common execution records: [{"id": "symmetric-saddle-minres", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-matrix-free-jfnk", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-fold-sensitivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-distributed-vjp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; sparse-advection-diffusion)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; sparse-advection-diffusion)
- [有限次元線形方程式と行列分解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja) (`finite-dimensional-linear-system`; symmetric-saddle-minres)
- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu-matrix-free-jfnk, bratu-fold-sensitivity, bratu-distributed-vjp)

#### 問題の図 (`method-problems-ja`)

##### [非対称移流拡散離散系の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja) (`sparse-advection-diffusion`)

![保存済み非対称離散系の真の残差履歴。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`)

![速度サイズ24の固定例で使う、保存した35×35鞍点行列。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#code-ja)

- [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) (`symmetric-saddle-minres`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

- [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

- [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。


#### 厳密解・参照解 (`method-references-ja`)

##### [非対称移流拡散離散系の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#references-ja) (`sparse-advection-diffusion`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#references-ja) (`symmetric-saddle-minres`)

- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja) (`symmetric-saddle-minres`; 同じ問題の参照; 有限格子の数値参照)

理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。

[既存の参照図](/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-measurements)

##### [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja) (`bratu-matrix-free-jfnk`)

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja) (`bratu-matrix-free-jfnk`; 同じ問題の参照; 解析参照)

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-measurements)

##### [離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja) (`bratu-fold-sensitivity`)

- [離散fold近傍のBratu shooting・接線・随伴参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja) (`bratu-fold-sensitivity`; 同じ問題の参照; 有限格子の数値参照)

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-measurements)

##### [分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja) (`bratu-distributed-vjp`)

- [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja) (`bratu-distributed-vjp`; 同じ問題の参照; 有限格子の数値参照)

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

[既存の参照図](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 対称不定値鞍点系とSchur前処理 (`symmetric-saddle-minres`)

[対称不定値鞍点系とSchur前処理](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。

##### 解析・中央差分・方向ADによるJacobian不要Newton–Krylov (`bratu-matrix-free-jfnk`)

[解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

##### 離散fold近傍のBratu感度 (`bratu-fold-sensitivity`)

[離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

##### 分布係数Bratuの行列非形成VJP (`bratu-distributed-vjp`)

[分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/krylov.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_sparse_fem.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; sparse-advection-diffusion)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; sparse-advection-diffusion)
- [Finite-dimensional linear systems and factorizations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-linear-system-en) (`finite-dimensional-linear-system`; symmetric-saddle-minres)
- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu-matrix-free-jfnk, bratu-fold-sensitivity, bratu-distributed-vjp)

#### Problem figures (`method-problems-en`)

##### [Nonsymmetric advection-diffusion discrete manufactured system](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en) (`sparse-advection-diffusion`)

![Stored true-residual histories of the nonsymmetric discrete system.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`)

![The saved 35 x 35 saddle matrix for velocity size 24.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png)

Stored-basis Lanczos least squares provides the educational MINRES variant; GMRES uses two-pass modified Gram-Schmidt. An SPD congruence preserves symmetry. The internal target is min(configured rtol, fixed forward-error limit / kappa_infinity), using only the matrix. The independent solution is not a stopping input.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#code-en)

- [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) (`symmetric-saddle-minres`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`)

![Preview of stored N=127 Newton residuals,upper-branch field/reference,Jv errors and actual evaluation counts. Run indices match the saved CSV.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

Use analytic Jv, a two-residual central difference, or one-direction forward AD. Apply a Poisson Thomas right preconditioner with two-pass reorthogonalized GMRES/Givens. Start eta=.3, then clamp .9*(Fk/Fk-1)^1.5 to [.001,.5]. This is an explicit EW Choice2-style variant, not the paper’s full safeguards or PETSc defaults.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#code-en)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) (`bratu-matrix-free-jfnk`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`)

![Bratu sensitivity near the discrete fold. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

Analytic Jv, Poisson-Thomas right preconditioning and the preserved GMRES body solve tangents/adjoints. Save every rtol, returned candidate, true residual, termination and roundoff scale. Qualify the discrete oracle through shooting and separate high-precision Thomas-Newton. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#code-en)

- [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) (`bratu-fold-sensitivity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`)

![Matrix-free VJP for distributed Bratu coefficients. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

Bv uses local gather and B transpose scatter-add. Primary solves use Jv without an n-by-m matrix. One shared Poisson factor serves the one/three-objective runs on the same state. Dense hats and m tangent RHS are allowed only in the separate reference window. R2 uses a general near-neighbor-difference association in binary64 Jv; the original nonlinear residual,GMRES and tolerances are unchanged. R3 expands only stateNewtoncorrections ashi+lo,direct9productresidual and3productstateupdate. Physicalstates stayfloat64;derivative/adjointGMRES staysordinary.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#code-en)

- [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) (`bratu-distributed-vjp`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.


#### Exact / reference solutions (`method-references-en`)

##### [Nonsymmetric advection-diffusion discrete manufactured system](https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=en#references-en) (`sparse-advection-diffusion`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en#references-en) (`symmetric-saddle-minres`)

- [Symmetric saddles: independent dense solutions and the ideal-Schur spectrum](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-symmetric-saddle-minres-en) (`symmetric-saddle-minres`; Same-problem reference; Finite-grid numerical reference)

A dense, ideal-Schur educational control, not a complete Stokes PDE solver or a scalable approximate preconditioner.

[Existing reference profile](/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en#symmetric-saddle-minres-en-measurements)

##### [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en#references-en) (`bratu-matrix-free-jfnk`)

- [Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-matrix-free-jfnk-en) (`bratu-matrix-free-jfnk`; Same-problem reference; Analytic reference)

An educational small1D BVP. AD covers only elementary arithmetic, exp and linear boundary padding. Small Hessenberg matrices and Krylov bases are stored. The fixed eta floor precludes claiming the unmodified EW asymptotic theorem. No general-AD/PETSc equivalence, speedup or global-convergence guarantee.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en#bratu-matrix-free-jfnk-en-measurements)

##### [Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en#references-en) (`bratu-fold-sensitivity`)

- [Discrete Bratu shooting, tangent and adjoint references near a fold](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-fold-sensitivity-en) (`bratu-fold-sensitivity`; Same-problem reference; Finite-grid numerical reference)

The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en#bratu-fold-sensitivity-en-measurements)

##### [Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en#references-en) (`bratu-distributed-vjp`)

- [Independent dense sensitivities and matrix-free VJPs for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-distributed-vjp-en) (`bratu-distributed-vjp`; Same-problem reference; Finite-grid numerical reference)

Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en#bratu-distributed-vjp-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Symmetric saddle systems and Schur preconditioning (`symmetric-saddle-minres`)

[Symmetric saddle systems and Schur preconditioning](https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/atlas-linear-algebra-spectral-2026-11-24-r3.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/verification.json)

MINRES and GMRES use the same original-system residual criterion and are checked against the ideal Schur three-point spectrum.

##### Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products (`bratu-matrix-free-jfnk`)

[Jacobian-free Newton–Krylov with analytic, central-FD and directional-AD products](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json)

Solve both Bratu branches with three Jv choices without assembling the nonlinear Jacobian; retain forcing, actual residuals and evaluation counts.

##### Bratu sensitivity near the discrete fold (`bratu-fold-sensitivity`)

[Bratu sensitivity near the discrete fold](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

At six fixed points approaching the discrete Bratu fold, separate state error from linear-solve tolerance and compare against independent shooting gradients.

##### Matrix-free VJP for distributed Bratu coefficients (`bratu-distributed-vjp`)

[Matrix-free VJP for distributed Bratu coefficients](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

Represent8/16/32 spatial controls with two local hat weights per node; compare objective-wise adjoint VJPs with a separate full-sensitivity reference.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/krylov.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/krylov.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/run.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/fixtures.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/solvers.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/references/oracles.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/run.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/problem.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/continuation.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/matrix_free.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/dual.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/experiments.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/references/analytic_family.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py)
- [/code/validated-examples/2026-11-24/adjoint/operators.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py)
- [/code/validated-examples/2026-11-24/adjoint/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py)
- [/code/validated-examples/2026-11-24/adjoint/fold_study.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py)
- [/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py)
- [/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py)
- [/code/validated-examples/2026-11-24/adjoint/balanced_operator.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py)
- [/code/validated-examples/2026-11-24/adjoint/state_linear.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py)
- [/code/validated-examples/2026-11-24/adjoint/state_expansion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py)
- [/code/validated-examples/2026-11-24/adjoint/state_krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py)
- [/code/validated-examples/2026-11-24/adjoint/state_jacobian.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py)
- [/code/validated-examples/2026-11-24/adjoint/distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/time_adjoint.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py)
- [/code/validated-examples/2026-11-24/adjoint/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py)
- [/code/validated-examples/2026-11-24/adjoint/qualify_references.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/conftest.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_sparse_fem.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_algorithms.py)
- [/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/test_mass_action.py)
- [/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/test_bratu.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_sparse_fem.py
```
