# 角特異性・曲線座標・Neumann／Robin境界

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mesh-boundary/

この章に登録された手法・問題・実行例の関連資料です。 L字特異解のP1 FEM、環状領域の可変粘性ベクトルQ1 PDE、純Neumannの互換条件・平均ゲージ、混合Robinの製造解を実際に解きます。

## 手法

- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja>)
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)

  面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。
- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja>)

  polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。
- [可変粘性のベクトル応力境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja>)

  Cartesianの2成分を結合した線形応力発散BVPです。極座標内のQ1基底と正確な曲線Jacobianを使い、可変μの勾配と剪断応力を含みます。圧力・非圧縮拘束・対流項はありません。 1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。
- [可変粘性のベクトル応力境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#variable-viscosity-vector-ja>)

  Cartesianの2成分を結合した線形応力発散BVPです。極座標内のQ1基底と正確な曲線Jacobianを使い、可変μの勾配と剪断応力を含みます。圧力・非圧縮拘束・対流項はありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-algorithm>)

  面積と物理勾配からP1剛性を組み、境界を消去して疎直接法で解きます。隅要素は原点をDuffy写像の頂点に移し、Gauss48/96を比較。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-algorithm>)

  polarのmapped Q1にCartesian速度2成分を置き、r dr dthetaで2mu epsilonの弱形式を4×4 Gauss積分してblock疎解法。円周faceにはr dthetaと外向き法線を使う。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-algorithm>)

  共有面差分で特異行列を組み、体積重み平均のLagrange拘束付き疎直接法とcompatible CGを照合。物理的な不適合外力の平均を勝手に引かない。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-algorithm>)

  半セル距離を用いてRobin境界値を消去し、外向きgradientの面積積分を離散式と同じ重みで評価。

## 問題の図

- [L字領域P1特異解：graded格子と歪みの分離](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem-preview.png
- [環状領域の可変粘性・真2DベクトルMMS](<https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms-preview.png
- [純Neumannの互換条件と平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann-preview.png
- [2D混合Robinの製造解と境界流束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin-preview.png
- [L字領域P1特異解：graded格子と歪みの分離](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/lshape-fem.png
- [環状領域の可変粘性・真2DベクトルMMS](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/annular-viscous-mms.png
- [純Neumannの互換条件と平均値ゲージ](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-neumann.png
- [2D混合Robinの製造解と境界流束](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/mesh-boundary/results/poisson-robin.png

## 厳密解・参照解

- [L字領域P1特異解：graded格子と歪みの分離：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lshape-fem/?lang=ja#references-ja>)

  L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。
- [L字角の特異解：調和場と別の滑らかな製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。角の解析解と勾配を要素求積し、一様格子と事前graded格子を同じ自由度で比べます。別の単位正方形でsin(πx)sin(πy)をregular/warped格子へ置き、特異性と歪みを分けます。 特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。
- [環状領域の可変粘性・真2DベクトルMMS：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/annular-viscous-mms/?lang=ja#references-ja>)

  独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。
- [環状粘性ベクトルMMS：独立応力微分で外力を確認](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。s=x²+y²、A=(s−1)(4−s)のCartesianベクトル場から応力と外力を解析的に導き、別のCartesian差分応力微分で確認します。体積外力の独立積分(756π/5,0)も照合します。 線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。
- [純Neumannの互換条件と平均値ゲージ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-neumann/?lang=ja#references-ja>)

  L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。
- [純Neumann：解析場・互換条件・平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。u=cos(2πx)cos(2πy)、f=8π²u、外向き法線流束0を点DOFで比較します。平均0と平均.25を分け、source+1の物理的不適合を投影で隠さず拒否します。 同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。
- [2D混合Robinの製造解と境界流束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-robin/?lang=ja#references-ja>)

  2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。
- [混合Robin：2次元解析場と独立な法線流束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。f=5π²cos(πx)cos(2πy)を使い、x壁は外向きNeumann±1、y壁はαu+β∂nu=gの解析値です。境界条件の代数残差と、解析的な物理法線流束の誤差を別々に測ります。 Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。
- [L字角の特異解：調和場と別の滑らかな製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja>)
  reference_kind: analytic

  解析解 第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。角の解析解と勾配を要素求積し、一様格子と事前graded格子を同じ自由度で比べます。別の単位正方形でsin(πx)sin(πy)をregular/warped格子へ置き、特異性と歪みを分けます。
- [環状粘性ベクトルMMS：独立応力微分で外力を確認](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja>)
  reference_kind: manufactured

  製造解 1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。s=x²+y²、A=(s−1)(4−s)のCartesianベクトル場から応力と外力を解析的に導き、別のCartesian差分応力微分で確認します。体積外力の独立積分(756π/5,0)も照合します。
- [純Neumann：解析場・互換条件・平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja>)
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。u=cos(2πx)cos(2πy)、f=8π²u、外向き法線流束0を点DOFで比較します。平均0と平均.25を分け、source+1の物理的不適合を投影で隠さず拒否します。
- [混合Robin：2次元解析場と独立な法線流束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja>)
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。f=5π²cos(πx)cos(2πy)を使い、x壁は外向きNeumann±1、y壁はαu+β∂nu=gの解析値です。境界条件の代数残差と、解析的な物理法線流束の誤差を別々に測ります。
- [L字領域P1特異解：graded格子と歪みの分離：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja#lshape-fem-ja-validation>)

  L2/H1積分誤差・求積差、一様/gradedの同DOF改善、別のsquare/warped系列、最小角・aspect・1ノルム条件数推定・真の線形残差を保存。
- [L字角の特異解：調和場と別の滑らかな製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-lshape-fem-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 第4象限を除いた[-1,1]²、theta∈[0,3pi/2]、u=r^(2/3)sin(2theta/3)、解析Dirichlet。N8/16/32、graded map x→x max(|x|,|y|)。正方形sin(pi x)sin(pi y)を同Nのregular/warpedで別検査。角の解析解と勾配を要素求積し、一様格子と事前graded格子を同じ自由度で比べます。別の単位正方形でsin(πx)sin(πy)をregular/warped格子へ置き、特異性と歪みを分けます。 特異解に正方形のL2二次を要求しません。固定の事前graded写像でありAMRソフトではありません。条件数は推定で、任意歪みへの保証はしません。
- [環状領域の可変粘性・真2DベクトルMMS：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja#annular-viscous-mms-ja-validation>)

  独自解析外力を別のCartesian応力差分で資格確認。L2速度/歪み/traction細分化、反力/体積外力と物理tractionの収支、粘性散逸と外力仕事を別々に測定。 体積外力の解析積分(756pi/5,0)も別に照合。
- [環状粘性ベクトルMMS：独立応力微分で外力を確認](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-annular-viscous-mms-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 1≤r≤2、theta周期、mu=1+.2r²、lambda=0、両円でu=0。A(s)=(s−1)(4−s)、u=(A(1+xy),A(x²−y²)/2)。Nr8/16/32、Ntheta=2Nr。s=x²+y²、A=(s−1)(4−s)のCartesianベクトル場から応力と外力を解析的に導き、別のCartesian差分応力微分で確認します。体積外力の独立積分(756π/5,0)も照合します。 線形vector粘性BVPです。divfree拘束・圧力・非線形Navier–Stokesは含めません。原点なしのr>0であり、軸stencil検証ではありません。
- [純Neumannの互換条件と平均値ゲージ：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja#poisson-neumann-ja-validation>)

  L2細分化、零空間、平均、CG差、source+1拒否、境界流束/体積源の収支を保存。
- [純Neumann：解析場・互換条件・平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-neumann-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、セル中心の点DOF。cos(2pi x)cos(2pi y)、全壁Neumann0、平均0とN32の平均.25診断。u=cos(2πx)cos(2πy)、f=8π²u、外向き法線流束0を点DOFで比較します。平均0と平均.25を分け、source+1の物理的不適合を投影で隠さず拒否します。 同じ半離散系の別線形解法は独立PDE参照ではありません。既存Dirichlet MGの成功や2D任意境界へ一般化しません。
- [2D混合Robinの製造解と境界流束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja#poisson-robin-ja-validation>)

  2D解/誤差、真の残差、Robin関係残差と解析法線flux誤差、3格子細分化と積分収支を保存。
- [混合Robin：2次元解析場と独立な法線流束](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-robin-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形N16/32/64、u=cos(pi x)cos(2pi y)+x+y。x壁Neumann±1、y壁alpha1,beta.5の解析Robin。f=5π²cos(πx)cos(2πy)を使い、x壁は外向きNeumann±1、y壁はαu+β∂nu=gの解析値です。境界条件の代数残差と、解析的な物理法線流束の誤差を別々に測ります。 Robin問題は一意なので平均ゲージを重ねません。境界条件の代数残差と物理flux精度を区別します。

## コード・検証

- [環状領域の可変粘性・真2DベクトルMMS](<https://hrkoyama.github.io/numerical-methods-atlas/validation/annular-viscous-mms/?lang=ja>)
  availability: run

  軸を除く円環で可変粘性の応力発散方程式を実際に解き、速度・歪み・境界tractionと仕事を照合します。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja>)
  availability: run

  非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。
- [L字領域P1特異解：graded格子と歪みの分離](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja>)
  availability: run

  再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。
- [純Neumannの互換条件と平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja>)
  availability: run

  特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。
- [2D混合Robinの製造解と境界流束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-robin/?lang=ja>)
  availability: run

  2D PoissonのNeumann/Robin面を実際に組み、連続製造解と境界fluxを照合します。
- [Q1有限要素法（スカラー拡散・曲線座標ベクトルBVP）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/q1-fem/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
