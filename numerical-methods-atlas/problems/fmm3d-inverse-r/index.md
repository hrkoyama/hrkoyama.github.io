# 真3D 1/r FMM：多段変換・力・適応所有権 / Actual3D1/r FMM: multilevel translations, force and ownership

https://hrkoyama.github.io/numerical-methods-atlas/problems/fmm3d-inverse-r/

## 日本語

[固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-fmm3d/#fmm3d-inverse-r) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#fmm3d-inverse-r)

### 方程式・問題の定義

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。

#### [重力粒子モデル](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#particle-gravity-ja)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

孤立系のPlummer軟化力と、周期・平均密度除去のPoisson式は異なる境界問題です。公開例は静的な力と境界核の検証で、自己重力流体の時間発展ではありません。

#### 真3D 1/r FMM：多段変換・力・適応所有権

補助実行例 · 実行例の定義・検証式

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。

### 厳密解・参照解

有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。

#### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja#fmm3d-inverse-r-ja-measurements)

有限格子の数値参照 · 同じ問題の参照

Phi_i=-sum_{j!=i}G*m_j/r_ij; a_i=-sum_{j!=i}G*m_j*(x_i-x_j)/r_ij^3; finite6axis source Phi(0)=-1/a.

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。 有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。 小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

#### 真3D 1/r FMM：多段変換・力・適応所有権

有限6点閉形式、独立Cartesian直接和、次数/実深さ、混合深さ・cap粒子保持、剛体変換を別確認。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja)

### 計算法

P2M/M2M/M2L/L2Lと局所基底の物理勾配、近接P2P。全非自己対を一意に割当て、非零の全変換経路を記録。

- [高速多重極法の移動演算](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [真3D 1/r FMM：多段変換・力・適応所有権](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=ja)

補助実行例

非圧縮Chebyshev FMMを真の葉レベル2/3と別の適応配置で実行し、独立直接和のポテンシャル・加速度と比較します。

孤立重力-Gm/r、G1、64等質量、p3/5/7。主木は深さ強制、適応木のみcapacity8/maxdepth3。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

小Nの非圧縮教材。p^6 M2Lコストを保存し、SVD圧縮・球調和・Nスケーリング・運動量厳密保存は主張しません。 有限6点閉形式は独立directの資格確認で、FMM本体のgolden-target実行ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/fmm3d/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/run.py)
- [/code/validated-examples/2026-11-23/fmm3d/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/fmm.py)
- [/code/validated-examples/2026-11-23/fmm3d/references/direct.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/references/direct.py)
- [/code/validated-examples/2026-11-23/fmm3d/test_fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/test_fmm.py)

## English

[Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/fmm3d-inverse-r-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-fmm3d/#fmm3d-inverse-r) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#fmm3d-inverse-r-en)

### Equations and problem definitions

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

#### [Gravitational particle model](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#particle-gravity-en)

$$
\boldsymbol a_i=-G\sum_{j\ne i}m_j\frac{\boldsymbol x_i-\boldsymbol x_j}{(|\boldsymbol x_i-\boldsymbol x_j|^2+\epsilon^2)^{3/2}}
$$

$$
\nabla^2\phi=4\pi G(\rho-\overline\rho)\quad\text{(periodic)}
$$

Isolated Plummer-softened forces and periodic mean-subtracted Poisson are distinct boundary problems. Public examples check static forces and kernels, not coupled self-gravitating flow evolution.

#### Actual3D1/r FMM: multilevel translations, force and ownership

Supplementary execution example · Example definition or validation formula

$$
\Phi_i=-G\sum_{j\ne i}m_j/r_{ij},\quad a_i=-\nabla\Phi_i
$$

$$
K(x,y)\approx\sum_{\ell,m}L_\ell(x)K(x_\ell,y_m)L_m(y)
$$

$$
m=p^3,\quad {\rm dense\ M2L\ entries}=p^6
$$

Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.

### Exact and reference solutions

Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.

#### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en#fmm3d-inverse-r-en-measurements)

Finite-grid numerical reference · Reference for the same problem

Phi_i=-sum_{j!=i}G*m_j/r_ij; a_i=-sum_{j!=i}G*m_j*(x_i-x_j)/r_ij^3; finite6axis source Phi(0)=-1/a.

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

#### Actual3D1/r FMM: multilevel translations, force and ownership

Separate finite6source exact goldens, independent Cartesian sums, order/actual-depth comparisons, mixed-depth capped ownership and rigid transformation.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en)

### Numerical methods

Actual upward/downward translations, physical local-basis gradients and near P2P; audit unique nonself ownership and nonzero complete translation contributions.

- [Fast multipole translations](https://hrkoyama.github.io/numerical-methods-atlas/methods/fmm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Actual3D1/r FMM: multilevel translations, force and ownership](https://hrkoyama.github.io/numerical-methods-atlas/validation/fmm3d-inverse-r/?lang=en)

Supplementary execution example

Run uncompressed Chebyshev FMM at actual leaf levels2/3 and a separate adaptive configuration; compare independent direct potentials and accelerations.

Isolated-Gm/r,G1,64equal masses,p3/5/7. Main levels forced; adaptive case alone usescapacity8/maxdepth3.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/atlas-fmm3d-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Small-N uncompressed teaching example; reportp^6M2L cost. No SVD/spherical-harmonic/scaling or exact momentum-conservation claim. The finite6source exact probe qualifies the direct reference, not a production-FMM golden-target run.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/fmm3d/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/run.py)
- [/code/validated-examples/2026-11-23/fmm3d/fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/fmm.py)
- [/code/validated-examples/2026-11-23/fmm3d/references/direct.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/references/direct.py)
- [/code/validated-examples/2026-11-23/fmm3d/test_fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/fmm3d/test_fmm.py)
