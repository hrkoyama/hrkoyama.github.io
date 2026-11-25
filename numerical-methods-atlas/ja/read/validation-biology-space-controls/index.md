# 生物反応拡散の2次元・境界検証

Fisherの特殊速度前線、2次元Schnakenbergの境界別過渡、外力付きKeller–Segelのセル平均・流束を独立参照と比べます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Fisher–KPP：特殊波速の厳密前線

波形・位置・格子誤差・時間誤差・有限領域の影響を分けます。

**使用手法**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-algorithm)

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

- [Fisher–KPP侵入前線](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-fisher-kpp-ja) (`bio-fisher-kpp`)

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。


**問題の図**

![Fisher–KPP：特殊波速の厳密前線：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja) (`fisher-kpp-special-front`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fisher-kpp-special-front/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/?lang=ja#fisher-kpp-special-front-ja-validation)

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

- [Fisher–KPP：特殊波速の厳密前線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fisher-kpp-special-front-ja) (`fisher-kpp-special-front`; 同じ問題の参照 · 解析参照)

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。
### 前提・単位・境界

D=r=1、T=1。Ablowitz–Zeppetella型の特殊波速5/√6、L=12の空間・時間系列、定数端点L=6/12/24の境界比較を固定します。

**編集上の補足**

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

### 採用した計算法

2次中心差分とSSPRK3で計算し、厳密Dirichlet値を各段の時刻で与えます。時間誤差は同じ95未知数の半離散ODE参照と比較します。

$$
u_t=u_{xx}+u(1-u)
$$

$$
u(x,t)=[1+\exp((x-5t/\sqrt6)/\sqrt6)]^{-2}
$$

### 比較・検証

厳密波形と1/4等値線、同一格子の時間収束、全域と中央領域の境界誤差を別保存します。実数算術の離散障壁と、実測した浮動小数点の余裕を区別します。

### 確認の限界

特殊前線を一般の最小速度2の前線と同一視しません。急減衰初期値からの速度選択、長時間伝播、機械誤差込みの厳密障壁証明は対象外です。

### 調査した目標：達成6・未達0・未確定0（全6）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 6,
    "unmet": 0,
    "unresolved": 0,
    "total": 6
  },
  "goals": [
    {
      "name": "Fisher/space-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 9.239320837961529e-06,
        "target": 0.001
      }
    },
    {
      "name": "Fisher/space-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9958436278085308,
        "target": 1.7
      }
    },
    {
      "name": "Fisher/phase",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0002657675674280213,
        "target": 0.02
      }
    },
    {
      "name": "Fisher/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0607173908690903,
        "target": 2.7,
        "reference_spread": 2.886579864025407e-15
      }
    },
    {
      "name": "Fisher/time-finest",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.8780066390888805e-10,
        "target": 1e-05
      }
    },
    {
      "name": "Fisher/observed-boundary-margin",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "observed_margin": 9.999999795441408e-05,
        "scope": "Observed binary64 margin; analyticreal-arithmetic barrier is not a machine-error certificate"
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Fisher/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 11,
    "Fisher/space-finest/actual": 9.239320837961529e-06,
    "Fisher/space-order/actual": 1.9958436278085308,
    "Fisher/phase/actual": 0.0002657675674280213,
    "Fisher/time-order/actual": 3.0607173908690903,
    "Fisher/time-finest/actual": 1.8780066390888805e-10,
    "Fisher/observed-boundary-margin/observed_margin": 9.999999795441408e-05
  },
  "checks": {
    "Fisher/exact-PDE": true,
    "Fisher/wrong-special-speed-detected": true,
    "Fisher/finite-space/0.5": true,
    "Fisher/finite-space/0.25": true,
    "Fisher/finite-space/0.125": true,
    "Fisher/semidiscrete-reference": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fisher-kpp-special-front/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/fisher-kpp-special-front-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Ablowitz–Zeppetella(1979), Explicit solutions of Fisher’s equation for a special wave speed. https://doi.org/10.1007/BF02462380; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Schnakenberg：2D境界と初期モード

2つのNeumann摂動とDirichlet摂動を独立な非線形Galerkin参照と比較します。

**使用手法**

- [Crank–Nicolson法](https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja) (`crank-nicolson`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-algorithm)

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

- [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja) (`bio-schnakenberg`)

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。


**問題の図**

![Schnakenberg：2D境界と初期モード：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja) (`schnakenberg-2d-boundary-modes`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/schnakenberg-2d-boundary-modes/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/?lang=ja#schnakenberg-2d-boundary-modes-ja-validation)

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

- [Schnakenberg：2D境界と初期モード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-schnakenberg-2d-boundary-modes-ja) (`schnakenberg-2d-boundary-modes`; 同じ問題の参照 · 有限格子の数値参照)

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。
### 前提・単位・境界

[0,2π]²、T=2、a=0.1,b=0.9,Du=0.01,Dv=1。平衡(1,0.9)のまわりで3初期値と12/24/48セル、一定の非周期境界を使います。

**編集上の補足**

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

### 採用した計算法

セル平均のCN拡散と局所陰的中点反応をStrang分割します。独立参照は正規直交sin/cos Galerkin、K12/18,Q96/192と2許容誤差の4列を全初期値で残します。 元のDirichlet K12/18参照は初回の相対資格基準を満たさなかったため、失敗を残し、D境界だけK24/32・Q128/192の4参照を追加します。

$$
u_t=.01\Delta u+.1-u+u^2v,\qquad v_t=\Delta v+.9-u^2v
$$

### 比較・検証

線形モードの連続・離散記号、角の面所有、平衡、物質収支を照合。K/Q/時間許容差感度を別に測り、参照が資格条件を満たさなければ精度・次数を未確定にします。 精度目標には、新しい細参照が同じ絶対・相対基準に合格した場合だけその参照を用います。旧参照の不合格を合格へ読み替えません。

### 確認の限界

短時間の小振幅・固定初期値です。一般的な模様選択、成長後の成熟パターン、原著図の再現は主張しません。有限の参照差を連続体誤差の厳密上界と呼びません。

### 調査した目標：達成16・未達0・未確定1（全17）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 16,
    "unmet": 0,
    "unresolved": 1,
    "total": 17
  },
  "goals": [
    {
      "name": "Schnakenberg/positivity/N-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8880521241619382
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860615561401685
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855372535923153
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.250442438972883e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.944655350128315,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8798143344957898
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8771054043233121
      }
    },
    {
      "name": "Schnakenberg/positivity/N-mixed/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8763952220795853
      }
    },
    {
      "name": "Schnakenberg/space-finest/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.00011769804580841203,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/N-mixed",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9477700373628166,
        "target": 1.6
      }
    },
    {
      "name": "Schnakenberg/time-order",
      "observed": null,
      "outcome": "unresolved",
      "stored": {
        "observed": null,
        "actual": null,
        "target": 1.7
      }
    },
    {
      "name": "Schnakenberg/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.1208580182516432e-07,
        "finest_spatial_discrepancy": 0.00011769804580841203,
        "scope": "Secondorder Richardson indicator,notcertifiederrorbound"
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8862155577223321
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8860670448524426
      }
    },
    {
      "name": "Schnakenberg/positivity/D-mode42/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": 0.8855435379971976
      }
    },
    {
      "name": "Schnakenberg/space-finest/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 8.370124740819662e-05,
        "target": 0.02
      }
    },
    {
      "name": "Schnakenberg/space-order/D-mode42",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9463235349282928,
        "target": 1.6
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "Schnakenberg/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 33,
    "Schnakenberg/positivity/N-mode42/12/minimum": 0.8880521241619382,
    "Schnakenberg/positivity/N-mode42/24/minimum": 0.8860615561401685,
    "Schnakenberg/positivity/N-mode42/48/minimum": 0.8855372535923153,
    "Schnakenberg/space-finest/N-mode42/actual": 8.250442438972883e-05,
    "Schnakenberg/space-order/N-mode42/actual": 1.944655350128315,
    "Schnakenberg/positivity/N-mixed/12/minimum": 0.8798143344957898,
    "Schnakenberg/positivity/N-mixed/24/minimum": 0.8771054043233121,
    "Schnakenberg/positivity/N-mixed/48/minimum": 0.8763952220795853,
    "Schnakenberg/space-finest/N-mixed/actual": 0.00011769804580841203,
    "Schnakenberg/space-order/N-mixed/actual": 1.9477700373628166,
    "Schnakenberg/time-contamination/actual": 1.1208580182516432e-07,
    "Schnakenberg/positivity/D-mode42/12/minimum": 0.8862155577223321,
    "Schnakenberg/positivity/D-mode42/24/minimum": 0.8860670448524426,
    "Schnakenberg/positivity/D-mode42/48/minimum": 0.8855435379971976,
    "Schnakenberg/space-finest/D-mode42/actual": 8.370124740819662e-05,
    "Schnakenberg/space-order/D-mode42/actual": 1.9463235349282928
  },
  "checks": {
    "Schnakenberg/mode/N/1/1/12": true,
    "Schnakenberg/exp/N/1/1/12/0.1": true,
    "Schnakenberg/exp/N/1/1/12/0.5": true,
    "Schnakenberg/exp/N/1/1/12/1.0": true,
    "Schnakenberg/mode/N/1/1/24": true,
    "Schnakenberg/exp/N/1/1/24/0.1": true,
    "Schnakenberg/exp/N/1/1/24/0.5": true,
    "Schnakenberg/exp/N/1/1/24/1.0": true,
    "Schnakenberg/mode/N/1/1/48": true,
    "Schnakenberg/exp/N/1/1/48/0.1": true,
    "Schnakenberg/exp/N/1/1/48/0.5": true,
    "Schnakenberg/exp/N/1/1/48/1.0": true,
    "Schnakenberg/mode/N/4/2/12": true,
    "Schnakenberg/exp/N/4/2/12/0.1": true,
    "Schnakenberg/exp/N/4/2/12/0.5": true,
    "Schnakenberg/exp/N/4/2/12/1.0": true,
    "Schnakenberg/mode/N/4/2/24": true,
    "Schnakenberg/exp/N/4/2/24/0.1": true,
    "Schnakenberg/exp/N/4/2/24/0.5": true,
    "Schnakenberg/exp/N/4/2/24/1.0": true,
    "Schnakenberg/mode/N/4/2/48": true,
    "Schnakenberg/exp/N/4/2/48/0.1": true,
    "Schnakenberg/exp/N/4/2/48/0.5": true,
    "Schnakenberg/exp/N/4/2/48/1.0": true,
    "Schnakenberg/mode/N/3/1/12": true,
    "Schnakenberg/exp/N/3/1/12/0.1": true,
    "Schnakenberg/exp/N/3/1/12/0.5": true,
    "Schnakenberg/exp/N/3/1/12/1.0": true,
    "Schnakenberg/mode/N/3/1/24": true,
    "Schnakenberg/exp/N/3/1/24/0.1": true,
    "Schnakenberg/exp/N/3/1/24/0.5": true,
    "Schnakenberg/exp/N/3/1/24/1.0": true,
    "Schnakenberg/mode/N/3/1/48": true,
    "Schnakenberg/exp/N/3/1/48/0.1": true,
    "Schnakenberg/exp/N/3/1/48/0.5": true,
    "Schnakenberg/exp/N/3/1/48/1.0": true,
    "Schnakenberg/mode/D/1/1/12": true,
    "Schnakenberg/exp/D/1/1/12/0.1": true,
    "Schnakenberg/exp/D/1/1/12/0.5": true,
    "Schnakenberg/exp/D/1/1/12/1.0": true,
    "Schnakenberg/mode/D/1/1/24": true,
    "Schnakenberg/exp/D/1/1/24/0.1": true,
    "Schnakenberg/exp/D/1/1/24/0.5": true,
    "Schnakenberg/exp/D/1/1/24/1.0": true,
    "Schnakenberg/mode/D/1/1/48": true,
    "Schnakenberg/exp/D/1/1/48/0.1": true,
    "Schnakenberg/exp/D/1/1/48/0.5": true,
    "Schnakenberg/exp/D/1/1/48/1.0": true,
    "Schnakenberg/mode/D/4/2/12": true,
    "Schnakenberg/exp/D/4/2/12/0.1": true,
    "Schnakenberg/exp/D/4/2/12/0.5": true,
    "Schnakenberg/exp/D/4/2/12/1.0": true,
    "Schnakenberg/mode/D/4/2/24": true,
    "Schnakenberg/exp/D/4/2/24/0.1": true,
    "Schnakenberg/exp/D/4/2/24/0.5": true,
    "Schnakenberg/exp/D/4/2/24/1.0": true,
    "Schnakenberg/mode/D/4/2/48": true,
    "Schnakenberg/exp/D/4/2/48/0.1": true,
    "Schnakenberg/exp/D/4/2/48/0.5": true,
    "Schnakenberg/exp/D/4/2/48/1.0": true,
    "Schnakenberg/mode/D/3/1/12": true,
    "Schnakenberg/exp/D/3/1/12/0.1": true,
    "Schnakenberg/exp/D/3/1/12/0.5": true,
    "Schnakenberg/exp/D/3/1/12/1.0": true,
    "Schnakenberg/mode/D/3/1/24": true,
    "Schnakenberg/exp/D/3/1/24/0.1": true,
    "Schnakenberg/exp/D/3/1/24/0.5": true,
    "Schnakenberg/exp/D/3/1/24/1.0": true,
    "Schnakenberg/mode/D/3/1/48": true,
    "Schnakenberg/exp/D/3/1/48/0.1": true,
    "Schnakenberg/exp/D/3/1/48/0.5": true,
    "Schnakenberg/exp/D/3/1/48/1.0": true,
    "Schnakenberg/equilibrium-face-zero": true,
    "Schnakenberg/constant-equilibrium/N": true,
    "Schnakenberg/constant-equilibrium/D": true,
    "Schnakenberg/wrong-boundary-control": true,
    "Schnakenberg/corner-doublecount-control": true,
    "Schnakenberg/linear-action-count": true,
    "Schnakenberg/ledger/N-mode42/12": true,
    "Schnakenberg/ledger/N-mode42/24": true,
    "Schnakenberg/ledger/N-mode42/48": true,
    "Schnakenberg/reference/N-mode42": true,
    "Schnakenberg/ledger/N-mixed/12": true,
    "Schnakenberg/ledger/N-mixed/24": true,
    "Schnakenberg/ledger/N-mixed/48": true,
    "Schnakenberg/reference/N-mixed": true,
    "Schnakenberg/ledger/D-mode42/12": true,
    "Schnakenberg/ledger/D-mode42/24": true,
    "Schnakenberg/ledger/D-mode42/48": true,
    "Schnakenberg/reference/D-mode42": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-2d-boundary-modes/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/schnakenberg-2d-boundary-modes-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Schnakenberg(1979), Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=selected-primary-or-bibliographic-see-provenance
source-reading.jsonに実際の読取範囲と未読部分を記録。原著の全式・全図の再現とは主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Keller–Segel：連成流束の製造解

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

**使用手法**

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) (`rk45`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-algorithm)

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

- [Keller–Segel走化性](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja) (`bio-keller-segel`)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

- [外力・移流付きKeller–Segel製造問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja) (`forced-keller-segel-model`)

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。


**問題の図**

![Keller–Segel：連成流束の製造解：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja) (`keller-segel-forced-flux`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-validation)

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

- [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-keller-segel-forced-flux-ja) (`keller-segel-forced-flux`; 同じ問題の参照 · 製造解)

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。
### 前提・単位・境界

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

**編集上の補足**

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

### 採用した計算法

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

### 比較・検証

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

### 確認の限界

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

### 調査した目標：達成9・未達0・未確定0（全9）

必須の検証合格と元の調査目標の達成は別です。達成・未達は保存された比較結果を示し、統計的な認定ではありません。未確定と別の不確かさ区分を保持し、nullをfalseや0に置き換えません。

[元の保存結果 / JSON](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

<details><summary>全目標の記録を読む</summary>

```json
{
  "schema_version": 1,
  "counts": {
    "met": 9,
    "unmet": 0,
    "unresolved": 0,
    "total": 9
  },
  "goals": [
    {
      "name": "KS/minimum/12",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9022638544007324,
          0.9527970664018593
        ]
      }
    },
    {
      "name": "KS/minimum/24",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9005698543736446,
          0.9507102465265501
        ]
      }
    },
    {
      "name": "KS/minimum/48",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "minimum": [
          0.9001427078852056,
          0.9501782550064043
        ]
      }
    },
    {
      "name": "KS/time-order",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 3.0037445404571113,
        "target": 2.5
      }
    },
    {
      "name": "KS/space-finest/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 0.0001221189660198796,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/0",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.9965225132866062,
        "target": 1.7
      }
    },
    {
      "name": "KS/space-finest/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 2.9817290057465584e-05,
        "target": 0.002
      }
    },
    {
      "name": "KS/space-order/1",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.988907316937278,
        "target": 1.7
      }
    },
    {
      "name": "KS/time-contamination",
      "observed": true,
      "outcome": "met",
      "stored": {
        "observed": true,
        "actual": 1.893596390800667e-12,
        "finest_spatial_error": 0.0001221189660198796
      }
    }
  ],
  "classification_basis": "stored observed comparison; separate uncertainty classifications retained",
  "source": {
    "collection": "study_goals",
    "json_pointer": "/study_goals",
    "prefix": "KS/",
    "result_sha256": "090c187f89db9d05a2eb437eaf5e73b2dcf1e7600ef0163efd94bae4119cb6eb",
    "acceptance_sha256": "b2f1727f9f4e70c139af7d38c218608b369625ab8f5896d762b060f88432a117",
    "result_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json",
    "acceptance_url": "https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/acceptance.json"
  }
}
```

</details>

### 保存実測値と判定

```json
{
  "metrics": {
    "fixed_records": 10,
    "KS/time-order/actual": 3.0037445404571113,
    "KS/space-finest/0/actual": 0.0001221189660198796,
    "KS/space-order/0/actual": 1.9965225132866062,
    "KS/space-finest/1/actual": 2.9817290057465584e-05,
    "KS/space-order/1/actual": 1.988907316937278,
    "KS/time-contamination/actual": 1.893596390800667e-12
  },
  "checks": {
    "KS/source_point_pairs36": true,
    "KS/wholegrid_RHS_vectorpairs96": true,
    "KS/divergence_free_faces": true,
    "KS/independent_velocity": true,
    "KS/wrong_chi_detected": true,
    "KS/omitted_coupling_detected": true,
    "KS/stale_source_time_detected": true,
    "KS/duplicated_external_face_detected": true,
    "KS/massledger/12": true,
    "KS/massledger/24": true,
    "KS/massledger/48": true,
    "KS/reference": true,
    "KS/constant-control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/index.json

![精度・参照・統計の実測値と未達目標を分けて表示します。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux-diagnostics.png)

精度・参照・統計の実測値と未達目標を分けて表示します。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Atlas authored Keller–Segel manufactured fields, forcing and finite-volume balance controls (2026-11-25). https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py; review_level=authored-formulas-and-actually-executed-component-checks
本アトラス独自の製造解・外力・面流束の導出と実装です。保存された成分検査・独立なスカラー面/RHS参照・セル平均照合の範囲に限ります。原著論文の読了や元の無外力問題の再現を主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
