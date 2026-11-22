# CTとGLM：同条件の独立照合・格子・時間収束

この章の関連資料

https://hrkoyama.github.io/numerical-methods-atlas/ja/read/validation-mhd-convergence/

この章に登録された手法・問題・実行例の関連資料です。

## 手法

- [制約輸送法／CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja>)

  この問題に明示的に対応するct-glm-smooth-convergence配布例のCTとGLMです。同じLLF係数と時間刻みを使っても、磁場配置・角電場平均・法線場の扱いが異なる離散系全体の比較です。この発散ゼロの物理例を、別の非物理制約対照で測った能動的なcleaning性能と同一視しません。
- [GLM発散クリーニング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja>)

  この問題に明示的に対応するct-glm-smooth-convergence配布例のCTとGLMです。同じLLF係数と時間刻みを使っても、磁場配置・角電場平均・法線場の扱いが異なる離散系全体の比較です。この発散ゼロの物理例を、別の非物理制約対照で測った能動的なcleaning性能と同一視しません。
- [制約輸送法／CT](<https://hrkoyama.github.io/numerical-methods-atlas/methods/ct/?lang=ja>)
- [GLM発散クリーニング](<https://hrkoyama.github.io/numerical-methods-atlas/methods/glm/?lang=ja>)

## 方程式

- [理想MHD](<https://hrkoyama.github.io/numerical-methods-atlas/equations/?lang=ja#mhd-ja>)

  透磁率を1とする理想MHDの代表形。Eは熱・運動・磁場を含む全エネルギー密度。解説でCT・GLMと発散の測り方、HLLDテストへ進めます。 周期単位正方形・γ=5/3・μ0=1の平面理想MHDを扱います。構成した磁気静力学平衡を一定速度で移流する厳密解で、外力による製造解や標準円偏光Alfvén波とは異なります。GLMの補助方程式と具体的な保存変数セル平均は、実行例の式・入力・コードを参照してください。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-algorithm>)

  両法とも区分定数・同じ固定Rusanov速度α=3・前進Eulerです。CTは面Bと共有算術corner EMF、GLMはcell B/ψとch=3・物理減衰率κ=2を使用。全格子で同じ384刻み、両法のdt列も同一です。CT面平均から復元した初期cell BとGLM初期Bが一致します。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-algorithm>)

  主計算は固定α=ch=3のRusanovと前進Euler、GLMκ=2は格子に依存しません。独立C++ Athena++はHLLD・PLM・RK2・upwind CTです。同じ連続初期値を用いますが、Athenaのface/primitive離散化は主計算と完全同一ではありません。
- [この実行例の式と条件](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-algorithm>)

  同じ完全結合MHDコードを使用。y不変・By=vy=0ではGLMのBx/ψ系が流体応答から独立するため、離散Fourier記号の2×2行列と前進Euler行列冪を別に構成します。κ=2とκ=0を同じdt・LLF粘性で比較し、Bxだけの減少を物理減衰と取り違えません。

## 問題の図

- [CT・GLM：移動する磁気静力学平衡の格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja>)

  テスト問題の代表図。条件と出典は問題別ページで確認できます。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png
- [CT・GLM：移動する磁気静力学平衡の格子・時間収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-smooth-convergence.png
- [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-ot-convergence.png
- [CTの初期制約保持とGLMの能動的cleaning：非物理診断対照](<https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png>)

  この実行例自身の保存済み検証図です。

  https://hrkoyama.github.io/code/validated-examples/2026-11-22/mhd-convergence/results/ct-glm-constraint-control.png

## 厳密解・参照解

- [CT・GLM：移動する磁気静力学平衡の格子・時間収束：参照・比較条件](<https://hrkoyama.github.io/numerical-methods-atlas/problems/advected-magnetostatic-equilibrium/?lang=ja#references-ja>)

  構成厳密解の保存変数セル平均と格子誤差を比較します。固定した空間RHSを独立DOP853時間積分で解いた参照は時間誤差の確認用であり、別の空間ソルバーとは呼びません。18件の既存参照解ライブラリにはこの構成解のカードがないため、別問題の参照カードを流用せず、該当実行例の式・結果・ソースへ案内します。
- [CT・GLM：移動する磁気静力学平衡の格子・時間収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja#ct-glm-smooth-convergence-ja-validation>)

  16²/32²/64²の保存変数L1/L2/L∞誤差と観測次数を測ります。最細格子の刻み倍増差を空間誤差の.1以下と比較。時間収束は固定8²で16/32/64/128刻みを、許容誤差・最大刻みを二重に細分したDOP853へ照合します。質量・E、正値性、native CT divと共通cell div、ψも記録します。
- [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja#ct-glm-ot-convergence-ja-validation>)

  密度・磁場L1誤差、格子改善、正値性、保存量とdiv/ψを測定。Athena256²/512²はともにCFL=.15、512²のCFL=.3/.15差で参照の時間感度を確認し、両増分が主計算誤差の.1以下か判定します。主計算の固定16²での時間収束を別実行DOP853へ照合し、最細格子の刻み倍増差も確認します。
- [CTの初期制約保持とGLMの能動的cleaning：非物理診断対照：参照・検証](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja#ct-glm-constraint-control-ja-validation>)

  CT native divの初期違反保持、GLMのψ励起、Bx/ψ双方の独立FE参照一致、密度・圧力正値性、物理的総E/質量保存を確認。補助波エネルギーW=〈Bx²+ψ²/ch²〉のκ2/κ0比を判定し、半離散行列指数と連続Fourier解も区別して表示します。

## コード・検証

- [CT・GLM：移動する磁気静力学平衡の格子・時間収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-smooth-convergence/?lang=ja>)
  availability: run

  非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。
- [Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-ot-convergence/?lang=ja>)
  availability: run

  同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。
- [CTの初期制約保持とGLMの能動的cleaning：非物理診断対照](<https://hrkoyama.github.io/numerical-methods-atlas/validation/ct-glm-constraint-control/?lang=ja>)
  availability: run

  故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。
