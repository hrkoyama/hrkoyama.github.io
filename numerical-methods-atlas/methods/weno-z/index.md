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

## Small fixed-input validation supplements

Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects.

セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。

- WENO-JS/Z: fixed critical-point and epsilon comparison: https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/

Download: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip
Verification: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/results/result.json

Common execution records: [{"id": "shu-osher", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#shu-osher-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#shu-osher-en"}}, {"id": "weno-critical-epsilon", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/validation/releases.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en"}, "kind": "dedicated-supplement"}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/weno-z/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/

## 手法に関連する方程式・図・参照・コード / Method equations, figures, references and code

### 日本語

#### 方程式 (`method-equations-ja`)

問題から導かれた対応です。検証範囲は各問題の入力・境界条件に従います。

- [線形移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja) (`linear-advection`; advection-sine)
- [圧縮性Euler方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja) (`euler`; shu-osher, moving-contact)

#### 問題の図 (`method-problems-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) (`advection-sine`)

![保存済みのCIP・線形補間・厳密な移流波形。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。 p+1個のGauss解点、上流数値流束、Legendre多項式によるRadau左右補正、SSPRK(3,3)。初期L2射影・上流流束・時間刻み規約をバイト一致の既存modal DGと揃えます。スケールしたCourant数(2p+1)|a|Δt/h≤.15。最後にp2/N32で刻みを半減。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#code-ja)

- [WENO-JS／Z：臨界点とεの固定比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) (`weno-critical-epsilon`) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

##### [Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

- [Shu–Osher：特性WENO-Zと高解像度参照](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja) (`shu-osher`) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。

##### [移動接触不連続](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja) (`moving-contact`)

![保存したEuler密度波形（1つの手法を代表表示）。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

[この問題の参照・検証資料](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#references-ja) · [この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#code-ja)

この手法でこの問題を解く固定入力実行例は未登録です。


#### 厳密解・参照解 (`method-references-ja`)

##### [周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja#references-ja) (`advection-sine`)

- [移流／正弦波の平行移動](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-advection-ja) (`sine-advection`; 関連モデルの参照; 解析参照)

同じ周期・速度1の正弦移流モデルです。参照一覧は振幅0.25、共通固定入力は0.2で、DG・CIP等の表現や時間も異なります。

[既存の参照図](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-advection)

- [WENO臨界点：多項式セル平均と解析的周期輸送](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-weno-critical-profile-ja) (`weno-critical-profile`; 関連モデルの参照; 解析参照)

同じ一定速度の周期移流に対する追加参照ですが、cos+.1sin³のセル平均と局所臨界多項式は、従来の単一正弦・CIP表示と異なります。

[既存の参照図](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja#weno-critical-epsilon-ja-measurements)

- [FRとDGの周期正弦移流：平均0.4・T=.25の解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fr-periodic-advection-ja) (`fr-periodic-advection`; 同じ問題の参照; 解析参照)

全て無次元。u_t+u_x=0、区間[0,1)、周期境界、初期値0.4+sin(2πx)。解析解は0.4+sin(2π(x−t))。一定の正速度1、均一なアフィン区間要素。

[既存の参照図](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=ja)

##### [Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#references-ja) (`shu-osher`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### [移動接触不連続](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=ja#references-ja) (`moving-contact`)

参照解一覧の対応カードは未登録です。問題ごとの参照・検証資料に、解析的基準・数値参照・保存則などの確認範囲を示します。

##### 手法の解説・独立参照・保存結果

資料ごとの役割と適用条件・照合方法を確認してください。

- 解説: [手法の解説・条件](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/reconstruction/)


#### コード・検証 (`method-execution-ja`)

問題図に対応する実行例と、既存配布版・関連ソースを区別します。

##### WENO-JS／Z：臨界点とεの固定比較 (`weno-critical-epsilon`)

[周期正弦波の線形移流](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

同じセル平均からのWENO5再構成と実際の周期輸送で、JS重みとZ二乗重みを比較します。3種類の臨界性、3種類のε、固定格子と時間刻み半減を分けて保存します。

##### Shu–Osher：特性WENO-Zと高解像度参照 (`shu-osher`)

[Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) · [実行・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=ja) · [コードZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[固定入力](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json)

[検証記録](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

[-5,5]で衝撃波と密度正弦波の干渉をt=1.8まで計算。100/200点の特性FD WENO-Zを800点の同じ実装と比較し、参照との差と近似境界収支を別々に記録する。

##### 既存の配布版・関連ソースと検査

共用モジュールや配布版全体の検査を含み、すべてが個々の問題専用とは限りません。

セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### 関連ソース

- [/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py)
- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)

###### 配布版のテスト

- [/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)

配布版の案内で条件と作業フォルダを確認してください。複数例の検査や図生成を含む場合があります。

```sh
python -m pytest -q tests/test_reconstruction.py
```


### English

#### Equations (`method-equations-en`)

These links are derived through associated problems; checked scope follows their inputs and boundaries.

- [Linear advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#linear-advection-en) (`linear-advection`; advection-sine)
- [Compressible Euler equations](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#euler-en) (`euler`; shu-osher, moving-contact)

#### Problem figures (`method-problems-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) (`advection-sine`)

![Stored CIP, linear-interpolation and exact advection profiles.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/advection-sine.png)

Methods explicitly bound to this problem by the common fixed-input execution example. Inspect its input for differences from the figure’s conditions. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects. p+1 Gauss solution points, upwind interface flux, Legendre Radau corrections and SSPRK(3,3). Match initial L2 projection, upwind flux and timestep policy to the unchanged published modal DG. Scaled Courant(2p+1)|a|dt/h<=.15; separately halve the timestep at p2/N32.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#code-en)

- [WENO-JS/Z: fixed critical-point and epsilon comparison](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) (`weno-critical-epsilon`) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

##### [Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) (`shu-osher`)

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/shu-osher.png)

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#code-en)

- [Shu–Osher: characteristic WENO-Z and a numerical reference](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en) (`shu-osher`) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.

##### [Moving contact discontinuity](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en) (`moving-contact`)

![Stored Euler density profile, showing one representative method.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/moving-contact.png)

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

[This problem’s references and checks](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#references-en) · [This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#code-en)

No fixed-input execution of this problem is registered for this method.


#### Exact / reference solutions (`method-references-en`)

##### [Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en#references-en) (`advection-sine`)

- [Advection / sine translation](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-sine-advection-en) (`sine-advection`; Related-model reference; Analytic reference)

Same periodic sine-transport model at speed one. The library amplitude is 0.25 versus 0.2 in the common fixed input; DG/CIP representations and output times also differ.

[Existing reference profile](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-advection)

- [WENO critical points: polynomial cell means and analytic periodic transport](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-weno-critical-profile-en) (`weno-critical-profile`; Related-model reference; Analytic reference)

An additional constant-speed periodic-transport reference. The cos+.1sin³ cell means and local critical polynomials differ from the historical single-sine/CIP display.

[Existing reference profile](/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en#weno-critical-epsilon-en-measurements)

- [FR/DG periodic sine advection: analytic reference at mean0.4 andT=.25](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-fr-periodic-advection-en) (`fr-periodic-advection`; Same-problem reference; Analytic reference)

Dimensionless u_t+u_x=0 on[0,1), periodic boundary, initial0.4+sin(2pi x), analytic0.4+sin(2pi(x-t)). Constant positive speed1 and uniform affine intervals.

[Existing reference profile](/numerical-methods-atlas/validation/fr-periodic-advection/?lang=en)

##### [Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en#references-en) (`shu-osher`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### [Moving contact discontinuity](https://hrkoyama.github.io/numerical-methods-atlas/problems/moving-contact/?lang=en#references-en) (`moving-contact`)

No corresponding reference-library card is registered. The problem’s references and checks describe its analytic standards, numerical references or conservation checks.

##### Method explanations, independent references and saved results

Check each resource’s role, applicable conditions and comparison procedure.

- Explanation: [Method explanation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/en/read/reconstruction/)


#### Code and validation (`method-execution-en`)

Matched problem executions are separate from existing editions and related source.

##### WENO-JS/Z: fixed critical-point and epsilon comparison (`weno-critical-epsilon`)

[Periodic sine-wave advection](https://hrkoyama.github.io/numerical-methods-atlas/problems/advection-sine/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/validation/weno-critical-epsilon/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/atlas-weno-critical-2026-11-23.zip)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/inputs.json)

[Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/verification.json)

Compare WENO5 JS and Z power-two weights from the same cell means, then evolve actual periodic transport. Retain three regularity classes, three epsilon choices, fixed grids and separate halved-time-step diagnostics.

##### Shu–Osher: characteristic WENO-Z and a numerical reference (`shu-osher`)

[Shu–Osher shock/entropy interaction](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=en) · [Run and validate](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/shu-osher/?lang=en) · [Code ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip)

[Fixed input](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/shu-osher.json)

[Verification receipt](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json)

Evolve shock/entropy-wave interaction on [-5,5] to t=1.8. Compare characteristic FD WENO-Z at 100/200 points with the same implementation at 800 points, separately recording reference disagreement and approximate boundary balance.

##### Existing editions, related source and tests

Includes shared modules and package-wide checks; these resources are not all dedicated to individual problems.

Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects.

Scoped fixed-input examples; original method variants and earlier releases remain distinct.

[Related code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

###### Related source

- [/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/reconstruction.py)
- [/code/validated-examples/2026-11-23/weno-critical/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/run.py)
- [/code/validated-examples/2026-11-23/weno-critical/weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/weno.py)
- [/code/validated-examples/2026-11-23/weno-critical/references/analytic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/references/analytic.py)

###### Package tests

- [/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_reconstruction.py)
- [/code/validated-examples/2026-11-23/weno-critical/test_weno.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/weno-critical/test_weno.py)

Consult the edition’s guide for conditions and working directory; commands may check or generate figures for several cases.

```sh
python -m pytest -q tests/test_reconstruction.py
```
