# 中性長方形スラブ：真2P参照とYB補正 / Neutral rectangular slab: genuine2P reference and YB

https://hrkoyama.github.io/numerical-methods-atlas/problems/neutral-slab-yb/

## 日本語

[固定入力を実際に計算した保存配列からの検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-slab-ewald/#neutral-slab-yb) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#neutral-slab-yb)

### 方程式・問題の定義

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。

#### [Coulomb静電場と混合周期境界](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#coulomb-electrostatics-ja)

$$
\phi(\boldsymbol r)=\sum_j\sum_{\boldsymbol n}^{\prime}\frac{q_j}{|\boldsymbol r-\boldsymbol r_j+\boldsymbol L\boldsymbol n|},\quad\boldsymbol F_i=-q_i\nabla\phi_i
$$

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V,\quad M_z=\sum_iq_iz_i
$$

中性系・Coulomb定数1。真の2周期の参照と、有限真空厚の3周期＋補正を区別します。

#### 中性長方形スラブ：真2P参照とYB補正

補助実行例 · 実行例の定義・検証式

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。

### 厳密解・参照解

参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。

#### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja#neutral-slab-yb-ja-measurements)

半解析解 · 同じ問題の参照

phi=real2P+nonzero_modes+zero_mode-2alpha*q/sqrt(pi); E=.5sum(q*phi); F=-q grad(phi); DeltaE=2pi*Mz^2/V; DeltaFz=-4pi*q*Mz/V.

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。 参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。 中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

#### 中性長方形スラブ：真2P参照とYB補正

参照alpha/打切り資格、エネルギー差分、真空厚、全力、零モード負対照・遠方ゲージと中性平行移動を分離。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja)

### 計算法

全±3D波数、自己項、2pi Mz²/Vとその力。独立2Pには横零モード・自己減算と安定exp–erfcを保持。

- [Ewald法](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [スラブ静電場と2次元周期Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [中性長方形スラブ：真2P参照とYB補正](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=ja)

補助実行例

4電荷の長方形3P Ewaldに中性スラブ補正を加え、別実装の真2P和のエネルギー・全力成分と照合します。

Coulomb定数1、Lx1,Ly1.25、Lz1.5/3/6、4電荷±1、非周期zのMz=.34、alpha3/4。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

中性・固定4電荷・Cartesian z法線のみ。YBは有限ギャップ近似で任意真空の厳密2Pではありません。原著YB本文は未読。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/slab-ewald/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/run.py)
- [/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py)
- [/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py)
- [/code/validated-examples/2026-11-23/slab-ewald/test_slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/test_slab.py)

## English

[Validation figure from actual saved fixed-input calculation arrays.](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/neutral-slab-yb-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-slab-ewald/#neutral-slab-yb) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#neutral-slab-yb-en)

### Equations and problem definitions

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

#### [Coulomb electrostatics with mixed periodic boundaries](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#coulomb-electrostatics-en)

$$
\phi(\boldsymbol r)=\sum_j\sum_{\boldsymbol n}^{\prime}\frac{q_j}{|\boldsymbol r-\boldsymbol r_j+\boldsymbol L\boldsymbol n|},\quad\boldsymbol F_i=-q_i\nabla\phi_i
$$

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V,\quad M_z=\sum_iq_iz_i
$$

Neutral system,Coulomb constant1. Distinguish genuine2P references from finite-vacuum3P plus correction.

#### Neutral rectangular slab: genuine2P reference and YB

Supplementary execution example · Example definition or validation formula

$$
E_{\rm YB}=E_{3P}+2\pi M_z^2/V
$$

$$
\Delta F_{zi}=-4\pi q_iM_z/V
$$

$$
\phi(\pm\infty)=\pm2\pi M_z/(L_xL_y)
$$

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.

### Exact and reference solutions

Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.

#### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en#neutral-slab-yb-en-measurements)

Semi-analytic reference · Reference for the same problem

phi=real2P+nonzero_modes+zero_mode-2alpha*q/sqrt(pi); E=.5sum(q*phi); F=-q grad(phi); DeltaE=2pi*Mz^2/V; DeltaFz=-4pi*q*Mz/V.

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

#### Neutral rectangular slab: genuine2P reference and YB

Separate reference cutoff/splitting qualification, energy gradients, vacuum error, all forces, zero-mode control/far gauge and neutral translations.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en)

### Numerical methods

Full±3D reciprocal sum/self term and2pi Mz²/V correction; independent2P retains zero/self terms and stable exp-erfc evaluation.

- [Ewald summation](https://hrkoyama.github.io/numerical-methods-atlas/methods/ewald/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Slab electrostatics and 2D-periodic Ewald](https://hrkoyama.github.io/numerical-methods-atlas/methods/slab-ewald/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Neutral rectangular slab: genuine2P reference and YB](https://hrkoyama.github.io/numerical-methods-atlas/validation/neutral-slab-yb/?lang=en)

Supplementary execution example

Compare corrected orthorhombic3P Ewald energy/all forces against a separately implemented genuine2P series.

Coulomb1, lateral1×1.25, extendedLz1.5/3/6,4neutral charges±1,physical-z dipole.34 andalpha3/4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/atlas-slab-ewald-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Neutral fixed4charge Cartesian-z slab only. YB is a finite-gap approximation, not exact2P at arbitrary vacuum. Original Yeh full text not inspected.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/slab-ewald/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/run.py)
- [/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/electrostatics.py)
- [/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/references/twoperiodic.py)
- [/code/validated-examples/2026-11-23/slab-ewald/test_slab.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/slab-ewald/test_slab.py)
