# 3Dの1/r核：展開・木・力の検証

真の3D展開でM2M・M2L・L2Lを通った非零の最終寄与と一意な相互作用割当てを確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 真3D 1/r FMM：多段変換・力・適応所有権

非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。

**使用手法**

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) (`fmm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-algorithm)

P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

- [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja) (`particle-gravity`)

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。


**問題の図**

![真3D 1/r FMM：多段変換・力・適応所有権：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja) (`fmm3d-inverse-r`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-validation)

有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。

- [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fmm3d-inverse-r-ja) (`fmm3d-inverse-r`; 同じ問題の参照 · 有限格子の数値参照)

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。
### 前提・単位・境界

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。

**編集上の補足**

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

### 採用した計算法

P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

### 比較・検証

有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。

### 確認の限界

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_potential_error": 2.8255260194168475e-09,
    "finest_acceleration_error": 3.9236249160985455e-07,
    "primary_runs": 6,
    "additional_fixed_evaluations": 2
  },
  "checks": {
    "p3-d2 finite potential and force": true,
    "p3-d2 exact interaction ownership": true,
    "p3-d2 far path exercised": true,
    "p3-d2 actual forced depth": true,
    "p5-d2 finite potential and force": true,
    "p5-d2 exact interaction ownership": true,
    "p5-d2 far path exercised": true,
    "p5-d2 actual forced depth": true,
    "p7-d2 finite potential and force": true,
    "p7-d2 exact interaction ownership": true,
    "p7-d2 far path exercised": true,
    "p7-d2 actual forced depth": true,
    "p3-d3 finite potential and force": true,
    "p3-d3 exact interaction ownership": true,
    "p3-d3 far path exercised": true,
    "p3-d3 actual forced depth": true,
    "p3-d3 nonzero complete translation chain": true,
    "p5-d3 finite potential and force": true,
    "p5-d3 exact interaction ownership": true,
    "p5-d3 far path exercised": true,
    "p5-d3 actual forced depth": true,
    "p5-d3 nonzero complete translation chain": true,
    "p7-d3 finite potential and force": true,
    "p7-d3 exact interaction ownership": true,
    "p7-d3 far path exercised": true,
    "p7-d3 actual forced depth": true,
    "p7-d3 nonzero complete translation chain": true,
    "adaptive finite fields": true,
    "adaptive exact ownership": true,
    "adaptive far path": true,
    "adaptive unequal actual levels": true,
    "adaptive capped bucket retained": true,
    "adaptive potential accuracy": true,
    "adaptive force accuracy": true,
    "d2 finest potential_error": true,
    "d2 order refinement potential_error": true,
    "d2 finest acceleration_error": true,
    "d2 order refinement acceleration_error": true,
    "d3 finest potential_error": true,
    "d3 order refinement potential_error": true,
    "d3 finest acceleration_error": true,
    "d3 order refinement acceleration_error": true,
    "direct octahedron potential golden": true,
    "direct octahedron acceleration golden": true,
    "rigid transformed potential": true,
    "rigid transformed acceleration": true,
    "rigid transformed ownership": true,
    "rigid transformed actual level": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/index.json

![固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

固定入力を実際に計算した保存配列からの検証図。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- The black-box fast multipole method. https://mc.stanford.edu/cgi-bin/images/f/fa/Darve_bbfmm_2009.pdf; review_level=primary-selected-sections
Tensor interpolation Eq7 and multilevel stages sections2–3 inspected, printed8715–8717; compression is separate. Original uncompressed educational implementation here, no timing reproduction.

- FMM3D mathematical definitions. https://fmm3d.readthedocs.io/en/latest/math.html; review_level=official-kernel-normalization
Official potential+1/(4pi r), gradient and source-self convention inspected. Our gravitational kernel is-1/r; FMM3D is not installed or run.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
