# Mach 3前向きステップ / Mach-3 forward-facing step

https://hrkoyama.github.io/numerical-methods-atlas/problems/forward-step/

## 日本語

[実際の2次元Euler計算の密度場。Mach 3、γ=1.4、T=4、240×80セル。固体段差を除いて描きます。角のエントロピー補正は使わず、微細なすべり線・渦の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-forward-step/#forward-step-m3) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#forward-step)

### 方程式・問題の定義

γ=1.4、ρ=1.4、u=3、v=0、p=1の流入を、[0,3]×[0,1]から高さ.2・開始位置x=.6の段差を除いた2次元Euler系でT=4まで更新します。

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

#### Mach 3前向きステップ：壁面収支と多格子検証

補助実行例 · 実行例の定義・検証式

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

### 厳密解・参照解

全場の厳密解はありません。新規の別実装C++有限体積参照とその2格子差を示し、主計算との共通の流束族・時間積分、角無補正条件、有限格子の限界を明記します。

#### [Mach 3前向きステップ：独立C++有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja#forward-step-m3-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| on fluid cells (conservative restriction of a finite-grid reference).

γ=1.4の2次元Euler流れ。[0,3]×[0,1]のうちx≥.6,y<.2は固体とし、初期・入口の(ρ,u,v,p)=(1.4,3,0,1)、上下と段差は滑り壁、右端はゼロ勾配、T=4です。参照は独立したC++17実装のprimitive MUSCL（一般化minmod θ1.5）/Davis HLL/HeunをCFL=.3、240×80・480×160で新規実行しました。境界に接する法線方向の傾きはゼロにし、再構築の傾き再調整はセル平均を変えません。Python主計算は区分定数HLL/Heunで、流束族・時間積分式は共有しますが実装と空間再構築は別です。角のエントロピー/エンタルピー補正、状態floor、刻み再試行はありません。角の数値エントロピー層が下流へ移流され得る無補正条件であり、補正付き原著PPM像の再現とは区別します。固体を除いた保存量を保守的に制限してから圧力を算出し、参照格子差・保存収支・局所診断を残します。有限格子の数値参照であり、厳密2次元解、誤差上界、細いすべり線や巻き上がりの収束証明ではありません。

新しく独立実行したC++17のMUSCL/HLL/Heun参照を保存量制限で比較します。同じHLL族・Heunと角無補正条件を共有する有限格子数値参照であり、全場の厳密解や誤差上界ではありません。

#### Mach 3前向きステップ：壁面収支と多格子検証

入力・受入基準・24単体検査・数値ソースを主計算の初回検査・PDE実行前に固定しました。解析的なMach3垂直衝撃波のRankine–Hugoniot関係、一様な平行流路、壁の質量・エネルギー流束ゼロ、段差の圧力力の向き、実際の4成分収支、不正段の保持を検査します。別実装のC++17 MUSCL/generalized-minmod θ1.5/HLL/HeunによるNy80/160の参照を新規に実行し、保存量を保守的に制限して密度・圧力の全流体領域L1を比較します。参照の再計算は通常の公開ZIP追試には含めず、保存データ・ソース・契約・実行記録を同梱します。 最初の参照Ny160は事前固定の120秒上限で停止した記録を保持し、診断文字列の不要なメモリ割当てだけを除く参照改訂を、主計算の初回実行前に再固定しました。入力・演算・CFL・判定値は変更していません。 24検査と全3計算・45判定が-W errorで合格。主計算の密度L1は.14754/.12878/.10265、圧力L1は.19373/.16015/.12242、密度の最後の2格子の傾きは.327。参照80/160増分は.02636/.03063で、最細主計算差の約.257/.250。全4成分の境界収支の最大相対残差は2.99e-13、全壁の積分質量・エネルギー流束は0でした。主計算3格子は元のMacで約46秒、性能改訂後の参照80/160は約8/65秒です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja)

### 計算法

従来のHLL・MUSCLと勾配制限の比較データを保持し、追加の軽量例は区分定数HLL＋Heunを使います。参照実装の手法は参照の出典と条件で区別します。

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [単調中心勾配制限／MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Mach 3前向きステップ：壁面収支と多格子検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=ja)

補助実行例

実際の2次元Euler有限体積計算を60×20・120×40・240×80でT=4まで行い、別実装のMUSCL有限格子参照と比較します。段差の垂直面・上面を含む実際の数値流束から4保存量の収支を評価し、角のエントロピー補正を加えない変種として図とコードを公開します。

無次元[0,3]×[0,1]からx≥.6・y<.2の固体を除き、γ=1.4、初期・左流入(ρ,u,v,p)=(1.4,3,0,1)。音速1なのでMach3です。右はゼロ勾配流出、上下と段差の両面は法線運動量を反転する滑り壁。格子Nyは5の倍数で両壁を厳密に整列し、固体記憶領域は流体ノルム・積分から除外します。Woodward–Colella型の角エントロピー・エンタルピー再設定は行いません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

参照は別実装ですがHLL流束族とHeunを共有し、外部AMROC・LAVA・RKDGを実行した意味ではありません。有限格子の数値参照であり、厳密2D解や誤差上界ではありません。角の特別処理を加えない入力では数値的なエントロピー層が下流へ運ばれうるため、補正付き原著PPMの細部一致を主張しません。全流体領域の差とL∞、固定した角近傍の密度・圧力・エントロピー診断を隠さず残します。傾きは純粋な空間次数の証明ではなく、薄いすべり線・巻き上がり・一般形状や高次精度の収束は未検証です。 正規化した密度の最大差は.592/.670/.665で減少せず、角近傍のlog(p/ρ^γ)の最小値も−.0784/−.1224/−.3510と大きく変わります。これは任意の定数を含む絶対量で、負になるほど誤差が大きいという指標ではありませんが、角の極値や点ごとのパターンが安定・収束したとは主張できません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)

## English

[Density from the actual 2D Euler computation: Mach3,gamma=1.4,T=4,240×80 cells. The solid step is masked. No corner entropy correction is used; the picture does not establish convergence of fine slip lines or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/forward-step-m3-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-forward-step/#forward-step-m3) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#forward-step-en)

### Equations and problem definitions

Two-dimensional Euler flow with gamma=1.4 and inflow rho=1.4,u=3,v=0,p=1 evolves to T=4 in [0,3]×[0,1] minus a step of height .2 starting at x=.6.

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

#### Mach3 forward step: wall budgets and grid verification

Supplementary execution example · Example definition or validation formula

$$
\partial_tU+\partial_xF(U)+\partial_yG(U)=0,\qquad U=(\rho,\rho u,\rho v,E)^T
$$

$$
\Omega=([0,3]\times[0,1])\setminus([0.6,3]\times[0,0.2]),\quad (\rho,u,v,p)_\infty=(1.4,3,0,1)
$$

$$
\sum_{C\subset\Omega}|C|(\bar U_C^{n+1}-\bar U_C^n)=\frac{\Delta t}{2}(B(U^n)+B(U^{(1)})),\quad B=-\sum_{\partial\Omega}|f|\widehat F_n
$$

$$
\epsilon_1(\rho)=\frac{\sum_{C\subset\Omega}|\bar\rho_C-\overline{\rho_{\rm ref}}_C|}{\sum_{C\subset\Omega}|\overline{\rho_{\rm ref}}_C|}
$$

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

### Exact and reference solutions

No exact full-field solution is attached. A newly executed separate C++ finite-volume reference and its two-grid increment are shown, with the shared flux family/time integration,uncorrected corner and finite-grid limits made explicit.

#### [Mach-3 forward-facing step: independent C++ finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en#forward-step-m3-en-measurements)

Finite-grid numerical reference · Reference for the same problem

partial_t U + partial_x F(U) + partial_y G(U) = 0; Uref_C = sum_f(|C_f| Uref_f)/|C| on fluid cells (conservative restriction of a finite-grid reference).

Two-dimensional ideal-gas Euler flow with gamma=1.4 in [0,3]×[0,1] excluding the solid step x>=.6,y<.2. Uniform initial/inflow primitive state (rho,u,v,p)=(1.4,3,0,1), reflecting slip channel/step walls, right zero-gradient outflow and T=4. The reference is a separately written C++17 unsplit finite-volume implementation with primitive MUSCL generalized minmod(theta=1.5), Davis HLL flux and Heun/SSPRK2 at CFL=.3 on 240×80 and480×160 cells. Normal slopes touching walls/exterior boundaries are zero; reconstructed primitive slopes may be rescaled without altering cell means. The primary Python calculation uses piecewise-constant HLL plus Heun; flux family/time equations are shared, while implementation and spatial reconstruction are separate. No Woodward–Colella corner entropy/enthalpy reset, state floors or time-step retries are used. The uncorrected corner can produce an entropy layer that affects the downstream reflected shock/Mach stem. This is a finite-grid numerical reference, not an exact solution, rigorous error bound, replication of corner-corrected original PPM figures, or proof that fine slip lines/vortices are resolved.

Conservatively restrict newly independently executed C++17 MUSCL/HLL/Heun reference data. The finite-grid numerical reference shares the HLL family,Heun and the uncorrected corner; it is not an exact full-field solution or error bound.

#### Mach3 forward step: wall budgets and grid verification

Inputs, acceptance,24 unit checks and numerical source were frozen before the first primary test/PDE execution. Checks cover analytic Mach3 normal-shock Rankine-Hugoniot identities, uniform parallel-channel flow, zero stationary-wall mass/energy flux, step-pressure force orientation, actual four-component budgets and raw failure retention. Newly executed separate C++17 MUSCL/generalized-minmod theta1.5/HLL/Heun references atNy80/160 are conservatively restricted for whole-fluid density/pressure L1 comparison. Ordinary public-ZIP verification reads saved reference data; reference source, contracts and execution records are bundled. The first referenceNy160 exhausted its preregistered120second budget; that actual timeout is preserved. A reference revision removed only unnecessary diagnostic-string allocation and was repinned before first primary execution; physical inputs,arithmetic,CFL and acceptance values did not change. All24 tests, three final-time runs and45 gates passed with-W error. Primary density L1=.14754/.12878/.10265, pressure L1=.19373/.16015/.12242 and last-pair density slope=.327. Reference80/160 increments=.02636/.03063, about.257/.250 of the finest primary differences. Maximum four-component relative boundary-budget residual=2.99e-13; all integrated wall mass/energy fluxes are zero. The three primary grids took about46seconds on the original Mac; revised reference80/160 took about8/65seconds.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en)

### Numerical methods

Retain the earlier HLL/MUSCL and slope-limiter comparisons; the additional lightweight example uses piecewise-constant HLL plus Heun. Methods belonging to the reference implementation are identified separately with its source and conditions.

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Monotonized central / MC](https://hrkoyama.github.io/numerical-methods-atlas/methods/mc/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Mach3 forward step: wall budgets and grid verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/forward-step-m3/?lang=en)

Supplementary execution example

Actual2D Euler finite volumes evolve60x20,120x40 and240x80 meshes toT4, comparing separately implemented MUSCL finite-grid references. Actual numerical wall fluxes, including the vertical and horizontal step faces, close all four conserved budgets. Figures and code explicitly use the variant without corner entropy correction.

Nondimensional[0,3]x[0,1] minus solidx>=.6,y<.2; gamma1.4, initial/left-inflow(rho,u,v,p)=(1.4,3,0,1), giving sound speed1 and Mach3. Right zero-gradient outflow; top,bottom and both step faces are slip walls by normal-momentum reflection. Ny multiples of5 align both walls exactly; solid storage is excluded from every fluid norm/integral. No Woodward-Colella corner entropy/enthalpy reset.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/atlas-forward-step-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

The reference is separately implemented but shares the HLL family and Heun; no external AMROC,LAVA or RKDG engine was executed. Finite-grid numerical data are neither an exact2D solution nor an error bound. Without special corner treatment, a numerical entropy layer may be advected downstream; no agreement with corrected originalPPM fine structures is claimed. Whole-fluid differences,Linf and fixed corner density/pressure/entropy diagnostics are retained. Slopes do not prove pure spatial order; thin slip lines,roll-up,general geometries and high-order convergence remain unverified. Normalized maximum density differences=.592/.670/.665 do not decrease. Corner minima of log(p/rho^gamma)=-.0784/-.1224/-.3510 change substantially. This absolute entropy variable includes an arbitrary additive constant; a more-negative value is not itself an error increase. Neither stable corner extrema nor pointwise pattern convergence is established.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/forward-step/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/run.py)
- [/code/validated-examples/2026-11-23/forward-step/fs_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/fs_solver.py)
- [/code/validated-examples/2026-11-23/forward-step/test_fs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/forward-step/test_fs.py)
