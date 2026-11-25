# SSPRK(3,3) / SSPRK(3,3)

Status: educational-example

Read about SSPRK(3,3), follow the original references and inspect related educational code and checks.

「SSPRK(3,3)」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers.

Other names: SSPRK33, SSPRK3, Shu-Osher RK3, SSP RK3, TVD RK3

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py

- Reference: https://doi.org/10.1175/2009MWR2724.1 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1137/S003614450036757X — Checked the three-stage updates and the forward-Euler hypothesis behind SSP. No general SSP/TVD/nonlinear stability guarantee is borrowed for this Miczek flux; the stated Fourier matrices and actual stage states are checked separately.

## Small fixed-input validation supplements

A fixed smooth 2D Euler isentropic vortex at background Mach numbers .1 and .01 compares ordinary Roe and Miczek-type dissipation-matrix preconditioning D=P⁻¹|PA|, with unlimited central primitive-variable MUSCL reconstruction for both. SSPRK(3,3) retains physical time and the acoustic CFL. Velocity error, dynamically normalized pressure error, periodic conservation and sampled Fourier diagnostics are evaluated separately. Pseudo-time or dual-time steady acceleration, slope limiting and TVD guarantees remain outside this example. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

背景Mach数.1/.01の滑らかな2D Euler等エントロピー渦で、両流束に無制限の中心primitive MUSCL再構築を用い、通常RoeとMiczek系の数値散逸行列前処理D=P⁻¹|PA|を比較します。SSPRK(3,3)で元の物理時間項と音響CFLを保ち、速度誤差・動圧規格化した圧力誤差・周期保存収支・標本Fourier診断を分けて評価します。擬似時間・二重時間積分の定常加速や、勾配制限・TVDの保証は扱いません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

- Low-Mach isentropic vortex: preconditioned Roe flux verification: https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/result.json

- Euler double rarefaction: positivity at every stage: https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/results/result.json

- Zalesak-type 2D rotation: conservation, bounds and shape error: https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/result.json

- SRHD symmetric two-shock collision: https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/
- SRMHD finite-amplitude circularly polarized Alfvén wave: https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/result.json

- Fisher–KPP: a special-speed exact front: https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/
- Keller–Segel: a manufactured coupled-flux solution: https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json

Common execution records: [{"id": "low-mach-vortex", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "euler-double-rarefaction-positivity", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "zalesak-rotation", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srhd-collision", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "srmhd-alfven", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "fisher-kpp-special-front", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "keller-segel-forced-flux", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [非粘性Burgers方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#burgers-ja) (`burgers`; burgers-shock, burgers-fan)
- [LWR交通流モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#traffic-ja) (`traffic`; traffic-jam, traffic-fan)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; double-rarefaction, isentropic-vortex)
- [浅水方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#shallow-water-ja) (`shallow-water`; dam-break)
- [等温流体方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#isothermal-ja) (`isothermal`; isothermal-jump)
- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`; zalesak)
- [特殊相対論的流体（SRHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srhd-ja) (`srhd`; srhd-collision)
- [特殊相対論的理想MHD（SRMHD）](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#srmhd-ja) (`srmhd`; srmhd-alfven)
- [Fisher–KPP侵入前線](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja) (`bio-fisher-kpp`; fisher-kpp-special-front)
- [Keller–Segel走化性](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja) (`bio-keller-segel`; keller-segel-forced-flux)
- [外力・移流付きKeller–Segel製造問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja) (`forced-keller-segel-model`; keller-segel-forced-flux)

#### 問題の図 (`method-problems-ja`)

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja) (`burgers-shock`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja) (`burgers-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja) (`traffic-jam`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja) (`traffic-fan`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

従来のGodunov／HLLEプレビューと、追加のMUSCL・Lax–Friedrichs・平均保存スケーリング・SSPRK(3,3)固定入力は別の実行例です。段階正値性の条件は追加版の説明・契約・全段ログに限定します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

- [Euler二重膨張波：段階ごとの正値性](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) (`euler-double-rarefaction-positivity`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja) (`dam-break`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja) (`isothermal-jump`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) (`isentropic-vortex`)

![M∞=.01、64²、T=.1の実際の2次元Euler計算。全\[-10,10\]²領域から中心\[-3,3\]²を拡大し、保存速度から差分で求めた渦度と背景流を引いた速度矢印で、MUSCL付き通常Roe／前処理Roeを比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

従来のKEEP/RK4固定例を保持し、新しい低Mach比較にRoe・数値散逸の前処理・無制限中心primitive MUSCL・SSPRK(3,3)を対応付けます。個々の実行例が使う手法は実行ページで区別します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#code-ja)

- [低Mach等エントロピー渦：前処理Roe流束の軽量検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja) (`low-mach-vortex`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja) (`nonlinear-exp-ode`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

公開の全陽的RK tableauに対する非自律・非線形製造解の検査です。保存プレビューはRK4を使います。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja) (`nonlinear-rational-decay`)

![保存済み有理減衰ODEの時間刻み収束（代表3手法）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

![実際の2次元スカラー輸送の最細格子の保存セル平均。全\[0,1\]²のうちx∈\[.28,.72\], y∈\[.53,.97\]の円盤周辺を拡大し、一回転後の一次風上とminmod MUSCLを幾何学的な参照セル平均と比較します。切り欠きの数値拡散を残した図で、FCT法やEuler流体の計算ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

同じ回転速度・周期有限体積格子で、一次風上とminmod MUSCLをSSPRK(3,3)で進めます。Zalesak FCTを実装したという意味ではありません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

- [Zalesak型2D回転輸送：保存・有界性・形状誤差](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) (`zalesak-rotation`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) (`srhd-collision`)

![最細格子の実際の保存密度Dの1D x–t図。5保存時刻を使用し、2D流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

同じ7保存量RMHD演算子をB=0で使い、MUSCL/minmod・因果的HLL波速±1・SSPRK33で進めます。Z=ρhW²の物理根を保護付きNewton法で復元し、残差と保存量往復を確認します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#code-ja)

- [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) (`srhd-collision`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) (`srmhd-alfven`)

![最細格子の実際の横磁場Byの1D x–t図。5保存時刻を使い、計算は完全な磁気結合を含みます。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

D・運動量3成分・全エネルギー・横磁場2成分の全7変数を同じMUSCL/minmod–HLL–SSPRK33で進めます。磁場は動的に結合し、完全なRMHDのZ根で原始変数へ復元します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#code-ja)

- [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) (`srmhd-alfven`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

##### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`)

![波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。 特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#code-ja)

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

![滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。


#### 厳密解・参照解 (`method-references-ja`)

##### [Burgers衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=ja#references-ja) (`burgers-shock`)

- [Burgers／衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-shock-ja) (`burgers-shock`; 関連モデルの参照; 解析参照)

左右状態(1,0)、段差位置0.5、端点継続が一致します。点値とセル平均の評価は区別します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-shock)

##### [Burgers膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=ja#references-ja) (`burgers-fan`)

- [Burgers／膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-burgers-fan-ja) (`burgers-fan`; 関連モデルの参照; 解析参照)

左右状態(0,1)、段差位置0.5、端点継続が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=burgers-fan)

##### [交通流の渋滞衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=ja#references-ja) (`traffic-jam`)

- [交通流／上流へ進む衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-jam-ja) (`traffic-jam`; 関連モデルの参照; 解析参照)

流束ρ(1-ρ)、左右密度(0.3,0.9)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-jam)

##### [交通流の希薄化波](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=ja#references-ja) (`traffic-fan`)

- [交通流／渋滞解消の膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-traffic-fan-ja) (`traffic-fan`; 関連モデルの参照; 解析参照)

流束ρ(1-ρ)、左右密度(0.9,0.1)、段差位置0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=traffic-fan)

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) (`double-rarefaction`)

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction)

##### [湿潤床ダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=ja#references-ja) (`dam-break`)

- [浅水流／水深が正のダム崩壊](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-swe-dam-break-ja) (`swe-dam-break`; 関連モデルの参照; 半解析参照)

湿潤河床、g=1、左右水深(2,1)・速度0、x0=0.5が一致します。乾燥河床例への対応ではありません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=swe-dam-break)

##### [等温流体の密度ジャンプ](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=ja#references-ja) (`isothermal-jump`)

- [等温流／密度跳躍](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isothermal-jump-ja) (`isothermal-jump`; 関連モデルの参照; 半解析参照)

p=ρ、音速1、左右密度(1,0.125)・速度0、x0=0.5が一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=isothermal-jump)

##### [周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja#references-ja) (`isentropic-vortex`)

- [等エントロピー渦：低Mach比較に用いるEuler解析場](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-isentropic-vortex-ja) (`isentropic-vortex`; 同じ問題の参照; 解析参照)

同じ等エントロピー移動渦族の解析場です。保存量をGauss求積してから圧力・速度を算出し、周期の継ぎ目に残るGaussianの裾と求積誤差を明記します。

[既存の参照図](/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja#low-mach-vortex-ja-measurements)

##### [指数関数を厳密解に持つ非線形・非自律ODE](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=ja#references-ja) (`nonlinear-exp-ode`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [有理減衰ODE（y′ = −y²）](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=ja#references-ja) (`nonlinear-rational-decay`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#references-ja) (`zalesak`)

- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja) (`zalesak-rotation`; 同じ問題の参照; 解析参照)

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。

[既存の参照図](/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-measurements)

##### [SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja#references-ja) (`srhd-collision`)

- [相対論的対称衝突：特殊化した二衝撃波Taub参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srhd-collision-ja) (`srhd-collision`; 同じ問題の参照; 半解析参照)

独自の穏やかな対称入力で、接触面は同じ静止状態へ退化します。一般三波Riemann解、高Lorentz因子、原著の数値入力は検証しません。Eは静止質量を含み、保存量の厳密セル平均と比較します。

[既存の参照図](/numerical-methods-atlas/validation/srhd-collision/?lang=ja#srhd-collision-ja-measurements)

##### [SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja#references-ja) (`srmhd-alfven`)

- [SRMHD円偏波：有限振幅厳密族と独立テンソル積分](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-srmhd-alfven-ja) (`srmhd-alfven`; 同じ問題の参照; 解析参照)

原著の厳密解族を独立な低次法で計算し、ECHO法や原著誤差表は再現しません。一般RMHD衝撃波、極端な磁化・Lorentz因子、GR、抵抗MHD、多次元磁場発散制御は対象外。図は実際の1D時空間場です。

[既存の参照図](/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja#srmhd-alfven-ja-measurements)

##### [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#references-ja) (`fisher-kpp-special-front`)

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja) (`fisher-kpp-special-front`; 同じ問題の参照; 解析参照)

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

[既存の参照図](/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-measurements)

##### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#references-ja) (`keller-segel-forced-flux`)

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja) (`keller-segel-forced-flux`; 同じ問題の参照; 製造解)

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

[既存の参照図](/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/time-integration/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Euler二重膨張波：段階ごとの正値性 (`euler-double-rarefaction-positivity`)

[Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

既存の強い二重希薄波を128/256/512セルで計算し、平均保存型の正値性スケーリングをMUSCL・大域LF流束・SSPRK(3,3)へ接続します。各前進Euler段と各SSP凸結合の密度・圧力・境界保存収支を記録します。

##### 低Mach等エントロピー渦：前処理Roe流束の軽量検証 (`low-mach-vortex`)

[周期移動等エントロピー渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/verification.json)

同じ非線形2次元Euler渦をN=16/32/64、背景Mach数.1/.01でT=.1まで進め、通常RoeとMiczek型の空間流束前処理を比較します。全12計算で、速度・動圧スケールの圧力誤差、保存収支、音響刻み、実段状態を調べます。

##### Zalesak型2D回転輸送：保存・有界性・形状誤差 (`zalesak-rotation`)

[Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

##### SRHDの対称二衝撃波衝突 (`srhd-collision`)

[SRHDの対称二衝撃波衝突](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

相対論的な対称衝突を、独立なTaub関係から得る厳密な保存量セル平均と比較し、実際の1D時空間場を保存します。

##### SRMHDの有限振幅円偏極Alfvén波 (`srmhd-alfven`)

[SRMHDの有限振幅円偏極Alfvén波](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

完全な磁気応力と誘導を含むSRMHDで非線形有限振幅波を1周期進め、厳密セル平均、位相、振幅と細分化を検査します。

##### Fisher–KPP：特殊波速の厳密前線 (`fisher-kpp-special-front`)

[Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

##### Keller–Segel：連成流束の製造解 (`keller-segel-forced-flux`)

[Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

背景Mach数.1/.01の滑らかな2D Euler等エントロピー渦で、両流束に無制限の中心primitive MUSCL再構築を用い、通常RoeとMiczek系の数値散逸行列前処理D=P⁻¹|PA|を比較します。SSPRK(3,3)で元の物理時間項と音響CFLを保ち、速度誤差・動圧規格化した圧力誤差・周期保存収支・標本Fourier診断を分けて評価します。擬似時間・二重時間積分の定常加速や、勾配制限・TVDの保証は扱いません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。 追加の軽量1D SRHD対称衝突/SRMHD有限振幅円偏極波は、同じ完全7量の応力/誘導、MUSCL-minmod、因果的HLL±1、SSPRK33とZ回復を使用。一般Riemann・GR・極端速度の認証ではありません。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/low-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/run.py)
- [/code/validated-examples/2026-11-23/low-mach/lm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/lm_solver.py)
- [/code/validated-examples/2026-11-23/low-mach/linear_stability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/linear_stability.py)
- [/code/validated-examples/2026-11-23/low-mach/references/analytic_vortex.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/references/analytic_vortex.py)
- [/code/validated-examples/2026-11-23/low-mach/references/miczek_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/references/miczek_matrix.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/low-mach/test_low_mach.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/test_low_mach.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Inviscid Burgers equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#burgers-en) (`burgers`; burgers-shock, burgers-fan)
- [LWR traffic model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#traffic-en) (`traffic`; traffic-jam, traffic-fan)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; double-rarefaction, isentropic-vortex)
- [Shallow-water equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#shallow-water-en) (`shallow-water`; dam-break)
- [Isothermal flow equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#isothermal-en) (`isothermal`; isothermal-jump)
- [Two-dimensional rotational advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en) (`rotational-advection`; zalesak)
- [Special-relativistic hydrodynamics (SRHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srhd-en) (`srhd`; srhd-collision)
- [Special-relativistic ideal MHD (SRMHD)](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#srmhd-en) (`srmhd`; srmhd-alfven)
- [Fisher–KPP invasion front](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-fisher-kpp-en) (`bio-fisher-kpp`; fisher-kpp-special-front)
- [Keller–Segel chemotaxis](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en) (`bio-keller-segel`; keller-segel-forced-flux)
- [Forced advective Keller–Segel manufactured problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en) (`forced-keller-segel-model`; keller-segel-forced-flux)

#### Problem figures (`method-problems-en`)

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en) (`burgers-shock`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-shock.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en) (`burgers-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/burgers-fan.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en) (`traffic-jam`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-jam.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en) (`traffic-fan`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/traffic-fan.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

The earlier Godunov/HLLE preview and the new MUSCL/Lax–Friedrichs/mean-preserving-scaling/SSPRK(3,3) run are separate execution records. Stage-positivity conditions are scoped to the additional release, its contract and all-stage diagnostics.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

- [Euler double rarefaction: positivity at every stage](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) (`euler-double-rarefaction-positivity`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en) (`dam-break`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/dam-break.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en) (`isothermal-jump`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/isothermal-jump.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) (`isentropic-vortex`)

![Actual 2D Euler evolution at M∞=.01, 64² and T=.1. A central \[-3,3\]² crop of the full \[-10,10\]² computation compares ordinary and preconditioned Roe with MUSCL. Vorticity is derived by finite differences of saved velocity; arrows show velocity minus the background flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/results/low-mach-vortex-preview.png)

Retain the historical KEEP/RK4 fixed case and connect Roe, dissipation preconditioning, unlimited central primitive MUSCL and SSPRK(3,3) to the additional low-Mach comparison. Each execution page states its own methods.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#code-en)

- [Low-Mach isentropic vortex: preconditioned Roe flux verification](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en) (`low-mach-vortex`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en) (`nonlinear-exp-ode`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-exp-ode.png)

Public nonautonomous/nonlinear manufactured-solution checks exercise every explicit RK tableau; the saved preview uses RK4.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en) (`nonlinear-rational-decay`)

![Stored time-refinement errors for rational decay, showing three methods.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/nonlinear-rational-decay.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

![Saved cell means on the finest grid of actual two-dimensional scalar transport. Zoom x in\[.28,.72\],y in\[.53,.97\] from the full unit square and compare donor-cell upwinding and minmod MUSCL after one revolution against geometric reference cell means. Slot diffusion remains visible; this is not an FCT algorithm or Euler-flow calculation.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

Donor-cell upwinding and minmod MUSCL use the same prescribed rotation, periodic finite-volume grid and SSPRK(3,3). This does not claim implementation of Zalesak FCT.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

- [Zalesak-type 2D rotation: conservation, bounds and shape error](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) (`zalesak-rotation`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) (`srhd-collision`)

![Actual finest-grid1D x–t conserved-density field from five stored times; not a two-dimensional flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srhd-collision-preview.png)

Use the shared seven-component RMHD operator at B=0 with primitive MUSCL/minmod, causal HLL bounds±1 and SSPRK33. Safeguarded Newton recovers the physical Z=rho h W² root; check residual and full conserved-state roundtrip.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#code-en)

- [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) (`srhd-collision`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) (`srmhd-alfven`)

![Actual finest-grid transverse By in1D x–t from five stored times; the solver includes full magnetic coupling.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/results/srmhd-alfven-preview.png)

Evolve all seven variables D,three momenta,total E and two transverse magnetic fields with the shared MUSCL/minmod–HLL–SSPRK33 operator. Magnetic dynamics are coupled; primitive recovery solves the full RMHD Z root.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#code-en)

- [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) (`srmhd-alfven`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

##### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`)

![Separate profile, phase, grid, time and finite-boundary errors. The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

Use centered second-order differences and SSPRK3 with exact Dirichlet values at every stage. Compare time errors to an independent reference for the same95-unknown semidiscreteODE.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#code-en)

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en) (`fisher-kpp-special-front`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Separate profile, phase, grid, time and finite-boundary errors.

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`)

![Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#code-en)

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) (`keller-segel-forced-flux`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.


#### Exact / reference solutions (`method-references-en`)

##### [Burgers shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-shock/?lang=en#references-en) (`burgers-shock`)

- [Burgers / shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-shock-en) (`burgers-shock`; Related-model reference; Analytic reference)

States (1,0), jump position 0.5 and endpoint continuation match; distinguish point and cell-average evaluation. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-shock)

##### [Burgers rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/burgers-fan/?lang=en#references-en) (`burgers-fan`)

- [Burgers / rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-burgers-fan-en) (`burgers-fan`; Related-model reference; Analytic reference)

States (0,1), jump position 0.5 and endpoint continuation match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=burgers-fan)

##### [Traffic jam shock](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-jam/?lang=en#references-en) (`traffic-jam`)

- [Traffic / upstream shock](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-jam-en) (`traffic-jam`; Related-model reference; Analytic reference)

Flux ρ(1-ρ), left/right densities (0.3,0.9) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-jam)

##### [Traffic clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/problems/traffic-fan/?lang=en#references-en) (`traffic-fan`)

- [Traffic / clearing fan](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-traffic-fan-en) (`traffic-fan`; Related-model reference; Analytic reference)

Flux ρ(1-ρ), left/right densities (0.9,0.1) and jump position 0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=traffic-fan)

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) (`double-rarefaction`)

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference; Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction)

##### [Wet-bed dam break](https://hrkoyama.github.io/numerical-methods-atlas/problems/dam-break/?lang=en#references-en) (`dam-break`)

- [Shallow water / wet dam break](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-swe-dam-break-en) (`swe-dam-break`; Related-model reference; Semi-analytic reference)

Wet bed, g=1, depths (2,1), zero velocities and x0=0.5 match; this is not a dry-bed correspondence. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=swe-dam-break)

##### [Isothermal density jump](https://hrkoyama.github.io/numerical-methods-atlas/problems/isothermal-jump/?lang=en#references-en) (`isothermal-jump`)

- [Isothermal / density jump](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isothermal-jump-en) (`isothermal-jump`; Related-model reference; Semi-analytic reference)

p=ρ, sound speed one, densities (1,0.125), zero velocities and x0=0.5 match. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=isothermal-jump)

##### [Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en#references-en) (`isentropic-vortex`)

- [Isentropic vortex: analytic Euler field for low-Mach comparisons](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-isentropic-vortex-en) (`isentropic-vortex`; Same-problem reference; Analytic reference)

Analytic field for the same translating isentropic-vortex family. Pressure and velocity are evaluated after Gauss integration of conserved variables; finite-periodic Gaussian tails and quadrature error remain explicit.

[Existing reference profile](/numerical-methods-atlas/validation/low-mach-vortex/?lang=en#low-mach-vortex-en-measurements)

##### [Nonlinear nonautonomous ODE with exponential exact solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-exp-ode/?lang=en#references-en) (`nonlinear-exp-ode`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Rational-decay ODE (y′ = −y²)](https://hrkoyama.github.io/numerical-methods-atlas/problems/nonlinear-rational-decay/?lang=en#references-en) (`nonlinear-rational-decay`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#references-en) (`zalesak`)

- [Zalesak-type slotted disk: rigid rotation and geometric cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en) (`zalesak-rotation`; Same-problem reference; Analytic reference)

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.

[Existing reference profile](/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-measurements)

##### [SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en#references-en) (`srhd-collision`)

- [Relativistic symmetric collision: specialized two-shock Taub reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srhd-collision-en) (`srhd-collision`; Same-problem reference; Semi-analytic reference)

Custom mild symmetric input; contact degenerates to identical resting states. No general three-wave Riemann,extreme-Lorentz-factor or original-paper numerical-input reproduction claim. E includes rest mass; compare exact conserved cell means.

[Existing reference profile](/numerical-methods-atlas/validation/srhd-collision/?lang=en#srhd-collision-en-measurements)

##### [SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en#references-en) (`srmhd-alfven`)

- [SRMHD circular wave: finite-amplitude exact family and independent tensor integration](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-srmhd-alfven-en) (`srmhd-alfven`; Same-problem reference; Analytic reference)

Use the original exact family with an independent lower-order operator; no ECHO-algorithm or error-table reproduction. Generic RMHD shocks,extreme magnetization/Lorentz factors,GR,resistive MHD and multidimensional divergence control are outside scope. Figures show actual1D x–t fields.

[Existing reference profile](/numerical-methods-atlas/validation/srmhd-alfven/?lang=en#srmhd-alfven-en-measurements)

##### [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en#references-en) (`fisher-kpp-special-front`)

- [Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fisher-kpp-special-front-en) (`fisher-kpp-special-front`; Same-problem reference; Analytic reference)

The special front is distinct from the minimum linear speed2. This is not a steep-data speed-selection study, long-time propagation result or certified machine-error barrier proof.

[Existing reference profile](/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en#fisher-kpp-special-front-en-measurements)

##### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en#references-en) (`keller-segel-forced-flux`)

- [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-keller-segel-forced-flux-en) (`keller-segel-forced-flux`; Same-problem reference; Manufactured solution)

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

[Existing reference profile](/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/time-integration/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Euler double rarefaction: positivity at every stage (`euler-double-rarefaction-positivity`)

[Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/euler-double-rarefaction-positivity/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/atlas-euler-positivity-2026-11-23-r2.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/verification.json)

Evolve the existing strong double rarefaction on 128/256/512 cells, connecting mean-preserving positivity scaling to MUSCL, global LF fluxes and SSPRK(3,3). Log density, pressure and boundary budgets for every FE substep and SSP convex combination.

##### Low-Mach isentropic vortex: preconditioned Roe flux verification (`low-mach-vortex`)

[Periodic moving isentropic vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/isentropic-vortex/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/atlas-low-mach-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/verification.json)

The same nonlinear 2D Euler vortex is evolved to T=0.1 on N=16/32/64 at background Mach 0.1/0.01, comparing ordinary Roe with Miczek spatial flux preconditioning. Twelve fixed runs retain velocity and dynamically scaled pressure errors, conserved budgets, acoustic steps and actual stage states.

##### Zalesak-type 2D rotation: conservation, bounds and shape error (`zalesak-rotation`)

[Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json)

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

##### SRHD symmetric two-shock collision (`srhd-collision`)

[SRHD symmetric two-shock collision](https://hrkoyama.github.io/numerical-methods-atlas/problems/srhd-collision/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srhd-collision/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Compare a relativistic symmetric collision with independent exact Taub-based conserved cell means; save actual1D x–t fields.

##### SRMHD finite-amplitude circularly polarized Alfvén wave (`srmhd-alfven`)

[SRMHD finite-amplitude circularly polarized Alfvén wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/srmhd-alfven/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/srmhd-alfven/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/atlas-relativistic-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/verification.json)

Evolve a nonlinear finite-amplitude wave for one period with full SRMHD magnetic stress and induction; check exact cell means,phase,amplitude and refinement.

##### Fisher–KPP: a special-speed exact front (`fisher-kpp-special-front`)

[Fisher–KPP: a special-speed exact front](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Separate profile, phase, grid, time and finite-boundary errors.

##### Keller–Segel: a manufactured coupled-flux solution (`keller-segel-forced-flux`)

[Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

A fixed smooth 2D Euler isentropic vortex at background Mach numbers .1 and .01 compares ordinary Roe and Miczek-type dissipation-matrix preconditioning D=P⁻¹|PA|, with unlimited central primitive-variable MUSCL reconstruction for both. SSPRK(3,3) retains physical time and the acoustic CFL. Velocity error, dynamically normalized pressure error, periodic conservation and sampled Fourier diagnostics are evaluated separately. Pseudo-time or dual-time steady acceleration, slope limiting and TVD guarantees remain outside this example. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds. Additional lightweight1D SRHD symmetric collision/SRMHD finite-amplitude CP wave use the shared full7-variable stress/induction,MUSCL-minmod,causalHLL±1,SSPRK33 and Z recovery; no generic Riemann,GR or extreme-speed claim.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/time_integration.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/hamiltonian.py)
- [/code/validated-examples/2026-11-23/low-mach/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/run.py)
- [/code/validated-examples/2026-11-23/low-mach/lm_solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/lm_solver.py)
- [/code/validated-examples/2026-11-23/low-mach/linear_stability.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/linear_stability.py)
- [/code/validated-examples/2026-11-23/low-mach/references/analytic_vortex.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/references/analytic_vortex.py)
- [/code/validated-examples/2026-11-23/low-mach/references/miczek_matrix.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/references/miczek_matrix.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/run.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/euler_positivity.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/double_rarefaction.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/references/numart_reference_riemann.py)
- [/code/validated-examples/2026-11-23/zalesak/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/run.py)
- [/code/validated-examples/2026-11-23/zalesak/rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/rotation.py)
- [/code/validated-examples/2026-11-23/zalesak/references/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/geometry.py)
- [/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/references/qualify_reference.py)
- [/code/validated-examples/2026-11-23/relativistic/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/run.py)
- [/code/validated-examples/2026-11-23/relativistic/relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/relativistic.py)
- [/code/validated-examples/2026-11-23/relativistic/references/exact.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/references/exact.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/fisher.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/fisher.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/schnakenberg.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_time_geometry.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_runge_kutta.py)
- [/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_hamiltonian.py)
- [/code/validated-examples/2026-11-23/low-mach/test_low_mach.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/low-mach/test_low_mach.py)
- [/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/euler-positivity/test_euler_positivity.py)
- [/code/validated-examples/2026-11-23/zalesak/test_rotation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/test_rotation.py)
- [/code/validated-examples/2026-11-23/relativistic/test_relativistic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/relativistic/test_relativistic.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_time_geometry.py tests/test_runge_kutta.py tests/test_hamiltonian.py
```
