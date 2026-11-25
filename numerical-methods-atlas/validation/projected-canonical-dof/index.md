# 拘束・重心除去と正準統計

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
## 前提・単位・境界

質量1/2/3の1D3粒子と1つの共通調和ポテンシャル。拘束なし・COM・COM＋相対・冗長行を含む同じ拘束でf=3/2/1/1、各1,024レプリカを用います。

**編集上の補足**

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

## 採用した計算法

質量重み付き接空間でLangevin/CSVRをOBABO分割します。初期正準共分散からの有限時刻写像・雑音共分散を直接組み、連続参照と離散定常Lyapunov解を別に求めます。

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

## 比較・検証

Fractionによる独立なrank/共分散、符号付きf1浴、正しい投影OU恒等式と誤ったambient自由度の負例を照合。220分布族、符号付き2時刻積、正しい/誤った温度分母を保存します。

## 確認の限界

固定線形拘束の小例です。非線形分子拘束、Fixman補正、輸送係数へ一般化しません。独立seedの冗長拘束系には軌跡の一致を要求せず、CSVRの動的相関は経験的な結果です。

## 調査した目標：達成120・未達0・未確定0（全120）

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

## 保存実測値と判定

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

- LAMMPS,compute temp. https://docs.lammps.org/compute_temp.html; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Bussi,Donadio,Parrinello,Canonical sampling through velocity-rescaling. https://arxiv.org/pdf/0803.4060; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
著者公開ページの原著抄録でIID・両側定数2を確認。公式本文はiframeで閲覧できず、証明の全読はしていません。

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
v1の1–3頁、IID設定・定理1・系1/2のみ確認。詳細な証明は未読です。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Constraints,centre-of-mass removal and canonical statistics

Separate effectiveDOF,momentum covariance,transient distributions and time correlations.

**Methods used**

- [Langevin thermostat](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=en) (`langevin-thermostat`)
- [Stochastic velocity rescaling (CSVR)](https://hrkoyama.github.io/numerical-methods-atlas/methods/stochastic-velocity-rescaling/?lang=en) (`stochastic-velocity-rescaling`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-algorithm)

Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

- [Canonical momentum under fixed linear constraints](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#projected-canonical-model-en) (`projected-canonical-model`)

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.


**Problem figure**

![Constraints,centre-of-mass removal and canonical statistics: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en) (`projected-canonical-dof`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/projected-canonical-dof/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/?lang=en#projected-canonical-dof-en-validation)

Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.

- [Constraints,centre-of-mass removal and canonical statistics](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-projected-canonical-dof-en) (`projected-canonical-dof`; Same-problem reference · Semi-analytic reference)

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.
## Assumptions, units and boundaries

Use three1Dparticles of masses1/2/3 in one common harmonic potential. No constraints,COM,COM-relative and a redundant-row equivalent have f3/2/1/1,each with1,024replicas.

**Editorial clarification**

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

## Adopted numerical method

Apply tangent-space Langevin/CSVR in OBABO form. Build finite-time maps and noise covariance from canonical initial data; compute continuous references and stationary discrete Lyapunov solutions separately.

$$
Cq=0,\quad CM^{-1}p=0,\quad f=3-\mathrm{rank}(C)
$$

$$
\mathrm{Cov}(p)=T(M-C^T(CM^{-1}C^T)^+C)
$$

## References and validation

Check independent Fraction rank/covariance,signedf1 baths,the valid projectedOU identity and a wrong-ambientDOF counterexample. Retain220CDF families,signed two-time products and correct/incorrect temperature denominators.

## Limits

These fixed linear constraints do not cover nonlinear molecular constraints,Fixman corrections or transport coefficients. Redundant systems with independent seeds need not have identical paths; CSVR dynamical correlations are empirical.

## Study goals: 120 met, 0 unmet, 0 unresolved (120 total)

Mandatory qualification is separate from study-goal attainment. Met/unmet follow stored comparisons, not statistical certification. Unresolved and separate uncertainty classifications are retained; null is not replaced by false or zero.

[Original saved results / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/result.json)

<details><summary>Read every study-goal record</summary>

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

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/projected-canonical-dof/index.json

![Separate actual accuracy,reference and statistical measurements,including unmet targets.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/thermostat-constraint-controls/results/projected-canonical-dof-diagnostics.png)

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

- LAMMPS,compute temp. https://docs.lammps.org/compute_temp.html; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.

- Bussi,Donadio,Parrinello,Canonical sampling through velocity-rescaling. https://arxiv.org/pdf/0803.4060; review_level=selected-primary-or-bibliographic-see-provenance
Actual selected read scopes and unread limits are recorded in source-reading.json; no full original-paper equation/figure reproduction claim.

- Massart(1990),The Tight Constant in the Dvoretzky–Kiefer–Wolfowitz Inequality. https://doi.org/10.1214/aop/1176990746; review_level=selected-primary-abstract
Selected original abstract on the author-uploaded page:IID/two-sidedconstant2. Official body access was blocked by an iframe; proof unread.

- Reeve(2024),A short proof of the Dvoretzky–Kiefer–Wolfowitz–Massart inequality. https://arxiv.org/pdf/2403.16651; review_level=selected-primary-theorem
Selected v1pp1–3:IIDsetup,Theorem1,Corollaries1/2. Detailed proofs unread.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
