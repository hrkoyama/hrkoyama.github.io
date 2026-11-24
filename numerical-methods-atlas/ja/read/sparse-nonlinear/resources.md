# 疎行列・非線形方程式系：真の残差を測る

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/sparse-nonlinear/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)
- [BiCGSTAB](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=ja>)
- [Jacobi／対角前処理](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=ja>)
- [ピボット選択なしILU(0)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)
- [組み立てたJacobianによるNewton–Krylov法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton-krylov/?lang=ja>)
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。
- [自動微分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/automatic-differentiation/?lang=ja>)

  共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。
- [陰関数微分・随伴法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/adjoint/?lang=ja>)

  共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。
- [勾配法・準Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/optimization/?lang=ja>)

  共通実行例では減衰Newton法で前進の境界値問題を解きます。関連する自動微分・感度・随伴・係数推定の検証は各手法の別配布版へ進めます。感度・逆問題（1個または2個の係数）の入力と判定は別であり、共通の前進実行例に合算しません。
- [再始動GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [BiCGSTAB](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Jacobi／対角前処理](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [ピボット選択なしILU(0)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Armijo減衰Newton法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [線形移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#linear-advection-ja>)

  一定速度aによる輸送。波形の移動、数値拡散、安定性へ。 定常の離散移流拡散行列です。リンク先は移流項と拡散項の基礎であり、各単独式がこの行列問題全体を表すわけではありません。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 定常の離散移流拡散行列です。リンク先は移流項と拡散項の基礎であり、各単独式がこの行列問題全体を表すわけではありません。
- [Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bratu-ja>)

  ここでは−u″=λexp(u)の符号規約。Newton–Krylov法で残差・格子収束・内側線形解法の失敗を確認します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-bratu-ja>)

  31/63/127内部点、零初期値で小さい枝を選ぶ。βtanh(β/2)<2の枝を対象とし、大きい枝や分岐点の追跡を行わない。

## 問題の図

- [1次元Bratu非線形境界値問題](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/bratu.png
- [非対称移流拡散離散系の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sparse-advection-diffusion.png
- [減衰Newton法による3次方程式の求根](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/cubic-root.png

## 厳密解・参照解

- [1次元Bratu非線形境界値問題：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#references-ja>)

  小さい枝の双曲線関数による連続解と格子収束を確認します。感度・逆問題の追補では微分・目的関数を別に検証し、18件の参照解一覧にBratu専用カードはありません。
- [非対称移流拡散離散系の製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#references-ja>)

  既知の離散ベクトルからb=A xを構成する製造系で、真の残差と解誤差を確認します。連続移流拡散方程式の厳密解を使った検証とは区別します。
- [減衰Newton法による3次方程式の求根：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#references-ja>)

  x³-1=0の既知の実根x=1と残差を用い、Armijo減衰Newtonの収束を確認します。
- [1次元Bratu：小さい枝のNewton–GMRES：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja#bratu-ja-validation>)

  CSVは最細格子の数値解・解析解・絶対誤差。JSONには各格子の真の非線形残差、Newton反復数と最小減衰長を記録する。

## コード・検証

- [対称不定値鞍点系とSchur前処理](<https://hrkoyama.github.io/numerical-methods-atlas/validation/symmetric-saddle-minres/?lang=ja>)
  availability: run

  同じ元残差の基準でMINRESとGMRESを比較し、理想Schurの三点スペクトルを検査します。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja>)
  availability: run

  非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。
- [1次元Bratu：小さい枝のNewton–GMRES](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/bratu/?lang=ja>)
  availability: run

  −u''=λexp(u)、β=1・λ=2β²/cosh²(β/2)の小さい枝を零初期値から解く。31/63/127内部点で解析解、独立に再評価した非線形残差、2次格子収束を確認する。
- [擬似弧長継続でBratuのfoldを越える](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-fold-continuation/?lang=ja>)
  availability: run

  同じ1次元Bratu境界値問題の下枝から上枝までを追跡し、接線・fold・独立解析族との空間誤差を調べます。
- [再始動GMRES：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gmres/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [BiCGSTAB：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/bicgstab/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Jacobi／対角前処理：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-preconditioner/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [ピボット選択なしILU(0)：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ilu0/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Armijo減衰Newton法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [組み立てたJacobianによるNewton–Krylov法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/newton-krylov/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [1次元Bratu非線形境界値問題：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/bratu/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [非対称移流拡散離散系の製造解：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sparse-advection-diffusion/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [減衰Newton法による3次方程式の求根：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/cubic-root/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
