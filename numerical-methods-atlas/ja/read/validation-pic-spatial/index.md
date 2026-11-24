# PICの独立空間実装との照合

各kickで独立なCICと明示DFTから場を更新し、同じ時間積分の共有範囲を明示します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## PIC空間演算の独立実装照合

ベクトル化CIC/FFTと、別に書いた粒子ループCIC・密なDFTを、それぞれが自己無撞着な場を毎kick計算する軌道全体で照合します。

**使用手法**

- [Particle-in-Cell（PIC）](https://hrkoyama.github.io/numerical-methods-atlas/methods/pic/?lang=ja) (`pic`)
- [Cloud-in-cellの割当てと補間](https://hrkoyama.github.io/numerical-methods-atlas/methods/cic/?lang=ja) (`cic`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-algorithm)

独立側はPythonスカラー配置、明示的な複素DFT和、独自の補間ループを所有します。主側のFFT・配置・補間を呼びません。数学上のCIC、Nyquist規約、velocity-Verlet法、初期配列は共通です。

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

- [静電Vlasov–Poisson方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#vlasov-poisson-ja) (`vlasov-poisson`)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。


**問題の図**

![PIC空間演算の独立実装照合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[CIC静電PICの冷たいプラズマ振動](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja) (`cold-plasma-pic`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/cold-plasma-pic/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/?lang=ja#pic-independent-spatial-ja-validation)

19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。

- [PIC空間演算の独立実装照合](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pic-independent-spatial-ja) (`pic-independent-spatial`; 関連モデルの参照 · 有限格子の数値参照)

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。
### 前提・単位・境界

周期[0,2π]、256粒子、格子8/16/32、シード35001/35002、dt=.02、T=.24。位置は一様乱数、v=.2 Normal+.1 sin x。6組は別々に進めた12軌道です。

**編集上の補足**

離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。

### 採用した計算法

独立側はPythonスカラー配置、明示的な複素DFT和、独自の補間ループを所有します。主側のFFT・配置・補間を呼びません。数学上のCIC、Nyquist規約、velocity-Verlet法、初期配列は共通です。

$$
\rho_j=1-\frac1h\sum_p w_p S_j(x_p),\quad a_p=-\sum_j S_j(x_p)E_j
$$

$$
\widehat E_m=\widehat\rho_m/(ik_m),\quad E_0=0,\quad E_{N/2}=0\ \text{(even N)}
$$

$$
\rho=-\tfrac12\cos2x\ \Longrightarrow\ E=-\tfrac14\sin2x,\quad a=+\tfrac14\sin2x
$$

### 比較・検証

19 pytestと58/58固定判定が合格。6組＝12の自己無撞着軌道を13時刻全てで照合し、最大差は位置8.88e−16・速度3.33e−16・電場8.33e−16・電荷2.89e−15。pytest+mainは0.392秒。最初の小pytestは周期端点の添字不具合で17/18となり、元記録を保持して修正後に全計算を実行しました。

### 確認の限界

離散演算の独立したコーディング照合です。時間積分法や連続方程式を変えた独立エンジン、連続極限の収束、冷たいプラズマの振動参照の再現を意味しません。既存cold-plasma-picの関連補助検証として扱い、温かい初期速度の軌道を冷たい解と同一視しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "comparison_pairs": 6,
    "separate_trajectories": 12,
    "saved_states_per_trajectory": 13,
    "maximum_position_discrepancy": 8.881784197001252e-16,
    "maximum_velocity_discrepancy": 3.3306690738754696e-16,
    "maximum_field_discrepancy": 8.326672684688674e-16,
    "maximum_charge_discrepancy": 2.886579864025407e-15
  },
  "checks": {
    "primary analytic charge field electron-sign fixture": true,
    "independent analytic charge field electron-sign fixture": true,
    "deliberate wrong electron sign is detected": true,
    "odd-grid force": true,
    "odd-grid field": true,
    "odd-grid charge": true,
    "positive-weight force": true,
    "positive-weight field": true,
    "positive-weight charge": true,
    "n8-seed35001 all saved arrays finite": true,
    "n8-seed35001 all-step position": true,
    "n8-seed35001 all-step velocity": true,
    "n8-seed35001 all-step field": true,
    "n8-seed35001 all-step charge": true,
    "n8-seed35001 independent charge conservation": true,
    "n8-seed35001 independent momentum conservation": true,
    "n8-seed35001 own fields at every fixed kick": true,
    "n8-seed35002 all saved arrays finite": true,
    "n8-seed35002 all-step position": true,
    "n8-seed35002 all-step velocity": true,
    "n8-seed35002 all-step field": true,
    "n8-seed35002 all-step charge": true,
    "n8-seed35002 independent charge conservation": true,
    "n8-seed35002 independent momentum conservation": true,
    "n8-seed35002 own fields at every fixed kick": true,
    "n16-seed35001 all saved arrays finite": true,
    "n16-seed35001 all-step position": true,
    "n16-seed35001 all-step velocity": true,
    "n16-seed35001 all-step field": true,
    "n16-seed35001 all-step charge": true,
    "n16-seed35001 independent charge conservation": true,
    "n16-seed35001 independent momentum conservation": true,
    "n16-seed35001 own fields at every fixed kick": true,
    "n16-seed35002 all saved arrays finite": true,
    "n16-seed35002 all-step position": true,
    "n16-seed35002 all-step velocity": true,
    "n16-seed35002 all-step field": true,
    "n16-seed35002 all-step charge": true,
    "n16-seed35002 independent charge conservation": true,
    "n16-seed35002 independent momentum conservation": true,
    "n16-seed35002 own fields at every fixed kick": true,
    "n32-seed35001 all saved arrays finite": true,
    "n32-seed35001 all-step position": true,
    "n32-seed35001 all-step velocity": true,
    "n32-seed35001 all-step field": true,
    "n32-seed35001 all-step charge": true,
    "n32-seed35001 independent charge conservation": true,
    "n32-seed35001 independent momentum conservation": true,
    "n32-seed35001 own fields at every fixed kick": true,
    "n32-seed35002 all saved arrays finite": true,
    "n32-seed35002 all-step position": true,
    "n32-seed35002 all-step velocity": true,
    "n32-seed35002 all-step field": true,
    "n32-seed35002 all-step charge": true,
    "n32-seed35002 independent charge conservation": true,
    "n32-seed35002 independent momentum conservation": true,
    "n32-seed35002 own fields at every fixed kick": true,
    "six paired comparisons equal twelve separate trajectories": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/pic-independent-spatial/index.json

![12独立軌道の1つから保存した実際の位相空間。色は自己無撞着電場による速度変化です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/pic-independent-spatial-preview.png)

12独立軌道の1つから保存した実際の位相空間。色は自己無撞着電場による速度変化です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/atlas-pic-spatial-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/pic-spatial/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Enrico Camporeale, Gian Luca Delzanno, Benjamin K. Bergen and J. David Moulton (2013). On the velocity space discretization for the Vlasov–Poisson system: comparison between Hermite spectral and Particle-in-Cell methods. Part 1: semi-implicit scheme [accessed 2026-11-23]. https://arxiv.org/abs/1311.2098; review_level=primary-selected-original-pdf-text
原著の規格化方程式、再帰・雑音、Landauと二流の線形窓の議論を選択して確認。原著の計算値は転用しません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
