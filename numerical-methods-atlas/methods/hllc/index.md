# HLLC / HLLC

Status: educational-example

An approximate Riemann flux that restores the contact wave missing from HLL, improving Euler contact resolution. The released implementation is one-dimensional and perfect-gas, with Davis-type outer acoustic speeds.

HLL近似Riemann流束に接触波を加え、Euler方程式の密度接触面を捉えやすくする界面流束。公開例はDavis型の左右音響波速を用いる理想気体・1次元版である。

Contact restoration is not a general positivity or entropy-stability guarantee. This Davis-speed version should not be extended without additional treatment to strong rarefactions, vacuum, general equations of state, MHD or relativistic flow. Exact agreement for a stationary contact does not imply an exact solution for moving shocks or arbitrary problems.

Other names: HLLC法, HLLC流束, HLLC solver, HLLCリーマンソルバー


## 条件と確認範囲 (ja)

problem: セル界面の左右Euler状態から、接触波を含む近似保存流束を求める。

variant: riemann.numerical_flux(...,solver='hllc')。Davis型外側波速、左右star状態、接触波を使う理想気体Euler版。

use_when:
- 正の理想気体状態から、HLLより鮮明な密度接触面を求めたい。
- 再構成・時間積分・境界条件を別に選ぶGodunov型solverの流束部品が必要。

avoid_when:
- 真空や極端な希薄波に対して正値性の保証が必須。
- 非理想気体、浅水、MHD等のための別のHLLC定式化が必要。

assumptions [specified]:
- 左右状態は理想気体Eulerの(ρ,ρu,E)、有限かつρ>0、p>0で、物理的な比熱比γ>1を使う。
- 外側波速はS_L=min(u_L−c_L,u_R−c_R)、S_R=max(u_L+c_L,u_R+c_R)。接触速度と左右star状態を代数的に計算する。
- HLLCは界面流束であり、再構成、時間積分、CFLと境界状態は呼び出し側が与える。
- 本実装のHLLC分岐はEuler専用であり、HLLを使える他のモデルにも自動適用できるわけではない。
numerical_fluxのEuler型検査と波速・star状態の式を確認。

units [specified]:
左右で同じ単位系を使う。ρは密度、uとcと各波速は長さ/時間、pとEはエネルギー/体積。数値流束は保存量×長さ/時間の単位を持つ。γは無次元で、公開例も無次元。
Eulerの保存変数と波速の次元から指定。

boundary_conditions [not-applicable]:
界面流束そのものには物理境界条件を指定しない。呼び出し元が左右状態を作る。既存1次元solverは周期・端点初期値固定・端値外挿を用いる。
流束関数は左右状態を受け取り、境界を設定しない。

limitations [specified]:
接触波の復元は一般的な正値性・エントロピー安定性の保証ではない。このDavis型波速版を、強い希薄波・真空や一般EOS、MHD、相対論的流体に追加処理なしで用いない。静止接触の一致テストも、移動衝撃波や全問題での厳密性を意味しない。
局所の静止接触テストと一般的保証を区別。

Review: riemann.pyのnumerical_fluxのHLL/HLLC分岐、exact_eulerの非真空検査と圧力の区間二分探索を読んだ。test_flux_consistency・test_hllc_stationary_contact_is_exact・Sod参照値/精度のテストを確認。再実行なし。

Not checked:
- Toroら・Davis・Sod各論文の全文との逐式・数値表照合。
- 今回の再実行、全状態での正値性・エントロピー安定性、他の波速推定やEOS。

Evidence:
- numerical_flux HLL/HLLC branches; exact_euler: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- solve numerical_flux call; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- test_flux_consistency; test_hllc_stationary_contact_is_exact; test_exact_sod_star_and_regions; test_sod_accuracy_and_refinement: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [original-method / primary-research] Toro, Spruce & Speares (1994). Restoration of the contact surface in the HLL-Riemann solver. — https://doi.org/10.1007/BF01414629
  HLL近似解へ接触波を復元する考え方の原報。論文中の各波速推定やWAF計算をすべて再現したという意味ではない。
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic record; full text not reviewed.; https://link.springer.com/article/10.1007/BF01414629
- [adopted-variant / primary-research] Davis (1988). Simplified Second-Order Godunov-Type Methods. — https://doi.org/10.1137/0909030
  近似Riemann解の外側波速推定に関する一次文献。本実装のmin/max音響波速式はコードで確認し、原論文全式との照合は未実施。
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; wave-speed formulae in full text not reviewed.; https://epubs.siam.org/doi/10.1137/0909030
- [reference-solution / primary-research] Sod (1978). A survey of several finite difference methods for systems of nonlinear hyperbolic conservation laws. — https://doi.org/10.1016/0021-9991(78)90023-2
  Sod衝撃波管という比較課題の出典。参照値は本サイトの非真空・理想気体Riemann解評価器で求め、論文表を転記した値とは区別する。
  abstract-and-metadata (2026-11-22); Publisher-indexed abstract and bibliographic record; detailed initial-state tables not reviewed.; https://www.sciencedirect.com/science/article/pii/0021999178900232

## Conditions and review scope (en)

problem: Compute a contact-resolving approximate conservative flux from left/right Euler states.

variant: riemann.numerical_flux(...,solver='hllc'): perfect-gas Euler HLLC with Davis-type outer speeds, two star states and a contact wave.

use_when:
- Density contacts should be sharper than with HLL for positive perfect-gas states.
- A flux component is needed in a Godunov-type solver that separately selects reconstruction, time integration and boundaries.

avoid_when:
- Guaranteed positivity is required near vacuum or extreme rarefactions.
- A different HLLC formulation is needed for nonideal gases, shallow water or MHD.

assumptions [specified]:
- Left/right states are perfect-gas Euler variables (ρ,ρu,E), finite with ρ>0 and p>0, using a physical γ>1.
- Outer speeds are S_L=min(u_L−c_L,u_R−c_R) and S_R=max(u_L+c_L,u_R+c_R); the contact speed and two star states are computed algebraically.
- HLLC supplies an interface flux. Reconstruction, time integration, CFL control and boundary states are provided by the caller.
- The local HLLC branch accepts Euler only; availability of HLL for another model does not make this HLLC implementation applicable to it.
Inspected the Euler type restriction and wave-speed/star-state formulae.

units [specified]:
Use one consistent unit system on both sides. ρ is density, u, c and wave speeds are length/time, and p and E are energy/volume. Numerical fluxes have conserved-variable units times length/time. γ is dimensionless; released examples are nondimensional.
Specified from Euler conserved variables and wave-speed dimensions.

boundary_conditions [not-applicable]:
Physical boundary conditions do not belong to the interface-flux function. The caller constructs left/right states; the existing one-dimensional solver uses periodic, fixed-initial-endpoint or extrapolated-edge states.
The flux function accepts two states and does not impose boundaries.

limitations [specified]:
Contact restoration is not a general positivity or entropy-stability guarantee. This Davis-speed version should not be extended without additional treatment to strong rarefactions, vacuum, general equations of state, MHD or relativistic flow. Exact agreement for a stationary contact does not imply an exact solution for moving shocks or arbitrary problems.
Separates a local stationary-contact test from general guarantees.

Review: Read the HLL/HLLC branches of numerical_flux, the non-vacuum check and bracketed pressure bisection in exact_euler. Inspected flux consistency, stationary-contact and Sod reference/accuracy tests. No rerun was performed.

Not checked:
- No full-text equation/table audit of Toro et al., Davis or Sod.
- No new runs, all-state positivity/entropy proof, alternative wave-speed estimates or equations of state.

Evidence:
- numerical_flux HLL/HLLC branches; exact_euler: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/riemann.py
- solve numerical_flux call; _pad: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/numart/solvers.py
- test_flux_consistency; test_hllc_stationary_contact_is_exact; test_exact_sod_star_and_regions; test_sod_accuracy_and_refinement: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_numerics.py

References:
- [original-method / primary-research] Toro, Spruce & Speares (1994). Restoration of the contact surface in the HLL-Riemann solver. — https://doi.org/10.1007/BF01414629
  Primary source for restoring the contact wave missing from HLL. Its complete wave-speed alternatives and WAF experiments were not audited.
  abstract-and-metadata (2026-11-22); Publisher abstract and bibliographic record; full text not reviewed.; https://link.springer.com/article/10.1007/BF01414629
- [adopted-variant / primary-research] Davis (1988). Simplified Second-Order Godunov-Type Methods. — https://doi.org/10.1137/0909030
  Primary paper on bounds for approximate Riemann solvers. The exact min/max formula used here was verified in local code; the full paper was not compared.
  abstract-and-metadata (2026-11-22); Publisher abstract and metadata; wave-speed formulae in full text not reviewed.; https://epubs.siam.org/doi/10.1137/0909030
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

- Reference: https://doi.org/10.1007/BF01414629 — Original HLLC contact-restoration source; no claim that all wave-speed estimates or WAF experiments in the paper are implemented.
- Reference: https://doi.org/10.1137/0909030 — Wave-speed-estimation lineage for the Davis-type min/max acoustic bounds identified in riemann.py; the precise local formula was inspected in code, not checked against the full article.
- Reference: https://doi.org/10.1016/0021-9991(78)90023-2 — Historical shock-tube comparison used as a benchmark source. The atlas reference is its own non-vacuum ideal-gas Riemann evaluator, with a bracketed numerical pressure solve.

Common execution records: [{"id": "sod", "registry_url": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json", "guide": {"ja": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=ja#sod-ja", "en": "https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/?lang=en#sod-en"}}]

Source: https://hrkoyama.github.io/numerical-methods-atlas/methods/hllc/
Edition and terms: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/
