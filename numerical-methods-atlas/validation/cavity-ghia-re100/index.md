# Re=100蓋駆動キャビティ：Ghia中心線との比較

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

- [LBMのRe100キャビティ：実2D場とGhia中心線](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lbm-cavity-re100-ja) (`lbm-cavity-re100`; 関連モデルの参照 · 有限格子の数値参照)

物理単位正方形、蓋U1、ν.01、Re100。N24/32/48、格子蓋速度.04、dt=.04/N。3壁静止、上壁右向き、同時上面/側面crossingは静止側を優先。初期rho1・静止。
## 前提・単位・境界

無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。

**編集上の補足**

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。 科学ソース改訂3・不変配布版2026-11-23-r2は22単体検査と群全体94判定に合格しました。初回のNumPy真偽値のJSON直列化失敗に加え、次の未公開候補は共通verifierが必要とする完了状態・ケースID別の最上位合否が不足していました。この配布版はJSONのtermination・failure・ケース別checksを整え、従来の3診断をsummary_checksへ保持する封筒形式だけの修正と、回帰検査1件を追加しています。入力・受入条件・数値ソルバー・参照と従来21検査は不変で、6計算の保存NPZ配列は前候補とビット一致しています。元の未公開配布物は公開ツリー外の作業記録へ保存し、旧候補の失敗履歴も保持しました。 最細Ghia中心線の最大誤差はu約.00277820、v約.00590408、格子主渦は(.609375,.734375)、真の定常残差は約9.68×10⁻¹⁰です。圧力を消去する流れ関数法であり、キャビティ圧力を検証したとは表示しません。

## 採用した計算法

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

## 比較・検証

22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。

## 確認の限界

Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。

## 保存実測値と判定

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

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

## 出典と確認範囲

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
原著の式・境界図・表I/IIのRe100列と表Vの主渦を直接目視確認。公開ミラーは原著の配送元として記録し、論文PDFは配布しません。本実装は原著のCSI-MG法とは異なります。

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Sandia/OSTI公式書誌・抄録と、原著報告の印刷12頁で製造解と格子細分化の併用を確認。本例の多項式と圧力場は独自に構成しました。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Re100 lid-driven cavity: Ghia centerline comparison

March a real nonperiodic 2D viscous incompressible solver to steady state on 17/33/65 node grids and compare against original Ghia centerlines. Retain streamlines, grid vortex center, true PDE residual and discrete divergence.

**Methods used**

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) (`centered-difference`)
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) (`heun`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-algorithm)

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

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

- [Incompressible Navier–Stokes](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#navier-stokes-en) (`navier-stokes`)

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.


**Problem figure**

![Re100 lid-driven cavity: Ghia centerline comparison: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Re100 lid-driven cavity](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en) (`lid-driven-cavity`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=en#cavity-ghia-re100-en-validation)

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

- [Ghia Re100: original finite-grid velocity centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-ghia-re100-en) (`ghia-re100`; Same-problem reference · Finite-grid numerical reference)

Educational Re100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

- [LBM Re100 cavity: actual2D fields and Ghia centerlines](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-lbm-cavity-re100-en) (`lbm-cavity-re100`; Related-model reference · Finite-grid numerical reference)

Physical unit square, lid1, viscosity.01, Re100; N24/32/48, lattice lid.04, dt=.04/N. Three stationary walls/rightward lid; stationary side owns a simultaneous top/side link. Initialrho1/rest.
## Assumptions, units and boundaries

Dimensionless unit square, viscosity .01, lid speed1, Re=100. Top interior nodes have u=1; other walls and all four corners have zero velocity. Psi=0 on every wall; initial interior vorticity 0. Reapply Thom wall vorticity at every Heun stage.

**Editorial clarification**

Educational Re=100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed. Scientific-source revision3, immutable edition2026-11-23-r2, passed22 unit checks and all94 group gates. After the initial NumPy-boolean JSON-serialization failure, the next unpublished candidate lacked completion status and case-ID top-level checks required by the common verifier. This edition only repairs the JSON envelope with termination,failure and case-keyed checks, retaining the prior three diagnostics under summary_checks, and adds one regression. Inputs,acceptance,numerical solver,references and the prior21 tests are unchanged. All six saved NPZ field arrays are bit-identical to the previous candidate. The original unpublished packet is archived outside the public tree, and earlier failure history is retained. Finest Ghia centerline maximum errors are about.00277820 foru and.00590408 forv; the grid primary vortex is(.609375,.734375), with true steady residual about9.68e-10. Pressure is eliminated in streamfunction evolution; cavity pressure is not validated.

## Adopted numerical method

Advance vorticity transport with centered differences and Heun. Each stage solves−Delta_h psi=omega using a nonperiodic Dirichlet DST, then forms u=psi_y,v=−psi_x. Use local first-order Thom wall vorticity; this is an independent method, not Ghia CSI-MG or its higher-order wall formula.

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

## References and validation

Freeze 22 pytest checks and 94 group gates. Linearly interpolate to 17 points per velocity transcribed after direct visual reading of original TablesI/II, printed 398–399. Require finest component maximum errors≤.03, refinement decrease and steady residual≤1e−7. Also check primary-vortex grid location from TableV, wall values, Poisson residual and discrete divergence.

## Limits

Educational Re=100 checks on three fixed grids. Lid/sidewall corner velocities are discontinuous; stationary corners take precedence. Ghia values are rounded numerical references, not an exact solution, and printed four-decimal coordinates are preserved. No high-Re, turbulence, original-algorithm reproduction or cavity-pressure validation is claimed.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/index.json

![Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.](https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png)

Saved finest Re100 streamlines and speed. Red dot: computed grid primary vortex; hollow dot: original Ghia TableV location.

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/atlas-wall-flow-2026-11-23-r2.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/attempts/01/source/inputs.json

## Sources and review scope

- U. Ghia, K. N. Ghia and C. T. Shin (1982). High-Re solutions for incompressible flow using the Navier-Stokes equations and a multigrid method. https://www.sciencedirect.com/science/article/pii/0021999182900584; review_level=primary-original-selected-pages
Visually inspected original equations/boundary figure, Re100 columns in TablesI/II and primary vortex in TableV. The public mirror delivers the original paper; its PDF is not redistributed. This independently written solver differs from CSI-MG.

- Kambiz Salari and Patrick Knupp (2000). Code Verification by the Method of Manufactured Solutions. https://www.sandia.gov/research/publications/details/code-verification-by-the-method-of-manufactured-solutions-2000-06-01/; review_level=primary-selected-section-and-official-abstract
Read official Sandia/OSTI metadata/abstract and original report printed12 on MMS together with mesh refinement. The polynomial and pressure field are constructed for this example.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
