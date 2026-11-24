import {projectMethodBeforeBatch38,groupsAddedAfterBatch37,problemCount,examplesAddedAfterBatch37,supplementCaseCount,supplementGroupCount} from './fixtures/atlas-inventory.mjs';
import {methodCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root=new URL('../',import.meta.url),base='code/validated-examples/2026-11-23/level-set/';
const text=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const objectHash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
// Only these eight existing methods gained the separately validated batch13–17 bindings/scope.
// Their original IDs, names, statuses and all other scientific metadata remain in the golden.
const batchBindingFields={"p1-fem":["depth_release","depth_scope","depth_previous_status"],"dg":["depth_release","depth_scope","depth_previous_status"],"centered-difference":["depth_scope","depth_additional_releases"],"godunov":["depth_scope","depth_release"],"weno-js":["depth_release","depth_scope"],"hll":["depth_scope","depth_additional_releases"],"forward-euler":["depth_release","depth_scope"],"heun":["depth_scope","depth_additional_releases"],"rk4":["depth_scope","depth_additional_releases"],"weno-z":["depth_scope","depth_release"]};
const canonicalMethodValue=value=>Array.isArray(value)?value.map(canonicalMethodValue):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(key=>[key,canonicalMethodValue(value[key])])):value;
// Project only named batch28 metadata additions/approved curation for historical hashes.
// The root-owned new batch test independently protects current scientific fields and bindings.
const batch28LegacyMethods=new Map(json('scripts/fixtures/atlas-batch28-37-baseline.json').legacy_method_records.map(row=>[row.id,row]));
const batch28BoundMethodIds=new Set(['amg', 'barnes-hut', 'cg', 'cic', 'dsmc', 'ewald', 'fmm', 'multigrid', 'pic', 'q1-fem', 'slab-ewald', 'verlet']);
const batch28HistoricalMethod=method=>{
 const old=batch28LegacyMethods.get(method.id),copy={...method};
 const restore=key=>{if(Object.hasOwn(old,key))copy[key]=old[key];else delete copy[key];};
 if(batch28BoundMethodIds.has(method.id)){
  for(const key of ['summary','limitations','depth_release','depth_additional_releases','supplemental_scope_profiles','batch28_existing_variant_labels'])restore(key);
  const review={...(copy.metadata_review||{})},prior=old.metadata_review||{};
  if(Object.hasOwn(prior,'supplemental_review'))review.supplemental_review=prior.supplemental_review;else delete review.supplemental_review;
  if(Object.hasOwn(old,'metadata_review')||Object.keys(review).length)copy.metadata_review=review;else delete copy.metadata_review;
 }
 if(['verlet','multigrid','cic','barnes-hut','slab-ewald'].includes(method.id))restore('depth_scope');
 if(method.id==='slab-ewald')for(const key of ['status','depth_previous_status','previous_planned_description','next_deliverable'])restore(key);
 if(method.id==='q1-fem')for(const key of ['name','code_mapping_scope'])restore(key);
 if(method.id==='thomas')for(const key of ['summary','references','metadata_review','bibliographic_original'])restore(key);
 return copy;
};
// Project only this batch's appended bindings back to the recorded pre-batch fields.
const batch18MethodBindings={"centered-difference":{"depth_release":{"group":"models","edition":"2026-11-22","case_ids":["reaction-diffusion-fourier","turing-schnakenberg"]},"depth_additional_releases":[{"group":"biology","edition":"2026-11-22","case_ids":["schnakenberg-nonlinear","schnakenberg-pattern"]},{"group":"wall-flow","edition":"2026-11-23-r2","case_ids":["cavity-ghia-re100","wall-manufactured"]}],"depth_scope":{"ja":"反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。","en":"Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct."},"depth_previous_status":"educational-example"},"heun":{"depth_release":{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},"depth_additional_releases":[{"group":"noh-cartesian","edition":"2026-11-23-r2","case_ids":["noh-cartesian-2d"]},{"group":"sedov","edition":"2026-11-23-r2","case_ids":["sedov-blast"]},{"group":"double-mach","edition":"2026-11-23","case_ids":["double-mach-reflection"]},{"group":"forward-step","edition":"2026-11-23","case_ids":["forward-step-m3"]},{"group":"guderley","edition":"2026-11-23-r3","case_ids":["guderley-implosion"]},{"group":"wall-flow","edition":"2026-11-23-r2","case_ids":["cavity-ghia-re100","wall-manufactured"]}],"depth_scope":{"ja":"初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。","en":"An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct."},"depth_previous_status":"educational-example"},"hlld":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["brio-independent"]},"depth_scope":{"ja":"公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。","en":"Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit."},"depth_previous_status":"educational-example"},"muscl":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["shu-independent"]},"depth_additional_releases":[{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},{"group":"low-mach","edition":"2026-11-23","case_ids":["low-mach-vortex"]},{"group":"euler-positivity","edition":"2026-11-23-r2","case_ids":["euler-double-rarefaction-positivity"]},{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。 追加Noh版では球対称系列だけに体積重心を用いる保存量MUSCL/minmod＋Heunを実装し、平面・円筒は区分定数のままです。 低Mach渦の追加例は、両Roe流束に同じ無制限の中心primitive再構築を用います。勾配制限付きMUSCL全般やTVDの保証ではありません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code. The additional Noh edition uses volume-centroid conservative MUSCL/minmod with Heun only in spherical runs; planar/cylindrical states stay piecewise constant. The additional low-Mach vortex uses the same unlimited central primitive reconstruction for both Roe variants. It does not verify general limited MUSCL or a TVD guarantee. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"ct":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["ct-glm-independent"]},"depth_additional_releases":[{"group":"mhd-convergence","edition":"2026-11-22","case_ids":["ct-glm-smooth-convergence","ct-glm-ot-convergence","ct-glm-constraint-control"]}],"depth_scope":{"ja":"Orszag–Tang：CT・GLMと独立Athena++比較: 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 CT・GLM：移動する磁気静力学平衡の格子・時間収束: 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。 Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束: 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。 CTの初期制約保持とGLMの能動的cleaning：非物理診断対照: 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。","en":"Orszag–Tang: CT, GLM and independent Athena++: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence. Orszag–Tang: matched CT/GLM and converged independent references: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated. Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem."},"depth_previous_status":"educational-example"},"p1-fem":{},"cg":{},"ale":{},"upwind":{"depth_release":{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]},"depth_scope":{"ja":"追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."}},"rk4":{"depth_release":{"group":"models","edition":"2026-11-22","case_ids":["reaction-diffusion-fourier","turing-schnakenberg","fitzhugh-nagumo"]},"depth_additional_releases":[{"group":"weno-critical","edition":"2026-11-23","case_ids":["weno-critical-epsilon"]}],"depth_scope":{"ja":"反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照: 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。","en":"Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects."},"depth_previous_status":"educational-example"},"hll":{"depth_release":{"group":"double-mach","edition":"2026-11-23","case_ids":["double-mach-reflection"]},"depth_additional_releases":[{"group":"forward-step","edition":"2026-11-23","case_ids":["forward-step-m3"]},{"group":"guderley","edition":"2026-11-23-r3","case_ids":["guderley-implosion"]},{"group":"shallow-water","edition":"2026-11-23","case_ids":["swashes-topography","dry-bed-dam-break"]}],"depth_scope":{"ja":"既存のHLL流束・Heunによる2D Double Mach反射を3格子で検証し、別実装の有限格子数値参照との差、境界流束収支、衝撃位置と未解像の壁近傍構造を示します。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。","en":"Three-grid 2D Double Mach verification using HLL and Heun compares a separately written finite-grid numerical reference, boundary-flux budgets, shock position and unresolved near-wall structure. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front."},"depth_previous_status":"educational-example"},"minmod":{"depth_release":{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},"depth_additional_releases":[{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"このNoh配布の球対称系列で、保存量のMUSCL型再構築の傾きをminmodで制限します。平面・円筒は区分定数のままです。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"Minmod limits conserved-variable MUSCL slopes in this Noh edition's spherical series. Planar/cylindrical runs retain piecewise-constant states. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"ssprk33":{"depth_release":{"group":"low-mach","edition":"2026-11-23","case_ids":["low-mach-vortex"]},"depth_additional_releases":[{"group":"euler-positivity","edition":"2026-11-23-r2","case_ids":["euler-double-rarefaction-positivity"]},{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"背景Mach数.1/.01の滑らかな2D Euler等エントロピー渦で、両流束に無制限の中心primitive MUSCL再構築を用い、通常RoeとMiczek系の数値散逸行列前処理D=P⁻¹|PA|を比較します。SSPRK(3,3)で元の物理時間項と音響CFLを保ち、速度誤差・動圧規格化した圧力誤差・周期保存収支・標本Fourier診断を分けて評価します。擬似時間・二重時間積分の定常加速や、勾配制限・TVDの保証は扱いません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"A fixed smooth 2D Euler isentropic vortex at background Mach numbers .1 and .01 compares ordinary Roe and Miczek-type dissipation-matrix preconditioning D=P⁻¹|PA|, with unlimited central primitive-variable MUSCL reconstruction for both. SSPRK(3,3) retains physical time and the acoustic CFL. Velocity error, dynamically normalized pressure error, periodic conservation and sampled Fourier diagnostics are evaluated separately. Pseudo-time or dual-time steady acceleration, slope limiting and TVD guarantees remain outside this example. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"dg":{}};
const batch18HistoricalMethod=method=>{if(!Object.hasOwn(batch18MethodBindings,method.id))return method;const copy={...method},old=batch18MethodBindings[method.id];for(const key of ['depth_release','depth_additional_releases','depth_scope','depth_previous_status']){if(Object.hasOwn(old,key))copy[key]=old[key];else delete copy[key];}return copy;};
const historicalMethod=current=>{const method=batch18HistoricalMethod(batch28HistoricalMethod(projectMethodBeforeBatch38(current)));return canonicalMethodValue(Object.fromEntries(Object.entries(method).filter(([key])=>!(batchBindingFields[method.id]||[]).includes(key))));};
const ids=['level-set-translation','level-set-rotation'];
const inputs=json(base+'inputs.json'),result=json(base+'results/result.json');

test('the dedicated two-case release preserves all previous releases, method records, primary pictures and the shared execution registry',()=>{
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.releases.length,supplementGroupCount);assert.equal(registry.case_count,supplementCaseCount);
 assert.equal(registry.releases.filter(r=>!['coefficient-diffusion', 'slab-ewald', 'fmm3d', 'gravity-dynamics', 'warm-pic', 'pic-spatial', 'dsmc-wall', 'dsmc-shock',...groupsAddedAfterBatch37].includes(r.group)).reduce((s,r)=>s+r.tests,0),893);
 assert.equal(objectHash(registry.releases.filter(r=>!['level-set','weno-critical','shallow-water','wall-flow', 'instability-growth', 'mhd-transport', 'mesh-boundary', 'moving-waves', 'relativistic', 'sem-fr','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(r.group))),'150a2bfb669938f7c9c67dde0f23fcc4dace9e54c3298841fed651a57bb5fd3f');
 const methods=json('catalog/atlas-methods.json').methods;
 assert.equal(methods.length,methodCount);
 assert.equal(objectHash(methods.filter(m=>!['level-set','vof', 'q1-fem', 'spectral-element', 'flux-reconstruction'].includes(m.id)).map(historicalMethod)),'6462e0c0e177b17a95b97d953fd12bf2887933124691bb8844c5cc0eda9ee904');
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 assert.equal(pictures.length,problemCount);
 assert.equal(objectHash(pictures.filter(p=>!['level-set-circle','swashes-topography','dry-bed-dam-break','lid-driven-cavity','wall-manufactured', 'kh-initial-growth', 'rt-initial-growth', 'lshape-fem', 'annular-viscous-mms', 'poisson-neumann', 'poisson-robin', 'ale-nonuniform-transport', 'cgrid-rotating-wave', 'srhd-collision', 'srmhd-alfven','checkerboard-diffusion','rotated-anisotropic-diffusion','neutral-slab-yb','fmm3d-inverse-r','gravity-kepler','gravity-plummer-short','thermal-landau-damping','thermal-two-stream','dsmc-couette','dsmc-fourier','dsmc-planar-shock',...examplesAddedAfterBatch37].includes(p.id))),'ea4dfdfc33dfb4da3c54b6a6a5d8e1c02fd10b94b2281af9e21fd15f55938d9c');
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 assert.equal(sha(base+'inputs.json'),sha(base+'inputs-initial.json'));
 const contract=json(base+'pre-run-contract.json');assert.equal(contract.planned_tests,22);
 for(const [p,h] of Object.entries(contract.files_sha256))assert.equal(sha(base+p),h,p);
 const history=json(base+'protocol-history.json');assert.equal(history.first_fixed_protocol_passed,true);assert.equal(history.acceptance_modified_after_first_execution,false);
 assert.equal(history.unit_test_revision.original_passed,21);assert.equal(history.unit_test_revision.original_failed,1);
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,22);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);
 for(const[p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(sha(base+p),h,p);
});

test('observed errors follow the actual intermediate interface samples, balanced refinement and explicit redistancing jumps',()=>{
 assert.equal(result.passed,true);assert.equal(result.input_sha256,sha(base+'inputs.json'));
 for(const c of result.cases){
  assert.ok(ids.includes(c.id));assert.ok(c.passed&&Object.values(c.checks).every(Boolean));
  const config=inputs.cases[c.id];assert.deepEqual(config.grids,[32,64,128]);
  for(const mode of ['advection-only','redistance']){
   const rows=c.records.filter(r=>r.mode===mode);assert.deepEqual(rows.map(r=>r.n),config.grids);
   rows.forEach((row,index)=>{
    assert.deepEqual(row.snapshots.map(s=>s.time),config.snapshots);
    assert.equal(row.maximum_interface_error,Math.max(...row.snapshots.slice(1).map(s=>s.interface_max_radial_error)));
    if(index)assert.ok(Math.abs(row.observed_order-Math.log2(rows[index-1].maximum_interface_error/row.maximum_interface_error))<1e-12);
    row.contours.forEach((points,k)=>{
     const t=config.snapshots[k],angle=config.omega*t;
     const center=c.id.endsWith('translation')?[.3+.2*t,.35+.1*t]:[.5+.18*Math.cos(angle),.5+.18*Math.sin(angle)];
     const error=Math.max(...points.map(p=>Math.abs(Math.hypot(p[0]-center[0],p[1]-center[1])-.15)));
     assert.ok(Math.abs(error-row.snapshots[k].interface_max_radial_error)<2e-15);
    });
    assert.equal(row.redistance_calls,mode==='redistance'?10:0);
    assert.equal(row.state_clip_count,row.volume_correction_count);assert.equal(row.state_clip_count,0);
    for(const log of row.redistance_log)assert.equal(log.area_change,log.area_after-log.area_before);
   });
  }
  assert.ok(c.metrics.advection_observed_order>1.5&&c.metrics.advection_observed_order<2.5);
  assert.ok(c.metrics.redistance_finest_relative_area_error>c.metrics.advection_finest_relative_area_error);
 }
});

test('the distribution retains real finite128x128 numerical fields that differ from the analytic interior',()=>{
 const program=String.raw`
import array,ast,math,pathlib,struct,zipfile
base=pathlib.Path('code/validated-examples/2026-11-23/level-set/results')
for ident in ['level-set-translation','level-set-rotation']:
 with zipfile.ZipFile(base/(ident+'.npz')) as z:
  def field(name):
   b=z.read(name+'.npy');assert b[:6]==b'\x93NUMPY' and b[6]==1
   n=struct.unpack('<H',b[8:10])[0];h=ast.literal_eval(b[10:10+n].decode())
   assert h['shape']==(128,128) and h['descr']=='<f8' and not h['fortran_order']
   a=array.array('d');a.frombytes(b[10+n:]);assert all(math.isfinite(x) for x in a);return a
  reference=field('reference_final');plain=field('phi_advection');red=field('phi_redistance')
  assert max(abs(x-y) for x,y in zip(plain,reference))>1e-5
  assert max(abs(x-y) for x,y in zip(plain,red))>1e-5
print('real2D fields retained')
`;
 assert.match(execFileSync('python3',['-B','-c',program],{cwd:fileURLToPath(root),encoding:'utf8'}),/real2D fields retained/);
});

test('level sets have dedicated educational code while VOF remains reading-only with no borrowed execution',()=>{
 const methods=json('numerical-methods-atlas/methods/index.json').methods;
 const level=methods.find(m=>m.id==='level-set'),vof=methods.find(m=>m.id==='vof');
 assert.equal(level.status,'educational-example');assert.equal(level.depth_release.group,'level-set');
 assert.deepEqual(level.execution_examples.map(e=>e.id),ids);
 assert.ok(level.code_urls.some(u=>u.endsWith('/level-set/level_set.py')));
 assert.equal(vof.status,'reading-only');assert.deepEqual(vof.code_urls,[]);assert.deepEqual(vof.test_urls,[]);assert.deepEqual(vof.execution_examples,[]);
 const problems=json('catalog/atlas-test-problems.json').problems;
 assert.deepEqual(problems.filter(p=>(p.supplemental_examples||[]).some(e=>ids.includes(e.id))).map(p=>p.id),['level-set-circle']);
 for(const ident of ids){
  const page=json(`numerical-methods-atlas/validation/${ident}/index.json`);
  assert.equal(page.problem_id,'level-set-circle');assert.deepEqual(page.method_ids,['level-set']);
  assert.deepEqual(page.execution_navigation.equations.map(e=>e.id),['level-set-advection']);
 }
});

test('both languages and searches expose the theory, VOF comparison, geometry, two executable cases and manifest links',()=>{
 for(const lang of ['ja','en']){
  const chapter=json(`numerical-methods-atlas/${lang}/read/level-set/index.json`);
  assert.ok(chapter.html.includes('id="vof-comparison"')&&chapter.html.includes('<table'));
  assert.ok(chapter.html.includes('katex-mathml')&&!chapter.html.includes('math-placeholder'));
  assert.deepEqual(chapter.scoped_supplements.map(c=>c.id),ids);
  assert.ok(chapter.html.includes('level-set-overview.png'));
  assert.equal(chapter.implementation_status.vof,'reading-only');
  assert.ok(json(`numerical-methods-atlas/${lang}/read/index.json`).groups.some(g=>g.chapters.some(c=>c.id==='level-set')));
  for(const ident of ids){
   const html=text(`numerical-methods-atlas/validation/${ident}/index.html`);
   for(const suffix of ['inputs.json','verification.json','source-manifest.json','atlas-level-set-2026-11-23.zip',`results/${ident}.png`])assert.ok(html.includes('/'+base+suffix));
  }
 }
 const global=makeSearch(json('search/index.json').documents),inline=json('numerical-methods-atlas/home-search-index.json');
 for(const [q,lang,id]of [['レベルセット 平行移動 実行','ja',ids[0]],['level set rotation run','en',ids[1]]]){
  for(const result of [global(q,lang,'atlas'),searchChapters(inline,q,lang)])assert.ok(result.some(r=>r.kind==='execution-example'&&r.url.includes('/validation/'+id+'/')),q);
 }
});
