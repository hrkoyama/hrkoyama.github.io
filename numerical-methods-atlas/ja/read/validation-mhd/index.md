# 流体・MHDの独立照合とCT／GLM

小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Orszag–Tang：CT・GLMと独立Athena++比較

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

**使用手法**

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) (`ct`)
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-algorithm)

公開済みの1次Rusanov/前進Eulerを再利用。CTは共有corner EMFの離散curl、GLMはcell中心Bと双曲・放物型cleaning。Athena++は別実装のHLLD+PLM+RK2。

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Orszag–Tang：CT・GLMと独立Athena++比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/ct-glm-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Orszag–Tang渦（CT・GLM・発散誤差摂動を統合）](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja) (`orszag-tang`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja#ct-glm-independent-ja-validation)

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

- [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-postshock-orszag-tang-ja) (`postshock-orszag-tang`; 関連モデルの参照 · 有限格子の数値参照)

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。
### 前提・単位・境界

単位正方形、γ=5/3、μ₀=1、vz=Bz=0、t=0.05。rho=25/(36π)、p=5/(12π)、v=(-sin2πy,sin2πx)、B=(-sin2πy,sin4πx)/sqrt(4π)。

**編集上の補足**

採用GLMはch=3、減衰率κ=0.18 ch nです。nは各軸のセル数で、この減衰は格子依存です。同じ連続初期場・終了時刻・CFLを用いますが、CT/GLMで実ステップ数とdiv Bのnative演算子は異なります。

### 採用した計算法

公開済みの1次Rusanov/前進Eulerを再利用。CTは共有corner EMFの離散curl、GLMはcell中心Bと双曲・放物型cleaning。Athena++は別実装のHLLD+PLM+RK2。

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

### 比較・検証

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

### 確認の限界

CTの面上divergenceとGLMの中心差分divergenceは異なる演算子です。共通cell演算子の値も別記します。Athenaの初期磁場はベクトルポテンシャルの差分による面平均で、同じ連続場の離散化差を含みます。短時間の平面MHD比較であり、衝撃波・3D・UCTやCTUの検証ではありません。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_density_128_256_l1": 4.631344236627223e-05,
    "ct_glm_finest_density_l1": 0.0016910992352830488
  },
  "checks": {
    "independent_reference_refined": true,
    "ct_native_constraint_16": true,
    "ct_native_constraint_32": true,
    "ct_native_constraint_64": true,
    "ct_density_error": true,
    "ct_magnetic_error": true,
    "ct_refinement": true,
    "glm_density_error": true,
    "glm_magnetic_error": true,
    "glm_refinement": true,
    "conservation": true,
    "positive_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Brio–Wu：別実装HLLDとの照合

公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。

**使用手法**

- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) (`hlld`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-algorithm)

アトラス側はMC再構成とSSPRK2、参照は独立C++のHLLD・PLM・RK3。異なる実装ですがHLLDという数値流束の系列は共有します。

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Brio–Wu：別実装HLLDとの照合：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/brio-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Brio–Wu衝撃波管](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja) (`brio-wu`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/brio-wu/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/?lang=ja#brio-independent-ja-validation)

128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

1D、[0,1]、t=0.1、γ=2、Bx=0.75。左右(rho,p,By)=(1,1,1)/(0.125,0.1,-1)、速度ゼロ、流出境界。

### 採用した計算法

アトラス側はMC再構成とSSPRK2、参照は独立C++のHLLD・PLM・RK3。異なる実装ですがHLLDという数値流束の系列は共有します。

$$
\mathbf U_t+\mathbf F(\mathbf U)_x=0,\qquad B_x=0.75
$$

### 比較・検証

128/256/512セルを、2048/4096セルで再実行した独立参照の保存的細胞平均と比較。rho/ByのL1誤差、格子改善、密度・圧力正値性を判定します。

### 確認の限界

Brio–Wuの複合波を含む数値解との照合であり、一般MHD Riemann問題の唯一の厳密解とは呼びません。参照の再生成にはC++コンパイルが必要で、通常Python実行は同梱参照を使います。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.00048642415115017165,
    "reference_finest_n": 4096,
    "finest_density_l1": 0.0018299450752667257
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true,
    "magnetic_error": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/brio-independent/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- M. Brio and C. C. Wu (1988). An upwind differencing scheme for the equations of ideal magnetohydrodynamics. https://doi.org/10.1016/0021-9991(88)90120-9; review_level=bibliographic identity and official Athena test definition

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## Shu–Osher：独立参照と格子収束

衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。

**使用手法**

- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) (`muscl`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-algorithm)

アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![Shu–Osher：独立参照と格子収束：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/shu-independent.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Shu–Osher衝撃波・エントロピー波干渉](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja) (`shu-osher`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/shu-osher/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/?lang=ja#shu-independent-ja-validation)

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

γ=1.4、[-5,5]、t=1.8。x<-4は(rho,u,p)=(3.857143,2.629369,10.33333)、右はrho=1+0.2sin5x,u=0,p=1。

### 採用した計算法

アトラス側はMC-MUSCL/HLLC/SSPRK3、Athena++側はPLM/HLLC/RK3。公式problem generatorの位置と正弦波の波数だけを合わせるpatchを保存し、solver本体は変更しません。

$$
\rho(x,0)=1+0.2\sin(5x)\quad(x\geq-4)
$$

### 比較・検証

100/200/400セルの密度L1誤差と改善率、正値性を測り、参照2048/4096/8192セルの差も事前幅と比較します。境界へ衝撃波が届かない固定時刻で比較します。

### 確認の限界

参照は厳密解ではなく独立した有限格子数値解です。異なる流束系列すべての優劣、WENOの一般的高次数、負圧防止の保証には広げません。 参照2048→4096のL1差0.005346は事前幅0.005を満たさず、8192へ細分しました。途中の未達記録も残します。

### 保存実測値と判定

```json
{
  "metrics": {
    "reference_last_pair_l1": 0.003374178434921656,
    "reference_finest_n": 8192,
    "finest_density_l1": 0.05377749991959067
  },
  "checks": {
    "independent_reference_refined": true,
    "density_error": true,
    "grid_improvement": true,
    "positive_states": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/shu-independent/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- J. M. Stone, K. Tomida, C. J. White and K. G. Felker (2020). The Athena++ Adaptive Mesh Refinement Framework: Design and Magnetohydrodynamic Solvers. https://doi.org/10.3847/1538-4365/ab929b; review_level=official-code-and-metadata; pinned source compiled and executed
- C.-W. Shu and S. Osher (1989). Efficient implementation of essentially non-oscillatory shock-capturing schemes, II. https://doi.org/10.1016/0021-9991(89)90222-2; review_level=bibliographic identity and official Athena problem generator

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## GLMの磁気単極子モード：解析的減衰

GLM cleaning単独の縦磁場Fourierモードを、連続線形方程式の行列指数解と比較します。

**使用手法**

- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) (`glm`)

**方程式**

[この実行例の診断式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-algorithm)

∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![GLMの磁気単極子モード：解析的減衰：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/glm-fourier-mode.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

この検査・診断例には、別の物理テスト問題を割り当てていません。固有の診断図と検証資料を示しています。

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/?lang=ja#glm-fourier-mode-ja-validation)

16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

周期[0,1]、Bx=cos2πx、psi=0、ch=1、減衰κ=2、t=1。流体との結合を外した線形診断です。

### 採用した計算法

∂tBx=-∂xpsi、∂tpsi=-ch²∂xBx-κpsiを中心差分とRK4で積分。独立参照は連続Fourier記号の2×2行列指数です。

$$
B_t=-\psi_x,\quad\psi_t=-c_h^2B_x-\kappa\psi
$$

### 比較・検証

16/32/64点でL2誤差、空間2次収束、磁場divergenceモード振幅の減衰を判定します。

### 確認の限界

この線形モードの減衰を、非線形MHDの全divergenceや大域的な精度の保証とはしません。CTで表せない単極子モードをCTとの同条件比較には用いません。

### 保存実測値と判定

```json
{
  "metrics": {
    "observed_order": 2.001546730427675,
    "continuum_amplitude_ratio": 0.3619556718500278
  },
  "checks": {
    "analytic_expm_comparison": true,
    "spatial_order": true,
    "divergence_damping": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/glm-fourier-mode/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- A. Dedner et al. (2002). Hyperbolic Divergence Cleaning for the MHD Equations. https://www.tp4.ruhr-uni-bochum.de/~sw/papers/JCP2002.6961.pdf; review_level=author-hosted primary paper; linear cleaning equations checked

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
