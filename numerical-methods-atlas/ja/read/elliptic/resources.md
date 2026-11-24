# 拡散、楕円型方程式、境界条件、反復法

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/elliptic/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [Crank–Nicolson法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja>)
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)
- [Jacobi反復](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=ja>)
- [Gauss–Seidel反復](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-seidel/?lang=ja>)
- [逐次過緩和法／SOR](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=ja>)
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)
- [赤黒Gauss–Seidel法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=ja>)
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。 入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。 入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。
- [PINN・ニューラル演算子](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。 入力(u₀,ν)を幅2へ写し、局所線形項・DCと1–4モードの複素Fourier項・tanhからなる2ブロックを適用します。L-BFGS-Bの固定予算で学習し、同じ重みをN=32/64へ転送。非線形項は各格子上で評価しdealiasingしません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [前進Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/forward-euler/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [後退Euler法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/backward-euler/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Crank–Nicolson法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。
- [PINN・ニューラル演算子](<https://hrkoyama.github.io/numerical-methods-atlas/methods/pinn-operators/?lang=ja>)

  この問題への対応が共通の固定入力・実行例で明示された手法です。図と実行例の条件の違いは入力で確認してください。 x(1−x)を掛けて境界値を厳密に組み込むtanhネットワークを、解析的な全パラメータJacobian付きTRF最小二乗法で学習します。固定予算後の全モデルを保存し、31/63/127未知数の2次中心差分とThomas法も計算します。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  公開境界値実装のThomas消去と離散平均ゲージを使います。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  公開の混合境界Poisson検査で使うThomas消去です。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  公開のRobin境界Poisson検査で使うThomas消去です。
- [Jacobi反復](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [赤黒Gauss–Seidel法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [逐次過緩和法／SOR](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Fourier微分と時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Jacobi反復](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [赤黒Gauss–Seidel法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [逐次過緩和法／SOR](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Thomas法／三重対角消去](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [Fourier微分と時間発展](<https://hrkoyama.github.io/numerical-methods-atlas/methods/fourier/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [幾何マルチグリッドVサイクル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。
- [共役勾配法](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja>)

  この問題の保存済み比較データまたは対応する公開検査で使われる手法です。一般的な適用可能性だけでは追加していません。

## 方程式

- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [熱・拡散方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#heat-ja>)

  一定拡散係数νの代表形。モードの減衰、時間積分、境界条件へ。
- [Poisson・Laplace方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#poisson-laplace-ja>)

  楕円型境界値問題。符号規約を確認し、反復解法・疎行列・境界条件をたどる。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#execution-poisson-1d-dirichlet-ja>)

  一様格子の3点差分を15/31/63内部点で解く。残差が小さいことと連続解に近いことは別々に判定する。

## 問題の図

- [周期Fourierモードの熱拡散](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/heat-periodic.png
- [Dirichlet境界の熱拡散](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/diffusion-boundaries.png
- [1次元Poisson・Dirichlet製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-dirichlet.png
- [1次元Poisson・純Neumann境界](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-neumann.png
- [1次元Poisson・Dirichlet/Neumann混合境界](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-mixed.png
- [1次元Poisson・Robin境界の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-1d-robin.png
- [2次元Poisson・広帯域の滑らかな製造解](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/manufactured-63-fields.png
- [2次元Poisson・局在ソース](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/assets/poisson-comparison/localized-63-fields.png
- [2次元Poisson・一様ソース](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-uniform.png
- [2次元Poisson・乱数ソースの離散残差](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/poisson-2d-random.png

## 厳密解・参照解

- [周期Fourierモードの熱拡散：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#references-ja>)

  周期区間の単一Fourierモードの指数減衰が解析基準です。保存図の振幅0.25・粘性0.02の条件を、別周波数のコード検査と区別します。 全93実座標の損失勾配を2つの固定差分幅で照合し、Fourierブロックを直接DFTと比較。解析的な熱モード減衰に対する絶対・相対誤差、格子制限差、ID/OODを分離します。参照RMS≤10⁻¹²では相対誤差をNAとし、ゼロ・微小振幅では絶対誤差を保存します。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、拡散係数0.02。 保存ギャラリーの周期[0,1]、1+0.25sin(2πx)、ν=0.02、最終時刻1が一致します。別周波数のコード検査への一致は意味しません。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-fno-periodic-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 周期区間[0,2π)、uₜ=νuₓₓ、T=0.25。同じ関数の点を分散させず、全46問題を学習24・検証6・未見ID8・νのOOD4・周波数のOOD4に分けます。2固定seed、93実パラメータです。 固定された小型離散作用素の比較で、任意の解像度・分布に対する一般化やOOD精度を保証しません。N=64から32への差には非線形aliasingが含まれ、連続体離散化誤差とは呼びません。最適化収束と固定予算終了は別です。
- [Dirichlet境界の熱拡散：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#references-ja>)

  零Dirichlet境界でのsin(πx)の指数減衰と格子収束を確認します。周期境界・平均値1の参照解一覧の熱モードとは別条件です。
- [熱拡散／Fourierモードの減衰](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sine-heat-ja>)
  relation: related-model
  reference_kind: analytic

  解析解 単位区間の周期境界、拡散係数0.02。 こちらは零Dirichlet・sin(πx)、参照カードは周期境界・1+0.25sin(2πx)・ν=0.02です。
- [1次元Poisson・Dirichlet製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#references-ja>)

  零Dirichlet境界の製造正弦解、複合正弦の比較例、および離散残差で確認します。単一sin(πx)の参照カードが全ソース条件を表すわけではありません。 全49列の残差Jacobianと損失勾配、空間微分を別資格段階で独立照合。解析解sin(πx)に対する独立点誤差、PDE残差、境界値、FD誤差を別に保存します。収束・精度目標の実際の真偽を残し、正常な予算終了を収束と呼びません。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。 1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。
- [1次元Poisson・純Neumann境界：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja#references-ja>)

  f=-2、外向き微分(0,2)に対するx²から離散平均を除いた解と、Neumann整合条件・平均値ゲージを確認します。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 参照カードはsin(πx)・零Dirichlet、こちらはf=-2・純Neumann・平均ゲージです。
- [1次元Poisson・Dirichlet/Neumann混合境界：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja#references-ja>)

  f=-2、左Dirichlet値1・右外向き微分2の製造解u=1+x²と比較します。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 参照カードは零Dirichletの正弦解、こちらは混合境界の1+x²です。
- [1次元Poisson・Robin境界の製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja#references-ja>)

  f=-exp(x)と指定Robin係数を満たすu=exp(x)が製造解です。境界処理を含む2次収束を確認します。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 参照カードは零Dirichletの正弦解、こちらはRobin境界のexp(x)です。
- [2次元Poisson・広帯域の滑らかな製造解：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-broad/?lang=ja#references-ja>)

  比較資料の滑らかな製造解から選んだ右辺と、分離変数の離散直接解を区別し、連続誤差と代数誤差を確認します。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 同じPoisson製造解の考え方ですが、カードは1次元単一正弦、こちらは2次元の滑らかな複合ソースです。
- [2次元Poisson・局在ソース：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-localized/?lang=ja#references-ja>)

  局在ソースに対する離散直接解と真の残差を基準に反復法を比較します。公開資料にこのソースの閉形式連続解は添付されていません。
- [2次元Poisson・一様ソース：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#references-ja>)

  一様右辺・零Dirichletの離散Poisson問題について、保存した多重格子の真の残差と、緩和法との残差低下の違いを確認します。連続厳密解との誤差照合とは区別します。
- [2次元Poisson・乱数ソースの離散残差：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#references-ja>)

  固定seedのランダム右辺に対する離散残差を直接評価します。残差の小ささを、未知の連続解との誤差と同一視しません。
- [1次元Poisson：Dirichlet正弦解と2次収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja#poisson-1d-dirichlet-ja-validation>)

  CSVは最細格子でx・数値解・解析解・誤差を整列。全3格子の誤差と残差、隣接格子間の次数はresult.jsonに保存。Thomasの原報告は既存台帳でも直接確認未済のため、未検証の一次文献を新たに掲げない。
- [Poisson／正弦波の製造解](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-poisson-manufactured-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 両端はゼロDirichlet条件。目標解から外力を選ぶ製造解であり、任意の外力のPoisson解ではありません。 単一sin(πx)の共通固定入力とは一致しますが、保存比較図は複合正弦製造解も含みます。同じ零Dirichletでも全ソースが同一ではありません。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-pinn-poisson-ja>)
  relation: related-model
  reference_kind: manufactured

  製造解 無次元区間[0,1]で −uₓₓ=π²sin(πx)、u(0)=u(1)=0。中間層16素子・49実パラメータ、固定seed 8401–8403、学習64点と独立評価257点を用います。 1つの滑らかなPoisson問題と3seedの固定予算実験です。小さい学習損失だけで独立点精度の達成や一般的なPINN学習成功を保証しません。未達目標も表示します。

## コード・検証

- [1次元Poisson：Dirichlet正弦解と2次収束](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-1d-dirichlet/?lang=ja>)
  availability: run

  既存Thomas解法で −u''=π²sin(πx) を15/31/63内部点で解き、解析解sin(πx)、独立な差分残差、格子幅半減の次数を別々に確認する。
- [1D Poisson PINNと独立格子誤差](<https://hrkoyama.github.io/numerical-methods-atlas/validation/pinn-poisson/?lang=ja>)
  availability: run

  3固定seedの49パラメータPINNを解析解・FDと比較します。
- [解析・中央差分・方向ADによるJacobian不要Newton–Krylov](<https://hrkoyama.github.io/numerical-methods-atlas/validation/bratu-matrix-free-jfnk/?lang=ja>)
  availability: run

  非線形Jacobianを組み立てずにBratuの上下枝を3種類のJvで解き、forcingと実際の残差・評価回数を保存します。
- [時間離散拡散の随伴とcheckpoint](<https://hrkoyama.github.io/numerical-methods-atlas/validation/diffusion-discrete-adjoint/?lang=ja>)
  availability: run

  後退Eulerの離散写像を実際に逆伝播し、接線・独立高精度mode解・block replayと比較します。
- [2次元Poisson：CG・多重格子とP1 FEM](<https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/poisson-2d-sine/?lang=ja>)
  availability: run

  単位正方形のsin(πx)sin(πy)を参照し、CG/MGは15/31/63内部点、P1 FEMは4/8/16分割で細分化。FDの最大誤差と真の残差、FEMの要素内L2誤差とH1半ノルムを独立に評価する。
- [純Neumannの互換条件と平均値ゲージ](<https://hrkoyama.github.io/numerical-methods-atlas/validation/poisson-neumann/?lang=ja>)
  availability: run

  特異な2D Poissonを互換条件と指定平均込みで解き、不適合な外力を拒否します。
- [係数ジャンプ拡散：共有流束とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/checkerboard-diffusion/?lang=ja>)
  availability: run

  不連続係数のFV解を独立なP1参照と比較し、線形系の残差・前進誤差と連続問題の誤差を分けます。
- [回転異方性拡散：完全テンソルQ1とMG・AMG](<https://hrkoyama.github.io/numerical-methods-atlas/validation/rotated-anisotropic-diffusion/?lang=ja>)
  availability: run

  非零Kxyを保つQ1弱形式で、解析解への収束と同じ行列のMG・AMG収束を比較します。
- [小型FNOの問題単位検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/fno-periodic-heat/?lang=ja>)
  availability: run

  同じ重みで32/64点・未見関数・OODを分けて評価します。
- [Crank–Nicolson法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/crank-nicolson/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Thomas法／三重対角消去：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/thomas/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Jacobi反復：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/jacobi-iteration/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [Gauss–Seidel反復：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gauss-seidel/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [逐次過緩和法／SOR：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sor/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [共役勾配法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/cg/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [赤黒Gauss–Seidel法：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rbgs/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [幾何マルチグリッドVサイクル：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/multigrid/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
- [周期Fourierモードの熱拡散：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-periodic/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [Dirichlet境界の熱拡散：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/heat-dirichlet/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [1次元Poisson・Dirichlet製造解：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-dirichlet/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [1次元Poisson・純Neumann境界：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-neumann/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [1次元Poisson・Dirichlet/Neumann混合境界：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-mixed/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [1次元Poisson・Robin境界の製造解：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-1d-robin/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [2次元Poisson・一様ソース：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-uniform/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
- [2次元Poisson・乱数ソースの離散残差：コード・検証状況](<https://hrkoyama.github.io/numerical-methods-atlas/problems/poisson-2d-random/?lang=ja#code-ja>)
  availability: source

  対応する公開検査と配布版の条件を確認できます。
