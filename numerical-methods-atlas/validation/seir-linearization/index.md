# SEIR保存則と初期線形化

人口保存と2モードの初期線形化を別々に検査します。

**使用手法**

- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) (`rk4`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-algorithm)

全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

- [閉鎖SEIR区画モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#seir-compartment-ja) (`seir-compartment`)

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。


**問題の図**

![SEIR保存則と初期線形化：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja) (`seir-linearization`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=ja#seir-linearization-ja-validation)

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

- [SEIR保存則と初期線形化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-seir-linearization-ja) (`seir-linearization`; 同じ問題の参照 · 有限格子の数値参照)

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。
## 前提・単位・境界

閉鎖人口S+E+I+R=1、β=0.6、σ=0.3、γ=0.2。η=10⁻⁴/5×10⁻⁵に対し(S,E,I,R)(0)=(1−2η,η,η,0)、0≤t≤20。出生・死亡・外部流入はありません。

**編集上の補足**

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。 時間・濃度・個体数の軸は空間次元ではありません。率は教育用で疾病・実験予測ではありません。

## 採用した計算法

全4状態を固定400/800/1600ステップのRK4で積分。独立非線形参照は偏差をηで尺度化してRadau/BDFで求め、早期のE・I線形化は2×2行列指数の両モードを使います。

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

## 比較・検証

t≤20の全ODE積分誤差・人口保存・非負性と、0≤t≤1の201参照点での線形化モデル誤差を分けます。参照では両ηの尺度付きJacobian、Radau/BDF差とη²に対する余裕、解析的な全行列指数を別資格しています。

## 確認の限界

2つの小初期感染量による固定係数の整合性比較です。早期線形化をt=20全体の厳密解と見なさず、単一の優勢モードで両モードを置き換えません。実流行の予測・統計的被覆・任意人口への一般保証は行いません。

## 元の数値目標と未達の結果

実行・記録の検証合格は、元の精度目標の全達成を意味しません。元の判定を保持します。

```json
{
  "original_target_results": {
    "seir-1e-4-400:integration": true,
    "seir-1e-4-400:mass": true,
    "seir-1e-4-400:negative-part": true,
    "seir-1e-4-800:integration": true,
    "seir-1e-4-800:mass": true,
    "seir-1e-4-800:negative-part": true,
    "seir-1e-4-1600:integration": true,
    "seir-1e-4-1600:mass": true,
    "seir-1e-4-1600:negative-part": true,
    "seir-1e-4:early-linearization": true,
    "seir-5e-5-400:integration": true,
    "seir-5e-5-400:mass": true,
    "seir-5e-5-400:negative-part": true,
    "seir-5e-5-800:integration": true,
    "seir-5e-5-800:mass": true,
    "seir-5e-5-800:negative-part": true,
    "seir-5e-5-1600:integration": true,
    "seir-5e-5-1600:mass": true,
    "seir-5e-5-1600:negative-part": true,
    "seir-5e-5:early-linearization": true
  },
  "original_target_summary": {
    "met": 20,
    "total": 20,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## 保存実測値と判定

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "seir-1e-4-400:actual-grid-finite": true,
    "seir-1e-4-800:actual-grid-finite": true,
    "seir-1e-4-1600:actual-grid-finite": true,
    "seir-5e-5-400:actual-grid-finite": true,
    "seir-5e-5-800:actual-grid-finite": true,
    "seir-5e-5-1600:actual-grid-finite": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/index.json

![人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

人口保存と2モードの初期線形化を別々に検査します。 保存値だけを描画します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- The Mathematics of Infectious Diseases [accessed 2026-11-24]. https://math.uchicago.edu/~shmuel/Modeling/hethcote2000%20Mathematics%20of%20Infectious%20diseases.pdf; review_level=selected-primary-body
Header, selected introduction compartment definitions and §3.1 printedpp618–619, displayed mass-action numbers and Eq(3.1); search around3.2/SEIR limit. Not whole55pages or visual diagram audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# SEIR conservation and initial linearization

Check population conservation and the full two-mode initial linearization separately.

**Methods used**

- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) (`rk4`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-algorithm)

Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

- [Closed SEIR compartment model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#seir-compartment-en) (`seir-compartment`)

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.


**Problem figure**

![SEIR conservation and initial linearization: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en) (`seir-linearization`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/seir-linearization/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/?lang=en#seir-linearization-en-validation)

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

- [SEIR conservation and initial linearization](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-seir-linearization-en) (`seir-linearization`; Same-problem reference · Finite-grid numerical reference)

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.
## Assumptions, units and boundaries

Use a closed population S+E+I+R=1 with β=0.6, σ=0.3 and γ=0.2. For η=10⁻⁴ or 5×10⁻⁵, start from (1−2η,η,η,0) and evolve to t=20. There are no births, deaths or external inflows.

**Editorial clarification**

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed. Time, concentrations and populations do not define a spatial dimension. The rates are educational, not disease or experimental predictions.

## Adopted numerical method

Evolve all four physical states with RK4 at 400, 800 and 1600 fixed steps. Independently compute the nonlinear reference with scaled-deviation Radau/BDF and the early E/I linearization with both modes of the full 2×2 matrix exponential.

$$
\begin{aligned}\dot S&=-\beta SI,&\dot E&=\beta SI-\sigma E,\\\dot I&=\sigma E-\gamma I,&\dot R&=\gamma I.\end{aligned}
$$

$$
\beta=0.6,\quad\sigma=0.3,\quad\gamma=0.2,\quad(S,E,I,R)(0)=(1-2\eta,\eta,\eta,0)
$$

$$
S+E+I+R=1,\quad\eta\in\{10^{-4},5\times10^{-5}\}
$$

$$
\begin{pmatrix}E_{\rm lin}(t)\\ I_{\rm lin}(t)\end{pmatrix}=\exp\!\left[t\begin{pmatrix}-0.3&0.6\\0.3&-0.2\end{pmatrix}\right]\begin{pmatrix}\eta\\\eta\end{pmatrix}
$$

## References and validation

Separate full-ODE integration error, population conservation and nonnegativity through t=20 from linearization-model error at 201 reference points on 0≤t≤1. Qualify scaled Jacobians, Radau/BDF agreement with an η² margin and the analytic full matrix exponential independently.

## Limits

These fixed-coefficient calculations compare two small initial infection levels. The early linearization is not an exact solution through t=20, and a single dominant mode does not replace the two-mode solution. No epidemic forecast, statistical coverage or arbitrary-population guarantee is claimed.

## Original numerical targets and unmet outcomes

Passing reproduction/reporting verification does not mean that all original accuracy goals were met. Original decisions are retained.

```json
{
  "original_target_results": {
    "seir-1e-4-400:integration": true,
    "seir-1e-4-400:mass": true,
    "seir-1e-4-400:negative-part": true,
    "seir-1e-4-800:integration": true,
    "seir-1e-4-800:mass": true,
    "seir-1e-4-800:negative-part": true,
    "seir-1e-4-1600:integration": true,
    "seir-1e-4-1600:mass": true,
    "seir-1e-4-1600:negative-part": true,
    "seir-1e-4:early-linearization": true,
    "seir-5e-5-400:integration": true,
    "seir-5e-5-400:mass": true,
    "seir-5e-5-400:negative-part": true,
    "seir-5e-5-800:integration": true,
    "seir-5e-5-800:mass": true,
    "seir-5e-5-800:negative-part": true,
    "seir-5e-5-1600:integration": true,
    "seir-5e-5-1600:mass": true,
    "seir-5e-5-1600:negative-part": true,
    "seir-5e-5:early-linearization": true
  },
  "original_target_summary": {
    "met": 20,
    "total": 20,
    "all_met": true,
    "acceptance_sha256": "b468e78459cf81bda6a32cade0051f6615b44def256c66308ae7acc82ff516ce"
  }
}
```

## Stored measurements and decisions

```json
{
  "metrics": {
    "actual_primary_records": 6,
    "reference_role": "Qualified Radau/BDF full ODE; reduction/linearization errors are distinct modeling diagnostics"
  },
  "checks": {
    "seir-1e-4-400:actual-grid-finite": true,
    "seir-1e-4-800:actual-grid-finite": true,
    "seir-1e-4-1600:actual-grid-finite": true,
    "seir-5e-5-400:actual-grid-finite": true,
    "seir-5e-5-800:actual-grid-finite": true,
    "seir-5e-5-1600:actual-grid-finite": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/seir-linearization/index.json

![Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/seir-linearization-preview.png)

Check population conservation and the full two-mode initial linearization separately. This figure reads saved data only.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/atlas-small-models-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/small-models/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- The Mathematics of Infectious Diseases [accessed 2026-11-24]. https://math.uchicago.edu/~shmuel/Modeling/hethcote2000%20Mathematics%20of%20Infectious%20diseases.pdf; review_level=selected-primary-body
Header, selected introduction compartment definitions and §3.1 printedpp618–619, displayed mass-action numbers and Eq(3.1); search around3.2/SEIR limit. Not whole55pages or visual diagram audit.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
