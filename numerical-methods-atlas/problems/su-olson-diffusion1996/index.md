# Su–Olson1996非平衡拡散 / Su–Olson1996 non-equilibrium diffusion

https://hrkoyama.github.io/numerical-methods-atlas/problems/su-olson-diffusion1996/

## 日本語

[保存した実計算場の科学プレビュー。](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-radiation-matter/#su-olson-diffusion1996) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#su-olson-diffusion1996)

### 方程式・問題の定義

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。

#### [Su–Olson1996の非平衡拡散・物質交換](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#non-equilibrium-diffusion-exchange-ja)

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u-\frac{2}{\sqrt3}u_x=1\ (x=0),\quad \epsilon u+v\ \mathrm{is\ the\ weighted\ energy}
$$

x=√3κz。1997輸送のx=κzとは規格化も境界・参照も分けます。非単位epsilonの閉セル検査を別に行います。

#### Su–Olson1996非平衡拡散

補助実行例 · 実行例の定義・検証式

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

### 厳密解・参照解

独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。

#### [Su–Olson1996拡散：固定版の独立積分評価関数](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja#su-olson-diffusion1996-ja-measurements)

半解析解 · 同じ問題の参照

epsilon*u_tau-u_xx=v-u; v_tau=u-v; u(0,tau)-2/sqrt(3)*u_x(0,tau)=1; u(infinity,tau)=0; epsilon*u+v is the capacity-weighted total.

初期の輻射・物質変数が0、ε=1の半無限Marshak拡散です。無次元評価関数を直接用い、物理単位の質量吸収係数ラッパーに起因する曖昧な規約は持ち込みません。

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

#### Su–Olson1996非平衡拡散

独立参照54項目を輸送ケースと共有して資格済み。5主計算で独立u/v誤差、全stepの容量重み収支・正値、時間・有限領域差を分離します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja)

### 計算法

保存的FVと後退Euler。輻射物質の反対sourceを同じSchur補元で結合し、Robinのβ+h/2半セル抵抗を用います。ε.25/2の同じ交換operatorも解析検査します。

- [輻射輸送・モーメント法](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [後退Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Su–Olson1996非平衡拡散](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=ja)

補助実行例

実際の輻射・物質2場とMarshak境界を進め、固定版ExactPackの独立積分参照と比較します。

無次元ε1、区間[0,16]、初期u=v0、左Robin入射、右0。128/256/512セルと時間半減・区間24probe。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1996拡散であり1997角度輸送とは別です。原典本文は未読、公式ソフトの選択値を資格。物理単位の質量opacity解釈は使わず無次元関数を直接参照します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)

## English

[Scientific preview from the actual saved numerical fields.](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/su-olson-diffusion1996-preview.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-radiation-matter/#su-olson-diffusion1996) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#su-olson-diffusion1996-en)

### Equations and problem definitions

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.

#### [Su–Olson1996 non-equilibrium diffusion and material exchange](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#non-equilibrium-diffusion-exchange-en)

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u-\frac{2}{\sqrt3}u_x=1\ (x=0),\quad \epsilon u+v\ \mathrm{is\ the\ weighted\ energy}
$$

x=sqrt(3)kappa*z,distinct from x=kappa*z in1997 transport. Boundary data and references remain separate; non-unit-epsilon closed cells are separate controls.

#### Su–Olson1996 non-equilibrium diffusion

Supplementary execution example · Example definition or validation formula

$$
\epsilon u_\tau-u_{xx}=v-u,\quad v_\tau=u-v
$$

$$
u(0,\tau)-\frac2{\sqrt3}u_x(0,\tau)=1
$$

$$
\epsilon=4a/\alpha,\quad e_m/E_0=v/\epsilon,\quad \mathcal E=\epsilon u+v
$$

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

### Exact and reference solutions

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

#### [Su–Olson1996 diffusion: pinned independent integral evaluator](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en#su-olson-diffusion1996-en-measurements)

Semi-analytic reference · Reference for the same problem

epsilon*u_tau-u_xx=v-u; v_tau=u-v; u(0,tau)-2/sqrt(3)*u_x(0,tau)=1; u(infinity,tau)=0; epsilon*u+v is the capacity-weighted total.

Half-space Marshak diffusion with zero initial radiation/material variables and epsilon1. Direct dimensionless evaluator; no ambiguous physical mass-opacity wrapper convention.

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

#### Su–Olson1996 non-equilibrium diffusion

The independent54check reference study is shared with transport. Five primary runs separate u/vreferenceerror,all-step capacity-weighted budgets/positivity,time and finite-domain sensitivity.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en)

### Numerical methods

Conservative FV/backwardEuler with opposite exchange sources coupled by a shared Schur complement and Robin half-cell resistance beta+h/2. Analytic nonunitepsilon.25/2controls exercise the same exchange operators.

- [Radiation transport and moment methods](https://hrkoyama.github.io/numerical-methods-atlas/methods/radiation-transport/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Backward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Su–Olson1996 non-equilibrium diffusion](https://hrkoyama.github.io/numerical-methods-atlas/validation/su-olson-diffusion1996/?lang=en)

Supplementary execution example

Advance actual radiation/material fields with the Marshak boundary and compare with independently qualified pinned ExactPack integrals.

Nondimensionalepsilon1,x0..16,initialu=v0,leftRobin inflow/right0;128/256/512cells plus half-step/domain24probes.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/atlas-radiation-matter-2026-11-24-r2.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This1996diffusion model is distinct from1997angular transport. Original paper fulltext unread;officialsoftware selected values qualified. Direct dimensionless functions avoid ambiguous mass-opacity physical-wrapper units.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-24-r2/radiation-matter/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/run.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/diffusion.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_matter.py)
- [/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py](https://hrkoyama.github.io/code/validated-examples/2026-11-24-r2/radiation-matter/test_thick_limit.py)
