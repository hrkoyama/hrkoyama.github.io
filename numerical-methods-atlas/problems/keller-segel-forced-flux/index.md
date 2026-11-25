# Keller–Segel：連成流束の製造解 / Keller–Segel: a manufactured coupled-flux solution

https://hrkoyama.github.io/numerical-methods-atlas/problems/keller-segel-forced-flux/

## 日本語

[滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。 著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-biology-space-controls/#keller-segel-forced-flux) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#keller-segel-forced-flux)

### 方程式・問題の定義

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

#### [Keller–Segel走化性](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-keller-segel-ja)

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

細胞密度が化学物質の勾配に応答する2場の代表的な縮約系。次元・境界・化学場の動態が重要です。 全モデル族の実装ではありません。今回の固定例：Keller–Segel：連成流束の製造解

#### [外力・移流付きKeller–Segel製造問題](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-keller-segel-model-ja)

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

$$
n_*=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y)
$$

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

#### Keller–Segel：連成流束の製造解

補助実行例 · 実行例の定義・検証式

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

### 厳密解・参照解

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

#### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja#keller-segel-forced-flux-ja-measurements)

製造解 · 同じ問題の参照

n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n;\quad \tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c;\quad n_*(x,y,t)=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*(x,y,t)=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y),\quad\psi=\sin(\pi x)\sin(\pi y)/\pi,\quad w=(\partial_y\psi,-\partial_x\psi)

単位正方形でT=0.25まで、n=1+0.1e⁻ᵗcos(πx)cos(πy)、c=1+0.05e⁻²ᵗcos(πx)cos(2πy)に対応する外力を製造し、発散零で境界に接する移流を用います。無次元の係数と外力をinputs.jsonに固定。内面・角の所有を明示して製造外力と境界流束を扱います。

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

#### Keller–Segel：連成流束の製造解

36点の源項、96セル状態ベクトル、符号・欠落連成・古い段・面重複の負例を検査。空間・同一MOL時間・正値性・実際の段収支を分けて保存します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja)

### 計算法

セル平均の中心面流束とSSPRK3を使い、n/c/強制項を同じ段に揃えます。展開した三角多項式の積分を、別の未展開積分とスカラー面ループ参照で確認します。

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Keller–Segel：連成流束の製造解](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=ja)

補助実行例

滑らかな2D厳密場で、交差流束・段時刻・収支を検証します。

単位正方形、T=0.25。n=1+0.1e⁻ᵗcosπx cosπy、c=1+0.05e⁻²ᵗcosπx cos2πyに合う強制項と接線方向の発散ゼロ移流を与えます。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

著者作成の強制2場モデルです。原著の全生物モデル、ピーク形成、真のblow-upやその抑制を実証しません。負値をクリップして正値性を装いません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)

## English

[Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers. This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/keller-segel-forced-flux.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-biology-space-controls/#keller-segel-forced-flux) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#keller-segel-forced-flux-en)

### Equations and problem definitions

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

#### [Keller–Segel chemotaxis](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-keller-segel-en)

$$
n_t=D_n\Delta n-\chi\nabla\cdot(n\nabla c)
$$

$$
\tau_c c_t=D_c\Delta c+\alpha n-\lambda c
$$

Cell density n drifts up a chemoattractant gradient; τc=0 gives an elliptic chemical subproblem. This is a common two-field reduction of a more detailed original formulation. Blowup thresholds depend on dimension, domain, boundary and chemical dynamics. Not implementation of the entire model family. Fixed cases: Keller–Segel: a manufactured coupled-flux solution

#### [Forced advective Keller–Segel manufactured problem](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#forced-keller-segel-model-en)

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

$$
n_*=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y)
$$

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

#### Keller–Segel: a manufactured coupled-flux solution

Supplementary execution example · Example definition or validation formula

$$
n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n
$$

$$
\tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c
$$

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

### Exact and reference solutions

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

#### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en#keller-segel-forced-flux-en-measurements)

Manufactured solution · Reference for the same problem

n_t+\nabla\cdot(wn)=D_n\Delta n-\chi\nabla\cdot(n\nabla c)+rn(1-n)+s_n;\quad \tau c_t=D_c\Delta c+\alpha n-\lambda c+s_c;\quad n_*(x,y,t)=1+0.1e^{-t}\cos(\pi x)\cos(\pi y),\quad c_*(x,y,t)=1+0.05e^{-2t}\cos(\pi x)\cos(2\pi y),\quad\psi=\sin(\pi x)\sin(\pi y)/\pi,\quad w=(\partial_y\psi,-\partial_x\psi)

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection. Dimensionless; manufactured-field coefficients and forcing are fixed in inputs.json. Manufactured forcing and boundary fluxes, with explicit ownership of interior faces and corners.

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

#### Keller–Segel: a manufactured coupled-flux solution

Qualify36source pairs,96cell-state vectors and wrong-sign,omitted-coupling,stale-stage and face-duplication controls. Separate spatial,same-MOL time,positivity and actual stage-ledger outcomes.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en)

### Numerical methods

Use cell-average centered face fluxes and SSPRK3 with n,c and forcing at the same stage. Check expanded trigonometric integrals against independent unexpanded integrals and scalar face-loop references.

- [SSPRK(3,3)](https://hrkoyama.github.io/numerical-methods-atlas/methods/ssprk33/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Dormand–Prince RK45](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk45/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Keller–Segel: a manufactured coupled-flux solution](https://hrkoyama.github.io/numerical-methods-atlas/validation/keller-segel-forced-flux/?lang=en)

Supplementary execution example

Use smooth exact2D fields to test cross fluxes, stage timing and mass ledgers.

On the unit square toT.25,manufacture forcing for n=1+.1e⁻ᵗcosπx cosπy,c=1+.05e⁻²ᵗcosπx cos2πy with divergence-free tangential advection.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/atlas-biology-space-controls-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This authored forced two-field model does not reproduce the full original biological model or demonstrate aggregation, true blow-up or suppression. No clipping is used to manufacture positivity.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/biology-space-controls/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/run.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/common.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/common.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/keller_segel.py)
- [/code/validated-examples/2026-11-25/biology-space-controls/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/biology-space-controls/test_models.py)
