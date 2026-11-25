# ALEピストン・球面輸送・SPH/GSPHの限定検証

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-continuum-particle-controls/

この章に登録された手法・問題・実行例の関連資料です。 4拡張候補に対応する5ケース。元論文の全設定や一般的な精度の検証には広げません。

## 手法

- [セミラグランジュ法：所与球面回転の限定例](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja>)
- [ALE一様状態・幾何保存モデル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja>)

  Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)

  Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
- [セミラグランジュ法：所与球面回転の限定例](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja>)

  単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)

  a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)

  a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [Godunov SPH／GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja>)

  GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
- [SPHカーネル再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja>)

  GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
- [ALE一様状態・幾何保存モデル](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ale/?lang=ja>)
- [Rusanov／局所Lax–Friedrichs流束](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rusanov/?lang=ja>)
- [空間中心差分](<https://hrkoyama.github.io/numerical-methods-atlas/methods/centered-difference/?lang=ja>)
- [古典的RK4](<https://hrkoyama.github.io/numerical-methods-atlas/methods/rk4/?lang=ja>)
- [Godunov SPH／GSPH](<https://hrkoyama.github.io/numerical-methods-atlas/methods/gsph/?lang=ja>)
- [SPHカーネル再構成](<https://hrkoyama.github.io/numerical-methods-atlas/methods/sph/?lang=ja>)

## 方程式

- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [球面上の所与速度スカラー移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja>)

  単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [球面浅水波の軸対称部分問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#spherical-shallow-water-ja>)

  a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。 この問題に関連する代表式です。初期条件・境界条件・パラメータは「図と問題の条件・根拠」と各実行例で確認できます。
- [球面上の所与速度スカラー移流](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#sphere-scalar-advection-ja>)

  単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
- [球面浅水波の軸対称部分問題](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#spherical-shallow-water-ja>)

  a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-algorithm>)

  固定入力・宣言したアルゴリズム・補正しない停止条件を用います。
- [圧縮性Euler方程式](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#euler-ja>)

  1次元の保存形。状態方程式と初期・境界条件は各テストの定義を参照する。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-algorithm>)

  固定入力・宣言したアルゴリズム・補正しない停止条件を用います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-algorithm>)

  固定入力・宣言したアルゴリズム・補正しない停止条件を用います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-algorithm>)

  固定入力・宣言したアルゴリズム・補正しない停止条件を用います。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-algorithm>)

  固定入力・宣言したアルゴリズム・補正しない停止条件を用います。

## 問題の図

- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png
- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/saltzman-ale-piston.png
- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/williamson-sphere-transport.png
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sphere-zonal-balance.png
- [Gaussian畳込みGSPHによるSod型粒子衝撃管](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/gsph-sod.png
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-25/continuum-particle-controls/results/sph-pressure-acoustics.png
- [Sod衝撃波管](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja>)

  4拡張候補に対応する5ケース。元論文の全設定や一般的な精度の検証には広げません。 テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/numerical-methods-atlas/gallery/previews/sod.png

## 厳密解・参照解

- [Saltzman型の歪み格子ピストン：2次元EulerとALE：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/saltzman-ale-piston/?lang=ja#references-ja>)

  固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 Tan–Lv–Zhu（2023）Example 8に対応するe0=10⁻⁴・有限初期圧力の変種です。規定したアフィンALE、2次元Euler、Rusanovを用います。同論文の物質Lagrange格子・WENO/remap法や、未読の1985年原報全体の再現ではありません。 固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
- [Williamson型の球面固体回転輸送：傾いた軸と極通過：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/williamson-sphere-transport/?lang=ja#references-ja>)

  固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 単位球上の規定スカラー剛体回転に限定します。W92原著の式は未読で、Nair著者資料の選択式から規約を照合。両格子で整合しない位相の11回再配置を用います。双線形補間は非保存なので質量変動を報告し、時間収束や非線形の全球浅水コアは主張しません。 固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
- [球面浅水波の軸対称定常釣合いを時間積分：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sphere-zonal-balance/?lang=ja#references-ja>)

  固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 a=g=1、Ω=2、u0=0.5、h0=10の無次元軸対称部分問題です。中心差分のprimitive運動量、有限体積の質量、RK4で実際に時間発展させます。標準地球パラメータ、多次元の全球浅水コア、離散厳密釣合い、渦位保存の主張は含みません。 固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sph-pressure-acoustics/?lang=ja#references-ja>)

  固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 t=0.2、位置を揺らした128粒子のGSPHです。初期kernel再構成誤差は0.011834に達し、音波振幅0.001を上回って左の密度波形に残ります。右図はその初期誤差です。合格条件は基本Fourierモードの位相・振幅と固定した保存検査であり、各点の高精度や一般的な優位性ではありません。 固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja>)
  reference_kind: analytic

  解析解 Tan–Lv–Zhu（2023）Example 8に対応するe0=10⁻⁴・有限初期圧力の変種です。規定したアフィンALE、2次元Euler、Rusanovを用います。同論文の物質Lagrange格子・WENO/remap法や、未読の1985年原報全体の再現ではありません。
- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja>)
  reference_kind: analytic

  解析解 単位球上の規定スカラー剛体回転に限定します。W92原著の式は未読で、Nair著者資料の選択式から規約を照合。両格子で整合しない位相の11回再配置を用います。双線形補間は非保存なので質量変動を報告し、時間収束や非線形の全球浅水コアは主張しません。
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja>)
  reference_kind: analytic

  解析解 a=g=1、Ω=2、u0=0.5、h0=10の無次元軸対称部分問題です。中心差分のprimitive運動量、有限体積の質量、RK4で実際に時間発展させます。標準地球パラメータ、多次元の全球浅水コア、離散厳密釣合い、渦位保存の主張は含みません。
- [Gaussian畳込みGSPHによるSod型粒子衝撃管](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja>)
  reference_kind: semi-analytic

  半解析解 Gaussianの線形比体積GSPH重なり積分、対称な可変h、独立な対Riemann解、反対称な全エネルギー交換を実装します。通常SPHへの星状態圧力の代入とは区別。再構築は1次に限定し、原著の3次/MUSCL実装や一般的な高精度は主張しません。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja>)
  reference_kind: analytic

  解析解 t=0.2、位置を揺らした128粒子のGSPHです。初期kernel再構成誤差は0.011834に達し、音波振幅0.001を上回って左の密度波形に残ります。右図はその初期誤差です。合格条件は基本Fourierモードの位相・振幅と固定した保存検査であり、各点の高精度や一般的な優位性ではありません。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja#saltzman-ale-piston-ja-validation>)

  解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-saltzman-ale-piston-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 Tan–Lv–Zhu（2023）Example 8に対応するe0=10⁻⁴・有限初期圧力の変種です。規定したアフィンALE、2次元Euler、Rusanovを用います。同論文の物質Lagrange格子・WENO/remap法や、未読の1985年原報全体の再現ではありません。 固定入力の式・参照・図と実行コードを対応付けます。 Tan–Lv–Zhu (2023) Example 8 の e0=10^-4 を明示した有限圧力版。所与のアフィンALE格子を使う2D Euler/Rusanov例で、物質追従格子、WENO、remapや1985原報の全面再現ではありません。
- [Williamson型の球面固体回転輸送：傾いた軸と極通過：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja#williamson-sphere-transport-ja-validation>)

  解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。
- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-williamson-sphere-transport-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 単位球上の規定スカラー剛体回転に限定します。W92原著の式は未読で、Nair著者資料の選択式から規約を照合。両格子で整合しない位相の11回再配置を用います。双線形補間は非保存なので質量変動を報告し、時間収束や非線形の全球浅水コアは主張しません。 固定入力の式・参照・図と実行コードを対応付けます。 単位球の所与の剛体回転によるスカラー輸送だけです。原W92全文の式は未閲読で、Nairらの選択した著者資料との規約照合に限ります。両格子とも11回の非整合なremap。非保存の双線形補間で質量ずれを報告し、時間収束とは呼びません。
- [球面浅水波の軸対称定常釣合いを時間積分：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja#sphere-zonal-balance-ja-validation>)

  解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sphere-zonal-balance-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 a=g=1、Ω=2、u0=0.5、h0=10の無次元軸対称部分問題です。中心差分のprimitive運動量、有限体積の質量、RK4で実際に時間発展させます。標準地球パラメータ、多次元の全球浅水コア、離散厳密釣合い、渦位保存の主張は含みません。 固定入力の式・参照・図と実行コードを対応付けます。 a=g=1, Ω=2, u0=.5, h0=10 の軸対称な無次元部分問題。運動量中心差分・質量FV・RK4の混成で実際に時間発展させます。標準地球条件や全球多次元SWE、厳密な離散釣合い・PV保存の再現ではありません。
- [Gaussian畳込みGSPHによるSod型粒子衝撃管：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja#gsph-sod-ja-validation>)

  解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。
- [Euler／Sod問題](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja>)
  relation: related-model
  reference_kind: semi-analytic

  半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。 γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
- [Gaussian畳込みGSPHによるSod型粒子衝撃管](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  半解析解 Gaussianの線形比体積GSPH重なり積分、対称な可変h、独立な対Riemann解、反対称な全エネルギー交換を実装します。通常SPHへの星状態圧力の代入とは区別。再構築は1次に限定し、原著の3次/MUSCL実装や一般的な高精度は主張しません。 固定入力の式・参照・図と実行コードを対応付けます。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja#sph-pressure-acoustics-ja-validation>)

  解析参照、保存量、細分化、独立成分検査と意図した誤式の負例を区別して保存します。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-sph-pressure-acoustics-ja>)
  relation: same-problem
  reference_kind: analytic

  解析解 t=0.2、位置を揺らした128粒子のGSPHです。初期kernel再構成誤差は0.011834に達し、音波振幅0.001を上回って左の密度波形に残ります。右図はその初期誤差です。合格条件は基本Fourierモードの位相・振幅と固定した保存検査であり、各点の高精度や一般的な優位性ではありません。 固定入力の式・参照・図と実行コードを対応付けます。 GSPH、摂動した128粒子、t=0.2。初期カーネル再構成誤差は最大0.011834で、音波振幅0.001より大きく、左の密度分布にその影響が残ります。右は初期誤差です。判定は基本Fourierモードの位相・振幅と保存量などの固定条件であり、点ごとの高精度や一般的な優位性を示しません。
- [Sod衝撃波管：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/sod/?lang=ja#references-ja>)

  4拡張候補に対応する5ケース。元論文の全設定や一般的な精度の検証には広げません。 理想気体γ=1.4の標準Sod初期値に対する半解析的Riemann解が基準です。同じ問題でも点値・保存変数のセル平均・格子と誤差ノルムは同一とは限りません。
- [Euler／Sod問題](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-euler-sod-ja>)
  relation: related-model
  reference_kind: semi-analytic

  4拡張候補に対応する5ケース。元論文の全設定や一般的な精度の検証には広げません。 半解析解 比熱比gamma>1の理想気体、平面1次元波。真空の保存変数はゼロ、速度は未定義です。 γ=1.4、左右(ρ,u,p)=(1,0,1)/(0.125,0,0.1)、x0=0.5、[0,1]、t=0.2が一致します。点値・保存セル平均・誤差ノルムは別に確認します。 物理的な入力は一致しますが、参照カードの点値標本と保存計算の有限体積セル平均・離散格子は別表現です。
- [Gaussian畳込みGSPHによるSod型粒子衝撃管](<https://hrkoyama.github.io/numerical-methods-atlas/solutions/?lang=ja#solution-gsph-sod-ja>)
  relation: same-problem
  reference_kind: semi-analytic

  4拡張候補に対応する5ケース。元論文の全設定や一般的な精度の検証には広げません。 半解析解 Gaussianの線形比体積GSPH重なり積分、対称な可変h、独立な対Riemann解、反対称な全エネルギー交換を実装します。通常SPHへの星状態圧力の代入とは区別。再構築は1次に限定し、原著の3次/MUSCL実装や一般的な高精度は主張しません。 固定入力の式・参照・図と実行コードを対応付けます。 Gaussianの線形比体積畳み込み、対称な可変h、独立な対Riemann解と反対称な全エネルギー交換を持つGSPHです。通常SPHへp*を代入する代用ではありません。一次再構成に限定し、論文のcubic/MUSCLや一般精度を主張しません。

## コード・検証

- [Williamson型の球面固体回転輸送：傾いた軸と極通過](<https://hrkoyama.github.io/numerical-methods-atlas/validation/williamson-sphere-transport/?lang=ja>)
  availability: run

  所与の固体回転速度で球面上のcosine bellを輸送し、傾いた軸・極通過・1周後の誤差を調べる限定例。
- [Saltzman型の歪み格子ピストン：2次元EulerとALE](<https://hrkoyama.github.io/numerical-methods-atlas/validation/saltzman-ale-piston/?lang=ja>)
  availability: run

  2023年版の歪み格子と有限初期圧力を明示した、所与の格子移動による2次元Eulerピストン計算。
- [球面浅水波の軸対称定常釣合いを時間積分](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sphere-zonal-balance/?lang=ja>)
  availability: run

  球面浅水波の軸対称な無次元定常状態を実際に時間積分し、釣合い残差と格子依存を分ける。
- [一様圧力と線形音波：SPH/GSPHの粒子配置依存](<https://hrkoyama.github.io/numerical-methods-atlas/validation/sph-pressure-acoustics/?lang=ja>)
  availability: run

  規則・摂動粒子の一様圧力と小振幅音波について、初期カーネル誤差と時間発展誤差を区別する。
- [Gaussian畳込みGSPHによるSod型粒子衝撃管](<https://hrkoyama.github.io/numerical-methods-atlas/validation/gsph-sod/?lang=ja>)
  availability: run

  Gaussian畳込みの線形比体積近似と対称な可変平滑化長を使う、限定GSPH粒子流体計算。
- [セミラグランジュ法：所与球面回転の限定例：コード・検証](<https://hrkoyama.github.io/numerical-methods-atlas/methods/semi-lagrangian/?lang=ja#method-execution-ja>)
  availability: source

  手法固有の配布版と関連ソースを案内します。固定入力例は別の項目で区別します。
