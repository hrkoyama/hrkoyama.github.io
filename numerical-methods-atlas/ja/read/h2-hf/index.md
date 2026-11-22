# H₂分子の閉殻HF：独立参照・SCF残差・基底の収束

固定した2つの陽子と2電子からなるH₂を、自作のs型Gaussian積分と閉殻Hartree–Fock（RHF）で解きます。エネルギーが変わらなくなること、離散SCF方程式を満たすこと、基底を広げたときの変化、物理近似の妥当性を別々に確かめます。

## 何を計算するか

核間距離Rを入力で固定するBorn–Oppenheimer電子問題です。原子単位系を用い、距離はbohr、エネルギーはhartreeで記録します。電子の相対論効果、核運動、振動・回転、溶媒、周期境界は含めません。核間反発1/Rを含む全エネルギーと、電子エネルギーを混同しないように出力を分けます。

2電子は同じ空間軌道を逆向きスピンで占有する閉殻RHFに制限します。結合を伸ばした点でも同じ制約を保った解を比較します。SCFが収束して別実装と一致しても、正しい解離極限や電子相関まで再現したことにはなりません。UHF、配置間相互作用、DFTへ切り替えた計算でもありません。

$$
\hat H_{\mathrm{el}}=\sum_{i=1}^{2}\left[-\tfrac12\nabla_i^2-\sum_{A=1}^{2}\frac{1}{|\mathbf r_i-\mathbf R_A|}\right]+\frac{1}{r_{12}},\qquad E_{\mathrm{tot}}=E_{\mathrm{el}}+\frac1R
$$

## Gaussian基底と自作の積分

各核を中心とする規格化されたs型Gaussianを基底にします。縮約関数では複数の指数と係数をまとめ、縮約後の規格化もそろえます。STO-3Gを使う場合の3つのprimitiveは、独立した3基底関数ではなく1つの縮約s関数を表すことに注意します。指数・係数・縮約の定義は入力と結果に残します。STO-3Gの数値はBasis Set Exchangeのversion 1と照合した規約を採用し、原論文の印刷値から直接転記したものとして扱いません。

重なりS、運動エネルギーT、電子–核引力V、電子間反発積分を教育用コードで計算し、1電子行列をh=T+Vと定義します。s型のCoulomb積分に現れるBoys関数F₀はt→0で1に近づきます。この付近を安定に扱わずerf(√t)/√tを直接評価すると0/0が生じます。JとKは化学者の積分添字規約とスピン和密度Pに対応させ、交換項の1/2をそろえます。

$$
g_{\alpha A}(\mathbf r)=\left(\frac{2\alpha}{\pi}\right)^{3/4}e^{-\alpha|\mathbf r-\mathbf R_A|^2},\quad \chi_\mu=\sum_p d_{\mu p}g_{\alpha_{\mu p}A_\mu},\quad F_0(t)=\int_0^1e^{-tu^2}\,du
$$

$$
P_{\mu\nu}=2\sum_{i\in\mathrm{occ}} C_{\mu i}C_{\nu i},\quad F_{\mu\nu}=h_{\mu\nu}+\sum_{\lambda\sigma}P_{\lambda\sigma}\left[(\mu\nu|\lambda\sigma)-\tfrac12(\mu\lambda|\nu\sigma)\right]
$$

## SCFの収束をどう判定するか

重なり行列を対称直交化してRoothaan方程式を解き、占有軌道から密度を作り、Fock行列を再構築して反復します。密度混合で反復を安定化できますが、混合途中の密度は一般に純粋な単一行列式の冪等条件を満たしません。最終的な密度・軌道・Fockを同じ状態で再評価して検査します。

小さなエネルギー差だけでは停止を正当化できません。エネルギー変化、AO密度差のFrobeniusノルム、直交座標系の交換子残差のFrobeniusノルムを入力のしきい値と比較し、軌道の直交性、電子数Tr(PS)=2、閉殻の冪等条件PSP=2Pも測定します。最終密度からF[P]を作り直して求める行列トレースのエネルギーと、占有軌道と電子反発積分から別の式で再構成したエネルギーを照合します。

最小重なり固有値と条件数も出力します。基底がほぼ線形従属になるとS⁻¹ᐟ²が誤差を増幅します。停止理由と反復上限を残し、上限到達を収束と表示しません。また、停留解は安定なエネルギー極小とは限らず、これらの残差検査は完全なRHF/UHF安定性解析の代用ではありません。

$$
FC=SC\varepsilon,\qquad C^{\mathsf T}SC=I,\qquad X=S^{-1/2},\qquad XFX\widetilde C=\widetilde C\varepsilon,\quad C=X\widetilde C
$$

$$
E_{\mathrm{tot}}[P]=\frac12\sum_{\mu\nu}P_{\mu\nu}\bigl(h_{\mu\nu}+F_{\mu\nu}[P]\bigr)+\frac1R
$$

$$
\mathcal R=X(FPS-SPF)X,\qquad \operatorname{Tr}(PS)=2,\qquad PSP=2P
$$

## 基底を広げる検査と、その限界

SCFの許容誤差は固定した基底内での解き残しです。基底の変更は離散問題自体の変更です。SCFの厳しい設定をそろえ、同じ幾何・核間反発・RHF制約で基底系列を比較します。入れ子の変分空間で真のRHF最小値を得ていれば、基底を広げても最小エネルギーは上がりません。ただし異なる局所停留枝へ移れば、この単純な比較は成立しません。

ここでの細分化は公開入力で定義した有限のs型基底系列に限定します。連続する基底のエネルギー差を測ることはできますが、p型以上の角運動量成分がなく、完全基底極限（CBS）への収束や化学精度を証明しません。異なる縮約や無関係な基底集合の全てを、入れ子の系列として扱うこともしません。末尾の2回の追加について、指定したエネルギー変化の公差を両方満たしたかを核間距離ごとに記録します。これは公開系列の停止目安であり、真の基底誤差の上限ではありません。

許容誤差走査ではSCFのしきい値だけを変更した結果を厳しい設定と比較します。基底走査ではSCF設定をそろえた結果を比較します。独立実装との差とこれらの差を別の量として出力し、最後の基底差が小さいという理由だけで物理近似の誤差をゼロにしません。

$$
V_n\subseteq V_{n+1}\ \Longrightarrow\ E_{n+1}^{\mathrm{RHF,min}}\le E_n^{\mathrm{RHF,min}},\qquad \Delta E_n=|E_{n+1}-E_n|
$$

$$
\underbrace{E_{n,\tau}-E_{n,\mathrm{tight}}}_{\text{SCF tolerance effect}},\qquad\underbrace{E_{n+1,\mathrm{tight}}-E_{n,\mathrm{tight}}}_{\text{basis-space change}},\qquad\underbrace{E_{n,\mathrm{tight}}-E_{n,\mathrm{PySCF}}}_{\text{independent-implementation difference}}
$$

## 独立参照と再現手順

参照スクリプトは同じ核配置・電荷・スピン・明示的なGaussian基底をPySCFへ渡し、独立した積分ライブラリとSCFでRHFエネルギーを求めます。教育用の積分・Fock・SCF関数を参照側から呼び出しません。両者が同じ物理モデルと有限基底を解く比較であり、厳密な相関電子エネルギーを参照する比較ではありません。

公開版は入力ハッシュ、参照ハッシュ、依存関係の版、全エネルギー、参照との差、反復履歴、終了理由を保存します。ZIPを別フォルダへ展開して同じ固定入力を実行し、JSONの合否だけでなく残差・誤差の値と許容条件を照合します。参照の再生成と、保存済み参照を使った通常の追試は別の操作です。

## 保存した実測値

- max_reference_energy_error: 2.53130849615e-14
- max_scf_commutator: 9.13387953717e-11
- max_orbital_residual: 5.00061911168e-11
- max_orthogonality_error: 3.697042672e-14
- max_electron_count_error: 3.10862446895e-15
- max_energy_consistency_error: 2.22044604925e-15
- max_idempotency_error: 1.77828610609e-15
- basis_energy_increase_max: 0
- last_basis_energy_change_max: 0.000355298306571
- last_two_basis_changes_max: 0.000355298306571
- scf_tolerance_energy_error_max: 2.1869092981e-07
- scf_tolerance_errors: [2.1869092980963956e-07, 6.483702463810914e-14, 0.0]
- max_overlap_condition_number: 3534.73030868

https://hrkoyama.github.io/code/molecular-hf/2026-11-22/results/result.json

## 実行

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples/h2-rhf/?lang=ja

## 文献

- Boys, S. F. (1950). Electronic wave functions - I. A general method of calculation for the stationary states of any molecular system. https://doi.org/10.1098/rspa.1950.0036 — 既存アトラスの原著書誌とDOIを確認。今回の実装により原論文全体を再現・監査したという意味ではありません。
- Roothaan, C. C. J. (1951). New Developments in Molecular Orbital Theory. https://doi.org/10.1103/RevModPhys.23.69 — 既存アトラスの原著書誌とDOIを確認。今回の実装により原論文全体を再現・監査したという意味ではありません。
- C. A. Coulson and I. Fischer (1949). XXXIV. Notes on the molecular orbital treatment of the hydrogen molecule. https://doi.org/10.1080/14786444908521726 — RHFの解離と制約を考える歴史的出典として書誌・DOIを確認。原文全文の監査ではありません。
- Qiming Sun et al. (2020). Recent developments in the PySCF program package. https://doi.org/10.1063/5.0006074 — 出版社の書誌・抄録と著者機関の登録を確認。参照コードの実行は別の数値検査です。
- PySCF developers (2026). Self-consistent field (SCF) methods. https://pyscf.org/user/scf.html — 公式資料のSCF方程式・収束・安定性・線形従属の節を参照。原法の論文とは区別。
- W. J. Hehre, R. F. Stewart and J. A. Pople (1969). Self-Consistent Molecular-Orbital Methods. I. Use of Gaussian Expansions of Slater-Type Atomic Orbitals. https://doi.org/10.1063/1.1672392 — 出版社由来の書誌・DOIを確認。STO-nGの原著として引用し、今回使う係数の全桁をこの原論文から転記したという意味ではありません。原文の全文監査は未実施。
- Basis Set Exchange (2018). STO-3G version 1: hydrogen basis data. https://www.basissetexchange.org/basis/sto-3g/format/json/?elements=1%2C2&version=1 — 公式APIのversion 1にあるHの指数・係数を入力と照合。数値の採用規約はBSE v1（Gaussian由来の桁数）であり、1969年論文の印刷桁の再現ではありません。
