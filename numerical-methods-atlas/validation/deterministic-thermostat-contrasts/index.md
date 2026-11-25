# NH・chain・弱結合・速度固定の比較

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
## 前提・単位・境界

単位質量,kBT=1、周波数1/1.7、quartic係数0/0.2。NH1/NHC3/Berendsen/速度固定、2結合・2刻み、正準256＋加熱128レプリカを固定します。

**編集上の補足**

著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。 調査目標には、異なる熱浴の正準モーメント・相関と、固定した正準/加熱アンサンブルの有限時刻での比較が含まれます。未達は熱浴・初期集団ごとの結果を残したもので、必須の実装・再現検査とは別に読みます。

## 採用した計算法

明示した凍結変数の厳密bath部分流を対称合成し、各半bathを2副周期で計算します。etaはE部分流だけで進め、独立な全拡張ODEの短時間参照と照合します。

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

## 比較・検証

物理的時間反転、Hextの微分、phi1、弱結合の局所逆と非可逆な速度固定を別に検査。時刻20の4分布・揺らぎ・符号付き相関とDKWの未確定範囲を残します。

## 確認の限界

著者作成の分割でありLAMMPS/MKT実装の完全再現ではありません。時刻20は混合・平衡化の証明でなく、平均温度一致だけで正準分布や一般的なエルゴード性を認定しません。

## 調査した目標：達成91・未達117・未確定0（全208）

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

## 保存実測値と判定

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

## 取得・実行

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

## 出典と確認範囲

- GROMACS2026.4,Temperature coupling. https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# NH,chains,weak coupling and fixed-speed contrasts

Compare distributions,fluctuations and correlations as well as mean temperature on the same two-mode systems.

**Methods used**

- [Nosé–Hoover thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover/?lang=en) (`nose-hoover`)
- [Nosé–Hoover chains](https://hrkoyama.github.io/numerical-methods-atlas/methods/nose-hoover-chains/?lang=en) (`nose-hoover-chains`)
- [Berendsen weak-coupling thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/berendsen-thermostat/?lang=en) (`berendsen-thermostat`)
- [Direct velocity rescaling](https://hrkoyama.github.io/numerical-methods-atlas/methods/velocity-rescaling/?lang=en) (`velocity-rescaling`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-algorithm)

Symmetrically compose exact frozen-variable bath subflows,two subcycles per half bath. Advance eta only in E subflows and compare short trajectories against independent full extendedODE references.

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

- [Hamiltonian systems and oscillators](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hamiltonian-en) (`hamiltonian`)

Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas.

- [Two-mode deterministic thermostat model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#finite-mode-thermostat-model-en) (`finite-mode-thermostat-model`)

Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas.


**Problem figure**

![NH,chains,weak coupling and fixed-speed contrasts: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Anharmonic CSVR versus Langevin: distribution checks against Boltzmann quadrature](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en) (`thermostatted-quartic`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/thermostatted-quartic/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/?lang=en#deterministic-thermostat-contrasts-en-validation)

Separately test physical reversal,Hext derivative,phi1,local weak-coupling inverses and noninjective rescaling. Retain four distributions,fluctuations,signed correlations and unresolved DKW precision at time20.

- [NH,chains,weak coupling and fixed-speed contrasts](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-deterministic-thermostat-contrasts-en) (`deterministic-thermostat-contrasts`; Same-problem reference · Semi-analytic reference)

Same two-mode quartic system plus a harmonic control; short-time and finite-sample deterministic-bath comparisons.
## Assumptions, units and boundaries

Fix unit masses,kBT1,frequencies1/1.7 and quartic0/.2. Compare NH1,NHC3,Berendsen and fixed-speed baths at two couplings/two steps with256canonical and128heated replicas.

**Editorial clarification**

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity. Study targets compare canonical moments and correlations across different baths and finite-time canonical/heated ensembles. Retained unmet outcomes must be read by bath and initial ensemble, separately from mandatory implementation and reproduction checks.

## Adopted numerical method

Symmetrically compose exact frozen-variable bath subflows,two subcycles per half bath. Advance eta only in E subflows and compare short trajectories against independent full extendedODE references.

$$
\dot p=-\nabla U-\xi_1p,\quad\dot\xi_1=(2K-fT)/Q_1-\xi_2\xi_1
$$

$$
H_{ext}=H+\sum_jQ_j\xi_j^2/2+fT\eta_1+T\sum_{j>1}\eta_j
$$

## References and validation

Separately test physical reversal,Hext derivative,phi1,local weak-coupling inverses and noninjective rescaling. Retain four distributions,fluctuations,signed correlations and unresolved DKW precision at time20.

## Limits

This authored splitting is not a full LAMMPS/MKT reproduction. Time20does not prove mixing/equilibration; correct mean temperature alone does not establish canonical sampling or general ergodicity.

## Study goals: 91 met, 117 unmet, 0 unresolved (208 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

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

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/deterministic-thermostat-contrasts/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/deterministic-thermostat-contrasts-diagnostics.png)

Separate actual accuracy,reference and statistical measurements,including unmet targets.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/atlas-thermostat-constraint-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- GROMACS2026.4,Temperature coupling. https://manual.gromacs.org/current/reference-manual/algorithms/molecular-dynamics.html; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
Selected original abstract on the author-uploaded page:IID/two-sidedconstant2. Official body access was blocked by an iframe; proof unread.

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
Selected v1pp1–3:IIDsetup,Theorem1,Corollaries1/2. Detailed proofs unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
