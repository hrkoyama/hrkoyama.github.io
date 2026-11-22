# Krylov固有値解法

Krylov固有値法は、巨大な行列全体を対角化せず、少数の固有対を小さい部分空間から近似します。Arnoldi、対称問題のLanczos、シフト反転では必要な仮定が異なります。

## 対象と代表式

初期ベクトルvからKₘ(A,v)=span{v,Av,…,Aᵐ⁻¹v}を作ります。直交基底Vₘと上Hessenberg行列HₘのArnoldi関係から、Hₘy=θyを解いてx=VₘyをRitzベクトルとします。最後の基底ベクトルとhₘ₊₁,ₘが残差を表します。

$$
AV_m=V_mH_m+h_{m+1,m}v_{m+1}e_m^T,\qquad \|Ax-\theta x\|_2=|h_{m+1,m}e_m^Ty|\quad(\|y\|_2=1).
$$

## 計算の流れ

行列ベクトル積と直交化で基底を伸ばし、小さい固有値問題を解き、必要に応じて再スタートします。AがHermitianならLanczosの三項漸化式が使えます。内部固有値には(A−σI)⁻¹を作用させる方法がありますが、各作用は線形系の解法を必要とします。

## 適用条件と落とし穴

有限精度では直交性の喪失により重複した見かけの固有値が出ます。非正規行列の小残差は小さい固有値誤差を保証しません。一般化問題Ax=λBxではBの性質と内積を明記し、シフト反転の内部許容誤差も評価します。

小さな固有残差は近い行列の固有対という後退誤差の情報を与えますが、非正規行列で真の固有値・固有ベクトルが近いとは限りません。近接固有値では個々の固有ベクトルの対応付けが不安定になるため、クラスターの不変部分空間を主角などで比較する方が適切な場合があります。

## 検証するときに見る量

正規化した残差∥Ax−θx∥/(∥A∥+|θ|)、直交性、既知固有対、縮退/近接固有値を確認します。対称問題ではRayleigh商も比較し、再スタート数や初期ベクトル依存を記録します。

追加版は固有値間隔と非正規性を分けた小行列で、Krylov空間の大きさや残差に対する固有値誤差・部分空間誤差を独立参照と比較します。残差だけの合格を「真の固有値を高精度に得た」と読み替えず、近接・非正規の対照では条件付けと観測した誤差を併記します。任意の大規模非対称系の保証には広げません。 射影コアと密行列参照はLAPACK基盤を共有し得るため、全面的に独立なバックエンドとは呼びません。解析固有値と構成した擬似固有対の対照も併用します。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### Lanczos・Arnoldi：Ritz値と固有対残差の収束

固定標的の計算例

32・48次の対称／非対称行列でLanczosとArnoldiを自作し、Krylov次元4・8・16による最大実部の固有対の収束を測ります。行列全体を解く独立LAPACK参照と照合します。

非再始動・小行列・分離した極端固有対の教材です。内部固有値、クラスタ、巨大な疎行列、強い非正規性、shift-invertやimplicitly restarted Arnoldiは対象外です。小さな固有対残差だけで非正規行列の固有値誤差の厳密上界とはしません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/krylov-eigenvalues/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations/#krylov-eigenvalues) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [テスト test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations/verification.json)

### Krylov固有値：クラスター部分空間と非正規感度

固定標的の計算例

48次のクラスター固有値と強い非正規上三角行列で、次元4/8/16/32のLanczos・Arnoldiを測ります。残差・前進誤差・固有値条件数・不変部分空間を分けます。

NumPyの射影コアとSciPyの密参照はLAPACK基盤を共有し得るため、全面的に独立なバックエンドとはしません。解析固有値と独立構成対照を併用します。再始動、内部固有値、大規模疎行列、普遍的な単調収束は対象外です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/krylov-eigen-conditioning/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations-conditioning/#krylov-eigen-conditioning) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [コード fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [コード mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [テスト test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## 公開範囲

旧版の入力・測定値・公差を保持し、条件数・残差・収束の追加検証を別の配布版として案内します。診断対照の合格は、その対照で意図した限界を確認した意味を含み、一般的な成功や原論文全体の再現を意味しません。

## 文献

- W. E. Arnoldi (1951). The principle of minimized iterations in the solution of the matrix eigenvalue problem. https://doi.org/10.1090/qam/42792
- C. Lanczos (1950). An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. https://doi.org/10.6028/jres.045.026
- LAPACK authors (1999). Error Bounds for the Nonsymmetric Eigenproblem; Overview. https://www.netlib.org/lapack/lug/node91.html
