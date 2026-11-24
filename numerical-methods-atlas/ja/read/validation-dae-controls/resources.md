# DAEの初期化・保存則・拘束ドリフト

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-dae-controls/

この章に登録された手法・問題・実行例の関連資料です。 整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。

## 手法

- [微分代数方程式（DAE）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja>)

  連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。
- [微分代数方程式（DAE）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja>)

  指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
- [SHAKE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja>)

  指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
- [RATTLE拘束積分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja>)

  指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。 独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。
- [微分代数方程式（DAE）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dae/?lang=ja>)
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

## 方程式

- [半陽的index-1 DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja>)

  整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。 無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。
- [拘束付き平面振り子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja>)

  元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-algorithm>)

  連立Newtonと同じ尺度のArmijo線探索を用い、特異な初期推測は修復せず記録します。
- [半陽的index-1 DAE](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#index-one-dae-ja>)

  整合初期化と微分・代数残差を扱う小規模な固定例です。一般DAEソルバーの完成を意味しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-algorithm>)

  解析Jacobian付き固定BE/Newtonを使い、質量の投影・濃度クリップはしません。
- [Robertson反応系](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#robertson-kinetics-ja>)

  3成分の硬い反応ODEと、保存則を代数式に置き換えたindex-1 DAEを区別して比較します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-algorithm>)

  指数低減ODEと臨界拘束誤差拡張を固定RK4で積分し、拘束仕事も同じ段で積分します。
- [拘束付き平面振り子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja>)

  元の位置拘束DAE、微分した拘束に基づくODE、SHAKE/RATTLEの離散写像を区別します。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。

## 問題の図

- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization-preview.png
- [拘束付き振り子](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum-preview.png
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/index1-dae-consistent-initialization.png
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/robertson-conservation-dae.png
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24/dae-controls/results/high-index-pendulum.png
- [Robertson反応系：ODEと保存則DAE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja>)

  整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/ode-adaptivity/results/robertson-stiff-kinetics-preview.png

## 厳密解・参照解

- [index-1 DAEの整合初期化と離散残差：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/index1-dae-consistent-initialization/?lang=ja#references-ja>)

  独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。 単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。
- [拘束付き振り子：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#references-ja>)

  Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。 独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。 原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja>)
  reference_kind: manufactured

  製造解 無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja>)
  reference_kind: semi-analytic

  半解析解 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。
- [index-1 DAEの整合初期化と離散残差：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja#index1-dae-consistent-initialization-ja-validation>)

  独立Decimal製造解・3つの離散根と3固定格子を比較し、一次誤差と代数拘束を確認します。
- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-index1-dae-consistent-initialization-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 無次元・正枝。微分行と代数行の尺度はそれぞれ1で、最大ノルムを用います。 単一の製造正枝・固定BE計算です。IDA実行や一般DAEソルバーの検証ではありません。
- [Robertson保存制約DAEと公式IDA保存値：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja#robertson-conservation-dae-ja-validation>)

  元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。
- [振り子の指数低減・拘束ドリフト・明示安定化：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja#high-index-pendulum-ja-validation>)

  Jacobi解析族と独立角度ODE2計算を資格確認し、場・拘束の厳密法則・エネルギー仕事収支を比較します。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 m=L=g=1、初期角0.7、初期角速度0。非整合制御では半径方向速度を明示的に加えます。 投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。 原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
- [Robertson反応系：ODEと保存則DAE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/robertson-stiff-kinetics/?lang=ja#references-ja>)

  整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。 22共通時刻の実誤差、全受理時刻の質量/最小値、真の段階残差、実RHS/Jacobian/因子/solve数を別判定します。 元39目標をすべて実測し、精度・細分化4目標の未達を変更せず研究結果として記録します。他35条件と独立参照・保存配列からの判定再計算は必須です。
- [Robertson反応系の初期剛性と実誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-stiff-kinetics-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。 有限格子の数値参照 無次元3成分、初期値(1,0,0)、T=.4。固定512/1024/2048刻みと2許容誤差の適応法で計8run。 保存/正値性は固定入力の観測で、一般的な保証ではありません。T=.4の短時間・標本時刻での精度であり、長時間化学精度や全時刻誤差上限は主張しません。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-robertson-conservation-dae-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  整合初期化、index-1保存則DAE、index-3振り子の微分拘束に基づくODEを比較します。保存された公式IDA出力との比較と、新たに実行した独立ODE参照を区別します。 有限格子の数値参照 モデル時間0から4。中間種と残差の尺度は1e-4。公式印字値の丸め幅と数値誤差を区別します。 公式SUNDIALS v7.1.1の2印字行のみ。IDAの新規実行0、長時間の化学精度や一般DAE性能は扱いません。 この固定時間格子の漸近収束や元精度目標の全合格は主張しません。

## コード・検証

- [index-1 DAEの整合初期化と離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/index1-dae-consistent-initialization/?lang=ja>)
  availability: run

  既知の正枝を持つindex-1 DAEで初期化と後退Eulerの誤差・残差を分離します。
- [振り子の指数低減・拘束ドリフト・明示安定化](<https://hrkoyama.github.io/numerical-methods-atlas/validation/high-index-pendulum/?lang=ja>)
  availability: run

  位置拘束の指数3系から明示ODEを導き、整合・非整合初期値の拘束ドリフトと安定化を比較します。
- [SHAKEとRATTLE：拘束と運動量の違い](<https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja>)
  availability: run

  単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。
- [Robertson保存制約DAEと公式IDA保存値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/robertson-conservation-dae/?lang=ja>)
  availability: run

  Robertsonの保存制約DAEと全ODEを同じ固定時間格子で比較し、公式IDA保存値を別に照合します。 初回は元の時間精度・細分化目標4件が未達でした。
