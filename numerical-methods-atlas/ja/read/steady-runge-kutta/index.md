# 定常解のためのダンピングRunge–Kutta反復

定常解を求めるダンピングルンゲクッタ（damping Runge–Kutta）反復を、擬似時間で残差を減らす多段RKスムーザーとして読む章です。Jameson–Schmidt–Turkel系の反復を例に、段係数、安定性多項式、非線形次数、高周波減衰、前処理との関係を整理します。

## 目的は物理時間の軌道ではなくR(U)=0

定常Euler・Navier–Stokesなどの離散残差Rに対し、擬似時間τの常微分方程式を反復して根を求めます。ここではセル体積で割った保存変数の残差をRとし、反復の時間刻みは擬似時間幅です。物理時間の過渡履歴の精度ではなく、残差と定常量が所要精度へ達することを目指します。

各段を同じ基準U^(0)から作る以下の形式は、直前の段からEulerステップを足し続ける方式とは違います。残差の符号、セル体積、前処理作用素を含めた定義をそろえて係数を比較します。

$$
\frac{dU}{d\tau}=-R(U),\quad U^{(0)}=U^n,\quad U^{(k)}=U^{(0)}-\alpha_k\Delta\tau R(U^{(k-1)}),\quad U^{n+1}=U^{(s)}.
$$

## Jameson系4段反復の代表例

以下の係数を用い、各段で同じ自律残差を再評価する例を考えます。線形問題R(U)=AUでは安定性多項式が古典RK4と同じになります。ただし原著の流束・人工散逸・散逸の更新頻度を含む設計と、この簡略な反復式を同じものとは呼びません。

この一致だけで非線形の物理時間4次精度とは言えません。この基準状態型4段式は一般の非線形自律ODEでは2次までで、3次条件の一つbᵀ(c⊙c)=1/3を満たしません。Jameson型の定常反復と古典RK4は、用途と非線形の次数条件を分けて読む必要があります。

$$
(\alpha_1,\alpha_2,\alpha_3,\alpha_4)=(1/4,1/3,1/2,1),\qquad z=-\Delta\tau\lambda,\quad \mathcal R_4(z)=1+z+z^2/2+z^3/6+z^4/24.
$$

$$
b^Tc=\tfrac12,\qquad b^T(c\odot c)=\tfrac14\ne\tfrac13\quad\text{for the stated base-state four-stage recurrence}.
$$

## 安定領域と高周波減衰は別の評価

線形化した残差の誤差モードに対し、反復の倍率は安定性多項式で決まります。|ℛ|≤1は増幅を防ぎますが、|ℛ|が1に近いと誤差はほとんど減りません。マルチグリッドのsmootherでは、粗格子で表せない高周波集合H上での最大倍率μを小さくする係数・CFLを選びます。

純減衰モードz=−2では上の4段式はℛ=1/3ですが、zが0近傍の低周波誤差はゆっくりしか減りません。安定領域の端まで刻みを上げることが、最大のダンピングや最短の収束を意味するわけではありません。移流と拡散では固有値の位置が異なります。

$$
e^{n+1}=\mathcal R_s(-\Delta\tau A)e^n,\qquad\mu=\max_{\theta\in\mathcal H}\left|\mathcal R_s(-\Delta\tau\lambda_h(\theta))\right|.
$$

## 残差平滑化・前処理・多重格子の役割

残差平滑化は残差へ空間フィルターを作用させる追加操作で、RKの段係数の選び方とは別です。例えば周期一様格子の無次元2階差分D₂とε≥0に対し、下式は高周波残差を弱めます。フィルターが可逆なら同じ残差の根を保ちますが、反復のスペクトルは変わります。

低Mach前処理は音響と対流の速度尺度を変え、局所時間刻みはセルごとの反復幅を変え、粗格子補正はsmootherで減りにくい誤差を扱います。これらを組み合わせる場合でも、物理時間の時刻歴とは区別し、境界・可変係数・非正規性を含めて評価します。

$$
(I-\varepsilon D_2)\overline r=r,\qquad \widehat D_2(\theta)=-4\sin^2(\theta/2),\quad \widehat{\overline r}(\theta)=\frac{\widehat r(\theta)}{1+4\varepsilon\sin^2(\theta/2)}.
$$

## 残差・定常量・コストを測る

製造解PoissonなどでFourierモードごとの減衰を測り、式のμと比較します。圧縮性流では保存変数ごとに規格化した真の残差と、揚抗力・質量流量・保存収支などの定常量を追います。残差を平滑化しているなら、平滑化前の真の残差も必ず表示します。

1サイクルの段数だけでなく、残差評価回数と線形解法の仕事、最終誤差、停止理由を報告します。異なる方式は同じ定常解・同じ許容誤差で比較します。本章はアルゴリズムの解説で、Jameson方式の専用コードや新しい流体検証結果を追加したものではありません。

## 公開範囲

定常多段RK反復の解説のみです。既存の古典RK4・二重時間・多重格子のコードは、Jameson型圧縮性ソルバー全体の実装や検証を意味しません。専用ソルバー・新しい実測結果は今回追加していません。

## 文献

- A. JAMESON and WOLFGANG SCHMIDT and ELI TURKEL (1981). Numerical solution of the Euler equations by finite volume methods using Runge Kutta time stepping schemes. https://doi.org/10.2514/6.1981-1259
- Jameson, Antony (1991). Time dependent calculations using multigrid, with applications to unsteady flows past airfoils and wings. https://doi.org/10.2514/6.1991-1596
- J. C. Butcher (1963). Coefficients for the study of Runge-Kutta integration processes. https://doi.org/10.1017/S1446788700027932
