# PINN・ニューラル演算子

PINNは特定の問題の近似解をニューラル関数として学習し、neural operatorは係数場や初期条件から解の関数への写像を学びます。同じニューラルネットでも、学習対象と検証方法が違います。

## 対象と代表式

PINNではu_θのPDE残差、境界残差、データ残差を重みλで足した経験損失を最小化します。NとBはPDE・境界演算子、f,gは与えた右辺です。FNOはvを特徴関数とし、Fourier空間の積分核Kと局所作用Wを組み合わせる層の代表形を使います。

$$
\mathcal L(\theta)=\lambda_r\langle|\mathcal N[u_\theta]-f|^2\rangle_r+\lambda_b\langle|\mathcal B[u_\theta]-g|^2\rangle_b+\lambda_d\langle|u_\theta-u_{\rm obs}|^2\rangle_d.
$$

$$
v_{\ell+1}=\sigma\!\left(W_\ell v_\ell+\mathcal F^{-1}[K_\ell\,\mathcal Fv_\ell]\right).
$$

## 計算の流れ

PINNでは領域と単位をスケーリングし、自動微分で残差を作り、学習点と境界条件の課し方を指定して最適化します。FNOでは入力・参照解の集合で写像を学習し、Fourierモードを有限数に切ります。原PINN論文とFNO論文は別の提案です。

## 適用条件と落とし穴

小さい訓練損失は、領域全体の小さい解誤差や保存則の保証ではありません。残差項の不均衡、衝撃波、硬い尺度、学習分布外の入力を調べます。格子間転送の可能性と、任意解像度で正しい物理を再現する保証も区別します。

## 検証するときに見る量

解析解または独立に収束させた従来法と比較し、学習点外のL1/L2/L∞誤差、境界・保存則、複数seedを測ります。operator学習では同じ軌道の近接時刻を無作為分割するだけでなく、問題単位でtrain/testを分け、入力分布外も別報告します。

## 公開範囲

解説・代表式・文献を公開しています。専用コードと数値検証結果は実装予定です。上記の検証案は未実施で、他の手法のコードや計算結果をこの手法の検証として流用しません。

## 文献

- M. Raissi and P. Perdikaris and G.E. Karniadakis (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. https://doi.org/10.1016/j.jcp.2018.10.045
- Zongyi Li and Nikola Kovachki and Kamyar Azizzadenesheli and Burigede Liu and Kaushik Bhattacharya and Andrew Stuart and Anima Anandkumar (2021). Fourier Neural Operator for Parametric Partial Differential Equations. https://openreview.net/forum?id=c8P9NQVtmnO
