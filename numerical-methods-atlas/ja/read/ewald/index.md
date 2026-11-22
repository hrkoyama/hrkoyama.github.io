# Ewald法

Ewald法は、条件付き収束する周期Coulomb相互作用の和を、短距離の実空間和と滑らかな逆空間和に分ける方法です。有限半径で1/rを切ることとは、境界値問題が異なります。

## 対象と代表式

中性の3次元周期セルにある点電荷qᵢを考えます。rᵢⱼₙ=rᵢ−rⱼ+n、セル体積V、分割定数α>0、逆格子ベクトルk、S(k)=Σⱼqⱼexp(ik·rⱼ)とします。下式はCoulomb定数を1にしたエネルギーで、k=0を除き、巨視的境界を導体極限とした場合です。プライムはi=jかつn=0だけを除きます。

$$
\begin{aligned}S(\mathbf k)&=\sum_jq_j e^{i\mathbf k\cdot\mathbf r_j},\\E&=\frac12\sum_{i,j,\mathbf n}^{\prime}q_iq_j\frac{\operatorname{erfc}(\alpha r_{ij\mathbf n})}{r_{ij\mathbf n}}+\frac{2\pi}{V}\sum_{\mathbf k\ne0}\frac{e^{-k^2/(4\alpha^2)}}{k^2}|S(\mathbf k)|^2-\frac{\alpha}{\sqrt\pi}\sum_iq_i^2.\end{aligned}
$$

## 計算の流れ

erfcで減衰する実空間項を近接像まで、Gaussianで減衰する逆空間項を有限波数まで足し、自己エネルギーを引きます。実装単位系では全項に同じCoulomb係数を掛けます。αを変えると両和への仕事の配分が変わりますが、収束した総和は変わりません。力は同じエネルギー規約から微分します。

## 適用条件と落とし穴

正味電荷がある場合は、背景電荷など追加の規約なしにはこの式を使えません。平均電位のゲージ、表面項、自己像、分子内除外は別々に指定します。重力の周期Poisson問題は核・符号・平均密度の扱いが異なるため、そのまま置き換えません。

## 検証するときに見る量

小さい中性配置で実空間・逆空間の打切りを独立に伸ばし、α依存が消えることを確認します。エネルギーの位置差分と力、全体平行移動に対する不変性、総力を比較します。収束前の和同士の一致は独立検証ではありません。

## 公開範囲

既存の教育用コードと版を固定した検証記録への案内です。今回の本文・翻訳の追加でコードや過去の測定結果を変更せず、原論文全体の再現を主張しません。

## 文献

- Ewald, P. P. (1921). Die Berechnung optischer und elektrostatischer Gitterpotentiale. https://doi.org/10.1002/andp.19213690304
- Hockney, R. W. and Eastwood, J. W. (1981). Computer Simulation Using Particles. https://doi.org/10.1201/9780367806934
