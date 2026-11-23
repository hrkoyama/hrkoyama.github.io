# 非周期壁面：キャビティと製造解

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-wall-flow/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

  共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [Heun法／SSPRK(2,2)](<https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja>)

## 方程式

- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。 無次元の単位正方形、ν=.01、蓋速度U=1、Re=100。上面の内部節点だけu=1、他壁と四隅の速度は0、全壁ψ=0。初期内部渦度は0。壁渦度はThom条件で各Heun段に再設定します。
- [外力付き非圧縮流と壁面製造解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja>)

  一定密度1の外力付き非圧縮系です。実際の流れは外力のcurlを使う渦度・流れ関数形で圧力を消去します。p_opは独立の非零Dirichlet Poisson・勾配演算子の製造問題で、流れと結合した圧力場やキャビティ圧力ではありません。 単位正方形、ν=.01、17/33/65点、ψ=8f(x)f(y),f(z)=z²(1−z)²。全壁で非浸透・滑りなし。渦度外力は連続方程式から解析的に導出し、全壁にキャビティと同じThom条件を使用します。厳密壁渦度は注入しません。
- [外力付き非圧縮流と壁面製造解](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#forced-incompressible-ja>)

  一定密度1の外力付き非圧縮系です。実際の流れは外力のcurlを使う渦度・流れ関数形で圧力を消去します。p_opは独立の非零Dirichlet Poisson・勾配演算子の製造問題で、流れと結合した圧力場やキャビティ圧力ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-algorithm>)

  ωt+uωx+vωy=νΔωを中央差分とHeun法で進め、各段で−Δhψ=ωを非周期Dirichlet DSTで解きます。u=ψy,v=−ψx。局所一次のThom壁渦度を使用し、原著のCSI-MGと高次壁公式は実装していません。
- [非圧縮Navier–Stokes](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#navier-stokes-ja>)

  一定密度・粘性の代表形。周期2D MAC射影・Taylor–Green渦に加え、圧力を消去する非周期Re100キャビティを別配布で検証します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-algorithm>)

  共通の中央差分・Heun・非周期Dirichlet DST Poissonを使用します。多項式の明示微分と、独立な係数行列の微分を照合します。別途p=x²+y²+sinπx sinπyの非零Dirichlet Poisson問題を解き、内部中央差分・壁上の二次片側差分勾配を検査します。

## 問題の図

- [Re100の蓋駆動キャビティ](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100-preview.png
- [非周期壁面の製造非圧縮流](<https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured-preview.png
- [Re=100蓋駆動キャビティ：Ghia中心線との比較](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/cavity-ghia-re100.png
- [非周期壁面の製造解：速度・剪断・圧力演算子](<https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-23-r2/wall-flow/results/wall-manufactured.png

## 厳密解・参照解

- [Re100の蓋駆動キャビティ：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/lid-driven-cavity/?lang=ja#references-ja>)

  21単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。
- [Ghia Re100：原著の有限格子速度中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。 Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。
- [非周期壁面の製造非圧縮流：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/wall-manufactured/?lang=ja#references-ja>)

  ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。
- [壁面製造解：多項式速度と独立した圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形・ν.01・滑りなし、ψ*=8x²(1−x)²y²(1−y)²、u*=ψ*y、v*=−ψ*x、ω*=−Δψ*。連続の渦度式からs=u*ω*x+v*ω*y−νΔω*を構成し、独立の係数行列微分と照合します。PDE計算の壁渦度はキャビティと同じThom式で、厳密値を注入しません。p_op=x²+y²+sinπx sinπyの非零Dirichlet Poisson・勾配は別の演算子問題で、流れに結合した圧力やキャビティ圧力ではありません。 Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。
- [Ghia Re100：原著の有限格子速度中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja>)
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。
- [壁面製造解：多項式速度と独立した圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja>)
  reference_kind: manufactured

  製造解 単位正方形・ν.01・滑りなし、ψ*=8x²(1−x)²y²(1−y)²、u*=ψ*y、v*=−ψ*x、ω*=−Δψ*。連続の渦度式からs=u*ω*x+v*ω*y−νΔω*を構成し、独立の係数行列微分と照合します。PDE計算の壁渦度はキャビティと同じThom式で、厳密値を注入しません。p_op=x²+y²+sinπx sinπyの非零Dirichlet Poisson・勾配は別の演算子問題で、流れに結合した圧力やキャビティ圧力ではありません。
- [Re=100蓋駆動キャビティ：Ghia中心線との比較：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja#cavity-ghia-re100-ja-validation>)

  22単体検査と群全体94判定を事前固定。原著の表I/II（印刷398–399頁）を直接確認して転記した17点ずつへ線形補間し、最細の各速度最大誤差≤.03、細分化で減少、定常残差≤1e−7を検査します。表Vの主渦位置・壁値・Poisson残差・離散発散も確認します。
- [Ghia Re100：原著の有限格子速度中心線](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-ghia-re100-ja>)
  relation: same-problem
  reference_kind: numerical-reference

  有限格子の数値参照 単位正方形、Re100、蓋速度1、他壁静止。Ghia原著の表I/IIのRe100列から速度u(0.5,y)とv(x,0.5)各17点を直接確認して転記し、印刷された4桁座標を保持します。表Vの格子上の主渦位置(.6172,.7344)を別に比較します。丸めを含む有限格子数値表で、厳密な連続解でも今回のソルバー出力でもありません。 Re=100・3固定格子の教育用検査です。蓋と側壁の角に速度の不連続があり、角の速度は静止側を優先します。Ghia値は丸めた数値参照で厳密解ではなく、4桁座標をそのまま使います。高Re・乱流・原著アルゴリズムの再現・キャビティ圧力を検証したとは主張しません。
- [非周期壁面の製造解：速度・剪断・圧力演算子：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja#wall-manufactured-ja-validation>)

  ψと速度の最細刻み対の次数≥1.7、誤差減少・絶対誤差、実際の壁渦度と速度勾配剪断の誤差減少を検査します。圧力演算子はp次数≥1.8、全体と境界の勾配次数≥1.7。独立多項式照合5項目、全壁値、真の定常残差、非周期Poisson残差も記録します。
- [壁面製造解：多項式速度と独立した圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-wall-mms-ja>)
  relation: same-problem
  reference_kind: manufactured

  製造解 単位正方形・ν.01・滑りなし、ψ*=8x²(1−x)²y²(1−y)²、u*=ψ*y、v*=−ψ*x、ω*=−Δψ*。連続の渦度式からs=u*ω*x+v*ω*y−νΔω*を構成し、独立の係数行列微分と照合します。PDE計算の壁渦度はキャビティと同じThom式で、厳密値を注入しません。p_op=x²+y²+sinπx sinπyの非零Dirichlet Poisson・勾配は別の演算子問題で、流れに結合した圧力やキャビティ圧力ではありません。 Thomの壁渦度局所打切りは一次で、壁剪断の二次精度は主張せず観測次数を示します。流れ関数の発展では圧力を消去するためゲージは該当しません。圧力診断は独立した演算子製造問題であり、キャビティの圧力・応力境界やMAC射影の検証ではありません。多項式の別微分は独立な流体ソルバーとの比較とは区別します。

## コード・検証

- [Re=100蓋駆動キャビティ：Ghia中心線との比較](<https://hrkoyama.github.io/numerical-methods-atlas/validation/cavity-ghia-re100/?lang=ja>)
  availability: run

  非周期・粘性非圧縮の実際の2D計算を17/33/65点格子で定常化し、Ghia原著の速度中心線と比較します。流線・渦中心・真の残差と発散を同時に保存します。
- [非周期壁面の製造解：速度・剪断・圧力演算子](<https://hrkoyama.github.io/numerical-methods-atlas/validation/wall-manufactured/?lang=ja>)
  availability: run

  キャビティと同じ壁条件付き2Dソルバーに解析外力を与え、速度と流れ関数の格子収束、壁渦度・壁剪断の誤差を測ります。別の非零Dirichlet圧力製造解でPoisson・勾配の境界演算子も検査します。
