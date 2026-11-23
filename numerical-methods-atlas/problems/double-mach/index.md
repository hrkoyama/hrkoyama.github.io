# 二重Mach反射 / Double Mach reflection

https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/

## 日本語

[実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-double-mach/#double-mach-reflection) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#double-mach)

### 方程式・問題の定義

同じMach10設定・γ=1.4の圧縮性Euler系を、長方形[0,4]×[0,1]の全域で更新します。

#### [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。

#### Double Mach反射：多格子の軽量検証

補助実行例 · 実行例の定義・検証式

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

### 厳密解・参照解

公開済みの低解像度HLL像を保持し、別の有限体積コードの保存参照との比較を追加します。参照も有限格子の数値解であり、全場の厳密解や誤差上界ではありません。

#### [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| (conservative restriction of saved finite-grid data).

領域[0,4]×[0,1]の2次元理想気体Euler、γ=1.4、Mach10・角度60度の入射衝撃波、初期の衝撃脚x=1/6、最終時刻T=.2。保存参照は別実装の非分割primitive MUSCL/HLL/Heun有限体積法（勾配制限はgeneralized minmodのθ=1.5、MC型であり標準MCのθ=2とは異なる）で、256×64と512×128セルです。主計算とHLLという流束族・Heun時間積分の数式を共有しますが、空間再構成と実装は別です。保存量を保つ制限で比較用セル平均を得ます。不変のRKDG2Dキットで以前に実行したソース・配列・記録を再利用し、今回の参照PDE・Athena・LAVAの新規実行ではありません。参照の格子差も有限分解能の感度指標で、厳密な誤差上界ではありません。厳密2D解でも細いwall jet・渦構造の収束検証でもありません。 入射不連続面の初期化はセル中心での状態判定であり、衝撃面で切られたセルの厳密平均からの初期化ではありません。

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

#### Double Mach反射：多格子の軽量検証

初回事前契約の20単体検査は合格。全3格子の実行前の読み取りレビューで、衝撃探索窓に前線が無い場合を拒否する診断ガードと1検査を追加し、旧契約・ソースを保持して改訂契約を固定しました。その21検査と全3計算・40判定が-W errorで合格しました。参照はRKDGキットで既に独立実行済みの、別実装primitive MUSCL/generalized-minmod θ=1.5/HLL/HeunのNy64/128データを再利用し、今回は参照PDEを再実行していません。Ny128保存量を保守的に制限して比較した密度L1は.08431/.05802/.03503、圧力L1は.09556/.06798/.04156。参照64/128増分は.00955/.01250で、最細主計算差の約.273/.301です。4保存量の境界収支の最大相対残差は約4.60e-13でした。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja)

### 計算法

既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。

- [Godunov型有限体積法](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Double Mach反射：多格子の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja)

補助実行例

既存のDouble Mach反射と同じ初期値・境界を使い、64×16・128×32・256×64の実2D Euler有限体積計算をT=.2まで実行します。別実装の有限格子参照との差、実際の境界流束収支、上部の入射衝撃位置と壁近傍を比較します。

無次元[0,4]×[0,1]、γ=1.4、Mach10。衝撃脚x=1/6、角度60度、後方状態(ρ,u,v,p)=(8,8.25√3/2,−4.125,116.5)、前方(1.4,0,0,1)。初期セルは衝撃のセル中心側で分類し、切断セルの厳密平均ではありません。左は後方流入、右はゼロ勾配、底はx<1/6で後方状態・他は滑り壁、上はx<1/6+(1+20t)/√3で後方状態を与えます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

参照は有限格子の数値解で、厳密2D解でも独立のAthena/LAVA実行でもありません。HLLという流束族は共有しますが、参照は主計算の空間演算をimportしない別実装です。参照増分は不確かさの診断で誤差の上界ではありません。差には初期射影、動く境界の格子標本化、離散化と有限参照の影響が入り、傾きは厳密な空間次数や反射パターン全体の収束証明ではありません。上部前線の2セル差は物理幅では細分化で縮小しますが、セル単位の誤差は下がりません。壁近傍は固定領域x∈[1,2.75],y≤.25の比較で、ジェットを追跡した評価ではありません。最細でも領域最大uは主計算12.644に対し参照16.125で、薄いwall jet・巻き上がりは未解像です。前向きステップ、他の壁条件・一般摂動、高次精度、完全なパターン収束は今回の検証外です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)

## English

[Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-double-mach/#double-mach-reflection) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#double-mach-en)

### Equations and problem definitions

Compressible Euler with the same Mach10 data and gamma1.4 is evolved over the full rectangle[0,4]×[0,1].

#### [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en)

$$
\partial_tU+\partial_xF(U)=0
$$

$$
U=(\rho,\rho u,E)^{\mathsf T}
$$

$$
F=(\rho u,\rho u^2+p,u(E+p))^{\mathsf T}
$$

The one-dimensional conservative form. Consult each test for its equation of state, initial data and boundaries.

#### Double Mach reflection: lightweight grid verification

Supplementary execution example · Example definition or validation formula

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
x_s(y,t)=\frac16+\frac{y+20t}{\sqrt3},\quad \gamma=1.4,\quad M_s=10
$$

$$
\Delta t=0.4\left[\max(|u|+c)/\Delta x+\max(|v|+c)/\Delta y\right]^{-1}
$$

$$
\sum_{ij}|C_{ij}|(\bar U_{ij}^{n+1}-\bar U_{ij}^{n})=\frac{\Delta t}{2}(B(U^n,t_n)+B(U^{(1)},t_n+\Delta t))
$$

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

### Exact and reference solutions

Preserve the previously published coarse HLL view and add comparison with a saved reference from a separate finite-volume implementation. The reference is itself a finite-grid numerical solution, not an exact full-field solution or error bound.

#### [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-measurements)

Finite-grid numerical reference · Reference for the same problem

partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| (conservative restriction of saved finite-grid data).

Two-dimensional ideal-gas Euler flow on [0,4] × [0,1], with gamma = 1.4, a Mach-10 incident shock at 60 degrees, initial shock foot x = 1/6 and final time T = 0.2. The saved reference uses a separately written, unsplit primitive MUSCL/HLL/Heun finite-volume code on 256 × 64 and 512 × 128 cells. Its generalized-minmod slope parameter is theta = 1.5 (MC-type, rather than canonical MC with theta = 2). The primary and reference codes share the HLL flux family and Heun time-integration equations, while their spatial reconstruction and implementations are separate. Conservative restriction produces comparison cell means. Previously executed source, data and receipts are reused from the immutable RKDG2D kit; no reference PDE, Athena or LAVA was executed anew for this addition. Reference grid differences indicate finite-resolution sensitivity, not rigorous error bounds. This is not an analytic 2D solution or a convergence test for the thin wall jet and vortex pattern. The incident discontinuity is classified at cell centers, rather than initialized from exact cut-cell averages.

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

#### Double Mach reflection: lightweight grid verification

The original preregistered20 unit tests passed. Before the full three-grid run, read-only review added an absent-front diagnostic guard and one test; the old contract/source are preserved and a revision contract was frozen. All21 tests, three final-time runs and40 gates passed with-W error. Previously independently executed Ny64/128 primitive MUSCL/generalized-minmod theta1.5/HLL/Heun data from the RKDG kit are reused; no reference PDE was rerun. Density L1 differences from conservatively restricted Ny128 are.08431/.05802/.03503 and pressure differences.09556/.06798/.04156. Reference64/128 increments are.00955/.01250, about.273/.301 of the finest primary differences. Maximum relative four-component boundary-budget residual is about4.60e-13.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en)

### Numerical methods

Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.

- [Godunov-type finite volumes](https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Double Mach reflection: lightweight grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/double-mach-reflection/?lang=en)

Supplementary execution example

Full 2D Euler finite volumes evolve the existing Double Mach initial/boundary data to T=.2 on64x16,128x32 and256x64 cells. Compare a separately written finite-grid reference, actual boundary-flux budgets, an upper incident-front position and a fixed near-wall region.

Nondimensional[0,4]x[0,1], gamma1.4, Mach10. Shock footx=1/6, angle60degrees; postshock(rho,u,v,p)=(8,8.25sqrt(3)/2,-4.125,116.5), upstream(1.4,0,0,1). Initial cells are classified by their centers, not exact cut-cell means. Left postshock inflow, right zero-gradient, bottom postshock forx<1/6 and slip wall otherwise; top postshock forx<1/6+(1+20t)/sqrt(3).

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/atlas-double-mach-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The reference is finite-grid numerical data, not an exact2D solution or an Athena/LAVA execution. The HLL family is shared, but reference spatial operators are separately written and not imported by the primary. The reference increment is an uncertainty diagnostic, not an error bound. Initial projection, sampled moving boundaries, discretization and finite-reference effects all enter the difference; the slope is no rigorous order or full reflection-pattern convergence proof. The upper-front discrepancy stays2cells while its physical width shrinks. Fixed near-wall ROIx in[1,2.75],y<=.25 is not feature tracking. Finest ROI maxu12.644 versus reference16.125 shows the thin wall jet/roll-up is unresolved. Forward step, other wall data, general perturbations, higher order and full-pattern convergence are unverified.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/double-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/run.py)
- [/code/validated-examples/2026-11-23/double-mach/dm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/dm_solver.py)
- [/code/validated-examples/2026-11-23/double-mach/test_dm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/test_dm.py)
