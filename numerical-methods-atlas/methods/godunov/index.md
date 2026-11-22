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
