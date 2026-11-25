# Turing不安定性：線形成長率と小振幅パターン / Turing instability: linear growth and small-amplitude patterns

https://hrkoyama.github.io/numerical-methods-atlas/problems/turing-schnakenberg/

## 日本語

[a=0.1,b=0.9、拡散係数0.01/1のSchnakenberg型。行列指数に対する線形誤差・成長率と、t=4の小振幅非線形初期パターンを保存値から表示。](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-models/#turing-schnakenberg) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#turing-schnakenberg)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [Schnakenberg反応拡散](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-schnakenberg-ja)

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

自己触媒反応の空間拡張。反応平衡と分散関係から模様の発生を検証するための数理モデルです。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。この旧1次元例だけから一般の模様選択、生物実験への較正、流体連成へ広げません。 全モデル族の実装ではありません。今回の固定例：Schnakenberg：2D境界と初期モード

#### [Turing反応拡散の枠組み](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#bio-turing-ja)

$$
u_t=D_u\Delta u+f(u,v)
$$

$$
v_t=D_v\Delta v+g(u,v)
$$

2成分反応拡散の枠組み。f・gは個別に指定する必要があり、模様の画像だけでTuring機構とは判定できません。 限定した実行例：a=0.1,b=0.9、拡散係数0.01/1、長さ2πの1次元周期Schnakenberg系。旧線形発現例を保持し、固定した反射対称の有限振幅初期値の非線形発展と成長後パターンを独立Fourier–Galerkin/Radau参照および空間・時間細分化で比較します。一般の模様選択、2次元、生物実験への較正、流体連成には広げません。

#### Turing不安定性：線形成長率と小振幅パターン

補助実行例 · 実行例の定義・検証式

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

#### Schnakenberg有限振幅過渡：非線形性と独立参照

補助実行例 · 実行例の定義・検証式

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

#### Schnakenberg飽和パターン：近定常性と格子・時間収束

補助実行例 · 実行例の定義・検証式

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

#### 同じ非線形反応拡散でLie–TrotterとStrangを比較する

補助実行例 · 実行例の定義・検証式

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

### 厳密解・参照解

小振幅では行列指数の線形成長率を使い、非線形追補では独立Radau参照と正値性・収束を確認します。線形近似を非線形飽和パターンの厳密解と呼びません。

#### Turing不安定性：線形成長率と小振幅パターン

連続Fourier行列J-k²DのSciPy expmと線形数値解を比較し空間収束を測定。非線形計算は半離散線形行列指数との小振幅差を測り、成熟模様の参照照合とは区別します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja)

#### Schnakenberg有限振幅過渡：非線形性と独立参照

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja)

#### Schnakenberg飽和パターン：近定常性と格子・時間収束

空間も異なるcosine Fourier–Galerkin＋Radau参照（K32/64/96、cubic投影M=4(K+1)>4K、analytic Jacobian）とraw L1/L2/L∞を比較。参照のK感度とODE公差感度を別検査し、時間次数は同じFD半離散系を別実装Radauで積分した値に対して測定。平均L1・RMS L2・最大L∞を成分ごとに求め悪い方を採用。反応収支・全step正濃度・初期ゼロのk≥5（本対称性で最初はk6）・線形化との差を記録します。 収束ノルムと参照感度は固定最終時刻で判定し、途中スナップショット誤差は別の推移診断です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja)

#### 同じ非線形反応拡散でLie–TrotterとStrangを比較する

参照は同じFD半離散系を実空間の疎行列・別記述の反応RHSで組み、分割せずRadauで積分した数値解です。Radauの公差細分化と別のDOP853で参照自身の差を測り、最細Strang誤差との比を判定します。ノルムは成分ごとの平均L1・RMS L2・最大L∞を求めて悪い成分を採用し、4つの正の共通出力時刻の最大値で次数を測定。Newton公差感度、全副段階の正濃度、反応source/sink収支と逆順Lieの対照も記録します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [空間中心差分](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [古典的RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [陰的中点則](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Lie–Trotter分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Strang分割](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Turing不安定性：線形成長率と小振幅パターン](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=ja)

補助実行例

Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。

無次元a=0.1,b=0.9、平衡(1,0.9)、拡散係数(0.01,1)、周期k=2、初期振幅1e-4。線形t=1と非線形t=4の短い計算に限定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

1つの平衡近傍の発生段階です。原著係数や原著実験の再現、成熟模様、ランダム擾乱からの波数選択、実生物の較正は主張しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

#### [Schnakenberg有限振幅過渡：非線形性と独立参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=ja)

補助実行例

t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。

1D周期x∈[0,2π)、a=.1,b=.9、D=(.01,1)。共通初期値u=1+.08cos2x+.01cos4x、v=.9−.03cos2x−.002cos4x。反射対称かつπ周期の不変部分空間で、原点を固定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

#### [Schnakenberg飽和パターン：近定常性と格子・時間収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=ja)

補助実行例

t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。

1D周期x∈[0,2π)、a=.1,b=.9、D=(.01,1)。共通初期値u=1+.08cos2x+.01cos4x、v=.9−.03cos2x−.002cos4x。反射対称かつπ周期の不変部分空間で、原点を固定します。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

選択対称性を持つ1D教育用モデルで、乱数からの自由な波数選択・位相安定性・2D斑点・実生物の較正を検証しません。原著の係数や実験の再現ではありません。陰的midpointはA安定でもL安定・無条件正値ではなく、反応でu+vは保存しません。初回粗刻みは不合格で、受入基準を変えず時間解像度を強化した履歴を保持。量子計算は追加しません。 近飽和は参照の90→100の検査窓に対する判定で、厳密定常解・非線形安定性・長期吸引の証明ではありません。lateの巨大な線形差は線形化の破綻診断で、精度誤差ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

#### [同じ非線形反応拡散でLie–TrotterとStrangを比較する](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=ja)

補助実行例

32格子・終了時刻1のSchnakenberg反応拡散を、同じ入力・部分ソルバーでLie–TrotterとStrangにより進めます。4段階の時間刻みで1次／2次の収束、参照の感度、反応収支と未収束時の失敗を確かめる軽量な比較例です。

無次元の1D周期区間[0,2π)、N=32、a=.1,b=.9、D=(.01,1)。u₀=1+.08cos2x+.01cos4x、v₀=.9−.03cos2x−.002cos4xは既存の有限振幅例と同じ初期場です。今回の終時刻はT=1、ステップ数16/32/64/128、共通出力時刻0/.25/.5/.75/1。反射対称・π周期の限定入力です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

固定格子での採用合成法の時間誤差であり、分割誤差と反応中点則の離散誤差を含みます。連続PDEの厳密解・空間収束・独立PDE実装の照合とは呼びません。u+vは反応で保存せず、正濃度は固定入力での観測です。計算費は実際の部分流呼出し数で示し、速度の順位やStrangの一般的優越を主張しません。既存Schnakenberg問題の追加比較で、物理問題数・共通22例・旧配布版の公差や成功履歴を増減・変更しません。長時間パターン・2D・一般境界は対象外です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/splitting/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py)
- [/code/validated-examples/2026-11-22/splitting/splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py)
- [/code/validated-examples/2026-11-22/splitting/reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py)
- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)

## English

[Schnakenberg-type a=0.1,b=0.9 and diffusivities 0.01/1: stored linear errors/growth against a matrix exponential and a small nonlinear onset pattern at t=4.](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/turing-schnakenberg.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-models/#turing-schnakenberg) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#turing-schnakenberg-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Schnakenberg reaction–diffusion](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-schnakenberg-en)

$$
u_t=D_u\Delta u+a-u+u^2v
$$

$$
v_t=D_v\Delta v+b-u^2v
$$

A simple autocatalytic kinetic law extended in space, useful for reproducible Turing-onset tests. A mathematical chemical pattern model; matching a visual biological pattern does not calibrate it to a tissue. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. The earlier 1D case alone makes no general pattern-selection, biological-calibration or fluid-coupling claim. Not implementation of the entire model family. Fixed cases: Schnakenberg:2D boundaries and initial modes

#### [Turing reaction–diffusion framework](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#bio-turing-en)

$$
u_t=D_u\Delta u+f(u,v)
$$

$$
v_t=D_v\Delta v+g(u,v)
$$

A framework for diffusion-driven pattern onset around a homogeneous reaction equilibrium, not a unique choice of f and g. A spot image or unequal diffusion coefficients alone do not establish a Turing mechanism. Boundary conditions determine the available modes. Scoped executed example: A 1D periodic Schnakenberg system of length 2pi, a=0.1, b=0.9 and diffusivities 0.01/1. Preserve the earlier linear-onset example and compare finite-amplitude nonlinear evolution and post-growth patterns from fixed reflection-symmetric data with independent Fourier–Galerkin/Radau references and separate spatial/temporal refinement. No general pattern selection, 2D, biological calibration or fluid-coupling claim.

#### Turing instability: linear growth and small-amplitude patterns

Supplementary execution example · Example definition or validation formula

$$
u_t=D_u u_{xx}+a-u+u^2v,\quad v_t=D_v v_{xx}+b-u^2v
$$

$$
\partial_t\widehat{\delta z}=(J-k^2D)\widehat{\delta z},\quad \widehat{\delta z}(t)=e^{(J-k^2D)t}\widehat{\delta z}(0)
$$

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

#### Finite-amplitude Schnakenberg transient: nonlinearity and independent reference

Supplementary execution example · Example definition or validation formula

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

#### Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence

Supplementary execution example · Example definition or validation formula

$$
u_t=D_u u_{xx}+a-u+u^2v,\qquad v_t=D_v v_{xx}+b-u^2v
$$

$$
\frac{d\langle u+v\rangle}{dt}=a+b-\langle u\rangle,\quad S_{n+1}-S_n=h(a+b-\langle\bar u\rangle)
$$

$$
\lambda_{h,k}=-4\sin^2(\pi k/N)/\Delta x^2,\quad\Phi_h=e^{hDL_h/2}\,\Phi_{\rm midpoint}^{F}(h)\,e^{hDL_h/2}
$$

$$
\|e\|_1=\max_s\frac1N\sum_j|e_{s,j}|,\quad\|e\|_2=\max_s\sqrt{\frac1N\sum_j e_{s,j}^2},\quad\|e\|_\infty=\max_{s,j}|e_{s,j}|
$$

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

#### Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input

Supplementary execution example · Example definition or validation formula

$$
u_t=0.01u_{xx}+0.1-u+u^2v,\qquad v_t=v_{xx}+0.9-u^2v
$$

$$
\lambda_{h,k}=-\frac{4}{\Delta x^2}\sin^2\!\left(\frac{\pi k}{N}\right),\quad L_h=\Psi_R^h\circ e^{hD L_{\rm FD}},\quad S_h=e^{hD L_{\rm FD}/2}\circ\Psi_R^h\circ e^{hD L_{\rm FD}/2}
$$

$$
\Psi_R^h(y)=y+hR\!\left(\frac{y+\Psi_R^h(y)}2\right),\quad \langle u+v\rangle_{n+1}-\langle u+v\rangle_n=h(0.1+0.9-\langle u_{\rm mid}\rangle)
$$

$$
E_2(h)=\max_{t\in\{.25,.5,.75,1\}}\max_{s\in\{u,v\}}\sqrt{\frac1N\sum_j(e_{s,j}(t))^2},\quad p_{\rm obs}=\log_2\frac{E_2(h)}{E_2(h/2)}
$$

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

### Exact and reference solutions

Use matrix-exponential linear growth rates at small amplitude; nonlinear supplements check independent Radau references, positivity and refinement. A linearization is not an exact saturated nonlinear pattern.

#### Turing instability: linear growth and small-amplitude patterns

Compare linear numerical fields with SciPy expm of continuum J-k²D and measure spatial convergence. Quantify the nonlinear run against a semidiscrete linear matrix exponential as a small-amplitude check, not validation of mature morphology.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en)

#### Finite-amplitude Schnakenberg transient: nonlinearity and independent reference

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en)

#### Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence

Compare raw L1/L2/L∞ with a spatially independent cosine Fourier–Galerkin/Radau reference (K32/64/96, cubic projection M=4(K+1)>4K, analytic Jacobian). Separately check K and ODE-tolerance sensitivity. Measure time order against a separately implemented Radau integration of the SAME FD semidiscretization. Norms are per-species mean-absolute/RMS/maximum, then the worse species. Record source/sink balance, every-step positive concentrations, initially absent k≥5 (first allowed k6 here), and departure from linearization. Convergence norms and reference sensitivities are assessed at the fixed final time; intermediate snapshot errors are separate evolution diagnostics.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en)

#### Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input

The reference independently assembles the SAME FD semidiscretization with a real-space sparse matrix and separately written reaction RHS, then integrates it unsplit with Radau. Tighter Radau and separate DOP853 runs measure reference sensitivity relative to the finest Strang error. Norms are per-species mean L1, RMS L2 and maximum L∞, then the worse species; refinement uses the maximum across the four common positive observation times. Also record Newton-tolerance sensitivity, positive tested substeps, reaction source/sink balance and reversed-Lie ordering.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Centered spatial difference](https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Classical RK4](https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Implicit midpoint](https://hrkoyama.github.io/numerical-methods-atlas/methods/implicit-midpoint/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Lie–Trotter splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/lie-trotter/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Strang splitting](https://hrkoyama.github.io/numerical-methods-atlas/methods/strang-splitting/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Turing instability: linear growth and small-amplitude patterns](https://hrkoyama.github.io/numerical-methods-atlas/validation/turing-schnakenberg/?lang=en)

Supplementary execution example

Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode.

Dimensionless a=0.1,b=0.9, equilibrium(1,0.9), diffusivities(0.01,1), periodic k=2 and initial amplitude1e-4. Restrict runs to linear t=1 and nonlinear t=4.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/atlas-models-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

One near-equilibrium onset experiment. No claim reproduces original-paper parameters/experiments, mature patterns, wavenumber selection from random noise or biological calibration.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/models/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/run.py)
- [/code/validated-examples/2026-11-22/models/test_models.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/models/test_models.py)

#### [Finite-amplitude Schnakenberg transient: nonlinearity and independent reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-nonlinear/?lang=en)

Supplementary execution example

Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics.

1D periodic x∈[0,2π), a=.1,b=.9,D=(.01,1). Common IC u=1+.08cos(2x)+.01cos(4x), v=.9−.03cos(2x)−.002cos(4x), restricted to a reflection-even, pi-periodic invariant subspace with a fixed origin.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

#### [Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence](https://hrkoyama.github.io/numerical-methods-atlas/validation/schnakenberg-pattern/?lang=en)

Supplementary execution example

Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual.

1D periodic x∈[0,2π), a=.1,b=.9,D=(.01,1). Common IC u=1+.08cos(2x)+.01cos(4x), v=.9−.03cos(2x)−.002cos(4x), restricted to a reflection-even, pi-periodic invariant subspace with a fixed origin.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/atlas-biology-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

A selected-symmetry1D educational model: no test of free noise-driven wavenumber selection, phase stability,2D spots or biological calibration. Not an original-paper reproduction. Implicit midpoint is A-stable but not L-stable or unconditionally positive; reactions do not conserve u+v. The initial coarse protocol failed; temporal resolution was strengthened while retaining every acceptance threshold and the failed record. No quantum calculations. Near-saturation refers to the reference90→100 test window; it proves no exact steady state, nonlinear stability or long-term attractor. A huge late linearized difference diagnoses failure of linearization, not numerical error.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/biology/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/run.py)
- [/code/validated-examples/2026-11-22/biology/biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/biology.py)
- [/code/validated-examples/2026-11-22/biology/test_biology.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/biology/test_biology.py)

#### [Lie–Trotter versus Strang on the same nonlinear reaction–diffusion input](https://hrkoyama.github.io/numerical-methods-atlas/validation/reaction-diffusion-splitting/?lang=en)

Supplementary execution example

Advance a 32-point Schnakenberg reaction–diffusion problem to T=1 with matched inputs and subsolvers. Four step sizes check first-/second-order temporal convergence, reference sensitivity, reaction balance and failure on nonconvergence in a lightweight comparison.

Nondimensional 1D periodic [0,2pi), N=32, a=.1, b=.9, D=(.01,1). The initial fields u₀=1+.08cos2x+.01cos4x and v₀=.9−.03cos2x−.002cos4x match the earlier finite-amplitude example. This new run ends at T=1, uses 16/32/64/128 steps and common output times 0/.25/.5/.75/1. The fixed input is reflection-even and pi-periodic.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/atlas-splitting-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This measures temporal error of the adopted compositions at fixed space, including splitting and midpoint-reaction discretization errors. It is not an exact continuum solution, spatial convergence check or independent PDE-engine comparison. Reactions do not conserve u+v; positivity is observed only for the fixed input. Work is reported as actual subflow calls, without runtime rankings or universal Strang superiority. This additional comparison of the existing Schnakenberg problem changes neither physical-problem counts, the common 22 examples, old release criteria nor success history. Long-time patterns, 2D and general boundaries are outside scope.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/splitting/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/run.py)
- [/code/validated-examples/2026-11-22/splitting/splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/splitting.py)
- [/code/validated-examples/2026-11-22/splitting/reference.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/reference.py)
- [/code/validated-examples/2026-11-22/splitting/test_splitting.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/splitting/test_splitting.py)
