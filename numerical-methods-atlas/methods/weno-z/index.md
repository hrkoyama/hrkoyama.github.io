# FD WENO5-Z / 有限差分WENO5-Z

Status: educational-example

A WENO method targeting fifth-order spatial accuracy in smooth regions while adapting stencil weights near discontinuities. The released Euler example is pointwise finite-difference WENO-Z with global Lax–Friedrichs flux splitting and SSPRK3.

滑らかな領域では5次の空間近似を狙い、不連続付近では非線形重みでステンシルの寄与を調整するWENO法。公開Euler例は点値の有限差分WENO-Zで、大域LF流束分割とSSPRK3を用いる。

Fifth order refers to smooth-region spatial accuracy; time accuracy is third order. The same order is not expected near discontinuities, and ε, scaling and basis matter. Invalid stages trigger step halving and retries, which do not constitute a positivity theorem. The WENO branch uses neither HLLC nor the positive-reconstruction scaling used by the finite-volume PPM/MUSCL branch.

Other names: WENO-Z, WENO5Z, WENO-Z法, WENO, WENO法, WENOスキーム


## 条件と確認範囲 (ja)

problem: 滑らかな波と衝撃波を併せ持つ1次元Euler流の空間流束微分。

variant: reconstruction.pyのweno-z: p=2のWENO-Z重み、点値FD、大域LF分割、界面固定特性基底（既定）、SSPRK3。

use_when:
- 一様格子上で滑らかな解の高次空間精度と不連続の捕獲を比較したい。
- 点値とセル平均を区別し、ε・CFL・特性投影の選択を管理できる。

avoid_when:
- 一般の非構造格子や多次元、保証付きの真空処理が必要。
- セル平均を入力する有限体積WENOと、この点値FD実装を同一視して使いたい。

assumptions [specified]:
- 対象は1次元・一様Cartesian格子の理想気体Eulerで、各段階に有限かつ正の密度・圧力を要する。
- qはセル平均ではなく点値。大域波速a=max|u±c|でf±=(f±a q)/2に分け、正負の流束に逆向きの5点ステンシルを使う。
- 重みはd=(0.1,0.6,0.3)、Jiang–Shuのβ_k、τ_5=|β_0−β_2|、α_k=d_k[1+(τ_5/(ε+β_k))²]。既定ε=10^-6。
- 既定は界面で固定したRoe特性基底で両流束を投影し、成分別も選べる。時間積分はSSPRK(3,3)、入力CFLは0<CFL≤0.5。
weno_left・weno_flux・solve_eulerの係数と表現を確認。

units [specified]:
公開例は無次元Euler量。一般の単位を使う場合、βとτは投影した流束の2乗の尺度を持つため、固定ε=10^-6の効果も変わる。状態・流束の無次元化または尺度に合うεを検討する。Δt・Δx・波速の単位は整合させる。
βとτの式、固定εから尺度依存性を明記。

boundary_conditions [specified]:
reconstruction._padで周期、端点初期値固定、または端値外挿のゴースト値を使う。境界での一様な高次精度や無反射性は保証しない。
同モジュールのゴースト値分岐を確認。

limitations [specified]:
5次は滑らかな領域での空間精度であり、時間は3次。不連続近傍で同じ次数は期待できず、ε・尺度・基底の影響を受ける。段階で非正値になると時間刻みを半減して再試行するが、これは正値性の定理ではない。WENO分岐はHLLCを使わず、有限体積PPM/MUSCL用の正値再構成スケーリングも使わない。
FD/FV、空間/時間次数、再試行/正値保証を区別。

Review: reconstruction.pyのweno_left・weno_flux・euler_eigenbasis・solve_eulerを読んだ。既存test_reconstruction.pyの滑らかな流束微分次数、一定解、周期総量、Sod・移動接触、基底の逆変換テストを確認。数値再実行なし。

Not checked:
- WENO-Z原報全文と局所係数の逐式比較、原論文全テストの再現。
- 今回の再実行、すべての臨界点・境界での5次精度、一般の正値性保証。

Evidence:
- weno_left; weno_flux; euler_eigenbasis; solve_euler; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py
- test_weno_constant_and_smooth_spatial_flux_derivative; test_uniform_state_and_periodic_primary_conservation; test_sod_and_moving_contact; test_characteristic_basis_inverts_and_diagonalizes_euler_flux: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py

References:
- [original-method / primary-research] Borges, Carmona, Costa & Don (2008). An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. — https://doi.org/10.1016/j.jcp.2007.11.038
  WENO-JSの滑らかさ指標から重みを改良する有限差分WENO-Zの原報。p、ε、流束分割、特性投影、時間積分の採用値は本サイトのコードを根拠にする。
  abstract-and-metadata (2026-11-22); Publisher-indexed article preview: abstract and bibliographic record; PDF fetch returned 403, so no full-text claim.; https://www.sciencedirect.com/science/article/pii/S0021999107005232/pdfft?md5=cfc2cfb9543e13a4d128bd4b3ed2260d&pid=1-s2.0-S0021999107005232-main.pdf
- [adopted-variant / primary-research] Shu & Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. — https://doi.org/10.1016/0021-9991(88)90177-5
  流束ベースの構成とTVD Runge–Kutta時間離散化に関する一次文献。ここで用いる3段3次の係数は公開コードで確認した。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; full tableau not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999188901775
- [reference-solution / primary-research] Sod (1978). A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. — https://doi.org/10.1016/0021-9991(78)90023-2
  Sod衝撃波管という比較課題の出典。参照値は本サイトの非真空・理想気体Riemann解評価器で求め、論文表を転記した値とは区別する。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; detailed initial-state tables not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999178900232

## Conditions and review scope (en)

problem: Approximate spatial flux derivatives for one-dimensional Euler flows containing both smooth waves and shocks.

variant: weno-z in reconstruction.py: p=2 WENO-Z weights, pointwise FD, global LF splitting, face-frozen characteristic projection by default, and SSPRK3.

use_when:
- Compare smooth-solution high-order spatial accuracy with discontinuity capture on a uniform grid.
- Point values and cell averages can be distinguished, and ε, CFL and characteristic projection can be controlled.

avoid_when:
- General unstructured meshes, multiple dimensions or guaranteed vacuum treatment are required.
- A finite-volume WENO accepting cell averages is required instead of this pointwise FD implementation.

assumptions [specified]:
- The scope is one-dimensional perfect-gas Euler on a uniform Cartesian grid, with finite positive density and pressure at each stage.
- q contains point values, not cell averages. A global a=max|u±c| splits f±=(f±a q)/2; oppositely biased five-point stencils reconstruct the two fluxes.
- Weights use d=(0.1,0.6,0.3), Jiang–Shu β_k, τ_5=|β_0−β_2| and α_k=d_k[1+(τ_5/(ε+β_k))²], with default ε=10^-6.
- Both split fluxes use the same face-frozen Roe characteristic basis by default; component reconstruction is optional. Time integration is SSPRK(3,3), with 0<CFL≤0.5.
Inspected coefficients and data representation in weno_left, weno_flux and solve_euler.

units [specified]:
Released Euler examples are nondimensional. With dimensional data, β and τ scale as the squared projected flux, so the effect of a fixed ε=10^-6 changes with scaling. Nondimensionalize states/fluxes or choose a scale-consistent ε. Use compatible units for Δt, Δx and wave speed.
Scaling dependence follows from β/τ formulae and the fixed ε.

boundary_conditions [specified]:
reconstruction._pad uses periodic ghosts, fixed initial endpoint states or edge extrapolation. Uniform high-order boundary accuracy and nonreflection are not guaranteed.
Inspected the module's ghost-state branches.

limitations [specified]:
Fifth order refers to smooth-region spatial accuracy; time accuracy is third order. The same order is not expected near discontinuities, and ε, scaling and basis matter. Invalid stages trigger step halving and retries, which do not constitute a positivity theorem. The WENO branch uses neither HLLC nor the positive-reconstruction scaling used by the finite-volume PPM/MUSCL branch.
Separates FD/FV, spatial/time order and retry logic/positivity guarantees.

Review: Read weno_left, weno_flux, euler_eigenbasis and solve_euler in reconstruction.py. Inspected existing tests for smooth flux-derivative order, constant states, periodic totals, Sod/moving contacts and eigenbasis inversion. No numerical rerun was performed.

Not checked:
- Full-text comparison of all local coefficients with the WENO-Z paper, or reproduction of all its experiments.
- New runs, fifth-order accuracy at every critical point/boundary or a general positivity proof.

Evidence:
- weno_left; weno_flux; euler_eigenbasis; solve_euler; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py
- test_weno_constant_and_smooth_spatial_flux_derivative; test_uniform_state_and_periodic_primary_conservation; test_sod_and_moving_contact; test_characteristic_basis_inverts_and_diagonalizes_euler_flux: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py

References:
- [original-method / primary-research] Borges, Carmona, Costa & Don (2008). An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. — https://doi.org/10.1016/j.jcp.2007.11.038
  Original finite-difference WENO-Z paper. Its abstract establishes the weight-improvement lineage; local numerical choices are documented from the released code.
  abstract-and-metadata (2026-11-22); Publisher-indexed article preview: abstract and bibliographic record; PDF fetch returned 403, so no full-text claim.; https://www.sciencedirect.com/science/article/pii/S0021999107005232/pdfft?md5=cfc2cfb9543e13a4d128bd4b3ed2260d&pid=1-s2.0-S0021999107005232-main.pdf
- [adopted-variant / primary-research] Shu & Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes. — https://doi.org/10.1016/0021-9991(88)90177-5
  Primary source for TVD Runge–Kutta time discretization and flux-based construction. The atlas three-stage third-order coefficients were checked in code.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; full tableau not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999188901775
- [reference-solution / primary-research] Sod (1978). A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. — https://doi.org/10.1016/0021-9991(78)90023-2
  Benchmark provenance for the Sod shock tube. Atlas reference values come from its non-vacuum ideal-gas Riemann evaluator, rather than transcribed paper tables.
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; detailed initial-state tables not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999178900232


- Reading (ja): https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/
- Reading (en): https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/

- Code: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py

- Reference: https://doi.org/10.1016/j.jcp.2007.11.038 — Original WENO-Z finite-difference scheme; p=2, epsilon, flux splitting, characteristic projection and time integration are separately identified from the atlas implementation.
- Reference: https://doi.org/10.1016/0021-9991(88)90177-5 — Primary source for TVD Runge–Kutta time discretization and flux-based ENO construction; the local SSPRK(3,3) coefficients are independently visible in code.
- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Historical shock-tube comparison used as a benchmark source. The atlas reference is its own non-vacuum ideal-gas Riemann evaluator, with a bracketed numerical pressure solve.

Common execution records: [{"id": "shu-osher", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#shu-osher-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#shu-osher-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
