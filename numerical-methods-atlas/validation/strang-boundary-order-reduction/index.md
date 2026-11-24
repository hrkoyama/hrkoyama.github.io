# Dirichlet境界でのStrang次数低下と補正

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。

**使用手法**

- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)
- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) (`lie-trotter`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-algorithm)

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

- [非同次境界を持つ線形反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja) (`inhomogeneous-reaction-diffusion`)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。


**問題の図**

![Dirichlet境界でのStrang次数低下と補正：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja) (`strang-boundary-order-reduction`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-validation)

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

- [Dirichlet境界でのStrang次数低下と補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja) (`strang-boundary-order-reduction`; 同じ問題の参照 · 半解析参照)

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。
## 前提・単位・境界

u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。

**編集上の補足**

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

## 採用した計算法

w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

## 比較・検証

独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。

## 確認の限界

原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

## 保存実測値と判定

```json
{
  "metrics": {
    "N127_finest_raw_temporal_error": 0.00011072277594093016,
    "N127_finest_corrected_temporal_error": 9.830520841802581e-08,
    "reference_spatial_order": 1.9999950873134633,
    "scope": "Actual1Dnonperiodicfields. TimevsSAME-FDoracle; spacevsanalyticcontinuum. Linearautonomousspecialization, fixed-regime order; no universal reduction/theorem reproduction."
  },
  "checks": {
    "boundary-n31-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-lie-8:actual-field-and-work": true,
    "boundary-n127-lie-8:boundary-compatibility-ledger": true,
    "boundary-n127-lie-16:actual-field-and-work": true,
    "boundary-n127-lie-16:boundary-compatibility-ledger": true,
    "boundary-n127-lie-32:actual-field-and-work": true,
    "boundary-n127-lie-32:boundary-compatibility-ledger": true,
    "boundary-n127-lie-64:actual-field-and-work": true,
    "boundary-n127-lie-64:boundary-compatibility-ledger": true,
    "n31:corrected-finest-accuracy": true,
    "n63:corrected-finest-accuracy": true,
    "n127:corrected-finest-accuracy": true,
    "strang-unmodified:fixed-regime-temporal-order": true,
    "strang-boundary-corrected:fixed-regime-temporal-order": true,
    "finest:boundary-correction-improves": true,
    "separate-reference-spatial-order": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/index.json

![実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。 保存済みの数値場と参照を用いた図です。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- L. Einkemmer; A. Ostermann (2014). Overcoming order reduction in diffusion-reaction splitting. Part1: Dirichlet boundary conditions [accessed 2026-11-24]. https://arxiv.org/abs/1411.0465; review_level=primary-preprint-selected-sections
2014v1の§2/Algorithm2/定数境界例、§3.2の定理・仮定、1D例の選択抽出テキストを閲読。全証明・原PDF全画像の監査ではありません。今回線形特殊例で、原著の非線形数値表ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Strang splitting: Dirichlet boundary order reduction and correction

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization.

**Methods used**

- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) (`strang-splitting`)
- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) (`lie-trotter`)
- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-algorithm)

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

- [Linear reaction-diffusion with inhomogeneous boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#inhomogeneous-reaction-diffusion-en) (`inhomogeneous-reaction-diffusion`)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

- [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en) (`heat`)

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.


**Problem figure**

![Strang splitting: Dirichlet boundary order reduction and correction: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en) (`strang-boundary-order-reduction`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=en#strang-boundary-order-reduction-en-validation)

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

- [Strang splitting: Dirichlet boundary order reduction and correction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-strang-boundary-order-reduction-en) (`strang-boundary-order-reduction`; Same-problem reference · Semi-analytic reference)

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.
## Assumptions, units and boundaries

Solve u_t = u_xx + u on [0, 1] with both boundary values equal to 1, an analytic steady state plus a 0.1 sine perturbation, and T = 0.1. Use 31, 63 and 127 interior nodes with 8, 16, 32 and 64 steps, plus four Lie controls: 28 runs.

**Editorial clarification**

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

## Adopted numerical method

For w = u - 1, use the unmodified split (Lw, w + 1) or the corrected split (Lw + 1, w). Compose actual Dirichlet DST-I flows and retain the reaction boundary mismatch.

$$
u_t=u_{xx}+u,\quad u(0,t)=u(1,t)=1,\quad w=u-1
$$

$$
A_{\rm raw}(w)=L_hw,\ B_{\rm raw}(w)=w+1;\quad A_{\rm corr}(w)=L_hw+1,\ B_{\rm corr}(w)=w
$$

## References and validation

First qualify an independent sparse affine exponential action against separately written sine sums. Then separate temporal error against the same finite-difference system, spatial error against the analytic continuum field, and observed order in the fixed regime.

## Limits

This is an authored linear specialization, not a reproduction of the original nonlinear tables. It makes no general claim for nonautonomous boundaries or universal order loss. The final reaction-trace mismatch of Lie splitting is disclosed separately.

## Stored measurements and decisions

```json
{
  "metrics": {
    "N127_finest_raw_temporal_error": 0.00011072277594093016,
    "N127_finest_corrected_temporal_error": 9.830520841802581e-08,
    "reference_spatial_order": 1.9999950873134633,
    "scope": "Actual1Dnonperiodicfields. TimevsSAME-FDoracle; spacevsanalyticcontinuum. Linearautonomousspecialization, fixed-regime order; no universal reduction/theorem reproduction."
  },
  "checks": {
    "boundary-n31-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n31-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n31-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n31-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n63-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n63-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n63-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-8:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-16:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-32:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-unmodified-64:actual-field-and-work": true,
    "boundary-n127-strang-unmodified-64:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-8:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-8:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-16:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-16:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-32:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-32:boundary-compatibility-ledger": true,
    "boundary-n127-strang-boundary-corrected-64:actual-field-and-work": true,
    "boundary-n127-strang-boundary-corrected-64:boundary-compatibility-ledger": true,
    "boundary-n127-lie-8:actual-field-and-work": true,
    "boundary-n127-lie-8:boundary-compatibility-ledger": true,
    "boundary-n127-lie-16:actual-field-and-work": true,
    "boundary-n127-lie-16:boundary-compatibility-ledger": true,
    "boundary-n127-lie-32:actual-field-and-work": true,
    "boundary-n127-lie-32:boundary-compatibility-ledger": true,
    "boundary-n127-lie-64:actual-field-and-work": true,
    "boundary-n127-lie-64:boundary-compatibility-ledger": true,
    "n31:corrected-finest-accuracy": true,
    "n63:corrected-finest-accuracy": true,
    "n127:corrected-finest-accuracy": true,
    "strang-unmodified:fixed-regime-temporal-order": true,
    "strang-boundary-corrected:fixed-regime-temporal-order": true,
    "finest:boundary-correction-improves": true,
    "separate-reference-spatial-order": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/index.json

![Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png)

Evolve actual one-dimensional nonperiodic fields and compare unmodified and boundary-corrected Strang splitting against the same spatial discretization. This preview reads saved numerical fields and references only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/atlas-ode-adaptivity-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- L. Einkemmer; A. Ostermann (2014). Overcoming order reduction in diffusion-reaction splitting. Part1: Dirichlet boundary conditions [accessed 2026-11-24]. https://arxiv.org/abs/1411.0465; review_level=primary-preprint-selected-sections
Read selected extracted text from the 2014 v1 preprint: section 2, Algorithm 2, the constant-boundary example, section 3.2 assumptions and result, and the one-dimensional example. This was not a full-proof or whole-PDF visual audit; the present linear specialization does not reproduce the nonlinear tables.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
