# AMGの条件数・異方性・残差と前進誤差

49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

**使用手法**

- [代数的マルチグリッド（AMG）](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja) (`amg`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-algorithm)

MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![AMGの条件数・異方性・残差と前進誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=ja#amg-conditioning-ja-validation)

真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
## 前提・単位・境界

正方格子から作るA=T⊗I+εI⊗T、n=7/15/31、ε=1/.1/.01です。これは既知解を持つ代数系の診断であり、連続PDEの精度検証は既存Poisson例に残します。同じnではκ₂はεによらず一定です。

**編集上の補足**

これは行列の代数的な条件と反復誤差の診断であり、旧Poisson製造解の連続PDE精度の確認とは別です。同じ格子の異方性と2ノルム条件数は一致する指標ではありません。残差、解誤差、反復予算切れを区別します。

## 採用した計算法

MITライセンスの既存アトラス教材の平滑化集約AMGを新しい独立ソースへ再利用します。階層は行列だけから構築し、強度閾値.08、Jacobi平滑化、固定相対公差10⁻¹⁰、最大180 V-cycleを使います。DSTの正弦変換による直接反転は参照側だけです。

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

## 比較・検証

真の残差、独立直接解との差、DSTとの差、operator complexity、全残差履歴を保存します。最大固有値方向の右辺へ最小固有値方向の摂動を加え、相対増幅κ₂を直接解で照合します。等方例は収束必須、異方性stress例は予算終了も正直に記録する事前基準です。1-cycle対照は未収束を検出します。

## 確認の限界

固定した小規模な一定係数系列のみです。任意の係数ジャンプ、非構造格子、不定値系、最適計算量・一様収束を保証しません。異方性が常にκ₂を増やす、あるいは単調に収束を悪化させるとは主張しません。

## 保存実測値と判定

```json
{
  "metrics": {
    "maximum_condition_2": 414.3450622319016,
    "maximum_actual_relative_residual": 9.213509371626832e-11,
    "maximum_actual_forward_error": 6.249776614864638e-11,
    "stress_budget_exhaustions": 0,
    "maximum_condition_gain_relative_error": 3.2097435820332976e-11
  },
  "checks": {
    "n7-eps1-true-residual": true,
    "n7-eps1-forward-bound": true,
    "n7-eps1-condition-gain": true,
    "n7-eps1-complexity": true,
    "n7-eps1-independent-dst": true,
    "n7-eps1-resolved": true,
    "n7-eps0.1-true-residual": true,
    "n7-eps0.1-forward-bound": true,
    "n7-eps0.1-condition-gain": true,
    "n7-eps0.1-complexity": true,
    "n7-eps0.1-independent-dst": true,
    "n7-eps0.1-stress-honest": true,
    "n7-eps0.01-true-residual": true,
    "n7-eps0.01-forward-bound": true,
    "n7-eps0.01-condition-gain": true,
    "n7-eps0.01-complexity": true,
    "n7-eps0.01-independent-dst": true,
    "n7-eps0.01-stress-honest": true,
    "n7-independent-spectrum": true,
    "n15-eps1-true-residual": true,
    "n15-eps1-forward-bound": true,
    "n15-eps1-condition-gain": true,
    "n15-eps1-complexity": true,
    "n15-eps1-independent-dst": true,
    "n15-eps1-resolved": true,
    "n15-eps0.1-true-residual": true,
    "n15-eps0.1-forward-bound": true,
    "n15-eps0.1-condition-gain": true,
    "n15-eps0.1-complexity": true,
    "n15-eps0.1-independent-dst": true,
    "n15-eps0.1-stress-honest": true,
    "n15-eps0.01-true-residual": true,
    "n15-eps0.01-forward-bound": true,
    "n15-eps0.01-condition-gain": true,
    "n15-eps0.01-complexity": true,
    "n15-eps0.01-independent-dst": true,
    "n15-eps0.01-stress-honest": true,
    "n15-independent-spectrum": true,
    "n31-eps1-true-residual": true,
    "n31-eps1-forward-bound": true,
    "n31-eps1-condition-gain": true,
    "n31-eps1-complexity": true,
    "n31-eps1-independent-dst": true,
    "n31-eps1-resolved": true,
    "n31-eps0.1-true-residual": true,
    "n31-eps0.1-forward-bound": true,
    "n31-eps0.1-condition-gain": true,
    "n31-eps0.1-complexity": true,
    "n31-eps0.1-independent-dst": true,
    "n31-eps0.1-stress-honest": true,
    "n31-eps0.01-true-residual": true,
    "n31-eps0.01-forward-bound": true,
    "n31-eps0.01-condition-gain": true,
    "n31-eps0.01-complexity": true,
    "n31-eps0.01-independent-dst": true,
    "n31-eps0.01-stress-honest": true,
    "n31-independent-spectrum": true,
    "short-budget-failure-explicit": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://ww3.math.ucla.edu/camreport/cam99-29.pdf; review_level=author-hosted original preprint abstract and opening text via official university search extraction
弱近似性等の仮定に基づく理論と、教材の限られた行列系列での観測を区別します。任意異方性への頑健性は主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# AMG: conditioning, anisotropy, residual and forward error

Separate condition number from anisotropy on SPD systems of 49, 225 and 961 unknowns. Compare analytic spectra, independent sparse direct solutions and DST diagonalization, and measure how residual translates to forward error.

**Methods used**

- [Algebraic multigrid / AMG](https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=en) (`amg`)

**Equations**

[This example’s diagnostic and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-algorithm)

Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

No corresponding equation-registry entry is registered; consult the example-specific formulation, approximation or diagnostic above.

**Problem figure**

![AMG: conditioning, anisotropy, residual and forward error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/amg-conditioning.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

No separate physical test problem is assigned to this check or diagnostic. Its own diagnostic figure and validation material are provided.

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/?lang=en#amg-conditioning-en-validation)

Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.

No corresponding reference-library card is registered; execution-specific material above documents its reference values and acceptance checks.
## Assumptions, units and boundaries

A=T⊗I+εI⊗T with n=7/15/31 and ε=1/.1/.01. This is a known-solution algebraic diagnostic; continuum PDE validation remains in the earlier Poisson example. At fixed square n, κ₂ is independent of ε.

**Editorial clarification**

This diagnoses algebraic matrix conditioning and iteration error, separately from the earlier Poisson manufactured-solution PDE accuracy. Anisotropy and the 2-norm condition number need not vary together on a fixed grid. Distinguish residual, solution error and an exhausted iteration budget.

## Adopted numerical method

Reuse the earlier MIT-licensed Atlas educational smoothed-aggregation AMG in a separate source release. Matrix-only hierarchy setup uses strength .08, Jacobi smoothing, fixed relative tolerance 10⁻¹⁰ and at most 180 V-cycles. Sine-transform spectral inversion is reference-side only.

$$
\kappa_2(A)=\cot^2\!\left(\frac{\pi}{2(n+1)}\right)
$$

$$
\frac{\|x-\hat x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|b-A\hat x\|_2}{\|b\|_2}
$$

## References and validation

Store true residual, forward error, DST agreement, operator complexity and complete histories. Perturb a maximal-eigenmode RHS in the minimal-eigenmode direction and check the predicted relative amplification κ₂ with direct solves. Isotropic runs must converge; the predeclared anisotropy stress policy permits honestly reported budget exhaustion. A one-cycle control detects nonconvergence.

## Limits

Only a small constant-coefficient family is checked. Arbitrary coefficient jumps, unstructured grids, indefinite systems, optimal complexity and uniform convergence are outside scope. No claim that anisotropy necessarily increases κ₂ or monotonically worsens convergence.

## Stored measurements and decisions

```json
{
  "metrics": {
    "maximum_condition_2": 414.3450622319016,
    "maximum_actual_relative_residual": 9.213509371626832e-11,
    "maximum_actual_forward_error": 6.249776614864638e-11,
    "stress_budget_exhaustions": 0,
    "maximum_condition_gain_relative_error": 3.2097435820332976e-11
  },
  "checks": {
    "n7-eps1-true-residual": true,
    "n7-eps1-forward-bound": true,
    "n7-eps1-condition-gain": true,
    "n7-eps1-complexity": true,
    "n7-eps1-independent-dst": true,
    "n7-eps1-resolved": true,
    "n7-eps0.1-true-residual": true,
    "n7-eps0.1-forward-bound": true,
    "n7-eps0.1-condition-gain": true,
    "n7-eps0.1-complexity": true,
    "n7-eps0.1-independent-dst": true,
    "n7-eps0.1-stress-honest": true,
    "n7-eps0.01-true-residual": true,
    "n7-eps0.01-forward-bound": true,
    "n7-eps0.01-condition-gain": true,
    "n7-eps0.01-complexity": true,
    "n7-eps0.01-independent-dst": true,
    "n7-eps0.01-stress-honest": true,
    "n7-independent-spectrum": true,
    "n15-eps1-true-residual": true,
    "n15-eps1-forward-bound": true,
    "n15-eps1-condition-gain": true,
    "n15-eps1-complexity": true,
    "n15-eps1-independent-dst": true,
    "n15-eps1-resolved": true,
    "n15-eps0.1-true-residual": true,
    "n15-eps0.1-forward-bound": true,
    "n15-eps0.1-condition-gain": true,
    "n15-eps0.1-complexity": true,
    "n15-eps0.1-independent-dst": true,
    "n15-eps0.1-stress-honest": true,
    "n15-eps0.01-true-residual": true,
    "n15-eps0.01-forward-bound": true,
    "n15-eps0.01-condition-gain": true,
    "n15-eps0.01-complexity": true,
    "n15-eps0.01-independent-dst": true,
    "n15-eps0.01-stress-honest": true,
    "n15-independent-spectrum": true,
    "n31-eps1-true-residual": true,
    "n31-eps1-forward-bound": true,
    "n31-eps1-condition-gain": true,
    "n31-eps1-complexity": true,
    "n31-eps1-independent-dst": true,
    "n31-eps1-resolved": true,
    "n31-eps0.1-true-residual": true,
    "n31-eps0.1-forward-bound": true,
    "n31-eps0.1-condition-gain": true,
    "n31-eps0.1-complexity": true,
    "n31-eps0.1-independent-dst": true,
    "n31-eps0.1-stress-honest": true,
    "n31-eps0.01-true-residual": true,
    "n31-eps0.01-forward-bound": true,
    "n31-eps0.01-condition-gain": true,
    "n31-eps0.01-complexity": true,
    "n31-eps0.01-independent-dst": true,
    "n31-eps0.01-stress-honest": true,
    "n31-independent-spectrum": true,
    "short-budget-failure-explicit": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/amg-conditioning/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- P. Vaněk, J. Mandel and M. Brezina (1996). Algebraic multigrid by smoothed aggregation for second and fourth order elliptic problems. https://link.springer.com/article/10.1007/BF02238511; review_level=publisher-abstract-and-metadata
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://ww3.math.ucla.edu/camreport/cam99-29.pdf; review_level=author-hosted original preprint abstract and opening text via official university search extraction
Distinguish theory conditional on weak approximation and related assumptions from observations on a small matrix family; no general anisotropy robustness claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
