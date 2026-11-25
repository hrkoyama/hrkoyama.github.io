# 神経膜と反応SSAの独立検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-ode-controls/

この章に登録された手法・問題・実行例の関連資料です。 Hodgkin–Huxleyの電位固定・静止・発火と、移入–死亡SSAの厳密過渡分布を、小さな固定入力で照合します。

## 手法

- [Gillespie直接確率シミュレーション（SSA）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

  古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。
- [Gillespie直接確率シミュレーション（SSA）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=ja>)

  Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)
- [Dormand–Prince RK45](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja>)

## 方程式

- [Hodgkin–Huxley膜動態](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja>)

  電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火 6.3°C、ms/mV/µA cm⁻²。NEURON8.2.6の解析的な絶対電位規約を固定し、4電位×3刻み、静止20 ms、10–11 msの電流パルスを扱います。
- [化学マスター方程式とGillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja>)

  整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布 移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。
- [移入–死亡反応と厳密過渡法則](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#immigration-death-model-ja>)

  有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。 移入率6、粒子ごとの死亡率1、時刻0/0.5/2/4。初期0・5・名目上のPoisson(6)定常標本を2seedずつ、各2,048本で比較します。
- [移入–死亡反応と厳密過渡法則](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#immigration-death-model-ja>)

  有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-algorithm>)

  古典RK4を用い、電流の切り替わりでは全段の片側値を区間に帰属させます。ゲートの可除特異点、Decimal静止根、独立なDP5(4)/Cash–Karp参照を別に照合します。
- [Hodgkin–Huxley膜動態](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-hodgkin-huxley-ja>)

  電位とゲート変数z=m,h,nの膜モデル。元のイカ軸索モデルと、人心筋や空間ケーブルへの拡張を区別します。 全モデル族の実装ではありません。今回の固定例：Hodgkin–Huxley：電位固定・静止平衡・発火
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-algorithm>)

  Gillespie direct SSAで、次の事象時刻を観測点の間で保持します。生のPCG64から開区間一様数を作り、初期Poissonの有限格子逆CDFと全ストリームを記録します。
- [化学マスター方程式とGillespie SSA](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-chemical-master-ja>)

  整数分子数n、反応ジャンプνj、傾向関数ajの確率モデル。Gillespie SSAは軌道を標本化する解法で、反応網自体とは区別します。 全モデル族の実装ではありません。今回の固定例：移入–死亡SSA：有限時刻の厳密分布

## 問題の図

- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png
- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/hodgkin-huxley-controls.png
- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-ode-controls/results/immigration-death-ssa.png

## 厳密解・参照解

- [Hodgkin–Huxley：電位固定・静止平衡・発火：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/hodgkin-huxley-controls/?lang=ja#references-ja>)

  全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 6.3°C、NEURON8.2.6の解析的な絶対電位規約を固定し、時間ms・電位mV・電流密度μA/cm²を用います。4固定電位、3刻み、20msの静止と10–11msの電流パルスを比較。ゲートは無次元で、空間一様な1細胞膜の電位固定または区分電流の初期値問題です。 1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。
- [移入–死亡SSA：有限時刻の厳密分布：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/immigration-death-ssa/?lang=ja#references-ja>)

  Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。
- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 移入率6、粒子ごとの死亡率1、観測時刻0/0.5/2/4。初期値0・5・名目上の定常Poisson(6)を各2seed、各記録2,048軌跡で比較します。粒子数は非負整数、時間単位を固定し、N=0では死亡propensityが零になります。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja>)
  reference_kind: semi-analytic

  半解析解 6.3°C、NEURON8.2.6の解析的な絶対電位規約を固定し、時間ms・電位mV・電流密度μA/cm²を用います。4固定電位、3刻み、20msの静止と10–11msの電流パルスを比較。ゲートは無次元で、空間一様な1細胞膜の電位固定または区分電流の初期値問題です。
- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja>)
  reference_kind: analytic

  解析解 移入率6、粒子ごとの死亡率1、観測時刻0/0.5/2/4。初期値0・5・名目上の定常Poisson(6)を各2seed、各記録2,048軌跡で比較します。粒子数は非負整数、時間単位を固定し、N=0では死亡propensityが零になります。
- [Hodgkin–Huxley：電位固定・静止平衡・発火：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja#hodgkin-huxley-controls-ja-validation>)

  全採用時刻のゲート誤差、電位・ゲート範囲、採用端点の新しい微分を使うHermite発火時刻を保存。元の1e-8ゲート目標も未達を含めて表示します。
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-hodgkin-huxley-controls-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 6.3°C、NEURON8.2.6の解析的な絶対電位規約を固定し、時間ms・電位mV・電流密度μA/cm²を用います。4固定電位、3刻み、20msの静止と10–11msの電流パルスを比較。ゲートは無次元で、空間一様な1細胞膜の電位固定または区分電流の初期値問題です。 1細胞膜の教育例です。元論文の電位規約、TABLE/cnexp実装、ケーブル伝播や生体実測の再現とは呼びません。区間内に括れない発火は捏造せず、静止根の一意性・区間Hurwitz安定性は主張しません。
- [移入–死亡SSA：有限時刻の厳密分布：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja#immigration-death-ssa-ja-validation>)

  Binomial＋Poissonの厳密過渡法則を、80/120桁の有向区間・尾部上界で照合。20個のDKW目標と20個の厳密和平均目標を名目union bound0.01にまとめ、分散の5SE目標は別に残します。
- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-immigration-death-ssa-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 移入率6、粒子ごとの死亡率1、観測時刻0/0.5/2/4。初期値0・5・名目上の定常Poisson(6)を各2seed、各記録2,048軌跡で比較します。粒子数は非負整数、時間単位を固定し、N=0では死亡propensityが零になります。 有限時間の決定論的初期状態を定常分布とは呼びません。区間の保証は理想IID法則の参照に限り、PRNG・対数演算を含むソフトウェア全体の被覆率保証や単一軌跡の代表性を主張しません。

## コード・検証

- [移入–死亡SSA：有限時刻の厳密分布](<https://hrkoyama.github.io/numerical-methods-atlas/validation/immigration-death-ssa/?lang=ja>)
  availability: run

  1本の軌跡と12,288本の固定アンサンブルを分けて検証します。
- [Hodgkin–Huxley：電位固定・静止平衡・発火](<https://hrkoyama.github.io/numerical-methods-atlas/validation/hodgkin-huxley-controls/?lang=ja>)
  availability: run

  固定電位の解析ゲート解と、区分電流下の4状態系を照合します。
- [Gillespie直接確率シミュレーション（SSA）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gillespie-ssa/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
