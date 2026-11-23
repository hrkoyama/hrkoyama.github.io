# Godunov-type finite volumes / Godunov型有限体積法

Status: educational-example

A finite-volume baseline using a local Riemann problem at each interface. The released example combines piecewise-constant spatial reconstruction, an approximate flux and SSPRK3, enabling comparison with higher-order solvers on Sod's problem.

保存則の各界面を局所Riemann問題として扱う有限体積の基準法。公開例は区分一定の空間再構成に近似流束とSSPRK3を組み合わせ、Sod問題で高次法との差を比較する。

First-order spatial reconstruction smears shocks and contacts. This is not the original one-step exact-Riemann algorithm, and third-order time stepping does not raise its spatial order. Results depend on the approximate flux, sampled initialization and boundary treatment. Vacuum, wet/dry fronts, general equations of state, multiple dimensions, and general positivity/entropy guarantees are outside scope.

Other names: Godunov法, Godunov method, Godunov scheme, ゴドノフ法, ゴドゥノフ法


## 条件と確認範囲 (ja)

problem: 圧縮性流体など、衝撃波を含む1次元保存則の時間発展。

variant: solvers.solveのmethod='godunov': 区分一定状態＋選択した近似Riemann流束＋SSPRK(3,3)。既定Euler流束はHLLC。

use_when:
- 高次再構成の効果を測る、保守的な空間1次の比較基準が欲しい。
- 実装範囲内の1次元モデルで、波速に応じた時間刻みを選べる。

avoid_when:
- 接触面や滑らかな波を少ないセルで高精度に保ちたい。
- 真空・乾燥・複雑な境界を、この基準solverだけで保証付きに扱いたい。

assumptions [specified]:
- 対象は1次元・一様Cartesian格子上の双曲型保存則で、各方程式に整合する流束を選ぶ。
- Eulerでは理想気体、正の密度・圧力を前提とし、HLLC等を選べる。浅水・等温モデルにはHLLまたはRusanovを選ぶ。
- 公開solve(...,method='godunov')は傾きを0にし、SSPRK(3,3)で時間積分する。初期値は格子点でのサンプルをセル値として与える。
- 公開solverが受け付けるCFLは0<CFL≤0.5。この上限だけで任意の入力の正値性を保証するものではない。
solveの再構成分岐、対応モデル、CFL検査を確認。

units [specified]:
方程式ごとの保存変数と流束に一貫した単位を使う。Eulerでは密度ρ、運動量密度ρu、全エネルギー密度Eで、流束の単位は各保存量×長さ/時間。公開衝撃波管は無次元。
equations.pyの保存変数・物理流束で定義。

boundary_conditions [specified]:
公開_padは周期、端点初期値固定、または端値の外挿でゴースト値を作る。外挿は厳密な無反射条件ではなく、反射壁や一般の流入条件は実装していない。非周期領域の総量変化には境界流束が入る。
_padの3つの分岐を確認。

limitations [specified]:
空間1次なので衝撃波や接触面が広がる。原報の厳密Riemann解を用いる1段更新そのものではなく、時間3次でも全体の空間精度は1次のまま。近似流束・初期値の点サンプル・境界処理の選択に依存し、真空、乾湿境界、一般EOS、多次元および一般的な正値性・エントロピー保証は対象外。
空間再構成と時間積分を分け、原法との差を明記。

Review: solvers.pyのsolve・rk3・_pad、equations.pyのEuler/Barotropic、riemann.pyの近似流束とexact_eulerを読んだ。test_sod_accuracy_and_refinementのgodunov分岐と参照Riemann値のテストを確認。実行や原論文の数値表の再現はしていない。

Not checked:
- Godunov原報のロシア語本文、原法との逐式比較。
- 新しい再実行、全流束・全モデルでの収束証明、真空・乾湿境界。

Evidence:
- solve(method='godunov'); rk3; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Euler; Barotropic: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- numerical_flux; exact_euler: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- test_sod_accuracy_and_refinement; test_exact_sod_star_and_regions: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [original-method / primary-research] Godunov (1959). A difference method for numerical calculation of discontinuous solutions of the equations of hydrodynamics. — https://www.mathnet.ru/eng/sm4873
  Godunov法の原報。今回確認したのは原誌の書誌であり、局所実装の時間積分・近似流束を原報と同一とは扱わない。
  metadata (2026-11-22); Journal archive bibliographic record; Russian full text not reviewed.; https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=sm&paperid=4873&option_lang=eng
- [adopted-variant / primary-research] Shu & Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. — https://doi.org/10.1016/0021-9991(88)90177-5
  流束ベースの構成とTVD Runge–Kutta時間離散化に関する一次文献。ここで用いる3段3次の係数は公開コードで確認した。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; full tableau not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999188901775
- [original-method / primary-research] Toro, Spruce & Speares (1994). Restoration of the contact surface in the HLL-Riemann solver. — https://doi.org/10.1007/BF01414629
  HLL近似解へ接触波を復元する考え方の原報。論文中の各波速推定やWAF計算をすべて再現したという意味ではない。
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic record; full text not reviewed.; https://link.springer.com/article/10.1007/BF01414629
- [reference-solution / primary-research] Sod (1978). A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. — https://doi.org/10.1016/0021-9991(78)90023-2
  Sod衝撃波管という比較課題の出典。参照値は本サイトの非真空・理想気体Riemann解評価器で求め、論文表を転記した値とは区別する。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; detailed initial-state tables not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999178900232

## Conditions and review scope (en)

problem: Time evolution of one-dimensional conservation laws, including shocks in compressible flow.

variant: method='godunov' in solvers.solve: piecewise-constant states, a selected approximate Riemann flux and SSPRK(3,3). HLLC is the default Euler flux.

use_when:
- A conservative first-order spatial baseline is needed to measure the effect of higher-order reconstruction.
- A supported one-dimensional model can be stepped according to its wave speeds.

avoid_when:
- Contacts or smooth waves must remain highly accurate on a coarse mesh.
- Vacuum, dry states or complex boundaries require guarantees absent from this baseline solver.

assumptions [specified]:
- The scope is one-dimensional hyperbolic conservation laws on a uniform Cartesian grid with a model-compatible numerical flux.
- Euler assumes a perfect gas and positive density/pressure; HLLC and other Euler fluxes are available. Shallow-water and isothermal models require HLL or Rusanov in this solver.
- solve(...,method='godunov') sets reconstruction slopes to zero and advances with SSPRK(3,3). Initial data are sampled at grid locations and used as cell values.
- The released solver requires 0<CFL≤0.5; this bound alone is not a positivity guarantee for arbitrary inputs.
Inspected reconstruction branches, model restrictions and CFL checks in solve.

units [specified]:
Use units consistent with each model's conserved variables and fluxes. Euler uses density ρ, momentum density ρu and total energy density E; each flux has its conserved-variable unit times length/time. Released shock tubes are nondimensional.
Specified from conserved variables and physical fluxes in equations.py.

boundary_conditions [specified]:
The released _pad supplies periodic ghosts, fixed initial endpoint states, or edge extrapolation. Extrapolation is not an exact nonreflecting condition; reflecting walls and general inflow conditions are not implemented. Boundary fluxes contribute to global balances on nonperiodic domains.
Inspected the three _pad branches.

limitations [specified]:
First-order spatial reconstruction smears shocks and contacts. This is not the original one-step exact-Riemann algorithm, and third-order time stepping does not raise its spatial order. Results depend on the approximate flux, sampled initialization and boundary treatment. Vacuum, wet/dry fronts, general equations of state, multiple dimensions, and general positivity/entropy guarantees are outside scope.
Distinguishes spatial reconstruction, time integration and the historical algorithm.

Review: Read solve, rk3 and _pad in solvers.py, Euler/Barotropic in equations.py, and the approximate-flux and exact_euler functions in riemann.py. Inspected the Godunov branch of test_sod_accuracy_and_refinement and reference-Riemann tests. No tests were rerun and no paper tables reproduced.

Not checked:
- Russian full text and equation-by-equation comparison with the original Godunov method.
- New numerical runs, convergence proofs for every flux/model combination, vacuum or wet/dry fronts.

Evidence:
- solve(method='godunov'); rk3; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Euler; Barotropic: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- numerical_flux; exact_euler: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- test_sod_accuracy_and_refinement; test_exact_sod_star_and_regions: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [original-method / primary-research] Godunov (1959). A difference method for numerical calculation of discontinuous solutions of the equations of hydrodynamics. — https://www.mathnet.ru/eng/sm4873
  Original paper for the Godunov method; its journal record was checked. The atlas uses a separately specified time integrator and approximate flux.
  metadata (2026-11-22); Journal archive bibliographic record; Russian full text not reviewed.; https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=sm&paperid=4873&option_lang=eng
- [adopted-variant / primary-research] Shu & Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. — https://doi.org/10.1016/0021-9991(88)90177-5
  Primary source for TVD Runge–Kutta time discretization and flux-based construction. The atlas three-stage third-order coefficients were checked in code.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; full tableau not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999188901775
- [original-method / primary-research] Toro, Spruce & Speares (1994). Restoration of the contact surface in the HLL-Riemann solver. — https://doi.org/10.1007/BF01414629
  Primary source for restoring the contact wave missing from HLL. Its complete wave-speed alternatives and WAF experiments were not audited.
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic record; full text not reviewed.; https://link.springer.com/article/10.1007/BF01414629
- [reference-solution / primary-research] Sod (1978). A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. — https://doi.org/10.1016/0021-9991(78)90023-2
  Benchmark provenance for the Sod shock tube. Atlas reference values come from its non-vacuum ideal-gas Riemann evaluator, rather than transcribed paper tables.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; detailed initial-state tables not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999178900232


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py
- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py

- Reference: https://www.mathnet.ru/eng/sm4873 — Original Godunov-method source. It is not evidence that the local SSPRK3/approximate-flux implementation reproduces the original fully discrete algorithm.
- Reference: https://doi.org/10.1016/0021-9991(88)90177-5 — Primary source for TVD Runge–Kutta time discretization and flux-based ENO construction; the local SSPRK(3,3) coefficients are independently visible in code.
- Reference: https://doi.org/10.1007/BF01414629 — Original HLLC contact-restoration source; no claim that all wave-speed estimates or WAF experiments in the paper are implemented.
- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Historical shock-tube comparison used as a benchmark source. The atlas reference is its own non-vacuum ideal-gas Riemann evaluator, with a bracketed numerical pressure solve.

Common execution records: [{"id": "sod", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#sod-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#sod-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/godunov/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [非粘性Burgers方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#burgers-ja) (`burgers`; burgers-shock, burgers-fan)
- [LWR交通流モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#traffic-ja) (`traffic`; traffic-jam, traffic-fan)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; sod, double-rarefaction, double-mach)

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

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) (`sod`)

![保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#code-ja)

- [Sod衝撃波管：Godunov型更新と自己相似解](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja) (`sod`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja) (`double-rarefaction`)

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

従来のGodunov／HLLEプレビューと、追加のMUSCL・Lax–Friedrichs・平均保存スケーリング・SSPRK(3,3)固定入力は別の実行例です。段階正値性の条件は追加版の説明・契約・全段ログに限定します。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja) (`double-mach`)

![実際の2次元Euler計算の密度場。Mach10、γ=1.4、T=.2、256×64セル。保存済みの別実装FV参照への差とwall jet診断を示します。細い噴流・渦構造の収束を保証する図ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

既存のGodunov/HLL像と、新しい区分定数HLL＋Heunの固定入力を区別します。各実行例にはその計算で実際に使う手法だけを結びます。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


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

##### [Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#references-ja) (`sod`)

- [Euler／Sod問題](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja) (`euler-sod`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-sod)

##### [Euler二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=ja#references-ja) (`double-rarefaction`)

- [Euler／二重膨張波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-double-rarefaction-ja) (`euler-double-rarefaction`; 関連モデルの参照; 半解析参照)

γ=1.4、左右(1,-2,0.4)/(1,2,0.4)、[0,1]、x0=0.5、t=0.15が保存プレビューと一致します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=euler-double-rarefaction)

##### [二重Mach反射](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=ja#references-ja) (`double-mach`)

- [Double Mach反射：保存済み独立有限格子数値参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-double-mach-ja) (`double-mach`; 同じ問題の参照; 有限格子の数値参照)

以前に独立実行した2格子の有限体積参照を保存量制限で比較します。有限格子数値参照であり、厳密2D解や誤差上界ではありません。

[既存の参照図](/numerical-methods-atlas/validation/double-mach-reflection/?lang=ja#double-mach-reflection-ja-measurements)

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/benchmarks/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### Sod衝撃波管：Godunov型更新と自己相似解 (`sod`)

[Sod衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、初期不連続x=0.5、t=0.2の標準問題。80/160セルの区分一定Godunov型＋HLLC＋SSPRK3を自己相似Euler解と比較する。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

Related chapter modules and test files; not a claim that each test covers every named method.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_numerics.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Inviscid Burgers equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#burgers-en) (`burgers`; burgers-shock, burgers-fan)
- [LWR traffic model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#traffic-en) (`traffic`; traffic-jam, traffic-fan)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; sod, double-rarefaction, double-mach)

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

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) (`sod`)

![Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#code-en)

- [Sod shock tube: Godunov-type update and self-similar reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en) (`sod`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en) (`double-rarefaction`)

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/double-rarefaction.png)

The earlier Godunov/HLLE preview and the new MUSCL/Lax–Friedrichs/mean-preserving-scaling/SSPRK(3,3) run are separate execution records. Stage-positivity conditions are scoped to the additional release, its contract and all-stage diagnostics.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en) (`double-mach`)

![Density from the actual 2D Euler calculation: Mach 10, gamma = 1.4, T = 0.2, 256 × 64 cells. Differences from a saved reference computed with a separate FV implementation and wall-jet diagnostics remain visible. The picture does not establish convergence of thin jets or vortices.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/double-mach/results/double-mach-reflection-preview.png)

Distinguish the existing Godunov/HLL view from new piecewise-constant HLL plus Heun fixed inputs. Each execution links only the methods actually used in that computation.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


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

##### [Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en#references-en) (`sod`)

- [Euler / Sod](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-sod-en) (`euler-sod`; Related-model reference; Semi-analytic reference)

γ=1.4, primitive states (1,0,1)/(0.125,0,0.1), x0=0.5, [0,1] and t=0.2 match. Inspect point/conserved-cell-average sampling and error norms separately. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-sod)

##### [Euler double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-rarefaction/?lang=en#references-en) (`double-rarefaction`)

- [Euler / double rarefaction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-euler-double-rarefaction-en) (`euler-double-rarefaction`; Related-model reference; Semi-analytic reference)

γ=1.4, states (1,-2,0.4)/(1,2,0.4), [0,1], x0=0.5 and t=0.15 match the saved preview. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=euler-double-rarefaction)

##### [Double Mach reflection](https://hrkoyama.github.io/numerical-methods-atlas/problems/double-mach/?lang=en#references-en) (`double-mach`)

- [Double Mach reflection: saved independent finite-grid numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-double-mach-en) (`double-mach`; Same-problem reference; Finite-grid numerical reference)

Compare against two previously independently executed finite-volume reference grids using conservative restriction. This is a finite-grid numerical reference, not an exact2D solution or error bound.

[Existing reference profile](/numerical-methods-atlas/validation/double-mach-reflection/?lang=en#double-mach-reflection-en-measurements)

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/benchmarks/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### Sod shock tube: Godunov-type update and self-similar reference (`sod`)

[Sod shock tube](https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/sod/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/sod.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Standard γ=1.4 Sod tube with left/right (ρ,u,p)=(1,0,1)/(0.125,0,0.1), initial jump x=0.5 and t=0.2. Compare 80/160-cell piecewise-constant Godunov-type/HLLC/SSPRK3 updates with a self-similar Euler solution.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Related chapter modules and test files; not a claim that each test covers every named method.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/solvers.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/riemann.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/benchmarks.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/equations.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/equations.py)
- [/code/numerical-methods-atlas/2026-11-21/numart/advection.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/advection.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_numerics.py
```
