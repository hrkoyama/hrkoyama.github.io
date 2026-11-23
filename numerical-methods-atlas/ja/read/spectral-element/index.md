# スペクトル要素法：高次の有限要素と2D Poisson

スペクトル要素法：高次の有限要素と2D Poisson

スペクトル要素法（SEM）は、領域を要素に分け、各要素の中を高次多項式で近似する方法です。有限要素法の幾何学的な分割と、滑らかな関数を高次で表す考え方を結びます。ここでは連続Galerkin型のLegendre GLL変種を、手元で再実行できる2D Poisson問題から学びます。

要素ごとの高次多項式をつなぐ


$$
u_h|_{K_e}(\xi,\eta)=\sum_{i,j=0}^{p}U^e_{ij}\ell_i(\xi)\ell_j(\eta),\qquad u_h\in C^0(\Omega)
$$
ξ・ηは各正方形を[−1,1]²に写した参照座標です。隣り合う要素の境界節点を共有し、関数値をC0連続に組み立てます。導関数まで連続にする条件ではありません。SEMは高次有限要素法の一群であり、有限要素法全般を一次要素に限定する呼び方ではありません。領域全体を一組のFourier基底で表す方法とも分けて考えます。

Poisson方程式の弱形式から出発する


$$
\int_\Omega\nabla v_h\cdot\nabla u_h\,d\Omega=\int_\Omega v_h f\,d\Omega,\qquad v_h|_{\partial\Omega}=0
$$
−Δu=fに試験関数vを掛け、部分積分して微分を両者へ一つずつ配ります。零Dirichlet境界では境界項が消えます。以下の実装は一定係数・アフィン正方形だけを対象にし、この積分をGLL求積で近似します。

GLL節点・求積と行列


$$
(1-\xi_i^2)P_p^\prime(\xi_i)=0,\qquad w_i=\frac{2}{p(p+1)P_p(\xi_i)^2},\qquad i=0,\ldots,p
$$

$$
D_{ij}=\ell_j^\prime(\xi_i),\quad W=\operatorname{diag}(w_i),\quad S=D^TWD,\quad K_e=\frac{h_y}{h_x}S\otimes W+\frac{h_x}{h_y}W\otimes S
$$

$$
b^e_{ij}=\frac{h_xh_y}{4}w_iw_jf(x_{e,i},y_{e,j}),\qquad KU=b
$$
p次Legendre多項式Ppの導関数の根と両端点がp+1個のGLL節点です。1D求積の厳密次数は2p−1。節点値を自由度に選ぶと求積質量は対角になりますが、一般の2p次の積まで厳密に積分した質量行列とは異なります。2Dの剛性も横方向の積を含むため、求積の規約を明記する必要があります。コードはテンソル積の局所剛性と右辺を疎に組み立て、境界値を消去して解きます。

既存のP1有限要素法との比較



既存のP1有限要素法との比較

| 比較点 | 既存のP1 FEM | 今回のGLL-SEM |
| --- | --- | --- |
| 要素内の近似 | 三角形上の一次多項式 | 正方形上のテンソル積Qp多項式 |
| 要素間の接続 | C0連続 | C0連続 |
| 求積 | Duffy変換によるGauss積分 | GLL節点での剛性・荷重求積 |
| 精度を増やす操作 | 主にh細分化 | h細分化とp増加を分けられる |
| 今回の連立解法 | 既存NumartのILU(0)・GMRES | SciPyの疎な直接解法 |
| 比較で揃えるもの | 方程式・境界・製造解・自由未知数 | 同じ条件。速度の優劣は判定しない |

軽量実行例：2D Poissonのh/p収束


$$
\Omega=(0,1)^2,\quad u_*=\sin(\pi x)\sin(\pi y),\quad f=2\pi^2u_*,\quad u|_{\partial\Omega}=0
$$
p=2のSEMで各方向2/4/8要素、既存の三角形P1 FEMで4/8/16分割を使います。自由未知数は両者とも9/49/225です。さらに2×2要素を固定しp=1〜6を実行します。比較用P1 FEMのソースと依存モジュールは、公開済みNumart版とバイト一致で同梱し、元の配布版を保持しています。

[](/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png)実際の保存場と誤差の図。節点誤差の画像と、領域内を積分した誤差ノルムは別の量です。残差・連続誤差・観測次数を区別する


$$
E_{L^2}=\left[\int_\Omega(u_h-u_*)^2\,d\Omega\right]^{1/2},\quad E_{H^1}=\left[\int_\Omega|\nabla u_h-\nabla u_*|^2\,d\Omega\right]^{1/2}
$$

$$
E_{L^2}\sim h^{p+1},\qquad E_{H^1}\sim h^p\quad\text{(smooth solution and resolved quadrature)}
$$
誤差はGLL節点だけでなく、要素内の別の高次Gauss点で積分します。小さい連立方程式の残差だけでは連続PDEの小さい誤差を意味しません。この滑らかな固定問題の最後のh細分化では、p2 SEMのL2観測次数は約3.04、H1半ノルムは約2.01。P1 FEMはそれぞれ約1.97と0.99です。自由未知数225でのL2誤差はSEM約2.49×10⁻⁴、P1約5.38×10⁻³でした。p6・2×2要素のL2誤差は約3.78×10⁻⁷です。

滑らかさ、境界、要素の形、求積と解法に依存する結果です。特異点や不連続係数で同じp収束を保証せず、この一例からSEMが常に速い・優れるとは結論しません。曲線要素、圧力との混合空間、流体の連成は今回の実行範囲に含めません。

関連実装：Nek5000とnekRS

[Nek5000](https://nek5000.github.io/NekDoc/theory.html)は高次のスペクトル要素流体ソルバーです。[nekRS](https://github.com/Nek5000/nekRS)はCPU/GPUに対応する関連する後継実装として、[公式プロジェクト](https://nek5000.github.io/)から資料・ソースへ進めます。ここで実行した小さなPythonのPoisson例は、その流体ソルバーや性能を再現・検証したものではありません。Pateraの原報は起源をたどる書誌として挙げ、今回のLegendre GLL変種と区別します。

[既存の有限要素法](/numerical-methods-atlas/ja/read/fem/) · [不連続な要素を使うFR・DGとの比較](/numerical-methods-atlas/ja/read/flux-reconstruction/)

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較

固定標的の計算例

単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。

滑らかな固定問題だけの結果。要素・求積・代数ソルバーが異なるので、速度・計算量・汎用的優位性の比較ではありません。GLLの対角求積質量は一般の積の厳密な質量行列ではない。曲線格子・特異解・非圧縮流体・Nek5000/nekRS本体は未実行。

[入力・結果・受入条件](/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-sem-fr/#sem-poisson-2d) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/run.py) · [コード sem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/sem.py) · [コード polynomials.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/polynomials.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/experiments.py) · [コード fem.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/fem.py) · [コード krylov.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/krylov.py) · [コード fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/fr.py) · [コード advection.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/advection.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/solvers.py) · [コード riemann.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/riemann.py) · [コード equations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/equations.py) · [コード limiters.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/legacy/limiters.py) · [テスト test_sem_fr.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/test_sem_fr.py) · [ZIP](/code/validated-examples/2026-11-23/sem-fr/atlas-sem-fr-2026-11-23.zip) · [結果](/code/validated-examples/2026-11-23/sem-fr/results/result.json) · [追試記録](/code/validated-examples/2026-11-23/sem-fr/verification.json)

## 公開範囲

この章に対応する専用の軽量コード・固定入力・保存場・判定と、ZIP独立展開で再実行した25検査を公開します。関連する外部ソフトは公式資料の紹介であり、導入・動作検証済みの表示ではありません。

## 文献

- A. T. Patera (1984). A spectral element method for fluid dynamics: Laminar flow in a channel expansion. https://doi.org/10.1016/0021-9991(84)90128-1
- Nek5000 development team (2026). Nek5000 documentation: Theory and spectral-element basis (accessed 2026-11-23). https://nek5000.github.io/NekDoc/theory.html
- Nek5000/RS development team (2026). Nek5000/RS project: spectral-element solvers and related implementations (accessed 2026-11-23). https://nek5000.github.io/
