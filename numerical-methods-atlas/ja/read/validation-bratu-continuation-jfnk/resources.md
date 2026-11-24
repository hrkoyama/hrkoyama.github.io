# Bratuのfold継続とJacobian不要Newton–Krylov

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-bratu-continuation-jfnk/

この章に登録された手法・問題・実行例の関連資料です。 同じ1次元Bratu境界値問題で、foldを越える継続とJacobianを組み立てない反復を独立解析族へ照合します。

## 手法

- [重み付き擬似弧長継続](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja>)
- [Jacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja>)
- [重み付き擬似弧長継続](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja>)

  hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。
- [Jacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

## 方程式

- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 無次元x∈[0,1]、両端u=0、中心差分の内点31/63/127。零解から固定ds=0.1で80step。λ=2で上下枝を補正し、λ=4は離散無解の意図的な対照です。擬似弧長は物理時間ではありません。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 同じ無次元1次元Dirichlet問題でλ=3、内点63/127、初期値0または4sin(πx)。3Jv×2格子×2枝の12解法と固定η=1e-8の解析Jv対照1本。GMRES restart24/max96、Newton最大24、残差許容1e-9です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-algorithm>)

  hΣdu²+dλ²の重み付き単位接線、予測点と接線超平面によるNewton補正。別の拡大系でfoldと正規化null vectorを解きます。このcaseは疎Jacobianを明示的に組み立てます。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-algorithm>)

  解析Jv、残差2評価の中央差分、または方向1本のforward ADを使います。PoissonのThomas右前処理、2回の再直交化とGivensによるGMRES。η0=.3、その後η=clamp(.9(Fk/Fk−1)^1.5,.001,.5)。これはEW Choice 2型の明示的な変形で、原著のsafeguard全体やPETSc既定値ではありません。

## 問題の図

- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation-preview.png
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk-preview.png
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-fold-continuation.png
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/bratu-continuation-jfnk/results/bratu-matrix-free-jfnk.png

## 厳密解・参照解

- [擬似弧長継続でBratuのfoldを越える：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-continuation/?lang=ja#references-ja>)

  保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。 小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-matrix-free-jfnk/?lang=ja#references-ja>)

  保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。 小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja>)
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja>)
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。
- [擬似弧長継続でBratuのfoldを越える：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja#bratu-fold-continuation-ja-validation>)

  保存R3では共通27pytestと本caseの67固定判定が合格。離散残差、接線の向き・単位長、fold方程式・null条件・transversality、独立Decimal80解析族、固定3格子の誤差を別々に確認しています。
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-continuation-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。 小さな1次元の単純foldだけです。分岐曲線の解析族比較では計算した中点値を族の座標に使い、固定λの独立形状比較と区別します。連続foldは離散解そのものではなく、一般の分岐追跡や大規模性能は保証しません。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja#bratu-matrix-free-jfnk-ja-validation>)

  保存R3では共通27pytestと本caseの129固定判定が合格。非零Jvの解析検算、離散残差、独立解析上下枝、3modeの一致、forcing、評価回数、Krylov記憶幅、Armijoと固定η対照を確認。解析forcing検算は別計数で、FD/ADの反復制御には使いません。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-matrix-free-jfnk-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 同じ無次元1次元Bratu、x∈[0,1]、両端u=0。連続解析族は独立Decimal80評価であり、離散解やNewton/GMRES反復の厳密解ではありません。 小1次元BVP向けの教育実装です。ADは四則・exp・境界paddingの方向微分に限ります。小Hessenberg行列と基底は保持します。ηの固定下限があるため、原著EWの漸近収束定理、一般AD/PETScとの同等性、速度向上や大域収束は主張しません。

## コード・検証

- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja>)
  availability: run

  同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja>)
  availability: run

  非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。
- [重み付き擬似弧長継続：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudo-arclength-continuation/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Jacobian不要Newton–Krylov：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobian-free-newton-krylov/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
