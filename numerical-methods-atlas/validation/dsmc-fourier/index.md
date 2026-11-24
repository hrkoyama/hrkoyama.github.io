# 硬球DSMCの有限Kn Fourier熱伝導

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-algorithm)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [剛体球Boltzmann輸送と壁・流入出](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hard-sphere-boltzmann-ja) (`hard-sphere-boltzmann`)

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。


**問題の図**

![硬球DSMCの有限Kn Fourier熱伝導：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja) (`dsmc-fourier`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=ja#dsmc-fourier-ja-validation)

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

- [硬球DSMCの有限Kn Fourier熱伝導](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-fourier-ja) (`dsmc-fourier`; 同じ問題の参照 · 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。
## 前提・単位・境界

1次元位置・3次元速度、H=2、Kn0=.5、完全拡散壁。静止壁、左温度1・右2。16セル、N=1024、dt=.02、burn20/sample40、4seed。

**編集上の補足**

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

## 採用した計算法

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

## 比較・検証

各群18pytestを事前固定。新しい固定計算は群で14本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。

## 確認の限界

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。Kn=.5で連続体の直線・no-slip分布を厳密解としません。図は保存した粒子位相空間であり、2D物理流れではありません。

## 保存実測値と判定

```json
{
  "metrics": {
    "profile_comparison": {
      "4": {
        "error": 0.0046350333567375225,
        "combined_3se": 0.01986770882165603,
        "primary_3se": 0.018610142257145208,
        "reference_3se": 0.006956181351210389
      },
      "0": {
        "error": 0.006206560932103681,
        "combined_3se": 0.014725327832097481,
        "primary_3se": 0.012851725754092255,
        "reference_3se": 0.007188075187722132
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "4": 0.06340714719603799,
        "0": 0.03983352063527729
      }
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "4": 0.02668632575679284,
        "0": 0.013283289135740131
      },
      "double_particles": {
        "4": 0.012688404465360077,
        "0": 0.009002412684556585
      },
      "half_dt": {
        "4": 0.008201282077196198,
        "0": 0.010766498591131742
      }
    },
    "t95_multiplier_df3": 3.182446305284263,
    "flux": {
      "bulk_mean": -0.5644605772254152,
      "bulk_se": 0.0023868795505760263,
      "reference_mean": -0.5756964840332293,
      "reference_se": 0.005479198503847574,
      "wall_mean": -0.566381423471522,
      "wall_se": 0.00224129249203519,
      "wall_minus_bulk": -0.00192084624610675,
      "wall_minus_bulk_se": 0.00029712049609058333
    }
  },
  "checks": {
    "dsmc-fourier-base-361101/finite": true,
    "dsmc-fourier-base-361101/boundary budget": true,
    "dsmc-fourier-base-361101/physical collisions": true,
    "dsmc-fourier-base-361101/collision probability": true,
    "dsmc-fourier-base-361101/maxwell time resolution": true,
    "dsmc-fourier-base-361101/mean free path resolution": true,
    "dsmc-fourier-base-361102/finite": true,
    "dsmc-fourier-base-361102/boundary budget": true,
    "dsmc-fourier-base-361102/physical collisions": true,
    "dsmc-fourier-base-361102/collision probability": true,
    "dsmc-fourier-base-361102/maxwell time resolution": true,
    "dsmc-fourier-base-361102/mean free path resolution": true,
    "dsmc-fourier-base-361103/finite": true,
    "dsmc-fourier-base-361103/boundary budget": true,
    "dsmc-fourier-base-361103/physical collisions": true,
    "dsmc-fourier-base-361103/collision probability": true,
    "dsmc-fourier-base-361103/maxwell time resolution": true,
    "dsmc-fourier-base-361103/mean free path resolution": true,
    "dsmc-fourier-base-361104/finite": true,
    "dsmc-fourier-base-361104/boundary budget": true,
    "dsmc-fourier-base-361104/physical collisions": true,
    "dsmc-fourier-base-361104/collision probability": true,
    "dsmc-fourier-base-361104/maxwell time resolution": true,
    "dsmc-fourier-base-361104/mean free path resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/finite": true,
    "dsmc-fourier-fixed_weight_mesh-361101/boundary budget": true,
    "dsmc-fourier-fixed_weight_mesh-361101/physical collisions": true,
    "dsmc-fourier-fixed_weight_mesh-361101/collision probability": true,
    "dsmc-fourier-fixed_weight_mesh-361101/maxwell time resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/mean free path resolution": true,
    "dsmc-fourier-double_particles-361101/finite": true,
    "dsmc-fourier-double_particles-361101/boundary budget": true,
    "dsmc-fourier-double_particles-361101/physical collisions": true,
    "dsmc-fourier-double_particles-361101/collision probability": true,
    "dsmc-fourier-double_particles-361101/maxwell time resolution": true,
    "dsmc-fourier-double_particles-361101/mean free path resolution": true,
    "dsmc-fourier-half_dt-361101/finite": true,
    "dsmc-fourier-half_dt-361101/boundary budget": true,
    "dsmc-fourier-half_dt-361101/physical collisions": true,
    "dsmc-fourier-half_dt-361101/collision probability": true,
    "dsmc-fourier-half_dt-361101/maxwell time resolution": true,
    "dsmc-fourier-half_dt-361101/mean free path resolution": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "stationarity/4": true,
    "stationarity/0": true,
    "bulk molecular flux agreement": true,
    "bulk molecular flux precision": true,
    "wall versus bulk molecular flux": true,
    "wall molecular flux precision": true,
    "half step sensitivity/4": true,
    "half step sensitivity/0": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/index.json

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields [accessed 2026-11-23]. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
公式固定版のHS衝突率・境界・分子モーメントを選択確認し、独立36計算と87判定を実施。原著書籍全読や全コード監査は主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Hard-sphere DSMC finite-Kn Fourier heat conduction

Evolve physical-time hard-sphere collisions and molecular streaming; compare actual moments with qualified independent SPARTA fields.

**Methods used**

- [DSMC and kinetic transport](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=en) (`dsmc`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-algorithm)

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

- [Hard-sphere Boltzmann transport,walls and reservoirs](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#hard-sphere-boltzmann-en) (`hard-sphere-boltzmann`)

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.


**Problem figure**

![Hard-sphere DSMC finite-Kn Fourier heat conduction: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Hard-sphere DSMC finite-Kn Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en) (`dsmc-fourier`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-fourier/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/?lang=en#dsmc-fourier-en-validation)

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

- [Finite-Kn hard-sphere Fourier heat conduction](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-dsmc-fourier-en) (`dsmc-fourier`; Same-problem reference · Finite-grid numerical reference)

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.
## Assumptions, units and boundaries

{"kind":"wall","cells":16,"length":2,"weight":0.001953125,"dt":0.02,"burn_in":20,"sample_time":40,"blocks":5,"bins":8,"sample_every":10,"hist_velocity":[-6,6],"temperatures":[1,2],"speeds":[0,0]} Four independent seeds; primary fixed-weight mesh,particle-weight,and half-step companions each retain seed1.

**Editorial clarification**

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

## Adopted numerical method

Disjoint cell-local random pairs with even/odd finite-N physical-time sigma*g acceptance,energy-based safe majorant and predeclared bounded subcycling; no probability caps. Exact flight-to-wall and flux-conditioned diffuse/reservoir velocities with remaining flight time.

$$
\partial_t f+v_x\partial_x f=Q_{\mathrm{HS}}(f,f),\quad \sigma=\pi d^2=1/\sqrt{2}
$$

$$
P_{ij}=n\langle c_i c_j\rangle,\quad q_x=\frac{n}{2}\langle c_x|\mathbf c|^2\rangle,\quad\mathbf c=\mathbf v-\mathbf u
$$

$$
p_{ij}=a_N W\sigma g_{ij}\Delta t/V,\quad a_N=\begin{cases}N-1&N\text{ even}\\N&N\text{ odd}\end{cases}
$$

$$
g_{ij}\le\sqrt{2\sum_i|\mathbf v_i-\mathbf v_{cm}|^2}
$$

## References and validation

Predeclare18pytest per group and14new fixed primary runs. Separate boundary-inclusive budgets,local lambda/collision-time diagnostics,reference error,whole-seed precision and block stationarity. Reference36runs/87qualifiers already passed; primary results remain pending until the frozen run.

## Limits

Finite-particle finite-grid independent stochastic reference,empirically qualified; no rigorous continuum bound,linear-response/general-DSMC/VHS or spatial-order claim. AtKn.5,continuum straight/no-slip profiles are not exact. Saved phase space is not a2D physical flow.

## Stored measurements and decisions

```json
{
  "metrics": {
    "profile_comparison": {
      "4": {
        "error": 0.0046350333567375225,
        "combined_3se": 0.01986770882165603,
        "primary_3se": 0.018610142257145208,
        "reference_3se": 0.006956181351210389
      },
      "0": {
        "error": 0.006206560932103681,
        "combined_3se": 0.014725327832097481,
        "primary_3se": 0.012851725754092255,
        "reference_3se": 0.007188075187722132
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "4": 0.06340714719603799,
        "0": 0.03983352063527729
      }
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "4": 0.02668632575679284,
        "0": 0.013283289135740131
      },
      "double_particles": {
        "4": 0.012688404465360077,
        "0": 0.009002412684556585
      },
      "half_dt": {
        "4": 0.008201282077196198,
        "0": 0.010766498591131742
      }
    },
    "t95_multiplier_df3": 3.182446305284263,
    "flux": {
      "bulk_mean": -0.5644605772254152,
      "bulk_se": 0.0023868795505760263,
      "reference_mean": -0.5756964840332293,
      "reference_se": 0.005479198503847574,
      "wall_mean": -0.566381423471522,
      "wall_se": 0.00224129249203519,
      "wall_minus_bulk": -0.00192084624610675,
      "wall_minus_bulk_se": 0.00029712049609058333
    }
  },
  "checks": {
    "dsmc-fourier-base-361101/finite": true,
    "dsmc-fourier-base-361101/boundary budget": true,
    "dsmc-fourier-base-361101/physical collisions": true,
    "dsmc-fourier-base-361101/collision probability": true,
    "dsmc-fourier-base-361101/maxwell time resolution": true,
    "dsmc-fourier-base-361101/mean free path resolution": true,
    "dsmc-fourier-base-361102/finite": true,
    "dsmc-fourier-base-361102/boundary budget": true,
    "dsmc-fourier-base-361102/physical collisions": true,
    "dsmc-fourier-base-361102/collision probability": true,
    "dsmc-fourier-base-361102/maxwell time resolution": true,
    "dsmc-fourier-base-361102/mean free path resolution": true,
    "dsmc-fourier-base-361103/finite": true,
    "dsmc-fourier-base-361103/boundary budget": true,
    "dsmc-fourier-base-361103/physical collisions": true,
    "dsmc-fourier-base-361103/collision probability": true,
    "dsmc-fourier-base-361103/maxwell time resolution": true,
    "dsmc-fourier-base-361103/mean free path resolution": true,
    "dsmc-fourier-base-361104/finite": true,
    "dsmc-fourier-base-361104/boundary budget": true,
    "dsmc-fourier-base-361104/physical collisions": true,
    "dsmc-fourier-base-361104/collision probability": true,
    "dsmc-fourier-base-361104/maxwell time resolution": true,
    "dsmc-fourier-base-361104/mean free path resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/finite": true,
    "dsmc-fourier-fixed_weight_mesh-361101/boundary budget": true,
    "dsmc-fourier-fixed_weight_mesh-361101/physical collisions": true,
    "dsmc-fourier-fixed_weight_mesh-361101/collision probability": true,
    "dsmc-fourier-fixed_weight_mesh-361101/maxwell time resolution": true,
    "dsmc-fourier-fixed_weight_mesh-361101/mean free path resolution": true,
    "dsmc-fourier-double_particles-361101/finite": true,
    "dsmc-fourier-double_particles-361101/boundary budget": true,
    "dsmc-fourier-double_particles-361101/physical collisions": true,
    "dsmc-fourier-double_particles-361101/collision probability": true,
    "dsmc-fourier-double_particles-361101/maxwell time resolution": true,
    "dsmc-fourier-double_particles-361101/mean free path resolution": true,
    "dsmc-fourier-half_dt-361101/finite": true,
    "dsmc-fourier-half_dt-361101/boundary budget": true,
    "dsmc-fourier-half_dt-361101/physical collisions": true,
    "dsmc-fourier-half_dt-361101/collision probability": true,
    "dsmc-fourier-half_dt-361101/maxwell time resolution": true,
    "dsmc-fourier-half_dt-361101/mean free path resolution": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "stationarity/4": true,
    "stationarity/0": true,
    "bulk molecular flux agreement": true,
    "bulk molecular flux precision": true,
    "wall versus bulk molecular flux": true,
    "wall molecular flux precision": true,
    "half step sensitivity/4": true,
    "half step sensitivity/0": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-fourier/index.json

![Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/dsmc-fourier-preview.png)

Actual saved particle position-velocity histograms; phase space of1D position and molecular velocity,not2D physical flow.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/atlas-dsmc-wall-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/dsmc-wall/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields [accessed 2026-11-23]. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
Read selected official HS rate,boundary and moment definitions; execute36independent runs and87qualifiers. No full-original-book or whole-source audit claim.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
