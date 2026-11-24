# 時間離散・fold近傍・分布係数の随伴

離散写像の接線と随伴を比較し、参照精度・要求残差・保存bufferと再計算を分けます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 時間離散拡散の随伴とcheckpoint

後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) (`backward-euler`)
- [Thomas法／三重対角消去](https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja) (`thomas`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-algorithm)

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

- [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja) (`heat`)

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。


**問題の図**

![時間離散拡散の随伴とcheckpoint：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[時間離散拡散の随伴とcheckpoint](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja) (`diffusion-discrete-adjoint`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/diffusion-discrete-adjoint/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja#diffusion-discrete-adjoint-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

- [後退Euler離散モードと時間厳密半離散拡散の参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-diffusion-discrete-adjoint-ja) (`diffusion-discrete-adjoint`; 同じ問題の参照 · 解析参照)

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。
### 前提・単位・境界

無次元x∈[0,1]、u(0,t)=u(1,t)=0。内点7/15、時間step64/128/256、T=.1。κ=.1、θ=.2。目的関数のh重みを含む座標転置です。

**編集上の補足**

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

### 採用した計算法

ThomasでB u次=u現在+dt θbを解き、Bの転置を逆順に解きます。16stepごとにcheckpointを保存し、1blockを同じ順で再計算します。full配列を保存・解放した後で別の所有期間を測ります。

$$
B=I+\Delta t\,\kappa A_h,\quad Bu_{k+1}=u_k+\Delta t\,\theta b
$$

$$
p_N=h(u_N-d),\quad z_k=B^{-T}p_{k+1},\quad p_k=z_k
$$

$$
J_\kappa=0.01\kappa-\Delta t\sum_k z_k^TA_hu_{k+1},\quad J_\theta=0.02\theta+\Delta t\sum_kz_k^Tb
$$

### 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。

### 確認の限界

固定stepの離散随伴でありCVODESや最適checkpoint法ではありません。40nは状態・随伴・RHS/solve scratchの一意な所有要素数です。静的因子・model配列は別表示し総所有byteへ含めます。検証/NPZ組立は測定後で、RSSではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "time_ratios": [
      {
        "n": 7,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.5007714700172587,
        "denominator": 0.00011295826203078933
      },
      {
        "n": 7,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.5003862639676856,
        "denominator": 5.6566274927753076e-05
      },
      {
        "n": 15,
        "coarse": 64,
        "fine": 128,
        "ratio": 0.500801018633583,
        "denominator": 0.00011971557684064543
      },
      {
        "n": 15,
        "coarse": 128,
        "fine": 256,
        "ratio": 0.500401075710245,
        "denominator": 5.99536828281022e-05
      }
    ],
    "principal_records": 6,
    "FD_forward_evolutions": 18,
    "ownership_scope": "Unique explicit scientific arrays; validation loaded after the separate ownership windows; serialization internals are not process RSS."
  },
  "checks": {
    "n7-N64-finite-boundary": true,
    "n7-N64-state-modal": true,
    "n7-N64-adjoint-modal": true,
    "n7-N64-tangent-modal": true,
    "n7-N64-adjoint-tangent": true,
    "n7-N64-replay-state": true,
    "n7-N64-replay-gradient": true,
    "n7-N64-exact-work": true,
    "n7-N128-finite-boundary": true,
    "n7-N128-state-modal": true,
    "n7-N128-adjoint-modal": true,
    "n7-N128-tangent-modal": true,
    "n7-N128-adjoint-tangent": true,
    "n7-N128-replay-state": true,
    "n7-N128-replay-gradient": true,
    "n7-N128-exact-work": true,
    "n7-N256-finite-boundary": true,
    "n7-N256-state-modal": true,
    "n7-N256-adjoint-modal": true,
    "n7-N256-tangent-modal": true,
    "n7-N256-adjoint-tangent": true,
    "n7-N256-replay-state": true,
    "n7-N256-replay-gradient": true,
    "n7-N256-exact-work": true,
    "n7-time-ratio-64-128": true,
    "n7-time-ratio-128-256": true,
    "n7-N256-storage": true,
    "n15-N64-finite-boundary": true,
    "n15-N64-state-modal": true,
    "n15-N64-adjoint-modal": true,
    "n15-N64-tangent-modal": true,
    "n15-N64-adjoint-tangent": true,
    "n15-N64-replay-state": true,
    "n15-N64-replay-gradient": true,
    "n15-N64-exact-work": true,
    "n15-N128-finite-boundary": true,
    "n15-N128-state-modal": true,
    "n15-N128-adjoint-modal": true,
    "n15-N128-tangent-modal": true,
    "n15-N128-adjoint-tangent": true,
    "n15-N128-replay-state": true,
    "n15-N128-replay-gradient": true,
    "n15-N128-exact-work": true,
    "n15-N256-finite-boundary": true,
    "n15-N256-state-modal": true,
    "n15-N256-adjoint-modal": true,
    "n15-N256-tangent-modal": true,
    "n15-N256-adjoint-tangent": true,
    "n15-N256-replay-state": true,
    "n15-N256-replay-gradient": true,
    "n15-N256-exact-work": true,
    "n15-time-ratio-64-128": true,
    "n15-time-ratio-128-256": true,
    "n15-N256-storage": true,
    "FD-direction0": true,
    "FD-direction1": true,
    "FD-direction2": true,
    "FD-all-finite": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/index.json

![時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/diffusion-discrete-adjoint-preview.png)

時間離散拡散の随伴とcheckpoint。実際の保存数値データの縮小図で、1次元問題です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 離散fold近傍のBratu感度

離散Bratuのfoldへ近づく6固定点で、状態誤差と線形許容差の影響を分け、独立shooting勾配と照合します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-algorithm)

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。


**問題の図**

![離散fold近傍のBratu感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[離散fold近傍のBratu感度](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja) (`bratu-fold-sensitivity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-fold-sensitivity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/?lang=ja#bratu-fold-sensitivity-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

- [離散fold近傍のBratu shooting・接線・随伴参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-fold-sensitivity-ja) (`bratu-fold-sensitivity`; 同じ問題の参照 · 有限格子の数値参照)

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
### 前提・単位・境界

内点31/63、離散fold anchorとの差.1/.01/.001。各状態は零初期値からの下枝。λの文字列を一度binary floatへ変換し、参照はその正確な値をDecimalで評価します。

**編集上の補足**

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

### 採用した計算法

解析Jv、Poisson-Thomas右前処理、固定GMRES本体で接線と随伴を解きます。全rtol・最終候補・true residual・終了状態・丸めscaleを保存します。shootingと別の高精度Thomas-Newtonで離散参照を資格します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G(u,\lambda)=A_hu-\lambda e^u=0,\quad Js=e^u,\quad J^Tp=hu
$$

$$
\mathcal J=\tfrac12h\sum_i u_i^2+0.025\lambda^2,\quad \mathcal J_\lambda=0.05\lambda+p^Te^u
$$

$$
q^T(s_D-\hat s)-p_D^Tr=-p_D^Tr_D+r_{p,D}^T(s_D-\hat s)
$$

### 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

### 確認の限界

連続foldは離散foldではありません。rtol1e-4/1e-8は達成必須、requested1e-12は観測のみで未達を収束と表示しません。返却候補の独立勾配精度は別判定。最小固有値/丸めscaleは浮動小数点の診断で保証区間ではありません。BratuのJは対称であり、非対称転置は別の演算子対照です。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

### 保存実測値と判定

```json
{
  "metrics": {
    "principal_records": 6,
    "FD_state_solves": 36,
    "tight_target_policy": "1e-12 observational; exact returned candidate retained. Passing case does not imply target attained."
  },
  "checks": {
    "n31-point0-finite-state-branches": true,
    "n31-point0-strict-state-reference": true,
    "n31-point0-state-residuals": true,
    "n31-point0-below-discrete-fold": true,
    "n31-point0-strict-gradient-reference": true,
    "n31-point0-direct-duality": true,
    "n31-point0-GMRES-fixed-targets": true,
    "n31-point0-residual-identities": true,
    "n31-point0-FD-complete": true,
    "n31-point1-finite-state-branches": true,
    "n31-point1-strict-state-reference": true,
    "n31-point1-state-residuals": true,
    "n31-point1-below-discrete-fold": true,
    "n31-point1-strict-gradient-reference": true,
    "n31-point1-direct-duality": true,
    "n31-point1-GMRES-fixed-targets": true,
    "n31-point1-residual-identities": true,
    "n31-point1-FD-complete": true,
    "n31-point2-finite-state-branches": true,
    "n31-point2-strict-state-reference": true,
    "n31-point2-state-residuals": true,
    "n31-point2-below-discrete-fold": true,
    "n31-point2-strict-gradient-reference": true,
    "n31-point2-direct-duality": true,
    "n31-point2-GMRES-fixed-targets": true,
    "n31-point2-residual-identities": true,
    "n31-point2-FD-complete": true,
    "n63-point0-finite-state-branches": true,
    "n63-point0-strict-state-reference": true,
    "n63-point0-state-residuals": true,
    "n63-point0-below-discrete-fold": true,
    "n63-point0-strict-gradient-reference": true,
    "n63-point0-direct-duality": true,
    "n63-point0-GMRES-fixed-targets": true,
    "n63-point0-residual-identities": true,
    "n63-point0-FD-complete": true,
    "n63-point1-finite-state-branches": true,
    "n63-point1-strict-state-reference": true,
    "n63-point1-state-residuals": true,
    "n63-point1-below-discrete-fold": true,
    "n63-point1-strict-gradient-reference": true,
    "n63-point1-direct-duality": true,
    "n63-point1-GMRES-fixed-targets": true,
    "n63-point1-residual-identities": true,
    "n63-point1-FD-complete": true,
    "n63-point2-finite-state-branches": true,
    "n63-point2-strict-state-reference": true,
    "n63-point2-state-residuals": true,
    "n63-point2-below-discrete-fold": true,
    "n63-point2-strict-gradient-reference": true,
    "n63-point2-direct-duality": true,
    "n63-point2-GMRES-fixed-targets": true,
    "n63-point2-residual-identities": true,
    "n63-point2-FD-complete": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-sensitivity/index.json

![離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-fold-sensitivity-preview.png)

離散fold近傍のBratu感度。実際の保存数値データの縮小図で、1次元問題です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
math.sumprodの公式API選択箇所を確認。閲覧日は出版年ではなく、一般の正丸め保証ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 分布係数Bratuの行列非形成VJP

2重みだけの局所hat作用で8/16/32個の空間係数を表し、目的関数ごとの随伴VJPを全感度参照と比較します。

**使用手法**

- [陰関数微分・随伴法](https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja) (`adjoint`)
- [再始動GMRES](https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja) (`gmres`)
- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Armijo減衰Newton法](https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja) (`newton`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-algorithm)

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

- [Bratu非線形境界値問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja) (`bratu`)

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。


**問題の図**

![分布係数Bratuの行列非形成VJP：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[分布係数Bratuの行列非形成VJP](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja) (`bratu-distributed-vjp`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu-distributed-vjp/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/?lang=ja#bratu-distributed-vjp-ja-validation)

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

- [分布Bratu係数の独立dense感度と行列不要VJP](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-bratu-distributed-vjp-ja) (`bratu-distributed-vjp`; 同じ問題の参照 · 有限格子の数値参照)

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。
### 前提・単位・境界

内点63、a(x)=2+Bθ、θ=.2sin(2πξ)+.1cos(πξ)。uと感度は固定零Dirichlet境界ですが、係数の両端controlは固定零ではありません。

**編集上の補足**

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

### 採用した計算法

Bvは局所gather、B転置はscatter-add。一次実装はn×m行列を作らずJvで解き、同一状態の1/3目的関数で実際に1個のPoisson因子を共有します。別の参照期間のみdense hatとm本の接線RHSを許可します。 R2は同じfloat64の隣接差を先に取る一般Jvで、元の非線形残差・GMRES・許容差は変更しません。 R3は状態Newton補正だけをhi+loで保持し、直接9積残差と3積状態更新を使います。物理状態はfloat64、感度/随伴GMRESは旧方式です。

$$
G=A_hu-(2+B\theta)e^u,\quad J^Tp=q,\quad \nabla_\theta\mathcal J=B^T(e^u\odot p)
$$

$$
a_{\rm endpoints}=[a-b,a+b],\quad\theta_{\rm endpoints}=[a-b-2,a+b-2]
$$

### 比較・検証

実行前凍結:独立67項目の参照資格後、共有32pytestと本群141固定判定。各候補の全入力・全許容差・失敗を保存します。実合否は同梱result/verificationを参照。 初回は32pytestと拡散59/近fold45判定後に内側残差未達で停止し保存。R2の一般Jv演算順は別96成分で資格済みですが、本試験の成功を意味しません。 R2本試験も保存済み未達。R3の状態専用hi+loは別20成分で資格済み、本3caseの合否は実result/verificationで確認します。 所有配列の全詳細はrecordsのlinear_memory内のfile/byteoffset/recordSHAからJSONLへ辿れ、本文には要約だけを表示します。

### 確認の限界

同じ離散状態の微分検証で、独立した物理PDE解の証明や一般ADではありません。保存arrayと固定Krylov workspaceの記録はRSS測定ではありません。m=2のθ端点は[a-b-2,a+b-2]で、物理係数端点[a-b,a+b]と区別します。 inputsの/solver/gmres/retention_adaptationはR1/R2の履歴記述で、現状態解法は新契約の明示混合精度が上書きします。射影解の未達は別保存します。

### 保存実測値と判定

```json
{
  "metrics": {
    "principal_records": 3,
    "FD_state_solves": 18,
    "affine_error": 4.440892098500626e-16,
    "wrong_offset_error": 2.0000000000000004,
    "primary_scope": "Persistent named-array inventory and declared fixed Krylov workspace; not an RSS/peak-allocation measurement."
  },
  "checks": {
    "m8-state-residual": true,
    "m8-coefficient": true,
    "m8-duality": true,
    "m8-VJP-dense-reference": true,
    "m8-FD-finest": true,
    "m8-objective-count": true,
    "m8-allocation": true,
    "m8-finite-boundary": true,
    "m16-state-residual": true,
    "m16-coefficient": true,
    "m16-duality": true,
    "m16-VJP-dense-reference": true,
    "m16-FD-finest": true,
    "m16-objective-count": true,
    "m16-allocation": true,
    "m16-finite-boundary": true,
    "m32-state-residual": true,
    "m32-coefficient": true,
    "m32-duality": true,
    "m32-VJP-dense-reference": true,
    "m32-FD-finest": true,
    "m32-objective-count": true,
    "m32-allocation": true,
    "m32-finite-boundary": true,
    "nonsymmetric-transpose": true,
    "affine-offset": true,
    "qualified-cache": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-distributed-vjp/index.json

![分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/bratu-distributed-vjp-preview.png)

分布係数Bratuの行列非形成VJP。実際の保存数値データの縮小図で、1次元問題です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/atlas-adjoint-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/adjoint/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- SUNDIALS CVODES adjoint usage [accessed 2026-11-24]. https://sundials.readthedocs.io/en/latest/cvodes/Usage/ADJ.html; review_level=official-documentation-selected-sections
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- JAX vjp API [accessed 2026-11-24]. https://docs.jax.dev/en/latest/_autosummary/jax.vjp.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 decimal documentation [accessed 2026-11-24]. https://docs.python.org/3.12/library/decimal.html; review_level=official-documentation-selected-API
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Dickson,Kelley,Ipsen,Kevrekidis:Condition Estimates for Pseudo-Arclength Continuation [accessed 2026-11-24]. https://ipsen.math.ncsu.edu/ps/sinum65438.pdf; review_level=author-paper-selected-equations
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Author-hosted INF5620 nonlinear exercises,Problem8,Eq52 [accessed 2026-11-24]. https://hplgit.github.io/INF5620/doc/pub/._main_nonlin005.html; review_level=author-teaching-source-selected-equation
選択部分のみを確認。閲覧日は出版年ではありません。独立数値参照の資格は別途記録します。

- Python3.12.16 math documentation,math.sumprod [accessed 2026-11-24]. https://docs.python.org/3.12/library/math.html#math.sumprod; review_level=official-selected-API
math.sumprodの公式API選択箇所を確認。閲覧日は出版年ではなく、一般の正丸め保証ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
