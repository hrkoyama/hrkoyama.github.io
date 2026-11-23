# 中性スラブ：3周期補正と真の2周期参照

長方形の周期箱と非周期zの分枝を固定し、Yeh–Berkowitz補正を真の2周期の自己項・零モード込みの参照と照合します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 中性長方形スラブ：真2P参照とYB補正

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。

**使用手法**

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) (`ewald`)
- [スラブ静電場と2次元周期Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=ja) (`slab-ewald`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-algorithm)

全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

- [Coulomb静電場と混合周期境界](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja) (`coulomb-electrostatics`)

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。


**問題の図**

![中性長方形スラブ：真2P参照とYB補正：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja) (`neutral-slab-yb`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-validation)

参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。

- [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-neutral-slab-yb-ja) (`neutral-slab-yb`; 同じ問題の参照 · 半解析参照)

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。
### 前提・単位・境界

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。

**編集上の補足**

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

### 採用した計算法

全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

### 比較・検証

参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。

### 確認の限界

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_energy": -4.45950558164492,
    "maximum_reference_force": 5.484895963941495,
    "dipole_z": 0.33999999999999997,
    "finest_energy_error": 4.618527782440651e-14,
    "finest_force_error": 1.0009770790020411e-12
  },
  "checks": {
    "reference splitting energy": true,
    "reference splitting force": true,
    "reference cutoff energy": true,
    "reference cutoff force": true,
    "z1.5-a3 finite saved fields": true,
    "z1.5-a3 neutral net force": true,
    "z1.5-a4 finite saved fields": true,
    "z1.5-a4 neutral net force": true,
    "z3-a3 finite saved fields": true,
    "z3-a3 neutral net force": true,
    "z3-a4 finite saved fields": true,
    "z3-a4 neutral net force": true,
    "z6-a3 finite saved fields": true,
    "z6-a3 neutral net force": true,
    "z6-a4 finite saved fields": true,
    "z6-a4 neutral net force": true,
    "z1.5 alpha energy": true,
    "z1.5 alpha force": true,
    "z3 alpha energy": true,
    "z3 alpha force": true,
    "z6 alpha energy": true,
    "z6 alpha force": true,
    "z6-a3 finest energy": true,
    "z6-a3 finest force": true,
    "z6-a3 correction improves energy": true,
    "z6-a3 correction improves force": true,
    "z6-a4 finest energy": true,
    "z6-a4 finest force": true,
    "z6-a4 correction improves energy": true,
    "z6-a4 correction improves force": true,
    "neutral translation energy": true,
    "neutral translation force": true,
    "production energy gradient h1e-05": true,
    "reference energy gradient h1e-05": true,
    "production energy gradient h5e-06": true,
    "reference energy gradient h5e-06": true,
    "omitted zero mode is detected": true,
    "far-z potential step": true,
    "far-z zero field": true,
    "source permutation energy": true,
    "source permutation force": true,
    "charged cell rejected": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/index.json

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

固定入力を実際に計算した保存配列からの検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Fast and spectrally accurate Ewald summation for2-periodic electrostatic systems. https://arxiv.org/pdf/1109.1667; review_level=primary-selected-equations
Eq4 and AppendixA Eq41/zero-mode inspected; rendered selected pages requested. No full-paper audit or spectral-PME implementation claimed.

- Ewald summation for systems with slab geometry. https://doi.org/10.1063/1.479595; review_level=bibliography-original-unaccessed
Original publisher full text unavailable; no original-text review claimed. Neutral correction independently derived and checked against official LAMMPS implementation/documentation.

- LAMMPS slab Ewald documentation and neutral correction. https://docs.lammps.org/kspace_modify.html; review_level=official-selected-docs-and-formulas
Slab geometry restrictions and official Ewald::slabcorr neutral formula inspected. No LAMMPS code copied or executed; mutable stable source is contextual, not a numerical dependency.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
