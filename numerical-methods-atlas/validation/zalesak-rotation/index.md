# Zalesak型2D回転輸送：保存・有界性・形状誤差

スロット付き円盤を実際の2次元有限体積法で一回転させ、donor-cellとminmod MUSCLを比較します。3格子と、半セルの中心ずらし・45度の初期向きを含む8計算で、保存・各SSP段の有界性・形状誤差とスロットの埋まりを測ります。

**使用手法**

- [風上差分（upwind）](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=ja) (`upwind`)
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=ja) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) (`ssprk33`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-algorithm)

解析的な発散ゼロの法線面速度と、隣接セルで共有する上流数値流束を用います。区分定数donor-cellと、方向別minmod勾配による平均保存型MUSCLを、どちらもSSPRK(3,3)で進めます。4面中点の平均がセル平均に等しいことと、各面のCourant数≤1/4による凸結合を使い、実際の値.20を各FE段で確認します。セル平均のクリップ、状態floor、刻み棄却・再試行は行いません。

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

- [2次元の回転移流](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#rotational-advection-ja) (`rotational-advection`)

qの2次元保存形輸送。速度a=−ω(y−yc), b=ω(x−xc)は与えられ、∂xa+∂yb=0です。面で共有する速度・数値流束を使い、スカラーのセル平均を更新します。


**問題の図**

![Zalesak型2D回転輸送：保存・有界性・形状誤差：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Zalesak型の切り欠き円盤の回転輸送](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja) (`zalesak`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=ja#zalesak-rotation-ja-validation)

26単体検査と8固定計算158判定を実行前に固定します。全FE候補・SSP凸結合のmin/max、共有流束による質量収支、再構築の平均保存、3格子のL1/L∞・相対L2を保存します。円と凸多角形の交差面積から独立に作る厳密輸送のセル平均を、SciPyの鉛直切片求積と面積・一次モーメントで照合します。1/4・1/2・3/4回転の誤差と重心も検査し、回転方向や速度の誤りが一回転のreturnだけで隠れないようにします。

- [Zalesak型の切り欠き円盤：剛体回転と幾何学的セル平均](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-zalesak-rotation-ja) (`zalesak-rotation`; 同じ問題の参照 · 解析参照)

円盤とスロットの定義を固定し、保存した初期・帰還時のセル平均と比較します。指示関数の点値や別実装PDEの細格子解を参照と混同しません。
## 前提・単位・境界

無次元の[0,1]²、回転中心(.5,.5)、円盤中心(.5,.75)、半径.15、スロット幅.05・上端y=.85、角速度1、一回転T=2π、64²/128²/256²セルを固定します。スロット以外はq=1、外側は0です。周期境界を使い、厳密な物体の支持は境界から離れます。速度の周期延長には接線成分の継ぎ目があり、数値拡散の裾が届く場合は境界帯の質量として記録します。

**編集上の補足**

与えた発散ゼロの回転速度に従うスカラー輸送で、Euler流体の発展ではありません。Zalesak型の円盤・スロットによる形状保持の問題を用いますが、ZalesakのFCTアルゴリズムそのものを実装した例ではありません。連続指示関数の点値と保存量の幾何学的セル平均を区別し、周期境界での数値的な裾も測ります。 初版の32²/64²/128²では26検査・156/158判定に合格しましたが、最細の相対L1誤差が一次風上で約1.11675（基準1.0）、MUSCLで約.6023（基準.55）となり不合格でした。元入力・受入基準・保存配列・失敗を保持し、受入基準と流束・26検査を変えずに、改訂の実行前契約で基準系列を64²/128²/256²へ細分化しました。 改訂は26検査と8計算158判定に合格し、テストと本計算は同じ120秒枠で約19.58秒でした。N256の相対L1は一次風上約.932256、MUSCL約.394271（比約.423）、全計算の質量変化の最大値は約8.90×10⁻¹⁵です。全段の記録範囲は0〜1でしたが、この範囲には初期状態も含み、有界性だけで切り欠きが正しく保たれたとは判断しません。空スロット内プローブはセル平均の区分定数場を重み付けする離散診断で、連続解の点値ではありません。参照セル平均にも混合セルによる射影基準があるため、数値平均・参照平均・その差を別に保存します。N256の超過量は一次風上約.63465、MUSCL約.36501と、なお拡散が残ります。N64ではMUSCLのプローブ超過量が一次風上を上回る場合もあり、全指標・全格子での一様な優位は主張しません。幅.05の境界帯にある質量の割合はN256で約.0178615/.000243761（一次風上/MUSCL）でした。連続の厳密場はこの帯でゼロであり、周期境界へ伸びる数値的な裾を隠していません。

## 採用した計算法

解析的な発散ゼロの法線面速度と、隣接セルで共有する上流数値流束を用います。区分定数donor-cellと、方向別minmod勾配による平均保存型MUSCLを、どちらもSSPRK(3,3)で進めます。4面中点の平均がセル平均に等しいことと、各面のCourant数≤1/4による凸結合を使い、実際の値.20を各FE段で確認します。セル平均のクリップ、状態floor、刻み棄却・再試行は行いません。

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

## 比較・検証

26単体検査と8固定計算158判定を実行前に固定します。全FE候補・SSP凸結合のmin/max、共有流束による質量収支、再構築の平均保存、3格子のL1/L∞・相対L2を保存します。円と凸多角形の交差面積から独立に作る厳密輸送のセル平均を、SciPyの鉛直切片求積と面積・一次モーメントで照合します。1/4・1/2・3/4回転の誤差と重心も検査し、回転方向や速度の誤りが一回転のreturnだけで隠れないようにします。

## 確認の限界

標準的なスロット形状を単独の0–1物体として使う周期境界の限定例です。Zalesak原著のFCTアルゴリズム、原著の格子・境界、bell/coneを加えたFiredrakeデモ全体の再現ではありません。スロット内の診断は、固定した内側長方形と区分定数セル平均との面積重み付き値です。粗格子では厳密セル平均の投影だけでも0にならないため、その参照baselineと過剰な埋まりを別々に示します。格子中心・45度方向の2診断を普遍的な等方性保証とせず、完全な形状保持や一般流れの最大値原理を主張しません。解析幾何の微小な面積丸め処理と、実際の輸送状態をクリップしないことを区別します。

## 保存実測値と判定

```json
{
  "metrics": {
    "n": 256,
    "shift_cells": 0.0,
    "angle0": 0.0,
    "time": 6.283185307179586,
    "steps": 4008,
    "stages": 12024,
    "snapshots": 5,
    "relative_l1": 0.39427105204685026,
    "l1_absolute": 0.022954737845935866,
    "linf": 0.7430454904444476,
    "relative_l2": 0.3404884399563395,
    "initial_mass": 0.05822070305889007,
    "final_mass": 0.05822070305888117,
    "mass_change": -8.902600878712974e-15,
    "initial_area_error": 6.938893903907228e-18,
    "reference_area_error": 6.938893903907228e-18,
    "reference_return_maximum": 5.5067062021407764e-14,
    "minimum": 0.0,
    "maximum": 1.0,
    "maximum_courant": 0.2,
    "maximum_mean_preservation_defect": 1.1102230246251565e-16,
    "maximum_fe_mass_defect": 2.7755575615628914e-17,
    "maximum_rk_mass_defect": 8.902600878712974e-15,
    "maximum_discrete_divergence": 0.0,
    "slot_probe_mean": 0.36500692217705044,
    "slot_probe_reference_mean": 0.0,
    "slot_probe_excess": 0.36500692217705044,
    "slot_probe_weight_sum": 286.72000000000116,
    "boundary_band_width": 0.05,
    "boundary_band_mass_fraction": 0.00024376119280261055,
    "total_variation": 1.353666880236625,
    "state_clip_count": 0,
    "retries": 0,
    "rejected_steps": 0,
    "all_saved_values_finite": true
  },
  "checks": {
    "all eight fixed rotations completed": true,
    "base-donor-cell-n64: final time": true,
    "base-donor-cell-n64: initial represented area": true,
    "base-donor-cell-n64: periodic mass conservation": true,
    "base-donor-cell-n64: three FE records per SSP step": true,
    "base-donor-cell-n64: finite saved means and stage data": true,
    "base-donor-cell-n64: all stage lower bounds": true,
    "base-donor-cell-n64: all stage upper bounds": true,
    "base-donor-cell-n64: sufficient individual face Courant": true,
    "base-donor-cell-n64: four-face mean preserved": true,
    "base-donor-cell-n64: each FE shared-flux balance": true,
    "base-donor-cell-n64: each SSP convex-mean balance": true,
    "base-donor-cell-n64: all rotated reference areas": true,
    "base-donor-cell-n64: full-turn geometric return": true,
    "base-donor-cell-n64: zero clipping and retries": true,
    "base-donor-cell-n64: exact discrete velocity divergence": true,
    "base-donor-cell-n64: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n64: final time": true,
    "base-muscl-minmod-n64: initial represented area": true,
    "base-muscl-minmod-n64: periodic mass conservation": true,
    "base-muscl-minmod-n64: three FE records per SSP step": true,
    "base-muscl-minmod-n64: finite saved means and stage data": true,
    "base-muscl-minmod-n64: all stage lower bounds": true,
    "base-muscl-minmod-n64: all stage upper bounds": true,
    "base-muscl-minmod-n64: sufficient individual face Courant": true,
    "base-muscl-minmod-n64: four-face mean preserved": true,
    "base-muscl-minmod-n64: each FE shared-flux balance": true,
    "base-muscl-minmod-n64: each SSP convex-mean balance": true,
    "base-muscl-minmod-n64: all rotated reference areas": true,
    "base-muscl-minmod-n64: full-turn geometric return": true,
    "base-muscl-minmod-n64: zero clipping and retries": true,
    "base-muscl-minmod-n64: exact discrete velocity divergence": true,
    "base-muscl-minmod-n64: quarter-turn snapshots retained": true,
    "base-donor-cell-n128: final time": true,
    "base-donor-cell-n128: initial represented area": true,
    "base-donor-cell-n128: periodic mass conservation": true,
    "base-donor-cell-n128: three FE records per SSP step": true,
    "base-donor-cell-n128: finite saved means and stage data": true,
    "base-donor-cell-n128: all stage lower bounds": true,
    "base-donor-cell-n128: all stage upper bounds": true,
    "base-donor-cell-n128: sufficient individual face Courant": true,
    "base-donor-cell-n128: four-face mean preserved": true,
    "base-donor-cell-n128: each FE shared-flux balance": true,
    "base-donor-cell-n128: each SSP convex-mean balance": true,
    "base-donor-cell-n128: all rotated reference areas": true,
    "base-donor-cell-n128: full-turn geometric return": true,
    "base-donor-cell-n128: zero clipping and retries": true,
    "base-donor-cell-n128: exact discrete velocity divergence": true,
    "base-donor-cell-n128: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n128: final time": true,
    "base-muscl-minmod-n128: initial represented area": true,
    "base-muscl-minmod-n128: periodic mass conservation": true,
    "base-muscl-minmod-n128: three FE records per SSP step": true,
    "base-muscl-minmod-n128: finite saved means and stage data": true,
    "base-muscl-minmod-n128: all stage lower bounds": true,
    "base-muscl-minmod-n128: all stage upper bounds": true,
    "base-muscl-minmod-n128: sufficient individual face Courant": true,
    "base-muscl-minmod-n128: four-face mean preserved": true,
    "base-muscl-minmod-n128: each FE shared-flux balance": true,
    "base-muscl-minmod-n128: each SSP convex-mean balance": true,
    "base-muscl-minmod-n128: all rotated reference areas": true,
    "base-muscl-minmod-n128: full-turn geometric return": true,
    "base-muscl-minmod-n128: zero clipping and retries": true,
    "base-muscl-minmod-n128: exact discrete velocity divergence": true,
    "base-muscl-minmod-n128: quarter-turn snapshots retained": true,
    "base-donor-cell-n256: final time": true,
    "base-donor-cell-n256: initial represented area": true,
    "base-donor-cell-n256: periodic mass conservation": true,
    "base-donor-cell-n256: three FE records per SSP step": true,
    "base-donor-cell-n256: finite saved means and stage data": true,
    "base-donor-cell-n256: all stage lower bounds": true,
    "base-donor-cell-n256: all stage upper bounds": true,
    "base-donor-cell-n256: sufficient individual face Courant": true,
    "base-donor-cell-n256: four-face mean preserved": true,
    "base-donor-cell-n256: each FE shared-flux balance": true,
    "base-donor-cell-n256: each SSP convex-mean balance": true,
    "base-donor-cell-n256: all rotated reference areas": true,
    "base-donor-cell-n256: full-turn geometric return": true,
    "base-donor-cell-n256: zero clipping and retries": true,
    "base-donor-cell-n256: exact discrete velocity divergence": true,
    "base-donor-cell-n256: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n256: final time": true,
    "base-muscl-minmod-n256: initial represented area": true,
    "base-muscl-minmod-n256: periodic mass conservation": true,
    "base-muscl-minmod-n256: three FE records per SSP step": true,
    "base-muscl-minmod-n256: finite saved means and stage data": true,
    "base-muscl-minmod-n256: all stage lower bounds": true,
    "base-muscl-minmod-n256: all stage upper bounds": true,
    "base-muscl-minmod-n256: sufficient individual face Courant": true,
    "base-muscl-minmod-n256: four-face mean preserved": true,
    "base-muscl-minmod-n256: each FE shared-flux balance": true,
    "base-muscl-minmod-n256: each SSP convex-mean balance": true,
    "base-muscl-minmod-n256: all rotated reference areas": true,
    "base-muscl-minmod-n256: full-turn geometric return": true,
    "base-muscl-minmod-n256: zero clipping and retries": true,
    "base-muscl-minmod-n256: exact discrete velocity divergence": true,
    "base-muscl-minmod-n256: quarter-turn snapshots retained": true,
    "half-cell-shift: final time": true,
    "half-cell-shift: initial represented area": true,
    "half-cell-shift: periodic mass conservation": true,
    "half-cell-shift: three FE records per SSP step": true,
    "half-cell-shift: finite saved means and stage data": true,
    "half-cell-shift: all stage lower bounds": true,
    "half-cell-shift: all stage upper bounds": true,
    "half-cell-shift: sufficient individual face Courant": true,
    "half-cell-shift: four-face mean preserved": true,
    "half-cell-shift: each FE shared-flux balance": true,
    "half-cell-shift: each SSP convex-mean balance": true,
    "half-cell-shift: all rotated reference areas": true,
    "half-cell-shift: full-turn geometric return": true,
    "half-cell-shift: zero clipping and retries": true,
    "half-cell-shift: exact discrete velocity divergence": true,
    "half-cell-shift: quarter-turn snapshots retained": true,
    "oblique-start: final time": true,
    "oblique-start: initial represented area": true,
    "oblique-start: periodic mass conservation": true,
    "oblique-start: three FE records per SSP step": true,
    "oblique-start: finite saved means and stage data": true,
    "oblique-start: all stage lower bounds": true,
    "oblique-start: all stage upper bounds": true,
    "oblique-start: sufficient individual face Courant": true,
    "oblique-start: four-face mean preserved": true,
    "oblique-start: each FE shared-flux balance": true,
    "oblique-start: each SSP convex-mean balance": true,
    "oblique-start: all rotated reference areas": true,
    "oblique-start: full-turn geometric return": true,
    "oblique-start: zero clipping and retries": true,
    "oblique-start: exact discrete velocity divergence": true,
    "oblique-start: quarter-turn snapshots retained": true,
    "donor-cell finest relative L1": true,
    "donor-cell refinement ratio 1": true,
    "donor-cell refinement ratio 2": true,
    "donor-cell intermediate relative L1 1": true,
    "donor-cell intermediate centroid distance 1": true,
    "donor-cell intermediate relative L1 2": true,
    "donor-cell intermediate centroid distance 2": true,
    "donor-cell intermediate relative L1 3": true,
    "donor-cell intermediate centroid distance 3": true,
    "muscl-minmod finest relative L1": true,
    "muscl-minmod refinement ratio 1": true,
    "muscl-minmod refinement ratio 2": true,
    "muscl-minmod intermediate relative L1 1": true,
    "muscl-minmod intermediate centroid distance 1": true,
    "muscl-minmod intermediate relative L1 2": true,
    "muscl-minmod intermediate centroid distance 2": true,
    "muscl-minmod intermediate relative L1 3": true,
    "muscl-minmod intermediate centroid distance 3": true,
    "finest MUSCL/donor relative L1": true,
    "half-cell-shift shape error": true,
    "oblique-start shape error": true,
    "independent geometry: analytic circle partitions conserve closed total area": true,
    "independent geometry: twelve fixed cut cells agree with independent vertical quadrature": true,
    "independent geometry: independent whole-area quadrature agrees with closed area": true,
    "independent geometry: true analytic centroid agrees with independent first moments": true,
    "independent geometry: full-turn geometric cell means return": true,
    "independent geometry: quarter-turn geometry has the correct counterclockwise orientation": true,
    "independent geometry: geometric fraction roundoff cleanup remains within its separate band": true,
    "independent geometry: analytic area cleanup remains within its dimensional floating-point band": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/index.json

![一回転後の実2次元セル平均。厳密幾何参照・donor-cell・minmod MUSCLを同じ色尺度で比較します。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

一回転後の実2次元セル平均。厳密幾何参照・donor-cell・minmod MUSCLを同じ色尺度で比較します。

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

## 出典と確認範囲

- Steven T. Zalesak (1979). Fully multidimensional flux-corrected transport algorithms for fluids [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999179900512; review_level=publisher bibliography and abstract inspected; direct full-paper open returned403; original test geometry and boundary conditions not audited
出版社の書誌と多次元FCTの抄録を確認。原著全文とその格子・境界・具体形状は今回未確認です。本例をZalesakのFCTアルゴリズム再現とは表示しません。

- Firedrake developers (n.d.). DG advection equation with upwinding [accessed 2026-11-23]. https://www.firedrakeproject.org/demos/DG_advection.py.html; review_level=official documentation equations and source lines46,63–92: disk(.5,.75),R.15,slot(.475,.525),y<.85,velocity(.5−y,x−.5),T2pi; SSP equations43–45 and135–143
公式デモの形状・回転速度・周期とSSPRK式を確認。元デモはbell・coneと背景1を加え、DQ1・流入値1を使います。本例はスロット円板だけの0–1指示関数・有限体積・周期境界という明示的な変形です。Firedrakeは実行・転載しません。

- Randall J. LeVeque (1996). High-Resolution Conservative Algorithms for Advection in Incompressible Flow [accessed 2026-11-23]. https://faculty.washington.edu/rjl/pubs/hiresadv/0733033.pdf; review_level=author-hosted paper selected sections1–3 actually inspected: PDE/incompressibility, FV means, minmod definition, donor-cell flux; no full-paper or numerical-table reproduction
著者公開論文の節1–3で保存形・非圧縮条件・セル平均・minmod・donor-cellを確認。Firedrakeが標準複合図形の出典として引用しています。本例のMUSCL＋SSPRKは同論文のCTU／波動伝播法そのものではありません。

- Chi-Wang Shu and Stanley Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999188901775; review_level=publisher bibliography/abstract inspected; actual three-stage convex formulas checked in official Firedrake demo, not a full original-paper audit
出版社の書誌とTVD Runge–Kuttaの抄録を確認。使う三段凸結合はFiredrake公式記述でも確認しました。原著全文の監査とは区別します。

- SciPy developers (n.d.). scipy.integrate.quad — SciPy v1.14.1 Manual [accessed 2026-11-23]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=official versioned API: QUADPACK integration, break points, epsabs/epsrel, reported error; use is evidenced by qualification receipts
版を固定した公式APIでQUADPACK、分割点、絶対・相対公差と推定誤差の意味を確認。解析的な円・多角形の面積計算とは異なる垂直断面求積を、実行記録付きで照合します。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Zalesak-type 2D rotation: conservation, bounds and shape error

Rotate a slotted disk through one full turn with an actual 2D finite-volume solver, comparing donor-cell and minmod MUSCL. Eight runs combine three grids with half-cell-center and 45-degree-start probes; measure conservation, bounds at every SSP stage, shape error and slot filling.

**Methods used**

- [Upwind finite differences](https://hrkoyama.github.io/numerical-methods-atlas/methods/upwind/?lang=en) (`upwind`)
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) (`muscl`)
- [Minmod](https://hrkoyama.github.io/numerical-methods-atlas/methods/minmod/?lang=en) (`minmod`)
- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) (`ssprk33`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-algorithm)

Use analytic divergence-free normal face averages and one shared upwind flux per interface. Both piecewise-constant donor-cell and mean-preserving directional-minmod MUSCL use SSPRK(3,3). The four face-midpoint mean equals the cell mean; individual outgoing-face Courant<=1/4 gives a convex FE update. Check the actual .20 bound at every stage. No transported-state clipping/floors or rejected/retried steps are used.

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

- [Two-dimensional rotational advection](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#rotational-advection-en) (`rotational-advection`)

Two-dimensional conservative transport of q with prescribed a=-omega(y-yc), b=omega(x-xc), whose divergence is zero. Shared face velocities and numerical fluxes update scalar cell means.


**Problem figure**

![Zalesak-type 2D rotation: conservation, bounds and shape error: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Zalesak-type slotted-disk rotation](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en) (`zalesak`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/zalesak/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/?lang=en#zalesak-rotation-en-validation)

Freeze26 unit checks and158 gates across eight fixed runs before execution. Retain min/max of every FE candidate/SSP convex mean, shared-flux mass budgets, reconstruction mean preservation and three-grid L1/Linf/relative-L2 errors. Independent circle/convex-polygon intersection means are qualified against SciPy vertical-slice quadrature, total area and first moments. Also check quarter/half/three-quarter-turn errors and centroids so a wrong direction or speed cannot hide behind a full-turn return.

- [Zalesak-type slotted disk: rigid rotation and geometric cell means](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-zalesak-rotation-en) (`zalesak-rotation`; Same-problem reference · Analytic reference)

Fix the disk and slot geometry and compare stored initial/returned cell means. Distinguish indicator point samples and a finer PDE calculation from this geometric reference.
## Assumptions, units and boundaries

Fix the dimensionless unit square, rotation center(.5,.5), disk center(.5,.75), radius.15, slot width.05/top y=.85, angular speed1, T=2pi and64²/128²/256² cells. The body is1 and exterior/slot0. Periodic normal face velocities match; the exact compact support stays away from the boundary. The periodic extension has a tangential-velocity seam, and diffusive tails reaching its fixed-width boundary band are measured.

**Editorial clarification**

This is scalar transport in a prescribed divergence-free rotation, not Euler-fluid evolution. It uses a Zalesak-type slotted-disk shape test without claiming implementation of Zalesak’s FCT algorithm. Pointwise indicator values and geometric conserved cell means are distinguished; numerical tails near periodic boundaries are also measured. The initial32²/64²/128² series passed26 tests and156/158 gates, but its finest relative L1 was about1.11675 for donor-cell(limit1.0) and.6023 for MUSCL(limit.55), so it failed. Retain all original inputs,criteria,fields and failed decisions. A new pre-execution contract refines the base series to64²/128²/256² without changing acceptance thresholds, flux algorithms or the26 tests. Revision 2 passed all 26 tests and all 158 gates over eight runs; tests plus the fixed-input driver took about 19.58 seconds within one 120-second budget. At N=256 the relative L1 errors are about 0.932256 for donor-cell and 0.394271 for MUSCL (ratio about 0.423); the maximum absolute mass change over all runs is about 8.90e-15. Recorded stage bounds are 0 to 1, including initial states, but bounds alone do not establish accurate slot preservation. The inner empty-slot probe weights the piecewise-constant cell-mean field; it is not a point value of the continuum solution. Mixed reference cells create a projection baseline, so numerical mean, reference mean and their excess are stored separately. At N=256 the excesses are about 0.63465 and 0.36501 for donor-cell/MUSCL, showing substantial remaining diffusion. At N=64 the MUSCL slot excess can exceed donor-cell, so no uniform improvement across every metric and grid is claimed. The N=256 mass fractions in the fixed-width 0.05 boundary band are about 0.0178615/0.000243761 for donor-cell/MUSCL. The compact exact field vanishes there; these periodic-boundary tails remain visible in the diagnostics.

## Adopted numerical method

Use analytic divergence-free normal face averages and one shared upwind flux per interface. Both piecewise-constant donor-cell and mean-preserving directional-minmod MUSCL use SSPRK(3,3). The four face-midpoint mean equals the cell mean; individual outgoing-face Courant<=1/4 gives a convex FE update. Check the actual .20 bound at every stage. No transported-state clipping/floors or rejected/retried steps are used.

$$
\partial_t q+\partial_x(uq)+\partial_y(vq)=0,\qquad (u,v)=(-(y-y_c),x-x_c),\quad T=2\pi
$$

$$
q(x,t)=q_0\!\left(c+R_{-t}(x-c)\right),\qquad \bar q_{ij}(t)=h^{-2}\int_{C_{ij}}q(x,t)\,dx\,dy
$$

$$
s_i=\operatorname{minmod}(q_i-q_{i-1},q_{i+1}-q_i),\quad q_i^{\pm}=\bar q_i\pm\tfrac12 s_i,\quad \bar q_{ij}=\tfrac14(q_L+q_R+q_D+q_U)
$$

$$
\widehat F_{i+1/2,j}=u_j^+q_{R,ij}+u_j^-q_{L,i+1,j},\qquad E_{\Delta t}(q)_{ij}=q_{ij}-\frac{\Delta t}{h}(\Delta_x\widehat F+\Delta_y\widehat G)_{ij}
$$

$$
q^{(1)}=E_{\Delta t}(q^n),\quad q^{(2)}=\tfrac34q^n+\tfrac14E_{\Delta t}(q^{(1)}),\quad q^{n+1}=\tfrac13q^n+\tfrac23E_{\Delta t}(q^{(2)})
$$

$$
\frac{\Delta t}{h}\max(|u|,|v|)\le\tfrac14,\quad D_h\!\cdot u=0\quad\Longrightarrow\quad 0\le E_{\Delta t}(\bar q)\le1\ \text{if all four face states lie in }[0,1]
$$

## References and validation

Freeze26 unit checks and158 gates across eight fixed runs before execution. Retain min/max of every FE candidate/SSP convex mean, shared-flux mass budgets, reconstruction mean preservation and three-grid L1/Linf/relative-L2 errors. Independent circle/convex-polygon intersection means are qualified against SciPy vertical-slice quadrature, total area and first moments. Also check quarter/half/three-quarter-turn errors and centroids so a wrong direction or speed cannot hide behind a full-turn return.

## Limits

This is an isolated0–1 standard slotted body with periodic boundaries. It does not implement Zalesak FCT, reproduce the original paper’s grid/boundaries or the entire Firedrake bell/cone/background demonstration. The inner-slot diagnostic area-weights piecewise-constant means over a fixed rectangle. Coarse exact cell projection can already give a nonzero baseline, which is reported separately from excess numerical filling. Two center/orientation probes do not establish universal isotropy, perfect shape retention or a maximum principle for arbitrary flows. Tiny geometric-area roundoff handling is distinguished from the absence of transported-state clipping.

## Stored measurements and decisions

```json
{
  "metrics": {
    "n": 256,
    "shift_cells": 0.0,
    "angle0": 0.0,
    "time": 6.283185307179586,
    "steps": 4008,
    "stages": 12024,
    "snapshots": 5,
    "relative_l1": 0.39427105204685026,
    "l1_absolute": 0.022954737845935866,
    "linf": 0.7430454904444476,
    "relative_l2": 0.3404884399563395,
    "initial_mass": 0.05822070305889007,
    "final_mass": 0.05822070305888117,
    "mass_change": -8.902600878712974e-15,
    "initial_area_error": 6.938893903907228e-18,
    "reference_area_error": 6.938893903907228e-18,
    "reference_return_maximum": 5.5067062021407764e-14,
    "minimum": 0.0,
    "maximum": 1.0,
    "maximum_courant": 0.2,
    "maximum_mean_preservation_defect": 1.1102230246251565e-16,
    "maximum_fe_mass_defect": 2.7755575615628914e-17,
    "maximum_rk_mass_defect": 8.902600878712974e-15,
    "maximum_discrete_divergence": 0.0,
    "slot_probe_mean": 0.36500692217705044,
    "slot_probe_reference_mean": 0.0,
    "slot_probe_excess": 0.36500692217705044,
    "slot_probe_weight_sum": 286.72000000000116,
    "boundary_band_width": 0.05,
    "boundary_band_mass_fraction": 0.00024376119280261055,
    "total_variation": 1.353666880236625,
    "state_clip_count": 0,
    "retries": 0,
    "rejected_steps": 0,
    "all_saved_values_finite": true
  },
  "checks": {
    "all eight fixed rotations completed": true,
    "base-donor-cell-n64: final time": true,
    "base-donor-cell-n64: initial represented area": true,
    "base-donor-cell-n64: periodic mass conservation": true,
    "base-donor-cell-n64: three FE records per SSP step": true,
    "base-donor-cell-n64: finite saved means and stage data": true,
    "base-donor-cell-n64: all stage lower bounds": true,
    "base-donor-cell-n64: all stage upper bounds": true,
    "base-donor-cell-n64: sufficient individual face Courant": true,
    "base-donor-cell-n64: four-face mean preserved": true,
    "base-donor-cell-n64: each FE shared-flux balance": true,
    "base-donor-cell-n64: each SSP convex-mean balance": true,
    "base-donor-cell-n64: all rotated reference areas": true,
    "base-donor-cell-n64: full-turn geometric return": true,
    "base-donor-cell-n64: zero clipping and retries": true,
    "base-donor-cell-n64: exact discrete velocity divergence": true,
    "base-donor-cell-n64: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n64: final time": true,
    "base-muscl-minmod-n64: initial represented area": true,
    "base-muscl-minmod-n64: periodic mass conservation": true,
    "base-muscl-minmod-n64: three FE records per SSP step": true,
    "base-muscl-minmod-n64: finite saved means and stage data": true,
    "base-muscl-minmod-n64: all stage lower bounds": true,
    "base-muscl-minmod-n64: all stage upper bounds": true,
    "base-muscl-minmod-n64: sufficient individual face Courant": true,
    "base-muscl-minmod-n64: four-face mean preserved": true,
    "base-muscl-minmod-n64: each FE shared-flux balance": true,
    "base-muscl-minmod-n64: each SSP convex-mean balance": true,
    "base-muscl-minmod-n64: all rotated reference areas": true,
    "base-muscl-minmod-n64: full-turn geometric return": true,
    "base-muscl-minmod-n64: zero clipping and retries": true,
    "base-muscl-minmod-n64: exact discrete velocity divergence": true,
    "base-muscl-minmod-n64: quarter-turn snapshots retained": true,
    "base-donor-cell-n128: final time": true,
    "base-donor-cell-n128: initial represented area": true,
    "base-donor-cell-n128: periodic mass conservation": true,
    "base-donor-cell-n128: three FE records per SSP step": true,
    "base-donor-cell-n128: finite saved means and stage data": true,
    "base-donor-cell-n128: all stage lower bounds": true,
    "base-donor-cell-n128: all stage upper bounds": true,
    "base-donor-cell-n128: sufficient individual face Courant": true,
    "base-donor-cell-n128: four-face mean preserved": true,
    "base-donor-cell-n128: each FE shared-flux balance": true,
    "base-donor-cell-n128: each SSP convex-mean balance": true,
    "base-donor-cell-n128: all rotated reference areas": true,
    "base-donor-cell-n128: full-turn geometric return": true,
    "base-donor-cell-n128: zero clipping and retries": true,
    "base-donor-cell-n128: exact discrete velocity divergence": true,
    "base-donor-cell-n128: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n128: final time": true,
    "base-muscl-minmod-n128: initial represented area": true,
    "base-muscl-minmod-n128: periodic mass conservation": true,
    "base-muscl-minmod-n128: three FE records per SSP step": true,
    "base-muscl-minmod-n128: finite saved means and stage data": true,
    "base-muscl-minmod-n128: all stage lower bounds": true,
    "base-muscl-minmod-n128: all stage upper bounds": true,
    "base-muscl-minmod-n128: sufficient individual face Courant": true,
    "base-muscl-minmod-n128: four-face mean preserved": true,
    "base-muscl-minmod-n128: each FE shared-flux balance": true,
    "base-muscl-minmod-n128: each SSP convex-mean balance": true,
    "base-muscl-minmod-n128: all rotated reference areas": true,
    "base-muscl-minmod-n128: full-turn geometric return": true,
    "base-muscl-minmod-n128: zero clipping and retries": true,
    "base-muscl-minmod-n128: exact discrete velocity divergence": true,
    "base-muscl-minmod-n128: quarter-turn snapshots retained": true,
    "base-donor-cell-n256: final time": true,
    "base-donor-cell-n256: initial represented area": true,
    "base-donor-cell-n256: periodic mass conservation": true,
    "base-donor-cell-n256: three FE records per SSP step": true,
    "base-donor-cell-n256: finite saved means and stage data": true,
    "base-donor-cell-n256: all stage lower bounds": true,
    "base-donor-cell-n256: all stage upper bounds": true,
    "base-donor-cell-n256: sufficient individual face Courant": true,
    "base-donor-cell-n256: four-face mean preserved": true,
    "base-donor-cell-n256: each FE shared-flux balance": true,
    "base-donor-cell-n256: each SSP convex-mean balance": true,
    "base-donor-cell-n256: all rotated reference areas": true,
    "base-donor-cell-n256: full-turn geometric return": true,
    "base-donor-cell-n256: zero clipping and retries": true,
    "base-donor-cell-n256: exact discrete velocity divergence": true,
    "base-donor-cell-n256: quarter-turn snapshots retained": true,
    "base-muscl-minmod-n256: final time": true,
    "base-muscl-minmod-n256: initial represented area": true,
    "base-muscl-minmod-n256: periodic mass conservation": true,
    "base-muscl-minmod-n256: three FE records per SSP step": true,
    "base-muscl-minmod-n256: finite saved means and stage data": true,
    "base-muscl-minmod-n256: all stage lower bounds": true,
    "base-muscl-minmod-n256: all stage upper bounds": true,
    "base-muscl-minmod-n256: sufficient individual face Courant": true,
    "base-muscl-minmod-n256: four-face mean preserved": true,
    "base-muscl-minmod-n256: each FE shared-flux balance": true,
    "base-muscl-minmod-n256: each SSP convex-mean balance": true,
    "base-muscl-minmod-n256: all rotated reference areas": true,
    "base-muscl-minmod-n256: full-turn geometric return": true,
    "base-muscl-minmod-n256: zero clipping and retries": true,
    "base-muscl-minmod-n256: exact discrete velocity divergence": true,
    "base-muscl-minmod-n256: quarter-turn snapshots retained": true,
    "half-cell-shift: final time": true,
    "half-cell-shift: initial represented area": true,
    "half-cell-shift: periodic mass conservation": true,
    "half-cell-shift: three FE records per SSP step": true,
    "half-cell-shift: finite saved means and stage data": true,
    "half-cell-shift: all stage lower bounds": true,
    "half-cell-shift: all stage upper bounds": true,
    "half-cell-shift: sufficient individual face Courant": true,
    "half-cell-shift: four-face mean preserved": true,
    "half-cell-shift: each FE shared-flux balance": true,
    "half-cell-shift: each SSP convex-mean balance": true,
    "half-cell-shift: all rotated reference areas": true,
    "half-cell-shift: full-turn geometric return": true,
    "half-cell-shift: zero clipping and retries": true,
    "half-cell-shift: exact discrete velocity divergence": true,
    "half-cell-shift: quarter-turn snapshots retained": true,
    "oblique-start: final time": true,
    "oblique-start: initial represented area": true,
    "oblique-start: periodic mass conservation": true,
    "oblique-start: three FE records per SSP step": true,
    "oblique-start: finite saved means and stage data": true,
    "oblique-start: all stage lower bounds": true,
    "oblique-start: all stage upper bounds": true,
    "oblique-start: sufficient individual face Courant": true,
    "oblique-start: four-face mean preserved": true,
    "oblique-start: each FE shared-flux balance": true,
    "oblique-start: each SSP convex-mean balance": true,
    "oblique-start: all rotated reference areas": true,
    "oblique-start: full-turn geometric return": true,
    "oblique-start: zero clipping and retries": true,
    "oblique-start: exact discrete velocity divergence": true,
    "oblique-start: quarter-turn snapshots retained": true,
    "donor-cell finest relative L1": true,
    "donor-cell refinement ratio 1": true,
    "donor-cell refinement ratio 2": true,
    "donor-cell intermediate relative L1 1": true,
    "donor-cell intermediate centroid distance 1": true,
    "donor-cell intermediate relative L1 2": true,
    "donor-cell intermediate centroid distance 2": true,
    "donor-cell intermediate relative L1 3": true,
    "donor-cell intermediate centroid distance 3": true,
    "muscl-minmod finest relative L1": true,
    "muscl-minmod refinement ratio 1": true,
    "muscl-minmod refinement ratio 2": true,
    "muscl-minmod intermediate relative L1 1": true,
    "muscl-minmod intermediate centroid distance 1": true,
    "muscl-minmod intermediate relative L1 2": true,
    "muscl-minmod intermediate centroid distance 2": true,
    "muscl-minmod intermediate relative L1 3": true,
    "muscl-minmod intermediate centroid distance 3": true,
    "finest MUSCL/donor relative L1": true,
    "half-cell-shift shape error": true,
    "oblique-start shape error": true,
    "independent geometry: analytic circle partitions conserve closed total area": true,
    "independent geometry: twelve fixed cut cells agree with independent vertical quadrature": true,
    "independent geometry: independent whole-area quadrature agrees with closed area": true,
    "independent geometry: true analytic centroid agrees with independent first moments": true,
    "independent geometry: full-turn geometric cell means return": true,
    "independent geometry: quarter-turn geometry has the correct counterclockwise orientation": true,
    "independent geometry: geometric fraction roundoff cleanup remains within its separate band": true,
    "independent geometry: analytic area cleanup remains within its dimensional floating-point band": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/zalesak-rotation/index.json

![Actual2D cell means after one full turn: analytic geometric reference, donor-cell and minmod MUSCL use a common color scale.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/zalesak-rotation-preview.png)

Actual2D cell means after one full turn: analytic geometric reference, donor-cell and minmod MUSCL use a common color scale.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/atlas-zalesak-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/zalesak/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- Steven T. Zalesak (1979). Fully multidimensional flux-corrected transport algorithms for fluids [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999179900512; review_level=publisher bibliography and abstract inspected; direct full-paper open returned403; original test geometry and boundary conditions not audited
Publisher record and abstract checked. The full original test geometry/grid/boundaries were not audited. This example does not implement or reproduce Zalesak FCT.

- Firedrake developers (n.d.). DG advection equation with upwinding [accessed 2026-11-23]. https://www.firedrakeproject.org/demos/DG_advection.py.html; review_level=official documentation equations and source lines46,63–92: disk(.5,.75),R.15,slot(.475,.525),y<.85,velocity(.5−y,x−.5),T2pi; SSP equations43–45 and135–143
Inspected official geometry, velocity, period and SSP formulas. The demo includes a bell, cone, background1, DQ1 elements and inflow1. This is an explicit isolated0–1 slotted-disk FV/periodic variant. No Firedrake software was executed or copied.

- Randall J. LeVeque (1996). High-Resolution Conservative Algorithms for Advection in Incompressible Flow [accessed 2026-11-23]. https://faculty.washington.edu/rjl/pubs/hiresadv/0733033.pdf; review_level=author-hosted paper selected sections1–3 actually inspected: PDE/incompressibility, FV means, minmod definition, donor-cell flux; no full-paper or numerical-table reproduction
Read sections1–3 on conservative transport, incompressibility, means, minmod and donor-cell fluxes. Firedrake cites this paper for its composite-shape test. Our MUSCL/SSPRK update is not the paper’s CTU/wave-propagation algorithm.

- Chi-Wang Shu and Stanley Osher (1988). Efficient implementation of essentially non-oscillatory shock-capturing schemes [accessed 2026-11-23]. https://www.sciencedirect.com/science/article/pii/0021999188901775; review_level=publisher bibliography/abstract inspected; actual three-stage convex formulas checked in official Firedrake demo, not a full original-paper audit
Publisher bibliography/abstract checked; the actual three-stage convex formulas were also inspected in the official Firedrake demo. The original full paper was not audited.

- SciPy developers (n.d.). scipy.integrate.quad — SciPy v1.14.1 Manual [accessed 2026-11-23]. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.quad.html; review_level=official versioned API: QUADPACK integration, break points, epsabs/epsrel, reported error; use is evidenced by qualification receipts
Versioned official API checked for QUADPACK, break points, tolerances and reported error. Independently integrated vertical sections are compared with circle/polygon areas; execution is established by saved receipts.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
