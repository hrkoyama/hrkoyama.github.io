# 前処理行列・低Mach数・音速点とエントロピー修正

低速での音響剛性を変える前処理と、遷音速での数値散逸の修正を分けて説明します。具体的なΓ、線形モデルの固有値、Machカットオフ、二重時間積分を同じ変数規約で結び付けます。

## 線形方程式の前処理とPDE前処理

Ax=bの左前処理はP⁻¹Ax=P⁻¹bで反復線形解法を助けます。一方、低MachのPDE前処理は擬似時間の質量行列や数値散逸の特性を変えます。両方を同じPという記号で書く文献もありますが、作用する対象を先に明示する必要があります。

低Mach数では対流速度|u_n|に対して音響速度|u_n±a|が大きく、定常反復と低速の流束精度に問題が出ます。これと、u_n±a=0になる遷音速点は別の極限です。

## Γは擬似時間側に置く

保存変数Uとprimitive変数qを区別し、擬似時間τと物理時間tを分けます。定常問題では物理時間項を0にし、非定常問題ではBDF2などで離散化した物理時間項を内側の擬似時間反復中にも残します。ΓとU_qは別の行列です。

Γが可逆で同じRを使うなら、擬似時間が十分収束したときの定常方程式はR=0です。ただし空間流束の散逸も前処理する場合はR自体の離散構成も変わります。物理時間微分を無差別に前処理すると、音波を含む時間依存解は変わります。

$$
\Gamma(q)\frac{\partial q}{\partial\tau}+\frac{\partial U(q)}{\partial t}+R(U(q))=0,\qquad q=(p,u,v,w,T)^T.
$$

## Weiss–Smith型の具体的な行列

以下は熱的・熱量的に完全な理想気体について、q=(p,u,v,w,T)、全比エンタルピーH=c_pT+(u²+v²+w²)/2を使う表現です。c_pは一定、ρ_T=(∂ρ/∂T)_p、aは物理音速です。Θが通常の圧力に対する密度微分を置き換えます。一般の実在流体へこの理想気体の式をそのまま使いません。

U_ref=aならΘ=ρ/pとなり、Γはこの変数順序での物理Jacobian U_qへ戻ります。U_refを流速の尺度へ落とすと、擬似音響速度の尺度を変えられます。文献のΓと、その逆行列や保存変数系のPは同じ数値行列ではありません。

$$
\Gamma=\begin{pmatrix}\Theta&0&0&0&\rho_T\\\Theta u&\rho&0&0&\rho_Tu\\\Theta v&0&\rho&0&\rho_Tv\\\Theta w&0&0&\rho&\rho_Tw\\\Theta H-1&\rho u&\rho v&\rho w&\rho_TH+\rho c_p\end{pmatrix},\qquad\Theta=\frac1{U_{\rm ref}^2}-\frac{\rho_T}{\rho c_p},\quad\rho_T=-\frac\rho T.
$$

## 淀み点の特異化とMachカットオフ

代表的な有界係数は以下です。M_cutは正の下限で、M=0でU_refが0になる特異化を防ぎます。上限1は超音速で物理系へ戻すためのものです。これは一般的な例であり、粘性尺度・非定常の時間尺度・境界条件に応じた改良版では係数が異なります。

ここで回避しているのはゼロ流速に伴う前処理行列の特異化であり、物理的なMach 1の流れを計算領域から除くことではありません。カットオフが大き過ぎると低Machでの改善を弱め、小さ過ぎると頑健性や境界処理に影響します。

$$
M=\frac{\|\mathbf u\|}{a},\quad\beta=\min(1,\max(M,M_{\rm cut})),\quad U_{\rm ref}=\beta a,\quad 0<M_{\rm cut}\le1.
$$

## 固有値がどう変わるか

効果を明示するため、一定密度・音速の基準状態まわりで、圧力摂動をρ₀aで割った変数と法線速度・接線速度・エントロピー変数を使う線形モデルを考えます。エントロピー変数の一定スケーリングは任意です。以下のPは説明用の圧力行スケーリングで、上の非線形Γそのものではありません。

βがMach数と同程度で非零なら、低速の音響固有値も対流と同じ速度尺度になります。ただし行列の2ノルム条件数は特異値の比で、固有値の絶対値比と一般には一致しません。正規性、変数の規格化、境界条件と離散化まで含めて調べます。

$$
A=\begin{pmatrix}u_n&a&0&0\\a&u_n&0&0\\0&0&u_n&0\\0&0&0&u_n\end{pmatrix},\quad P=\operatorname{diag}(\beta^2,1,1,1),\quad q_\tau+PAq_x=0.
$$

$$
\lambda_{\pm}=\frac{(1+\beta^2)u_n\pm\sqrt{(1-\beta^2)^2u_n^2+4\beta^2a^2}}2,\quad\lambda_0=u_n\ (\text{twice}),\quad\lambda_+\lambda_-=\beta^2(u_n^2-a^2).
$$

$$
\kappa_2(A)=\sigma_{\max}(A)/\sigma_{\min}(A),\qquad\chi_\lambda(A)=\max_i|\lambda_i|/\min_{\lambda_i\ne0}|\lambda_i|.
$$

## 前処理だけでは音速点のゼロ固有値は消えない

上のモデルではu_n²=a²で音響固有値の積が0です。一般にも可逆Pを左から掛けただけでは、Aの零固有値を消せません。したがって「前処理行列を掛ければ音速点を消せる」とは説明しません。音響固有値を全方向で等方化しようとする特定の前処理に現れるsonic singularityも、個別の式を指定して議論する必要があります。

$$
\det(PA)=\det(P)\det(A),\qquad P\text{ nonsingular}.
$$

## 遷音速希薄波とエントロピー修正

Roeの線形化は、希薄波の中で特性速度が0を横切る場合に非物理的な膨張衝撃波を作ることがあります。代表的な平滑化では散逸に使う|λ|を下式へ置き換えます。δは速度の次元を持ち、状態から決める方法と一定割合で与える方法は異なります。

これは物理的なλを消す操作ではなく、数値粘性関数を変更する処理です。掲載コードの音響波への二次平滑化を、全Harten–Hyman方式の忠実な再現とは呼びません。また、エントロピー修正、HLLEの低密度時の頑健性、carbuncle対策、低Mach前処理は目的の異なる処理です。

$$
\psi_\delta(\lambda)=\begin{cases}|\lambda|,&|\lambda|\ge\delta,\\(\lambda^2+\delta^2)/(2\delta),&|\lambda|<\delta,\end{cases}\qquad\delta>0.
$$

## 比較・検証で分けて測る量

行列を掛ける前後の固有値、β→1の物理Jacobianへの復帰、低Machでの速度尺度、淀み点近くの可逆性を小さい線形問題で調べます。Γによる擬似時間収束と、空間流束を変えたときの解の誤差も別々に測ります。境界からの反射は、内部の固有値だけの解析で判断できません。

遷音速のスカラーBurgers希薄波やEuler希薄波では、膨張衝撃波の有無、格子収束、δ依存を調べます。非定常計算は物理時間の収束と内側擬似残差を分けて確認します。ここでの前処理検証は今後の計画であり、公開済みのJacobi行列スケーリングや二重時間の例を低Mach流体ソルバーの検証に流用しません。

## 公開範囲

専用の固定入力例として、数値散逸行列をMiczek系の行列で前処理する2次元等エントロピー渦のコードと検証を追加しました。両Roe流束に無制限primitive MUSCLを用い、背景Mach数.1/.01・3格子の12計算を、元の物理時間と音響CFLによるSSPRK(3,3)でT=.1まで進めます。実行・検証先は https://hrkoyama.github.io/numerical-methods-atlas/validation/low-mach-vortex/?lang=ja です。擬似時間の質量行列Γ、Weiss–Smith法、二重時間積分、定常収束の加速は引き続き解説のみです。この数値散逸側の例で、それらの実装や物理音響刻み制約の除去を検証したとは扱いません。初回の区分定数計算の圧力判定不合格と、以前の版別検証記録を保持します。

## 文献

- Turkel, Eli (1987). Preconditioned methods for solving the incompressible and low speed compressible equations. https://doi.org/10.1016/0021-9991(87)90084-2
- Jonathan M. Weiss and Wayne A. Smith (1995). Preconditioning applied to variable and constant density flows. https://doi.org/10.2514/3.12946
- David L. Darmofal and Pierre Moinier and Michael B. Giles (2000). Eigenmode Analysis of Boundary Conditions for the One-Dimensional Preconditioned Euler Equations. https://doi.org/10.1006/jcph.2000.6472
- Ami Harten (1983). High resolution schemes for hyperbolic conservation laws. https://doi.org/10.1016/0021-9991(83)90136-5
- Roe, Philip L. (1981). Approximate Riemann solvers, parameter vectors, and difference schemes. https://doi.org/10.1016/0021-9991(81)90128-5
