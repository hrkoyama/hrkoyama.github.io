# van der Polの短時間剛性遷移 / Van der Pol: an early stiffness transition

https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/

## 日本語

[保存済みの固定刻み比較と局所/大域誤差の区別。初回208/209で、μ=1適応法の大域目標2e-5は未達のまま保持します。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-ode-adaptivity/#van-der-pol-stiff-transition) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#van-der-pol-stiff-transition)

### 方程式・問題の定義

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

#### [van der Pol振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja)

$$
\dot x=v,\qquad\dot v=\mu(1-x^2)v-x
$$

固定したμと短い時区間で硬さによる仕事量と誤差を比較します。完全な緩和振動周期の検証ではありません。

#### van der Polの短時間剛性遷移

補助実行例 · 実行例の定義・検証式

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

### 厳密解・参照解

資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。

#### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

#### van der Polの短時間剛性遷移

資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja)

### 計算法

BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [L安定なSDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [適応SDIRK2／ステップ倍分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [van der Polの短時間剛性遷移](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja)

補助実行例

局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。

x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)

## English

[Saved fixed-step comparisons and the local/global error distinction. The first study met 208/209 targets; the unmet mu = 1 adaptive global goal of 2e-5 remains recorded. Axes for trajectories, states, time or iterations do not represent physical spatial dimensions.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-ode-adaptivity/#van-der-pol-stiff-transition) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#van-der-pol-stiff-transition-en)

### Equations and problem definitions

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

#### [Van der Pol oscillator](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#van-der-pol-en)

$$
\dot x=v,\qquad\dot v=\mu(1-x^2)v-x
$$

Compare work and error for fixed mu values over a short interval; this does not validate a full relaxation cycle.

#### Van der Pol: an early stiffness transition

Supplementary execution example · Example definition or validation formula

$$
\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}
$$

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

### Exact and reference solutions

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

#### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en#van-der-pol-stiff-transition-en-measurements)

Finite-grid numerical reference · Reference for the same problem

\dot x=v,\qquad \dot v=\mu(1-x^2)v-x,\quad\mu\in\{1,100\}

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

#### Van der Pol: an early stiffness transition

Compare 21 sampled times with qualified Radau and BDF references. Preserve every original decision, including false values. Require the other 208 conditions separately from three checks of faithful disclosure, actual local controls and retained original failure evidence.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en)

### Numerical methods

Use actual BDF2, SDIRK2 and adaptive step doubling, analytic Jacobians, factor reuse within each implicit stage, and retained candidates on failure.

- [BDF2](https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [L-stable SDIRK2](https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Adaptive SDIRK2 / step doubling](https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Van der Pol: an early stiffness transition](https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=en)

Supplementary execution example

Separate local control from global error. The first study met 208 of 209 original targets; the mu = 1 tight adaptive run missed the 2e-5 global goal.

The system is xprime = v and vprime = mu(1 - x squared)v - x, initially (2, 0), over T = 2. Two fixed methods, three step counts and two mu values plus four adaptive runs give 16 runs.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This post-measurement reporting revision is not a numerical repair. The first error, 4.535633779e-5, exceeded the original 2e-5 goal. Local tolerances do not guarantee global accuracy, and reporting PASS does not mean all original goals were met. Full large-mu cycles are outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/run.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/experiments.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/io_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reference_eval.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/models.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/stiff.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/reporting_policy.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_boundary.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_contract.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_dopri.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_reporting.py)
- [/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/test_stiff.py)
