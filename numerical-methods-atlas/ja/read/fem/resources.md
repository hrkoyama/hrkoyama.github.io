# 連続有限要素法：弱形式から疎行列の組立てへ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [スペクトル要素法（SEM）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-poisson-2d-sine-ja>)

  CG/MGは15/31/63内部点、P1 FEMは4/8/16分割。FEMの値誤差L2と勾配誤差H1半ノルムは要素内で評価する。単一固有モードのCG反復数は一般的速度比較に用いない。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。

## 問題の図

- [2次元Poisson・正弦単一モード（FEMを含む）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png

## 厳密解・参照解

- [2次元Poisson・正弦単一モード（FEMを含む）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja>)

  単位正方形の製造解sin(πx)sin(πy)を使い、差分・連続P1 FEMの格子誤差と、補助AMG例の離散参照を確認します。 追加のamg-conditioningは既知の代数解を使う条件数・残差診断で、物理問題への紐付けはありません。このPoisson問題の格子精度・独立参照の証拠として流用しません。 解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [2次元Poisson：CG・多重格子とP1 FEM：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja#poisson-2d-sine-ja-validation>)

  CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

## コード・検証

- [2次元Poisson：CG・多重格子とP1 FEM](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja>)
  availability: run

  単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。
- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja>)
  availability: run

  単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。
- [L字領域P1特異解：graded格子と歪みの分離](<https://hrkoyama.github.io/numerical-methods-atlas/validation/lshape-fem/?lang=ja>)
  availability: run

  再入隅の調和特異解を真の2D P1で解き、同じ未知数の一様/graded格子と、独立した滑らかな正方形の歪みを比較します。
- [行列から粗視化するAMG：残差と解誤差を分ける](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja>)
  availability: run

  正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。
- [連続P1 Galerkin有限要素法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
