# SWASHES地形上の静止湖・定常浅水流 / SWASHES lakes and steady shallow flow over topography

https://hrkoyama.github.io/numerical-methods-atlas/problems/swashes-topography/

## 日本語

[保存した有限体積配列から描いた地形・水面と定常誤差のプレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-shallow-water/#swashes-topography) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#swashes-topography)

### 方程式・問題の定義

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

#### [地形源項付き浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-bed-ja)

$$
\partial_t h+\partial_xq=0
$$

$$
\partial_tq+\partial_x\!\left(q^2/h+gh^2/2\right)=-gh\,\partial_x z,\qquad q=hu
$$

$$
u=0,\qquad h_i=\max(\eta_0-z_i,0)
$$

摩擦・降雨なしの1次元Saint–Venant系。連続の地形と、保存平均から表現した区分定数の床を区別し、静水再構成の釣合いを確認します。 真の乾燥状態h=q=0では運動量の移流流束q²/hを0と定義します。

#### SWASHES地形流：静水と非零流量の定常解

補助実行例 · 実行例の定義・検証式

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

### 厳密解・参照解

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

#### [静止湖：表現した床の上の湿潤・露出平衡](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

解析解 · 同じ問題の参照

q_i=0; h_i=max(eta0-z_i,0); z_i=cellmean(z); eta0=.5 or .1.

g9.81、[0,25]m、200セル。8<x<12の放物線床z=.2−.05(x−10)²をセルごとにGauss8で平均し、h_i=max(η₀−z_i,0)、q_i=0、η₀=.5/.1mを初期化します。静水再構成が保つのはこの表現した区分定数床の平衡であり、連続床上の水深平均をそのまま使う別問題ではありません。

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

#### [SWASHES定常流：非射流Bernoulli根](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja#swashes-topography-ja-measurements)

半解析解 · 同じ問題の参照

q=4.42; h+z+q²/(2gh²)=2+q²/(8g); h>(q²/g)^(1/3).

g9.81、[0,25]m、同じ放物線床、流量q4.42m²/s、下流h2m。h+z+q²/(2gh²)=2+q²/(8g)の非射流根を別の二分法で求め、セル平均求積を比較します。100/200/400セルのPDE計算は定常参照から初期化してt2まで進め、SWASHESの静止状態からの過渡計算そのものは再現しません。

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

#### SWASHES地形流：静水と非零流量の定常解

31単体検査と8固定計算を事前固定。静水の水深・流量の最大変化、全FE段の非負水深、共有流束と地形運動量の収支、定常流3格子の保存量セル平均L1誤差・細分化比を保存します。独立したBernoulli二分法のエネルギー一定・亜臨界枝を照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja)

### 計算法

非負な静水圧再構成、共有HLL流束と左右の圧力補正で地形源項を離散化します。前進Euler、面Courant数.4。静水は反射壁。亜臨界流は上流で流量・下流で水深のみを指定し他変数を外挿します。floor・clip・retryはありません。 HLL更新を非負の水量packetに代数的に分解し、丸め後の同じ水量から移流運動量を作ります。微小水深閾値や事後修復は使いません。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [SWASHES地形流：静水と非零流量の定常解](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=ja)

補助実行例

水没・露出した隆起上の静水と、非零流量の亜臨界定常解を別々に検査します。静水の保存と、動く定常流に残る離散化誤差を区別します。

1次元、g=9.81、長さ25m、8<x<12でz=.2−.05(x−10)²m。水位.5/.1mの静水は200セル、流量4.42m²/s・下流深さ2mの定常流は100/200/400セル、t=2s。地形は区分定数セル平均。定常流から開始し、静水からの定常化実験とは区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

静水の厳密釣合いは表現したセル地形に対する性質です。非零流量の定常解は厳密には保存されず、有限時刻の誤差を測ります。遷移流・跳水・摩擦・降雨・浸透・2次元流や完全離散エントロピー安定性は検証しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)

## English

[Preview of represented bed, saved FV surfaces and moving-steady errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/swashes-topography-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-shallow-water/#swashes-topography) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#swashes-topography-en)

### Equations and problem definitions

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

#### [Shallow-water equations with bed source](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-bed-en)

$$
\partial_t h+\partial_xq=0
$$

$$
\partial_tq+\partial_x\!\left(q^2/h+gh^2/2\right)=-gh\,\partial_x z,\qquad q=hu
$$

$$
u=0,\qquad h_i=\max(\eta_0-z_i,0)
$$

One-dimensional frictionless Saint–Venant flow without rainfall. Distinguish the continuous topography from represented piecewise-constant bed means when checking hydrostatic balance. At a genuinely dry state h=q=0, define the advective momentum flux q²/h as0.

#### SWASHES topographic flow: lakes and nonzero steady discharge

Supplementary execution example · Example definition or validation formula

$$
\partial_t h+\partial_x q=0,\qquad \partial_tq+\partial_x(q^2/h+gh^2/2)=-gh\partial_xz
$$

$$
z^*=\max(z_L,z_R),\quad h_K^*=\max(0,h_K+z_K-z^*),\quad q_K^*=h_K^*u_K
$$

$$
F_K=F_{\mathrm{HLL}}(U_L^*,U_R^*)+(0,\tfrac12g(h_K^2-(h_K^*)^2))^T
$$

$$
q=4.42,\quad h+z+q^2/(2gh^2)=2+4.42^2/(8g),\quad h>(q^2/g)^{1/3}
$$

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

### Exact and reference solutions

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

#### [Lake at rest: wet and emerged equilibrium over represented bed](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

Analytic reference · Reference for the same problem

q_i=0; h_i=max(eta0-z_i,0); z_i=cellmean(z); eta0=.5 or .1.

Use g9.81,[0,25]m and200cells. Represent z=.2−.05(x−10)² on8<x<12 by split Gauss8 cell means, initializing h_i=max(eta0−z_i,0),q_i0 with eta0=.5/.1m. Hydrostatic reconstruction preserves equilibrium over this represented piecewise-constant bed; this differs from directly averaging depth over the continuous bed.

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

#### [SWASHES steady flow: subcritical Bernoulli root](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en#swashes-topography-en-measurements)

Semi-analytic reference · Reference for the same problem

q=4.42; h+z+q²/(2gh²)=2+q²/(8g); h>(q²/g)^(1/3).

Use g9.81,[0,25]m, the parabolic bed, discharge q4.42m²/s and downstream depth2m. Independently bisect the subcritical root of h+z+q²/(2gh²)=2+q²/(8g) and qualify cell quadrature. PDE runs on100/200/400cells start from the steady reference and advance to t2; they do not reproduce the original rest-to-steady transient.

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

#### SWASHES topographic flow: lakes and nonzero steady discharge

Freeze31 unit checks and eight group runs. Record lake drift, every FE minimum depth, shared-flux/bed-impulse budgets, conservative-mean L1 errors and three-grid ratios. Qualify an independent Bernoulli bisection by energy and branch checks.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en)

### Numerical methods

Hydrostatic reconstruction, shared HLL flux and left/right pressure corrections discretize the bed source; forward Euler and face CFL .4. Lakes use reflecting walls. Moving subcritical boundaries impose upstream q and downstream h, extrapolating the other datum. No state floors, clipping or retries. Algebraically factor HLL updates into nonnegative water packets; advected momentum uses those same rounded masses, without a small-depth threshold or subsequent repair.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [SWASHES topographic flow: lakes and nonzero steady discharge](https://hrkoyama.github.io/numerical-methods-atlas/validation/swashes-topography/?lang=en)

Supplementary execution example

Check two lake equilibria separately from nonzero subcritical flow, distinguishing lake preservation from moving-flow discretization error.

1D, g=9.81, L=25m, compact parabolic bed z=.2-.05(x-10)^2 on8<x<12. Lakes at surface .5/.1m use200 cells. Moving flow q=4.42m2/s, downstream h=2m uses100/200/400 cells to2s. Initialize the steady branch, not the published rest-to-steady transient.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/atlas-shallow-water-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Exact lake balance concerns the represented cell bed. Moving steady states retain finite-time numerical error. Transcritical flows, jumps, friction, rain, infiltration, 2D flow and fully discrete entropy stability are outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/shallow-water/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/run.py)
- [/code/validated-examples/2026-11-23/shallow-water/shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/shallow_water.py)
- [/code/validated-examples/2026-11-23/shallow-water/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/references/analytic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_packet_arithmetic.py)
- [/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/shallow-water/test_shallow_water.py)
