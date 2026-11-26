# 拘束・軌道・多周波数の幾何積分

SHAKE/RATTLE、Kepler軌道、結合振動子を固定した小規模条件で比較します。拘束、位相、エネルギーと丸め誤差を別々に示します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## SHAKEとRATTLE：拘束と運動量の違い

単振り子の10固定軌道で、位置拘束、全時刻の接線運動量と内部点の中心化運動量を区別します。

**使用手法**

- [SHAKE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/shake/?lang=ja) (`shake`)
- [RATTLE拘束積分](https://hrkoyama.github.io/numerical-methods-atlas/methods/rattle/?lang=ja) (`rattle`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-algorithm)

独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

- [拘束付き平面振り子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#constrained-pendulum-ja) (`constrained-pendulum`)

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。


**問題の図**

![SHAKEとRATTLE：拘束と運動量の違い：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[拘束付き振り子](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja) (`high-index-pendulum`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/high-index-pendulum/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/?lang=ja#shake-rattle-pendulum-ja-validation)

独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

- [振り子の指数低減・拘束ドリフト・明示安定化](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-high-index-pendulum-ja) (`high-index-pendulum`; 同じ問題の参照 · 半解析参照)

投影・正規化・SHAKE/RATTLEなし。一般指数3ソルバーやシンプレクティック性の検証ではありません。

- [SHAKEとRATTLE：拘束と運動量の違い](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-shake-rattle-pendulum-ja) (`shake-rattle-pendulum`; 同じ問題の参照 · 半解析参照)

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。
### 前提・単位・境界

L=m=g=1、初期角0.7、初期角速度0。C=(q·q−1)/2、T=100、h=0.04/0.02/0.01。拘束目標1e−13と粗格子の1e−10比較を固定。

**編集上の補足**

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

独自のスカラーNewton位置拘束、RATTLE終端接線impulse、SHAKE位置対。SHAKEの運動量は内部点だけで中心化し、端点を作りません。 SHAKEのsolves列はeta、eta/h^2、位置残差、Newton更新数です。列1は一律にeta/h^2ですが、初回半刻みの物理乗数は2eta/h^2、以後の位置Verletではeta/h^2です。逆位置対はすべて後者です。判定と図はこの列1を使いません。

$$
C(q)=\tfrac12(q^Tq-1)=0
$$

$$
q_{n+1}=q_n+h p_n+\tfrac12h^2 f-\eta_n q_n
$$

$$
q_n^Tp_n^c=\frac{\|q_n-q_{n-1}\|^2-\|q_{n+1}-q_n\|^2}{4h}+\frac{C_{n+1}-C_{n-1}}{2h}
$$

### 比較・検証

独立Jacobi解析族と角度系DOP853の資格、74主判定。有限Cの中心化恒等式、2段階FDの縮約写像診断、位置対／全状態の逆積分を分離。

### 確認の限界

原著SHAKE/RATTLE本文は未読で、著者講義ノートの選択箇所を確認。有限差分のsymplectic defectは一般証明ではなく、中心化SHAKE速度にRATTLEの接線拘束を要求しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "rattle_observed_orders": [
      2.0002044529735445,
      2.0000564458078465
    ],
    "shake_observed_orders": [
      2.000077432739235,
      2.0000041345609065
    ],
    "reduced_map_probes": [
      {
        "state": [
          0.7,
          0.0
        ],
        "symplectic_defect": 3.424459604772778e-10,
        "FD_difference": 1.7850310118916468e-10
      },
      {
        "state": [
          0.3,
          0.2
        ],
        "symplectic_defect": 3.746203347532173e-11,
        "FD_difference": 1.8735013540549517e-10
      },
      {
        "state": [
          -0.4,
          -0.3
        ],
        "symplectic_defect": 1.2937362292575472e-10,
        "FD_difference": 2.7755575615628914e-10
      }
    ],
    "evolution_count": 10,
    "centered_SHAKE_not_RATTLE_tangent": true,
    "maximum_constraint": 3.811062576630775e-12
  },
  "checks": {
    "rattle-tight-2500-finite": true,
    "rattle-tight-2500-completed": true,
    "rattle-tight-2500-constraint": true,
    "rattle-tight-2500-state": true,
    "rattle-tight-2500-energy": true,
    "rattle-tight-2500-solver": true,
    "rattle-tight-2500-tangent": true,
    "rattle-tight-5000-finite": true,
    "rattle-tight-5000-completed": true,
    "rattle-tight-5000-constraint": true,
    "rattle-tight-5000-state": true,
    "rattle-tight-5000-energy": true,
    "rattle-tight-5000-solver": true,
    "rattle-tight-5000-tangent": true,
    "rattle-tight-10000-finite": true,
    "rattle-tight-10000-completed": true,
    "rattle-tight-10000-constraint": true,
    "rattle-tight-10000-state": true,
    "rattle-tight-10000-energy": true,
    "rattle-tight-10000-solver": true,
    "rattle-tight-10000-tangent": true,
    "rattle-loose-2500-finite": true,
    "rattle-loose-2500-completed": true,
    "rattle-loose-2500-constraint": true,
    "rattle-loose-2500-state": true,
    "rattle-loose-2500-energy": true,
    "rattle-loose-2500-solver": true,
    "rattle-loose-2500-tangent": true,
    "rattle-reverse-finite": true,
    "rattle-reverse-steps": true,
    "rattle-reverse-recovery": true,
    "shake-tight-2500-finite": true,
    "shake-tight-2500-completed": true,
    "shake-tight-2500-constraint": true,
    "shake-tight-2500-state": true,
    "shake-tight-2500-energy": true,
    "shake-tight-2500-solver": true,
    "shake-tight-2500-finite-C-identity": true,
    "shake-tight-2500-centered-tangency": true,
    "shake-tight-5000-finite": true,
    "shake-tight-5000-completed": true,
    "shake-tight-5000-constraint": true,
    "shake-tight-5000-state": true,
    "shake-tight-5000-energy": true,
    "shake-tight-5000-solver": true,
    "shake-tight-5000-finite-C-identity": true,
    "shake-tight-5000-centered-tangency": true,
    "shake-tight-10000-finite": true,
    "shake-tight-10000-completed": true,
    "shake-tight-10000-constraint": true,
    "shake-tight-10000-state": true,
    "shake-tight-10000-energy": true,
    "shake-tight-10000-solver": true,
    "shake-tight-10000-finite-C-identity": true,
    "shake-tight-10000-centered-tangency": true,
    "shake-loose-2500-finite": true,
    "shake-loose-2500-completed": true,
    "shake-loose-2500-constraint": true,
    "shake-loose-2500-state": true,
    "shake-loose-2500-energy": true,
    "shake-loose-2500-solver": true,
    "shake-loose-2500-finite-C-identity": true,
    "shake-loose-2500-centered-tangency": true,
    "shake-reverse-finite": true,
    "shake-reverse-steps": true,
    "shake-reverse-recovery": true,
    "rattle-state-order": true,
    "shake-state-order": true,
    "reduced-map-0-symplectic-proxy": true,
    "reduced-map-0-FD-consistency": true,
    "reduced-map-1-symplectic-proxy": true,
    "reduced-map-1-FD-consistency": true,
    "reduced-map-2-symplectic-proxy": true,
    "reduced-map-2-FD-consistency": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/shake-rattle-pendulum/index.json

![保存したh=0.01の縮約位相軌道。SHAKEは内部点の中心化運動量、RATTLEは全時刻の接線運動量です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/shake-rattle-pendulum-preview.png)

保存したh=0.01の縮約位相軌道。SHAKEは内部点の中心化運動量、RATTLEは全時刻の接線運動量です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Solving Differential Equations on Manifolds [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly-sde-mani.pdf; review_level=selected-primary-scope
Author-hosted lecture notes, selected printed page50, SectionV.5, equations5.1–5.3 and Theorem5.1 statement, rendered and visually read. Centered SHAKE momentum and RATTLE final tangency are explicit. The original1977 SHAKE and1983 RATTLE articles remain full-text unread; no full proof review is claimed.

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- DLMF22.4: Periods, Poles, and Zeros (version 1.2.8, released 2026-09-15) [accessed 2026-11-24]. https://dlmf.nist.gov/22.4; review_level=selected-primary-scope
Official Table22.4.1 selected real periods: sn and cn have4K, dn has2K. Version date is not an initial publication date. Common-period reduction and direct-library periodicity qualification are separate from the independent angular DOP853 state comparison.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 離心率を変えたKepler軌道と時間刻み

e=0.1/0.7の16固定軌道で、保存量と同時刻の位相誤差、実際の近日点時刻と逆積分を比較します。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-algorithm)

独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の動径速度での交差をbrentqで局在化。

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

- [Kepler二体問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kepler-two-body-ja) (`kepler-two-body`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。


**問題の図**

![離心率を変えたKepler軌道と時間刻み：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja) (`gravity-kepler`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/gravity-kepler/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/?lang=ja#kepler-eccentricity-ja-validation)

独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

- [無軟化Kepler二体の時間誤差](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gravity-kepler-ja) (`gravity-kepler`; 同じ問題の参照 · 解析参照)

1周期・固定離心率のみ。軟化軌道や長時間安定性はこの参照の範囲外。

- [離心率を変えたKepler軌道と時間刻み](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-kepler-eccentricity-ja) (`kepler-eccentricity`; 同じ問題の参照 · 半解析参照)

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。
### 前提・単位・境界

a=μ=換算質量=1、軟化なし。1周期は512/1024/2048刻み、10周期は基準2048刻み/周期。変動刻みh=h0|q|を現在状態から定め、最後だけ物理終端へ短縮。

**編集上の補足**

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

独自の中心力KDK Verlet。固定・保存刻み再生・再生成刻みを区別し、cubic Hermite軌道の正の動径速度での交差をbrentqで局在化。

$$
\ddot q=-q/\|q\|^3
$$

$$
E-e\sin E=t,\quad q=(\cos E-e,\sqrt{1-e^2}\sin E)
$$

$$
H=\tfrac12\|p\|^2-1/\|q\|
$$

### 比較・検証

独立のKepler方程式brentq／二分法解析族、92主判定。全状態誤差とエネルギー・角運動量、8回以上の近日点、有限窓の順序と反転誤差を検査。

### 確認の限界

保存量の小さい誤差から位相精度を推論しません。変動刻み写像の正準symplectic defectは測定せず、固定hの性質をそのまま移しません。初期解像度R1は数値実行前の漸近解析でR2へ改訂。

### 保存実測値と判定

```json
{
  "metrics": {
    "e0.1_orders": [
      1.9999876782390122,
      1.9999962905452664
    ],
    "e0.7_orders": [
      1.987542094585538,
      2.000215589787777
    ],
    "evolution_count": 16,
    "variable_map_symplecticity_measured": false,
    "max_state_error": 0.39849708597264355
  },
  "checks": {
    "e0p1-fixed-512-finite": true,
    "e0p1-fixed-512-time": true,
    "e0p1-fixed-512-radius": true,
    "e0p1-fixed-512-angular": true,
    "e0p1-fixed-512-energy": true,
    "e0p1-fixed-512-reference": true,
    "e0p1-fixed-1024-finite": true,
    "e0p1-fixed-1024-time": true,
    "e0p1-fixed-1024-radius": true,
    "e0p1-fixed-1024-angular": true,
    "e0p1-fixed-1024-energy": true,
    "e0p1-fixed-1024-reference": true,
    "e0p1-fixed-2048-finite": true,
    "e0p1-fixed-2048-time": true,
    "e0p1-fixed-2048-radius": true,
    "e0p1-fixed-2048-angular": true,
    "e0p1-fixed-2048-energy": true,
    "e0p1-fixed-2048-reference": true,
    "e0p1-fixed-long-finite": true,
    "e0p1-fixed-long-time": true,
    "e0p1-fixed-long-radius": true,
    "e0p1-fixed-long-angular": true,
    "e0p1-fixed-long-energy": true,
    "e0p1-fixed-long-reference": true,
    "e0p1-fixed-long-periapsis-count": true,
    "e0p1-fixed-long-periapsis-time": true,
    "e0p1-variable-long-finite": true,
    "e0p1-variable-long-time": true,
    "e0p1-variable-long-radius": true,
    "e0p1-variable-long-angular": true,
    "e0p1-variable-long-energy": true,
    "e0p1-variable-long-reference": true,
    "e0p1-variable-long-periapsis-count": true,
    "e0p1-variable-long-periapsis-time": true,
    "e0p1-reverse-fixed-finite": true,
    "e0p1-reverse-fixed-schedule": true,
    "e0p1-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-replay-finite": true,
    "e0p1-reverse-variable-replay-schedule": true,
    "e0p1-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p1-reverse-variable-regenerated-finite": true,
    "e0p1-reverse-variable-regenerated-schedule": true,
    "e0p1-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0p7-fixed-512-finite": true,
    "e0p7-fixed-512-time": true,
    "e0p7-fixed-512-radius": true,
    "e0p7-fixed-512-angular": true,
    "e0p7-fixed-512-energy": true,
    "e0p7-fixed-512-reference": true,
    "e0p7-fixed-1024-finite": true,
    "e0p7-fixed-1024-time": true,
    "e0p7-fixed-1024-radius": true,
    "e0p7-fixed-1024-angular": true,
    "e0p7-fixed-1024-energy": true,
    "e0p7-fixed-1024-reference": true,
    "e0p7-fixed-2048-finite": true,
    "e0p7-fixed-2048-time": true,
    "e0p7-fixed-2048-radius": true,
    "e0p7-fixed-2048-angular": true,
    "e0p7-fixed-2048-energy": true,
    "e0p7-fixed-2048-reference": true,
    "e0p7-fixed-long-finite": true,
    "e0p7-fixed-long-time": true,
    "e0p7-fixed-long-radius": true,
    "e0p7-fixed-long-angular": true,
    "e0p7-fixed-long-energy": true,
    "e0p7-fixed-long-reference": true,
    "e0p7-fixed-long-periapsis-count": true,
    "e0p7-fixed-long-periapsis-time": true,
    "e0p7-variable-long-finite": true,
    "e0p7-variable-long-time": true,
    "e0p7-variable-long-radius": true,
    "e0p7-variable-long-angular": true,
    "e0p7-variable-long-energy": true,
    "e0p7-variable-long-reference": true,
    "e0p7-variable-long-periapsis-count": true,
    "e0p7-variable-long-periapsis-time": true,
    "e0p7-reverse-fixed-finite": true,
    "e0p7-reverse-fixed-schedule": true,
    "e0p7-reverse-fixed-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-replay-finite": true,
    "e0p7-reverse-variable-replay-schedule": true,
    "e0p7-reverse-variable-replay-recovery-or-diagnostic-scope": true,
    "e0p7-reverse-variable-regenerated-finite": true,
    "e0p7-reverse-variable-regenerated-schedule": true,
    "e0p7-reverse-variable-regenerated-recovery-or-diagnostic-scope": true,
    "e0.1-fine-state": true,
    "e0.1-state-order": true,
    "e0.1-fine-energy": true,
    "e0.7-fine-state": true,
    "e0.7-state-order": true,
    "e0.7-fine-energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/kepler-eccentricity/index.json

![保存したe=0.7、10周期の固定刻み／変動刻み軌道。物理座標は等倍率で、中心力は軟化していません。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/kepler-eccentricity-preview.png)

保存したe=0.7、10周期の固定刻み／変動刻み軌道。物理座標は等倍率で、中心力は軟化していません。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.

- Approximate Positions of the Planets [accessed 2026-11-24]. https://ssd.jpl.nasa.gov/planets/approx_pos.html; review_level=selected-primary-scope
Official JPL page, selected steps3–4 and Kepler equation. Only the eccentric-anomaly equation and elliptic coordinate transformation are used; no planetary coefficient tables, fitted ephemeris accuracy or Horizons calculation is claimed. Publication date was not verified.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 結合した2周波数系と共鳴の有限窓

2自由度の実結合系で、12の64刻みprobeと6の精度軌道を使い、真のモード、座標間交換、離散写像と丸めを分けます。

**使用手法**

- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-algorithm)

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

- [二周波数の結合調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coupled-harmonic-oscillators-ja) (`coupled-harmonic-oscillators`)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

- [Hamilton系・振動子](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hamiltonian-ja) (`hamiltonian`)

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。


**問題の図**

![結合した2周波数系と共鳴の有限窓：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja) (`multifrequency-resonance`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/multifrequency-resonance/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/?lang=ja#multifrequency-resonance-ja-validation)

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

- [結合した2周波数系と共鳴の有限窓](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-multifrequency-resonance-ja) (`multifrequency-resonance`; 同じ問題の参照 · 半解析参照)

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。
### 前提・単位・境界

α=1、ω=10/20、q0=(1,1/ω)、p0=0。中心probeは保存binary64のhとsin/cosをそのまま使い、πへ丸め直しません。

**編集上の補足**

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。 図の軌道・状態・時刻・反復の軸は、物理空間の次元を表しません。

### 採用した計算法

全ポテンシャルVerletと、B半kick・A厳密flow・B半kickのStrang impulse。Aには高速調和振動子と低速自由流、Bには低速位置項と結合を含めます。

$$
H=\tfrac12(p_1^2+p_2^2+q_1^2+\omega^2q_2^2)+\alpha q_1q_2
$$

$$
\Phi_h=\varphi^B_{h/2}\circ\varphi^A_h\circ\varphi^B_{h/2}
$$

$$
\chi_{\theta=\pi}(z)=(z+1)^2[z^2-(2-h^2)z+1]
$$

### 比較・検証

116主判定。独立の結合固有モード解析、保存係数Decimal80/120・Fraction写像、段階別γ8丸め上界を区別。理想πのJordan構造は有理恒等式で別確認。 各probeは現在保存した係数hexからDecimal80/120を評価し、6精度軌道はDecimal80を用います。

### 確認の限界

中心の実浮動係数写像はunresolvedとし、理想πのJordan性を移しません。64刻み増幅と小さい固定入力の観測であり、走査した共鳴図・一般安定性・長時間の普遍誤差定理は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "verlet_observed_orders": [
      2.0006335257949495,
      2.0004237164828513
    ],
    "impulse_observed_orders": [
      2.000688773919643,
      2.0001158542645605
    ],
    "evolution_count": 18,
    "probe_steps": 64,
    "ideal_pi_separate_from_actual_float": true,
    "maximum_frozen_map_relative_error": 2.432468376162801e-15
  },
  "checks": {
    "w10-verlet-1p0-finite-cap": true,
    "w10-verlet-1p0-completed": true,
    "w10-verlet-1p0-discrete-reference": true,
    "w10-verlet-1p0-roundoff": true,
    "w10-verlet-1p0-symplectic": true,
    "w10-verlet-1p0-classification": true,
    "w10-verlet-1p8-finite-cap": true,
    "w10-verlet-1p8-completed": true,
    "w10-verlet-1p8-discrete-reference": true,
    "w10-verlet-1p8-roundoff": true,
    "w10-verlet-1p8-symplectic": true,
    "w10-verlet-1p8-classification": true,
    "w10-verlet-2p2-finite-cap": true,
    "w10-verlet-2p2-completed": true,
    "w10-verlet-2p2-discrete-reference": true,
    "w10-verlet-2p2-roundoff": true,
    "w10-verlet-2p2-symplectic": true,
    "w10-verlet-2p2-classification": true,
    "w10-impulse-0p9-finite-cap": true,
    "w10-impulse-0p9-completed": true,
    "w10-impulse-0p9-discrete-reference": true,
    "w10-impulse-0p9-roundoff": true,
    "w10-impulse-0p9-symplectic": true,
    "w10-impulse-0p9-classification": true,
    "w10-impulse-1p0-finite-cap": true,
    "w10-impulse-1p0-completed": true,
    "w10-impulse-1p0-discrete-reference": true,
    "w10-impulse-1p0-roundoff": true,
    "w10-impulse-1p0-symplectic": true,
    "w10-impulse-1p0-classification": true,
    "w10-impulse-1p1-finite-cap": true,
    "w10-impulse-1p1-completed": true,
    "w10-impulse-1p1-discrete-reference": true,
    "w10-impulse-1p1-roundoff": true,
    "w10-impulse-1p1-symplectic": true,
    "w10-impulse-1p1-classification": true,
    "w20-verlet-1p0-finite-cap": true,
    "w20-verlet-1p0-completed": true,
    "w20-verlet-1p0-discrete-reference": true,
    "w20-verlet-1p0-roundoff": true,
    "w20-verlet-1p0-symplectic": true,
    "w20-verlet-1p0-classification": true,
    "w20-verlet-1p8-finite-cap": true,
    "w20-verlet-1p8-completed": true,
    "w20-verlet-1p8-discrete-reference": true,
    "w20-verlet-1p8-roundoff": true,
    "w20-verlet-1p8-symplectic": true,
    "w20-verlet-1p8-classification": true,
    "w20-verlet-2p2-finite-cap": true,
    "w20-verlet-2p2-completed": true,
    "w20-verlet-2p2-discrete-reference": true,
    "w20-verlet-2p2-roundoff": true,
    "w20-verlet-2p2-symplectic": true,
    "w20-verlet-2p2-classification": true,
    "w20-impulse-0p9-finite-cap": true,
    "w20-impulse-0p9-completed": true,
    "w20-impulse-0p9-discrete-reference": true,
    "w20-impulse-0p9-roundoff": true,
    "w20-impulse-0p9-symplectic": true,
    "w20-impulse-0p9-classification": true,
    "w20-impulse-1p0-finite-cap": true,
    "w20-impulse-1p0-completed": true,
    "w20-impulse-1p0-discrete-reference": true,
    "w20-impulse-1p0-roundoff": true,
    "w20-impulse-1p0-symplectic": true,
    "w20-impulse-1p0-classification": true,
    "w20-impulse-1p1-finite-cap": true,
    "w20-impulse-1p1-completed": true,
    "w20-impulse-1p1-discrete-reference": true,
    "w20-impulse-1p1-roundoff": true,
    "w20-impulse-1p1-symplectic": true,
    "w20-impulse-1p1-classification": true,
    "w10-verlet-accuracy-500-finite": true,
    "w10-verlet-accuracy-500-completed": true,
    "w10-verlet-accuracy-500-state": true,
    "w10-verlet-accuracy-500-energy": true,
    "w10-verlet-accuracy-500-mode": true,
    "w10-verlet-accuracy-500-discrete-reference": true,
    "w10-verlet-accuracy-1000-finite": true,
    "w10-verlet-accuracy-1000-completed": true,
    "w10-verlet-accuracy-1000-state": true,
    "w10-verlet-accuracy-1000-energy": true,
    "w10-verlet-accuracy-1000-mode": true,
    "w10-verlet-accuracy-1000-discrete-reference": true,
    "w10-verlet-accuracy-2000-finite": true,
    "w10-verlet-accuracy-2000-completed": true,
    "w10-verlet-accuracy-2000-state": true,
    "w10-verlet-accuracy-2000-energy": true,
    "w10-verlet-accuracy-2000-mode": true,
    "w10-verlet-accuracy-2000-discrete-reference": true,
    "w10-impulse-accuracy-500-finite": true,
    "w10-impulse-accuracy-500-completed": true,
    "w10-impulse-accuracy-500-state": true,
    "w10-impulse-accuracy-500-energy": true,
    "w10-impulse-accuracy-500-mode": true,
    "w10-impulse-accuracy-500-discrete-reference": true,
    "w10-impulse-accuracy-1000-finite": true,
    "w10-impulse-accuracy-1000-completed": true,
    "w10-impulse-accuracy-1000-state": true,
    "w10-impulse-accuracy-1000-energy": true,
    "w10-impulse-accuracy-1000-mode": true,
    "w10-impulse-accuracy-1000-discrete-reference": true,
    "w10-impulse-accuracy-2000-finite": true,
    "w10-impulse-accuracy-2000-completed": true,
    "w10-impulse-accuracy-2000-state": true,
    "w10-impulse-accuracy-2000-energy": true,
    "w10-impulse-accuracy-2000-mode": true,
    "w10-impulse-accuracy-2000-discrete-reference": true,
    "verlet-state-order": true,
    "verlet-fine-state": true,
    "verlet-fine-relative-H": true,
    "verlet-fine-coordinate-energy": true,
    "impulse-state-order": true,
    "impulse-fine-state": true,
    "impulse-fine-relative-H": true,
    "impulse-fine-coordinate-energy": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/multifrequency-resonance/index.json

![保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/multifrequency-resonance-preview.png)

保存した最細impulse軌道の実q1–q2座標と物理時刻。これは走査相図ではなく、結合した1軌道です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/atlas-geometric-controls-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/geometric-controls/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Lecture2: Symplectic integrators [accessed 2026-11-24]. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=selected-primary-scope
Author-hosted course notes, selected rendered printed pages2,12–13: Verlet kick/drift form, symplectic statement, Lie and symmetric Strang compositions. This does not qualify every state-dependent step rule or the authored coupled resonance experiment.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
