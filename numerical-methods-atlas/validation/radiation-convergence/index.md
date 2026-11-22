# 放射輸送：空間・角度収束と光子統計

純吸収平板で特性解・独立適応求積・光子生存率を比較し、離散収支と標本誤差・区間被覆を別々に測ります。

## 前提・単位・境界

定常一様平板、光学的厚さ.1/.7/3、正の半球から単位強度、逆入射・散乱・内部放射0。フラックス基準の光子入射方向はpdf=2muです。

**編集上の補足**

純吸収平板の空間・角度誤差を分離し、特性解・適応求積・光子生存率を照合します。有限seedの区間被覆を全seed保証とせず、散乱や放射流体連成は未検証です。

## 採用した計算法

1次風上有限体積の空間更新とGauss–Legendre方向を使い、角度系列は正確な指数伝播で空間誤差を除きます。MCはmu=sqrt(U)と指数光学距離から生存・吸収を独立に判定します。

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

## 比較・検証

16〜256セル・4〜64方向を別に収束させ、QUADPACK積分とE3を照合。64seed・1024/4096/16384光子で平均誤差、RMSE、二項標準偏差と95% Clopper–Pearson区間の実測被覆を記録します。全光子の出射＋吸収、正値性と離散フラックス収支を確認します。

## 確認の限界

区間被覆は有限の固定seedでの観測で、ちょうど95%の実測値や全seedの成功を保証しません。決定論的求積誤差を統計誤差へ含めず、多重散乱・周波数依存・熱放射・放射流体連成は未検証です。

## 保存実測値と判定

```json
{
  "metrics": {
    "reference_difference": 8.881784197001252e-16,
    "quad_reported_error": 4.357392576641327e-12,
    "minimum_spatial_order": 0.9856180164488282,
    "finest_spatial_flux_error": 0.0022447377157130965,
    "finest_angular_flux_error": 9.019895941264622e-12,
    "minimum_angular_reduction": 291718065.1011767,
    "balance_error": 7.771561172376096e-16,
    "minimum_intensity": 1.9515912759331092e-130,
    "maximum_intensity": 1.0,
    "mc_mean_standard_errors": 1.2889293439083243,
    "minimum_mc_rmse_ratio": 0.8350073934277391,
    "maximum_mc_rmse_ratio": 1.0858116678301433,
    "minimum_measured_coverage": 0.9375,
    "minimum_mc_rmse_reduction": 1.6796261124956355
  },
  "checks": {
    "independent_characteristic_reference": true,
    "reference_quadrature_error": true,
    "spatial_convergence": true,
    "spatial_accuracy": true,
    "angular_accuracy": true,
    "angular_convergence": true,
    "balance": true,
    "positivity": true,
    "mc_mean": true,
    "mc_binomial_error": true,
    "mc_coverage": true,
    "mc_statistical_scaling": true
  }
}
```

全recordsとreference_records：https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/index.json

## 取得・実行

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

このコマンドは配布グループの全例を実行します。

入力・検証手順の履歴：https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## 出典と確認範囲

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
  出版社HTMLの書誌・抄録と基本の輸送式を確認。離散座標の背景として引用し、本例はDISORT全機能の実装ではありません。
- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
  一般化指数積分の積分表示を公式資料で確認。年は確認年。
- SciPy developers (2024). SciPy 1.14.1: BinomTestResult.proportion_ci. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html; review_level=official-versioned-documentation
  公式資料でexactがClopper–Pearson法を使うことと区間APIを確認。1934年原著本文は取得できず、本文閲覧とはしません。

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.

# Radiation transport: space/angle convergence and photon statistics

Compare characteristics, independent adaptive integration and photon survival in a pure-absorption slab; separate discrete balance, sampling error and interval coverage.

## Assumptions, units and boundaries

Steady uniform slab, optical depths .1/.7/3, unit incoming positive-hemisphere intensity, no reverse inflow/scattering/emission. Incoming photon directions for a flux estimator have density 2mu.

**Editorial clarification**

Separate space and angle errors for a pure-absorption slab, comparing characteristics, adaptive quadrature and photon survival. Finite-seed coverage is no all-seed guarantee; scattering and radiation hydrodynamics remain unvalidated.

## Adopted numerical method

Use upstream finite volumes and Gauss-Legendre ordinates; exact exponential propagation removes spatial error in the angle series. Monte Carlo independently tracks survival/absorption using mu=sqrt(U) and exponential optical paths.

$$
F_{\rm out}=2\pi E_3(\tau)=\pi p,\qquad\mu=\sqrt U
$$

$$
\sigma_{\widehat F}=\pi\sqrt{p(1-p)/N_\gamma}
$$

## References and validation

Refine 16–256 cells and 4–64 ordinates separately; compare QUADPACK integration with E3. For 64 seeds and 1024/4096/16384 photons, record mean error, RMSE, binomial standard deviation and observed 95% Clopper–Pearson coverage. Check photon exit-plus-absorption counts, positivity and discrete flux balance.

## Limits

Coverage is observed over finite fixed seeds; neither exactly 95% empirical coverage nor all-seed success is guaranteed. Keep deterministic quadrature error separate from statistical error. Multiple scattering, frequency dependence, thermal emission and radiation hydrodynamics are unvalidated.

## Stored measurements and decisions

```json
{
  "metrics": {
    "reference_difference": 8.881784197001252e-16,
    "quad_reported_error": 4.357392576641327e-12,
    "minimum_spatial_order": 0.9856180164488282,
    "finest_spatial_flux_error": 0.0022447377157130965,
    "finest_angular_flux_error": 9.019895941264622e-12,
    "minimum_angular_reduction": 291718065.1011767,
    "balance_error": 7.771561172376096e-16,
    "minimum_intensity": 1.9515912759331092e-130,
    "maximum_intensity": 1.0,
    "mc_mean_standard_errors": 1.2889293439083243,
    "minimum_mc_rmse_ratio": 0.8350073934277391,
    "maximum_mc_rmse_ratio": 1.0858116678301433,
    "minimum_measured_coverage": 0.9375,
    "minimum_mc_rmse_reduction": 1.6796261124956355
  },
  "checks": {
    "independent_characteristic_reference": true,
    "reference_quadrature_error": true,
    "spatial_convergence": true,
    "spatial_accuracy": true,
    "angular_accuracy": true,
    "angular_convergence": true,
    "balance": true,
    "positivity": true,
    "mc_mean": true,
    "mc_binomial_error": true,
    "mc_coverage": true,
    "mc_statistical_scaling": true
  }
}
```

Complete records and reference_records: https://hrkoyama.github.io/numerical-methods-atlas/validation/radiation-convergence/index.json

## Download and run

ZIP: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/atlas-particle-transport-2026-11-22.zip
Input: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json
Results: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/results/result.json
Receipt: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/verification.json

```sh
python -m pip install -r requirements.txt
python -m pytest -q
python run.py --input inputs.json --output output
```

This command executes every fixed case in the distribution group.

Input and validation protocol history: https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/protocol-history.json

https://hrkoyama.github.io/code/validated-examples/2026-11-22/particle-transport/inputs.json

## Sources and review scope

- K. Stamnes, S.-C. Tsay, W. Wiscombe and K. Jayaweera (1988). Numerically stable algorithm for discrete-ordinate-method radiative transfer in multiple scattering and emitting layered media. https://doi.org/10.1364/AO.27.002502; review_level=selected-full-text
  Publisher HTML bibliography, abstract and base transfer equation checked; cited as discrete-ordinate background, not full DISORT implementation.
- NIST Digital Library of Mathematical Functions (2026). §8.19 Generalized Exponential Integral. https://dlmf.nist.gov/8.19; review_level=official-documentation
  Official integral representation of the generalized exponential integral checked; year denotes access year.
- SciPy developers (2024). SciPy 1.14.1: BinomTestResult.proportion_ci. https://docs.scipy.org/doc/scipy-1.14.1/reference/generated/scipy.stats._result_classes.BinomTestResult.proportion_ci.html; review_level=official-versioned-documentation
  Official documentation confirms the exact Clopper–Pearson method and interval API. The 1934 publisher text was unavailable; no full-paper reading is claimed.

Original code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.
