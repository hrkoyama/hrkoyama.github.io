# 1次元箱型井戸・量子調和振動子 / Small 1D box and quantum harmonic-oscillator eigenpairs

https://hrkoyama.github.io/numerical-methods-atlas/problems/quantum-box-ho/

## 日本語

[1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。 8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

[解説](https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-quantum-small/#quantum-box-ho) · [条件・根拠](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=ja#quantum-box-ho)

### 方程式・問題の定義

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

#### [電子の定常Schrödinger方程式](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#stationary-schrodinger-ja)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

固定核・非相対論の電子固有値問題。核間反発は電子Hamiltonianの外に加える。従来の水素型動径例を保持し、追加は1次元の箱/HOと3AO以下の2電子FCIに限定する。一般多電子系の直接解法や連続空間の厳密分子解の検証ではない。

#### 1次元箱型井戸・量子調和振動子

補助実行例 · 実行例の定義・検証式

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。

### 厳密解・参照解

Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。

#### [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja#quantum-box-ho-ja-measurements)

解析解 · 同じ問題の参照

H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2;\quad E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M;\quad E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

8回の全固有対計算で824組をraw保存、規格化等の資格判定は選択24組です。節の閾値と位相は診断、HO0.003は固定例の達成目標で証明済み上界ではありません。有限壁と格子感度を相殺から独立に保証しません。

#### 1次元箱型井戸・量子調和振動子

Decimal箱スペクトル、連続解、native規格化・直交性・残差・parityを照合します。

- [保存結果](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[参照・検証条件の詳細](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja)

### 計算法

NumPyで8回全対角化し、native824固有対を保存して低24対を表示します。

- [Schrödinger固有値問題](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=ja) — この問題の実行例で使用; 手法台帳の状態：教育用例・関連コードあり

### コード・実行

#### [1次元箱型井戸・量子調和振動子](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=ja)

補助実行例

1次元の箱と量子調和振動子で、低3固有対と有限領域・格子の影響を比較します。

原子単位、ゼロDirichlet端点、一様内点格子。箱[0,1]とHO[-L,L]です。 1次元模型の原子単位でℏ=m=1、HOはω=1。箱[0,1]とHOの有限区間[-L,L]はいずれも同次Dirichlet。

[コード / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [検証記録](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[固定入力](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[配布ファイルとハッシュ](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

ZIPを展開し、実行案内の作業フォルダで実行します。配布版の複数例をまとめて実行する場合があります。

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

HOの壁誤差と格子誤差の個別保証はありません。節の近零点・tailは診断、0.003は精度目標です。

同じ配布版で共有するソースとテストを含みます。すべてがこの問題専用とは限りません。

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)

## English

[Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity. Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/quantum-box-ho.png)

[Reading](https://hrkoyama.github.io/numerical-methods-atlas/en/read/validation-quantum-small/#quantum-box-ho) · [Conditions and evidence](https://hrkoyama.github.io/numerical-methods-atlas/test-cases/?lang=en#quantum-box-ho-en)

### Equations and problem definitions

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

#### [Stationary electronic Schrödinger equation](https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=en#stationary-schrodinger-en)

$$
\hat H_{\rm el}\Psi=E_{\rm el}\Psi,\qquad E_{\rm tot}=E_{\rm el}+\sum_{A<B}\frac{Z_AZ_B}{R_{AB}}
$$

Fixed-nuclei nonrelativistic electronic eigenproblems; add nuclear repulsion separately. Preserve the existing hydrogenic radial examples. Additional examples are restricted to one-dimensional box/HO and two-electron FCI in at most3AOs, not general many-electron direct solvers or continuum-exact molecules.

#### Small 1D box and quantum harmonic-oscillator eigenpairs

Supplementary execution example · Example definition or validation formula

$$
H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2
$$

$$
E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M
$$

$$
E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h
$$

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

### Exact and reference solutions

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

#### [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en#quantum-box-ho-en-measurements)

Analytic reference · Reference for the same problem

H_h=-\frac12D_{xx}+V,\quad V_{\rm box}=0,\quad V_{\rm HO}=x^2/2;\quad E_j^{\rm box}=\frac{(j\pi)^2}{2},\quad u_j=\sqrt2\sin(j\pi x),\quad\lambda_{h,j}=2h^{-2}\sin^2\left(\frac{j\pi}{2M}\right),\ h=1/M;\quad E_n^{\rm HO}=n+\frac12,\quad u_n(x)=\frac{H_n(x)e^{-x^2/2}}{\pi^{1/4}\sqrt{2^nn!}},\quad u_h=v_h/\sqrt h

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

Eight full solves save824raw pairs; qualification applies to24selected pairs. Thresholded nodes/phase are diagnostics. HO0.003 is a met fixed-case goal, not a proved bound; finite-wall/mesh sensitivities do not certify separate errors.

#### Small 1D box and quantum harmonic-oscillator eigenpairs

Compare a stable Decimal box spectrum, continuum profiles, native normalization, orthogonality, residuals and reflection parity; report nodes and tail signs separately.

- [Saved result](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/results/result.json)

[Reference and validation details](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en)

### Numerical methods

Use centered differences and eight full NumPy eigensolves, saving824 native pairs before selecting24 low pairs.

- [Schrodinger eigenproblems](https://hrkoyama.github.io/numerical-methods-atlas/methods/schrodinger/?lang=en) — Used by this problem’s execution examples; Method-registry status: Educational example / related code

### Code and execution

#### [Small 1D box and quantum harmonic-oscillator eigenpairs](https://hrkoyama.github.io/numerical-methods-atlas/validation/quantum-box-ho/?lang=en)

Supplementary execution example

Compare low stationary eigenpairs of a1D box and harmonic oscillator, with finite-domain and mesh sensitivity.

Finite Dirichlet boxes and central differences; whole-line HO formulas do not isolate finite-wall error. Node counts diagnostic until forward sign qualification. Atomic model units hbar=m=1 and HO omega=1. The box[0,1] and finite HO[-L,L] domains both use homogeneous Dirichlet conditions.

[Code / ZIP](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/atlas-quantum-small-2026-11-25.zip) · [Verification receipt](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/verification.json)

[Fixed input](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/inputs.json)

[File manifest and hashes](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/source-manifest.json)

After extracting the ZIP, run these in the working directory specified by the guide. A command may execute several package cases.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

No separate certified finite-wall/mesh decomposition for HO; raw nodal count is a diagnostic. HO0.003 is the fixed-input study target, not a proved finite-h bound.

These source and test lists include files shared across the package; they are not all dedicated to this problem.

- [/code/validated-examples/2026-11-25/quantum-small/run.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/run.py)
- [/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/eigenpairs.py)
- [/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py](https://hrkoyama.github.io/code/validated-examples/2026-11-25/quantum-small/test_quantum_small.py)
