# Implicit differentiation and adjoint methods / 陰関数微分・随伴法

Status: educational-example

Compare implicit sensitivities and discrete adjoints on Bratu, then follow separate synthetic inverse editions for one and two fitted coefficients. Additional fixed examples: Discrete diffusion adjoint and checkpoint replay, Bratu sensitivity near the discrete fold, Matrix-free VJP for distributed Bratu coefficients. See each release for assumptions and checked scope.

Bratuのパラメータ感度で陰関数微分と離散随伴を照合し、別配布版で1個・2個の係数を推定する合成逆問題へ進む。 追加固定例：時間離散拡散の随伴とcheckpoint、離散fold近傍のBratu感度、分布係数Bratuの行列非形成VJP。条件と検証範囲は各配布版で確認してください。

The sensitivity edition verifies smooth lower-branch Bratu and a small nonsymmetric linear example with explicit adjoint pairing and objective quadrature. Separate inverse editions fit constant lambda and two spatial coefficients with regularization and identifiability checks. Time-dependent adjoints and shock sensitivities remain unimplemented. The preceding limitations describe earlier editions. This additional release: Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS. The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

Other names: 随伴法, 随伴解析, adjoint method, adjoint analysis, 陰関数微分, implicit differentiation, parameter sensitivity, パラメータ感度, Bratu, 随伴法・逆問題, Adjoint methods and inverse problems

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/



- Reference: https://doi.org/10.1007/bf01061285 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.1007/bf01931367 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://jaxopt.github.io/stable/implicit_diff.html — Official explanation of root-equation differentiation versus unrolling; the local NumPy supplement is an independent implementation.
- Reference: https://papers.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html — Selected implicit-root and JVP/VJP passages support the formulation; no reproduction of the full paper is claimed.

Bratu implicit sensitivity and discrete-adjoint supplement. Includes analytic continuous sensitivity, finite differences with fresh nonlinear solves, grid refinement and a nonsymmetric transpose test.

- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/operators.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/krylov.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/newton.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/time_adjoint.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/modal_decimal.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/shooting_decimal.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/references/linear_oracle.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/fold_study.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/balanced_operator.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_linear.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_expansion.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_krylov.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/state_jacobian.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/distributed.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/io_contract.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/qualify_references.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/conftest.py

- Tests: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py

Download: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/bratu-sensitivity-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/docs/figures/bratu-sensitivity.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_sensitivity.py
python scripts/build_bratu_sensitivity.py
```

## Small fixed-input validation supplements

Additional fixed examples: Discrete diffusion adjoint and checkpoint replay, Bratu sensitivity near the discrete fold, Matrix-free VJP for distributed Bratu coefficients. See each release for assumptions and checked scope. Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS. The continuum fold is not the discrete fold. rtol1e-4/1e-8 targets are required; requested1e-12 is observational and unmet is never called converged. Independent accuracy of the returned gradient is a separate gate. Eigenvalue/roundoff scales are floating diagnostics, not certified intervals. Bratu J is symmetric; the nonsymmetric transpose is a separate operator control. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved. Derivative verification at the same discrete state, not independent physical-PDE truth or general AD. Persistent arrays and fixed Krylov workspace inventories are not RSS measurements. For m=2, theta endpoints are[a-b-2,a+b-2], distinct from physical coefficient endpoints[a-b,a+b]. The retained /solver/gmres/retention_adaptation text is historicalR1/R2;the newcontract explicitly overrides it for mixed-precisionSTATEsolves. ProjectedUNMET is separatelysaved.

追加固定例：時間離散拡散の随伴とcheckpoint、離散fold近傍のBratu感度、分布係数Bratuの行列非形成VJP。条件と検証範囲は各配布版で確認してください。 固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。 連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。 同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

- Discrete diffusion adjoint and checkpoint replay: https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/
- Bratu sensitivity near the discrete fold: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/
- Matrix-free VJP for distributed Bratu coefficients: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json

Common execution records: [{"id": "diffusion-discrete-adjoint", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-fold-sensitivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-distributed-vjp", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Separate validation for time-dependent adjoints, high-dimensional inverse problems and nonsmooth models. Dedicated chapters and editions cover one- and two-coefficient synthetic inversions.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu, bratu-fold-sensitivity, bratu-distributed-vjp)
- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`; diffusion-discrete-adjoint)

#### 問題の図 (`method-problems-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`)

![時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#code-ja)

- [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

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

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#references-ja) (`diffusion-discrete-adjoint`)

- [後退Euler離散モードと時間厳密半離散拡散の参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja) (`diffusion-discrete-adjoint`; 同じ問題の参照; 解析参照)

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

[既存の参照図](/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-measurements)

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

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/adjoint/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/docs/figures/bratu-sensitivity.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### 時間離散拡散の随伴とcheckpoint (`diffusion-discrete-adjoint`)

[時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

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

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/bratu-sensitivity-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json)

###### 関連ソース

- [/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-sensitivity/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/autodiff.py)
- [/code/bratu-sensitivity/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/krylov.py)
- [/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py)
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

- [/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_bratu_sensitivity.py
python scripts/build_bratu_sensitivity.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu, bratu-fold-sensitivity, bratu-distributed-vjp)
- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`; diffusion-discrete-adjoint)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`)

![Discrete diffusion adjoint and checkpoint replay. Preview from actual saved numerical data for a one-dimensional problem.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

Thomas solves B u_next=u_current+dt theta b; reverse solves use B transpose. Save checkpoints every16steps and replay one block in the original order. Serialize and release the full trajectory before the separate checkpoint ownership window.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#code-en)

- [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en) (`diffusion-discrete-adjoint`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

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

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en#references-en) (`diffusion-discrete-adjoint`)

- [Backward-Euler discrete modes and time-exact semidiscrete diffusion references](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-diffusion-discrete-adjoint-en) (`diffusion-discrete-adjoint`; Same-problem reference; Analytic reference)

Fixed-step discrete adjoints, not CVODES or an optimal checkpoint schedule. The40n limit counts unique evolving state/adjoint/RHS/solve-scratch elements. Static factors/model arrays are separately listed and included in total bytes. Validation/NPZ assembly follows the ownership windows; this is not RSS.

[Existing reference profile](/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en#diffusion-discrete-adjoint-en-measurements)

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

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/adjoint/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/docs/figures/bratu-sensitivity.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Discrete diffusion adjoint and checkpoint replay (`diffusion-discrete-adjoint`)

[Discrete diffusion adjoint and checkpoint replay](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json)

Reverse the actual backward-Euler map and compare tangent derivatives, independent high-precision modes and block replay.

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

[Related code edition / ZIP](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/bratu-sensitivity-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/verification.json)

###### Related source

- [/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-sensitivity/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/autodiff.py)
- [/code/bratu-sensitivity/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/numart/krylov.py)
- [/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/scripts/build_bratu_sensitivity.py)
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

- [/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-sensitivity/2026-11-22/tests/test_bratu_sensitivity.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_distributed.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_fold.py)
- [/code/validated-examples/2026-11-24/adjoint/tests/test_time.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/tests/test_time.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_bratu_sensitivity.py
python scripts/build_bratu_sensitivity.py
```
