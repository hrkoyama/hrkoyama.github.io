# 剛体球DSMCのMach2平面衝撃波

流入出を持つ1D空間・3D速度の衝撃波で、RH遠方状態と内部の独立な数値参照を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 硬球DSMCのMach2平面衝撃波

物理時間の硬球衝突と実際の分子輸送を計算し、独立SPARTAの資格確認済みモーメント場と比較します。

**使用手法**

- [DSMC・運動論輸送](https://hrkoyama.github.io/numerical-methods-atlas/methods/dsmc/?lang=ja) (`dsmc`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-algorithm)

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。 2026-11-24版は固定reservoir係数、同一vで既評価の逆CDF残差、keep→left→right順の連結の再利用と、範囲確認した整数sort keyだけの可逆uint8圧縮を行う性能修正版です。元の乱数呼出順・安定sortの同値粒子順位・衝突対・科学設定を保ち、前3点の成分資格163項目に加え、sort keyを含む別348項目でbit/RNG一致を確認しました。いずれも成分検査であり、新mainと全保存科学値の一致はまだ未判定です。

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

1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。


**問題の図**

![硬球DSMCのMach2平面衝撃波：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja) (`dsmc-planar-shock`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/dsmc-planar-shock/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/?lang=ja#dsmc-planar-shock-ja-validation)

各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 Nov23保存成功と全15計算・129判定の厳密比較を行う新mainは、本契約の時点で未実行です。20pytestと全mainの外部共有上限120秒、全診断・NPZ・CSVを維持します。

- [硬球DSMCのMach2平面衝撃波](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-dsmc-planar-shock-ja) (`dsmc-planar-shock`; 同じ問題の参照 · 有限格子の数値参照)

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。
### 前提・単位・境界

1次元位置・3次元速度、単原子硬球。Mach2、区間[0,16]、RHの開境界reservoir。192セル、粒子重み1/192、dt=.01、burn20/sample20、12seed。

**編集上の補足**

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

### 採用した計算法

セル内の非重複ランダム対へ、偶数・奇数粒子数を区別した物理時間のσg衝突確率を適用。エネルギーによる安全上界で事前にsubcycle数を定め、確率clipはしません。壁・流入はflux重み付き分布と実際の残り飛行時間を用います。 開境界のmacro粒子到着数は平均を保つfloor(平均)+Bernoulli(小数部)で分散を下げます。Poisson数揺らぎや熱揺らぎの再現は主張しません。 既存4seedを残して次の8連番seedを追加します。一様順列と安定整数sortは対選択法則を保ちますが、乱数消費と軌道のbit一致は主張しません。 2026-11-24版は固定reservoir係数、同一vで既評価の逆CDF残差、keep→left→right順の連結の再利用と、範囲確認した整数sort keyだけの可逆uint8圧縮を行う性能修正版です。元の乱数呼出順・安定sortの同値粒子順位・衝突対・科学設定を保ち、前3点の成分資格163項目に加え、sort keyを含む別348項目でbit/RNG一致を確認しました。いずれも成分検査であり、新mainと全保存科学値の一致はまだ未判定です。

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

### 比較・検証

各群20pytestを事前固定。新しい固定計算は15本。境界込みの質量・運動量・エネルギー、局所λ/衝突時間、独立参照への誤差とseed精度、時間block定常性を別に判定します。 群の判定は既存81項目を保持し、新8計算の48項目を追加した129項目です。primary t95はdf11、独立参照4seedはdf3です。 Nov23保存成功と全15計算・129判定の厳密比較を行う新mainは、本契約の時点で未実行です。20pytestと全mainの外部共有上限120秒、全診断・NPZ・CSVを維持します。

### 確認の限界

有限粒子・有限格子の独立確率参照との限定比較です。線形応答、連続体極限、全DSMC、VHS一般、空間次数を認証しません。RHは遠方状態・流束だけの参照で、内部構造の厳密解ではありません。図は保存した粒子位相空間であり、2D物理流れではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "profile_comparison": {
      "0": {
        "error": 0.009874127472267416,
        "combined_3se": 0.04946478705678961,
        "primary_3se": 0.03145643911579176,
        "reference_3se": 0.038174043494605424
      },
      "1": {
        "error": 0.006192836083404945,
        "combined_3se": 0.04640157562693747,
        "primary_3se": 0.03069818659770613,
        "reference_3se": 0.03479551063391386
      },
      "4": {
        "error": 0.008787013676147464,
        "combined_3se": 0.04976037231809162,
        "primary_3se": 0.035488922267584475,
        "reference_3se": 0.03488023866776783
      },
      "5": {
        "error": 0.008767734324833546,
        "combined_3se": 0.04646188409882251,
        "primary_3se": 0.03146941765264155,
        "reference_3se": 0.034181609479602165
      }
    },
    "stationarity": {
      "profile_equivalence": {
        "0": 0.051237907861461617,
        "1": 0.042550439680933805,
        "4": 0.052530861424159206,
        "5": 0.04623394154519991
      },
      "centroid_blocks": [
        [
          8.215335648148148,
          8.242578124999998,
          8.37534722222222,
          8.264756944444443,
          8.092187500000001
        ],
        [
          7.8806278935185174,
          7.732971643518519,
          7.8655381944444445,
          7.8228009259259235,
          7.707146990740742
        ],
        [
          8.088237847222222,
          8.194574652777776,
          8.386284722222221,
          8.335546875,
          8.221412037037037
        ],
        [
          7.609114583333332,
          7.680005787037035,
          7.577416087962962,
          7.347829861111112,
          7.23622685185185
        ],
        [
          7.620153356481483,
          7.693475115740742,
          7.670992476851854,
          7.572149884259257,
          7.589872685185185
        ],
        [
          8.473075810185184,
          8.567361111111111,
          8.567766203703703,
          8.53627025462963,
          8.390943287037034
        ],
        [
          8.005295138888886,
          8.019574652777777,
          7.905338541666666,
          7.990509259259259,
          7.868880208333332
        ],
        [
          8.190827546296296,
          8.03587962962963,
          8.154369212962964,
          8.220095486111111,
          8.337774884259257
        ],
        [
          8.411805555555553,
          8.436414930555557,
          8.455353009259259,
          8.48381076388889,
          8.650708912037034
        ],
        [
          8.18292824074074,
          8.153153935185184,
          8.265668402777775,
          8.268706597222222,
          8.303443287037037
        ],
        [
          7.841840277777777,
          7.737731481481482,
          7.718084490740742,
          7.826649305555556,
          7.872829861111111
        ],
        [
          7.868981481481481,
          7.905135995370369,
          7.91607349537037,
          8.006915509259258,
          7.7184895833333345
        ]
      ],
      "centroid_drift_bound": 0.1299701694340089
    },
    "sensitivities": {
      "fixed_weight_mesh": {
        "0": 0.04919268505889352,
        "1": 0.052838812527762305,
        "4": 0.0623901833211318,
        "5": 0.05359743514641371
      },
      "double_particles": {
        "0": 0.06216354691255698,
        "1": 0.06013078079263267,
        "4": 0.06006763400021631,
        "5": 0.06186520180345716
      },
      "half_dt": {
        "0": 0.03506052657485229,
        "1": 0.034593071784548436,
        "4": 0.0371459702067488,
        "5": 0.03752041004610139
      }
    },
    "primary_independent_seeds": 12,
    "primary_t95_degrees_of_freedom": 11,
    "primary_t95_multiplier": 2.200985160082949,
    "reference_independent_seeds": 4,
    "reference_t95_degrees_of_freedom": 3,
    "reference_t95_multiplier": 3.182446305284263,
    "far_states": {
      "upstream_n": {
        "relative_error": 0.0027311197916668473,
        "relative_3se": 0.004734773179813632
      },
      "upstream_ux": {
        "relative_error": 0.00226178222693619,
        "relative_3se": 0.004417322646908852
      },
      "upstream_T": {
        "relative_error": 0.00856692867855613,
        "relative_3se": 0.00919577401692969
      },
      "downstream_n": {
        "relative_error": 0.0007166883680555791,
        "relative_3se": 0.008778472486905992
      },
      "downstream_ux": {
        "relative_error": 0.0006619790814905539,
        "relative_3se": 0.011133999868080233
      },
      "downstream_T": {
        "relative_error": 0.0006120131785834495,
        "relative_3se": 0.0057144250470660685
      },
      "flux_mass": {
        "relative_error": 0.0009975883698689597,
        "relative_3se": 0.0029103940695329165
      },
      "flux_momentum": {
        "relative_error": 0.0013333838218918732,
        "relative_3se": 0.0028882793828942516
      },
      "flux_energy": {
        "relative_error": 0.0009104591488130677,
        "relative_3se": 0.00428618985183569
      }
    }
  },
  "checks": {
    "dsmc-planar-shock-base-371001/finite": true,
    "dsmc-planar-shock-base-371001/boundary budget": true,
    "dsmc-planar-shock-base-371001/physical collisions": true,
    "dsmc-planar-shock-base-371001/collision probability": true,
    "dsmc-planar-shock-base-371001/maxwell time resolution": true,
    "dsmc-planar-shock-base-371001/mean free path resolution": true,
    "dsmc-planar-shock-base-371002/finite": true,
    "dsmc-planar-shock-base-371002/boundary budget": true,
    "dsmc-planar-shock-base-371002/physical collisions": true,
    "dsmc-planar-shock-base-371002/collision probability": true,
    "dsmc-planar-shock-base-371002/maxwell time resolution": true,
    "dsmc-planar-shock-base-371002/mean free path resolution": true,
    "dsmc-planar-shock-base-371003/finite": true,
    "dsmc-planar-shock-base-371003/boundary budget": true,
    "dsmc-planar-shock-base-371003/physical collisions": true,
    "dsmc-planar-shock-base-371003/collision probability": true,
    "dsmc-planar-shock-base-371003/maxwell time resolution": true,
    "dsmc-planar-shock-base-371003/mean free path resolution": true,
    "dsmc-planar-shock-base-371004/finite": true,
    "dsmc-planar-shock-base-371004/boundary budget": true,
    "dsmc-planar-shock-base-371004/physical collisions": true,
    "dsmc-planar-shock-base-371004/collision probability": true,
    "dsmc-planar-shock-base-371004/maxwell time resolution": true,
    "dsmc-planar-shock-base-371004/mean free path resolution": true,
    "dsmc-planar-shock-base-371005/finite": true,
    "dsmc-planar-shock-base-371005/boundary budget": true,
    "dsmc-planar-shock-base-371005/physical collisions": true,
    "dsmc-planar-shock-base-371005/collision probability": true,
    "dsmc-planar-shock-base-371005/maxwell time resolution": true,
    "dsmc-planar-shock-base-371005/mean free path resolution": true,
    "dsmc-planar-shock-base-371006/finite": true,
    "dsmc-planar-shock-base-371006/boundary budget": true,
    "dsmc-planar-shock-base-371006/physical collisions": true,
    "dsmc-planar-shock-base-371006/collision probability": true,
    "dsmc-planar-shock-base-371006/maxwell time resolution": true,
    "dsmc-planar-shock-base-371006/mean free path resolution": true,
    "dsmc-planar-shock-base-371007/finite": true,
    "dsmc-planar-shock-base-371007/boundary budget": true,
    "dsmc-planar-shock-base-371007/physical collisions": true,
    "dsmc-planar-shock-base-371007/collision probability": true,
    "dsmc-planar-shock-base-371007/maxwell time resolution": true,
    "dsmc-planar-shock-base-371007/mean free path resolution": true,
    "dsmc-planar-shock-base-371008/finite": true,
    "dsmc-planar-shock-base-371008/boundary budget": true,
    "dsmc-planar-shock-base-371008/physical collisions": true,
    "dsmc-planar-shock-base-371008/collision probability": true,
    "dsmc-planar-shock-base-371008/maxwell time resolution": true,
    "dsmc-planar-shock-base-371008/mean free path resolution": true,
    "dsmc-planar-shock-base-371009/finite": true,
    "dsmc-planar-shock-base-371009/boundary budget": true,
    "dsmc-planar-shock-base-371009/physical collisions": true,
    "dsmc-planar-shock-base-371009/collision probability": true,
    "dsmc-planar-shock-base-371009/maxwell time resolution": true,
    "dsmc-planar-shock-base-371009/mean free path resolution": true,
    "dsmc-planar-shock-base-371010/finite": true,
    "dsmc-planar-shock-base-371010/boundary budget": true,
    "dsmc-planar-shock-base-371010/physical collisions": true,
    "dsmc-planar-shock-base-371010/collision probability": true,
    "dsmc-planar-shock-base-371010/maxwell time resolution": true,
    "dsmc-planar-shock-base-371010/mean free path resolution": true,
    "dsmc-planar-shock-base-371011/finite": true,
    "dsmc-planar-shock-base-371011/boundary budget": true,
    "dsmc-planar-shock-base-371011/physical collisions": true,
    "dsmc-planar-shock-base-371011/collision probability": true,
    "dsmc-planar-shock-base-371011/maxwell time resolution": true,
    "dsmc-planar-shock-base-371011/mean free path resolution": true,
    "dsmc-planar-shock-base-371012/finite": true,
    "dsmc-planar-shock-base-371012/boundary budget": true,
    "dsmc-planar-shock-base-371012/physical collisions": true,
    "dsmc-planar-shock-base-371012/collision probability": true,
    "dsmc-planar-shock-base-371012/maxwell time resolution": true,
    "dsmc-planar-shock-base-371012/mean free path resolution": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/finite": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/boundary budget": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/physical collisions": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/collision probability": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/maxwell time resolution": true,
    "dsmc-planar-shock-fixed_weight_mesh-371001/mean free path resolution": true,
    "dsmc-planar-shock-double_particles-371001/finite": true,
    "dsmc-planar-shock-double_particles-371001/boundary budget": true,
    "dsmc-planar-shock-double_particles-371001/physical collisions": true,
    "dsmc-planar-shock-double_particles-371001/collision probability": true,
    "dsmc-planar-shock-double_particles-371001/maxwell time resolution": true,
    "dsmc-planar-shock-double_particles-371001/mean free path resolution": true,
    "dsmc-planar-shock-half_dt-371001/finite": true,
    "dsmc-planar-shock-half_dt-371001/boundary budget": true,
    "dsmc-planar-shock-half_dt-371001/physical collisions": true,
    "dsmc-planar-shock-half_dt-371001/collision probability": true,
    "dsmc-planar-shock-half_dt-371001/maxwell time resolution": true,
    "dsmc-planar-shock-half_dt-371001/mean free path resolution": true,
    "profile error/0": true,
    "primary precision/0": true,
    "reference precision/0": true,
    "profile error/1": true,
    "primary precision/1": true,
    "reference precision/1": true,
    "profile error/4": true,
    "primary precision/4": true,
    "reference precision/4": true,
    "profile error/5": true,
    "primary precision/5": true,
    "reference precision/5": true,
    "stationarity/0": true,
    "stationarity/1": true,
    "stationarity/4": true,
    "stationarity/5": true,
    "centroid stationarity": true,
    "RH far or full flux/upstream_n": true,
    "RH precision/upstream_n": true,
    "RH far or full flux/upstream_ux": true,
    "RH precision/upstream_ux": true,
    "RH far or full flux/upstream_T": true,
    "RH precision/upstream_T": true,
    "RH far or full flux/downstream_n": true,
    "RH precision/downstream_n": true,
    "RH far or full flux/downstream_ux": true,
    "RH precision/downstream_ux": true,
    "RH far or full flux/downstream_T": true,
    "RH precision/downstream_T": true,
    "RH far or full flux/flux_mass": true,
    "RH precision/flux_mass": true,
    "RH far or full flux/flux_momentum": true,
    "RH precision/flux_momentum": true,
    "RH far or full flux/flux_energy": true,
    "RH precision/flux_energy": true,
    "half step sensitivity/0": true,
    "half step sensitivity/1": true,
    "half step sensitivity/4": true,
    "half step sensitivity/5": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/dsmc-planar-shock/index.json

![保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/dsmc-planar-shock-preview.png)

保存した実粒子の位置–速度ヒストグラム。1次元位置と分子速度の位相空間であり、2D物理流れではありません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/atlas-dsmc-shock-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/dsmc-shock/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Sandia SPARTA developers (2026). SPARTA, pinned official HS collision/boundary implementation and independently evolved fields [accessed 2026-11-23]. https://github.com/sparta/sparta/tree/1ae18f3646e7c89f86e965f0f3c13fcc5f32e399; review_level=primary-source-selected-functions-and-actual-reference-execution
公式固定版のHS衝突率・境界・分子モーメントを選択確認し、独立36計算と87判定を実施。原著書籍全読や全コード監査は主張しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
