# 線形代数：直接法・鞍点系・再始動と整合質量固有値

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-linear-algebra-spectral/

この章に登録された手法・問題・実行例の関連資料です。 小さい固定行列で、行列分解と反復改良、対称不定値の反復解法、再始動固有値解法、整合質量の弦を比較します。独立参照へ照合し、残差と解誤差・代数誤差と離散化誤差・作用回数を分けます。

## 手法

- [部分ピボットLUと混合精度反復改良](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=ja>)
- [Cholesky分解と三角代入](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=ja>)
- [対称不定値系の教育用MINRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja>)
- [SciPy LOBPCGによる一般化固有値比較](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja>)
- [部分ピボットLUと混合精度反復改良](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=ja>)

  手書き部分ピボットLU・下三角Cholesky・前後代入。
- [Cholesky分解と三角代入](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=ja>)

  手書き部分ピボットLU・下三角Cholesky・前後代入。
- [対称不定値系の教育用MINRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja>)

  全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)

  全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)

  二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)

  要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。
- [SciPy LOBPCGによる一般化固有値比較](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja>)

  要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)
- [Krylov固有値解法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/eigensolvers/?lang=ja>)

## 方程式

- [有限次元線形方程式と行列分解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja>)

  有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。 SPD12、低ランク近特異8、Hilbert5、Wilkinson12を固定。binary32因子・三角解法とbinary64残差・補正の5回です。
- [有限次元線形方程式と行列分解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja>)

  有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。 速度12/24、圧力5/11の代数的混合Poisson/Stokes型ブロック。元の真の残差1e-9を共通基準にします。
- [有限次元の行列固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-eigenproblem-ja>)

  主対象は31×31の固定対称行列の標準固有値問題です。行列の離散スペクトルを参照し、連続PDEの空間収束を検査したとはしません。 Dirichlet離散Laplacian31、再始動長8/16、最大40cycle、shiftなし/0/950。
- [固定端弦の固有値と整合質量FEM](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja>)

  単位弦の定常振動形の固有値問題です。整合質量P1の代数固有値誤差と連続体への離散化誤差を分けます。時間発展を実行した例ではありません。 単位弦・張力密度1、同次Dirichlet、内部15/31/63点、最低3固有対。
- [有限次元線形方程式と行列分解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-linear-system-ja>)

  有限行列Aと右辺bの代数問題です。LU/Cholesky・混合精度改良・対称不定値鞍点系を固定例で検査し、連続PDEの解とは区別します。
- [有限次元の行列固有値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-dimensional-eigenproblem-ja>)

  主対象は31×31の固定対称行列の標準固有値問題です。行列の離散スペクトルを参照し、連続PDEの空間収束を検査したとはしません。
- [固定端弦の固有値と整合質量FEM](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#dirichlet-string-eigenproblem-ja>)

  単位弦の定常振動形の固有値問題です。整合質量P1の代数固有値誤差と連続体への離散化誤差を分けます。時間発展を実行した例ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-algorithm>)

  手書き部分ピボットLU・下三角Cholesky・前後代入。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-algorithm>)

  全基底保存のLanczos最小残差LSと二重MGS GMRES。SPD合同変換で対称性を保持。 元入力の残差1e-9と固定前進上限2e-8から、行列のみのκ∞推定で内部目標min(rtol,2e-8/κ∞)を導出。独立解を停止に使わない。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-algorithm>)

  二重MGS Arnoldiを単一Ritzベクトルから明示的に再始動。自前LUでshift線形解を求め、元の固有残差で停止。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-algorithm>)

  要素からK,Mを組み立て、M内積のK^-1M KrylovとSciPy LOBPCGを比較。小規模な厳密K逆前処理。 LOBPCG初期列は{1,x³,x⁶}。K逆Mの次数+2像を初期spanから独立にし、{1,x,x²}の構造的階数欠落を避ける。 同じMの作用を資格済einsumのLinearOperatorで与え、dense-B adapterを通さない。固有値solver自体はSciPy LOBPCG。

## 問題の図

- [部分ピボットLU・Choleskyと反復改良](<https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement-preview.png
- [対称不定値鞍点系とSchur前処理](<https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres-preview.png
- [明示的再始動Krylovと内部固有値](<https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert-preview.png
- [整合質量FEM弦の一般化固有値](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen-preview.png
- [部分ピボットLU・Choleskyと反復改良](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/pivoted-direct-refinement.png
- [対称不定値鞍点系とSchur前処理](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/symmetric-saddle-minres.png
- [明示的再始動Krylovと内部固有値](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/restarted-shift-invert.png
- [整合質量FEM弦の一般化固有値](<https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-24-r3/linear-algebra-spectral/results/fem-mass-eigen.png

## 厳密解・参照解

- [部分ピボットLU・Choleskyと反復改良：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/pivoted-direct-refinement/?lang=ja#references-ja>)

  実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。
- [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pivoted-direct-refinement-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 固定4行列の実binary64 A,bをFractionへ厳密変換し、有理数消去の解を最後にbinary64へ変換。LAPACKは別比較であり共有数値基盤を含みます。任意の悪条件行列に対する前進精度保証ではありません。 小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。
- [対称不定値鞍点系とSchur前処理：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/symmetric-saddle-minres/?lang=ja#references-ja>)

  LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。
- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 A=[[H,Bᵀ],[B,0]]、速度サイズ12/24、圧力行数5/11の代数問題。SPD理想Schurは全行列を小さく直接構成し、元の真残差とdense参照解誤差を別に判定。実Stokes境界値問題ではありません。 理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。
- [明示的再始動Krylovと内部固有値：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/restarted-shift-invert/?lang=ja#references-ja>)

  既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。
- [再始動/shift-invert：固定離散行列の閉スペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-restarted-shift-invert-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 31×31 Dirichlet三重対角行列、h=1/32、再始動長8/16、shiftなし/0/950。参照はこの有限行列の固有値であり、格子細分化による連続PDE収束を認証しません。 単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。
- [整合質量FEM弦の一般化固有値：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/fem-mass-eigen/?lang=ja#references-ja>)

  一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。
- [P1整合質量弦：閉離散固有値と連続体固有値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 長さ・張力・密度1、両端Dirichlet0、内部15/31/63点、最低3固有対。閉離散固有値とgeneralized dense LAPACKを比較し、連続(jπ)²への誤差を別に調べます。表示ベクトルは保存した数値解で、符号は任意です。 小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。
- [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pivoted-direct-refinement-ja>)
  reference_kind: analytic

  解析解 固定4行列の実binary64 A,bをFractionへ厳密変換し、有理数消去の解を最後にbinary64へ変換。LAPACKは別比較であり共有数値基盤を含みます。任意の悪条件行列に対する前進精度保証ではありません。
- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 A=[[H,Bᵀ],[B,0]]、速度サイズ12/24、圧力行数5/11の代数問題。SPD理想Schurは全行列を小さく直接構成し、元の真残差とdense参照解誤差を別に判定。実Stokes境界値問題ではありません。
- [再始動/shift-invert：固定離散行列の閉スペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-restarted-shift-invert-ja>)
  reference_kind: analytic

  解析解 31×31 Dirichlet三重対角行列、h=1/32、再始動長8/16、shiftなし/0/950。参照はこの有限行列の固有値であり、格子細分化による連続PDE収束を認証しません。
- [P1整合質量弦：閉離散固有値と連続体固有値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja>)
  reference_kind: analytic

  解析解 長さ・張力・密度1、両端Dirichlet0、内部15/31/63点、最低3固有対。閉離散固有値とgeneralized dense LAPACKを比較し、連続(jπ)²への誤差を別に調べます。表示ベクトルは保存した数値解で、符号は任意です。
- [部分ピボットLU・Choleskyと反復改良：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja#pivoted-direct-refinement-ja-validation>)

  実binary64入力をFraction有理数で厳密に解き、別のLAPACK DGESV/DPOSVへ照合。条件数・前進誤差・後退誤差を分離。 保存する有理数参照ベクトルは、厳密Fraction解の各成分をbinary64へ丸めたものです。
- [部分ピボットLU/Cholesky：実二進入力の厳密有理数参照](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pivoted-direct-refinement-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 固定4行列の実binary64 A,bをFractionへ厳密変換し、有理数消去の解を最後にbinary64へ変換。LAPACKは別比較であり共有数値基盤を含みます。任意の悪条件行列に対する前進精度保証ではありません。 小さい固定例のみ。一般の高条件数系で混合精度の収束は保証しません。
- [対称不定値鞍点系とSchur前処理：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja#symmetric-saddle-minres-ja-validation>)

  LAPACK全系解、理想Schurの3点スペクトル、CGの明示的負曲率対照。
- [対称不定値鞍点系：独立dense解と理想Schurスペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-symmetric-saddle-minres-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 A=[[H,Bᵀ],[B,0]]、速度サイズ12/24、圧力行数5/11の代数問題。SPD理想Schurは全行列を小さく直接構成し、元の真残差とdense参照解誤差を別に判定。実Stokes境界値問題ではありません。 理想Schurは教育用の稠密制御であり、実Stokes PDEやスケーラブルな近似前処理の完成ではありません。
- [明示的再始動Krylovと内部固有値：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja#restarted-shift-invert-ja-validation>)

  既知の正弦スペクトルと独立な全行列LAPACK。shift解・Krylov作用・元残差作用を別計数。
- [再始動/shift-invert：固定離散行列の閉スペクトル](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-restarted-shift-invert-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 31×31 Dirichlet三重対角行列、h=1/32、再始動長8/16、shiftなし/0/950。参照はこの有限行列の固有値であり、格子細分化による連続PDE収束を認証しません。 単一対称実固有対だけ。暗黙再始動・Krylov-Schur・ロッキング・一般の非正規やクラスターは未実装。
- [整合質量FEM弦の一般化固有値：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja#fem-mass-eigen-ja-validation>)

  一般化dense eigh、独立離散スペクトル、連続体(jπ)^2への細分化。M直交性と元残差は別量。
- [P1整合質量弦：閉離散固有値と連続体固有値](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fem-mass-eigen-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 長さ・張力・密度1、両端Dirichlet0、内部15/31/63点、最低3固有対。閉離散固有値とgeneralized dense LAPACKを比較し、連続(jπ)²への誤差を別に調べます。表示ベクトルは保存した数値解で、符号は任意です。 小規模1D弦のみ。SciPyが返す前の例外では入力を保存し、未返却の内部反復を保存したとはしません。 成分資格35判定は4科学例の合格を代用せず、元SciPy内部の未返却反復は保存済みとしません。

## コード・検証

- [部分ピボットLU・Choleskyと反復改良](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pivoted-direct-refinement/?lang=ja>)
  availability: run

  独立の厳密有理数解と比較し、条件数・前進誤差・後退誤差・ピボット増大を分けます。
- [対称不定値鞍点系とSchur前処理](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja>)
  availability: run

  同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。
- [整合質量FEM弦の一般化固有値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fem-mass-eigen/?lang=ja>)
  availability: run

  整合質量のP1弦で、M内積Krylovと実際のSciPy LOBPCGを独立離散スペクトルへ照合します。
- [明示的再始動Krylovと内部固有値](<https://hrkoyama.github.io/numerical-methods-atlas/validation/restarted-shift-invert/?lang=ja>)
  availability: run

  固定長の明示的再始動とshift-invertを、元の固有値問題の残差と作用回数で比較します。
- [部分ピボットLUと混合精度反復改良：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lu-partial-pivoting/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Cholesky分解と三角代入：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cholesky/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [対称不定値系の教育用MINRES：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/minres/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [SciPy LOBPCGによる一般化固有値比較：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/lobpcg/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
