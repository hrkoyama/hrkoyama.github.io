# 硬いODE・RK45・境界分割

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-ode-adaptivity/

この章に登録された手法・問題・実行例の関連資料です。 Robertsonとvan der Pol、RK45の補間・イベント、非同次境界の分割法を小さな固定入力で検証します。独立参照、局所推定と実誤差、時間誤差と空間誤差を区別します。

## 手法

- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [微分代数方程式（DAE）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。 解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)

  BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)

  BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)

  BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

  実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)

  w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。
- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)

  w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。
- [BDF2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bdf2/?lang=ja>)
- [L安定なSDIRK2](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sdirk2/?lang=ja>)
- [適応SDIRK2／ステップ倍分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/step-doubling/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)
- [Strang分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja>)
- [Lie–Trotter分割](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

## 方程式

- [Robertson反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja>)

  3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。
- [半陽的index-1 DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja>)

  整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。
- [van der Pol振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja>)

  固定したμと短い時区間で硬さによる仕事量と誤差を比較します。完全な緩和振動周期の検証ではありません。 x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。
- [有限次元の線形発展系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja>)

  減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。 γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。
- [非同次境界を持つ線形反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja>)

  同じ非周期有限差分系に対する時間誤差と、連続厳密解に対する空間誤差を分けます。 u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-algorithm>)

  BDF2は同格子BE開始。SDIRK2の非線形段階は重み付き最大残差で判定し、同じ段階内だけJacobian因子を再利用。適応法はRMS倍分割誤差と2半刻みを採用。
- [Robertson反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja>)

  3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-algorithm>)

  BDF2/SDIRK2と倍分割適応法。解析Jacobian・段階内だけの因子再利用・失敗時の候補保存を実装します。
- [van der Pol振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#van-der-pol-ja>)

  固定したμと短い時区間で硬さによる仕事量と誤差を比較します。完全な緩和振動周期の検証ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-algorithm>)

  実Dormand–Prince5(4)・quartic連続拡張・受理状態が所有するFSAL・保存補間上の符号区間二分法。拒否端点を昇格しません。
- [有限次元の線形発展系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-evolution-system-ja>)

  減衰回転の物理時刻と、定常残差を減衰させる擬似時間を例ごとに区別します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-algorithm>)

  w=u−1で未補正(Lw,w+1)、補正(Lw+1,w)に分割。実DirichletDST-I指数流を合成し、反応の境界不整合を保持します。
- [非同次境界を持つ線形反応拡散](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#inhomogeneous-reaction-diffusion-ja>)

  同じ非周期有限差分系に対する時間誤差と、連続厳密解に対する空間誤差を分けます。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

## 問題の図

- [Robertson反応系：ODEと保存則DAE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition-preview.png
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events-preview.png
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction-preview.png
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics.png
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/van-der-pol-stiff-transition.png
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/rk45-dense-events.png
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/strang-boundary-order-reduction.png

## 厳密解・参照解

- [Robertson反応系：ODEと保存則DAE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja>)

  22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。 元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
- [van der Polの短時間剛性遷移：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/van-der-pol-stiff-transition/?lang=ja#references-ja>)

  資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。
- [RK45の埋込み推定・補間・イベント：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/rk45-dense-events/?lang=ja#references-ja>)

  解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。 接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。
- [Dirichlet境界でのStrang次数低下と補正：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/strang-boundary-order-reduction/?lang=ja#references-ja>)

  独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。 原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja>)
  reference_kind: analytic

  解析解 γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja>)
  reference_kind: semi-analytic

  半解析解 u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。
- [Robertson反応系の初期剛性と実誤差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja#robertson-stiff-kinetics-ja-validation>)

  22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
- [van der Polの短時間剛性遷移：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja#van-der-pol-stiff-transition-ja-validation>)

  資格済みRadau/BDFと21時刻で比較。元の全判定を偽値も含め保存し、他208条件と、結果の忠実な表示・実局所制御・元失敗保存の3検証を別に要求します。
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-van-der-pol-stiff-transition-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 x′=v,v′=μ(1−x²)v−x、初期値(2,0)、T=2。2方式×3刻み×2μと適応4runで計16run。 測定後の報告範囲変更で、数値的な修復ではありません。初回誤差4.535633779e-5は元目標2e-5を超えます。局所rtolは大域誤差を保証せず、報告検証の合格は全元目標の達成ではありません。大μ全周期は対象外です。
- [RK45の埋込み推定・補間・イベント：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja#rk45-dense-events-ja-validation>)

  解析状態とπ/6,π/2の単純交差を参照に、端点/97オフメッシュ点/イベント時刻・残差と実nfev=1+6試行数を判定。
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-rk45-dense-events-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 γ=.2,ω=3、初期値(1,0)、T=2。3対のrtol/atol×2最大刻みと終端交差2runで計8run。 接触根・1刻み内の多重交差・reset付き系の一般性は保証しません。初期零/所有権/resetは限定成分対照で、局所許容誤差と大域精度を同一視しません。
- [Dirichlet境界でのStrang次数低下と補正：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja#strang-boundary-order-reduction-ja-validation>)

  独立疎affine指数作用と別記述の正弦和を先に資格。同FD時間誤差・解析連続解との差・固定格子/刻み領域の観測次数を判定。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-strang-boundary-order-reduction-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 u_t=u_xx+u、[0,1]、両端u=1、解析定常解+.1正弦摂動、T=.1。内部31/63/127点・8/16/32/64刻みとLie対照4run、計28run。 原著の線形特殊例で非線形数値表の再現ではありません。非自律/一般境界や普遍的な次数低下は主張せず、Lie終端の反応trace不整合も別表示します。

## コード・検証

- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-stiff-kinetics/?lang=ja>)
  availability: run

  短い固定区間でBDF2・SDIRK2・倍分割適応法を、資格済みRadau/BDF参照と比較します。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja>)
  availability: run

  Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。
- [van der Polの短時間剛性遷移](<https://hrkoyama.github.io/numerical-methods-atlas/validation/van-der-pol-stiff-transition/?lang=ja>)
  availability: run

  局所制御と大域誤差を分離します。初回は元209目標中208達成で、μ=1の厳しい適応設定は大域目標2e-5に未達でした。
- [RK45の埋込み推定・補間・イベント](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rk45-dense-events/?lang=ja>)
  availability: run

  減衰回転の解析解を使い、受理/棄却・FSAL・区間内補間・向き付き交差時刻を分けて検査します。
- [Dirichlet境界でのStrang次数低下と補正](<https://hrkoyama.github.io/numerical-methods-atlas/validation/strang-boundary-order-reduction/?lang=ja>)
  availability: run

  実1D非周期場で、未補正/境界補正Strangを同じFD参照へ比較し、時間誤差と空間誤差を分けます。
