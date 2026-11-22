# Markov連鎖Monte Carlo

MCMCは目的分布を不変分布に持つMarkov連鎖を作ります。不変性、有限時間での混合、観測量の推定精度は別の問いです。旧単峰Gaussian例を保持し、多峰性による混合不良、診断の盲点と独立実装比較を新しい限定配布版で確かめます。

## 対象と代表式

非正規化密度π(x)と提案密度q(y|x)に対し、Metropolis–Hastings受理確率を使います。πの未知の正規化定数は比で消えます。対称なqでは提案比が消えますが、非対称提案でこれを省略すると目的分布を変えます。

新しい標的は1次元の等重みGaussian混合、π(x)=[N(−6,1)+N(6,1)]/2です。平均・分散・CDF・右側占有率を既知の目標と比べます。既存の標準正規標的とは異なる1つのテスト問題で、同じ目標の初期値・提案法・seed違いは問題数へ重複加算しません。

$$
a(x,y)=\min\!\left(1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right),\qquad N_{\rm eff}\approx\frac{N}{1+2\sum_{k\ge1}\rho_k}.
$$

## 計算の流れ

候補yを引いて受理/棄却し、棄却時にも現在の状態を標本に残します。初期過渡を評価し、複数の異なる初期値から鎖を動かします。自己相関ρₖを使う有効標本数N_effの近似は、定常性と自己相関の推定が妥当な場合に解釈します。

追加版は、峰ごとに分散させた初期値の局所ランダムウォーク、全鎖を同じ峰から始める局所ランダムウォーク、既知の対称性x→−xを使うreflection jumpを含む提案を区別します。最後の提案はこの標的の対称性を利用する対照で、未知の多峰分布に使える汎用解決策ではありません。

観測量xと右峰の指示変数を分けて評価します。古典的split R-hatと平均観測量のESSは旧版のまま保持し、新版ではrank正規化split/folded R-hat、bulk/tail ESSを別の定義として示します。ACF・ESSは観測量、有限標本、定常性と推定の約束に依存し、単一の「この鎖のESS」として万能視しません。

rank変換したbulk ESSを、原スケールの平均のMonte Carlo標準誤差（MCSE）へそのまま流用しません。定数observableでライブラリがESS=Nを返しても、それを良好な混合の証拠とは扱いません。

## 適用条件と落とし穴

詳細釣合いだけでは既約性や非周期性は保証されません。多峰性、強い相関、境界で混合が遅くなります。高い受理率だけを目標にすると微小移動に終わり得ます。鎖の間引きは、固定した計算量で情報を増やす一般的な解決策ではありません。

異なる峰に滞留した鎖は鎖間診断で混合不良を見つけやすくても、全鎖が同じ峰に閉じ込められるとR-hatが1付近でも未探索の峰が残ります。良好そうなR-hatや大きなESSだけで収束とせず、既知CDF・峰の占有率・峰間の遷移も確認します。反射提案による峰の移動だけで峰内の探索まで保証したとも扱いません。

意図した混合不良や診断の盲点を再現する検査が合格しても、そのシナリオの推定が成功したという意味ではありません。固定入力の閾値はこの小さな比較の受入条件であり、有限計算の保証、診断の偽陽性率、任意のseedや標的での信頼性を与えません。

今回の局所GaussianランダムウォークMHも理論上は既約です。有限時間に峰を移れないことを、恒久的に非エルゴードなアルゴリズムだとは呼びません。

## 検証するときに見る量

Gaussianなど既知分布で平均・分散・分位点を確認し、非対称提案の補正と棄却標本も試験します。多峰性の例では鎖間比較・自己相関・有効標本数・期待値の不確かさを報告し、見た目の定常性だけで収束としません。

新版の診断対照は、保存した同じ鎖についてACFを直接和と比較し、rank正規化R-hatとbulk/tail ESSをArviZ 0.20の独立実行で照合します。IID・既知の相関を持つ対照と定数系列などの境界例を、本来の混合正規サンプラーの推定精度と区別します。定義・中心化・分割・ties・端点の扱いと、どの指標を照合したかは専用例の固定入力・参照資料で確認します。

3つのシナリオと固定した3 seedについて、分布の誤差、峰の占有・移動、観測量別診断を並べます。旧Gaussian版の正値系列ESSや古典的split R-hatを書き換えたり、新しい診断の検証として流用したりしません。

定数系列などの退化例や非有限入力の扱いは分類・方針の検査であり、有限な診断量の数値一致とは区別します。参照fixtureの総欄数をそのまま数値一致の件数とは表示しません。

## 固定入力の実行例と診断対照

検査の合格と混合・推定の成功は区別します。旧版の入力・測定・公差は保持します。

### Gaussian標的のMCMC：分布・自己相関・ESS

固定標的の計算例

32本のMetropolis連鎖を既知の標準正規分布へ照合し、平均・分散・CDF、自己相関時間、ESSと標本予算依存を記録します。

固定seed・予算での統計検査です。ESSは平均という観測量だけ、Rhatはrank正規化版ではありません。多峰性・高次元・任意のseedでの混合や所定の偽陽性率は保証しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/gaussian-mcmc/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-models/#gaussian-mcmc) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py) · [コード models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/models.py) · [テスト test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py) · [ZIP](/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/models/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/models/verification.json)

### 多峰性MCMC：峰への閉じ込め・偽の安心・大域提案

固定標的の計算例

同じ2峰密度を、分散初期値の局所MH・同じ峰からの局所MH・対称reflectionを混ぜるMHで比較。期待した混合不良の検出と、実際の峰間移動を分けて検証します。

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/mcmc-multimodal-mixing/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-mcmc/#mcmc-multimodal-mixing) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py) · [コード sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py) · [コード diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py) · [コード fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py) · [コード generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py) · [コード prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py) · [テスト test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py) · [ZIP](/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/mcmc/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/mcmc/verification.json)

### MCMC診断の独立照合：rank Rhat・bulk/tail ESS・退化条件

診断対照・物理問題数へ非加算

同一鎖の62datasetを別環境ArviZ0.20.0で実計算し、固定recipe・入力・鎖・公式ソースSHAで結びます。通常の有限値照合と、不定値のpolicy差を分けて検査します。

固定seed・有限予算の教育用実験です。局所Gaussian RWも理論上は既約なMHであり、有限時間のtrappingを非エルゴードなアルゴリズムとは呼びません。小さいRhat・大きいESS・プールCDFの一致は未発見の峰を除外せず、既知対称性のreflection提案も一般多峰ソルバーではありません。量子計算は追加しません。 定数observableのESS=NというArviZ raw規約を混合の証拠にしません。全同値はnull＋status、鎖ごとに異なる定数のRhatはnull＋infinite-separationとして、ライブラリの巨大finite/infを残し通常有限値の一致点から除外します。bulk ESSは原スケール平均のMCSEへ流用しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/mcmc-diagnostic-reference/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-mcmc/#mcmc-diagnostic-reference) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/run.py) · [コード sampler.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/sampler.py) · [コード diagnostics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/diagnostics.py) · [コード experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/experiments.py) · [コード fixtures.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/fixtures.py) · [コード generate-arviz-reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/generate-arviz-reference.py) · [コード prepare-reference-input.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/prepare-reference-input.py) · [テスト test_mcmc.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mcmc/test_mcmc.py) · [ZIP](/code/validated-examples/2026-11-22/mcmc/atlas-mcmc-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/mcmc/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/mcmc/verification.json)

## 公開範囲

旧単峰Gaussian版と、新しい2峰混合の探索比較・診断対照を別々の不変配布版として案内します。混合不良の再現も検査の対象です。既知対称性を利用した低次元・固定seedの教育用例で、一般のMCMC・高次元・実際の推論モデルの収束保証ではありません。

## 文献

- Nicholas Metropolis and Arianna W. Rosenbluth and Marshall N. Rosenbluth and Augusta H. Teller and Edward Teller (1953). Equation of State Calculations by Fast Computing Machines. https://doi.org/10.1063/1.1699114
- W. K. Hastings (1970). Monte Carlo sampling methods using Markov chains and their applications. https://doi.org/10.1093/biomet/57.1.97
