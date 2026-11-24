# LBMのTaylor–Green渦と低Mach誤差

周期渦の解析解を使い、格子・時間刻み・Mach数が結び付く誤差と振幅依存性を調べます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## LBM Taylor–Green渦：格子・刻み・Machの結合感度

周期2Dの非線形渦を実際に時間発展し、連続解析場への速度・圧力・エネルギー誤差を保存します。amplitude感度と同格子のcoupled刻み感度も分けて示します。

**使用手法**

- [D2Q9–BGK衝突・並進](https://hrkoyama.github.io/numerical-methods-atlas/methods/d2q9-bgk/?lang=ja) (`d2q9-bgk`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-algorithm)

標準BGKと完全周期streaming。p=cs²(rho−平均rho)(dx/dt)²で圧力単位とゲージを揃えます。解析場は初期値以外に注入せず、微分を独立Fourier演算で資格確認します。

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

- [等温格子BGK](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bgk-ja) (`bgk`)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。


**問題の図**

![LBM Taylor–Green渦：格子・刻み・Machの結合感度：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja) (`taylor-green`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/taylor-green/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/?lang=ja#lbm-taylor-green-ja-validation)

22pytestと79判定、6固定発展。最細速度相対L2.03、圧力.08、combined速度次数1.5以上、エネルギー.03、発散・周期質量・平均運動量を判定。解析PDE5資格を区別して保存します。 最粗N16の初回エネルギー誤差5.0018%未達を保持し、同じ3%基準へ最粗だけN24へ細分化。次数は最細32/64対だけで評価します。

- [粘性流／2次元Taylor–Green渦](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-taylor-green-ja) (`taylor-green`; 関連モデルの参照 · 解析参照)

同じν=0.1・周期[0,2π]²の解析モデルですが、参照カードはy=π/4のx断面表示です。2次元速度・圧力場や格子誤差の配列とは一致しません。

- [LBMのTaylor–Green渦：格子・時間・Mach数が結び付く感度](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-taylor-green-ja) (`lbm-taylor-green`; 関連モデルの参照 · 解析参照)

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。
### 前提・単位・境界

[0,2pi)²、ν.1、基本U.2、N24/32/64、dt=.2dx²、tau.56、T=.2pi²、144/256/1024steps。N32/U.4,.8とN32/U.2/dt=.1dx²/tau.53/512stepsを追加。初期圧力整合rhoを使用。

**編集上の補足**

拡散尺度では格子・時間・Machが結合し、amplitude変更はReも変えます。純空間/純時間/純Mach次数や有限Machの厳密非圧縮性を主張しません。平衡初期化のkinetic startupも実誤差へ含めます。

### 採用した計算法

標準BGKと完全周期streaming。p=cs²(rho−平均rho)(dx/dt)²で圧力単位とゲージを揃えます。解析場は初期値以外に注入せず、微分を独立Fourier演算で資格確認します。

$$
u=U\sin x\cos y\,e^{-2\nu t},\quad v=-U\cos x\sin y\,e^{-2\nu t}
$$

$$
p=\frac{U^2}{4}(\cos2x+\cos2y)e^{-4\nu t},\quad\langle K\rangle=\frac{U^2}{4}e^{-4\nu t}
$$

### 比較・検証

22pytestと79判定、6固定発展。最細速度相対L2.03、圧力.08、combined速度次数1.5以上、エネルギー.03、発散・周期質量・平均運動量を判定。解析PDE5資格を区別して保存します。 最粗N16の初回エネルギー誤差5.0018%未達を保持し、同じ3%基準へ最粗だけN24へ細分化。次数は最細32/64対だけで評価します。

### 確認の限界

拡散尺度では格子・時間・Machが結合し、amplitude変更はReも変えます。純空間/純時間/純Mach次数や有限Machの厳密非圧縮性を主張しません。平衡初期化のkinetic startupも実誤差へ含めます。

### 保存実測値と判定

```json
{
  "metrics": {
    "combined_velocity_order": 1.9997408571265982,
    "reference_qualification": {
      "Fourier divergence": 4.718447854656915e-16,
      "Fourier NS x": 3.0878077872387166e-16,
      "Fourier NS y": 3.434752482434078e-16,
      "mean pressure gauge": 6.505213034913027e-19,
      "analytic mean energy": 1.734723475976807e-18
    },
    "scope": "Diffusive grid/time/Mach refinement, amplitude/Re sensitivity, and coupled dt/Mach/tau probe; no pure time or pure Mach order."
  },
  "checks": {
    "analytic reference Fourier divergence": true,
    "analytic reference Fourier NS x": true,
    "analytic reference Fourier NS y": true,
    "analytic reference mean pressure gauge": true,
    "analytic reference analytic mean energy": true,
    "0 finite arrays": true,
    "0 positive density": true,
    "0 actual maximum Mach": true,
    "0 mass ledger": true,
    "0 wall-open momentum ledger": true,
    "0 all fixed integer steps": true,
    "0 declared physical endpoint": true,
    "0 periodic mass": true,
    "0 zero mean momentum": true,
    "0 normalized divergence": true,
    "0 mean kinetic energy": true,
    "1 finite arrays": true,
    "1 positive density": true,
    "1 actual maximum Mach": true,
    "1 mass ledger": true,
    "1 wall-open momentum ledger": true,
    "1 all fixed integer steps": true,
    "1 declared physical endpoint": true,
    "1 periodic mass": true,
    "1 zero mean momentum": true,
    "1 normalized divergence": true,
    "1 mean kinetic energy": true,
    "2 finite arrays": true,
    "2 positive density": true,
    "2 actual maximum Mach": true,
    "2 mass ledger": true,
    "2 wall-open momentum ledger": true,
    "2 all fixed integer steps": true,
    "2 declared physical endpoint": true,
    "2 periodic mass": true,
    "2 zero mean momentum": true,
    "2 normalized divergence": true,
    "2 mean kinetic energy": true,
    "3 finite arrays": true,
    "3 positive density": true,
    "3 actual maximum Mach": true,
    "3 mass ledger": true,
    "3 wall-open momentum ledger": true,
    "3 all fixed integer steps": true,
    "3 declared physical endpoint": true,
    "3 periodic mass": true,
    "3 zero mean momentum": true,
    "3 normalized divergence": true,
    "3 mean kinetic energy": true,
    "4 finite arrays": true,
    "4 positive density": true,
    "4 actual maximum Mach": true,
    "4 mass ledger": true,
    "4 wall-open momentum ledger": true,
    "4 all fixed integer steps": true,
    "4 declared physical endpoint": true,
    "4 periodic mass": true,
    "4 zero mean momentum": true,
    "4 normalized divergence": true,
    "4 mean kinetic energy": true,
    "5 finite arrays": true,
    "5 positive density": true,
    "5 actual maximum Mach": true,
    "5 mass ledger": true,
    "5 wall-open momentum ledger": true,
    "5 all fixed integer steps": true,
    "5 declared physical endpoint": true,
    "5 periodic mass": true,
    "5 zero mean momentum": true,
    "5 normalized divergence": true,
    "5 mean kinetic energy": true,
    "finest combined velocity error": true,
    "finest pressure gauge error": true,
    "combined finest velocity order": true,
    "first diffusive refinement decreases velocity": true,
    "second diffusive refinement decreases velocity": true,
    "same physical endpoint all six runs": true,
    "amplitude probes change actual Mach": true,
    "exactly six distinct prescribed runs": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/lbm-taylor-green/index.json

![固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。](https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/lbm-taylor-green-preview.png)

固定入力を実計算した保存配列の2D場と検証診断。参照・境界・誤差の範囲は本文に明記。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/atlas-lbm-taylor-green-2026-11-24.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-24/lbm-taylor-green/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Qisu Zou and Xiaoyi He (1996). On pressure and velocity flow boundary conditions and bounceback for the lattice Boltzmann BGK model. https://arxiv.org/abs/comp-gas/9611001; review_level=primary-selected-extracted-text
原著preprintの式と平面流入出境界・角・圧縮性の範囲を選択読解。特殊d2q9iの成功を本BGKへ流用しません。

- Pierre Lallemand and Li-Shi Luo (2003). Lattice Boltzmann method for moving boundaries. https://doi.org/10.1016/S0021-9991(02)00022-0; review_level=primary-selected-text-via-mirror
原著の選択部分を著者資料ミラーから読解。今回の2点線形補間は別導出・単step資格で確認し、2001原著全文を読んだとはしません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
