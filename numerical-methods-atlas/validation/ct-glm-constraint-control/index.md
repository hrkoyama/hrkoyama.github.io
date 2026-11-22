# CTの初期制約保持とGLMの能動的cleaning：非物理診断対照

故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。

## 前提・単位・境界

32²周期格子、t=.1、128刻み、ρ=p=1、v=0、By=ψ=0。CT face Bx=.01cos[2π(i+1)/32]、GLM cell Bxはその左右face平均と同一です。CT初期native div≠0は意図的に無効な物理初期値で、CTの正しい物理計算例とは区別します。

**編集上の補足**

発散制約を意図的に破った初期場を共通のセル磁場として与える診断です。正当な発散ゼロ初期条件のCT計算とは区別し、CTが初期制約誤差を保持する性質を確認します。GLMは減衰なしの対照とも比較し、磁場とpsiの波エネルギーを使って輸送の位相変化や数値拡散を物理減衰と混同しません。

## 採用した計算法

同じ完全結合MHDコードを使用。y不変・By=vy=0ではGLMのBx/ψ系が流体応答から独立するため、離散Fourier記号の2×2行列と前進Euler行列冪を別に構成します。κ=2とκ=0を同じdt・LLF粘性で比較し、Bxだけの減少を物理減衰と取り違えません。

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

## 比較・検証

CT native divの初期違反保持、GLMのψ励起、Bx/ψ双方の独立FE参照一致、密度・圧力正値性、物理的総E/質量保存を確認。補助波エネルギーW=〈Bx²+ψ²/ch²〉のκ2/κ0比を判定し、半離散行列指数と連続Fourier解も区別して表示します。

## 確認の限界

対照の合格は「期待したCTの非除去とGLMの線形応答を正しく検出した」という意味です。非零CT divを許す物理計算を推奨しません。Wは診断用ノルムで、ψを含まない物理的総エネルギーEとは別です。GLMのBx減少には位相交換とLLF拡散も含まれ、κ0対照なしに減衰成功とは呼びません。一般非線形・境界流出・衝撃波のcleaning性能へ広げません。

## 保存実測値と判定

```json
{
  "metrics": {
    "damped_to_undamped_B_psi_wave_energy_ratio": 0.797707175433604,
    "ct_native_divergence_linf_change": 0.0,
    "ct_common_divergence_linf_change": 1.457167719820518e-16,
    "initial_common_divergence_l2": 0.04393133573771591,
    "initial_cell_state_difference": 4.7704895589362195e-18
  },
  "checks": {
    "ct_preserves_initial_constraint_defect": true,
    "ct_does_not_clean_common_initial_defect": true,
    "ct_initial_constraint_is_deliberately_nonzero": true,
    "damped_independent_discrete_fourier_agreement": true,
    "damped_positive_states": true,
    "damped_conservative_mass_energy": true,
    "damped_psi_is_activated": true,
    "glm_final_B_divergence_reduced": true,
    "undamped_independent_discrete_fourier_agreement": true,
    "undamped_positive_states": true,
    "undamped_conservative_mass_energy": true,
    "undamped_psi_is_activated": true,
    "physical_damping_separated_from_phase_and_LLF_viscosity": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "matched_initial_cell_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/index.json

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

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Initial-constraint preservation by CT and active GLM cleaning: nonphysical control

Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem.

## Assumptions, units and boundaries

Periodic32² grid,t=.1,128 steps,rho=p=1,v=0,By=psi=0. CT faceBx=.01cos[2pi(i+1)/32]; GLM cellBx equals the adjacent-face average. The intentional nonzero native CT divergence violates valid physical CT initial data and is treated solely as a diagnostic.

**Editorial clarification**

This diagnostic deliberately violates the divergence constraint while giving both methods the same initial cell magnetic field. It is separate from legitimate divergence-free CT initial data and checks CT preservation of an existing constraint error. Compare GLM with an undamped control using magnetic-plus-psi wave energy, distinguishing wave phase and numerical diffusion from physical damping.

## Adopted numerical method

Use the same fully coupled MHD code. With y-invariance andBy=vy=0, the GLM Bx/psi subsystem decouples from fluid feedback, allowing a separately constructed2x2 discrete Fourier symbol and forward-Euler matrix power. Compare kappa2/0 at identical dt and LLF viscosity, separating B/psi phase exchange from physical damping.

$$
\widehat{U}^{m+1}=(I+\Delta t M_h)\widehat{U}^{m},\quad M_h=\begin{pmatrix}\nu_h&-i\widetilde{k}\\-ic_h^2\widetilde{k}&\nu_h-\kappa\end{pmatrix}
$$

$$
\nu_h=\alpha N[\cos(2\pi/N)-1],\quad\widetilde{k}=N\sin(2\pi/N)
$$

$$
W=\langle B_x^2+\psi^2/c_h^2\rangle,\qquad W_{\kappa=2}/W_{\kappa=0}<0.95
$$

## References and validation

Check preservation of the initial CT defect, nonzero GLM psi, independent FE agreement for bothBx/psi, positive density/pressure, and conserved physical E/mass. Test the kappa2/0 ratio of auxiliary wave energy W=mean(Bx²+psi²/ch²), separating FE, semidiscrete-exponential and continuum-Fourier references.

## Limits

Passing means correctly detecting expected CT non-removal and the calibrated GLM response, not recommending non-solenoidal CT physical initial data. W is an auxiliary diagnostic norm, distinct from conserved physical total energy E without psi. B decay includes phase exchange and LLF diffusion; damping is assessed with the kappa0 control. No general nonlinear,boundary or shock cleaning guarantee is claimed.

## Stored measurements and decisions

```json
{
  "metrics": {
    "damped_to_undamped_B_psi_wave_energy_ratio": 0.797707175433604,
    "ct_native_divergence_linf_change": 0.0,
    "ct_common_divergence_linf_change": 1.457167719820518e-16,
    "initial_common_divergence_l2": 0.04393133573771591,
    "initial_cell_state_difference": 4.7704895589362195e-18
  },
  "checks": {
    "ct_preserves_initial_constraint_defect": true,
    "ct_does_not_clean_common_initial_defect": true,
    "ct_initial_constraint_is_deliberately_nonzero": true,
    "damped_independent_discrete_fourier_agreement": true,
    "damped_positive_states": true,
    "damped_conservative_mass_energy": true,
    "damped_psi_is_activated": true,
    "glm_final_B_divergence_reduced": true,
    "undamped_independent_discrete_fourier_agreement": true,
    "undamped_positive_states": true,
    "undamped_conservative_mass_energy": true,
    "undamped_psi_is_activated": true,
    "physical_damping_separated_from_phase_and_LLF_viscosity": true,
    "ct_positive_states": true,
    "ct_conservative_mass_energy": true,
    "matched_initial_cell_states": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/index.json

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

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
