# 非周期壁面の製造解：速度・剪断・圧力演算子

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-algorithm)

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja) (`forced-incompressible`)

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。


**問題の図**

![非周期壁面の製造解：速度・剪断・圧力演算子：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-validation)

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

- [壁面製造解：多項式速度と独立した圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja) (`wall-mms`; 同じ問題の参照 · 製造解)

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。
## 前提・単位・境界

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。

**編集上の補足**

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。 科学ソース改訂3・不変配布版2026-11-23-r2は22単体検査と群全体94判定に合格しました。初回のNumPy真偽値のJSON直列化失敗に加え、次の未公開候補は共通verifierが必要とする完了状態・ケースID別の最上位合否が不足していました。この配布版はJSONのtermination・failure・ケース別checksを整え、従来の3診断をsummary_checksへ保持する封筒形式だけの修正と、回帰検査1件を追加しています。入力・受入条件・数値ソルバー・参照と従来21検査は不変で、6計算の保存NPZ配列は前候補とビット一致しています。元の未公開配布物は公開ツリー外の作業記録へ保存し、旧候補の失敗履歴も保持しました。 最細速度L2は約2.638×10⁻⁵、最後の格子対の速度・流れ関数次数は約2.009/2.022です。実際の壁剪断の観測次数は約1.982ですが、厳密ψでのThom局所打切り次数は約.989で、一般の二次壁公式の保証ではありません。独立した圧力演算子のp・全勾配・境界勾配の次数は約1.978/2.318/1.998であり、キャビティ圧力とは別です。

## 採用した計算法

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

## 比較・検証

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

## 確認の限界

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

## 保存実測値と判定

```json
{
  "metrics": {
    "finest_velocity_l2": 2.637991527485713e-05,
    "finest_streamfunction_l2": 3.0579766556845255e-05,
    "observed_orders": {
      "psi_l2": [
        2.0426330065243574,
        2.021783836772359
      ],
      "velocity_l2": [
        1.9917746694984177,
        2.0086644375747413
      ],
      "wall_omega_maximum": [
        1.937772137605888,
        1.9794771588130946
      ],
      "wall_shear_maximum": [
        1.9412705074950394,
        1.9820164294643936
      ],
      "thom_exact_psi_wall_truncation": [
        0.9769163868869587,
        0.9885952367277506
      ],
      "pressure_l2": [
        1.9590185209239261,
        1.9784952274339704
      ],
      "pressure_gradient_l2": [
        2.3544980286788206,
        2.3175253385985015
      ],
      "pressure_boundary_gradient_l2": [
        1.9914961869556822,
        1.9978781190385215
      ]
    },
    "reference_qualification": {
      "checks": {
        "independent tensor-polynomial fields": true,
        "independent tensor-polynomial forcing": true,
        "analytic four-wall no slip": true,
        "analytic incompressibility": true,
        "two primary-table columns each 17 points": true
      },
      "field_maximum": 1.27675647831893e-15,
      "forcing_maximum": 4.038436252074007e-15,
      "exact_wall_speed": 1.27675647831893e-15,
      "passed": true
    },
    "pressure_scope": "Separate manufactured Dirichlet operator; cavity pressure not computed."
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "psi_l2 refinement 1": true,
    "velocity_l2 refinement 1": true,
    "wall_omega_maximum refinement 1": true,
    "wall_shear_maximum refinement 1": true,
    "psi_l2 refinement 2": true,
    "velocity_l2 refinement 2": true,
    "wall_omega_maximum refinement 2": true,
    "wall_shear_maximum refinement 2": true,
    "finest streamfunction order": true,
    "finest velocity order": true,
    "finest streamfunction accuracy": true,
    "finest velocity accuracy": true,
    "n17: separate pressure Dirichlet boundary": true,
    "n17: separate pressure Poisson residual": true,
    "n17: finite separate pressure solution": true,
    "n33: separate pressure Dirichlet boundary": true,
    "n33: separate pressure Poisson residual": true,
    "n33: finite separate pressure solution": true,
    "n65: separate pressure Dirichlet boundary": true,
    "n65: separate pressure Poisson residual": true,
    "n65: finite separate pressure solution": true,
    "finest separate pressure_l2 order": true,
    "finest separate pressure_gradient_l2 order": true,
    "finest separate pressure_boundary_gradient_l2 order": true,
    "independent tensor-polynomial fields": true,
    "independent tensor-polynomial forcing": true,
    "analytic four-wall no slip": true,
    "analytic incompressibility": true,
    "two primary-table columns each 17 points": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/index.json

![実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

## 出典と確認範囲

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
原著の式・境界図・表I/IIのRe100列と表Vの主渦を直接目視確認。公開ミラーは原著の配送元として記録し、論文PDFは配布しません。本実装は原著のCSI-MG法とは異なります。

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions [accessed 2026-11-23]. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Sandia/OSTI公式書誌・抄録と、原著報告の印刷12頁で製造解と格子細分化の併用を確認。本例の多項式と圧力場は独自に構成しました。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Nonperiodic wall MMS: velocity, shear and pressure operator

Apply analytic forcing to the same wall-bounded2D solver, measuring grid convergence of velocity/streamfunction and actual wall-vorticity/shear errors. A separate nonzero-Dirichlet manufactured pressure verifies Poisson and boundary-gradient operators.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-algorithm)

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [Forced incompressible flow and wall manufactured solutions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-incompressible-en) (`forced-incompressible`)

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.


**Problem figure**

![Nonperiodic wall MMS: velocity, shear and pressure operator: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Manufactured incompressible flow with nonperiodic walls](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en) (`wall-manufactured`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=en#wall-manufactured-en-validation)

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

- [Wall manufactured solution: polynomial velocity and separate pressure operator](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-wall-mms-en) (`wall-mms`; Same-problem reference · Manufactured solution)

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.
## Assumptions, units and boundaries

Unit square, viscosity .01,17/33/65nodes,psi8f(x)f(y), f(z)=z²(1−z)². All walls are impermeable/no-slip. Derive the curl forcing from the continuous PDE and use the same actual Thom closure as the cavity on every wall; never inject exact wall vorticity.

**Editorial clarification**

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver. Scientific-source revision3, immutable edition2026-11-23-r2, passed22 unit checks and all94 group gates. After the initial NumPy-boolean JSON-serialization failure, the next unpublished candidate lacked completion status and case-ID top-level checks required by the common verifier. This edition only repairs the JSON envelope with termination,failure and case-keyed checks, retaining the prior three diagnostics under summary_checks, and adds one regression. Inputs,acceptance,numerical solver,references and the prior21 tests are unchanged. All six saved NPZ field arrays are bit-identical to the previous candidate. The original unpublished packet is archived outside the public tree, and earlier failure history is retained. Finest velocityL2 is about2.638e-5, with last-pair velocity/streamfunction orders about2.009/2.022. Actual wall-shear order is about1.982, while local Thom truncation on exactpsi is about.989; this does not guarantee a universally second-order wall formula. The separate pressure-operatorp/full-gradient/boundary-gradient orders are about1.978/2.318/1.998, distinct from cavity pressure.

## Adopted numerical method

Use the shared centered FD/Heun/nonperiodic Dirichlet DST solver. Qualify explicit analytic derivatives against independently differentiated tensor coefficients. Separately solve nonzero-Dirichlet Poisson for p=x²+y²+sin(pi*x)sin(pi*y), checking central interior and second-order one-sided boundary gradients.

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

## References and validation

Require finest-pair psi/velocity orders ≥1.7, decreasing and bounded errors, and decreasing actual wall-vorticity/velocity-gradient shear errors. Separate pressure orders must be≥1.8 for p and≥1.7 for full/boundary gradients. Record five independent polynomial-reference checks, four-wall values, true steady residual and nonperiodic Poisson residual.

## Limits

Thom wall vorticity has first-order local truncation; publish observed shear rates without promising second order. Pressure is eliminated from streamfunction evolution, so a pressure gauge is inapplicable. The separate operator MMS does not verify cavity pressure, traction boundaries or MAC projection. Independent polynomial differentiation is distinct from comparison with an independent flow solver.

## Stored measurements and decisions

```json
{
  "metrics": {
    "finest_velocity_l2": 2.637991527485713e-05,
    "finest_streamfunction_l2": 3.0579766556845255e-05,
    "observed_orders": {
      "psi_l2": [
        2.0426330065243574,
        2.021783836772359
      ],
      "velocity_l2": [
        1.9917746694984177,
        2.0086644375747413
      ],
      "wall_omega_maximum": [
        1.937772137605888,
        1.9794771588130946
      ],
      "wall_shear_maximum": [
        1.9412705074950394,
        1.9820164294643936
      ],
      "thom_exact_psi_wall_truncation": [
        0.9769163868869587,
        0.9885952367277506
      ],
      "pressure_l2": [
        1.9590185209239261,
        1.9784952274339704
      ],
      "pressure_gradient_l2": [
        2.3544980286788206,
        2.3175253385985015
      ],
      "pressure_boundary_gradient_l2": [
        1.9914961869556822,
        1.9978781190385215
      ]
    },
    "reference_qualification": {
      "checks": {
        "independent tensor-polynomial fields": true,
        "independent tensor-polynomial forcing": true,
        "analytic four-wall no slip": true,
        "analytic incompressibility": true,
        "two primary-table columns each 17 points": true
      },
      "field_maximum": 1.27675647831893e-15,
      "forcing_maximum": 4.038436252074007e-15,
      "exact_wall_speed": 1.27675647831893e-15,
      "passed": true
    },
    "pressure_scope": "Separate manufactured Dirichlet operator; cavity pressure not computed."
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "psi_l2 refinement 1": true,
    "velocity_l2 refinement 1": true,
    "wall_omega_maximum refinement 1": true,
    "wall_shear_maximum refinement 1": true,
    "psi_l2 refinement 2": true,
    "velocity_l2 refinement 2": true,
    "wall_omega_maximum refinement 2": true,
    "wall_shear_maximum refinement 2": true,
    "finest streamfunction order": true,
    "finest velocity order": true,
    "finest streamfunction accuracy": true,
    "finest velocity accuracy": true,
    "n17: separate pressure Dirichlet boundary": true,
    "n17: separate pressure Poisson residual": true,
    "n17: finite separate pressure solution": true,
    "n33: separate pressure Dirichlet boundary": true,
    "n33: separate pressure Poisson residual": true,
    "n33: finite separate pressure solution": true,
    "n65: separate pressure Dirichlet boundary": true,
    "n65: separate pressure Poisson residual": true,
    "n65: finite separate pressure solution": true,
    "finest separate pressure_l2 order": true,
    "finest separate pressure_gradient_l2 order": true,
    "finest separate pressure_boundary_gradient_l2 order": true,
    "independent tensor-polynomial fields": true,
    "independent tensor-polynomial forcing": true,
    "analytic four-wall no slip": true,
    "analytic incompressibility": true,
    "two primary-table columns each 17 points": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/index.json

![Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

Computed finest manufactured-flow streamlines and velocity error, using the same Thom closure as the cavity without exact wall-vorticity injection.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

## Sources and review scope

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
Visually inspected original equations/boundary figure, Re100 columns in TablesI/II and primary vortex in TableV. The public mirror delivers the original paper; its PDF is not redistributed. This independently written solver differs from CSI-MG.

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions [accessed 2026-11-23]. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Read official Sandia/OSTI metadata/abstract and original report printed12 on MMS together with mesh refinement. The polynomial and pressure field are constructed for this example.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
