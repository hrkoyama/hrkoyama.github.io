# 時間離散・fold近傍・分布係数の随伴

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-adjoint/

この章に登録された手法・問題・実行例の関連資料です。 離散写像の接線と随伴を比較し、参照精度・要求残差・保存bufferと再計算を分けます。

## 手法

- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)

  ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。
- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)

  解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)

  解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)

  Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)

  Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

## 方程式

- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-algorithm>)

  ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-algorithm>)

  解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-algorithm>)

  Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

## 問題の図

- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png
- [離散fold近傍のBratu感度](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png
- [分布係数Bratuの行列非形成VJP](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png
- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png
- [離散fold近傍のBratu感度](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png
- [分布係数Bratuの行列非形成VJP](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png

## 厳密解・参照解

- [時間離散拡散の随伴とcheckpoint：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#references-ja>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。
- [後退Euler離散モードと時間厳密半離散拡散の参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元x∈[0,1]、同次Dirichlet、κ=.1、θ=.2、T=.1。内点7/15、時間step64/128/256。目的関数はh重み付き終端誤差と指定二次正則化です。 固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。
- [離散fold近傍のBratu感度：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#references-ja>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。
- [離散fold近傍のBratu shooting・接線・随伴参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet Bratu、内点31/63。検証する離散fold anchorの下.1/.01/.001に固定し、下枝状態を用います。λ文字列は一度binary64へ変換し、その正確な値を高精度参照へ渡します。 連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
- [分布係数Bratuの行列非形成VJP：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#references-ja>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。
- [分布Bratu係数の独立dense感度と行列不要VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet、63内点。a(x)=2+Bθは8/16/32個の線形hat制御で、主固定例は1.7≤a≤2.3。端点係数は零Dirichlet状態と異なり固定零にしません。 同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
- [後退Euler離散モードと時間厳密半離散拡散の参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja>)
  reference_kind: analytic

  解析解 無次元x∈[0,1]、同次Dirichlet、κ=.1、θ=.2、T=.1。内点7/15、時間step64/128/256。目的関数はh重み付き終端誤差と指定二次正則化です。
- [離散fold近傍のBratu shooting・接線・随伴参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet Bratu、内点31/63。検証する離散fold anchorの下.1/.01/.001に固定し、下枝状態を用います。λ文字列は一度binary64へ変換し、その正確な値を高精度参照へ渡します。
- [分布Bratu係数の独立dense感度と行列不要VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet、63内点。a(x)=2+Bθは8/16/32個の線形hat制御で、主固定例は1.7≤a≤2.3。端点係数は零Dirichlet状態と異なり固定零にしません。
- [時間離散拡散の随伴とcheckpoint：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-validation>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。
- [後退Euler離散モードと時間厳密半離散拡散の参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 無次元x∈[0,1]、同次Dirichlet、κ=.1、θ=.2、T=.1。内点7/15、時間step64/128/256。目的関数はh重み付き終端誤差と指定二次正則化です。 固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。
- [離散fold近傍のBratu感度：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-validation>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。
- [離散fold近傍のBratu shooting・接線・随伴参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet Bratu、内点31/63。検証する離散fold anchorの下.1/.01/.001に固定し、下枝状態を用います。λ文字列は一度binary64へ変換し、その正確な値を高精度参照へ渡します。 連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
- [分布係数Bratuの行列非形成VJP：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-validation>)

  実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。
- [分布Bratu係数の独立dense感度と行列不要VJP](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 1D同次Dirichlet、63内点。a(x)=2+Bθは8/16/32個の線形hat制御で、主固定例は1.7≤a≤2.3。端点係数は零Dirichlet状態と異なり固定零にしません。 同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

## コード・検証

- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja>)
  availability: run

  後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。
- [離散fold近傍のBratu感度](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja>)
  availability: run

  離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。
- [分布係数Bratuの行列非形成VJP](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja>)
  availability: run

  2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。
