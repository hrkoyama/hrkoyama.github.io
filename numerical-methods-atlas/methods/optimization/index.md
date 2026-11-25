# Gradient and quasi-Newton optimization / 勾配法・準Newton法

Status: educational-example

Fit Bratu coefficients from synthetic observations and verify two-parameter adjoint gradients, regularization bias, data-sensitivity singular values and nonidentifiable observations. Additional fixed examples: Bratu comparisons of GN, LM and bounded least squares, BFGS and three-pair L-BFGS at known minima, Noise, model discrepancy and finite gamma paths. See each release for assumptions and checked scope.

Bratuの合成観測から係数を推定し、2パラメータの随伴勾配、正則化の偏り、観測感度の特異値と識別不能例を検証する。 追加固定例：GN・LMと有界最小二乗のBratu比較、既知最小点でのBFGSと3組L-BFGS、雑音・モデル差と有限γ経路の正則化。条件と検証範囲は各配布版で確認してください。

Educational tests use small smooth lower-branch Bratu problems and fixed synthetic observations. They cover two spatial coefficients, Tikhonov regularization, local data-sensitivity SVD, rank loss with central observations and reflection ambiguity. Prior selection through regularization does not add observational information. Real data, high-dimensional function estimation, global uniqueness, statistical confidence intervals and quasi-Newton methods generally are outside scope. The preceding limitations describe earlier editions. This additional release: A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method. No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread. Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

Other names: 数値最適化, 勾配降下法, 準Newton法, 準ニュートン法, gradient descent, quasi Newton, Bratu, λ推定, パラメータ推定, 逆問題, inverse problem, parameter identification, projected gradient, Armijo, 複数パラメータ推定, 正則化, 識別可能性, Tikhonov regularization, identifiability, singular values, multi-parameter inverse problem

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/



- Reference: https://doi.org/10.1093/comjnl/13.3.317 — Method-specific source; see the detailed reading for source role and actual review depth.
- Reference: https://doi.org/10.2140/pjm.1966.16.1 — Original sufficient-decrease and backtracking construction; the detailed chapter distinguishes the local projected implementation from the original theorem.
- Reference: https://www.imm.dtu.dk/~pcha/Regutools/RTv4manual.pdf — Author official manual; the detailed chapter records the selected SVD and standard-form Tikhonov/nonzero-prior passages consulted. The local Bratu implementation is independent of the MATLAB toolbox.

## Small fixed-input validation supplements

Additional fixed examples: Bratu comparisons of GN, LM and bounded least squares, BFGS and three-pair L-BFGS at known minima, Noise, model discrepancy and finite gamma paths. See each release for assumptions and checked scope. A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method. No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread. Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

追加固定例：GN・LMと有界最小二乗のBratu比較、既知最小点でのBFGSと3組L-BFGS、雑音・モデル差と有限γ経路の正則化。条件と検証範囲は各配布版で確認してください。 小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。 厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。 楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

- Bratu comparisons of GN, LM and bounded least squares: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/
- BFGS and three-pair L-BFGS at known minima: https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/
- Noise, model discrepancy and finite gamma paths: https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json

Bratu inverse supplement: bounded projected adjoint-gradient fitting of one scalar parameter from fixed synthetic observations. Same-model consistency, continuous-observation grid bias and fixed-noise shifts are separate checks.

- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/scripts/build_bratu_inverse.py

- Tests: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/tests/test_bratu_inverse.py

Download: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/bratu-inverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-inverse/2026-11-22/docs/figures/bratu-inverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_inverse.py
python scripts/build_bratu_inverse.py
```

Multi-parameter Bratu inverse supplement: two spatial coefficients, adjoint fitting, Tikhonov regularization and data-only SVD identifiability diagnostics. Regularization does not add observational information.

- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py
- Code: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/model.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/regularization.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/public_contract.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/support.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/autodiff.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_inverse.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_multinverse.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_sensitivity.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/krylov.py
- Code: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/qualify.py

- Tests: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py
- Tests: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py

Download: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip
Manifest: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/source-manifest.json
Verification: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json
Measurements: https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json

Commands (from extracted supplement):

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```

Common execution records: [{"id": "bratu-gn-lm-bounds", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bfgs-lbfgs-controls", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "bratu-noise-regularization", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en"}, "kind": "dedicated-supplement"}]

Next: Separate validation for data-driven regularization selection, many coefficients, real data and more general optimization methods.

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`; bratu, bratu-gn-lm-bounds, bratu-noise-regularization)
- [有限次元代数最適化と既知最小点](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja) (`finite-dimensional-optimization`; bfgs-lbfgs-controls)

#### 問題の図 (`method-problems-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`)

![保存した2変数の反復点・残差評価点です。SciPy曲線は受理反復だけでなく残差評価を含み、これは2D物理空間の流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

独自SVD最小二乗GN/LM、元の投影勾配、SciPy TRF、非有界SciPy LM。lower/upperベクトルを元PGの係数別区間へ明示変換。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#code-ja)

- [GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja) (`bratu-gn-lm-bounds`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

##### [既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`)

![実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#code-ja)

- [既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

##### [雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`)

![保存した2変数推定値と固定γの局所1標準偏差楕円。楕円は選択事象で条件づけた区間でも、少数反復で保証した信頼領域でもありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

全γのfitを資格した完全経路だけから、実現雑音ノルムの1.05倍を満たす最大γを選択。不完全経路と完全だが候補なしを分離。4点L-curveは記述診断。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#code-ja)

- [雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja) (`bratu-noise-regularization`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。


#### 厳密解・参照解 (`method-references-ja`)

##### [1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja) (`bratu`)

- [1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-lower-branch-analytic-ja) (`bratu-lower-branch-analytic`; 同じ問題の参照; 解析参照)

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。

[既存の参照図](/numerical-methods-atlas/problems/bratu/?lang=ja)

##### [GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja#references-ja) (`bratu-gn-lm-bounds`)

- [Bratu逆最小二乗の独立Thomas局所参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-gn-lm-bounds-ja) (`bratu-gn-lm-bounds`; 同じ問題の参照; 有限格子の数値参照)

小さい滑らかな分枝の局所比較。SciPy最適化ライブラリは参照側でも共有し、大域最小・一意性を証明しません。LMに箱制約があるとは説明しません。

[既存の参照図](/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja#bratu-gn-lm-bounds-ja-measurements)

##### [既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#references-ja) (`bfgs-lbfgs-controls`)

- [既知最小点と現在の有限記憶作用に対する解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja) (`bfgs-lbfgs-controls`; 同じ問題の参照; 解析参照)

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。

[既存の参照図](/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-measurements)

##### [雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja#references-ja) (`bratu-noise-regularization`)

- [有限γ経路と局所線形雑音伝播のBratu参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-noise-regularization-ja) (`bratu-noise-regularization`; 同じ問題の参照; 有限格子の数値参照)

楕円は選択γを固定した局所Gauss–Newton線形モデルのplug-inです。非線形残差の二階微分、γ選択のランダム性、選択事象で条件づけた共分散、事後分布、被覆率を扱いません。全γ連続経路・実測データも未検証。

[既存の参照図](/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja#bratu-noise-regularization-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/bratu-multi-inverse/)
- 保存結果: [この配布版の保存結果](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json)
- 検証記録: [配布版の検証記録](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### GN・LMと有界最小二乗のBratu比較 (`bratu-gn-lm-bounds`)

[GN・LMと有界最小二乗のBratu比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

同じ観測からの17固定fitで、変数尺度・重み・境界と物理座標の停止条件を分けます。

##### 既知最小点でのBFGSと3組L-BFGS (`bfgs-lbfgs-controls`)

[既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

##### 雑音・モデル差と有限γ経路の正則化 (`bratu-noise-regularization`)

[雑音・モデル差と有限γ経路の正則化](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

2独立ノイズベクトルを尺度・データ文脈で共有し、42固定fitから有限γ選択と固定γの局所共分散を分けます。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip)

[配布版の検証記録](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)

###### 関連ソース

- [/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-multinverse/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py)
- [/code/bratu-multinverse/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py)
- [/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/model.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/model.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/regularization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/regularization.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/public_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/public_contract.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/support.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/autodiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/autodiff.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_inverse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_inverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_sensitivity.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/krylov.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/qualify.py)

###### 配布版のテスト

- [/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`; bratu, bratu-gn-lm-bounds, bratu-noise-regularization)
- [Finite-dimensional algebraic optimization and known minima](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en) (`finite-dimensional-optimization`; bfgs-lbfgs-controls)

#### Problem figures (`method-problems-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

The common example solves the forward boundary-value problem with damped Newton. Related method pages lead to separate editions for automatic differentiation, sensitivities, adjoints and coefficient fitting. Sensitivity and inverse problems with one or two coefficients have separate inputs and acceptance checks; they are not added to the common forward execution entry.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`)

![Saved two-parameter iterates and residual evaluations. SciPy paths include residual evaluations, not only accepted iterates; these are parameter coordinates, not a two-dimensional physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-gn-lm-bounds-preview.png)

Original SVD least-squares GN/LM, the retained projected-gradient solver, SciPy TRF and explicitly unbounded SciPy LM. A canonical lower/upper box is explicitly adapted to the legacy per-parameter intervals.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#code-en)

- [Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en) (`bratu-gn-lm-bounds`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

##### [BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`)

![Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#code-en)

- [BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

##### [Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`)

![Saved two-parameter estimates and fixed-gamma local one-standard-deviation ellipses. These are neither selection-conditional intervals nor confidence regions with coverage established by this small ensemble.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bratu-noise-regularization-preview.png)

Select the largest admissible gamma using 1.05 times the realized noise norm only after the full gamma path qualifies. Incomplete paths and complete paths with no admissible gamma are distinct. Four-point L-curves are descriptive diagnostics.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#code-en)

- [Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en) (`bratu-noise-regularization`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.


#### Exact / reference solutions (`method-references-en`)

##### [One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#references-en) (`bratu`)

- [1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-lower-branch-analytic-en) (`bratu-lower-branch-analytic`; Same-problem reference; Analytic reference)

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.

[Existing reference profile](/numerical-methods-atlas/problems/bratu/?lang=en)

##### [Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en#references-en) (`bratu-gn-lm-bounds`)

- [Independent Thomas-based local references for Bratu inverse least squares](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-gn-lm-bounds-en) (`bratu-gn-lm-bounds`; Same-problem reference; Finite-grid numerical reference)

A local comparison on a small smooth branch. The optimizer library is shared by the reference and a companion; no global minimum or uniqueness proof is claimed. LM is not presented as a box-constrained method.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en#bratu-gn-lm-bounds-en-measurements)

##### [BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#references-en) (`bfgs-lbfgs-controls`)

- [Analytic known minima and the current limited-memory action](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en) (`bfgs-lbfgs-controls`; Same-problem reference; Analytic reference)

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.

[Existing reference profile](/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-measurements)

##### [Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en#references-en) (`bratu-noise-regularization`)

- [Bratu references for finite gamma paths and local linear noise propagation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-noise-regularization-en) (`bratu-noise-regularization`; Same-problem reference; Finite-grid numerical reference)

Ellipses are plug-in noise propagation for a local Gauss–Newton linear model with the selected gamma treated as fixed. They omit nonlinear residual Hessians and selection randomness and are not selection-conditional covariance, a posterior or a coverage guarantee. Continuous gamma paths and real data remain unverified.

[Existing reference profile](/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en#bratu-noise-regularization-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/bratu-multi-inverse/)
- Saved result: [Saved results from this edition](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/docs/figures/bratu-multinverse.json)
- Verification receipt: [Edition verification receipt](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Bratu comparisons of GN, LM and bounded least squares (`bratu-gn-lm-bounds`)

[Bratu comparisons of GN, LM and bounded least squares](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-gn-lm-bounds/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-gn-lm-bounds/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

Seventeen fixed fits separate parameter scaling, weights, bounds and physical-coordinate stopping conditions.

##### BFGS and three-pair L-BFGS at known minima (`bfgs-lbfgs-controls`)

[BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

##### Noise, model discrepancy and finite gamma paths (`bratu-noise-regularization`)

[Noise, model discrepancy and finite gamma paths](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-noise-regularization/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-noise-regularization/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json)

Two independent noise vectors are reused across scales and data contexts. Forty-two fixed fits separate finite-list gamma selection from fixed-gamma local covariance.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/bratu-multinverse-2026-11-22.zip)

[Edition verification receipt](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/verification.json)

###### Related source

- [/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_multinverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_inverse.py)
- [/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/bratu_sensitivity.py)
- [/code/bratu-multinverse/2026-11-22/numart/autodiff.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/autodiff.py)
- [/code/bratu-multinverse/2026-11-22/numart/krylov.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/numart/krylov.py)
- [/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/scripts/build_bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/run.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/least_squares.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/model.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/model.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/thomas.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/oracles.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/quasi_newton.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/regularization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/regularization.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/public_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/public_contract.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/support.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/support.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/autodiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/autodiff.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_inverse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_inverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_multinverse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_sensitivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/bratu_sensitivity.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/legacy/numart/krylov.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/references/qualify.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/references/qualify.py)

###### Package tests

- [/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py](https://hrkoyama.github.io/code/bratu-multinverse/2026-11-22/tests/test_bratu_multinverse.py)
- [/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/test_inverse_optimization.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_bratu_multinverse.py
python scripts/build_bratu_multinverse.py
```
