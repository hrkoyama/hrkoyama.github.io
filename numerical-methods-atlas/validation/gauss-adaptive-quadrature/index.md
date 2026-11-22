# Gauss–Legendreと適応求積：厳密次数・推定誤差・予算切れ

Legendreの3項漸化式からGauss節点と重みを構成し、2n−1次までの多項式モーメントと指数関数を検査します。適応Simpsonは指数関数とLorentz型ピークを積分し、解析積分・独立QUADPACKと比較します。

## 前提・単位・境界

有限区間上の滑らかな実関数、無次元の積分です。固定Gauss次数2・4・8・16と、適応絶対公差10⁻⁵・10⁻⁷・10⁻⁹を別々に走査します。両端特異点・不連続・無限区間は今回の入力では扱いません。

## 採用した計算法

Golub–Welschで対称Jacobi行列の固有値を節点、最初の固有ベクトル成分の平方の2倍を重みとします。適応Simpsonは区間を二分し、|S左+S右−S全|/15を局所推定として公差を配分します。評価回数と深さの上限を持ち、未達を成功としません。

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

## 比較・検証

全指定次数の多項式モーメント、SciPy roots_legendreの節点・重みとの差、解析exp積分の次数収束、解析atan積分とSciPy quadへの一致を測ります。公差を厳しくしたときの評価数と誤差を示し、5評価の強制予算切れ、非有限関数値も検査します。

## 確認の限界

Simpsonの局所推定は任意の関数に対する厳密な誤差上界ではありません。高周波の見落とし、特異点、丸め誤差の停滞を一般に解決する実装ではなく、Gauss–KronrodやQUADPACK全体の再実装でもありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "max_polynomial_moment_error": 8.881784197001252e-16,
    "max_scipy_rule_error": 1.2490009027033011e-15,
    "gauss_final_exp_error": 0.0,
    "max_adaptive_error_over_tolerance": 0.01729971494390803,
    "budget_failure_evaluations": 5
  },
  "checks": {
    "gauss_polynomial_moments": true,
    "independent_scipy_gauss_rule": true,
    "gauss_nonsingular_refinement": true,
    "adaptive_exact_and_quad_references": true,
    "evaluation_budget_failure_reported": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

## 出典と確認範囲

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Gauss–Legendre and adaptive quadrature: exactness, error estimates and budgets

Construct Gaussian nodes/weights from the Legendre recurrence and test polynomial moments through degree 2n−1 and an exponential. Adaptive Simpson integrates exponential and Lorentzian peaks, against analytic integrals and independent QUADPACK.

## Assumptions, units and boundaries

Dimensionless smooth real functions on finite intervals. Fixed Gauss orders 2/4/8/16 and adaptive absolute tolerances 10⁻⁵/10⁻⁷/10⁻⁹ are swept separately. Endpoint singularities, discontinuities and infinite intervals are not covered by these inputs.

## Adopted numerical method

Golub–Welsch obtains nodes from a symmetric Jacobi matrix and weights from twice the squared first eigenvector components. Adaptive Simpson bisects intervals and allocates tolerances using |Sleft+Sright−Swhole|/15 as a local estimate. Evaluation and depth limits report unmet targets explicitly.

$$
\int_{-1}^{1}f(x)\,dx\simeq\sum_{j=1}^{n}w_jf(x_j)
$$

$$
E_{\mathrm{est}}=|S_{\mathrm{left}}+S_{\mathrm{right}}-S_{\mathrm{whole}}|/15
$$

## References and validation

Measure polynomial moments for every chosen order, node/weight differences from SciPy roots_legendre, order refinement for the analytic exponential integral, and agreement with analytic arctangent and SciPy quad references. Store evaluation counts/errors as tolerance tightens; test forced exhaustion after five evaluations and nonfinite integrands.

## Limits

The local Simpson estimate is not a rigorous error bound for arbitrary functions. The implementation does not generally solve missed high frequencies, singularities or roundoff stagnation, and it is not a reimplementation of Gauss–Kronrod or all of QUADPACK.

## Stored measurements and decisions

```json
{
  "metrics": {
    "max_polynomial_moment_error": 8.881784197001252e-16,
    "max_scipy_rule_error": 1.2490009027033011e-15,
    "gauss_final_exp_error": 0.0,
    "max_adaptive_error_over_tolerance": 0.01729971494390803,
    "budget_failure_evaluations": 5
  },
  "checks": {
    "gauss_polynomial_moments": true,
    "independent_scipy_gauss_rule": true,
    "gauss_nonsingular_refinement": true,
    "adaptive_exact_and_quad_references": true,
    "evaluation_budget_failure_reported": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/gauss-adaptive-quadrature/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

## Sources and review scope

- G. H. Golub and J. H. Welsch (1969). Calculation of Gauss Quadrature Rules. https://www.ams.org/journals/mcom/1969-23-106/S0025-5718-69-99647-1/S0025-5718-69-99647-1.pdf; review_level=publisher-search-first-page-and-metadata
- J. N. Lyness (1969). Notes on the Adaptive Simpson Quadrature Routine. https://dl.acm.org/doi/10.1145/321526.321537; review_level=publisher-metadata

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
