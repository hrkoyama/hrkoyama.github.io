# D2Q9–BGK collision and streaming / D2Q9–BGK衝突・並進

Status: educational-example

Read about D2Q9–BGK collision and streaming, follow the original references and inspect related educational code and checks. Additional fixed examples: LBM Re100 cavity: actual2D fields and Ghia centerlines. See each release for assumptions and checked scope. Additional fixed examples: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity. See each release for assumptions and checked scope. Additional fixed examples: Curved LBM annular Couette control: velocity,pressure andtorque. See each release for assumptions and checked scope. Additional fixed examples: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet. See each release for assumptions and checked scope.

「D2Q9–BGK衝突・並進」の考え方と適用範囲を、解説章・一次文献・関連する教育用コードからたどります。 追加固定例：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線。条件と検証範囲は各配布版で確認してください。 追加固定例：LBM Taylor–Green渦：格子・刻み・Machの結合感度。条件と検証範囲は各配布版で確認してください。 追加固定例：曲面LBMの環状Couette制御：速度・圧力・torque。条件と検証範囲は各配布版で確認してください。 追加固定例：LBMの実円柱Re20：Schäfer–Turek形状と明示出口。条件と検証範囲は各配布版で確認してください。

See the chapter and implementation for equations, boundaries and checked scope. Educational examples are not complete general-purpose solvers. Additional fixed examples: Three finite-Mach educational grids. Ghia is a rounded independent numerical reference, not exact. No pointwise corner order/high-Re claim or borrowed success from another cavity solver. A standard C++17compiler is required. Additional fixed examples: Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors. Additional fixed examples: Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T. Additional fixed examples: Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

Other names: LBM, LBM法, lattice Boltzmann, lattice Boltzmann method, 格子Boltzmann法, 格子ボルツマン法, D2Q9 BGK, D2Q9-BGK法, D2Q9, BGK collision

- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py

- Reference: https://doi.org/10.1103/PhysRev.94.511 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1209/0295-5075/17/6/001 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.
- Reference: https://doi.org/10.1103/PhysRevE.65.046308 — Cited by the linked chapter; inspect its source-review notes before treating this as a method-specific derivation.

## Small fixed-input validation supplements

Additional fixed examples: LBM Re100 cavity: actual2D fields and Ghia centerlines. See each release for assumptions and checked scope. Three finite-Mach educational grids. Ghia is a rounded independent numerical reference, not exact. No pointwise corner order/high-Re claim or borrowed success from another cavity solver. A standard C++17compiler is required. Additional fixed examples: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity. See each release for assumptions and checked scope. Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors. Additional fixed examples: Curved LBM annular Couette control: velocity,pressure andtorque. See each release for assumptions and checked scope. Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T. Additional fixed examples: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet. See each release for assumptions and checked scope. Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

追加固定例：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線。条件と検証範囲は各配布版で確認してください。 有限Machでの3格子教育例。Ghiaは丸めた独立数値参照で厳密解ではありません。蓋角は不連続で点ごとの二次精度や高Reを主張せず、他手法の既存キャビティ結果を本LBMの成功に流用しません。標準C++17compilerが必要です。 追加固定例：LBM Taylor–Green渦：格子・刻み・Machの結合感度。条件と検証範囲は各配布版で確認してください。 拡散尺度では格子・時間・Machが結合し、amplitude変更はReも変えます。純空間/純時間/純Mach次数や有限Machの厳密非圧縮性を主張しません。平衡初期化のkinetic startupも実誤差へ含めます。 追加固定例：曲面LBMの環状Couette制御：速度・圧力・torque。条件と検証範囲は各配布版で確認してください。 固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。 追加固定例：LBMの実円柱Re20：Schäfer–Turek形状と明示出口。条件と検証範囲は各配布版で確認してください。 原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

- LBM Re100 cavity: actual2D fields and Ghia centerlines: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/results/result.json

- LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/result.json

- Curved LBM annular Couette control: velocity,pressure andtorque: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/result.json

- Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet: https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/result.json

Common execution records: [{"id": "lbm-cavity-re100", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lbm-taylor-green", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lbm-annular-couette-control", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en"}, "kind": "dedicated-supplement"}, {"id": "lbm-cylinder-re20", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`; taylor-green, lbm-shear, channel-poiseuille, lid-driven-cavity, lbm-annular-couette-control, lbm-cylinder-re20)
- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`; taylor-green, lbm-shear, channel-poiseuille, lid-driven-cavity, lbm-annular-couette-control, lbm-cylinder-re20)

#### 問題の図 (`method-problems-ja`)

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

![保存済みTaylor–Green渦の速度と圧力。](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

- [LBM Taylor–Green渦：格子・刻み・Machの結合感度](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) (`lbm-taylor-green`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。

##### [周期せん断波の粘性減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja) (`lbm-shear`)

![保存済みせん断波振幅と粘性減衰の参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja) (`channel-poiseuille`)

![保存済み半格子壁Poiseuille速度分布と参照値。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

- [LBM Re100蓋駆動キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) (`lbm-cavity-re100`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。

##### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

円弧交点qから反射特性上の3点2次補間を行います。q<.5はoutgoingの内側2点、q>.5はincomingの内側1点を使用し、q=.5はhalfway。移動壁補正、実force/torqueと非零wall massを台帳化し、floorやmass補正をしません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#code-ja)

- [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja) (`lbm-annular-couette-control`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。

##### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`)

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

標準BGK、真円交点の2次補間、半格子channel壁、非周期open streaming。出口全9成分にfeq(1,ua)+fa−feq(rhoa,ua)を設定し、既知6成分を含む変化量を収支へ記録。初期Poiseuille圧力guessから円柱摂動を実発展し、実運動量交換を平均流速基準の力係数へ換算します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#code-ja)

- [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja) (`lbm-cylinder-re20`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#references-ja) (`taylor-green`)

- [粘性流／2次元Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja) (`taylor-green`; 関連モデルの参照; 解析参照)

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=taylor-green)

- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja) (`lbm-taylor-green`; 関連モデルの参照; 解析参照)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

[既存の参照図](/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-measurements)

##### [周期せん断波の粘性減衰](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=ja#references-ja) (`lbm-shear`)

- [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja) (`sine-heat`; 関連モデルの参照; 解析参照)

周期せん断速度の線形粘性減衰とスカラー熱モードは同型ですが、LBMの格子単位・波数・粘性と参照カードのν=0.02は異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

##### [平行平板Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=ja#references-ja) (`channel-poiseuille`)

- [粘性チャネル／Poiseuille流](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poiseuille-ja) (`poiseuille`; 関連モデルの参照; 解析参照)

放物線形は共通ですが、計算は格子幅ny・目標最大速度0.01に応じた体積力、カードは単位幅・G=1・ν=0.1です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=poiseuille)

##### [Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja) (`lid-driven-cavity`)

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照; 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

[既存の参照図](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-measurements)

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照; 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。

[既存の参照図](/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja#lbm-cavity-re100-ja-measurements)

##### [曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja#references-ja) (`lbm-annular-couette-control`)

- [曲面LBMの環状Couette制御：速度・圧力・トルク](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-annular-couette-control-ja) (`lbm-annular-couette-control`; 同じ問題の参照; 解析参照)

固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。

[既存の参照図](/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja#lbm-annular-couette-control-ja-measurements)

##### [LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja#references-ja) (`lbm-cylinder-re20`)

- [実LBMのRe20円柱流：Schäfer–Turek形状と明示した流出境界](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cylinder-re20-ja) (`lbm-cylinder-re20`; 同じ問題の参照; 有限格子の数値参照)

原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

[既存の参照図](/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja#lbm-cylinder-re20-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/lattice-boltzmann/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### LBM Taylor–Green渦：格子・刻み・Machの結合感度 (`lbm-taylor-green`)

[周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json)

周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。

##### LBM Re100蓋駆動キャビティ：実2D場とGhia中心線 (`lbm-cavity-re100`)

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/verification.json)

4壁のBGK更新を3固定格子で実行し、nominal蓋速度で正規化したGhia中心線、主渦、定常性と壁運動量収支を検査します。

##### 曲面LBMの環状Couette制御：速度・圧力・torque (`lbm-annular-couette-control`)

[曲面LBMの環状Couette制御：速度・圧力・torque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json)

実円弧交点の2次Lagrange補間とstair-halfwayを、回転内壁の解析Navier–Stokes場に比較します。円柱wakeとは別の追加制御です。

##### LBMの実円柱Re20：Schäfer–Turek形状と明示出口 (`lbm-cylinder-re20`)

[LBMの実円柱Re20：Schäfer–Turek形状と明示出口](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json)

標準2D-1の全長channelと偏心円柱を実際に発展し、抗力・揚力・表面圧力差・再循環長と定常性を2格子で検査します。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

追加固定例：LBM Re100蓋駆動キャビティ：実2D場とGhia中心線。条件と検証範囲は各配布版で確認してください。 有限Machでの3格子教育例。Ghiaは丸めた独立数値参照で厳密解ではありません。蓋角は不連続で点ごとの二次精度や高Reを主張せず、他手法の既存キャビティ結果を本LBMの成功に流用しません。標準C++17compilerが必要です。 追加固定例：LBM Taylor–Green渦：格子・刻み・Machの結合感度。条件と検証範囲は各配布版で確認してください。 拡散尺度では格子・時間・Machが結合し、amplitude変更はReも変えます。純空間/純時間/純Mach次数や有限Machの厳密非圧縮性を主張しません。平衡初期化のkinetic startupも実誤差へ含めます。 追加固定例：曲面LBMの環状Couette制御：速度・圧力・torque。条件と検証範囲は各配布版で確認してください。 固定円弧と低速回転のみ。2次補間は負係数を含み一般の正値性や安定性を保証しません。補間mass非保存は実値を記録。以前の線形版は圧力.617757>.08で不合格として保存し、半径平均への置換なし。移動solidの拓撲変化や円柱の代用ではありません。 2次版旧N80の圧力.352758>.08も不合格として保持し、Ui/tau/Tを変えず両境界を固定細分化します。 追加固定例：LBMの実円柱Re20：Schäfer–Turek形状と明示出口。条件と検証範囲は各配布版で確認してください。 原典p3/p7は出口を選択可。採用NEEは独立導出した有限reservoirで、原著NEE全文の同一実装やFEATflow do-nothingと偽りません。Nabh高精度値は同BCの厳密値ではなく、原典範囲も厳密誤差区間ではありません。線形/Zou–He旧試行はstep265出口近傍で不合格として保持。有限Mach/境界/曲面差を含み一般精度保証なし。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/run.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/run.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/run.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/check_repair.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/check_repair.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/check_refinement.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/check_refinement.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/check_repair.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/check_repair.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/check_refinement.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/check_refinement.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/reference_step.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_new_models.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`; taylor-green, lbm-shear, channel-poiseuille, lid-driven-cavity, lbm-annular-couette-control, lbm-cylinder-re20)
- [Isothermal lattice BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bgk-en) (`bgk`; taylor-green, lbm-shear, channel-poiseuille, lid-driven-cavity, lbm-annular-couette-control, lbm-cylinder-re20)

#### Problem figures (`method-problems-en`)

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) (`taylor-green`)

![Stored Taylor–Green velocity and pressure fields.](https://hrkoyama.github.io/numerical-methods-atlas/assets/field-taylor-green.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#code-en)

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) (`lbm-taylor-green`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.

##### [Viscous decay of a periodic shear wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en) (`lbm-shear`)

![Stored shear amplitudes and viscous-decay reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/lbm-shear.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en) (`channel-poiseuille`)

![Stored half-way-wall Poiseuille velocity profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/channel-poiseuille.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then formsu=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) (`lbm-cavity-re100`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.

##### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/results/lbm-annular-couette-control-preview.png)

Three-point quadratic interpolation on the reflected characteristic: twointerior outgoing samples forq<.5,oneinterior incoming sample forq>.5,exacthalfway atq=.5. Record movingwall correction,actual force/torque andnonzero wallmass; nofloor ormassrepair.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#code-en)

- [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en) (`lbm-annular-couette-control`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.

##### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`)

![Actual saved2Dfields anddiagnostics fromfixedinputs; reference,boundary anderror scopesaredeclaredinthecase.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/results/lbm-cylinder-re20-preview.png)

StandardBGK,true-circle quadratic links,halfwaychannelwalls,nonperiodic openstreaming. Setall9outlet populations tofeq(1,ua)+fa−feq(rhoa,ua); ledgerchanges include theknown6. Evolve fromaPoiseuille pressureguess; normalizeactual momentumexchange bymean speed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#code-en)

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en) (`lbm-cylinder-re20`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en#references-en) (`taylor-green`)

- [Viscous flow / 2D Taylor–Green](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-taylor-green-en) (`taylor-green`; Related-model reference; Analytic reference)

The analytic model shares ν=0.1 and periodic [0,2π]², but the card displays an x-slice at y=π/4, not full 2D velocity/pressure or mesh-error arrays.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=taylor-green)

- [LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-taylor-green-en) (`lbm-taylor-green`; Related-model reference; Analytic reference)

Periodic[0,2pi)²,nu.1,baseU.2,N24/32/64,dt=.2dx²,tau.56,T=.2pi²and144/256/1024steps. Add N32/U.4,.8andN32/U.2/dt=.1dx²/tau.53/512steps. Use pressure-consistent initial density.

[Existing reference profile](/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en#lbm-taylor-green-en-measurements)

##### [Viscous decay of a periodic shear wave](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-shear/?lang=en#references-en) (`lbm-shear`)

- [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-heat-en) (`sine-heat`; Related-model reference; Analytic reference)

Linear viscous shear decay and scalar heat modes have the same form, but LBM lattice units, wavenumber and viscosity differ from the card’s ν=0.02.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

##### [Plane Poiseuille channel flow](https://hrkoyama.github.io/numerical-methods-atlas/problems/channel-poiseuille/?lang=en#references-en) (`channel-poiseuille`)

- [Viscous channel / Poiseuille](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-poiseuille-en) (`poiseuille`; Related-model reference; Analytic reference)

Both have parabolic profiles, but the computation uses lattice height ny and forcing for peak speed 0.01; the card uses unit width, G=1 and ν=0.1.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=poiseuille)

##### [Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#references-en) (`lid-driven-cavity`)

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference; Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

[Existing reference profile](/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-measurements)

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference; Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.

[Existing reference profile](/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en#lbm-cavity-re100-en-measurements)

##### [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en#references-en) (`lbm-annular-couette-control`)

- [Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-annular-couette-control-en) (`lbm-annular-couette-control`; Same-problem reference; Analytic reference)

Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T.

[Existing reference profile](/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en#lbm-annular-couette-control-en-measurements)

##### [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en#references-en) (`lbm-cylinder-re20`)

- [Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cylinder-re20-en) (`lbm-cylinder-re20`; Same-problem reference; Finite-grid numerical reference)

Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

[Existing reference profile](/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en#lbm-cylinder-re20-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/lattice-boltzmann/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity (`lbm-taylor-green`)

[Periodic Taylor–Green vortex](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json)

Evolve a nonlinear periodic2D vortex and save velocity/pressure/energy errors against the continuous analytic field. Distinguish amplitude probes from a fixed-grid coupled-step probe.

##### LBM Re100 cavity: actual2D fields and Ghia centerlines (`lbm-cavity-re100`)

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cavity-re100/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/atlas-lbm-cavity-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/verification.json)

Advance genuine four-wall BGK flow on three fixed grids, checking nominal-lid Ghia centerlines, primary vortex, stationarity and wall momentum budgets.

##### Curved LBM annular Couette control: velocity,pressure andtorque (`lbm-annular-couette-control`)

[Curved LBM annular Couette control: velocity,pressure andtorque](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-annular-couette-control/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-annular-couette-control/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/atlas-lbm-annulus-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/verification.json)

Compare true-circle quadratic Lagrange link interpolation andstair halfway against analytic rotating-inner-wall Navier–Stokes flow; anadditional control distinct fromcylinderwake.

##### Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet (`lbm-cylinder-re20`)

[Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet](https://hrkoyama.github.io/numerical-methods-atlas/problems/lbm-cylinder-re20/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-cylinder-re20/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/atlas-lbm-curved-boundary-2026-11-24.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/verification.json)

Evolve the full-length original2D-1channel andoff-center cylinder on twogrids,checking drag,lift,surface pressure difference,recirculation length andstationarity.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Additional fixed examples: LBM Re100 cavity: actual2D fields and Ghia centerlines. See each release for assumptions and checked scope. Three finite-Mach educational grids. Ghia is a rounded independent numerical reference, not exact. No pointwise corner order/high-Re claim or borrowed success from another cavity solver. A standard C++17compiler is required. Additional fixed examples: LBM Taylor–Green vortex: coupled grid/time/Mach sensitivity. See each release for assumptions and checked scope. Diffusive scaling couples grid,time andMach; amplitude changesRe. No isolated spatial/time/Mach order or exact incompressibility atfiniteMach. Kinetic equilibrium-startup transients remain part of the measured errors. Additional fixed examples: Curved LBM annular Couette control: velocity,pressure andtorque. See each release for assumptions and checked scope. Fixedcircles andslowrotation only. Negative quadratic coefficients preclude a general positivity/stability guarantee; report actual interpolation massnonconservation. Prior linear attemptfailed pressure.617757>.08 andisretained; no radial-average substitution. No changing-solid topology orsubstitute forcylinderflow. Retain the failedquadraticN80pressure.352758>.08;refinebothboundariesatfixedUi/tau/T. Additional fixed examples: Actual LBM cylinderRe20: Schäfer–Turek geometry anddeclared outlet. See each release for assumptions and checked scope. Originalpp3/7allow selectingoutflow. AdoptedNEEis independently derived finite reservoir,not claimed exactunread authorimplementation orFEATflowdo-nothing. Nabhvaluesarenotexact adopted-BCtruth andoriginalrangesarenotrigorousenclosures. Retain failedlinear/Zou–Heattempt(outlet-nearstep265). FiniteMach/BC/curveerrors;nogeneralaccuracyguarantee.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/lattice_boltzmann.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/run.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/history/attempt-01-pytest-teardown-failure/source/run.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/history/lifecycle-r1-unexecuted/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/attempt-01-energy-failure/source/run.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/history/lifecycle-r1-unexecuted/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-01-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-history-and-execution/proposal-02-unexecuted/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/check_components.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/check_components.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/qualification/component-proposal-and-review/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/run.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/check_repair.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/check_repair.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/curved-boundary-87/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/check_refinement.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/check_refinement.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/qualification/new-mesh-29/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/run.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/analytic.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/diagnostics.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/experiments.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/evolution.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/evolution.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/check_repair.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/check_repair.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/curved-boundary-87/source/reference_step.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/execute-once.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/execute-once.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/check_refinement.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/check_refinement.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/geometry.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/geometry.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/kernel.cpp](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/kernel.cpp)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/native.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/native.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/reference_step.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/qualification/new-mesh-29/source/reference_step.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_new_models.py)
- [/code/validated-examples/2026-11-24/lbm-cavity/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-cavity/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-annulus/test_lbm.py)
- [/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-curved-boundary/test_lbm.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_new_models.py
```
