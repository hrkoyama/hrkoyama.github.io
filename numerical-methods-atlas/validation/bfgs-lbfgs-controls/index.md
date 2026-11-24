# 既知最小点でのBFGSと3組L-BFGS

8次元SPD二次関数と3初期値のRosenbrockを用い、曲率・strong Wolfe・現在の有限記憶作用を検査します。

**使用手法**

- [勾配法・準Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja) (`optimization`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-algorithm)

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

- [有限次元代数最適化と既知最小点](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-optimization-ja) (`finite-dimensional-optimization`)

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。


**問題の図**

![既知最小点でのBFGSと3組L-BFGS：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[既知最小点でのBFGSと3組L-BFGS](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja) (`bfgs-lbfgs-controls`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=ja#bfgs-lbfgs-controls-ja-validation)

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

- [既知最小点と現在の有限記憶作用に対する解析参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bfgs-lbfgs-controls-ja) (`bfgs-lbfgs-controls`; 同じ問題の参照 · 解析参照)

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。
## 前提・単位・境界

無次元の非有界代数的最適化。既知の解析最小点を持ち、物理PDEの境界条件はありません。

**編集上の補足**

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。 図の座標は有限次元の変数・反復・診断で、物理空間の次元やPDE境界を表しません。

## 採用した計算法

独自逆BFGSとベクトルだけの2-loop L-BFGS（3組）。独立な小稠密oracleは現在γ₀Iから現在保持する組だけを古い順に再生。SciPy BFGS/L-BFGS-B（bounds=None）を別実装として比較。

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

## 比較・検証

16固定fit、解析的な最小点・勾配、各受理stepのstrong Wolfeと解像された正曲率、BFGSの対称SPD、L-BFGS作用差を判定。保持組とoracle稠密行列の記憶を分離。

## 確認の限界

厳密線形探索ではないためn反復終了や一般的Rosenbrock大域収束を主張しません。原著選択箇所は弱Wolfeであり、本例のstrong Wolfeと区別。Fletcher1970本文は未読です。

## 保存実測値と判定

```json
{
  "metrics": {
    "attempted_fits": 16,
    "completed_fits": 16,
    "expected_fits": 16,
    "objective_evaluations": 722,
    "maximum_gradient_inf": 9.090384658211326e-08,
    "independent_target": "known analytic minima; current-scaling retained-pair dense action"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-point": true,
    "fit-0-gradient": true,
    "fit-0-strong-wolfe": true,
    "fit-0-resolved-curvature": true,
    "fit-0-inverse-symmetry": true,
    "fit-0-inverse-spd": true,
    "fit-1-complete": true,
    "fit-1-point": true,
    "fit-1-gradient": true,
    "fit-1-strong-wolfe": true,
    "fit-1-resolved-curvature": true,
    "fit-1-retained-dense-oracle": true,
    "fit-2-complete": true,
    "fit-2-point": true,
    "fit-2-gradient": true,
    "fit-3-complete": true,
    "fit-3-point": true,
    "fit-3-gradient": true,
    "fit-4-complete": true,
    "fit-4-point": true,
    "fit-4-gradient": true,
    "fit-4-objective": true,
    "fit-4-strong-wolfe": true,
    "fit-4-resolved-curvature": true,
    "fit-4-inverse-symmetry": true,
    "fit-4-inverse-spd": true,
    "fit-5-complete": true,
    "fit-5-point": true,
    "fit-5-gradient": true,
    "fit-5-objective": true,
    "fit-5-strong-wolfe": true,
    "fit-5-resolved-curvature": true,
    "fit-5-retained-dense-oracle": true,
    "fit-6-complete": true,
    "fit-6-point": true,
    "fit-6-gradient": true,
    "fit-6-objective": true,
    "fit-7-complete": true,
    "fit-7-point": true,
    "fit-7-gradient": true,
    "fit-7-objective": true,
    "fit-8-complete": true,
    "fit-8-point": true,
    "fit-8-gradient": true,
    "fit-8-objective": true,
    "fit-8-strong-wolfe": true,
    "fit-8-resolved-curvature": true,
    "fit-8-inverse-symmetry": true,
    "fit-8-inverse-spd": true,
    "fit-9-complete": true,
    "fit-9-point": true,
    "fit-9-gradient": true,
    "fit-9-objective": true,
    "fit-9-strong-wolfe": true,
    "fit-9-resolved-curvature": true,
    "fit-9-retained-dense-oracle": true,
    "fit-10-complete": true,
    "fit-10-point": true,
    "fit-10-gradient": true,
    "fit-10-objective": true,
    "fit-11-complete": true,
    "fit-11-point": true,
    "fit-11-gradient": true,
    "fit-11-objective": true,
    "fit-12-complete": true,
    "fit-12-point": true,
    "fit-12-gradient": true,
    "fit-12-objective": true,
    "fit-12-strong-wolfe": true,
    "fit-12-resolved-curvature": true,
    "fit-12-inverse-symmetry": true,
    "fit-12-inverse-spd": true,
    "fit-13-complete": true,
    "fit-13-point": true,
    "fit-13-gradient": true,
    "fit-13-objective": true,
    "fit-13-strong-wolfe": true,
    "fit-13-resolved-curvature": true,
    "fit-13-retained-dense-oracle": true,
    "fit-14-complete": true,
    "fit-14-point": true,
    "fit-14-gradient": true,
    "fit-14-objective": true,
    "fit-15-complete": true,
    "fit-15-point": true,
    "fit-15-gradient": true,
    "fit-15-objective": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/index.json

![実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

実際のRosenbrock反復点と解析目的関数の等高線。3つの固定初期値・4手法を示し、全問題での収束保証ではありません。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- On the limited memory BFGS method for large scale optimization [accessed 2026-11-24]. https://users.iems.northwestern.edu/~nocedal/PDFfiles/limited-memory.pdf; review_level=selected-primary-scope
Author-hosted PDF selected physical pages 3–5 (printed 2–4), rendered locally and visually inspected: limited storage, deletion of oldest correction, Eq. (2.1) inverse-BFGS, Algorithm 2.1 and Eq. (2.6) retained-update construction. No full-paper/proof/experiment or Section 4 scaling review. The selected original uses weak Wolfe; this study deliberately uses a separately specified strong-Wolfe line search. Current-gamma least-squares scaling is independently derived here, not attributed to unread text.

- SciPy 1.14.1 line_search documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.line_search.html; review_level=selected-primary-scope
Signature, c1/c2, descent-direction requirement, returned failure None and evaluation counts. Cited textbook pages were not read.

- SciPy 1.14.1 BFGS documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-bfgs.html; review_level=selected-primary-scope
Options gtol, norm, c1/c2, hess_inv0 and precision-loss notes; no claim of reading a BFGS original paper.

- SciPy 1.14.1 L-BFGS-B documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-lbfgsb.html; review_level=selected-primary-scope
Options maxcor, ftol, gtol/projected-gradient convention, maxfun, maxiter and maxls.

- A new approach to variable metric algorithms. https://academic.oup.com/comjnl/article-abstract/13/3/317/345520?login=false; review_level=bibliography-only-original-unread
Prior saved publisher metadata/abstract-search record only. Original article full text remains unavailable/unread; no new request was made and no derivation is claimed to have been checked against it.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# BFGS and three-pair L-BFGS at known minima

An eight-dimensional SPD quadratic and three Rosenbrock starts test curvature, strong Wolfe conditions and the current finite-memory action.

**Methods used**

- [Gradient and quasi-Newton optimization](https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=en) (`optimization`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-algorithm)

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

- [Finite-dimensional algebraic optimization and known minima](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-dimensional-optimization-en) (`finite-dimensional-optimization`)

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.


**Problem figure**

![BFGS and three-pair L-BFGS at known minima: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[BFGS and three-pair L-BFGS at known minima](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en) (`bfgs-lbfgs-controls`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bfgs-lbfgs-controls/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/?lang=en#bfgs-lbfgs-controls-en-validation)

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

- [Analytic known minima and the current limited-memory action](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bfgs-lbfgs-controls-en) (`bfgs-lbfgs-controls`; Same-problem reference · Analytic reference)

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.
## Assumptions, units and boundaries

Dimensionless unconstrained algebraic optimization with known analytic minima; there is no physical PDE boundary condition.

**Editorial clarification**

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread. Plot axes describe finite-dimensional variables, iterations or diagnostics, not a physical spatial dimension or PDE boundary.

## Adopted numerical method

Original inverse-BFGS and vector-only two-loop L-BFGS with three pairs. A separate small dense oracle replays only currently retained pairs from the current gamma0 I. SciPy BFGS and unbounded L-BFGS-B are distinct software companions.

$$
H_+=(I-\rho s y^T)H(I-\rho y s^T)+\rho s s^T
$$

$$
\rho=(y^Ts)^{-1},\quad\gamma_0=(s^Ty)/(y^Ty)
$$

$$
f(x,y)=100(y-x^2)^2+(1-x)^2
$$

## References and validation

Sixteen fixed fits check analytic minima/gradients, strong Wolfe and resolved positive curvature at every accepted step, symmetric SPD BFGS matrices and L-BFGS action defects. Retained-pair and dense-oracle storage are reported separately.

## Limits

No exact n-step termination or general global convergence on Rosenbrock is claimed. The selected original text uses weak Wolfe, distinct from this study’s strong Wolfe policy. Fletcher’s 1970 original article remains unread.

## Stored measurements and decisions

```json
{
  "metrics": {
    "attempted_fits": 16,
    "completed_fits": 16,
    "expected_fits": 16,
    "objective_evaluations": 722,
    "maximum_gradient_inf": 9.090384658211326e-08,
    "independent_target": "known analytic minima; current-scaling retained-pair dense action"
  },
  "checks": {
    "fit-0-complete": true,
    "fit-0-point": true,
    "fit-0-gradient": true,
    "fit-0-strong-wolfe": true,
    "fit-0-resolved-curvature": true,
    "fit-0-inverse-symmetry": true,
    "fit-0-inverse-spd": true,
    "fit-1-complete": true,
    "fit-1-point": true,
    "fit-1-gradient": true,
    "fit-1-strong-wolfe": true,
    "fit-1-resolved-curvature": true,
    "fit-1-retained-dense-oracle": true,
    "fit-2-complete": true,
    "fit-2-point": true,
    "fit-2-gradient": true,
    "fit-3-complete": true,
    "fit-3-point": true,
    "fit-3-gradient": true,
    "fit-4-complete": true,
    "fit-4-point": true,
    "fit-4-gradient": true,
    "fit-4-objective": true,
    "fit-4-strong-wolfe": true,
    "fit-4-resolved-curvature": true,
    "fit-4-inverse-symmetry": true,
    "fit-4-inverse-spd": true,
    "fit-5-complete": true,
    "fit-5-point": true,
    "fit-5-gradient": true,
    "fit-5-objective": true,
    "fit-5-strong-wolfe": true,
    "fit-5-resolved-curvature": true,
    "fit-5-retained-dense-oracle": true,
    "fit-6-complete": true,
    "fit-6-point": true,
    "fit-6-gradient": true,
    "fit-6-objective": true,
    "fit-7-complete": true,
    "fit-7-point": true,
    "fit-7-gradient": true,
    "fit-7-objective": true,
    "fit-8-complete": true,
    "fit-8-point": true,
    "fit-8-gradient": true,
    "fit-8-objective": true,
    "fit-8-strong-wolfe": true,
    "fit-8-resolved-curvature": true,
    "fit-8-inverse-symmetry": true,
    "fit-8-inverse-spd": true,
    "fit-9-complete": true,
    "fit-9-point": true,
    "fit-9-gradient": true,
    "fit-9-objective": true,
    "fit-9-strong-wolfe": true,
    "fit-9-resolved-curvature": true,
    "fit-9-retained-dense-oracle": true,
    "fit-10-complete": true,
    "fit-10-point": true,
    "fit-10-gradient": true,
    "fit-10-objective": true,
    "fit-11-complete": true,
    "fit-11-point": true,
    "fit-11-gradient": true,
    "fit-11-objective": true,
    "fit-12-complete": true,
    "fit-12-point": true,
    "fit-12-gradient": true,
    "fit-12-objective": true,
    "fit-12-strong-wolfe": true,
    "fit-12-resolved-curvature": true,
    "fit-12-inverse-symmetry": true,
    "fit-12-inverse-spd": true,
    "fit-13-complete": true,
    "fit-13-point": true,
    "fit-13-gradient": true,
    "fit-13-objective": true,
    "fit-13-strong-wolfe": true,
    "fit-13-resolved-curvature": true,
    "fit-13-retained-dense-oracle": true,
    "fit-14-complete": true,
    "fit-14-point": true,
    "fit-14-gradient": true,
    "fit-14-objective": true,
    "fit-15-complete": true,
    "fit-15-point": true,
    "fit-15-gradient": true,
    "fit-15-objective": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/bfgs-lbfgs-controls/index.json

![Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee.](https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/bfgs-lbfgs-controls-preview.png)

Actual Rosenbrock iterates on analytic objective contours for three fixed starts and four methods; this is not a general convergence guarantee.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/atlas-inverse-optimization-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/inverse-optimization/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- On the limited memory BFGS method for large scale optimization [accessed 2026-11-24]. https://users.iems.northwestern.edu/~nocedal/PDFfiles/limited-memory.pdf; review_level=selected-primary-scope
Author-hosted PDF selected physical pages 3–5 (printed 2–4), rendered locally and visually inspected: limited storage, deletion of oldest correction, Eq. (2.1) inverse-BFGS, Algorithm 2.1 and Eq. (2.6) retained-update construction. No full-paper/proof/experiment or Section 4 scaling review. The selected original uses weak Wolfe; this study deliberately uses a separately specified strong-Wolfe line search. Current-gamma least-squares scaling is independently derived here, not attributed to unread text.

- SciPy 1.14.1 line_search documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.optimize.line_search.html; review_level=selected-primary-scope
Signature, c1/c2, descent-direction requirement, returned failure None and evaluation counts. Cited textbook pages were not read.

- SciPy 1.14.1 BFGS documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-bfgs.html; review_level=selected-primary-scope
Options gtol, norm, c1/c2, hess_inv0 and precision-loss notes; no claim of reading a BFGS original paper.

- SciPy 1.14.1 L-BFGS-B documentation [accessed 2026-11-24]. https://docs.scipy.org/doc/scipy-1.14.1/reference/optimize.minimize-lbfgsb.html; review_level=selected-primary-scope
Options maxcor, ftol, gtol/projected-gradient convention, maxfun, maxiter and maxls.

- A new approach to variable metric algorithms. https://academic.oup.com/comjnl/article-abstract/13/3/317/345520?login=false; review_level=bibliography-only-original-unread
Prior saved publisher metadata/abstract-search record only. Original article full text remains unavailable/unread; no new request was made and no derivation is claimed to have been checked against it.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
