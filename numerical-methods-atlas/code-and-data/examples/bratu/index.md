# 1D Bratu: Newton–GMRES on the lower branch / 1次元Bratu：小さい枝のNewton–GMRES

Entry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/
Registry: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json
Source record: bratu

Public-file rerun: passed
Receipt: https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/verification/2026-11-22-forces.json

## ja

小さい枝をNewton–GMRESで求め、解析解・独立な非線形残差・2次格子収束を確認する。

**使用手法**

- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この固定入力の問題式と条件](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-bratu-ja)

31/63/127内部点、零初期値で小さい枝を選ぶ。βtanh(β/2)<2の枝を対象とし、大きい枝や分岐点の追跡を行わない。

$$
-u''=\lambda e^u,\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=2\log\frac{\cosh(\beta/2)}{\cosh[\beta(x-1/2)]},\qquad \lambda=\frac{2\beta^2}{\cosh^2(\beta/2)},\quad\beta=1
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

**問題の図**

![公開コード版を固定条件で実行して作成した計算結果。条件・値・検査結果を添付。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

この問題の代表図です。格子・時刻・初期値などは、この実行例の固定入力と異なる場合があります。

[1次元Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja) (`bratu`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja#bratu-ja-validation)

CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。

- [1次元Bratu：小さい枝のNewton–GMRES](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-lower-branch-analytic-ja) (`bratu-lower-branch-analytic`; 同じ問題の参照 · 解析参照)

既存の固定入力・保存結果に対応する解析参照カードを追加。解析式、点・時刻・動径の標本化、配布版SHAと実行コードを相互に辿れます。過去の計算を再実行した記録ではありません。


### scope

−u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。

### assumptions

既存の残差十分減少による減衰NewtonとILU(0)付きGMRES。解析解u=2log[cosh(β/2)/cosh(β(x−1/2))]。βtanh(β/2)<2で小さい枝を選び、初期値は全点零。内部Newton制御は非線形許容値1e-10、最大30反復。

### units

xとuは無次元。λは本規約で無次元化され、次元座標なら逆長さ²に対応する。残差は境界を除いた全内部点のEuclideanノルム。

### boundaries

x∈[0,1]、u(0)=u(1)=0。CSVに両端も含める。

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json
Input SHA-256: dc20c276f82f6dee68843ccc1cd7e225719bfea103cf2b8715a0a4091955eea9
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/bratu.json --output output-bratu
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/solution.csv

CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。

### Numerical acceptance

- nonlinear-convergence / 全格子でNewton–GMRESが指定の非線形残差許容値に到達する。: /metrics/all_converged; value = true
- lower-branch-continuous-error / β=1の小さい枝の解析解と一致する。127内部点の2次離散誤差に余裕を持つ上限。: /metrics/finest_linf_error; value ≤ 1e-05
- second-order-refinement / 小さい枝で格子幅半減により連続解誤差が2次で減る。: /metrics/minimum_observed_order; value ≥ 1.8
- independent-nonlinear-residual / 独立に再評価した非線形差分残差のEuclideanノルム。: /metrics/maximum_independent_residual_l2; value ≤ 1e-08
- dirichlet-boundary / 両端の零Dirichlet条件。: /metrics/boundary_maximum_absolute_value; value ≤ 1e-14
- all-criteria / 全数値条件の判定: /checks; all values = true
- input-provenance / 実行した固定入力のSHA-256: /input_sha256; value = dc20c276f82f6dee68843ccc1cd7e225719bfea103cf2b8715a0a4091955eea9
- case-passed / 入力に記載した条件の合格: /passed; value = true

### Failure and scope

小さい枝・零初期値・固定境界の指定を要求する。大きい枝、臨界点近傍の追跡、分岐、任意初期値からの大域収束は保証しない。解の細格子値を解析解とは呼ばない。

Reading: https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/

### References

- CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json
- λと解析解を同じβから独立に評価し、2β²の係数を落とさない。: https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/
- 既存Newton項目の十分減少・半減の文献。本例に原論文の最小化定理を直接適用する主張ではない。: https://doi.org/10.2140/pjm.1966.16.1
- 既存Newton項目の近似内部線形解法の文献。本レシピ固有の収束定理の証明ではない。: https://doi.org/10.1137/0719025

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
自作コードはMIT。入力・数値データ・図・本文はサイトの個別条件に従います。この台帳は利用許諾を拡大しません。

## en

Compute the lower branch with Newton–GMRES and check its analytic solution, recomputed nonlinear residual and second-order refinement.

**Methods used**

- [Armijo-damped Newton](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=en) (`newton`)

**Equations**

[This fixed-input problem and its conditions](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#execution-bratu-en)

31/63/127 interior nodes and a zero initial guess select the lower branch with βtanh(β/2)<2; no upper-branch or bifurcation tracking.

$$
-u''=\lambda e^u,\qquad u(0)=u(1)=0
$$

$$
u_{\rm ref}(x)=2\log\frac{\cosh(\beta/2)}{\cosh[\beta(x-1/2)]},\qquad \lambda=\frac{2\beta^2}{\cosh^2(\beta/2)},\quad\beta=1
$$

- [Bratu nonlinear boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bratu-en) (`bratu`)

**Problem figure**

![Calculated from the public code edition with fixed inputs; inputs, values and checks are linked.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png)

A representative figure for the problem. Its grid, time and initial data may differ from this execution’s fixed input.

[One-dimensional Bratu boundary-value problem](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en) (`bratu`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=en#bratu-en-validation)

CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.

- [1D Bratu: Newton–GMRES on the lower branch](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-bratu-lower-branch-analytic-en) (`bratu-lower-branch-analytic`; Same-problem reference · Analytic reference)

An analytic reference card now links the existing fixed inputs and saved results: formula, point/time/radial sampling, edition SHA and executable code. This metadata registration is not a new execution.


### scope

Solve the lower branch of −u''=λexp(u), with β=1 and λ=2β²/cosh²(β/2), starting at zero. Check the analytic solution, recomputed nonlinear residual and second-order refinement on 31/63/127 interior nodes.

### assumptions

Existing residual-decrease damped Newton and ILU(0)-GMRES. Analytic u=2log[cosh(β/2)/cosh(β(x−1/2))]. βtanh(β/2)<2 selects the lower branch and all initial unknowns are zero. Nonlinear tolerance is 1e-10 with at most 30 Newton iterations.

### units

Dimensionless x and u; λ is nondimensional here and scales as inverse length squared for dimensional coordinates. Residuals use the Euclidean norm of interior equations.

### boundaries

x∈[0,1], u(0)=u(1)=0; CSV includes both endpoints.

### Input and run

Input: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/recipes/bratu.json
Input SHA-256: dc20c276f82f6dee68843ccc1cd7e225719bfea103cf2b8715a0a4091955eea9
ZIP: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/atlas-code-2026-11-22.zip
Run from: atlas-code-2026-11-22

```sh
python -m pip install -r requirements.txt
python run_recipe.py --input recipes/bratu.json --output output-bratu
```

### Outputs

- result.json (json): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json
- solution.csv (csv): https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/solution.csv

CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.

### Numerical acceptance

- nonlinear-convergence / Newton–GMRES reaches its nonlinear residual tolerance on every grid.: /metrics/all_converged; value = true
- lower-branch-continuous-error / Agreement with the analytic lower branch at β=1; margin above the second-order error at 127 interior nodes.: /metrics/finest_linf_error; value ≤ 1e-05
- second-order-refinement / Second-order continuous-solution error reduction on the lower branch.: /metrics/minimum_observed_order; value ≥ 1.8
- independent-nonlinear-residual / Euclidean norm of the independently recomputed nonlinear difference residual.: /metrics/maximum_independent_residual_l2; value ≤ 1e-08
- dirichlet-boundary / Zero Dirichlet values at both endpoints.: /metrics/boundary_maximum_absolute_value; value ≤ 1e-14
- all-criteria / All numerical acceptance flags: /checks; all values = true
- input-provenance / SHA-256 of the executed fixed input: /input_sha256; value = dc20c276f82f6dee68843ccc1cd7e225719bfea103cf2b8715a0a4091955eea9
- case-passed / Acceptance conditions in the input passed: /passed; value = true

### Failure and scope

Require the lower-branch declaration, zero initial guess and fixed boundaries. No upper-branch continuation, critical-point tracking, bifurcation or global-convergence guarantee. Fine-grid solutions are not called analytic references.

Reading: https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/

### References

- CSV carries finest-grid numerical/analytic values and absolute error. JSON retains each mesh's nonlinear residual, Newton iteration count and minimum damping length.: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/reference/bratu/result.json
- Evaluate λ and the analytic solution independently from β, retaining the factor 2β².: https://hrkoyama.github.io/numerical-methods-atlas/en/read/sparse-nonlinear/
- Existing Newton-method source for sufficient decrease/halving, not direct application of the original minimization theorem.: https://doi.org/10.2140/pjm.1966.16.1
- Existing source for inexact Newton inner solves, not a proof specific to this recipe.: https://doi.org/10.1137/0719025

Code license: https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-22/LICENSE
Content/data terms: https://hrkoyama.github.io/rights/
Original code is MIT. Inputs, numerical data, figures and prose retain the site’s item-specific terms. This registry does not expand reuse permissions.
