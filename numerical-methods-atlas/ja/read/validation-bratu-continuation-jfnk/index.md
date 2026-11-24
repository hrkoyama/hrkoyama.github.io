# Bratuのfold継続とJacobian不要Newton–Krylov

同じ1次元Bratu境界値問題で、foldを越える継続とJacobianを組み立てない反復を独立解析族へ照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 擬似弧長継続でBratuのfoldを越える

同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。

**使用手法**

- [重み付き擬似弧長継続](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja) (`pseudo-arclength-continuation`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-algorithm)

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。


**問題の図**

![擬似弧長継続でBratuのfoldを越える：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja) (`bratu-fold-continuation`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-validation)

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

- [擬似弧長継続でBratuのfoldを越える](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja) (`bratu-fold-continuation`; 同じ問題の参照 · 解析参照)

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。
### 前提・単位・境界

無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。

**編集上の補足**

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

### 採用した計算法

hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

### 比較・検証

保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。

### 確認の限界

小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "fold_orders": [
      2.0003257002223824,
      2.000081417263765
    ],
    "intended_failure_reason": "line search exhausted",
    "discrete_nonexistence_bound": 3.6300955492983498,
    "matching": "Fullpathfamilycoordinatefrommidpointisexplicit;separatefixedlambda2rootsvalidatebothbrancheswithoutparameterfitting.",
    "reference_qualification_max_ODE": 6e-78
  },
  "checks": {
    "N31/finite complete branch": true,
    "N31/discrete residual": true,
    "N31/unit tangent": true,
    "N31/tangent equation": true,
    "N31/tangent orientation": true,
    "N31/turning tangent": true,
    "N31/lower and upper lambda2 neighborhoods": true,
    "N31/fold discrete equation": true,
    "N31/fold null equation": true,
    "N31/fold null normalization": true,
    "N31/fold sigma_min": true,
    "N31/simple fold parameter transversality": true,
    "N31/simple fold quadratic transversality": true,
    "N31/lower discrete root": true,
    "N31/upper discrete root": true,
    "N31/ordered distinct branches": true,
    "N31/nonzero reference fields": true,
    "N63/finite complete branch": true,
    "N63/discrete residual": true,
    "N63/unit tangent": true,
    "N63/tangent equation": true,
    "N63/tangent orientation": true,
    "N63/turning tangent": true,
    "N63/lower and upper lambda2 neighborhoods": true,
    "N63/fold discrete equation": true,
    "N63/fold null equation": true,
    "N63/fold null normalization": true,
    "N63/fold sigma_min": true,
    "N63/simple fold parameter transversality": true,
    "N63/simple fold quadratic transversality": true,
    "N63/lower discrete root": true,
    "N63/upper discrete root": true,
    "N63/ordered distinct branches": true,
    "N63/nonzero reference fields": true,
    "N127/finite complete branch": true,
    "N127/discrete residual": true,
    "N127/unit tangent": true,
    "N127/tangent equation": true,
    "N127/tangent orientation": true,
    "N127/turning tangent": true,
    "N127/lower and upper lambda2 neighborhoods": true,
    "N127/fold discrete equation": true,
    "N127/fold null equation": true,
    "N127/fold null normalization": true,
    "N127/fold sigma_min": true,
    "N127/simple fold parameter transversality": true,
    "N127/simple fold quadratic transversality": true,
    "N127/lower discrete root": true,
    "N127/upper discrete root": true,
    "N127/ordered distinct branches": true,
    "N127/nonzero reference fields": true,
    "Decimal80 continuum ODE": true,
    "Decimal80 zero endpoints": true,
    "reference fixed lambda": true,
    "reference fold printed anchor": true,
    "no-solution lambda4 proof bound": true,
    "lambda4 Newton reports failure": true,
    "lambda4 finite retained states": true,
    "lambda4 remains above tolerance": true,
    "finest full path shape": true,
    "finest family curve lambda": true,
    "finest continuous fold error": true,
    "fold first refinement order": true,
    "fold second refinement order": true,
    "finest lower exact solution": true,
    "finest upper exact solution": true,
    "both branch errors refine": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/index.json

![保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png)

保存した分岐曲線、λ=2の上下枝、Jacobianの最小特異値、3格子のfold誤差を示す縮小図。擬似弧長stepは物理時間ではありません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- K.I.Dickson,C.T.Kelley,I.C.F.Ipsen,I.G.Kevrekidis (2007). Condition Estimates for Pseudo-Arclength Continuation. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=primary-selected-PDF-text
原著PDFの選択部分2.2節の接線・正規化・超平面制約と単純foldの範囲を読解。全文・全証明の監査ではありません。

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
著者教材のBratu解析族と二枝・丸めた臨界値を確認。変数は採用thetaの2倍で、別導出とDecimal80で資格。1914原著は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 解析・中央差分・方向ADによるJacobian不要Newton–Krylov

非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。

**使用手法**

- [Jacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja) (`jacobian-free-newton-krylov`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)
- [自動微分](https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja) (`automatic-differentiation`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-algorithm)

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。


**問題の図**

![解析・中央差分・方向ADによるJacobian不要Newton–Krylov：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja) (`bratu-matrix-free-jfnk`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-validation)

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja) (`bratu-matrix-free-jfnk`; 同じ問題の参照 · 解析参照)

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。
### 前提・単位・境界

同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。

**編集上の補足**

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

### 採用した計算法

解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

$$
-u''=\lambda e^u,\quad u(0)=u(1)=0
$$

$$
u_\theta=2\log\frac{\cosh(\theta/2)}{\cosh(\theta(x-1/2))},\quad\lambda(\theta)=2\theta^2/\cosh^2(\theta/2)
$$

$$
J(u)v=A_hv-\lambda e^u\odot v
$$

$$
\eta_k=\min\{0.5,\max\{0.001,0.9(\|F_k\|_2/\|F_{k-1}\|_2)^{1.5}\}\}
$$

### 比較・検証

保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。

### 確認の限界

小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "mode_gap_max": 4.884981308350689e-15,
    "qualification_AD_relative": 1.1692887409033045e-17,
    "qualification_FD_relative": 8.651069407676375e-11,
    "reasons": [
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual",
      "nonlinear residual"
    ],
    "evaluation_scope": "Actualsolverevaluations;analyticlinear-forcingvalidationcountedseparately.NoPETScorassemblednonlinearJacobianusedbyJFNK."
  },
  "checks": {
    "nonzero Jv reference": true,
    "AD Jv exact": true,
    "AD primal exact": true,
    "central FD Jv": true,
    "zero Jv branch": true,
    "0/nonlinear converged": true,
    "0/finite states": true,
    "0/discrete residual": true,
    "0/continuous branch error": true,
    "0/analytic verified forcing": true,
    "0/declared eta": true,
    "0/evaluation count ledger": true,
    "0/bounded Krylov storage": true,
    "0/accepted Armijo steps": true,
    "1/nonlinear converged": true,
    "1/finite states": true,
    "1/discrete residual": true,
    "1/continuous branch error": true,
    "1/analytic verified forcing": true,
    "1/declared eta": true,
    "1/evaluation count ledger": true,
    "1/bounded Krylov storage": true,
    "1/accepted Armijo steps": true,
    "2/nonlinear converged": true,
    "2/finite states": true,
    "2/discrete residual": true,
    "2/continuous branch error": true,
    "2/analytic verified forcing": true,
    "2/declared eta": true,
    "2/evaluation count ledger": true,
    "2/bounded Krylov storage": true,
    "2/accepted Armijo steps": true,
    "3/nonlinear converged": true,
    "3/finite states": true,
    "3/discrete residual": true,
    "3/continuous branch error": true,
    "3/analytic verified forcing": true,
    "3/declared eta": true,
    "3/evaluation count ledger": true,
    "3/bounded Krylov storage": true,
    "3/accepted Armijo steps": true,
    "4/nonlinear converged": true,
    "4/finite states": true,
    "4/discrete residual": true,
    "4/continuous branch error": true,
    "4/analytic verified forcing": true,
    "4/declared eta": true,
    "4/evaluation count ledger": true,
    "4/bounded Krylov storage": true,
    "4/accepted Armijo steps": true,
    "5/nonlinear converged": true,
    "5/finite states": true,
    "5/discrete residual": true,
    "5/continuous branch error": true,
    "5/analytic verified forcing": true,
    "5/declared eta": true,
    "5/evaluation count ledger": true,
    "5/bounded Krylov storage": true,
    "5/accepted Armijo steps": true,
    "6/nonlinear converged": true,
    "6/finite states": true,
    "6/discrete residual": true,
    "6/continuous branch error": true,
    "6/analytic verified forcing": true,
    "6/declared eta": true,
    "6/evaluation count ledger": true,
    "6/bounded Krylov storage": true,
    "6/accepted Armijo steps": true,
    "7/nonlinear converged": true,
    "7/finite states": true,
    "7/discrete residual": true,
    "7/continuous branch error": true,
    "7/analytic verified forcing": true,
    "7/declared eta": true,
    "7/evaluation count ledger": true,
    "7/bounded Krylov storage": true,
    "7/accepted Armijo steps": true,
    "8/nonlinear converged": true,
    "8/finite states": true,
    "8/discrete residual": true,
    "8/continuous branch error": true,
    "8/analytic verified forcing": true,
    "8/declared eta": true,
    "8/evaluation count ledger": true,
    "8/bounded Krylov storage": true,
    "8/accepted Armijo steps": true,
    "9/nonlinear converged": true,
    "9/finite states": true,
    "9/discrete residual": true,
    "9/continuous branch error": true,
    "9/analytic verified forcing": true,
    "9/declared eta": true,
    "9/evaluation count ledger": true,
    "9/bounded Krylov storage": true,
    "9/accepted Armijo steps": true,
    "10/nonlinear converged": true,
    "10/finite states": true,
    "10/discrete residual": true,
    "10/continuous branch error": true,
    "10/analytic verified forcing": true,
    "10/declared eta": true,
    "10/evaluation count ledger": true,
    "10/bounded Krylov storage": true,
    "10/accepted Armijo steps": true,
    "11/nonlinear converged": true,
    "11/finite states": true,
    "11/discrete residual": true,
    "11/continuous branch error": true,
    "11/analytic verified forcing": true,
    "11/declared eta": true,
    "11/evaluation count ledger": true,
    "11/bounded Krylov storage": true,
    "11/accepted Armijo steps": true,
    "12/nonlinear converged": true,
    "12/finite states": true,
    "12/discrete residual": true,
    "12/continuous branch error": true,
    "12/analytic verified forcing": true,
    "12/declared eta": true,
    "12/evaluation count ledger": true,
    "12/bounded Krylov storage": true,
    "12/accepted Armijo steps": true,
    "mode agreement N63 lower": true,
    "mode agreement N63 upper": true,
    "mode agreement N127 lower": true,
    "mode agreement N127 upper": true,
    "finest exact branches": true,
    "all mode errors refine": true,
    "constant forcing companion matches": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/index.json

![保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png)

保存したN=127のNewton残差、上枝の解と解析参照、Jv誤差、実評価回数を示す縮小図。run indexは保存CSVに対応します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/atlas-bratu-continuation-jfnk-2026-11-24-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- D.A.Knoll,D.E.Keyes (2004). Jacobian-free Newton-Krylov methods: a survey of approaches and applications. https://inf.ufes.br/~luciac/comcie/JFNK-Knoll.pdf; review_level=primary-selected-PDF-text-via-course-mirror
原著のJv・差分刻み・inexact forcing・前処理の選択部分を講義ミラー配送から読解。中央差分と固定clamp付き比率則は明示的な実装選択です。

- S. C. Eisenstat and H. F. Walker (1996). Choosing the Forcing Terms in an Inexact Newton Method. https://users.wpi.edu/~walker/Papers/forcing_terms,SISC_17,1996,16-32.pdf; review_level=primary-selected-PDF-text
著者公開の原著PDFからAlgorithm IN、Choice 2と実用的safeguardの選択部分を確認。本文全体・全証明・性能表の監査ではありません。

- Hans Petter Langtangen (2014). Finite differences for the1D Bratu problem,Problem8. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-selected-exact-solution-exercise
著者教材のBratu解析族と二枝・丸めた臨界値を確認。変数は採用thetaの2倍で、別導出とDecimal80で資格。1914原著は未読です。

- PETSc developers (2026). PETSc SNES nonlinear solvers: matrix-free,inexact Newton and arc length. https://petsc.org/release/manual/snes/; review_level=official-selected-documentation
公式3.26.1文書の関連節のみ確認。PETScを使用・実行した成功値は借用せず、二次arc制約と採用超平面を区別します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
