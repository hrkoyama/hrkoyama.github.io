# 代数的マルチグリッド（AMG）

AMGは方程式の行列から階層と補間を構成する多重格子法です。「滑らかな誤差」を幾何的な波長だけでなく、緩和で減りにくい代数的な成分として捉えます。

## 対象と代表式

Au=bの残差r=b−Au、粗い空間への制限R、補間Pを用います。Galerkin粗行列A_c=RAPとし、粗問題で残差を近似的に解いて補正します。下式の逆行列は原理を表すもので、通常は階層を再帰的に解きます。

$$
A_c=RAP,\qquad r=b-Au,\qquad u\leftarrow u+P A_c^{-1}Rr.
$$

## 計算の流れ

前緩和、残差計算、粗格子補正、後緩和を行います。古典AMGでは強結合とC/F分割から補間を作り、aggregation型では未知数の集合から粗空間を作ります。弾性なら剛体運動など、近零空間の情報を補間に含めることが重要です。

## 適用条件と落とし穴

単一スカラー楕円型で良好でも、非対称移流、鞍点系、強異方性で同じ設定が通るとは限りません。CGの前処理に使うなら、作用素とサイクルの対称正定値性を確認します。純Neumann問題の定数零空間と右辺の適合条件も残ります。

条件数だけでAMGの性能は決まりません。条件数が同じ正定値行列でも、異方性の方向、強結合の判定、補間が表す近零空間と緩和法によって収束が変わります。固定した等方・異方行列の対照は、任意の楕円型問題や大規模並列計算の頑健性の保証ではありません。

## 検証するときに見る量

製造解Poissonで格子細分化と係数コントラストを変え、真の残差、解の誤差、サイクル当たりの減衰率を調べます。粗行列の非零数と階層の大きさも記録します。反復回数が少ないことと離散化誤差が小さいことは別です。

旧版の製造解Poisson例を保持し、追加版では既知の代数解から右辺を作った線形系について、独立疎直接解・離散正弦変換による対角化と比較し、解析的な離散スペクトルも照合します。真の相対残差、解の相対誤差、反復履歴、階層の複雑さを分けて記録し、行列の大きさ・異方性・条件数に対する依存を、固定した残差許容値と反復上限で調べます。この追加版は代数的な条件数診断であり、格子収束や連続Poisson解の精度を検証したことにはしません。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 行列から粗視化するAMG：残差と解誤差を分ける

固定標的の計算例

正方形Poisson問題から得たSPD行列だけを階層構築へ渡し、平滑化集約AMGのV-cycleを実行します。7²・15²・31²未知数で独立疎行列直接解、解析的な離散正弦モード、連続解への2次収束を分けて検査します。

3格子の固定スカラー問題だけの確認です。係数の大きな不連続、強い異方性、弾性系、任意の非構造格子、最適計算量・格子独立収束を保証しません。小さい残差だけを小さい解誤差の証明としません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/sa-amg/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations/#sa-amg) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/run.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/solvers.py) · [テスト test_foundations.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations/test_foundations.py) · [ZIP](/code/validated-examples/2026-11-22/foundations/atlas-foundations-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations/verification.json)

### AMGの条件数・異方性・残差と前進誤差

診断対照・物理問題数へ非加算

49・225・961未知数のSPD行列で、条件数と異方性を別々に変えます。解析スペクトル、独立疎行列直接解、DST対角化を比較し、同じ残差でも解誤差が条件数に依存することを確かめます。

固定した小規模な一定係数系列のみです。任意の係数ジャンプ、非構造格子、不定値系、最適計算量・一様収束を保証しません。異方性が常にκ₂を増やす、あるいは単調に収束を悪化させるとは主張しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/amg-conditioning/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-foundations-conditioning/#amg-conditioning) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/run.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/experiments.py) · [コード fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/fixtures.py) · [コード mpmath_reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/mpmath_reference.py) · [コード solvers.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/solvers.py) · [テスト test_conditioning.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/foundations-conditioning/test_conditioning.py) · [ZIP](/code/validated-examples/2026-11-22/foundations-conditioning/atlas-foundations-conditioning-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/foundations-conditioning/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/foundations-conditioning/verification.json)

## 公開範囲

旧版の入力・測定値・公差を保持し、条件数・残差・収束の追加検証を別の配布版として案内します。診断対照の合格は、その対照で意図した限界を確認した意味を含み、一般的な成功や原論文全体の再現を意味しません。

## 文献

- J. W. Ruge and K. Stüben (1987). 4. Algebraic Multigrid. https://doi.org/10.1137/1.9781611971057.ch4
- P. Vaněk, M. Brezina, J. Mandel (2001). Convergence of algebraic multigrid based on smoothed aggregation. https://doi.org/10.1007/s002110000226
