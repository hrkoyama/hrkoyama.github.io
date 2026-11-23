# Orszag–Tang渦（CT・GLM・発散誤差摂動を統合） / Orszag–Tang vortex (CT/GLM/error variants merged)

https://hrkoyama.github.io/numerical-methods-atlas/problems/orszag-tang/

## 日本語

[CT・GLMを統合した1問題のうち、CTの保存フレームを代表表示。](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/mhd/) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#orszag-tang)

### 方程式・問題の定義

この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。

#### [理想MHD](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。

#### Orszag–Tang：CT・GLMと独立Athena++比較

補助実行例 · 実行例の定義・検証式

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

#### Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束

補助実行例 · 実行例の定義・検証式

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

#### 後期Orszag–Tang：独立参照と圧縮構造

補助実行例 · 実行例の定義・検証式

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

### 厳密解・参照解

保存則・各離散配置に対応する磁場発散と、別実行のAthena++数値参照を確認します。この非線形MHD問題の厳密解を提供するものではありません。 実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

#### [後期Orszag–Tang：独立有限格子の密度・圧力参照](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja#postshock-orszag-tang-ja-measurements)

有限格子の数値参照 · 関連モデルの参照

rho0=25/(36*pi); p0=5/(12*pi); v=(sin(2*pi*y),-sin(2*pi*x),0); Az=(cos(4*pi*x)-2*cos(2*pi*y))/(4*pi*sqrt(4*pi)); T=.2.

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。公式Athena++を128²/256²と最細CFL半減でT=.2まで進めます。終端保存変数を保守的に粗視化し、その後で圧力を計算します。参照圧力の平均を先に作る規約ではありません。

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

#### Orszag–Tang：CT・GLMと独立Athena++比較

16²/32²/64²で密度とByのL1誤差、質量・エネルギードリフト、正値性を測定。独立参照は128²/256²でも収束を確認し、細胞平均を保存的に制限します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja)

#### Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束

密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja)

#### 後期Orszag–Tang：独立参照と圧縮構造

実行前契約で47pytest・全12計算を固定。3格子と最細格子の時間刻み半減を分離し、全段の正値性・有限性、保存量、Courant数、5時刻の実場を保存します。Athena++の2格子と刻み半減で参照を検定。終端保存変数を保守的に粗視化し、誤差と参照感度を分離します。共通セル発散と主計算の固有面発散は別の検査です。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja)

### 計算法

この問題に明示的に結び付けられた補助実行例と、存在する場合は共通実行例の手法です。別問題の配布物を借用していません。

- [制約輸送法／CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [GLM発散クリーニング](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [HLLDのMHDリーマン解法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [MUSCL再構成](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり
- [Heun法／SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [Orszag–Tang：CT・GLMと独立Athena++比較](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=ja)

補助実行例

同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。

単位正方形、γ=5/3、μ₀=1、vz=Bz=0、t=0.05。rho=25/(36π)、p=5/(12π)、v=(-sin2πy,sin2πx)、B=(-sin2πy,sin4πx)/sqrt(4π)。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

CTの面上divergenceとGLMの中心差分divergenceは異なる演算子です。共通cell演算子の値も別記します。Athenaの初期磁場はベクトルポテンシャルの差分による面平均で、同じ連続場の離散化差を含みます。短時間の平面MHD比較であり、衝撃波・3D・UCTやCTUの検証ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)

#### [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja)

補助実行例

同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。

標準周期OT、γ=5/3、ρ=25/(36π)、p=5/(12π)、v=(−sin2πy,sin2πx)、B=(−sin2πy,sin4πx)/√(4π)、t=.05。16²/32²/64²の両法に192刻みを共用します。旧配布版を改変しない追加検証です。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

短時間の滑らかなOTで、衝撃波後・3D・一般のcleaning性能の認証ではありません。独立Athena参照も有限格子数値解で、増分は誤差上界ではありません。旧128²/CFL.3は履歴だけで256²/CFL.15との組を純粋な格子次数に使いません。定数LLFによるGLMのdiv=ψ=0保存をcleaning成功とは呼びません。native面divと共通中心divを区別し、中心演算子のcheckerboard盲点も残します。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)

#### [後期Orszag–Tang：独立参照と圧縮構造](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=ja)

補助実行例

圧縮性理想MHDのOrszag–TangをT=.2まで進め、相互作用する圧縮・衝撃波構造の密度と圧力を独立有限格子参照で検査します。

γ=5/3、[-.5,.5]²周期、ρ=25/(36π)、p=5/(12π)、vx=sin2πy、vy=−sin2πx、Az=(cos4πx−2cos2πy)/(4π√(4π))、16/32/64²セル。原著の非圧縮・粘性抵抗モデルの再現ではありません。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

少数の固定入力に対する教育用検証です。HLLDのHLLE代替と再構成の正値性スケーリングを数え、セル状態の床・クリップ・再試行は行いません。有限格子参照は厳密解ではなく、任意問題の安定性・正値性や普遍的次数を保証しません。独立比較は終端のみ。中間Athena時刻は指定四半時刻直後で、正確に整列した場とは表示しません。Athenaの固有面発散は出力しておらず測定を主張しません。密度比は圧縮の診断であり数学的衝撃波の証明ではありません。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-23/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/run.py)
- [/code/validated-examples/2026-11-23/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-23/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py)

## English

[Stored CT frame representing the merged CT/GLM problem.](https://hrkoyama.github.io/numerical-methods-atlas/assets/movies/orszag-tang-ct/frame-080.webp)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/mhd/) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#orszag-tang-en)

### Equations and problem definitions

Representative equations related to this problem. See the image/problem conditions and each execution example for initial conditions, boundary conditions and parameters.

#### [Ideal magnetohydrodynamics](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#mhd-en)

$$
\rho_t+\nabla\cdot(\rho\boldsymbol v)=0
$$

$$
(\rho\boldsymbol v)_t+\nabla\cdot[\rho\boldsymbol v\otimes\boldsymbol v+(p+B^2/2)I-\boldsymbol B\otimes\boldsymbol B]=0
$$

$$
E_t+\nabla\cdot[(E+p+B^2/2)\boldsymbol v-(\boldsymbol v\cdot\boldsymbol B)\boldsymbol B]=0
$$

$$
\boldsymbol B_t=\nabla\times(\boldsymbol v\times\boldsymbol B),\quad\nabla\cdot\boldsymbol B=0
$$

Representative ideal MHD with magnetic permeability set to one. E is total thermal, kinetic and magnetic energy density. Follow CT/GLM, divergence conventions and HLLD tests.

#### Orszag–Tang: CT, GLM and independent Athena++

Supplementary execution example · Example definition or validation formula

$$
\nabla\cdot\mathbf B=0,\qquad \mathbf B_t+\nabla\times\mathbf E=0
$$

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

#### Orszag–Tang: matched CT/GLM and converged independent references

Supplementary execution example · Example definition or validation formula

$$
F_{i+1/2}=\tfrac12[F(U_L)+F(U_R)-\alpha(U_R-U_L)],\qquad\alpha=3
$$

$$
(B_x)_t+\partial_x\psi+\partial_y(v_yB_x-v_xB_y)=0,\quad\psi_t+c_h^2\nabla\cdot\mathbf B=-\kappa\psi
$$

$$
D_h^{\rm face}\,\operatorname{curl}_h E=0,\qquad D_h^{\rm cell}\ne D_h^{\rm face}
$$

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

#### Late Orszag-Tang: independent reference and compression structure

Supplementary execution example · Example definition or validation formula

$$
\partial_tU+\partial_xF_x(U)+\partial_yF_y(U)=0,\quad U=(\rho,\rho\mathbf v,E,\mathbf B)
$$

$$
E=\frac{p}{\gamma-1}+\frac12\rho|\mathbf v|^2+\frac12|\mathbf B|^2,\quad\gamma=5/3
$$

$$
\frac{dB_x}{dt}=-D_y\mathcal E_z,\quad\frac{dB_y}{dt}=D_x\mathcal E_z,\quad D_xB_x+D_yB_y=\mathrm{constant}
$$

$$
\bar U_i^{\mathrm{ref}}=\frac1{N_i}\sum_{j\in i}\bar U_j^{\mathrm{fine}},\qquad e_1=\frac{\sum|U-U^{\mathrm{ref}}|}{\sum|U^{\mathrm{ref}}|}
$$

$$
\rho_0=\frac{25}{36\pi},\quad p_0=\frac5{12\pi},\quad\mathbf v_0=(\sin2\pi y,-\sin2\pi x,0)
$$

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

### Exact and reference solutions

Check conservation, divergence appropriate to each discrete layout, and separately run Athena++ numerical references. These are not exact solutions of the nonlinear MHD problem. Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

#### [Late Orszag-Tang: independent finite-grid density/pressure reference](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en#postshock-orszag-tang-en-measurements)

Finite-grid numerical reference · Related-model reference

rho0=25/(36*pi); p0=5/(12*pi); v=(sin(2*pi*y),-sin(2*pi*x),0); Az=(cos(4*pi*x)-2*cos(2*pi*y))/(4*pi*sqrt(4*pi)); T=.2.

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model. Run official Athena++ at128²/256² and finest-grid half CFL to T.2. Conservatively restrict final conserved variables before computing pressure; pressure is not averaged separately.

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

#### Orszag–Tang: CT, GLM and independent Athena++

Measure density/By L1 error, mass/energy drift and positivity on 16²/32²/64². Check the independent 128²/256² reference and conservatively restrict its fine-cell averages.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en)

#### Orszag–Tang: matched CT/GLM and converged independent references

Measure density/magnetic L1 error, mesh improvement, positivity, conservation and div/psi. Athena256²/512² both useCFL.15; fixed512² CFL.3/.15 checks reference time sensitivity, with increments compared against.1 of primary error. At fixed16², compare primary time refinement with separately executed DOP853 and check finest-grid step doubling.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en)

#### Late Orszag-Tang: independent reference and compression structure

Freeze 47 pytest checks and12 primary runs before execution. Separate three grids and a finest-grid half-dt probe; retain stage positivity/finiteness, conservation, Courant number and five actual field snapshots. Qualify Athena++ with two grids and a half-CFL probe. Conservatively restrict final conserved states and separate reference sensitivity from primary error. Common-cell divergence and primary native-face divergence are distinct checks.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en)

### Numerical methods

Methods from explicitly bound supplementary examples and, where present, the common execution example. No release for a different problem is borrowed.

- [Constrained transport / CT](https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [GLM divergence cleaning](https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [HLLD MHD Riemann solver](https://hrkoyama.github.io/numerical-methods-atlas/methods/hlld/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [MUSCL reconstruction](https://hrkoyama.github.io/numerical-methods-atlas/methods/muscl/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code
- [Heun / SSPRK(2,2)](https://hrkoyama.github.io/numerical-methods-atlas/methods/heun/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Orszag–Tang: CT, GLM and independent Athena++](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-independent/?lang=en)

Supplementary execution example

Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++.

Unit square, gamma=5/3, mu0=1, vz=Bz=0, t=0.05. rho=25/(36pi), p=5/(12pi), v=(-sin2piy,sin2pix), B=(-sin2piy,sin4pix)/sqrt(4pi).

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/atlas-mhd-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Face CT divergence and centered GLM divergence use different operators; common cell-centered diagnostics are also reported. Athena initializes face-averaged magnetic fields by differencing a vector potential, so comparison includes discretization differences of identical continuous data. This is a short planar test, not validation of shocks, 3D, UCT or CTU.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd/legacy/mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/legacy/mhd.py)
- [/code/validated-examples/2026-11-22/mhd/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/run.py)
- [/code/validated-examples/2026-11-22/mhd/test_validation.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd/test_validation.py)

#### [Orszag–Tang: matched CT/GLM and converged independent references](https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=en)

Supplementary execution example

Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated.

Standard periodic OT: gamma5/3, rho25/(36pi), p5/(12pi), v=(−sin2piy,sin2pix), B=(−sin2piy,sin4pix)/sqrt(4pi), t=.05. Both methods share192 steps on16²/32²/64². This supplements the previous immutable release.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/atlas-mhd-convergence-2026-11-22.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Short smooth OT, not certification of post-shock,3D or general cleaning behavior. Athena is a finite-grid numerical reference; increments are not error bounds. Historical128²/CFL.3 is not paired with256²/CFL.15 to infer a pure spatial order. Constant-LLF preservation of GLM div=psi=0 is not evidence of active cleaning. Native face and common centered divergences differ; centered checkerboard blind spots remain.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-22/mhd-convergence/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/solver.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/experiments.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/experiments.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/run.py)
- [/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py](https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/test_convergence.py)

#### [Late Orszag-Tang: independent reference and compression structure](https://hrkoyama.github.io/numerical-methods-atlas/validation/postshock-orszag-tang/?lang=en)

Supplementary execution example

Evolve compressible ideal-MHD Orszag-Tang to T.2 and check density/pressure in interacting compression/shock structure against an independent finite-grid reference.

gamma5/3,periodic[-.5,.5]²,rho25/(36pi),p5/(12pi),vx=sin2piy,vy=-sin2pix,Az=(cos4pix-2cos2piy)/(4pi sqrt4pi),16/32/64² cells. This does not reproduce the original incompressible viscous/resistive model.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/atlas-mhd-transport-2026-11-23.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

Educational fixed inputs only. Count HLLD-to-HLLE fallbacks and face reconstruction positivity scaling; no cell floor/clipping/retry. Finite-grid references are not exact solutions; no universal stability, positivity or order guarantee. Independent comparisons are final-only. Intermediate Athena outputs occur just after requested quarter times and are not matched frames. Athena native-face divergence is not exported/measured. Density contrast diagnoses compression, not a mathematical proof of shock formation.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-23/mhd-transport/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/run.py)
- [/code/validated-examples/2026-11-23/mhd-transport/solver.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/solver.py)
- [/code/validated-examples/2026-11-23/mhd-transport/hlld.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/hlld.py)
- [/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/references/qualify_saved.py)
- [/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py](https://hrkoyama.github.io/code/validated-examples/2026-11-23/mhd-transport/test_mhd.py)
