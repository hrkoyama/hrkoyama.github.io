# 非周期壁面：キャビティと製造解

非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## Re=100蓋駆動キャビティ：Ghia中心線との比較

非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-algorithm)

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

- [非圧縮Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja) (`navier-stokes`)

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。


**問題の図**

![Re=100蓋駆動キャビティ：Ghia中心線との比較：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Re100の蓋駆動キャビティ](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja) (`lid-driven-cavity`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-validation)

22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

- [Ghia Re100：原著の有限格子速度中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja) (`ghia-re100`; 同じ問題の参照 · 有限格子の数値参照)

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。
### 前提・単位・境界

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

**編集上の補足**

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。 科学ソース改訂3・不変配布版2026-11-23-r2は22単体検査と群全体94判定に合格しました。初回のNumPy真偽値のJSON直列化失敗に加え、次の未公開候補は共通verifierが必要とする完了状態・ケースID別の最上位合否が不足していました。この配布版はJSONのtermination・failure・ケース別checksを整え、従来の3診断をsummary_checksへ保持する封筒形式だけの修正と、回帰検査1件を追加しています。入力・受入条件・数値ソルバー・参照と従来21検査は不変で、6計算の保存NPZ配列は前候補とビット一致しています。元の未公開配布物は公開ツリー外の作業記録へ保存し、旧候補の失敗履歴も保持しました。 最細Ghia中心線の最大誤差はu約.00277820、v約.00590408、格子主渦は(.609375,.734375)、真の定常残差は約9.68×10⁻¹⁰です。圧力を消去する流れ関数法であり、キャビティ圧力を検証したとは表示しません。

### 採用した計算法

ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega,\quad -\Delta\psi=\omega,\quad (u,v)=(\psi_y,-\psi_x)
$$

$$
\mathrm{Re}=UL/\nu=100,\quad \psi|_{\partial\Omega}=0,\quad u(x,1)=1\ (0<x<1)
$$

$$
\omega_{\mathrm{top},i}=-2\psi_{J-1,i}/h^2-2U/h,\quad \omega_{\mathrm{stationary}}=-2\psi_{\mathrm{adj}}/h^2+O(h)
$$

$$
\omega^{(1)}=\omega^n+\Delta t L(\omega^n),\quad \omega^{n+1}=\tfrac12\omega^n+\tfrac12[\omega^{(1)}+\Delta t L(\omega^{(1)})]
$$

### 比較・検証

22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

### 確認の限界

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_u_ghia_maximum": 0.0027781960789884375,
    "finest_v_ghia_maximum": 0.005904081227178365,
    "finest_vortex_center": [
      0.609375,
      0.734375
    ],
    "finest_steady_residual": 9.684821000721655e-10
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "finest u primary-table maximum error": true,
    "finest v primary-table maximum error": true,
    "Ghia centerline refinement 1": true,
    "Ghia centerline refinement 2": true,
    "finest primary-vortex grid location": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/index.json

![保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

保存した最細Re100計算の流線と速さ。赤点は格子上の主渦、白抜き点はGhia表Vの主渦位置です。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

### 出典と確認範囲

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
  原著の式・境界図・表I/IIのRe100列と表Vの主渦を直接目視確認。公開ミラーは原著の配送元として記録し、論文PDFは配布しません。本実装は原著のCSI-MG法とは異なります。
- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
  Sandia/OSTI公式書誌・抄録と、原著報告の印刷12頁で製造解と格子細分化の併用を確認。本例の多項式と圧力場は独自に構成しました。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 非周期壁面の製造解：速度・剪断・圧力演算子

キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。

**使用手法**

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) (`centered-difference`)
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) (`heun`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-algorithm)

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

- [外力付き非圧縮流と壁面製造解](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja) (`forced-incompressible`)

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。


**問題の図**

![非周期壁面の製造解：速度・剪断・圧力演算子：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[非周期壁面の製造非圧縮流](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja) (`wall-manufactured`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-validation)

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

- [壁面製造解：多項式速度と独立した圧力演算子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja) (`wall-mms`; 同じ問題の参照 · 製造解)

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。
### 前提・単位・境界

単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。

**編集上の補足**

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。 科学ソース改訂3・不変配布版2026-11-23-r2は22単体検査と群全体94判定に合格しました。初回のNumPy真偽値のJSON直列化失敗に加え、次の未公開候補は共通verifierが必要とする完了状態・ケースID別の最上位合否が不足していました。この配布版はJSONのtermination・failure・ケース別checksを整え、従来の3診断をsummary_checksへ保持する封筒形式だけの修正と、回帰検査1件を追加しています。入力・受入条件・数値ソルバー・参照と従来21検査は不変で、6計算の保存NPZ配列は前候補とビット一致しています。元の未公開配布物は公開ツリー外の作業記録へ保存し、旧候補の失敗履歴も保持しました。 最細速度L2は約2.638×10⁻⁵、最後の格子対の速度・流れ関数次数は約2.009/2.022です。実際の壁剪断の観測次数は約1.982ですが、厳密ψでのThom局所打切り次数は約.989で、一般の二次壁公式の保証ではありません。独立した圧力演算子のp・全勾配・境界勾配の次数は約1.978/2.318/1.998であり、キャビティ圧力とは別です。

### 採用した計算法

共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

$$
f(z)=z^2(1-z)^2,\quad \psi_\star=8f(x)f(y),\quad u_\star=\partial_y\psi_\star,\quad v_\star=-\partial_x\psi_\star,\quad\omega_\star=-\Delta\psi_\star
$$

$$
\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega+s,\quad s=u_\star\partial_x\omega_\star+v_\star\partial_y\omega_\star-\nu\Delta\omega_\star
$$

$$
p_\star=x^2+y^2+\sin(\pi x)\sin(\pi y),\quad -\Delta p_\star=-4+2\pi^2\sin(\pi x)\sin(\pi y),\quad p|_{\partial\Omega}=p_\star
$$

$$
\tau_{xy}/\mu=\partial_y u\quad\text{on stationary horizontal walls},\qquad p_{\mathrm{obs}}=\log_2(E_h/E_{h/2})
$$

### 比較・検証

ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。

### 確認の限界

Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

### 保存実測値と判定

```json
{
  "metrics": {
    "finest_velocity_l2": 2.637991527485713e-05,
    "finest_streamfunction_l2": 3.0579766556845255e-05,
    "observed_orders": {
      "psi_l2": [
        2.0426330065243574,
        2.021783836772359
      ],
      "velocity_l2": [
        1.9917746694984177,
        2.0086644375747413
      ],
      "wall_omega_maximum": [
        1.937772137605888,
        1.9794771588130946
      ],
      "wall_shear_maximum": [
        1.9412705074950394,
        1.9820164294643936
      ],
      "thom_exact_psi_wall_truncation": [
        0.9769163868869587,
        0.9885952367277506
      ],
      "pressure_l2": [
        1.9590185209239261,
        1.9784952274339704
      ],
      "pressure_gradient_l2": [
        2.3544980286788206,
        2.3175253385985015
      ],
      "pressure_boundary_gradient_l2": [
        1.9914961869556822,
        1.9978781190385215
      ]
    },
    "reference_qualification": {
      "checks": {
        "independent tensor-polynomial fields": true,
        "independent tensor-polynomial forcing": true,
        "analytic four-wall no slip": true,
        "analytic incompressibility": true,
        "two primary-table columns each 17 points": true
      },
      "field_maximum": 1.27675647831893e-15,
      "forcing_maximum": 4.038436252074007e-15,
      "exact_wall_speed": 1.27675647831893e-15,
      "passed": true
    },
    "pressure_scope": "Separate manufactured Dirichlet operator; cavity pressure not computed."
  },
  "checks": {
    "n17: steady stop reached": true,
    "n17: steady PDE residual": true,
    "n17: streamfunction Poisson residual": true,
    "n17: discrete divergence": true,
    "n17: u wall values": true,
    "n17: v wall values": true,
    "n17: psi wall values": true,
    "n17: finite states and history": true,
    "n17: no clipping or retry": true,
    "n17: recorded advective Courant": true,
    "n33: steady stop reached": true,
    "n33: steady PDE residual": true,
    "n33: streamfunction Poisson residual": true,
    "n33: discrete divergence": true,
    "n33: u wall values": true,
    "n33: v wall values": true,
    "n33: psi wall values": true,
    "n33: finite states and history": true,
    "n33: no clipping or retry": true,
    "n33: recorded advective Courant": true,
    "n65: steady stop reached": true,
    "n65: steady PDE residual": true,
    "n65: streamfunction Poisson residual": true,
    "n65: discrete divergence": true,
    "n65: u wall values": true,
    "n65: v wall values": true,
    "n65: psi wall values": true,
    "n65: finite states and history": true,
    "n65: no clipping or retry": true,
    "n65: recorded advective Courant": true,
    "psi_l2 refinement 1": true,
    "velocity_l2 refinement 1": true,
    "wall_omega_maximum refinement 1": true,
    "wall_shear_maximum refinement 1": true,
    "psi_l2 refinement 2": true,
    "velocity_l2 refinement 2": true,
    "wall_omega_maximum refinement 2": true,
    "wall_shear_maximum refinement 2": true,
    "finest streamfunction order": true,
    "finest velocity order": true,
    "finest streamfunction accuracy": true,
    "finest velocity accuracy": true,
    "n17: separate pressure Dirichlet boundary": true,
    "n17: separate pressure Poisson residual": true,
    "n17: finite separate pressure solution": true,
    "n33: separate pressure Dirichlet boundary": true,
    "n33: separate pressure Poisson residual": true,
    "n33: finite separate pressure solution": true,
    "n65: separate pressure Dirichlet boundary": true,
    "n65: separate pressure Poisson residual": true,
    "n65: finite separate pressure solution": true,
    "finest separate pressure_l2 order": true,
    "finest separate pressure_gradient_l2 order": true,
    "finest separate pressure_boundary_gradient_l2 order": true,
    "independent tensor-polynomial fields": true,
    "independent tensor-polynomial forcing": true,
    "analytic four-wall no slip": true,
    "analytic incompressibility": true,
    "two primary-table columns each 17 points": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/index.json

![実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png)

実計算した最細の製造流れの流線と速度誤差。厳密壁渦度を注入せず、キャビティと同じThom閉鎖を使います。

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

### 出典と確認範囲

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
  原著の式・境界図・表I/IIのRe100列と表Vの主渦を直接目視確認。公開ミラーは原著の配送元として記録し、論文PDFは配布しません。本実装は原著のCSI-MG法とは異なります。
- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
  Sandia/OSTI公式書誌・抄録と、原著報告の印刷12頁で製造解と格子細分化の併用を確認。本例の多項式と圧力場は独自に構成しました。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
