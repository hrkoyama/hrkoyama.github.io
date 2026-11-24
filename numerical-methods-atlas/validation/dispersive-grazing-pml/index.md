# 分散媒質の浅い入射角と長時間PML

80度の中心位相角を持つ有限波束をT=700まで進め、境界誤差を同格子の無PML参照から分離します。

**使用手法**

- [Yee FDTD](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=ja) (`fdtd`)
- [2ステップleapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=ja) (`leapfrog`)
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) (`implicit-midpoint`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-algorithm)

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

- [受動Lorentz・Ohmic分散Maxwell場](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#maxwell-lorentz-ja) (`maxwell-lorentz`)

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。


**問題の図**

![分散媒質の浅い入射角と長時間PML：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[分散媒質の浅い入射角と長時間PML](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja) (`dispersive-grazing-pml`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=ja#dispersive-grazing-pml-ja-validation)

3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。

- [浅角度分散波束の長時間・同格子孤立境界参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dispersive-grazing-pml-ja) (`dispersive-grazing-pml`; 同じ問題の参照 · 有限格子の数値参照)

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。
## 前提・単位・境界

c=1、均質Lorentz媒質ε∞=1、Δε=0.2、ω0=12はPML内まで連続。512/768/1024点とpeak6/9/12を同時に細分化します。垂直粗格子はpeak6、弱減衰細格子対照はpeak12。長さ64、層幅12、中心32、幅4、carrier6は固定です。

**編集上の補足**

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。 周期y方向の1周期を表示しています。波形を見やすくするため、x軸とy軸の表示縮尺は異なります。

## 採用した計算法

Yee・中点ADEに時刻配置を保った台形微分memoryを結合。正の物理散逸と符号付きPML数値仕事を区別し、補助場を含め全状態を保存します。

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

## 比較・検証

3つの格子・層強度の同時細分化、垂直・弱減衰対照の5長時間計算。参照入力が全て不変なことを確認して同一byteの無PML参照を再利用します。旧13検査本体を保持し、policy・peak12直接仕事の2回帰を追加。全44長時間判定は不変です。

## 確認の限界

有限kx帯域の中心角が80度で、全成分が厳密に80度ではありません。無PML参照は同じ離散化・初期場を使い、伝播分散を除いた境界誤差用です。任意角度・材料での大域安定性証明ではありません。 固定PMLの空間次数を測る族ではなく、旧100検査だけでpeak12の大域安定性が証明されたとはしません。

## 保存実測値と判定

```json
{
  "metrics": {
    "completed_primary_and_control_runs": 5,
    "spatial_dimensions": 2,
    "spatial_restriction": "Actual single-ky Yee evolution; no arbitrary-y scattering claim.",
    "reference": "Independent no-PML Fourier update matrix; shared discretization and initialization isolate boundary error from bulk dispersion.",
    "memory_scheme": "Trapezoidal derivative filter; original endpoint-held variant retained separately.",
    "refinement_family": "Joint grid and layer-strength co-refinement, not fixed-PML spatial order.",
    "actual_pml_peaks": {
      "grazing-n512": 6.0,
      "grazing-n768": 9.0,
      "grazing-n1024": 12.0,
      "normal-n512": 6.0,
      "damped-grazing-n1024": 12.0
    },
    "PML_work_is_signed_numerical_work": true,
    "material_continues_through_PML": true,
    "finite_band_carrier_not_exactly_monochromatic": true,
    "finest_grazing_boundary_error": 3.698206474875288e-05,
    "maximum_energy_budget_defect": 1.4663140868405557e-12,
    "maximum_positive_energy_ratio": 1.046709741179309,
    "normal_final_energy_fraction": 1.0466875150335664e-18
  },
  "checks": {
    "independent-reference-and-filter-qualified": true,
    "grazing-n512/all-fields-and-auxiliaries-finite": true,
    "grazing-n512/same-grid-isolated-boundary-error": true,
    "grazing-n512/direct-signed-work-ledger": true,
    "grazing-n512/nonnegative-physical-material-work": true,
    "grazing-n512/long-time-physical-energy-bounded": true,
    "grazing-n512/long-time-memory-bounded": true,
    "grazing-n512/long-time-residual": true,
    "grazing-n512/five-matched-actual-times": true,
    "grazing-n768/all-fields-and-auxiliaries-finite": true,
    "grazing-n768/same-grid-isolated-boundary-error": true,
    "grazing-n768/direct-signed-work-ledger": true,
    "grazing-n768/nonnegative-physical-material-work": true,
    "grazing-n768/long-time-physical-energy-bounded": true,
    "grazing-n768/long-time-memory-bounded": true,
    "grazing-n768/long-time-residual": true,
    "grazing-n768/five-matched-actual-times": true,
    "grazing-n1024/all-fields-and-auxiliaries-finite": true,
    "grazing-n1024/same-grid-isolated-boundary-error": true,
    "grazing-n1024/direct-signed-work-ledger": true,
    "grazing-n1024/nonnegative-physical-material-work": true,
    "grazing-n1024/long-time-physical-energy-bounded": true,
    "grazing-n1024/long-time-memory-bounded": true,
    "grazing-n1024/long-time-residual": true,
    "grazing-n1024/five-matched-actual-times": true,
    "normal-n512/all-fields-and-auxiliaries-finite": true,
    "normal-n512/same-grid-isolated-boundary-error": true,
    "normal-n512/direct-signed-work-ledger": true,
    "normal-n512/nonnegative-physical-material-work": true,
    "normal-n512/long-time-physical-energy-bounded": true,
    "normal-n512/long-time-memory-bounded": true,
    "normal-n512/long-time-residual": true,
    "normal-n512/five-matched-actual-times": true,
    "damped-grazing-n1024/all-fields-and-auxiliaries-finite": true,
    "damped-grazing-n1024/same-grid-isolated-boundary-error": true,
    "damped-grazing-n1024/direct-signed-work-ledger": true,
    "damped-grazing-n1024/nonnegative-physical-material-work": true,
    "damped-grazing-n1024/long-time-physical-energy-bounded": true,
    "damped-grazing-n1024/long-time-memory-bounded": true,
    "damped-grazing-n1024/long-time-residual": true,
    "damped-grazing-n1024/five-matched-actual-times": true,
    "finest-grazing-boundary-error": true,
    "grazing-refinement-n768": true,
    "grazing-refinement-n1024": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/index.json

![保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

保存した浅角度の実電場を周期y方向へ再構成。灰色はPML領域です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Meep developers (n.d.). Meep Materials documentation [accessed 2026-11-24]. https://meep.readthedocs.io/en/latest/Materials/; review_level=primary-official-documentation-selected-sections
Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.

- Steven G. Johnson (2021). Notes on Perfectly Matched Layers. https://arxiv.org/html/2108.05348v1; review_level=primary-author-notes-selected-derivation
Read sections 3.2–4.2, equations 7–8 and the time-domain ADE discussion, plus sections 5–7.2 on homogeneity, evanescent fields and grazing/discretization limitations. The served text is updated 2026-08-24. The trapezoidal filter is our derivation; no full original Berenger/Roden-Gedney paper review is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Long-time grazing PML in a dispersive medium

Evolve a finite packet with an 80-degree central phase angle to T = 700, isolating boundary error against a no-PML reference on the same grid.

**Methods used**

- [Yee finite-difference time-domain method](https://hrkoyama.github.io/numerical-methods-atlas/methods/fdtd/?lang=en) (`fdtd`)
- [Two-step leapfrog](https://hrkoyama.github.io/numerical-methods-atlas/methods/leapfrog/?lang=en) (`leapfrog`)
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) (`implicit-midpoint`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-algorithm)

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

- [Passive Lorentz–Ohmic Maxwell fields](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#maxwell-lorentz-en) (`maxwell-lorentz`)

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.


**Problem figure**

![Long-time grazing PML in a dispersive medium: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Long-time grazing PML in a dispersive medium](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en) (`dispersive-grazing-pml`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dispersive-grazing-pml/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/?lang=en#dispersive-grazing-pml-en-validation)

Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.

- [Isolated same-grid reference for a long grazing dispersive packet](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dispersive-grazing-pml-en) (`dispersive-grazing-pml`; Same-problem reference · Finite-grid numerical reference)

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.
## Assumptions, units and boundaries

Use c = 1 and a homogeneous Lorentz medium with epsilon_inf = 1, delta_epsilon = 0.2 and omega_0 = 12 continuing through the PML. Joint refinement uses 512/768/1024 cells and peaks 6/9/12. The normal coarse control has peak 6; the damped fine companion has peak 12. Length 64, layer thickness 12, center 32, width 4 and carrier 6 are fixed.

**Editorial clarification**

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability. One transverse y period is shown. The displayed x and y scales differ to make the fields visible.

## Adopted numerical method

Couple Yee and midpoint ADE updates to a trapezoidal derivative-memory filter at native times. Separate positive physical dissipation from signed numerical PML work, retaining all physical and auxiliary states.

$$
\partial_t\psi=-s_x(\psi+D_xu),\quad D_x^{\mathrm{PML}}u=D_xu+\psi
$$

$$
\psi^n=b\psi^{n-1}+c(D^n+D^{n-1}),\quad b=\frac{1-s_x\Delta t/2}{1+s_x\Delta t/2},\quad c=\frac{-s_x\Delta t/2}{1+s_x\Delta t/2}
$$

$$
\Delta\mathcal E_{\mathrm{mod}}+W_{\mathrm{physical}}-W_{\mathrm{PML}}=0
$$

## References and validation

Use five long trajectories: three joint grid/layer-strength resolutions, a normal control and a weakly damped companion. Reuse the byte-bound no-PML reference only after checking every unchanged reference argument. Retain the old 13 test bodies and add two parameter-policy/peak-12 work regressions; all original 44 long-trajectory gates remain unchanged.

## Limits

The central angle is 80 degrees; finite kx bandwidth gives neighboring angles. The no-PML reference shares the discretization and initialization to isolate boundary error from bulk dispersion. Small operator and finite-trajectory checks do not prove global stability for arbitrary angles and materials. The joint family does not measure fixed-PML spatial order; the older 100 checks alone do not prove peak-12 global stability.

## Stored measurements and decisions

```json
{
  "metrics": {
    "completed_primary_and_control_runs": 5,
    "spatial_dimensions": 2,
    "spatial_restriction": "Actual single-ky Yee evolution; no arbitrary-y scattering claim.",
    "reference": "Independent no-PML Fourier update matrix; shared discretization and initialization isolate boundary error from bulk dispersion.",
    "memory_scheme": "Trapezoidal derivative filter; original endpoint-held variant retained separately.",
    "refinement_family": "Joint grid and layer-strength co-refinement, not fixed-PML spatial order.",
    "actual_pml_peaks": {
      "grazing-n512": 6.0,
      "grazing-n768": 9.0,
      "grazing-n1024": 12.0,
      "normal-n512": 6.0,
      "damped-grazing-n1024": 12.0
    },
    "PML_work_is_signed_numerical_work": true,
    "material_continues_through_PML": true,
    "finite_band_carrier_not_exactly_monochromatic": true,
    "finest_grazing_boundary_error": 3.698206474875288e-05,
    "maximum_energy_budget_defect": 1.4663140868405557e-12,
    "maximum_positive_energy_ratio": 1.046709741179309,
    "normal_final_energy_fraction": 1.0466875150335664e-18
  },
  "checks": {
    "independent-reference-and-filter-qualified": true,
    "grazing-n512/all-fields-and-auxiliaries-finite": true,
    "grazing-n512/same-grid-isolated-boundary-error": true,
    "grazing-n512/direct-signed-work-ledger": true,
    "grazing-n512/nonnegative-physical-material-work": true,
    "grazing-n512/long-time-physical-energy-bounded": true,
    "grazing-n512/long-time-memory-bounded": true,
    "grazing-n512/long-time-residual": true,
    "grazing-n512/five-matched-actual-times": true,
    "grazing-n768/all-fields-and-auxiliaries-finite": true,
    "grazing-n768/same-grid-isolated-boundary-error": true,
    "grazing-n768/direct-signed-work-ledger": true,
    "grazing-n768/nonnegative-physical-material-work": true,
    "grazing-n768/long-time-physical-energy-bounded": true,
    "grazing-n768/long-time-memory-bounded": true,
    "grazing-n768/long-time-residual": true,
    "grazing-n768/five-matched-actual-times": true,
    "grazing-n1024/all-fields-and-auxiliaries-finite": true,
    "grazing-n1024/same-grid-isolated-boundary-error": true,
    "grazing-n1024/direct-signed-work-ledger": true,
    "grazing-n1024/nonnegative-physical-material-work": true,
    "grazing-n1024/long-time-physical-energy-bounded": true,
    "grazing-n1024/long-time-memory-bounded": true,
    "grazing-n1024/long-time-residual": true,
    "grazing-n1024/five-matched-actual-times": true,
    "normal-n512/all-fields-and-auxiliaries-finite": true,
    "normal-n512/same-grid-isolated-boundary-error": true,
    "normal-n512/direct-signed-work-ledger": true,
    "normal-n512/nonnegative-physical-material-work": true,
    "normal-n512/long-time-physical-energy-bounded": true,
    "normal-n512/long-time-memory-bounded": true,
    "normal-n512/long-time-residual": true,
    "normal-n512/five-matched-actual-times": true,
    "damped-grazing-n1024/all-fields-and-auxiliaries-finite": true,
    "damped-grazing-n1024/same-grid-isolated-boundary-error": true,
    "damped-grazing-n1024/direct-signed-work-ledger": true,
    "damped-grazing-n1024/nonnegative-physical-material-work": true,
    "damped-grazing-n1024/long-time-physical-energy-bounded": true,
    "damped-grazing-n1024/long-time-memory-bounded": true,
    "damped-grazing-n1024/long-time-residual": true,
    "damped-grazing-n1024/five-matched-actual-times": true,
    "finest-grazing-boundary-error": true,
    "grazing-refinement-n768": true,
    "grazing-refinement-n1024": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dispersive-grazing-pml/index.json

![Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/dispersive-grazing-pml-preview.png)

Actual saved grazing electric field reconstructed over the periodic y direction; gray shading marks the PML.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/atlas-maxwell-grazing-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/maxwell-grazing/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Meep developers (n.d.). Meep Materials documentation [accessed 2026-11-24]. https://meep.readthedocs.io/en/latest/Materials/; review_level=primary-official-documentation-selected-sections
Read Material Dispersion, Numerical Stability, Loss and Gain, and Conductivity. Confirmed the exp(-i omega t) convention, Lorentz polarization and dispersive-PML warning. Our sigma E conductivity and midpoint update differ from Meep. Unversioned latest documentation; no original Yee or Roden-Gedney paper claim. Publication and revision dates have not been verified. Accessed on 2026-11-24; this is a consultation date, not a publication year.

- Steven G. Johnson (2021). Notes on Perfectly Matched Layers. https://arxiv.org/html/2108.05348v1; review_level=primary-author-notes-selected-derivation
Read sections 3.2–4.2, equations 7–8 and the time-domain ADE discussion, plus sections 5–7.2 on homogeneity, evanescent fields and grazing/discretization limitations. The served text is updated 2026-08-24. The trapezoidal filter is our derivation; no full original Berenger/Roden-Gedney paper review is claimed.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
