# Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

## 前提・単位・境界

標準周期OT、γ=5/3、ρ=25/(36π)、p=5/(12π)、v=(−sin2πy,sin2πx)、B=(−sin2πy,sin4πx)/√(4π)、t=.05。16²/32²/64²の両法に192刻みを共用します。旧配布版を改変しない追加検証です。

**編集上の補足**

共通の数値流束族・速度上限・時間刻み・物理減衰率を固定しますが、CTの面磁場とGLMのセル磁場、法線磁場の扱いは異なります。離散化全体の比較であり、差のすべてを発散処理だけの効果とはしません。CT固有の面発散と共通のセル中心発散は別の演算子として報告します。

## 採用した計算法

主計算は固定α=ch=3のRusanovと前進Euler、GLMκ=2は格子に依存しません。独立C++ Athena++はHLLD・PLM・RK2・upwind CTです。同じ連続初期値を用いますが、Athenaのface/primitive離散化は主計算と完全同一ではありません。

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

## 比較・検証

密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。

## 確認の限界

短時間の滑らかなOTで、衝撃波後・3D・一般のcleaning性能の認証ではありません。独立Athena参照も有限格子数値解で、増分は誤差上界ではありません。旧128²/CFL.3は履歴だけで256²/CFL.15との組を純粋な格子次数に使いません。定数LLFによるGLMのdiv=ψ=0保存をcleaning成功とは呼びません。native面divと共通中心divを区別し、中心演算子のcheckerboard盲点も残します。

## 保存実測値と判定

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.04131948399815993,
    "ct_minimum_spatial_order": 0.7441584435125685,
    "ct_time_contamination_ratio": 0.005452472133120275,
    "ct_finest_temporal_scaled_l2": 0.0006451024853786959,
    "ct_minimum_temporal_order": 1.0051663785429696,
    "ct_time_reference_to_primary_ratio": 4.610829174194673e-13,
    "glm_finest_spatial_error": 0.06851242841151672,
    "glm_minimum_spatial_order": 0.6819406396313236,
    "glm_time_contamination_ratio": 0.003289333276474019,
    "glm_finest_temporal_scaled_l2": 0.0007617954701608142,
    "glm_minimum_temporal_order": 1.0056569861410107,
    "glm_time_reference_to_primary_ratio": 3.179752402329314e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "independent_reference_density_refinement": true,
    "independent_reference_magnetic_refinement": true,
    "independent_reference_time_refinement": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_refinement": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_independent_reference_resolved": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_independent_reference_resolved": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

## 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  通常のGLMのB/ψ式と減衰、エネルギー保存、追加のEGLM項との区別を原著の選択式で確認しました。全文監査ではありません。
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  面平均Bと共有corner EMFの構造を確認しました。今回の算術flux-CTを、論文のupwind CT・CTU実装そのものとは呼びません。
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  div B制約手法の比較という原著の主題と書誌を確認しました。今回の数値判定や新しい構成例の出典とはしません。
- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official source at pinned commit actually compiled/executed; paper metadata
  以前に別構築しハッシュを確認した公式commit1395e2f543f4368d448cb1a2cf92ba1f910e3416のC++バイナリーを再利用して新しい参照を実行し、入力・出力・binary/source SHAを保存しました。論文全文監査ではありません。
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  DOP853を別の時間積分器として実行します。空間RHSを共有するため、独立した空間離散化とは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Orszag–Tang: matched CT/GLM and converged independent references

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

## Assumptions, units and boundaries

Standard periodic OT: gamma5/3, rho25/(36pi), p5/(12pi), v=(−sin2piy,sin2pix), B=(−sin2piy,sin4pix)/sqrt(4pi), t=.05. Both methods share192 steps on16²/32²/64². This supplements the previous immutable release.

**Editorial clarification**

Match the flux family, signal bound, time steps and physical damping, while retaining intrinsic differences in face versus cell magnetic fields and normal-field treatment. Compare the whole discretizations; do not attribute every difference solely to divergence control. Report native CT face divergence separately from a common cell-centered divergence.

## Adopted numerical method

Primary runs use fixed alpha=ch=3 Rusanov/forward Euler and grid-independent GLM kappa2. Independent C++ Athena++ uses HLLD/PLM/RK2/upwind CT. Continuous initial fields agree; Athena’s face/primitive discretization is not identical.

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

## References and validation

Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.

## Limits

Short smooth OT, not certification of post-shock,3D or general cleaning behavior. Athena is a finite-grid numerical reference; increments are not error bounds. Historical128²/CFL.3 is not paired with256²/CFL.15 to infer a pure spatial order. Constant-LLF preservation of GLM div=psi=0 is not evidence of active cleaning. Native face and common centered divergences differ; centered checkerboard blind spots remain.

## Stored measurements and decisions

```json
{
  "metrics": {
    "initial_cell_state_linf_difference": 0.0,
    "ct_finest_spatial_error": 0.04131948399815993,
    "ct_minimum_spatial_order": 0.7441584435125685,
    "ct_time_contamination_ratio": 0.005452472133120275,
    "ct_finest_temporal_scaled_l2": 0.0006451024853786959,
    "ct_minimum_temporal_order": 1.0051663785429696,
    "ct_time_reference_to_primary_ratio": 4.610829174194673e-13,
    "glm_finest_spatial_error": 0.06851242841151672,
    "glm_minimum_spatial_order": 0.6819406396313236,
    "glm_time_contamination_ratio": 0.003289333276474019,
    "glm_finest_temporal_scaled_l2": 0.0007617954701608142,
    "glm_minimum_temporal_order": 1.0056569861410107,
    "glm_time_reference_to_primary_ratio": 3.179752402329314e-13
  },
  "checks": {
    "identical_initial_cell_states": true,
    "independent_reference_density_refinement": true,
    "independent_reference_magnetic_refinement": true,
    "independent_reference_time_refinement": true,
    "ct_native_constraint_n16": true,
    "ct_native_constraint_n32": true,
    "ct_native_constraint_n64": true,
    "ct_spatial_refinement": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_independent_reference_resolved": true,
    "ct_time_contamination_bounded": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "glm_spatial_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_independent_reference_resolved": true,
    "glm_time_contamination_bounded": true,
    "glm_positive_states": true,
    "glm_conservative_mass_energy": true,
    "ct_temporal_order": true,
    "ct_temporal_error": true,
    "ct_temporal_reference_resolved": true,
    "glm_temporal_order": true,
    "glm_temporal_error": true,
    "glm_temporal_reference_resolved": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs-initial.json

## Sources and review scope

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; selected original equations 17–19 and 24, pp.650–651
  Checked selected original GLM B/psi and damping equations, conserved physical energy, and the distinction from extra EGLM source terms; not a full-paper audit.
- T. A. Gardiner and J. M. Stone (2005). An unsplit Godunov method for ideal MHD via constrained transport. https://arxiv.org/abs/astro-ph/0501557; review_level=author preprint; selected section2.2/equations13–20
  Checked the face-average/shared-corner-EMF structure. The present arithmetic flux-CT is not identified with the paper’s upwind CT/CTU algorithm.
- G. Tóth (2000). The ∇·B=0 Constraint in Shock-Capturing Magnetohydrodynamics Codes. https://doi.org/10.1006/jcph.2000.6519; review_level=author paper abstract and bibliographic metadata
  Confirmed the original comparison topic and bibliographic identity; not a source of this experiment’s criteria or constructed equilibrium.
- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official source at pinned commit actually compiled/executed; paper metadata
  Executed new reference runs with the previously independently built, hashed official C++ commit1395e2f543f4368d448cb1a2cf92ba1f910e3416 binary, retaining input/output/binary/source hashes; not a full-paper audit.
- SciPy developers (2024). scipy.integrate.solve_ivp: DOP853. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official versioned API and actual independent time-integrator execution
  Execute DOP853 as a separate time integrator; shared spatial RHS means it is not an independent spatial discretization.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
