# Guderleyの収束衝撃波 / Guderley converging shock

https://hrkoyama.github.io/numerical-methods-atlas/problems/guderley/

## 日本語

[1次元球対称Eulerの保存済み半径密度を子午面に表示。γ=1.4、512球殻、r∈\[0,.75\]、R_s(−1)=.6、t=−.85。圧力ゼロの静止上流へ進む収束前の衝撃波を半解析参照と比較します。2D Cartesianや原点反射後の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-guderley/#guderley-implosion) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#guderley)

### 方程式・問題の定義

理想気体Eulerの球半径対称系。球殻体積を重みとして密度・半径運動量・全エネルギーを発展させ、半径運動量の幾何源を分けて積算します。

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

#### Guderley収束衝撃波：球対称の軽量検証

補助実行例 · 実行例の定義・検証式

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

### 厳密解・参照解

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

#### [Guderley収束衝撃波：固有値と球対称の半解析参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja#guderley-implosion-ja-measurements)

半解析解 · 同じ問題の参照

R_s(t)=0.6*(-t)^alpha, alpha=1/lambda; x=t*(0.6/r)^lambda; rho=rho0*R(x), u=-r*V(x)/(lambda*t), p=rho*(-r*C(x)/(lambda*t))^2/gamma. For r<R_s:rho=rho0,u=p=0.

理想気体Eulerの球半径対称、γ=1.4、未衝撃上流ρ0=1,u=p=0。Lazarus時間t∈[-1,-.85]、r∈[0,.75]、R_s(t)=.6(-t)^α、α=1/λです。原点収束t=0は区間外で、初期場の外側には衝撃後の相似状態があります。λは固定ExactPackの固有値探索と元stateの8点照合で求めた資格確認済みの保存値を通常追試で再利用し、相似ODE・Gauss16/32球殻求積・Euler計算は再実行します。固有値探索と元ソース点照合の再生成は別の明示コマンドです。衝撃で積分を分けた保存量の体積平均からpを求め、原始圧力の平均と区別します。閉形式の厳密セル平均や独立に実装した相似解とは呼びません。図は1D球半径結果の2D子午面表示で、2D Cartesianや反射後の計算ではありません。

γ=1.4・冷たい一様な上流を持つ球対称Guderley相似解の収束前分岐です。相似指数の固有値探索・相似ODE積分・衝撃位置で分割した球殻求積を含む半解析参照で、閉形式の厳密セル平均ではありません。通常追試は保存済みの資格確認で求めたλを再利用して相似ODEと求積を再実行し、固有値探索と元ExactPack点照合の再生成は別の明示コマンドとします。参照は固定ExactPackに基づくアダプターであり、独立に実装した相似解との照合とは扱いません。原点での収束、反射後の衝撃波、一般のEOSは今回の範囲外です。

#### Guderley収束衝撃波：球対称の軽量検証

33単体検査と3格子55判定を実行前に固定し、警告をエラーにする設定で合格しました。冷たい上流でのゼロ音速HLL分岐、幾何的な静止圧力釣合い、共有流束の収支、実際の2段の境界時刻、不正段の生配列保持を確認します。全体積L1と、あらかじめr≥.8Rsとした衝撃・非零流れ領域のL1を並べ、冷たい内側で誤差を薄めないようにします。密度・圧力の最大差と保存した時系列からの衝撃軌道も残します。半解析参照は固定LANL ExactPackの相似指数固有値ルーチンとODEを使い、反射後分岐を計算しないキャッシュ付きアダプターです。独自に再実装した相似ODEとは表示しません。別に実装したEuler有限体積計算と参照を比較します。 全体積の密度L1は.02345/.01339/.007722、圧力L1は.03277/.01743/.009477でした。r≥.8Rsの密度L1も.02414/.01378/.007948と減少します。最細の衝撃位置は.530273、相似参照は.533989で、差は約2.54セルです。最大の全3成分収支残差は8.85e-16、全段の最小内部エネルギーと音速専用丸めガード回数はともに0でした。参照のEuler差分代入残差は8.24e-9、有限オフセットの移動衝撃ジャンプ残差は4.40e-8。旧版で固有値を新規計算した全3計算は元のMacで約44.6秒でした。 公開r2のLinuxでは33検査は96.34秒で合格しましたが、検査と本計算を合わせた120秒枠の残り23.31秒で本計算が時間切れになりました。この公開追試の失敗記録と旧ソースを保持します。改訂では、既に実際のExactPack射撃法で求め、出典ソース・資格確認とSHAで結んだ固有値を再利用し、通常実行の各プロセスで射撃法を重複計算しません。臨界位相のCdiff残差と相似ODEは新しく評価します。入力・数値判定・Eulerソルバー・実行入口・120秒枠は変えません。 改訂版では33単体検査と全3入力55判定を共通120秒枠で続け、Macで計約.912秒で完了しました。全3格子の初期値・最終値・参照値・保存履歴の配列は公開r2とビット一致し、固有値の再利用で物理結果が変わらないことを別に照合しました。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja)

### 計算法

球殻の面積・体積と幾何学的な圧力源を使う区分定数HLL有限体積流束、物理時間のHeun更新による限定例です。

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Guderley収束衝撃波：球対称の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=ja)

補助実行例

冷たい静止気体へ内向きに進む球対称Guderley衝撃波を、128/256/512個の球殻でt=−1から−.85まで計算します。HLL流束とHeun法を、相似指数の固有値・半解析場・衝撃位置・保存収支と照合する軽量例です。

γ=1.4、球対称3次元の半径r∈[0,.75]、衝撃半径Rs(−1)=.6、時間t∈[−1,−.85]を固定します。衝撃前方の内側はρ0=1、u0=p0=0です。外側には初めから衝撃後の相似場があり、領域全体が冷たい一様気体という初期条件ではありません。初期保存量は衝撃位置で積分区間を分けた16点Gauss球殻体積平均とし、32点と照合します。圧力参照はp(保存量平均)で、原始圧力の体積平均とは区別します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

収束点t=0から離れた短い時間窓の1次元球対称検証です。原点の特異点、原点反射後、円筒対称、他のγ、一般摂動や非球対称の安定性は未検証です。2次元の図は保存した球殻平均を子午面へ表示したもので、2次元Cartesian計算ではありません。半解析場もODEと求積を数値評価した参照であり、閉形式の厳密セル平均ではありません。冷たい上流では圧力ゼロを許し、64epsの絶対内部エネルギー密度までの丸めによる負値を記録します。許容帯だけの音速平方根ガードは状態修復と分けて回数・最小圧力を残し、非線形正値性の一般保証は主張しません。 衝撃位置のセル単位誤差は1.13/2.27/2.54と単調に減りません。半径の絶対誤差は最初の2格子で同じ約.00665、最細で約.00372です。密度L∞差は.258/.271/.266、圧力L∞差は.492/.494/.466で、いずれも単調な減少を主張できません。L1の減少を衝撃内部の点ごとの解像や原点付近の収束へ拡張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23-r3/guderley/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/run.py)
- [/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)

## English

[A meridional-section display of saved one-dimensional spherical-radial Euler density: gamma=1.4, 512 shells, r in \[0,0.75\], Rs(-1)=0.6, t=-0.85. Compare the pre-collapse shock entering stationary zero-pressure upstream gas with a semi-analytic reference. This is not 2D Cartesian or post-collapse evolution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/guderley-implosion-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-guderley/#guderley-implosion) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#guderley-en)

### Equations and problem definitions

Spherical-radial ideal-gas Euler flow, evolving density, radial momentum and total energy with shell-volume weighting and separately integrating the radial-momentum geometric source.

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

#### Guderley converging shock: lightweight spherical-radial verification

Supplementary execution example · Example definition or validation formula

$$
\partial_t U+\frac{1}{r^2}\partial_r(r^2 F)=\left(0,\frac{2p}{r},0\right)^T,\quad U=(\rho,\rho u,E)^T
$$

$$
R_s(t)=0.6(-t)^\alpha,\quad\alpha=1/\lambda,\quad \lambda\simeq1.3943607844,\quad t<0
$$

$$
\frac{d\bar U_i}{dt}=-\frac{A_{i+1/2}\widehat F_{i+1/2}-A_{i-1/2}\widehat F_{i-1/2}}{V_i}+\left(0,p_i\frac{\Delta A_i}{V_i},0\right)^T
$$

$$
\bar U_i^{\rm ref}=\frac{\int_{r_{i-1/2}}^{r_{i+1/2}}U_{\rm sim}(r,t)r^2\,dr}{(r_{i+1/2}^3-r_{i-1/2}^3)/3},\qquad p_i^{\rm ref}=p(\bar U_i^{\rm ref})
$$

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

### Exact and reference solutions

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

#### [Guderley converging shock: eigenvalue and spherical semi-analytic reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en#guderley-implosion-en-measurements)

Semi-analytic reference · Reference for the same problem

R_s(t)=0.6*(-t)^alpha, alpha=1/lambda; x=t*(0.6/r)^lambda; rho=rho0*R(x), u=-r*V(x)/(lambda*t), p=rho*(-r*C(x)/(lambda*t))^2/gamma. For r<R_s:rho=rho0,u=p=0.

Ideal-gas Euler in spherical radial symmetry, gamma=1.4, with unshocked upstream rho0=1, u=p=0. Lazarus time t in [-1,-0.85] excludes collapse at 0; r in [0,0.75], Rs(t)=0.6*(-t)^alpha and alpha=1/lambda. The initial field already contains the shocked outer similarity state. Lambda was computed and qualified using pinned ExactPack eigenvalue shooting and eight original-state probes. Routine replay reuses that recorded lambda and freshly integrates the same pinned pre-collapse similarity ODE. Full eigenvalue and original-probe regeneration is a separate explicit command. Shells are split at the shock and conserved states are Gauss16 volume averaged, checked against Gauss32; pressure is p(Ubar). This is a dense-output adapter to ExactPack, not closed-form exact cell means or an independent similarity implementation. The figure maps 1D spherical-radial data onto a 2D meridional section, not 2D Cartesian or post-collapse evolution.

The pre-collapse branch of the spherical Guderley similarity solution at gamma=1.4 with a cold uniform upstream state. Eigenvalue shooting, similarity-ODE integration and shock-split shell quadrature make it semi-analytic rather than closed-form exact cell means. Routine replay reuses lambda from the retained qualification, freshly integrating the similarity ODE and quadrature; recomputing the eigenvalue and original ExactPack probes is a separate explicit command. This is an adapter to pinned ExactPack, not an independently implemented similarity evaluator. Collapse at the origin, the reflected shock and general equations of state remain outside this example.

#### Guderley converging shock: lightweight spherical-radial verification

The33 unit checks and55 gates over three refinements were fixed before execution and passed with warnings treated as errors. Checks cover the zero-sound-speed cold HLL branch, geometric static-pressure balance, shared-flux budgets, actual two-stage boundary times and raw failed-stage retention. Full-volume L1 is shown alongside the predetermined r>=0.8*Rs shock/nonzero-flow region, so cold inner gas does not hide active errors. Maximum density/pressure differences and the saved shock trajectory remain visible. The semi-analytic reference uses the pinned LANL ExactPack eigenvalue routine and ODE through a cached pre-collapse-only adapter. It is not an independently reimplemented similarity ODE; the separately implemented finite-volume Euler evolution is compared against that reference. Full-volume density L1 is0.02345/0.01339/0.007722 and pressure L1 is0.03277/0.01743/0.009477. Density L1 in the predetermined r>=0.8*Rs region also decreases:0.02414/0.01378/0.007948. The finest measured shock radius is0.530273 against similarity0.533989, about2.54 cells apart. The maximum scaled three-component budget residual is8.85e-16. Minimum internal energy and sound-speed-only roundoff guard evaluations are both0. The smooth-reference Euler finite-difference residual is8.24e-9 and finite-offset moving-jump residual4.40e-8. The older three-run execution with a newly computed similarity eigenvalue took about44.6 seconds on the original Mac. Public r2 passed all33 Linux tests in96.34 seconds, but its fixed-input runner timed out after the remaining23.31 seconds of the combined120-second test-plus-run budget. That failed replay and its sources are retained. The revision reuses the eigenvalue already obtained by actual ExactPack shooting, bound by SHA to its source and qualification, instead of shooting again in both normal processes. The critical-phase Cdiff residual and similarity ODE are freshly evaluated. Inputs, numerical criteria, Euler solver, fixed-input runner and120-second budget are unchanged. In the revision,33 unit tests and all three fixed inputs with55 gates completed sequentially within one120-second budget in about0.912s on the Mac. Initial,final,reference and saved-history arrays for all three grids were bit-identical to published r2, separately checking that reuse of the eigenvalue preserved the physical results.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en)

### Numerical methods

A scoped spherical-shell example with piecewise-constant HLL finite-volume fluxes, shell areas/volumes, the geometric pressure source and physical-time Heun updates.

- [HLL](https://hrkoyama.github.io/numerical-methods-atlas/methods/hll/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Guderley converging shock: lightweight spherical-radial verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/guderley-implosion/?lang=en)

Supplementary execution example

An inward spherical Guderley shock in cold stationary gas is evolved from t=-1 to -0.85 on 128/256/512 radial shells. HLL fluxes and Heun steps are checked against a similarity eigenvalue/field, shock trajectory and discrete conservation budgets.

Fix gamma=1.4, three-dimensional spherical symmetry on r in [0,0.75], Rs(-1)=0.6 and t in [-1,-0.85]. Ahead of the inward shock the inner gas is exactly rho0=1,u0=p0=0. The outer region already contains the shocked similarity field; the entire initial domain is not a uniform cold state. Initial conserved shell means use order16 Gauss integration split at the exact shock, checked against order32. Reference pressure is p(mean conserved state), not mean primitive pressure.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/atlas-guderley-2026-11-23-r3.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This is a short one-dimensional spherical verification away from collapse t=0. The singular origin, reflected branch, cylindrical geometry, other gammas and nonspherical perturbation stability are untested. Two-dimensional pictures map saved spherical shell means onto a meridional plane; they are not Cartesian2D evolution. The semi-analytic field is a numerically evaluated ODE/quadrature reference, not a closed-form exact cell average. Zero pressure is allowed in the cold upstream; cancellation-band negative internal energy density down to an absolute64eps is recorded. Sound-speed square-root guards only within that band have separate counts/minimum raw pressure and do not repair the state. No general nonlinear positivity theorem is claimed. Shock-position error in cell units does not decrease monotonically:1.13/2.27/2.54. Absolute radius error is about0.00665 for the first two grids and0.00372 for the finest. Density Linf differences0.258/0.271/0.266 and pressure Linf0.492/0.494/0.466 are also not monotonically decreasing. L1 reduction is not evidence that the discontinuity is pointwise resolved or that the collapse region converges.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23-r3/guderley/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/run.py)
- [/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/guderley_solver.py)
- [/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/references/precollapse.py)
- [/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r3/guderley/test_guderley.py)
