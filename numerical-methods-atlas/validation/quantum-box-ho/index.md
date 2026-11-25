# 1次元箱型井戸・量子調和振動子

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
## 前提・単位・境界

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

**編集上の補足**

8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。

## 採用した計算法

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

## 比較・検証

Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。

## 確認の限界

HOの壁誤差と格子誤差の個別保証はありません。節の近零点・tailは診断、0.003は精度目標です。

## 保存実測値と判定

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

## 取得・実行

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

## 出典と確認範囲

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
同一作業内の選択閲読：式7–8、13–15、24–35と近傍のHO/Coulomb・規格化・測度。章全体・出典書籍の通読ではありません。

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
NumPy2.0公式の引数、昇順固有値、規格化した固有ベクトル、Hermitian三角格納、LinAlgError、LAPACKの説明を選択閲読。全LAPACK実装・誤差証明の監査ではありません。


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Small 1D box and quantum harmonic-oscillator eigenpairs

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

**Methods used**

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) (`schrodinger`)

**Equations**

[This example’s formulation and conditions](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-algorithm)

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

- [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en) (`stationary-schrodinger`)

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.


**Problem figure**

![Small 1D box and quantum harmonic-oscillator eigenpairs: saved validation figure for this execution.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

A saved validation figure for this execution example. Its conditions and acceptance scope are documented by this page’s checks.

[Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en) (`quantum-box-ho`)

[This problem’s code and validation status](https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/?lang=en#code-en)

**Exact / reference solutions**

[References and checks for this execution](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-validation)

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

- [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=en#solution-quantum-box-ho-en) (`quantum-box-ho`; Same-problem reference · Analytic reference)

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.
## Assumptions, units and boundaries

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

**Editorial clarification**

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.

## Adopted numerical method

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

## References and validation

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

## Limits

No separate certified finite-wall/mesh decomposition for HO; raw nodal count is a diagnostic. HO0.003 is the fixed-input study target, not a proved finite-h bound.

## Stored measurements and decisions

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

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group. Bundled results/ are stored outputs. Rerun into a new output/ directory and use another fresh directory for subsequent runs.

## Sources and review scope

- NIST DLMF18.39 Applications in the Physical Sciences [accessed 2026-11-25]. https://dlmf.nist.gov/18.39; review_level=selected-official-documentation
Earlier same-session R3 selected E7–8,E13–15,E24–35; oscillator/Coulomb normalization and measure. Full chapter/books not audited.

- NumPy2.0 numpy.linalg.eigh [accessed 2026-11-25]. https://numpy.org/doc/2.0/reference/generated/numpy.linalg.eigh.html; review_level=selected-official-documentation
Signature, Hermitian lower-triangle handling, all ascending eigenvalues/normalized columns, LinAlgError and LAPACK syevd/heevd notes.


Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
