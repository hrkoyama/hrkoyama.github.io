# 輻射輸送・モーメント法

輻射輸送では位置・方向・周波数に依存する強度を解きます。角度を積分したモーメント法は未知数を減らしますが、失われた角度情報を閉包で補う必要があります。

## 対象と代表式

ここでは静止媒質・周波数積分済みの灰色強度Iを考え、等方な輻射源ηと吸収係数κを使い、散乱は省略します。κは長さの逆数です。E=(1/c)∫I dΩ、F=∫nI dΩ、P=(1/c)∫nnI dΩを定義すると、EとFの方程式はPを含みます。

$$
\frac1c\partial_t I+\mathbf n\cdot\nabla I=\eta-\kappa I,\qquad\partial_t E+\nabla\cdot\mathbf F=4\pi\eta-c\kappa E,\qquad c^{-2}\partial_t\mathbf F+\nabla\cdot\mathbf P=-\kappa\mathbf F/c.
$$

## 計算の流れ

離散方向法は角度を直接離散化し、モーメント法はP=D EのEddingtonテンソルを閉じます。M1は局所E,FからDを与える代表例で、FLDはFをEの勾配から表す別の近似です。光学的厚い極限と自由流の極限を照合し、物質との交換を同じエネルギー収支で計算します。

## 適用条件と落とし穴

M1は異なる方向の交差ビームを一般には独立に運べません。FLDは勾配方向に流束を結び付けるため影や強い異方性に制約があります。縮約光速は物理的な伝播/緩和時間を変えるので、支配的な時間尺度との関係を明示します。

追加版も1次元定常・純吸収・指定流入の平板で、μ∂xI=−κIを解きます。一般の輻射モーメント閉包、散乱、時間依存、多周波数や流体との結合は検証しません。

## 検証するときに見る量

吸収だけの指数減衰、等方拡散、自由流と影、交差ビームを分けて調べます。E≥0、|F|≤cEという実現可能性、輻射と物質の総エネルギー、角度/空間/時間収束を確認します。閉包誤差と離散化誤差を混同しません。

Beer–Lambertの各ray解析解と連続角度の指数積分を使い、固定角度での風上空間誤差と、厳密ray伝播での角度求積誤差を分離します。流入−流出と体積吸収の収支・正値性を別に確認し、保存則だけで角度分布の精度を判定しません。

光学的厚さ0.1・0.7・3で、連続角度参照を指数積分expnと別の適応QUADPACK求積でも照合します。独立な輸送標本化では入射fluxに対応するμ=√Uを用い、透過をBernoulli変数として数えます。64反復の有限標本で二項信頼区間とRMSEを調べますが、公称95%の被覆を任意の入力や標本で保証したとは表示しません。

## 固定入力の実行例と診断対照

受入条件が示す検証範囲と数学的な一般保証を区別します。旧版の入力・測定・公差は保持します。

### 純吸収平板の離散座標輻射輸送

固定標的の計算例

純吸収の定常輻射輸送を角度と空間で離散化し、Beer–Lambert解と積分された出射フラックスで検証します。

多重散乱、熱輻射、周波数再分配、動的媒質、輻射流体連成は未実装です。StamnesらのDISORTの全機能・安定化を再現したとは表示しません。

[入力・結果・受入条件](/numerical-methods-atlas/validation/radiation-transport/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particles/#radiation-transport) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/run.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/fmm.py) · [コード transport.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/transport.py) · [テスト test_particles.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particles/test_particles.py) · [ZIP](/code/validated-examples/2026-11-22/particles/atlas-particles-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particles/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particles/verification.json)

### 輻射輸送：空間・角度収束と光子統計

固定標的の計算例

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

区間被覆は有限の固定seedでの観測で、ちょうど95%の実測値や全seedの成功を保証しません。決定論的求積誤差を統計誤差へ含めず、多重散乱・周波数依存・熱輻射・輻射流体連成は未検証です。

[入力・結果・受入条件](/numerical-methods-atlas/validation/radiation-convergence/?lang=ja) · [手法・一次文献](/numerical-methods-atlas/ja/read/validation-particle-transport/#radiation-convergence) · [コード run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/run.py) · [コード kinetic_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetic_experiments.py) · [コード kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/kinetics.py) · [コード longrange_experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/longrange_experiments.py) · [コード electrostatics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/electrostatics.py) · [コード fmm.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/fmm.py) · [テスト test_kinetics.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_kinetics.py) · [テスト test_longrange.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_longrange.py) · [テスト test_runner.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/test_runner.py) · [ZIP](/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip) · [結果](/code/validated-examples/2026-11-22/particle-transport/results/result.json) · [追試記録](/code/validated-examples/2026-11-22/particle-transport/verification.json)

## 公開範囲

従来の解説・式・文献と旧配布版を保持し、条件を固定した追加検証を別配布版として案内します。上の一般的な検証案すべてを実施したという意味ではありません。各版の入力・参照・合否・制約は専用ページと保存記録で確認してください。

## 文献

- C.D. Levermore (1984). Relating Eddington factors to flux limiters. https://doi.org/10.1016/0022-4073(84)90112-2
