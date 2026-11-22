# 周期Fourierモードの熱拡散 / Periodic Fourier-mode heat decay

https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/

## 日本語

[保存した最終時刻の数値波形と参照解。](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#heat-periodic)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [熱・拡散方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja)

$$
\partial_tu=\nu\nabla^2u
$$

一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。

### 厳密解・参照解

周期区間の単一Fourierモードの指数減衰が解析基準です。保存図の振幅0.25・粘性0.02の条件を、別周波数のコード検査と区別します。

#### [熱拡散／Fourierモードの減衰](https://hrkoyama.github.io/numerical-methods-atlas/?lang=ja#/exact-solutions?case=sine-heat)

解析解 · 関連モデルの参照

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

単位区間の周期境界、拡散係数0.02。

保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。

### 計算法

この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり
- [前進Euler法](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja) — 関連する解説; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

この問題の固定入力実行例は未登録です。保存結果と解説は上のリンクから確認できます。

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

関連する既存のソース・検査。固定入力実行例とは別です。

`test_spectral_heat_exact_mode_decay`

[対応する配布版 / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

作業フォルダ：atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_spectral_heat_exact_mode_decay
```

## English

[Stored final-time numerical profile and reference.](https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/elliptic/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#heat-periodic-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Heat / diffusion equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#heat-en)

$$
\partial_tu=\nu\nabla^2u
$$

A representative constant-diffusivity form: mode decay, time integration and boundaries.

### Exact and reference solutions

Analytic exponential decay of a periodic Fourier mode is the standard. Distinguish the saved figure's amplitude 0.25 and viscosity 0.02 from code checks using other frequencies.

#### [Heat / Fourier-mode decay](https://hrkoyama.github.io/numerical-methods-atlas/?lang=en#/exact-solutions?case=sine-heat)

Analytic reference · Related-model reference

u = 1 + 0.25 sin(2πx) exp[−0.02(2π)²t]

Periodic unit interval; viscosity 0.02.

The saved gallery matches periodic [0,1], 1+0.25sin(2πx), ν=0.02 and final time one; this does not assert a match to separate-frequency code checks. Physical inputs match, but the card’s point samples and the saved computation’s finite-volume cell averages/discrete grid are different representations.

### Numerical methods

Methods used by this problem’s stored comparison data or corresponding public checks, rather than added solely for general applicability.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Related explanation; Method-registry status: Educational example / related code
- [Forward Euler](https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=en) — Related explanation; Method-registry status: Educational example / related code

### Code and execution

No fixed-input execution example is registered for this problem. The saved visual and reading remain available above.

#### [code/numerical-methods-atlas/2026-11-21/tests/test_linear.py](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/tests/test_linear.py)

Existing related source/check, separate from a registered fixed-input execution example.

`test_spectral_heat_exact_mode_decay`

[Corresponding code edition / ZIP](https://hrkoyama.github.io/code/numerical-methods-atlas/2026-11-21/atlas-code-2026-11-21.zip)

Working directory: atlas-code-2026-11-21/

```sh
python -m pytest -q tests/test_linear.py -k test_spectral_heat_exact_mode_decay
```
