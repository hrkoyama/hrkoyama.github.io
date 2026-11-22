# 連続有限要素法：弱形式から疎行列の組立てへ

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/fem/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
- [代数的マルチグリッド（AMG）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/amg/?lang=ja>)

  この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。
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

  単位正方形の製造解sin(πx)sin(πy)を使い、差分・連続P1 FEMの格子誤差と、補助AMG例の離散参照を確認します。 追加のamg-conditioningは既知の代数解を使う条件数・残差診断で、物理問題への紐付けはありません。このPoisson問題の格子精度・独立参照の証拠として流用しません。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2次元Poisson：CG・多重格子とP1 FEM：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja#poisson-2d-sine-ja-validation>)

  CSVのmethod_codeは0=CG、1=多重格子、2=P1 FEM。各方式の最細格子と境界点で、同一行座標の解析解を付す。resolutionはFDで内部点数、FEMで三角形分割前の軸方向分割数。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。

## コード・検証

- [2次元Poisson：CG・多重格子とP1 FEM](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja>)
  availability: run

  単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。
- [行列から粗視化するAMG：残差と解誤差を分ける](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sa-amg/?lang=ja>)
  availability: run

  正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。
- [連続P1 Galerkin有限要素法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
