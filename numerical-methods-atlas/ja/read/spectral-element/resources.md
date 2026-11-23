# スペクトル要素法：高次の有限要素と2D Poisson

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/spectral-element/

この章に登録された手法・問題・実行例の関連資料です。 新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。

## 手法

- [スペクトル要素法（SEM）](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja>)
- [連続P1 Galerkin有限要素法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/p1-fem/?lang=ja>)
- [不連続Galerkin法／Legendre](<https://hrkoyama.github.io/numerical-methods-atlas/methods/dg/?lang=ja>)

## 方程式

- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-algorithm>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 SEMはC0連続なテンソル積Qp Lagrange基底・p+1個のLegendre GLL節点と求積、疎な剛性行列・SciPy直接解法を使用。p=2で各方向2/4/8要素、別に2×2要素でp=1〜6。公開済みNumartのP1 FEM・GMRESをファイルのバイト列を保持して4/8/16分割で実行し、両者の自由未知数9/49/225を一致させます。

## 問題の図

- [2次元Poisson・正弦単一モード（FEMを含む）](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/field-fem-poisson.png
- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23/sem-fr/results/sem-poisson-2d.png

## 厳密解・参照解

- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  reference_kind: manufactured

  製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [2次元Poisson・正弦単一モード（FEMを含む）：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-sine/?lang=ja#references-ja>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 単位正方形の製造解sin(πx)sin(πy)を使い、差分・連続P1 FEMの格子誤差と、補助AMG例の離散参照を確認します。 追加のamg-conditioningは既知の代数解を使う条件数・残差診断で、物理問題への紐付けはありません。このPoisson問題の格子精度・独立参照の証拠として流用しません。 解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。
- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja#sem-poisson-2d-ja-validation>)

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 解析的な正弦製造解と勾配を参照し、GLL節点とは異なる高次Gauss点で連続L2誤差・H1半ノルムを積分。h/p収束・自由未知数を揃えた誤差・境界値・真の残差を検査し、実際の2D場とP1の頂点・三角形・解をNPZに保存。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 カードは1次元sin(πx)、こちらは2次元sin(πx)sin(πy)です。次元・右辺・FEMの誤差ノルムは異なります。
- [2D Poisson正弦製造解：SEMとP1 FEMの共通参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sem-poisson-2d-ja>)
  relation: same-problem
  reference_kind: manufactured

  新しい固定入力を実行した範囲で、手法・式・既存の物理問題・解析/製造参照・配布コードを対応させます。関連する外部ソフトの動作検証は含みません。 製造解 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。 全て無次元。−Δu=2π²sin(πx)sin(πy)、領域[0,1]²、境界u=0。係数は一定、SEMは直交するアフィン正方形、FEMは既存の規則的な三角形分割。

## コード・検証

- [スペクトル要素法の2D Poisson：P1 FEMとh/p収束を比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sem-poisson-2d/?lang=ja>)
  availability: run

  単位正方形の正弦製造解をGLLスペクトル要素法と既存P1三角形FEMで解きます。自由未知数を揃えたh細分化と、固定要素数でのp=1〜6を分けて測ります。
- [スペクトル要素法（SEM）：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/spectral-element/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
