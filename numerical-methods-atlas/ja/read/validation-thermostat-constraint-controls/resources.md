# 決定論的温度制御と拘束自由度

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-thermostat-constraint-controls/

この章に登録された手法・問題・実行例の関連資料です。 小さな調和・四次系で温度制御の違いを比較し、固定線形拘束の有効自由度・運動量共分散・過渡分布を検証します。未達の統計目標も表示します。

## 手法

- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)

  質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。
- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)

  質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。
- [Nosé–Hooverサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja>)
- [Nosé–Hoover chain](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja>)
- [Berendsen弱結合サーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=ja>)
- [単純な速度スケーリング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=ja>)
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)
- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)

## 方程式

- [固定線形拘束の正準運動量](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#projected-canonical-model-ja>)

  固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。 質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。
- [2モードの決定論的温度浴](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-mode-thermostat-model-ja>)

  著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。
- [固定線形拘束の正準運動量](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#projected-canonical-model-ja>)

  固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-algorithm>)

  明示した凍結変数の厳密bath部分流を対称合成し、各半bathを2副周期で計算します。etaはE部分流だけで進め、独立な全拡張ODEの短時間参照と照合します。
- [Hamilton系・振動子](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja>)

  正準方程式と分離可能なHamiltonianの代表形。調和・4次ポテンシャルの振動子で、エネルギー誤差とシンプレクティック性を比べます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-algorithm>)

  質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

## 問題の図

- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png
- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png
- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png
- [非調和CSVRとLangevin：Boltzmann求積との分布比較](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja>)

  小さな調和・四次系で温度制御の違いを比較し、固定線形拘束の有効自由度・運動量共分散・過渡分布を検証します。未達の統計目標も表示します。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/thermostats/results/csvr-langevin-quartic.png

## 厳密解・参照解

- [拘束・重心除去と正準統計：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#references-ja>)

  Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。
- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 共通の調和ポテンシャル中の1次元3粒子で質量1/2/3、kBT=1。無拘束・COM・COM相対・冗長行の等価拘束で有効自由度3/2/1/1、各1,024標本を比較します。固定線形拘束Cq=0、CM⁻¹p=0を用い、冗長行は同じ接空間上で比較します。 固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。
- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja>)
  reference_kind: semi-analytic

  半解析解 質量1、kBT=1、振動数1/1.7、四次係数0/0.2。NH1・NHC3・Berendsen・固定速さの熱浴を、2結合・2刻み、正準256/加熱128標本で比較します。無次元でQ1=2τ²、Qj=τ²。空間境界のない2モード初期値問題で、正準・加熱アンサンブルを固定します。
- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja>)
  reference_kind: semi-analytic

  半解析解 共通の調和ポテンシャル中の1次元3粒子で質量1/2/3、kBT=1。無拘束・COM・COM相対・冗長行の等価拘束で有効自由度3/2/1/1、各1,024標本を比較します。固定線形拘束Cq=0、CM⁻¹p=0を用い、冗長行は同じ接空間上で比較します。
- [NH・chain・弱結合・速度固定の比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-validation>)

  物理的時間反転、Hextの微分、phi1、弱結合の局所逆と非可逆な速度固定を別に検査。時刻20の4分布・揺らぎ・符号付き相関とDKWの未確定範囲を残します。
- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 質量1、kBT=1、振動数1/1.7、四次係数0/0.2。NH1・NHC3・Berendsen・固定速さの熱浴を、2結合・2刻み、正準256/加熱128標本で比較します。無次元でQ1=2τ²、Qj=τ²。空間境界のない2モード初期値問題で、正準・加熱アンサンブルを固定します。 同じ2モード四次系と調和対照。決定論的浴の短時間・有限標本比較。
- [拘束・重心除去と正準統計：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-validation>)

  Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。
- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 共通の調和ポテンシャル中の1次元3粒子で質量1/2/3、kBT=1。無拘束・COM・COM相対・冗長行の等価拘束で有効自由度3/2/1/1、各1,024標本を比較します。固定線形拘束Cq=0、CM⁻¹p=0を用い、冗長行は同じ接空間上で比較します。 固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。
- [非調和CSVRとLangevin：Boltzmann求積との分布比較：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#references-ja>)

  小さな調和・四次系で温度制御の違いを比較し、固定線形拘束の有効自由度・運動量共分散・過渡分布を検証します。未達の統計目標も表示します。 非調和ポテンシャルのBoltzmann分布を独立数値求積し、CSVR・Langevinの有限刻み分布とモーメントを比較します。厳密な確率軌道の比較ではありません。
- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  小さな調和・四次系で温度制御の違いを比較し、固定線形拘束の有効自由度・運動量共分散・過渡分布を検証します。未達の統計目標も表示します。 半解析解 質量1、kBT=1、振動数1/1.7、四次係数0/0.2。NH1・NHC3・Berendsen・固定速さの熱浴を、2結合・2刻み、正準256/加熱128標本で比較します。無次元でQ1=2τ²、Qj=τ²。空間境界のない2モード初期値問題で、正準・加熱アンサンブルを固定します。 同じ2モード四次系と調和対照。決定論的浴の短時間・有限標本比較。

## コード・検証

- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja>)
  availability: run

  有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。
- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja>)
  availability: run

  同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。
