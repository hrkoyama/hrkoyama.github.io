# サーモスタット：温度制御と分布の比較

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/thermostats/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [単純な速度スケーリング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=ja>)
- [Berendsen弱結合サーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=ja>)
- [Andersenサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/andersen-thermostat/?lang=ja>)
- [Langevinサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja>)
- [Noséの拡張系](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-thermostat/?lang=ja>)
- [Nosé–Hooverサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja>)
- [Nosé–Hoover chain](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja>)
- [確率的速度リスケーリング（CSVR）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja>)
- [Gaussian isokineticサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gaussian-isokinetic/?lang=ja>)
- [一般化Langevin・GLE](<https://hrkoyama.github.io/numerical-methods-atlas/methods/generalized-langevin/?lang=ja>)
- [DPDサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dpd-thermostat/?lang=ja>)
- [Lowe–Andersenサーモスタット](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lowe-andersen/?lang=ja>)

## 方程式

章固有の対応は未登録です。全体一覧：[方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja)

## 問題の図

章固有の対応は未登録です。全体一覧：[テスト問題の名前と図](https://hrkoyama.github.io/numerical-methods-atlas/gallery/?lang=ja)

## 厳密解・参照解

章固有の対応は未登録です。全体一覧：[厳密解・参照解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja)

## コード・検証

- [NH・chain・弱結合・速度固定の比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja>)
  availability: run

  同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。
- [Langevin温度制御：正準分布・刻み偏り・時間相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/langevin-harmonic/?lang=ja>)
  availability: run

  調和振動子のBAOABを、正準分布と離散Lyapunov定常分布、連続・離散の時間相関へ照合します。
- [CSVRとLangevin：調和2自由度の分布・揺らぎ・相関](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-harmonic/?lang=ja>)
  availability: run

  異なる周波数を持つ2自由度でglobal CSVRとlocal Langevinを同じOBABO分割で比較。位置・運動量・温度・全エネルギーの分布、揺らぎ、相関を記録します。
- [非調和CSVRとLangevin：Boltzmann求積との分布比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/csvr-langevin-quartic/?lang=ja>)
  availability: run

  弱い四次ポテンシャルを持つ2自由度で、CSVRとLangevinの分布・温度とエネルギーの揺らぎ・相関を比較。正準分布を独立なBoltzmann求積から得ます。
- [2準位模型のBO/CP型連成と短い核熱浴](<https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja>)
  availability: run

  電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。
- [拘束・重心除去と正準統計](<https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja>)
  availability: run

  有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。
- [単純な速度スケーリング：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Berendsen弱結合サーモスタット：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Langevinサーモスタット：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Nosé–Hooverサーモスタット：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Nosé–Hoover chain：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [確率的速度リスケーリング（CSVR）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
