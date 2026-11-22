# 作用素分割：同じ反応拡散でLie–TrotterとStrangを比較

短い時間区間の非線形Schnakenberg反応拡散を、同じ初期場・格子・部分ソルバー・出力時刻で比較します。時間の収束と数値参照の感度を調べる軽量な追加例です。既存の空間収束・長時間パターンの記録は保持します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 同じ非線形反応拡散でLie–TrotterとStrangを比較する

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

**使用手法**

- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) (`lie-trotter`)
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) (`strang-splitting`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-algorithm)

Lie–Trotterは拡散h→反応h、Strangは拡散h/2→反応h→拡散h/2。どちらも更新後の状態を次へ渡します。拡散は2次中心FD行列の指数をFFTで厳密適用、反応は同じ陰的中点則・Newton公差2e−13・上限12評価を使用。反応流は厳密解ではなく2次近似です。クリッピング・自動刻み変更・代替解法への切替を行わず、未収束は失敗にします。

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

方程式一覧の対応項目は未登録です。個別の式・近似・診断は上の定義に示します。

**問題の図**

![同じ非線形反応拡散でLie–TrotterとStrangを比較する：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/reaction-diffusion-splitting.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja) (`turing-schnakenberg`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja#reaction-diffusion-splitting-ja-validation)

参照は同じFD半離散系を実空間の疎行列・別記述の反応RHSで組み、分割せずRadauで積分した数値解です。Radauの公差細分化と別のDOP853で参照自身の差を測り、最細Strang誤差との比を判定します。ノルムは成分ごとの平均L1・RMS L2・最大L∞を求めて悪い成分を採用し、4つの正の共通出力時刻の最大値で次数を測定。Newton公差感度、全副段階の正濃度、反応source/sink収支と逆順Lieの対照も記録します。

参照解一覧の対応カードは未登録です。この実行例の参照値・判定方法は上の検証資料で確認できます。
### 前提・単位・境界

無次元の1D周期区間[0,2π)、N=32、a=.1,b=.9、D=(.01,1)。u₀=1+.08cos2x+.01cos4x、v₀=.9−.03cos2x−.002cos4xは既存の有限振幅例と同じ初期場です。今回の終時刻はT=1、ステップ数16/32/64/128、共通出力時刻0/.25/.5/.75/1。反射対称・π周期の限定入力です。

### 採用した計算法

Lie–Trotterは拡散h→反応h、Strangは拡散h/2→反応h→拡散h/2。どちらも更新後の状態を次へ渡します。拡散は2次中心FD行列の指数をFFTで厳密適用、反応は同じ陰的中点則・Newton公差2e−13・上限12評価を使用。反応流は厳密解ではなく2次近似です。クリッピング・自動刻み変更・代替解法への切替を行わず、未収束は失敗にします。

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

### 比較・検証

参照は同じFD半離散系を実空間の疎行列・別記述の反応RHSで組み、分割せずRadauで積分した数値解です。Radauの公差細分化と別のDOP853で参照自身の差を測り、最細Strang誤差との比を判定します。ノルムは成分ごとの平均L1・RMS L2・最大L∞を求めて悪い成分を採用し、4つの正の共通出力時刻の最大値で次数を測定。Newton公差感度、全副段階の正濃度、反応source/sink収支と逆順Lieの対照も記録します。

### 確認の限界

固定格子での採用合成法の時間誤差であり、分割誤差と反応中点則の離散誤差を含みます。連続PDEの厳密解・空間収束・独立PDE実装の照合とは呼びません。u+vは反応で保存せず、正濃度は固定入力での観測です。計算費は実際の部分流呼出し数で示し、速度の順位やStrangの一般的優越を主張しません。既存Schnakenberg問題の追加比較で、物理問題数・共通22例・旧配布版の公差や成功履歴を増減・変更しません。長時間パターン・2D・一般境界は対象外です。

### 保存実測値と判定

```json
{
  "metrics": {
    "grid": 32,
    "final_time": 1.0,
    "lie_finest_l2": 0.00048048614019260814,
    "strang_finest_l2": 3.554231191703374e-06,
    "lie_last_observed_order": 1.002936574094834,
    "strang_last_observed_order": 1.9991038173822453,
    "reference_tolerance_linf": 1.98463467881993e-12,
    "reference_algorithm_linf": 2.205471361094169e-10,
    "reference_to_strang_error_ratio": 6.205199499240203e-05,
    "newton_sensitivity_linf": 0.0,
    "reverse_order_l2_difference": 0.007637419068950036,
    "minimum_concentration": 0.8490853839816418,
    "maximum_reaction_balance_error": 1.5942108744226857e-15
  },
  "checks": {
    "lie_error_decreases": true,
    "strang_error_decreases": true,
    "lie_first_order": true,
    "strang_second_order": true,
    "lie_finest_error": true,
    "strang_finest_error": true,
    "strang_improves_this_input": true,
    "reference_tolerance": true,
    "reference_independent_time_algorithm": true,
    "reference_error_separated": true,
    "newton_error_separated": true,
    "reaction_converged": true,
    "reaction_source_balance": true,
    "positive_on_tested_substeps": true,
    "noncommuting_order_control": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs-initial.json

### 出典と確認範囲

- H. F. Trotter (1959). On the product of semi-groups of operators. https://doi.org/10.1090/S0002-9939-1959-0108732-6; review_level=metadata
  AMSの書誌を確認。半群の積公式の原著として引用し、非有界作用素の仮定・証明全体は監査していません。有限次元の次数は本章で直接展開します。
- G. Strang (1968). On the Construction and Comparison of Difference Schemes. https://doi.org/10.1137/0705041; review_level=metadata
  今回の追加では出版社の書誌を確認。対称分割の原著と、合成式・次数を参照したHairerの著者公開講義を区別します。原著全体の新たな監査ではありません。
- E. Hairer (2010). Geometric Numerical Integration, Lecture2. https://www.unige.ch/~hairer/poly_geoint/week2.pdf; review_level=full-text
  著者公開Lecture 2第5節、印刷12–14頁、式(23)–(27)と厳密流・数値流の議論を参照。Lie–Trotter、対称な2次合成、分離Hamilton系の例を確認。講義全体の監査ではありません。
- J. Schnakenberg (1979). Simple chemical reaction systems with limit cycle behaviour. https://pubmed.ncbi.nlm.nih.gov/537379/; review_level=official-bibliography-and-publisher-indexed-abstract
  PubMedの書誌・DOIと出版社索引の抄録を確認。原著本文は403で未取得。反応系の歴史的出典であり、a=.1,b=.9や今回の空間計算を原著の再現とは呼びません。
- The SciPy community (2024). SciPy1.14.1 solve_ivp reference. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.integrate.solve_ivp.html; review_level=official-versioned-documentation-selected-methods-and-tolerances
  SciPy 1.14.1公式資料のmethod・rtol/atolを参照。Radau 5次とDOP853 8次は同じ空間離散の独立した時間積分法として用い、連続PDEの厳密解とは呼びません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
