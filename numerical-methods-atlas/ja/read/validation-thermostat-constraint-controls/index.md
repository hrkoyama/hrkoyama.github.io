# 決定論的温度制御と拘束自由度

小さな調和・四次系で温度制御の違いを比較し、固定線形拘束の有効自由度・運動量共分散・過渡分布を検証します。未達の統計目標も表示します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## NH・chain・弱結合・速度固定の比較

同じ2モード系で、温度平均に加えて分布・揺らぎ・相関を比べます。

**使用手法**

- [Nosé–Hooverサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=ja) (`nose-hoover`)
- [Nosé–Hoover chain](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=ja) (`nose-hoover-chains`)
- [Berendsen弱結合サーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=ja) (`berendsen-thermostat`)
- [単純な速度スケーリング](https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=ja) (`velocity-rescaling`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-algorithm)

明示した凍結変数の厳密bath部分流を対称合成し、各半bathを2副周期で計算します。etaはE部分流だけで進め、独立な全拡張ODEの短時間参照と照合します。

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

単位質量,kBT=1、周波数1/1.7、quartic係数0/0.2。NH1/NHC3/Berendsen/速度固定、2結合・2刻み、正準256＋加熱128レプリカを固定します。

- [2モードの決定論的温度浴](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-mode-thermostat-model-ja) (`finite-mode-thermostat-model`)

単位質量,kBT=1、周波数1/1.7、quartic係数0/0.2。NH1/NHC3/Berendsen/速度固定、2結合・2刻み、正準256＋加熱128レプリカを固定します。


**問題の図**

![NH・chain・弱結合・速度固定の比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非調和CSVRとLangevin：Boltzmann求積との分布比較](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja) (`thermostatted-quartic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=ja#deterministic-thermostat-contrasts-ja-validation)

物理的時間反転、Hextの微分、phi1、弱結合の局所逆と非可逆な速度固定を別に検査。時刻20の4分布・揺らぎ・符号付き相関とDKWの未確定範囲を残します。

- [NH・chain・弱結合・速度固定の比較](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-deterministic-thermostat-contrasts-ja) (`deterministic-thermostat-contrasts`; 同じ問題の参照 · 半解析参照)

同じ2モード四次系と調和対照。決定論的浴の短時間・有限標本比較。
### 前提・単位・境界

単位質量,kBT=1、周波数1/1.7、quartic係数0/0.2。NH1/NHC3/Berendsen/速度固定、2結合・2刻み、正準256＋加熱128レプリカを固定します。

**編集上の補足**

著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。 調査目標には、異なる熱浴の正準モーメント・相関と、固定した正準/加熱アンサンブルの有限時刻での比較が含まれます。未達は熱浴・初期集団ごとの結果を残したもので、必須の実装・再現検査とは別に読みます。

### 採用した計算法

明示した凍結変数の厳密bath部分流を対称合成し、各半bathを2副周期で計算します。etaはE部分流だけで進め、独立な全拡張ODEの短時間参照と照合します。

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

### 比較・検証

物理的時間反転、Hextの微分、phi1、弱結合の局所逆と非可逆な速度固定を別に検査。時刻20の4分布・揺らぎ・符号付き相関とDKWの未確定範囲を残します。

### 確認の限界

著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。

### 調査した目標：達成91・未達117・未確定0（全208）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 91,
    "unmet": 117,
    "unresolved": 0,
    "total": 208
  },
  "goals": [
    {
      "name": "NH/short-accuracy/NH/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.5848659173536042e-07,
        "target": 2e-05
      }
    },
    {
      "name": "NH/short-order/NH/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.0000002696401498,
        "target": 1.7
      }
    },
    {
      "name": "NH/Hext/NH/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.74237467788837e-08,
        "target": 2e-05,
        "scope": "Predeclaredstudygoal,notrigorousflowbound"
      }
    },
    {
      "name": "NH/Hext-order/NH/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.999999697088544,
        "target": 1.7
      }
    },
    {
      "name": "NH/short-accuracy/NHC3/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.7014320588438852e-07,
        "target": 2e-05
      }
    },
    {
      "name": "NH/short-order/NHC3/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9999999439963565,
        "target": 1.7
      }
    },
    {
      "name": "NH/Hext/NHC3/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.273884871440915e-08,
        "target": 2e-05,
        "scope": "Predeclaredstudygoal,notrigorousflowbound"
      }
    },
    {
      "name": "NH/Hext-order/NHC3/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.99999954935859,
        "target": 1.7
      }
    },
    {
      "name": "NH/short-accuracy/NH/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.6016483388561827e-07,
        "target": 2e-05
      }
    },
    {
      "name": "NH/short-order/NH/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.0000002894019273,
        "target": 1.7
      }
    },
    {
      "name": "NH/Hext/NH/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.603876929816805e-08,
        "target": 2e-05,
        "scope": "Predeclaredstudygoal,notrigorousflowbound"
      }
    },
    {
      "name": "NH/Hext-order/NH/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9999996336228278,
        "target": 1.7
      }
    },
    {
      "name": "NH/short-accuracy/NHC3/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.719704998654336e-07,
        "target": 2e-05
      }
    },
    {
      "name": "NH/short-order/NHC3/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9999999864219544,
        "target": 1.7
      }
    },
    {
      "name": "NH/Hext/NHC3/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.162292742516266e-08,
        "target": 2e-05,
        "scope": "Predeclaredstudygoal,notrigorousflowbound"
      }
    },
    {
      "name": "NH/Hext-order/NHC3/0.2",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9999994926009597,
        "target": 1.7
      }
    },
    {
      "name": "NH/CDF/0.0/NH/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.037328055556311024,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.03486398684574196,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.30398764879622453,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.04044638234288861,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.026637281607520547,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.22964265488338453,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05444334970984788,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.03695958538816721,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.15799669961398322,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06249999999998901,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.057459905054390595,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.18105229800118616,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06640624999998901,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.11068722077730915,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.062091457705365505,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06009474606853438,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.13897307728127148,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.18301226348095767,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06640624999998901,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.11003077569742967,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07468942818825863,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NH/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06009474606853438,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NH/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1409948390802954,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NH/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.18165625477400915,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.049719340287366576,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06289684847404169,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.105316960783008,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.08593749999998901,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2573503227438096,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.20515080737770774,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.03540040029015212,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.04390270719771237,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.18924157081826976,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07055665029015212,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.11734648106374199,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.4896039036594748,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06746815971263342,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.04725976695909728,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.36374914504749767,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05607138234288861,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07652781015232571,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.16325205797201642,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07446290029015212,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0763966647966805,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.43706617063137054,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/NHC3/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05468750000001105,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/NHC3/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0893583787488137,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/NHC3/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2583285746820181,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3856568402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.04604737643210647,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8870863515317192,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3778443402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.12181564034817975,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8872338880995525,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3817505902873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.047247599054646615,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8809425672964785,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3778443402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.13927847589865558,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8835963267073677,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3049316502901521,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0484600872046271,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9687775714089403,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.4143066502901521,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.059532323355458695,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9724826718739034,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3010254002901521,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.046271292290813205,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9713837969974201,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/Berendsen/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3830566502901521,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/Berendsen/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05781974864183156,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/Berendsen/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9726050181310519,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.14517705360713543,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.135633888408617,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2501231860393838,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.18831515546963243,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.14517705360713543,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.135633888408617,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2501231860393838,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.0/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.0/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.18831515546963243,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.0/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06534434028736658,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06284212778751597,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.11102546209550827,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07812500000001127,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.12360137131850502,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.09170819813518122,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.04687500000001127,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05721004933365359,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.15005473407900216,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0756022167633873,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.11840346270348634,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8769604823369499,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.046183058828557666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.035121849580839415,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3318442738392695,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.14186546115985355,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.13693043058618415,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3184680271130289,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.042276808828557666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.033849951652796584,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3064253817265943,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NH/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.14186546115985355,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NH/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.13526802617722264,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NH/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.31833197329225116,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.08984375000001199,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1565814905108421,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.09620902195193537,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.08096934028736658,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.13730437940946333,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.1526691502918307,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023915168950881152,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02922607618927936,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/0.25/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.1652834824088769,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.09499046115985355,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.12277896692110372,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.4577441059352447,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.046183058828557666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.039020070489949155,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.08073306245753575,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05468750000001199,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05917037395513923,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.27415201326715566,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.042276808828557666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.03459278194212745,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.10116492329325755,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/NHC3/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06075455098541099,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "unresolved",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/NHC3/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.05020063320242029,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/NHC3/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2101242078168274,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/0.25/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.08999982677775874,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8664437278155491,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2919068402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/0.25/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0751108541867031,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.872962038014588,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.10090943528569678,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8513600448703635,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3075318402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/0.25/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0732616915767339,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.8766755459395119,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/1.0/0.1/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.06842677396309374,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9779432267177147,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/1.0/0.1/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.09129868302329051,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9757702245138156,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/1.0/0.05/canonical",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.07377814600734384,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.97796629543532,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/Berendsen/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.282995449014589,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/Berendsen/1.0/0.05/heated",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.08066633168353307,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/Berendsen/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.9758962473089666,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2011568303762045,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/0.25/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1263211715425267,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/0.25/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.25626757963570046,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/0.25/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1603078682805912,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/0.25/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.2011568303762045,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/1.0/0.1/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1263211715425267,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/1.0/0.1/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.13429544809882957,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.25626757963570046,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/1.0/0.05/canonical",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    },
    {
      "name": "NH/CDF/0.2/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.3934693402873666,
        "target": 0.08,
        "DKW_allowance": 0.18992244406633688,
        "simultaneous_classification": "certified_miss",
        "family_count_total": 256
      }
    },
    {
      "name": "NH/mean/0.2/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 0.1603078682805912,
        "target": 0.1
      }
    },
    {
      "name": "NH/variance/0.2/rescale/1.0/0.05/heated",
      "observed": false,
      "outcome": "unmet",
      "stored": {
        "observed": false,
        "actual": 1.0,
        "target": 0.2
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "NH/",
    "result_sha256": "45e4101f6676b2b971b144f5df45c1b28d3bff564d3896eeb309ee6c667d9351",
    "acceptance_sha256": "e741651e9ac010e4f500ce2d761a7d12c538827441fbec29a271dc526958cef2",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 49,
    "NH/short-accuracy/NH/0.0/actual": 1.5848659173536042e-07,
    "NH/short-order/NH/0.0/actual": 2.0000002696401498,
    "NH/Hext/NH/0.0/actual": 8.74237467788837e-08,
    "NH/Hext-order/NH/0.0/actual": 1.999999697088544,
    "NH/short-accuracy/NHC3/0.0/actual": 1.7014320588438852e-07,
    "NH/short-order/NHC3/0.0/actual": 1.9999999439963565,
    "NH/Hext/NHC3/0.0/actual": 8.273884871440915e-08,
    "NH/Hext-order/NHC3/0.0/actual": 1.99999954935859,
    "NH/short-accuracy/NH/0.2/actual": 1.6016483388561827e-07,
    "NH/short-order/NH/0.2/actual": 2.0000002894019273,
    "NH/Hext/NH/0.2/actual": 8.603876929816805e-08,
    "NH/Hext-order/NH/0.2/actual": 1.9999996336228278,
    "NH/short-accuracy/NHC3/0.2/actual": 1.719704998654336e-07,
    "NH/short-order/NHC3/0.2/actual": 1.9999999864219544,
    "NH/Hext/NHC3/0.2/actual": 8.162292742516266e-08,
    "NH/Hext-order/NHC3/0.2/actual": 1.9999994926009597,
    "NH/CDF/0.0/NH/0.25/0.1/canonical/actual": 0.037328055556311024,
    "NH/mean/0.0/NH/0.25/0.1/canonical/actual": 0.03486398684574196,
    "NH/variance/0.0/NH/0.25/0.1/canonical/actual": 0.30398764879622453,
    "NH/CDF/0.0/NH/0.25/0.1/heated/actual": 0.04044638234288861,
    "NH/mean/0.0/NH/0.25/0.1/heated/actual": 0.026637281607520547,
    "NH/variance/0.0/NH/0.25/0.1/heated/actual": 0.22964265488338453,
    "NH/CDF/0.0/NH/0.25/0.05/canonical/actual": 0.05444334970984788,
    "NH/mean/0.0/NH/0.25/0.05/canonical/actual": 0.03695958538816721,
    "NH/variance/0.0/NH/0.25/0.05/canonical/actual": 0.15799669961398322,
    "NH/CDF/0.0/NH/0.25/0.05/heated/actual": 0.06249999999998901,
    "NH/mean/0.0/NH/0.25/0.05/heated/actual": 0.057459905054390595,
    "NH/variance/0.0/NH/0.25/0.05/heated/actual": 0.18105229800118616,
    "NH/CDF/0.0/NH/1.0/0.1/canonical/actual": 0.06640624999998901,
    "NH/mean/0.0/NH/1.0/0.1/canonical/actual": 0.11068722077730915,
    "NH/variance/0.0/NH/1.0/0.1/canonical/actual": 0.062091457705365505,
    "NH/CDF/0.0/NH/1.0/0.1/heated/actual": 0.06009474606853438,
    "NH/mean/0.0/NH/1.0/0.1/heated/actual": 0.13897307728127148,
    "NH/variance/0.0/NH/1.0/0.1/heated/actual": 0.18301226348095767,
    "NH/CDF/0.0/NH/1.0/0.05/canonical/actual": 0.06640624999998901,
    "NH/mean/0.0/NH/1.0/0.05/canonical/actual": 0.11003077569742967,
    "NH/variance/0.0/NH/1.0/0.05/canonical/actual": 0.07468942818825863,
    "NH/CDF/0.0/NH/1.0/0.05/heated/actual": 0.06009474606853438,
    "NH/mean/0.0/NH/1.0/0.05/heated/actual": 0.1409948390802954,
    "NH/variance/0.0/NH/1.0/0.05/heated/actual": 0.18165625477400915,
    "NH/CDF/0.0/NHC3/0.25/0.1/canonical/actual": 0.049719340287366576,
    "NH/mean/0.0/NHC3/0.25/0.1/canonical/actual": 0.06289684847404169,
    "NH/variance/0.0/NHC3/0.25/0.1/canonical/actual": 0.105316960783008,
    "NH/CDF/0.0/NHC3/0.25/0.1/heated/actual": 0.08593749999998901,
    "NH/mean/0.0/NHC3/0.25/0.1/heated/actual": 0.2573503227438096,
    "NH/variance/0.0/NHC3/0.25/0.1/heated/actual": 0.20515080737770774,
    "NH/CDF/0.0/NHC3/0.25/0.05/canonical/actual": 0.03540040029015212,
    "NH/mean/0.0/NHC3/0.25/0.05/canonical/actual": 0.04390270719771237,
    "NH/variance/0.0/NHC3/0.25/0.05/canonical/actual": 0.18924157081826976,
    "NH/CDF/0.0/NHC3/0.25/0.05/heated/actual": 0.07055665029015212,
    "NH/mean/0.0/NHC3/0.25/0.05/heated/actual": 0.11734648106374199,
    "NH/variance/0.0/NHC3/0.25/0.05/heated/actual": 0.4896039036594748,
    "NH/CDF/0.0/NHC3/1.0/0.1/canonical/actual": 0.06746815971263342,
    "NH/mean/0.0/NHC3/1.0/0.1/canonical/actual": 0.04725976695909728,
    "NH/variance/0.0/NHC3/1.0/0.1/canonical/actual": 0.36374914504749767,
    "NH/CDF/0.0/NHC3/1.0/0.1/heated/actual": 0.05607138234288861,
    "NH/mean/0.0/NHC3/1.0/0.1/heated/actual": 0.07652781015232571,
    "NH/variance/0.0/NHC3/1.0/0.1/heated/actual": 0.16325205797201642,
    "NH/CDF/0.0/NHC3/1.0/0.05/canonical/actual": 0.07446290029015212,
    "NH/mean/0.0/NHC3/1.0/0.05/canonical/actual": 0.0763966647966805,
    "NH/variance/0.0/NHC3/1.0/0.05/canonical/actual": 0.43706617063137054,
    "NH/CDF/0.0/NHC3/1.0/0.05/heated/actual": 0.05468750000001105,
    "NH/mean/0.0/NHC3/1.0/0.05/heated/actual": 0.0893583787488137,
    "NH/variance/0.0/NHC3/1.0/0.05/heated/actual": 0.2583285746820181,
    "NH/CDF/0.0/Berendsen/0.25/0.1/canonical/actual": 0.3856568402873666,
    "NH/mean/0.0/Berendsen/0.25/0.1/canonical/actual": 0.04604737643210647,
    "NH/variance/0.0/Berendsen/0.25/0.1/canonical/actual": 0.8870863515317192,
    "NH/CDF/0.0/Berendsen/0.25/0.1/heated/actual": 0.3778443402873666,
    "NH/mean/0.0/Berendsen/0.25/0.1/heated/actual": 0.12181564034817975,
    "NH/variance/0.0/Berendsen/0.25/0.1/heated/actual": 0.8872338880995525,
    "NH/CDF/0.0/Berendsen/0.25/0.05/canonical/actual": 0.3817505902873666,
    "NH/mean/0.0/Berendsen/0.25/0.05/canonical/actual": 0.047247599054646615,
    "NH/variance/0.0/Berendsen/0.25/0.05/canonical/actual": 0.8809425672964785,
    "NH/CDF/0.0/Berendsen/0.25/0.05/heated/actual": 0.3778443402873666,
    "NH/mean/0.0/Berendsen/0.25/0.05/heated/actual": 0.13927847589865558,
    "NH/variance/0.0/Berendsen/0.25/0.05/heated/actual": 0.8835963267073677,
    "NH/CDF/0.0/Berendsen/1.0/0.1/canonical/actual": 0.3049316502901521,
    "NH/mean/0.0/Berendsen/1.0/0.1/canonical/actual": 0.0484600872046271,
    "NH/variance/0.0/Berendsen/1.0/0.1/canonical/actual": 0.9687775714089403,
    "NH/CDF/0.0/Berendsen/1.0/0.1/heated/actual": 0.4143066502901521,
    "NH/mean/0.0/Berendsen/1.0/0.1/heated/actual": 0.059532323355458695,
    "NH/variance/0.0/Berendsen/1.0/0.1/heated/actual": 0.9724826718739034,
    "NH/CDF/0.0/Berendsen/1.0/0.05/canonical/actual": 0.3010254002901521,
    "NH/mean/0.0/Berendsen/1.0/0.05/canonical/actual": 0.046271292290813205,
    "NH/variance/0.0/Berendsen/1.0/0.05/canonical/actual": 0.9713837969974201,
    "NH/CDF/0.0/Berendsen/1.0/0.05/heated/actual": 0.3830566502901521,
    "NH/mean/0.0/Berendsen/1.0/0.05/heated/actual": 0.05781974864183156,
    "NH/variance/0.0/Berendsen/1.0/0.05/heated/actual": 0.9726050181310519,
    "NH/CDF/0.0/rescale/0.25/0.1/canonical/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/0.25/0.1/canonical/actual": 0.14517705360713543,
    "NH/variance/0.0/rescale/0.25/0.1/canonical/actual": 1.0,
    "NH/CDF/0.0/rescale/0.25/0.1/heated/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/0.25/0.1/heated/actual": 0.135633888408617,
    "NH/variance/0.0/rescale/0.25/0.1/heated/actual": 1.0,
    "NH/CDF/0.0/rescale/0.25/0.05/canonical/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/0.25/0.05/canonical/actual": 0.2501231860393838,
    "NH/variance/0.0/rescale/0.25/0.05/canonical/actual": 1.0,
    "NH/CDF/0.0/rescale/0.25/0.05/heated/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/0.25/0.05/heated/actual": 0.18831515546963243,
    "NH/variance/0.0/rescale/0.25/0.05/heated/actual": 1.0,
    "NH/CDF/0.0/rescale/1.0/0.1/canonical/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/1.0/0.1/canonical/actual": 0.14517705360713543,
    "NH/variance/0.0/rescale/1.0/0.1/canonical/actual": 1.0,
    "NH/CDF/0.0/rescale/1.0/0.1/heated/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/1.0/0.1/heated/actual": 0.135633888408617,
    "NH/variance/0.0/rescale/1.0/0.1/heated/actual": 1.0,
    "NH/CDF/0.0/rescale/1.0/0.05/canonical/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/1.0/0.05/canonical/actual": 0.2501231860393838,
    "NH/variance/0.0/rescale/1.0/0.05/canonical/actual": 1.0,
    "NH/CDF/0.0/rescale/1.0/0.05/heated/actual": 0.3934693402873666,
    "NH/mean/0.0/rescale/1.0/0.05/heated/actual": 0.18831515546963243,
    "NH/variance/0.0/rescale/1.0/0.05/heated/actual": 1.0,
    "NH/CDF/0.2/NH/0.25/0.1/canonical/actual": 0.06534434028736658,
    "NH/mean/0.2/NH/0.25/0.1/canonical/actual": 0.06284212778751597,
    "NH/variance/0.2/NH/0.25/0.1/canonical/actual": 0.11102546209550827,
    "NH/CDF/0.2/NH/0.25/0.1/heated/actual": 0.07812500000001127,
    "NH/mean/0.2/NH/0.25/0.1/heated/actual": 0.12360137131850502,
    "NH/variance/0.2/NH/0.25/0.1/heated/actual": 0.09170819813518122,
    "NH/CDF/0.2/NH/0.25/0.05/canonical/actual": 0.04687500000001127,
    "NH/mean/0.2/NH/0.25/0.05/canonical/actual": 0.05721004933365359,
    "NH/variance/0.2/NH/0.25/0.05/canonical/actual": 0.15005473407900216,
    "NH/CDF/0.2/NH/0.25/0.05/heated/actual": 0.0756022167633873,
    "NH/mean/0.2/NH/0.25/0.05/heated/actual": 0.11840346270348634,
    "NH/variance/0.2/NH/0.25/0.05/heated/actual": 0.8769604823369499,
    "NH/CDF/0.2/NH/1.0/0.1/canonical/actual": 0.046183058828557666,
    "NH/mean/0.2/NH/1.0/0.1/canonical/actual": 0.035121849580839415,
    "NH/variance/0.2/NH/1.0/0.1/canonical/actual": 0.3318442738392695,
    "NH/CDF/0.2/NH/1.0/0.1/heated/actual": 0.14186546115985355,
    "NH/mean/0.2/NH/1.0/0.1/heated/actual": 0.13693043058618415,
    "NH/variance/0.2/NH/1.0/0.1/heated/actual": 0.3184680271130289,
    "NH/CDF/0.2/NH/1.0/0.05/canonical/actual": 0.042276808828557666,
    "NH/mean/0.2/NH/1.0/0.05/canonical/actual": 0.033849951652796584,
    "NH/variance/0.2/NH/1.0/0.05/canonical/actual": 0.3064253817265943,
    "NH/CDF/0.2/NH/1.0/0.05/heated/actual": 0.14186546115985355,
    "NH/mean/0.2/NH/1.0/0.05/heated/actual": 0.13526802617722264,
    "NH/variance/0.2/NH/1.0/0.05/heated/actual": 0.31833197329225116,
    "NH/CDF/0.2/NHC3/0.25/0.1/canonical/actual": 0.08984375000001199,
    "NH/mean/0.2/NHC3/0.25/0.1/canonical/actual": 0.1565814905108421,
    "NH/variance/0.2/NHC3/0.25/0.1/canonical/actual": 0.09620902195193537,
    "NH/CDF/0.2/NHC3/0.25/0.1/heated/actual": 0.08096934028736658,
    "NH/mean/0.2/NHC3/0.25/0.1/heated/actual": 0.13730437940946333,
    "NH/variance/0.2/NHC3/0.25/0.1/heated/actual": 0.1526691502918307,
    "NH/CDF/0.2/NHC3/0.25/0.05/canonical/actual": 0.023915168950881152,
    "NH/mean/0.2/NHC3/0.25/0.05/canonical/actual": 0.02922607618927936,
    "NH/variance/0.2/NHC3/0.25/0.05/canonical/actual": 0.1652834824088769,
    "NH/CDF/0.2/NHC3/0.25/0.05/heated/actual": 0.09499046115985355,
    "NH/mean/0.2/NHC3/0.25/0.05/heated/actual": 0.12277896692110372,
    "NH/variance/0.2/NHC3/0.25/0.05/heated/actual": 0.4577441059352447,
    "NH/CDF/0.2/NHC3/1.0/0.1/canonical/actual": 0.046183058828557666,
    "NH/mean/0.2/NHC3/1.0/0.1/canonical/actual": 0.039020070489949155,
    "NH/variance/0.2/NHC3/1.0/0.1/canonical/actual": 0.08073306245753575,
    "NH/CDF/0.2/NHC3/1.0/0.1/heated/actual": 0.05468750000001199,
    "NH/mean/0.2/NHC3/1.0/0.1/heated/actual": 0.05917037395513923,
    "NH/variance/0.2/NHC3/1.0/0.1/heated/actual": 0.27415201326715566,
    "NH/CDF/0.2/NHC3/1.0/0.05/canonical/actual": 0.042276808828557666,
    "NH/mean/0.2/NHC3/1.0/0.05/canonical/actual": 0.03459278194212745,
    "NH/variance/0.2/NHC3/1.0/0.05/canonical/actual": 0.10116492329325755,
    "NH/CDF/0.2/NHC3/1.0/0.05/heated/actual": 0.06075455098541099,
    "NH/mean/0.2/NHC3/1.0/0.05/heated/actual": 0.05020063320242029,
    "NH/variance/0.2/NHC3/1.0/0.05/heated/actual": 0.2101242078168274,
    "NH/CDF/0.2/Berendsen/0.25/0.1/canonical/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/0.25/0.1/canonical/actual": 0.08999982677775874,
    "NH/variance/0.2/Berendsen/0.25/0.1/canonical/actual": 0.8664437278155491,
    "NH/CDF/0.2/Berendsen/0.25/0.1/heated/actual": 0.2919068402873666,
    "NH/mean/0.2/Berendsen/0.25/0.1/heated/actual": 0.0751108541867031,
    "NH/variance/0.2/Berendsen/0.25/0.1/heated/actual": 0.872962038014588,
    "NH/CDF/0.2/Berendsen/0.25/0.05/canonical/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/0.25/0.05/canonical/actual": 0.10090943528569678,
    "NH/variance/0.2/Berendsen/0.25/0.05/canonical/actual": 0.8513600448703635,
    "NH/CDF/0.2/Berendsen/0.25/0.05/heated/actual": 0.3075318402873666,
    "NH/mean/0.2/Berendsen/0.25/0.05/heated/actual": 0.0732616915767339,
    "NH/variance/0.2/Berendsen/0.25/0.05/heated/actual": 0.8766755459395119,
    "NH/CDF/0.2/Berendsen/1.0/0.1/canonical/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/1.0/0.1/canonical/actual": 0.06842677396309374,
    "NH/variance/0.2/Berendsen/1.0/0.1/canonical/actual": 0.9779432267177147,
    "NH/CDF/0.2/Berendsen/1.0/0.1/heated/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/1.0/0.1/heated/actual": 0.09129868302329051,
    "NH/variance/0.2/Berendsen/1.0/0.1/heated/actual": 0.9757702245138156,
    "NH/CDF/0.2/Berendsen/1.0/0.05/canonical/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/1.0/0.05/canonical/actual": 0.07377814600734384,
    "NH/variance/0.2/Berendsen/1.0/0.05/canonical/actual": 0.97796629543532,
    "NH/CDF/0.2/Berendsen/1.0/0.05/heated/actual": 0.282995449014589,
    "NH/mean/0.2/Berendsen/1.0/0.05/heated/actual": 0.08066633168353307,
    "NH/variance/0.2/Berendsen/1.0/0.05/heated/actual": 0.9758962473089666,
    "NH/CDF/0.2/rescale/0.25/0.1/canonical/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/0.25/0.1/canonical/actual": 0.2011568303762045,
    "NH/variance/0.2/rescale/0.25/0.1/canonical/actual": 1.0,
    "NH/CDF/0.2/rescale/0.25/0.1/heated/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/0.25/0.1/heated/actual": 0.1263211715425267,
    "NH/variance/0.2/rescale/0.25/0.1/heated/actual": 1.0,
    "NH/CDF/0.2/rescale/0.25/0.05/canonical/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/0.25/0.05/canonical/actual": 0.25626757963570046,
    "NH/variance/0.2/rescale/0.25/0.05/canonical/actual": 1.0,
    "NH/CDF/0.2/rescale/0.25/0.05/heated/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/0.25/0.05/heated/actual": 0.1603078682805912,
    "NH/variance/0.2/rescale/0.25/0.05/heated/actual": 1.0,
    "NH/CDF/0.2/rescale/1.0/0.1/canonical/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/1.0/0.1/canonical/actual": 0.2011568303762045,
    "NH/variance/0.2/rescale/1.0/0.1/canonical/actual": 1.0,
    "NH/CDF/0.2/rescale/1.0/0.1/heated/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/1.0/0.1/heated/actual": 0.1263211715425267,
    "NH/variance/0.2/rescale/1.0/0.1/heated/actual": 1.0,
    "NH/CDF/0.2/rescale/1.0/0.05/canonical/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/1.0/0.05/canonical/actual": 0.25626757963570046,
    "NH/variance/0.2/rescale/1.0/0.05/canonical/actual": 1.0,
    "NH/CDF/0.2/rescale/1.0/0.05/heated/actual": 0.3934693402873666,
    "NH/mean/0.2/rescale/1.0/0.05/heated/actual": 0.1603078682805912,
    "NH/variance/0.2/rescale/1.0/0.05/heated/actual": 1.0
  },
  "checks": {
    "NH/phi1-limit-and-branches": true,
    "NH/fullODE-Hext-derivative": true,
    "NH/physical-R-reversal": true,
    "NH/Berendsen-local-inverse": true,
    "NH/Berendsen-invalid-rejected": true,
    "NH/rescale-noninjective-idempotent": true,
    "NH/unexcited-invariant-control": true,
    "NH/static-reference/0.0": true,
    "NH/short-reference/NH/0.0": true,
    "NH/short-reference/NHC3/0.0": true,
    "NH/static-reference/0.2": true,
    "NH/short-reference/NH/0.2": true,
    "NH/short-reference/NHC3/0.2": true,
    "NH/CDF-family-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- GROMACS2026.4,Temperature coupling. https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 拘束・重心除去と正準統計

有効自由度、運動量共分散、過渡分布と時間相関を分けて検証します。

**使用手法**

- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)
- [確率的速度リスケーリング（CSVR）](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=ja) (`stochastic-velocity-rescaling`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-algorithm)

質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

- [固定線形拘束の正準運動量](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#projected-canonical-model-ja) (`projected-canonical-model`)

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。


**問題の図**

![拘束・重心除去と正準統計：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja) (`projected-canonical-dof`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=ja#projected-canonical-dof-ja-validation)

Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。

- [拘束・重心除去と正準統計](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-projected-canonical-dof-ja) (`projected-canonical-dof`; 同じ問題の参照 · 半解析参照)

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。
### 前提・単位・境界

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

**編集上の補足**

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

### 採用した計算法

質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

### 比較・検証

Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。

### 確認の限界

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

### 調査した目標：達成120・未達0・未確定0（全120）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 120,
    "unmet": 0,
    "unresolved": 0,
    "total": 120
  },
  "goals": [
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018695766970879935,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01869576697088876,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0283203125,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0283203125,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.017578125,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.017578125,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.021955081901200657,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.021894131288046875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01953125,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01953125,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018695766970879935,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01869576697088876,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.029821308568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02989781212894929,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027484829470879935,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027305049183806218,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0146484375,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0146484375,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/Langevin/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.020253192449110724,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/0/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.020249483398038115,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018695766970879935,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0205078125,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019006816431457074,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027795878931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018695766970879935,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.020978519401200657,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0283203125,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.030018817449110724,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/0/CSVR/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.026082566171442334,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0256479835502319,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.012170878931457074,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.011991662569849182,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023522847212633424,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023451596879722536,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0185546875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0185546875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02782422057140488,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027766763237865477,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.013387253671442334,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.013231484438227747,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/Langevin/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023030595736612702,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/1/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023029285404728705,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0166015625,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023722121328557666,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.034704121068542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019983378931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019616597212633424,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022913066431457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.017663472212633424,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/1/CSVR/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.025305277787366576,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.021936503931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.021781729955460932,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.013147441431457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01291215635571688,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.020435507862913926,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0203913062368255,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0263671875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0185546875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0185546875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023510144550285217,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023409241981393603,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014070048603641583,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.014075036386548945,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/Langevin/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0146484375,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/2/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0146484375,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0234375,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.019603894550285217,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02440612781304652,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.010054819448179209,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02539855968695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0322265625,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02442199718695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.012623007862913926,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/2/CSVR/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02344543468695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.030797871068542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.030952645044539068,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01758605968695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.017158704828836413,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.010814492137086074,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.010858693763174498,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.018627332050285217,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01861171862351685,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.011194316431457074,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.011155653097271623,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.020055683568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02011450793625133,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01171875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01171875,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/Langevin/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0224609375,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/discreteCDF/3/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0224609375,
        "nominal_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.1/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.1/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0341796875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.1/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.01171875,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.1/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.021936503931457046,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.1/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.027271445362913926,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.05/0.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.022008808568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.05/0.5",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.02051574718695348,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.05/1.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.025842753931457074,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.05/2.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.016149433568542954,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    },
    {
      "name": "constraints/canonicalCDF/3/CSVR/0.05/4.0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.023364855449714783,
        "target": 0.08,
        "DKW_allowance": 0.06659442823030644
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "constraints/",
    "result_sha256": "45e4101f6676b2b971b144f5df45c1b28d3bff564d3896eeb309ee6c667d9351",
    "acceptance_sha256": "e741651e9ac010e4f500ce2d761a7d12c538827441fbec29a271dc526958cef2",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 21,
    "constraints/canonicalCDF/0/Langevin/0.1/0.0/actual": 0.018695766970879935,
    "constraints/discreteCDF/0/0.1/0.0/actual": 0.01869576697088876,
    "constraints/canonicalCDF/0/Langevin/0.1/0.5/actual": 0.0283203125,
    "constraints/discreteCDF/0/0.1/0.5/actual": 0.0283203125,
    "constraints/canonicalCDF/0/Langevin/0.1/1.0/actual": 0.017578125,
    "constraints/discreteCDF/0/0.1/1.0/actual": 0.017578125,
    "constraints/canonicalCDF/0/Langevin/0.1/2.0/actual": 0.021955081901200657,
    "constraints/discreteCDF/0/0.1/2.0/actual": 0.021894131288046875,
    "constraints/canonicalCDF/0/Langevin/0.1/4.0/actual": 0.01953125,
    "constraints/discreteCDF/0/0.1/4.0/actual": 0.01953125,
    "constraints/canonicalCDF/0/Langevin/0.05/0.0/actual": 0.018695766970879935,
    "constraints/discreteCDF/0/0.05/0.0/actual": 0.01869576697088876,
    "constraints/canonicalCDF/0/Langevin/0.05/0.5/actual": 0.029821308568542954,
    "constraints/discreteCDF/0/0.05/0.5/actual": 0.02989781212894929,
    "constraints/canonicalCDF/0/Langevin/0.05/1.0/actual": 0.027484829470879935,
    "constraints/discreteCDF/0/0.05/1.0/actual": 0.027305049183806218,
    "constraints/canonicalCDF/0/Langevin/0.05/2.0/actual": 0.0146484375,
    "constraints/discreteCDF/0/0.05/2.0/actual": 0.0146484375,
    "constraints/canonicalCDF/0/Langevin/0.05/4.0/actual": 0.020253192449110724,
    "constraints/discreteCDF/0/0.05/4.0/actual": 0.020249483398038115,
    "constraints/canonicalCDF/0/CSVR/0.1/0.0/actual": 0.018695766970879935,
    "constraints/canonicalCDF/0/CSVR/0.1/0.5/actual": 0.0205078125,
    "constraints/canonicalCDF/0/CSVR/0.1/1.0/actual": 0.0263671875,
    "constraints/canonicalCDF/0/CSVR/0.1/2.0/actual": 0.019006816431457074,
    "constraints/canonicalCDF/0/CSVR/0.1/4.0/actual": 0.027795878931457046,
    "constraints/canonicalCDF/0/CSVR/0.05/0.0/actual": 0.018695766970879935,
    "constraints/canonicalCDF/0/CSVR/0.05/0.5/actual": 0.020978519401200657,
    "constraints/canonicalCDF/0/CSVR/0.05/1.0/actual": 0.0283203125,
    "constraints/canonicalCDF/0/CSVR/0.05/2.0/actual": 0.030018817449110724,
    "constraints/canonicalCDF/0/CSVR/0.05/4.0/actual": 0.0263671875,
    "constraints/canonicalCDF/1/Langevin/0.1/0.0/actual": 0.019983378931457046,
    "constraints/discreteCDF/1/0.1/0.0/actual": 0.019983378931457046,
    "constraints/canonicalCDF/1/Langevin/0.1/0.5/actual": 0.026082566171442334,
    "constraints/discreteCDF/1/0.1/0.5/actual": 0.0256479835502319,
    "constraints/canonicalCDF/1/Langevin/0.1/1.0/actual": 0.012170878931457074,
    "constraints/discreteCDF/1/0.1/1.0/actual": 0.011991662569849182,
    "constraints/canonicalCDF/1/Langevin/0.1/2.0/actual": 0.023522847212633424,
    "constraints/discreteCDF/1/0.1/2.0/actual": 0.023451596879722536,
    "constraints/canonicalCDF/1/Langevin/0.1/4.0/actual": 0.0185546875,
    "constraints/discreteCDF/1/0.1/4.0/actual": 0.0185546875,
    "constraints/canonicalCDF/1/Langevin/0.05/0.0/actual": 0.019983378931457046,
    "constraints/discreteCDF/1/0.05/0.0/actual": 0.019983378931457046,
    "constraints/canonicalCDF/1/Langevin/0.05/0.5/actual": 0.02782422057140488,
    "constraints/discreteCDF/1/0.05/0.5/actual": 0.027766763237865477,
    "constraints/canonicalCDF/1/Langevin/0.05/1.0/actual": 0.013387253671442334,
    "constraints/discreteCDF/1/0.05/1.0/actual": 0.013231484438227747,
    "constraints/canonicalCDF/1/Langevin/0.05/2.0/actual": 0.0263671875,
    "constraints/discreteCDF/1/0.05/2.0/actual": 0.0263671875,
    "constraints/canonicalCDF/1/Langevin/0.05/4.0/actual": 0.023030595736612702,
    "constraints/discreteCDF/1/0.05/4.0/actual": 0.023029285404728705,
    "constraints/canonicalCDF/1/CSVR/0.1/0.0/actual": 0.019983378931457046,
    "constraints/canonicalCDF/1/CSVR/0.1/0.5/actual": 0.019983378931457046,
    "constraints/canonicalCDF/1/CSVR/0.1/1.0/actual": 0.0166015625,
    "constraints/canonicalCDF/1/CSVR/0.1/2.0/actual": 0.023722121328557666,
    "constraints/canonicalCDF/1/CSVR/0.1/4.0/actual": 0.034704121068542954,
    "constraints/canonicalCDF/1/CSVR/0.05/0.0/actual": 0.019983378931457046,
    "constraints/canonicalCDF/1/CSVR/0.05/0.5/actual": 0.019616597212633424,
    "constraints/canonicalCDF/1/CSVR/0.05/1.0/actual": 0.022913066431457046,
    "constraints/canonicalCDF/1/CSVR/0.05/2.0/actual": 0.017663472212633424,
    "constraints/canonicalCDF/1/CSVR/0.05/4.0/actual": 0.025305277787366576,
    "constraints/canonicalCDF/2/Langevin/0.1/0.0/actual": 0.02539855968695348,
    "constraints/discreteCDF/2/0.1/0.0/actual": 0.02539855968695348,
    "constraints/canonicalCDF/2/Langevin/0.1/0.5/actual": 0.021936503931457046,
    "constraints/discreteCDF/2/0.1/0.5/actual": 0.021781729955460932,
    "constraints/canonicalCDF/2/Langevin/0.1/1.0/actual": 0.013147441431457046,
    "constraints/discreteCDF/2/0.1/1.0/actual": 0.01291215635571688,
    "constraints/canonicalCDF/2/Langevin/0.1/2.0/actual": 0.020435507862913926,
    "constraints/discreteCDF/2/0.1/2.0/actual": 0.0203913062368255,
    "constraints/canonicalCDF/2/Langevin/0.1/4.0/actual": 0.0263671875,
    "constraints/discreteCDF/2/0.1/4.0/actual": 0.0263671875,
    "constraints/canonicalCDF/2/Langevin/0.05/0.0/actual": 0.02539855968695348,
    "constraints/discreteCDF/2/0.05/0.0/actual": 0.02539855968695348,
    "constraints/canonicalCDF/2/Langevin/0.05/0.5/actual": 0.0185546875,
    "constraints/discreteCDF/2/0.05/0.5/actual": 0.0185546875,
    "constraints/canonicalCDF/2/Langevin/0.05/1.0/actual": 0.023510144550285217,
    "constraints/discreteCDF/2/0.05/1.0/actual": 0.023409241981393603,
    "constraints/canonicalCDF/2/Langevin/0.05/2.0/actual": 0.014070048603641583,
    "constraints/discreteCDF/2/0.05/2.0/actual": 0.014075036386548945,
    "constraints/canonicalCDF/2/Langevin/0.05/4.0/actual": 0.0146484375,
    "constraints/discreteCDF/2/0.05/4.0/actual": 0.0146484375,
    "constraints/canonicalCDF/2/CSVR/0.1/0.0/actual": 0.02539855968695348,
    "constraints/canonicalCDF/2/CSVR/0.1/0.5/actual": 0.0234375,
    "constraints/canonicalCDF/2/CSVR/0.1/1.0/actual": 0.019603894550285217,
    "constraints/canonicalCDF/2/CSVR/0.1/2.0/actual": 0.02440612781304652,
    "constraints/canonicalCDF/2/CSVR/0.1/4.0/actual": 0.010054819448179209,
    "constraints/canonicalCDF/2/CSVR/0.05/0.0/actual": 0.02539855968695348,
    "constraints/canonicalCDF/2/CSVR/0.05/0.5/actual": 0.0322265625,
    "constraints/canonicalCDF/2/CSVR/0.05/1.0/actual": 0.02442199718695348,
    "constraints/canonicalCDF/2/CSVR/0.05/2.0/actual": 0.012623007862913926,
    "constraints/canonicalCDF/2/CSVR/0.05/4.0/actual": 0.02344543468695348,
    "constraints/canonicalCDF/3/Langevin/0.1/0.0/actual": 0.022008808568542954,
    "constraints/discreteCDF/3/0.1/0.0/actual": 0.022008808568542954,
    "constraints/canonicalCDF/3/Langevin/0.1/0.5/actual": 0.030797871068542954,
    "constraints/discreteCDF/3/0.1/0.5/actual": 0.030952645044539068,
    "constraints/canonicalCDF/3/Langevin/0.1/1.0/actual": 0.01758605968695348,
    "constraints/discreteCDF/3/0.1/1.0/actual": 0.017158704828836413,
    "constraints/canonicalCDF/3/Langevin/0.1/2.0/actual": 0.010814492137086074,
    "constraints/discreteCDF/3/0.1/2.0/actual": 0.010858693763174498,
    "constraints/canonicalCDF/3/Langevin/0.1/4.0/actual": 0.018627332050285217,
    "constraints/discreteCDF/3/0.1/4.0/actual": 0.01861171862351685,
    "constraints/canonicalCDF/3/Langevin/0.05/0.0/actual": 0.022008808568542954,
    "constraints/discreteCDF/3/0.05/0.0/actual": 0.022008808568542954,
    "constraints/canonicalCDF/3/Langevin/0.05/0.5/actual": 0.011194316431457074,
    "constraints/discreteCDF/3/0.05/0.5/actual": 0.011155653097271623,
    "constraints/canonicalCDF/3/Langevin/0.05/1.0/actual": 0.020055683568542954,
    "constraints/discreteCDF/3/0.05/1.0/actual": 0.02011450793625133,
    "constraints/canonicalCDF/3/Langevin/0.05/2.0/actual": 0.01171875,
    "constraints/discreteCDF/3/0.05/2.0/actual": 0.01171875,
    "constraints/canonicalCDF/3/Langevin/0.05/4.0/actual": 0.0224609375,
    "constraints/discreteCDF/3/0.05/4.0/actual": 0.0224609375,
    "constraints/canonicalCDF/3/CSVR/0.1/0.0/actual": 0.022008808568542954,
    "constraints/canonicalCDF/3/CSVR/0.1/0.5/actual": 0.0341796875,
    "constraints/canonicalCDF/3/CSVR/0.1/1.0/actual": 0.01171875,
    "constraints/canonicalCDF/3/CSVR/0.1/2.0/actual": 0.021936503931457046,
    "constraints/canonicalCDF/3/CSVR/0.1/4.0/actual": 0.027271445362913926,
    "constraints/canonicalCDF/3/CSVR/0.05/0.0/actual": 0.022008808568542954,
    "constraints/canonicalCDF/3/CSVR/0.05/0.5/actual": 0.02051574718695348,
    "constraints/canonicalCDF/3/CSVR/0.05/1.0/actual": 0.025842753931457074,
    "constraints/canonicalCDF/3/CSVR/0.05/2.0/actual": 0.016149433568542954,
    "constraints/canonicalCDF/3/CSVR/0.05/4.0/actual": 0.023364855449714783
  },
  "checks": {
    "constraints/rank/0": true,
    "constraints/projector/0": true,
    "constraints/rational-covariance/0": true,
    "constraints/projected-OU-positive/0": true,
    "constraints/rank/1": true,
    "constraints/projector/1": true,
    "constraints/rational-covariance/1": true,
    "constraints/projected-OU-positive/1": true,
    "constraints/rank/2": true,
    "constraints/projector/2": true,
    "constraints/rational-covariance/2": true,
    "constraints/projected-OU-positive/2": true,
    "constraints/rank/3": true,
    "constraints/projector/3": true,
    "constraints/rational-covariance/3": true,
    "constraints/projected-OU-positive/3": true,
    "constraints/full-rank-zero-dimensional-fixture": true,
    "constraints/redundant-common-latent": true,
    "constraints/six-signed-f1": true,
    "constraints/f0-rejects": true,
    "constraints/zeroK-rejects": true,
    "constraints/h0-owned-copy": true,
    "constraints/wrong-ambient-CSVR-detected": true,
    "constraints/actual-tangent/0/Langevin/0.1": true,
    "constraints/actual-tangent/0/Langevin/0.05": true,
    "constraints/actual-tangent/0/CSVR/0.1": true,
    "constraints/actual-tangent/0/CSVR/0.05": true,
    "constraints/actual-tangent/1/Langevin/0.1": true,
    "constraints/actual-tangent/1/Langevin/0.05": true,
    "constraints/actual-tangent/1/CSVR/0.1": true,
    "constraints/actual-tangent/1/CSVR/0.05": true,
    "constraints/actual-tangent/2/Langevin/0.1": true,
    "constraints/actual-tangent/2/Langevin/0.05": true,
    "constraints/actual-tangent/2/CSVR/0.1": true,
    "constraints/actual-tangent/2/CSVR/0.05": true,
    "constraints/actual-tangent/3/Langevin/0.1": true,
    "constraints/actual-tangent/3/Langevin/0.05": true,
    "constraints/actual-tangent/3/CSVR/0.1": true,
    "constraints/actual-tangent/3/CSVR/0.05": true,
    "constraints/CDF-family-count": true,
    "constraints/continuous-reference-count": true,
    "constraints/discrete-covariance-count": true,
    "constraints/initial-normal-count": true,
    "constraints/Langevin-normal-count": true,
    "constraints/CSVR-normal-count": true,
    "constraints/CSVR-chi-square-count": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- LAMMPS,compute temp. https://docs.lammps.org/compute_temp.html; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Bussi,Donadio,Parrinello,Canonical sampling through velocity-rescaling. https://arxiv.org/pdf/0803.4060; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
