# 小さな量子模型と保存参照カード

固定2準位連成・1D固有対・最小分子・3波模型と、H/He・周期Heの保存参照監査です。重い一般範囲は残します。

共通22実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。

## 2準位模型のBO/CP型連成と短い核熱浴

電子角と核座標を実際に結合した2準位模型を、短いNVEと核熱浴で比較します。

**使用手法**

- [Born–Oppenheimer分子動力学（BOMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/born-oppenheimer-md/?lang=ja) (`born-oppenheimer-md`)
- [カー–パリネロ法（CPMD）](https://hrkoyama.github.io/numerical-methods-atlas/methods/car-parrinello-md/?lang=ja) (`car-parrinello-md`)
- [Langevinサーモスタット](https://hrkoyama.github.io/numerical-methods-atlas/methods/langevin-thermostat/?lang=ja) (`langevin-thermostat`)
- [速度Verlet／粒子leapfrog法](https://hrkoyama.github.io/numerical-methods-atlas/methods/verlet/?lang=ja) (`verlet`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-algorithm)

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

- [2準位電子角と核のBO/CP型模型](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#two-state-bo-cp-model-ja) (`two-state-bo-cp-model`)

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。


**問題の図**

![2準位模型のBO/CP型連成と短い核熱浴：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/two-state-bo-cp-ou.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja) (`two-state-bo-cp-model`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/two-state-bo-cp-model/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/?lang=ja#two-state-bo-cp-ou-ja-validation)

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

- [2準位模型のBO/CP型連成と短い核熱浴](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-two-state-bo-cp-ou-ja) (`two-state-bo-cp-ou`; 同じ問題の参照 · 半解析参照)

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。
### 前提・単位・境界

無次元の核座標と規格化した1電子角。3固定刻み、2架空質量、1固定seedのOU熱浴です。 自作模型の無次元単位。Q,時間,電子角,温度を固定し、M=20、架空角質量μ=.04/.01。cp.xのemass規約とは別です。

**編集上の補足**

長時間第一原理NVE、一般の多軌道直交制約・SCF誤差、電子/核の一般熱浴、正準平衡・断熱分離・エルゴード性、実物質は未検証。

### 採用した計算法

解析BO力とCP型作用の式をVerlet/BAOABで積分し、核熱と架空電子運動エネルギーを分けます。

$$
H(Q)=\frac{kQ^2}{2}I+\begin{pmatrix}-\Delta&gQ\\gQ&\Delta\end{pmatrix},\quad\psi=(\cos\theta,\sin\theta)^T
$$

$$
E(Q,\theta)=\frac{kQ^2}{2}-\Delta\cos(2\theta)+gQ\sin(2\theta),\quad E_-(Q)=\frac{kQ^2}{2}-\sqrt{\Delta^2+g^2Q^2}
$$

$$
M\ddot Q=-kQ-g\sin(2\theta),\quad\mu\ddot\theta=-2\Delta\sin(2\theta)-2gQ\cos(2\theta)
$$

$$
V^+=aV^-+\sqrt{(T/M)(1-a^2)}\,\xi,\quad a=e^{-\gamma h},\quad Q_{\rm bath}=\sum\Delta K_{\rm nuclear}
$$

### 比較・検証

解析勾配、4096/8192段の固定RK4感度、拡張エネルギーとOU条件付き分散を照合します。

### 確認の限界

短い自作教育模型です。第一原理・長いNVE・一般CPMD・正準平衡・エルゴード性の成功は主張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "95 bo-0 NVE extended energy drift": 4.54374582403716e-08,
    "95 bo-1 NVE extended energy drift": 1.135934568630148e-08,
    "95 bo-2 NVE extended energy drift": 2.8398352558411943e-09,
    "95 cp-mu004-0 NVE extended energy drift": 4.543430420778094e-08,
    "95 cp-mu004-1 NVE extended energy drift": 1.1358568974273453e-08,
    "95 cp-mu004-2 NVE extended energy drift": 2.839641743968002e-09,
    "95 cp-mu001 NVE extended energy drift": 2.8397284523862254e-09,
    "95 bo finest RK4 state comparison": 5.443721431889809e-09,
    "95 cp-mu004 finest RK4 state comparison": 9.898870595217574e-08,
    "95 bo fixed RK4 companion sensitivity": 2.5547594848822963e-15,
    "95 cp-mu004 fixed RK4 companion sensitivity": 1.2252872249276024e-15,
    "95 OU extended energy minus measured heat": 4.47292801061816e-09,
    "95 OU conditional temperature variance identity": 0.0,
    "95 normalized orbital": 2.220446049250313e-16
  },
  "checks": {
    "95 bo-0 NVE extended energy drift": true,
    "95 bo-1 NVE extended energy drift": true,
    "95 bo-2 NVE extended energy drift": true,
    "95 cp-mu004-0 NVE extended energy drift": true,
    "95 cp-mu004-1 NVE extended energy drift": true,
    "95 cp-mu004-2 NVE extended energy drift": true,
    "95 cp-mu001 NVE extended energy drift": true,
    "95 bo finest RK4 state comparison": true,
    "95 cp-mu004 finest RK4 state comparison": true,
    "95 bo fixed RK4 companion sensitivity": true,
    "95 cp-mu004 fixed RK4 companion sensitivity": true,
    "95 OU extended energy minus measured heat": true,
    "95 OU conditional temperature variance identity": true,
    "95 normalized orbital": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/two-state-bo-cp-ou/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- Unified Approach for Molecular Dynamics and Density-Functional Theory [accessed 2026-11-25]. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.2471; review_level=abstract-and-metadata
出版社の題名・著者・日付・DOIと抄録のみ。PDF本文・式は今回読んでおらず、Si計算やこの自作模型を原論文から再現したとは主張しません。

- Quantum ESPRESSO cp.x input description [accessed 2026-11-25]. https://www.quantum-espresso.org/Doc/INPUT_CP.html; review_level=selected-official-documentation
公式cp.xのemass・直交化の選択箇所のみ。この無次元電子角の架空質量を同じ物理規約へ読み替えません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## H/Heの式・密度・固定参照カード

既存H/Heの式と保存参照を、単位・規格化・模型の限界とともに示します。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)
- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-algorithm)

pとn、軌道固有値と全エネルギーを区別し、既存の式と3保存行を照合します。

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。


**問題の図**

![H/Heの式・密度・固定参照カード：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/atomic-reference-cards.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[He基底状態：閉殻HF・交換のみLDA](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja) (`helium-ground-state`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/helium-ground-state/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/?lang=ja#atomic-reference-cards-ja-validation)

選択3行は各40基底関数です。保存値・電子数・出典を照合し、新SCFは実行しません。

- [H/Heの式・密度・固定参照カード](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-atomic-reference-cards-ja) (`atomic-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。
### 前提・単位・境界

Hは無限質量点核の1電子、Heは球対称1軌道の閉殻HFまたは交換のみLDAです。 エネルギーhartree、rはbohr。uはbohr^(-1/2)、pはbohr^(-1)、nはbohr^(-3)。保存3行は各40基底関数であり40計算行ではありません。

**編集上の補足**

参照カードの整備・保存値照合であり、新SCF/新独立参照は0回。相関込み厳密He、完全基底極限、全軌道の再実行は主張しません。

### 採用した計算法

pとn、軌道固有値と全エネルギーを区別し、既存の式と3保存行を照合します。

$$
E_n=-\frac{Z^2}{2n^2},\quad H_lu=-\frac12u^{\prime\prime}+\left[\frac{l(l+1)}{2r^2}-\frac Zr\right]u
$$

$$
\Psi=u(r)Y_{lm}/r,\quad\int|u|^2\,dr=1,\quad p_{\rm He}(r)=2|u|^2,\quad n_{\rm He}(r)=\frac{p_{\rm He}(r)}{4\pi r^2}
$$

$$
\int p_{\rm He}(r)\,dr=\int n_{\rm He}(\mathbf r)\,d^3r=2,\quad E_x^{\rm HF}=-E_H/2\ \text{one-orbital restricted Hartree--Fock He only}
$$

### 比較・検証

選択3行は各40基底関数です。保存値・電子数・出典を照合し、新SCFは実行しません。

### 確認の限界

有限基底HFや交換のみLDAを相関込みの厳密Heとは呼びません。独立参照の再生成は0回です。

### 保存実測値と判定

```json
{
  "metrics": {
    "96 selected saved row count": 0.0,
    "96 saved energy literal 0": 0.0,
    "96 basis functions 0": 0.0,
    "96 saved electron count 0": 1.7763568394002505e-15,
    "96 saved energy literal 1": 0.0,
    "96 basis functions 1": 0.0,
    "96 saved electron count 1": 3.1086244689504383e-15,
    "96 saved energy literal 2": 0.0,
    "96 basis functions 2": 0.0,
    "96 saved electron count 2": 3.1086244689504383e-15
  },
  "checks": {
    "96 selected saved row count": true,
    "96 saved energy literal 0": true,
    "96 basis functions 0": true,
    "96 saved electron count 0": true,
    "96 saved energy literal 1": true,
    "96 basis functions 1": true,
    "96 saved electron count 1": true,
    "96 saved energy literal 2": true,
    "96 basis functions 2": true,
    "96 saved electron count 2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/atomic-reference-cards/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
同一作業内の選択閲読：式7–8、13–15、24–35と近傍のHO/Coulomb・規格化・測度。章全体・出典書籍の通読ではありません。

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 1次元箱型井戸・量子調和振動子

1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-algorithm)

NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。


**問題の図**

![1次元箱型井戸・量子調和振動子：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja) (`quantum-box-ho`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-validation)

Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。

- [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-quantum-box-ho-ja) (`quantum-box-ho`; 同じ問題の参照 · 解析参照)

8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。
### 前提・単位・境界

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

**編集上の補足**

8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。

### 採用した計算法

NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

### 比較・検証

Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。

### 確認の限界

HOの壁誤差と格子誤差の個別保証はありません。節の近零点・tailは診断、0.003は精度目標です。

### 保存実測値と判定

```json
{
  "metrics": {
    "97 box-M32 native_norm_error": 9.992007221626409e-16,
    "97 box-M32 physical_norm_error": 9.992007221626409e-16,
    "97 box-M32 orthogonality_error": 9.992007221626409e-16,
    "97 box-M32 state1 residual": 2.6534314217337773e-16,
    "97 box-M32 state1 same-grid oracle": 2.521780905296546e-15,
    "97 box-M32 state2 residual": 2.6489743749213535e-16,
    "97 box-M32 state2 same-grid oracle": 1.6250574155051521e-15,
    "97 box-M32 state3 residual": 2.3939284948881844e-16,
    "97 box-M32 state3 same-grid oracle": 2.2560444050504554e-15,
    "97 box-M64 native_norm_error": 4.440892098500626e-16,
    "97 box-M64 physical_norm_error": 4.440892098500626e-16,
    "97 box-M64 orthogonality_error": 5.729429494880433e-16,
    "97 box-M64 state1 residual": 3.628867495606101e-16,
    "97 box-M64 state1 same-grid oracle": 1.5283589494924628e-13,
    "97 box-M64 state2 residual": 3.5175380832319105e-16,
    "97 box-M64 state2 same-grid oracle": 2.5578063468007826e-14,
    "97 box-M64 state3 residual": 3.511156850072398e-16,
    "97 box-M64 state3 same-grid oracle": 9.295888967353658e-15,
    "97 box-M128 native_norm_error": 1.3322676295501878e-15,
    "97 box-M128 physical_norm_error": 8.881784197001252e-16,
    "97 box-M128 orthogonality_error": 1.1102230246251565e-15,
    "97 box-M128 state1 residual": 3.7340644105619856e-16,
    "97 box-M128 state1 same-grid oracle": 7.066470719683718e-13,
    "97 box-M128 state2 residual": 3.901829244394146e-16,
    "97 box-M128 state2 same-grid oracle": 1.6885756120423205e-13,
    "97 box-M128 state3 residual": 4.0863269302611023e-16,
    "97 box-M128 state3 same-grid oracle": 7.042499776870415e-14,
    "97 HO-L8-h0.25 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 physical_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 orthogonality_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.25 state0 residual": 1.384362487647675e-16,
    "97 HO-L8-h0.25 state0 reflection parity": 9.906146009304781e-16,
    "97 HO-L8-h0.25 state1 residual": 1.549514541364104e-16,
    "97 HO-L8-h0.25 state1 reflection parity": 2.169025096981292e-15,
    "97 HO-L8-h0.25 state2 residual": 1.26030926507246e-16,
    "97 HO-L8-h0.25 state2 reflection parity": 5.378632453105551e-15,
    "97 HO-L8-h0.125 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.125 physical_norm_error": 8.881784197001252e-16,
    "97 HO-L8-h0.125 orthogonality_error": 8.881784197001252e-16,
    "97 HO-L8-h0.125 state0 residual": 3.9740329134654874e-16,
    "97 HO-L8-h0.125 state0 reflection parity": 1.489799852793317e-14,
    "97 HO-L8-h0.125 state1 residual": 4.0343427613151107e-16,
    "97 HO-L8-h0.125 state1 reflection parity": 3.32819383816502e-14,
    "97 HO-L8-h0.125 state2 residual": 3.816857166136067e-16,
    "97 HO-L8-h0.125 state2 reflection parity": 3.1052104675910025e-14,
    "97 HO-L8-h0.0625 native_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.0625 physical_norm_error": 1.1102230246251565e-15,
    "97 HO-L8-h0.0625 orthogonality_error": 1.3322676295501878e-15,
    "97 HO-L8-h0.0625 state0 residual": 5.118810100977104e-16,
    "97 HO-L8-h0.0625 state0 reflection parity": 1.0562240570035153e-14,
    "97 HO-L8-h0.0625 state1 residual": 5.6425322872051155e-16,
    "97 HO-L8-h0.0625 state1 reflection parity": 3.3151730411536006e-14,
    "97 HO-L8-h0.0625 state2 residual": 4.424438066999679e-16,
    "97 HO-L8-h0.0625 state2 reflection parity": 3.9175195970046425e-14,
    "97 HO-L4-h0.125 native_norm_error": 8.881784197001252e-16,
    "97 HO-L4-h0.125 physical_norm_error": 6.661338147750939e-16,
    "97 HO-L4-h0.125 orthogonality_error": 6.661338147750939e-16,
    "97 HO-L4-h0.125 state0 residual": 2.8638408377792463e-16,
    "97 HO-L4-h0.125 state0 reflection parity": 5.622962058212243e-15,
    "97 HO-L4-h0.125 state1 residual": 2.7780454534440377e-16,
    "97 HO-L4-h0.125 state1 reflection parity": 1.3088888066254994e-14,
    "97 HO-L4-h0.125 state2 residual": 3.13657233698048e-16,
    "97 HO-L4-h0.125 state2 reflection parity": 1.5345752054778173e-14,
    "97 HO-L6-h0.125 native_norm_error": 6.661338147750939e-16,
    "97 HO-L6-h0.125 physical_norm_error": 4.440892098500626e-16,
    "97 HO-L6-h0.125 orthogonality_error": 1.0478097465287758e-15,
    "97 HO-L6-h0.125 state0 residual": 2.3361979300913016e-16,
    "97 HO-L6-h0.125 state0 reflection parity": 1.654208719984383e-15,
    "97 HO-L6-h0.125 state1 residual": 3.0895334790910436e-16,
    "97 HO-L6-h0.125 state1 reflection parity": 3.966086461776309e-15,
    "97 HO-L6-h0.125 state2 residual": 3.0577186768266187e-16,
    "97 HO-L6-h0.125 state2 reflection parity": 9.059939709541788e-15,
    "97 box finest relative continuum 0": 5.019839662078447e-05,
    "97 box reduction lower (0, 0)": 3.99903629835137,
    "97 box reduction upper (0, 0)": 3.99903629835137,
    "97 box reduction lower (0, 1)": 3.9997589977320964,
    "97 box reduction upper (0, 1)": 3.9997589977320964,
    "97 box finest relative continuum 1": 0.0002007814885717256,
    "97 box reduction lower (1, 0)": 3.996146764158027,
    "97 box reduction upper (1, 0)": 3.996146764158027,
    "97 box reduction lower (1, 1)": 3.999036298147065,
    "97 box reduction upper (1, 1)": 3.999036298147065,
    "97 box finest relative continuum 2": 0.00045171299567713406,
    "97 box reduction lower (2, 0)": 3.9913360615376745,
    "97 box reduction upper (2, 0)": 3.9913360615376745,
    "97 box reduction lower (2, 1)": 3.9978320428851237,
    "97 box reduction upper (2, 1)": 3.9978320428851237,
    "97 HO finest total error 0": 0.0001221001366430441,
    "97 HO finest total error 1": 0.0006106201113647014,
    "97 HO finest total error 2": 0.0015879589598619681
  },
  "checks": {
    "97 box-M32 native_norm_error": true,
    "97 box-M32 physical_norm_error": true,
    "97 box-M32 orthogonality_error": true,
    "97 box-M32 state1 residual": true,
    "97 box-M32 state1 same-grid oracle": true,
    "97 box-M32 state2 residual": true,
    "97 box-M32 state2 same-grid oracle": true,
    "97 box-M32 state3 residual": true,
    "97 box-M32 state3 same-grid oracle": true,
    "97 box-M64 native_norm_error": true,
    "97 box-M64 physical_norm_error": true,
    "97 box-M64 orthogonality_error": true,
    "97 box-M64 state1 residual": true,
    "97 box-M64 state1 same-grid oracle": true,
    "97 box-M64 state2 residual": true,
    "97 box-M64 state2 same-grid oracle": true,
    "97 box-M64 state3 residual": true,
    "97 box-M64 state3 same-grid oracle": true,
    "97 box-M128 native_norm_error": true,
    "97 box-M128 physical_norm_error": true,
    "97 box-M128 orthogonality_error": true,
    "97 box-M128 state1 residual": true,
    "97 box-M128 state1 same-grid oracle": true,
    "97 box-M128 state2 residual": true,
    "97 box-M128 state2 same-grid oracle": true,
    "97 box-M128 state3 residual": true,
    "97 box-M128 state3 same-grid oracle": true,
    "97 HO-L8-h0.25 native_norm_error": true,
    "97 HO-L8-h0.25 physical_norm_error": true,
    "97 HO-L8-h0.25 orthogonality_error": true,
    "97 HO-L8-h0.25 state0 residual": true,
    "97 HO-L8-h0.25 state0 reflection parity": true,
    "97 HO-L8-h0.25 state1 residual": true,
    "97 HO-L8-h0.25 state1 reflection parity": true,
    "97 HO-L8-h0.25 state2 residual": true,
    "97 HO-L8-h0.25 state2 reflection parity": true,
    "97 HO-L8-h0.125 native_norm_error": true,
    "97 HO-L8-h0.125 physical_norm_error": true,
    "97 HO-L8-h0.125 orthogonality_error": true,
    "97 HO-L8-h0.125 state0 residual": true,
    "97 HO-L8-h0.125 state0 reflection parity": true,
    "97 HO-L8-h0.125 state1 residual": true,
    "97 HO-L8-h0.125 state1 reflection parity": true,
    "97 HO-L8-h0.125 state2 residual": true,
    "97 HO-L8-h0.125 state2 reflection parity": true,
    "97 HO-L8-h0.0625 native_norm_error": true,
    "97 HO-L8-h0.0625 physical_norm_error": true,
    "97 HO-L8-h0.0625 orthogonality_error": true,
    "97 HO-L8-h0.0625 state0 residual": true,
    "97 HO-L8-h0.0625 state0 reflection parity": true,
    "97 HO-L8-h0.0625 state1 residual": true,
    "97 HO-L8-h0.0625 state1 reflection parity": true,
    "97 HO-L8-h0.0625 state2 residual": true,
    "97 HO-L8-h0.0625 state2 reflection parity": true,
    "97 HO-L4-h0.125 native_norm_error": true,
    "97 HO-L4-h0.125 physical_norm_error": true,
    "97 HO-L4-h0.125 orthogonality_error": true,
    "97 HO-L4-h0.125 state0 residual": true,
    "97 HO-L4-h0.125 state0 reflection parity": true,
    "97 HO-L4-h0.125 state1 residual": true,
    "97 HO-L4-h0.125 state1 reflection parity": true,
    "97 HO-L4-h0.125 state2 residual": true,
    "97 HO-L4-h0.125 state2 reflection parity": true,
    "97 HO-L6-h0.125 native_norm_error": true,
    "97 HO-L6-h0.125 physical_norm_error": true,
    "97 HO-L6-h0.125 orthogonality_error": true,
    "97 HO-L6-h0.125 state0 residual": true,
    "97 HO-L6-h0.125 state0 reflection parity": true,
    "97 HO-L6-h0.125 state1 residual": true,
    "97 HO-L6-h0.125 state1 reflection parity": true,
    "97 HO-L6-h0.125 state2 residual": true,
    "97 HO-L6-h0.125 state2 reflection parity": true,
    "97 box finest relative continuum 0": true,
    "97 box reduction lower (0, 0)": true,
    "97 box reduction upper (0, 0)": true,
    "97 box reduction lower (0, 1)": true,
    "97 box reduction upper (0, 1)": true,
    "97 box finest relative continuum 1": true,
    "97 box reduction lower (1, 0)": true,
    "97 box reduction upper (1, 0)": true,
    "97 box reduction lower (1, 1)": true,
    "97 box reduction upper (1, 1)": true,
    "97 box finest relative continuum 2": true,
    "97 box reduction lower (2, 0)": true,
    "97 box reduction upper (2, 0)": true,
    "97 box reduction lower (2, 1)": true,
    "97 box reduction upper (2, 1)": true,
    "97 HO finest total error 0": true,
    "97 HO finest total error 1": true,
    "97 HO finest total error 2": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
同一作業内の選択閲読：式7–8、13–15、24–35と近傍のHO/Coulomb・規格化・測度。章全体・出典書籍の通読ではありません。

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
NumPy2.0公式の引数、昇順固有値、規格化した固有ベクトル、Hermitian三角格納、LinAlgError、LAPACKの説明を選択閲読。全LAPACK実装・誤差証明の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 最小基底H2のRHF/UHF/FCI・2固定幾何

同じ最小基底H2の2固定幾何で、RHF/UHF/有限基底FCIとスピン対称性を比較します。

**使用手法**

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) (`configuration-interaction`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-algorithm)

固定SCFでRHFと対称性を破ったUHFを求め、4x4二電子Hamiltonianを対角化します。

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

- [最小2電子模型のスピン非制限HF](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#unrestricted-hartree-fock-model-ja) (`unrestricted-hartree-fock-model`)

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。


**問題の図**

![最小基底H2のRHF/UHF/FCI・2固定幾何：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h2-rhf-uhf-fci.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[H₂分子RHF：独立参照・SCF・s型基底拡大](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja) (`h2-rhf`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h2-rhf/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/?lang=ja#h2-rhf-uhf-fci-ja-validation)

保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。

- [最小基底H2のRHF/UHF/FCI・2固定幾何](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h2-rhf-uhf-fci-ja) (`h2-rhf-uhf-fci`; 同じ問題の参照 · 半解析参照)

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。
### 前提・単位・境界

H-H距離1.4/3.0bohr、2電子、HごとにSTO-3G縮約s軌道を1個用います。 核間距離1.4/3.0bohr、全エネルギーhartree。各Hに同じ明示3primitiveのs型収縮を1つ置く2AO/2電子の固定部分空間。

**編集上の補足**

2固定距離のみ。有限基底FCIは連続空間の厳密解ではなく、UHF定常解の一般的な大域最小性は保証しません。角運動量・完全基底・広い解離曲線は未検証。

### 採用した計算法

固定SCFでRHFと対称性を破ったUHFを求め、4x4二電子Hamiltonianを対角化します。

$$
F^\sigma=h+J[P^\alpha+P^\beta]-K[P^\sigma],\quad F^\sigma C^\sigma=SC^\sigma\varepsilon^\sigma
$$

$$
\langle S^2\rangle_{1\alpha,1\beta}=1-|c_\alpha^\dagger S c_\beta|^2
$$

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs),\quad E_{\rm tot}=E_{\rm el}+E_{NN}
$$

### 比較・検証

保存PySCF RHF2値、独立g/u変分多項式・FCI閉形式・fermion組立と照合します。

### 確認の限界

UHFはスピン混入を持ちます。2幾何だけで完全な解離曲線や連続空間の厳密解を保証しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "98 R1.4 saved PySCF RHF": 1.7319479184152442e-14,
    "98 R1.4 UHF analytic paired ansatz": 1.3322676295501878e-15,
    "98 R1.4 finite-basis FCI analytic": 4.440892098500626e-16,
    "98 R1.4 independent fermion assembly": 1.1102230246251565e-16,
    "98 R1.4 FCI residual": 1.510066572755813e-15,
    "98 R1.4 UHF <= RHF": 0.0,
    "98 R1.4 FCI <= UHF": -0.02056161860694994,
    "98 R1.4 RHF electron count": 1.3322676295501878e-15,
    "98 R1.4 RHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 RHF SCF residual": 4.739336526991705e-16,
    "98 R1.4 UHF electron count": 1.3322676295501878e-15,
    "98 R1.4 UHF orbital norm": 9.992007221626409e-16,
    "98 R1.4 UHF SCF residual": 3.031599154361081e-11,
    "98 R3.0 saved PySCF RHF": 8.659739592076221e-15,
    "98 R3.0 UHF analytic paired ansatz": 0.0,
    "98 R3.0 finite-basis FCI analytic": 6.661338147750939e-16,
    "98 R3.0 independent fermion assembly": 1.1102230246251565e-16,
    "98 R3.0 FCI residual": 6.798699777552591e-16,
    "98 R3.0 UHF <= RHF": -0.06574294870227004,
    "98 R3.0 FCI <= UHF": -0.03413887592482623,
    "98 R3.0 RHF electron count": 8.881784197001252e-16,
    "98 R3.0 RHF orbital norm": 6.661338147750939e-16,
    "98 R3.0 RHF SCF residual": 1.0881821476711805e-16,
    "98 R3.0 UHF electron count": 4.440892098500626e-16,
    "98 R3.0 UHF orbital norm": 7.771561172376096e-16,
    "98 R3.0 UHF SCF residual": 1.610351596292876e-11,
    "98 stretched UHF energy lowering": 0.06574294870227004,
    "98 stretched UHF spin contamination": 0.7742403321308335
  },
  "checks": {
    "98 R1.4 saved PySCF RHF": true,
    "98 R1.4 UHF analytic paired ansatz": true,
    "98 R1.4 finite-basis FCI analytic": true,
    "98 R1.4 independent fermion assembly": true,
    "98 R1.4 FCI residual": true,
    "98 R1.4 UHF <= RHF": true,
    "98 R1.4 FCI <= UHF": true,
    "98 R1.4 RHF electron count": true,
    "98 R1.4 RHF orbital norm": true,
    "98 R1.4 RHF SCF residual": true,
    "98 R1.4 UHF electron count": true,
    "98 R1.4 UHF orbital norm": true,
    "98 R1.4 UHF SCF residual": true,
    "98 R3.0 saved PySCF RHF": true,
    "98 R3.0 UHF analytic paired ansatz": true,
    "98 R3.0 finite-basis FCI analytic": true,
    "98 R3.0 independent fermion assembly": true,
    "98 R3.0 FCI residual": true,
    "98 R3.0 UHF <= RHF": true,
    "98 R3.0 FCI <= UHF": true,
    "98 R3.0 RHF electron count": true,
    "98 R3.0 RHF orbital norm": true,
    "98 R3.0 RHF SCF residual": true,
    "98 R3.0 UHF electron count": true,
    "98 R3.0 UHF orbital norm": true,
    "98 R3.0 UHF SCF residual": true,
    "98 stretched UHF energy lowering": true,
    "98 stretched UHF spin contamination": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/h2-rhf-uhf-fci/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
公式CI文書の導入とFCIのスピン区分・行列式の例を選択閲読。章全体や実装全体の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 3中心H3+の小RHF/MP2/FCI模型

固定三角形H3+の3中心小分子で、RHF/MP2/有限基底FCIを示します。

**使用手法**

- [Hartree–Fock法](https://hrkoyama.github.io/numerical-methods-atlas/methods/hartree-fock/?lang=ja) (`hartree-fock`)
- [MP2摂動論](https://hrkoyama.github.io/numerical-methods-atlas/methods/mp2/?lang=ja) (`mp2`)
- [配置間相互作用（CI）](https://hrkoyama.github.io/numerical-methods-atlas/methods/configuration-interaction/?lang=ja) (`configuration-interaction`)
- [自己無撞着場反復（SCF）](https://hrkoyama.github.io/numerical-methods-atlas/methods/scf/?lang=ja) (`scf`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-algorithm)

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

- [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja) (`stationary-schrodinger`)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

- [閉殻Hartree–Fock方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#hartree-fock-model-ja) (`hartree-fock-model`)

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。


**問題の図**

![3中心H3+の小RHF/MP2/FCI模型：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/h3plus-mp2-fci.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja) (`h3plus-minimal`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/h3plus-minimal/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/?lang=ja#h3plus-mp2-fci-ja-validation)

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

- [3中心H3+の小RHF/MP2/FCI模型](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-h3plus-mp2-fci-ja) (`h3plus-mp2-fci`; 同じ問題の参照 · 有限格子の数値参照)

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。
### 前提・単位・境界

H核3個、電荷+1、2電子、3縮約s軌道の非対称三角形1個です。 H3+の固定3中心[(0,0,0),(1.5,0,0),(.5,1.5,0)]bohr、電荷+1、2電子/3s軌道。エネルギーhartree。

**編集上の補足**

独立な演算子組立と2電子RS2恒等式で固定小模型を照合します。新しい外部PySCF参照はありません。一般分子DFT、CC、多参照法、精密エネルギー・最適化・化学精度は未実装/未検証。MP2は変分上界ではありません。

### 採用した計算法

正準RHFから2電子MP2と9x9 FCIを求め、保存軌道から密度の2D断面を描画します。

$$
H_{pq,rs}=h_{pr}\delta_{qs}+h_{qs}\delta_{pr}+(pr|qs)
$$

$$
E_{\rm MP2}=E_{\rm RHF}+\sum_{a,b\in\mathrm{virt}}\frac{(0a|0b)^2}{2\varepsilon_0-\varepsilon_a-\varepsilon_b},\quad E_{\rm FCI}=\lambda_{\min}(H)+E_{NN}
$$

### 比較・検証

独立fermion組立、MP2行列要素の摂動式、電子数・SCF残差・FCI変分性を確認します。

### 確認の限界

一般分子DFT・CC・一般多参照法は未実装です。MP2は変分的でなく、外部独立エンジンの新参照値も生成しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "99 operator assembly": 4.440892098500626e-16,
    "99 FCI residual": 2.0196960871277348e-16,
    "99 singlet spatial symmetry": 1.821725679363684e-16,
    "99 MP2 determinant perturbation oracle": 0.0,
    "99 MP2 minimum denominator": 2.27228160503523,
    "99 FCI <= RHF": -0.02394188636845218,
    "99 RHF electron count": 0.0,
    "99 RHF SCF residual": 4.7552933164260536e-12
  },
  "checks": {
    "99 operator assembly": true,
    "99 FCI residual": true,
    "99 singlet spatial symmetry": true,
    "99 MP2 determinant perturbation oracle": true,
    "99 MP2 minimum denominator": true,
    "99 FCI <= RHF": true,
    "99 RHF electron count": true,
    "99 RHF SCF residual": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/h3plus-mp2-fci/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。

- PySCF Second-order Moller-Plesset perturbation theory [accessed 2026-11-25]. https://pyscf.org/user/mp.html; review_level=selected-official-documentation
公式MP2文書の導入、全/相関エネルギーとスピンの規約を選択閲読。新しい外部エンジン参照は生成しません。

- PySCF official mp2 module source [accessed 2026-11-25]. https://pyscf.org/_modules/pyscf/mp/mp2.html; review_level=selected-official-documentation
公式mp2ソースのkernel53–87行とenergy167–178行で分母・直接/交換項を確認。規約の参照でありコードのコピーや新PySCF参照生成ではありません。

- PySCF Configuration interaction (CISD and FCI) [accessed 2026-11-25]. https://pyscf.org/user/ci.html; review_level=selected-official-documentation
公式CI文書の導入とFCIのスピン区分・行列式の例を選択閲読。章全体や実装全体の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 保存周期Heエネルギー・力の参照台帳

既存周期Heのエネルギーと6座標力を、保存参照と元の受入基準へ対応付けます。

**使用手法**

- [Kohn–Sham密度汎関数法](https://hrkoyama.github.io/numerical-methods-atlas/methods/kohn-sham-dft/?lang=ja) (`kohn-sham-dft`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-algorithm)

保存エネルギー差分・解析力・Gaussian/PW比較の算術を再照合します。

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

- [局所Kohn–Sham DFT](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#kohn-sham-model-ja) (`kohn-sham-model`)

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。


**問題の図**

![保存周期Heエネルギー・力の参照台帳：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-he-reference-cards.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[周期He₂の原子間力：解析力・有限差分・BOMD接続](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja) (`periodic-he-forces`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/periodic-he-forces/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/?lang=ja#periodic-he-reference-cards-ja-validation)

元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。

- [保存周期Heエネルギー・力の参照台帳](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-he-reference-cards-ja) (`periodic-he-reference-cards`; 同じ問題の参照 · 有限格子の数値参照)

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。
### 前提・単位・境界

人工2He・4電子・5bohrセル、局所のみのGTH、固定LDA_X+VWNとコード版です。 人工He2、4電子、5bohrセル。保存した幾何・局所GTH版・LDA_X+VWN/Libxc・PySCF/DFTK版をsaved-data/periodic-he-reference.jsonに固定。エネルギーhartree、力hartree/bohr。

**編集上の補足**

既存の6力成分・エネルギー差分・Gaussian/PW比較の保存値照合です。電子計算の追加0回。新しい基底/k/カットオフ走査、一般物質、金属、長時間MDへ拡張しません。

### 採用した計算法

保存エネルギー差分・解析力・Gaussian/PW比較の算術を再照合します。

$$
F_{A\alpha}=-\frac{\partial E}{\partial R_{A\alpha}},\quad F^{\rm FD}_{A\alpha}=-\frac{E(R_{A\alpha}+\delta)-E(R_{A\alpha}-\delta)}{2\delta}
$$

### 比較・検証

元の数値・基準・履歴を保持し、単位・電子数・幾何・共有Libxcの独立性限界を明記します。

### 確認の限界

新電子計算や基底・k点・cutoff走査は0回です。局所Heの成功を非局所擬ポテンシャルへ拡張しません。

### 保存実測値と判定

```json
{
  "metrics": {
    "100 saved FD arithmetic 0": 0.0,
    "100 unchanged FD science bound 0": 8.486369273974503e-09,
    "100 saved FD arithmetic 1": 0.0,
    "100 unchanged FD science bound 1": 1.4108486323660685e-08,
    "100 saved FD arithmetic 2": 0.0,
    "100 unchanged FD science bound 2": 2.1580722472935854e-08,
    "100 saved FD arithmetic 3": 0.0,
    "100 unchanged FD science bound 3": 1.1233197302895626e-08,
    "100 saved FD arithmetic 4": 0.0,
    "100 unchanged FD science bound 4": 1.818304432021911e-08,
    "100 saved FD arithmetic 5": 0.0,
    "100 unchanged FD science bound 5": 2.3223412720652092e-08,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": 7.28156560618684e-05,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": 7.395629375217538e-05,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": 7.538249895754426e-05,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": 0.00017168416810697806
  },
  "checks": {
    "100 saved FD arithmetic 0": true,
    "100 unchanged FD science bound 0": true,
    "100 saved FD arithmetic 1": true,
    "100 unchanged FD science bound 1": true,
    "100 saved FD arithmetic 2": true,
    "100 unchanged FD science bound 2": true,
    "100 saved FD arithmetic 3": true,
    "100 unchanged FD science bound 3": true,
    "100 saved FD arithmetic 4": true,
    "100 unchanged FD science bound 4": true,
    "100 saved FD arithmetic 5": true,
    "100 unchanged FD science bound 5": true,
    "100 unchanged Gaussian/PW force basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-gth-qzv3p": true,
    "100 unchanged Gaussian/PW force basis-k2-gth-qzv3p": true,
    "100 unchanged Gaussian/PW energy basis-k2-gth-qzv3p": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-he-reference-cards/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
公式文書の分離形・ノルム保存・GTH形式と近似の導入。自作rank-one核を元素適合のノルム保存ポテンシャルと呼びません。

- PySCF Self-consistent field methods [accessed 2026-11-25]. https://pyscf.org/user/scf.html; review_level=selected-official-documentation
公式文書のFC=SCε、平均場・行列式、RHF/UHF、定常性と安定性、重なりの直交化を選択閲読。PySCF実行は行いません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

## 3平面波の非局所projectorと有限温度占有

3平面波の小周期模型で、非局所projectorと有限温度占有・力を示します。

**使用手法**

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) (`schrodinger`)
- [擬ポテンシャル・PAW](https://hrkoyama.github.io/numerical-methods-atlas/methods/pseudopotentials/?lang=ja) (`pseudopotentials`)

**方程式**

[この実行例の式と条件](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-algorithm)

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

- [3平面波・非局所核と平均Fermi占有](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#finite-projector-fermi-model-ja) (`finite-projector-fermi-model`)

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。


**問題の図**

![3平面波の非局所projectorと有限温度占有：この実行例の保存済み検証図。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/periodic-projector-occupations.png)

この実行例で保存した検証図です。図の条件と判定範囲は、このページの検証資料で確認できます。

[3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja) (`finite-projector-fermi`)

[この問題のコード・検証状況](https://hrkoyama.github.io/numerical-methods-atlas/problems/finite-projector-fermi/?lang=ja#code-ja)

**厳密解・参照解**

[この実行例の参照・検証](https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/?lang=ja#periodic-projector-occupations-ja-validation)

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

- [3平面波の非局所projectorと有限温度占有](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-periodic-projector-occupations-ja) (`periodic-projector-occupations`; 同じ問題の参照 · 半解析参照)

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。
### 前提・単位・境界

G=-1,0,1、k=±0.25、等重み、T=.05、電子数1.5の自作線形模型です。 無次元のG=-1,0,1、p=G+k、k=±.25、重み各.5、T=.05、平均電子数N=1.5、スピン係数2。実在格子定数や金属へ換算しません。

**編集上の補足**

自作3平面波の線形Hamiltonianです。平均占有の独立粒子Fermi模型であり、整数粒子の正準多体系ではありません。自己無撞着Hartree/XC、元素適合ノルム保存擬ポテンシャル、実金属、一般材料、長時間MDは未検証。

### 採用した計算法

rank1核のHermitian行列を解き、固定NのFermi占有と自由エネルギーの力を計算します。

$$
H_{GG\prime}(k,R)=\tfrac12(G+k)^2\delta_{GG\prime}+V_{GG\prime}+\eta\beta_G\beta_{G\prime}^*,\quad\beta_G=e^{-(G+k)^2/(2\sigma^2)}e^{-i(G+k)R}
$$

$$
f_{kn}=\frac{2}{1+e^{(\varepsilon_{kn}-\mu)/T}},\quad\sum_{kn}w_kf_{kn}=1.5
$$

$$
F=\sum_{kn}w_kf_{kn}\varepsilon_{kn}-TS,\quad F_R=-\sum_{kn}w_kf_{kn}\langle u_{kn}|\partial_RH_k|u_{kn}\rangle
$$

### 比較・検証

独立3次式固有値、Hermiticity・電子数・entropy・解析力と自由エネルギー差分を照合します。

### 確認の限界

元素に合わせたノルム保存擬ポテンシャルではありません。実金属、自己無撞着Hartree/XC、一般材料や長時間MDは未検証です。

### 保存実測値と判定

```json
{
  "metrics": {
    "101 Hermiticity 0": 3.58464566598299e-18,
    "101 residual 0": 2.751670084160633e-16,
    "101 independent cubic 0": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 0": 0.0,
    "101 Hermiticity 1": 3.58464566598299e-18,
    "101 residual 1": 2.7503882064100795e-16,
    "101 independent cubic 1": 2.7755575615628914e-16,
    "101 fixed-case cubic clamp activation 1": 0.0,
    "101 fixed electron number": 6.661338147750939e-16,
    "101 lower occupation": 4.6784131873466673e-05,
    "101 upper occupation": 1.4444120001743874,
    "101 nonnegative entropy": 1.4360712457901055,
    "101 finest free-energy force difference": 1.721169318180671e-10
  },
  "checks": {
    "101 Hermiticity 0": true,
    "101 residual 0": true,
    "101 independent cubic 0": true,
    "101 fixed-case cubic clamp activation 0": true,
    "101 Hermiticity 1": true,
    "101 residual 1": true,
    "101 independent cubic 1": true,
    "101 fixed-case cubic clamp activation 1": true,
    "101 fixed electron number": true,
    "101 lower occupation": true,
    "101 upper occupation": true,
    "101 nonnegative entropy": true,
    "101 finest free-energy force difference": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/periodic-projector-occupations/index.json

### 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。同梱のresults/は保存見本です。追試は新規output/へ出力し、繰り返す場合は別の新規フォルダを指定します。

### 出典と確認範囲

- DFTK periodic problems and plane-wave discretisations [accessed 2026-11-25]. https://docs.dftk.org/stable/guide/periodic_problems/; review_level=selected-official-documentation
公式周期問題ガイドのBloch・周期演算子・平面波の選択箇所。物質の数値計算は再現していません。

- DFTK Pseudopotentials [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/pseudopotentials/; review_level=selected-official-documentation
公式文書の分離形・ノルム保存・GTH形式と近似の導入。自作rank-one核を元素適合のノルム保存ポテンシャルと呼びません。

- DFTK Temperature and metallic systems [accessed 2026-11-25]. https://docs.dftk.org/stable/examples/metallic_systems/; review_level=selected-official-documentation
公式金属例のFermi温度・部分占有・Entropy項・高速例の未収束警告のみ。Mg計算や新k/基底/カットオフ走査は行いません。

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
NumPy2.0公式の引数、昇順固有値、規格化した固有ベクトル、Hermitian三角格納、LinAlgError、LAPACKの説明を選択閲読。全LAPACK実装・誤差証明の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
