import {projectMethodBeforeBatch38,groupsAddedAfterBatch37,problemCount,examplesAddedAfterBatch37,supplementCaseCount,supplementGroupCount} from './fixtures/atlas-inventory.mjs';
import {methodCount} from './fixtures/atlas-inventory.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {makeSearch} from '../search/engine.mjs';
import {searchChapters} from '../numerical-methods-atlas/home-search.js';

const root=new URL('../',import.meta.url),base='code/validated-examples/2026-11-23/sem-fr/';
const text=p=>readFileSync(new URL(p,root),'utf8'),json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const hash=x=>createHash('sha256').update(JSON.stringify(canonical(x))).digest('hex');

// Invert only the exact dated batch48 append, before the older historical projections.
// Old UTF-8/reference/release prefixes remain in the original whole-record golden;
// the nine fixed append fingerprints below reject arbitrary future additions.
const batch48Baseline=json('scripts/fixtures/atlas-batch48-57-baseline.json');
const batch48NewMethodIds=new Set(["lu-partial-pivoting","cholesky","minres","lobpcg","pseudo-arclength-continuation","jacobian-free-newton-krylov"]);
assert.deepEqual(batch48Baseline.expected_new_method_ids,[...batch48NewMethodIds]);
const batch48AppendSHA={"centered-difference":"b0fa5ecfc24bed42c54d3f7f817a7537cdaa2692530fad452311648a09d1f7c8","implicit-midpoint":"00ffd02c8d35a4b7771d107f35ab14d00e02c3a1422783e682919d37afc23588","leapfrog":"2a5a974977d04a9d3c634036cdda96d422b6dbfee41827a819d4e8cf251ff715","thomas":"b4388102fb4f9290f7c0a2a575b2c0f40efd3b705515e69b8b029dca0990ba98","gmres":"573ba798584e44f5a9fb85ea611c6b289f34c94b677a6c266f0a8f01769e6aca","newton":"ea5757d43ccfbd61a5ff562d8821caf9912a6bdef8abc6535e158b699956182e","fdtd":"2a5a974977d04a9d3c634036cdda96d422b6dbfee41827a819d4e8cf251ff715","eigensolvers":"7d02138efc932332491d93ddb9551a6725cd4c894a989b3cc601fd98c7ba3ae7","automatic-differentiation":"b4388102fb4f9290f7c0a2a575b2c0f40efd3b705515e69b8b029dca0990ba98"};
const batch48Canonical=value=>Array.isArray(value)?value.map(batch48Canonical):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(key=>[key,batch48Canonical(value[key])])):value;
const batch48Hash=value=>createHash('sha256').update(JSON.stringify(batch48Canonical(value))).digest('hex');
const projectMethodBeforeBatch48=row=>{
 if(!Object.hasOwn(batch48AppendSHA,row.id))return row;
 const before=batch48Baseline.methods[row.id],copy={...row},added={};
 for(const field of ['summary','limitations']){
  copy[field]={...row[field]};added[field]={};
  for(const [language,prefix]of Object.entries(before.text_prefixes[field])){
   const bytes=Buffer.from(row[field][language]),head=bytes.subarray(0,prefix.utf8_bytes);
   assert.equal(createHash('sha256').update(head).digest('hex'),prefix.sha256,row.id+'/'+field+'/'+language+'/old-prefix');
   copy[field][language]=head.toString('utf8');added[field][language]=bytes.subarray(prefix.utf8_bytes).toString('utf8');
  }
 }
 const referenceCount=before.reference_prefix_sha256.length;
 assert.ok(referenceCount>0&&row.references.length>=referenceCount,row.id+'/old-references');
 copy.references=row.references.slice(0,referenceCount);added.references=row.references.slice(referenceCount);
 for(const [field,prefix]of [['depth_additional_releases',before.additional_release_prefix_sha256],['supplemental_scope_profiles',before.scope_profile_prefix_sha256]]){
  const values=row[field]||[];assert.ok(values.length>=prefix.length,row.id+'/'+field+'/old-prefix');
  added[field]=values.slice(prefix.length);
  if(prefix.length)copy[field]=values.slice(0,prefix.length);else delete copy[field];
 }
 added.metadata_review=Object.fromEntries(Object.entries(row.metadata_review||{}).filter(([key])=>!before.review_keys.includes(key)));
 copy.metadata_review=Object.fromEntries(before.review_keys.map(key=>[key,row.metadata_review[key]]));
 added.depth_release=before.primary_release?null:(row.depth_release||null);
 if(before.primary_release)assert.deepEqual(row.depth_release,before.primary_release,row.id+'/old-primary-release');
 else{assert.ok(!Object.hasOwn(row,'depth_scope'),row.id+'/first-supplement-keeps-no-primary-scope');delete copy.depth_release;}
 assert.equal(batch48Hash(added),batch48AppendSHA[row.id],row.id+'/exact-reviewed-batch48-append');
 return copy;
};

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
// Restore only the additional batch18–27 binding fields from the frozen149-method baseline.
const batch18MethodBindings={"centered-difference":{"depth_release":{"group":"models","edition":"2026-11-22","case_ids":["reaction-diffusion-fourier","turing-schnakenberg"]},"depth_additional_releases":[{"group":"biology","edition":"2026-11-22","case_ids":["schnakenberg-nonlinear","schnakenberg-pattern"]},{"group":"wall-flow","edition":"2026-11-23-r2","case_ids":["cavity-ghia-re100","wall-manufactured"]}],"depth_scope":{"ja":"反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 Schnakenberg有限振幅過渡：非線形性と独立参照: t=8までの有限振幅反応拡散を、独立なFourier–Galerkin参照・格子と時間刻み収束・新しい高調波で検証します。 Schnakenberg飽和パターン：近定常性と格子・時間収束: t=100の1D選択パターンを独立参照で照合。参照の90→100の変化・全PDE残差と、有限刻みprimaryのFD残差を分けて測ります。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。","en":"Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. Finite-amplitude Schnakenberg transient: nonlinearity and independent reference: Validate a finite-amplitude reaction-diffusion transient to t=8 with an independent Fourier–Galerkin reference, grid/time convergence and newly generated harmonics. Near-saturated Schnakenberg pattern: near-stationarity and grid/time convergence: Compare the selected1D pattern at t=100 with an independent reference. Separate reference90→100 change/full-PDE residual from the finite-step primary FD residual. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct."},"depth_previous_status":"educational-example"},"heun":{"depth_release":{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},"depth_additional_releases":[{"group":"noh-cartesian","edition":"2026-11-23-r2","case_ids":["noh-cartesian-2d"]},{"group":"sedov","edition":"2026-11-23-r2","case_ids":["sedov-blast"]},{"group":"double-mach","edition":"2026-11-23","case_ids":["double-mach-reflection"]},{"group":"forward-step","edition":"2026-11-23","case_ids":["forward-step-m3"]},{"group":"guderley","edition":"2026-11-23-r3","case_ids":["guderley-implosion"]},{"group":"wall-flow","edition":"2026-11-23-r2","case_ids":["cavity-ghia-re100","wall-manufactured"]}],"depth_scope":{"ja":"初期圧力ゼロのNoh問題を、独自の小型1D有限体積コードで平面・円筒・球対称に計算します。64/128/256/512格子の全域誤差、原点過熱、衝撃位置、保存収支を測り、球で現れる境界流入の時間積分誤差を解析式と照合します。 追加の2D Cartesian Noh版は正方形全域のx/y流束と2成分運動量を更新する軽量例です。 Sedov球対称爆発の追加例では、有限半径へのエネルギー投入と格子の影響を分けて測ります。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 非周期壁面の2D渦度・流れ関数法でRe100蓋駆動キャビティと製造流れを解きます。Ghia原著の有限格子数値表、壁剪断と格子収束を比較し、独立した圧力Poisson・勾配製造問題を区別します。","en":"An original small 1D finite-volume code solves zero-pressure Noh flow in planar, cylindrical and spherical symmetry. Grids 64/128/256/512 measure full-domain error, origin heating, shock location and budgets, and compare spherical boundary-inflow time-quadrature error with its analytic identity. The additional2D Cartesian Noh edition updates both x/y fluxes and both momenta on a full square. The additional spherical Sedov blast measures grid and finite deposition-radius effects separately. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Solve a Re100 lid-driven cavity and manufactured flow with a nonperiodic wall-bounded2D vorticity/streamfunction method. Compare original finite-grid Ghia tables, wall shear and grid refinement, keeping a separate pressure-Poisson/gradient manufactured problem distinct."},"depth_previous_status":"educational-example"},"hlld":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["brio-independent"]},"depth_scope":{"ja":"公開HLLD-MC有限体積コードを、固定コミットから別に構築したAthena++のBrio–Wu参照と比較します。","en":"Compare the published HLLD-MC finite-volume code with Brio–Wu reference data independently produced by Athena++ at a pinned commit."},"depth_previous_status":"educational-example"},"muscl":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["shu-independent"]},"depth_additional_releases":[{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},{"group":"low-mach","edition":"2026-11-23","case_ids":["low-mach-vortex"]},{"group":"euler-positivity","edition":"2026-11-23-r2","case_ids":["euler-double-rarefaction-positivity"]},{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"衝撃波と密度正弦波の相互作用を、同じPython実装の細格子ではなく、別に実行したAthena++の参照と照合します。 追加Noh版では球対称系列だけに体積重心を用いる保存量MUSCL/minmod＋Heunを実装し、平面・円筒は区分定数のままです。 低Mach渦の追加例は、両Roe流束に同じ無制限の中心primitive再構築を用います。勾配制限付きMUSCL全般やTVDの保証ではありません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"Compare shock–density-wave interaction against separately executed Athena++ reference data rather than a finer grid of the same Python code. The additional Noh edition uses volume-centroid conservative MUSCL/minmod with Heun only in spherical runs; planar/cylindrical states stay piecewise constant. The additional low-Mach vortex uses the same unlimited central primitive reconstruction for both Roe variants. It does not verify general limited MUSCL or a TVD guarantee. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"ct":{"depth_release":{"group":"mhd","edition":"2026-11-22","case_ids":["ct-glm-independent"]},"depth_additional_releases":[{"group":"mhd-convergence","edition":"2026-11-22","case_ids":["ct-glm-smooth-convergence","ct-glm-ot-convergence","ct-glm-constraint-control"]}],"depth_scope":{"ja":"Orszag–Tang：CT・GLMと独立Athena++比較: 同じ周期Orszag–Tang初期値で、CTとGLMの密度・磁場、保存量、div Bを測り、別に実行したAthena++と比較します。 CT・GLM：移動する磁気静力学平衡の格子・時間収束: 非零の磁気力と圧力勾配が釣り合う構成厳密解を使い、同じ初期セル状態・流束の速度上界・刻み列でCT/GLMを比較します。 Orszag–Tang：条件を揃えたCT・GLMと独立参照の収束: 同じOT初期セル平均と同じdt列でCT/GLMを計算し、別に実行したAthena++の格子・時間感度を分離した参照と比較します。 CTの初期制約保持とGLMの能動的cleaning：非物理診断対照: 故意にdiv B≠0とした同じcell磁場で、CTが初期違反を除去しないこととGLMのB/ψ応答を確認します。物理問題数へ加算しない診断対照です。","en":"Orszag–Tang: CT, GLM and independent Athena++: Compare CT and GLM density, magnetic field, conservation and div B for the same periodic Orszag–Tang data, against separately executed Athena++. CT and GLM: mesh/time convergence of a moving magnetostatic equilibrium: Use a constructed exact equilibrium with nonzero magnetic force balanced by a pressure gradient, matching CT/GLM initial cell states, flux speed bound and time-step sequence. Orszag–Tang: matched CT/GLM and converged independent references: Run CT/GLM with the same OT initial cell averages and dt sequence, comparing with separately executed Athena++ references whose mesh/time sensitivities are separated. Initial-constraint preservation by CT and active GLM cleaning: nonphysical control: Intentionally begin with the same non-solenoidal cell B, checking that CT does not remove the initial defect and calibrating GLM’s B/psi response. This diagnostic adds no physical problem."},"depth_previous_status":"educational-example"},"p1-fem":{},"cg":{},"ale":{},"upwind":{"depth_release":{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]},"depth_scope":{"ja":"追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."}},"rk4":{"depth_release":{"group":"models","edition":"2026-11-22","case_ids":["reaction-diffusion-fourier","turing-schnakenberg","fitzhugh-nagumo"]},"depth_additional_releases":[{"group":"weno-critical","edition":"2026-11-23","case_ids":["weno-critical-epsilon"]}],"depth_scope":{"ja":"反応拡散：空間2次と時間4次を分けて測る: 線形の拡散・反応演算子を、連続と半離散のFourier厳密解を用いて小規模に検証します。 Turing不安定性：線形成長率と小振幅パターン: Schnakenberg型反応拡散で、一様平衡の安定性と拡散による選択モードの成長を行列指数で検証します。 FitzHugh–Nagumo：パルス興奮・回復と独立ODE参照: 2変数の膜興奮縮約ODEを電流パルスで励起し、DOP853との全出力時刻の誤差・時間収束・回復を確認します。 セル平均からのWENO-JS／Z二乗重みの臨界点再構成と、実際の周期スカラー輸送を比較します。εの違い、解析セル平均と点値、空間誤差と時間刻みの影響を分けます。","en":"Reaction-diffusion: separate second-order space and fourth-order time: Validate a small linear diffusion-reaction operator against continuous and semidiscrete Fourier solutions. Turing instability: linear growth and small-amplitude patterns: Use a matrix exponential to validate stable homogeneous kinetics and diffusion-driven growth of a selected Schnakenberg mode. FitzHugh-Nagumo: pulse excitation, recovery and an independent ODE reference: Excite a two-variable reduced membrane ODE with a current pulse; check all-output-time errors, temporal refinement and recovery against DOP853. Compare critical-point reconstruction from cell means using WENO-JS/Z power-two weights and actual periodic scalar transport. Separate epsilon choices, analytic cell means versus point values, and spatial error versus time-step effects."},"depth_previous_status":"educational-example"},"hll":{"depth_release":{"group":"double-mach","edition":"2026-11-23","case_ids":["double-mach-reflection"]},"depth_additional_releases":[{"group":"forward-step","edition":"2026-11-23","case_ids":["forward-step-m3"]},{"group":"guderley","edition":"2026-11-23-r3","case_ids":["guderley-implosion"]},{"group":"shallow-water","edition":"2026-11-23","case_ids":["swashes-topography","dry-bed-dam-break"]}],"depth_scope":{"ja":"既存のHLL流束・Heunによる2D Double Mach反射を3格子で検証し、別実装の有限格子数値参照との差、境界流束収支、衝撃位置と未解像の壁近傍構造を示します。 追加の前向きステップ例は段差面を含む反射壁境界の実2D有限体積計算を検証します。 追加のGuderley例は、圧力ゼロの上流へ進む球対称収束衝撃波を原点到達前だけ計算し、半解析的な相似参照と比較します。 浅水系の地形源項と静水再構成を、全湿潤・露出床の静止湖とSWASHESの定常Bernoulli流で検査します。別の平坦床Ritter破堤は、真の乾燥状態・保存収支・固定水深の前縁を確認します。","en":"Three-grid 2D Double Mach verification using HLL and Heun compares a separately written finite-grid numerical reference, boundary-flux budgets, shock position and unresolved near-wall structure. The additional forward-step example verifies actual 2D finite-volume flow with reflecting walls including the step faces. The additional Guderley example evolves a zero-upstream-pressure spherical converging shock only before collapse and compares a semi-analytic similarity reference. Check shallow-water bed sources and hydrostatic reconstruction with wet/emerged lakes and a SWASHES steady Bernoulli flow. A separate flat-bed Ritter dam break tests genuinely dry states, conservation budgets and a fixed-depth front."},"depth_previous_status":"educational-example"},"minmod":{"depth_release":{"group":"noh","edition":"2026-11-23-r5","case_ids":["noh-shock"]},"depth_additional_releases":[{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"このNoh配布の球対称系列で、保存量のMUSCL型再構築の傾きをminmodで制限します。平面・円筒は区分定数のままです。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"Minmod limits conserved-variable MUSCL slopes in this Noh edition's spherical series. Planar/cylindrical runs retain piecewise-constant states. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"ssprk33":{"depth_release":{"group":"low-mach","edition":"2026-11-23","case_ids":["low-mach-vortex"]},"depth_additional_releases":[{"group":"euler-positivity","edition":"2026-11-23-r2","case_ids":["euler-double-rarefaction-positivity"]},{"group":"zalesak","edition":"2026-11-23","case_ids":["zalesak-rotation"]}],"depth_scope":{"ja":"背景Mach数.1/.01の滑らかな2D Euler等エントロピー渦で、両流束に無制限の中心primitive MUSCL再構築を用い、通常RoeとMiczek系の数値散逸行列前処理D=P⁻¹|PA|を比較します。SSPRK(3,3)で元の物理時間項と音響CFLを保ち、速度誤差・動圧規格化した圧力誤差・周期保存収支・標本Fourier診断を分けて評価します。擬似時間・二重時間積分の定常加速や、勾配制限・TVDの保証は扱いません。 追加の二重膨張波は1次元保存量MUSCL・共有Lax–Friedrichs流束・平均を保つ正値状態スケーリング・SSPRK(3,3)を接続した限定例です。許容CFLと波速条件、各前進Euler候補・SSP段の平均と面状態、保存収支を測り、一般のEuler・WENO・DG・MHDの正値性保証へ拡張しません。 追加のZalesak型例は与えた発散ゼロ速度による2次元スカラー回転輸送です。同一の周期格子・SSPRK(3,3)で一次風上とminmod MUSCLを比較し、各段の範囲・保存量と一回転後の形状誤差を調べます。FCT法や多次元Euler全般の有界性を認証しません。","en":"A fixed smooth 2D Euler isentropic vortex at background Mach numbers .1 and .01 compares ordinary Roe and Miczek-type dissipation-matrix preconditioning D=P⁻¹|PA|, with unlimited central primitive-variable MUSCL reconstruction for both. SSPRK(3,3) retains physical time and the acoustic CFL. Velocity error, dynamically normalized pressure error, periodic conservation and sampled Fourier diagnostics are evaluated separately. Pseudo-time or dual-time steady acceleration, slope limiting and TVD guarantees remain outside this example. The additional double rarefaction connects one-dimensional conservative MUSCL, shared Lax–Friedrichs fluxes, mean-preserving positive-state scaling and SSPRK(3,3). Check the admissible CFL/wave-speed conditions, means and faces at each forward-Euler candidate/SSP stage, and conservation budgets; this does not certify general Euler, WENO, DG or MHD positivity. The additional Zalesak-type example is two-dimensional scalar rotation in a prescribed divergence-free velocity. Compare donor-cell upwinding and minmod MUSCL with the same periodic grid and SSPRK(3,3), measuring stage bounds, conservation and full-turn shape errors. It does not certify FCT or general multidimensional Euler bounds."},"depth_previous_status":"educational-example"},"dg":{}};
const batch18HistoricalMethod=method=>{if(!Object.hasOwn(batch18MethodBindings,method.id))return method;const copy={...method},old=batch18MethodBindings[method.id];for(const key of ['depth_release','depth_additional_releases','depth_scope','depth_previous_status']){if(Object.hasOwn(old,key))copy[key]=old[key];else delete copy[key];}return copy;};
const ids=['sem-poisson-2d','fr-periodic-advection'],methods=['spectral-element','flux-reconstruction'];
const baseline=json('scripts/sem-fr-baseline.json'),result=json(base+'results/result.json');

test('SEM/FR preserve the previous149 method records,24 releases,92 primary pictures and common executions',()=>{
 const rows=json('catalog/atlas-methods.json').methods;
 assert.equal(rows.length,methodCount);
 const original=rows.filter(m=>!batch48NewMethodIds.has(m.id)&&!methods.includes(m.id)&&m.id!=='q1-fem').map(projectMethodBeforeBatch48).map(projectMethodBeforeBatch38).map(batch28HistoricalMethod).map(batch18HistoricalMethod).map(m=>Object.fromEntries(Object.entries(m).filter(([k])=>!(['p1-fem','dg'].includes(m.id)&&['depth_release','depth_scope','depth_previous_status'].includes(k)))));
 assert.equal(hash(original),baseline.method_records_sha256);
 const registry=json('numerical-methods-atlas/validation/releases.json');
 assert.equal(registry.releases.length,supplementGroupCount);assert.equal(registry.case_count,supplementCaseCount);assert.equal(registry.releases.filter(r=>!['coefficient-diffusion', 'slab-ewald', 'fmm3d', 'gravity-dynamics', 'warm-pic', 'pic-spatial', 'dsmc-wall', 'dsmc-shock',...groupsAddedAfterBatch37].includes(r.group)).reduce((n,r)=>n+r.tests,0),893);
 assert.equal(hash(registry.releases.filter(r=>!['sem-fr','instability-growth','mhd-transport','mesh-boundary','moving-waves','relativistic','coefficient-diffusion','slab-ewald','fmm3d','gravity-dynamics','warm-pic','pic-spatial','dsmc-wall','dsmc-shock',...groupsAddedAfterBatch37].includes(r.group))),baseline.release_records_sha256);
 const pictures=json('numerical-methods-atlas/gallery/preview-manifest.json').items;
 assert.equal(pictures.length,problemCount);assert.equal(hash(pictures.filter(p=>!["kh-initial-growth","rt-initial-growth","lshape-fem","annular-viscous-mms","poisson-neumann","poisson-robin","ale-nonuniform-transport","cgrid-rotating-wave","srhd-collision","srmhd-alfven","checkerboard-diffusion","rotated-anisotropic-diffusion","neutral-slab-yb","fmm3d-inverse-r","gravity-kepler","gravity-plummer-short","thermal-landau-damping","thermal-two-stream","dsmc-couette","dsmc-fourier","dsmc-planar-shock",...examplesAddedAfterBatch37].includes(p.id))),baseline.primary_records_sha256);
 for(const p of pictures)assert.equal(sha(p.image.replace(/^\//,'')),p.image_sha256);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),baseline.common_registry_sha256);
});

test('the independent25-test ZIP retains original acceptance, both actual failed protocols and exact legacy baselines',()=>{
 const receipt=json(base+'verification.json');assert.equal(receipt.tests,25);assert.equal(receipt.passed,true);assert.equal(receipt.all_cases_rerun,true);
 for(const [p,h]of Object.entries(json(base+'source-manifest.json').files))assert.equal(sha(base+p),h,p);
 for(const [p,h]of Object.entries(json(base+'pre-run-contract.json').files_sha256))assert.equal(sha(base+p),h,p);
 assert.equal(sha(base+'inputs.json'),sha(base+'inputs-initial.json'));
 assert.equal(sha(base+'inputs.json'),sha(base+'attempts/01-dense-exponential/source/inputs.json'));
 const history=json(base+'protocol-history.json');assert.equal(history.acceptance_modified_after_first_execution,false);assert.equal(history.input_modified_after_first_execution,false);assert.equal(history.original_pytest.passed,23);assert.equal(history.original_pytest.failed,1);
 const provenance=json(base+'baseline-provenance.json');assert.equal(Object.keys(provenance.files).length,7);
 for(const [p,r]of Object.entries(provenance.files)){
  assert.equal(sha(base+p),r.sha256);assert.equal(sha(new URL(r.source_url).pathname.slice(1)),r.sha256);
 }
});

test('SEM has independently integrated errors, matched free unknowns and separate h/p refinement',()=>{
 const c=result.cases.find(c=>c.id===ids[0]);assert.ok(c.passed&&Object.values(c.checks).every(Boolean));
 const h=c.records.filter(r=>r.method==='GLL-SEM'&&r.series==='h'),p=c.records.filter(r=>r.series==='p'),fem=c.records.filter(r=>r.method==='published-P1-FEM');
 assert.deepEqual(h.map(r=>r.elements_per_axis),[2,4,8]);assert.deepEqual(h.map(r=>r.free_dofs),[9,49,225]);assert.deepEqual(fem.map(r=>r.free_dofs),[9,49,225]);assert.deepEqual(p.map(r=>r.degree),[1,2,3,4,5,6]);
 assert.ok(Math.abs(c.metrics.sem_h_l2_order-Math.log2(h[1].l2_error/h[2].l2_error))<1e-12);
 assert.ok(c.metrics.sem_h_l2_order>3&&c.metrics.p1_h_l2_order>1.9);
 assert.ok(c.metrics.p_refinement_l2_reduction>1e5);
 assert.ok(text(base+'sem.py').includes('leggauss(quadrature or p+4)'));
 assert.ok(text(base+'README.md').includes('not a runtime or universal superiority'));
});

test('FR compares the actual published DG, records every timestep mass and separates temporal error',()=>{
 const c=result.cases.find(c=>c.id===ids[1]);assert.ok(c.passed&&Object.values(c.checks).every(Boolean));assert.equal(c.records.length,6);
 assert.ok(c.metrics.maximum_fr_vs_published_dg<2e-10);assert.ok(c.metrics.maximum_stage_mass_drift<2e-12);
 for(const h of c.mass_energy_histories){
  const row=c.records.find(r=>r.degree===h.degree&&r.cells===h.cells);
  assert.equal(h.samples.length,row.steps+1);assert.equal(h.samples.at(-1).time,.25);
  for(const sample of h.samples)assert.ok(Math.abs(sample.mass-h.samples[0].mass)<=c.metrics.maximum_stage_mass_drift+1e-16);
 }
 assert.ok(c.metrics.time_error_halving_ratio>.1&&c.metrics.time_error_halving_ratio<.15);
 assert.ok(c.metrics.actual_transport_l2_change>.9);
 assert.ok(text(base+'experiments.py').includes('dg_advection(n, p,'));assert.ok(text(base+'fr.py').includes('expm_multiply(csr_matrix(time*matrix)'));
});

test('two new methods and two saved-data previews connect to existing physical problems without duplicating them',()=>{
 const rows=json('numerical-methods-atlas/methods/index.json').methods;
 for(let i=0;i<2;i++){
  const m=rows.find(m=>m.id===methods[i]);assert.equal(m.status,'educational-example');assert.deepEqual(m.execution_examples.map(e=>e.id),[ids[i]]);
  const c=json('numerical-methods-atlas/validation/'+ids[i]+'/index.json');assert.equal(c.problem_id,['poisson-2d-sine','advection-sine'][i]);
  assert.deepEqual(c.execution_navigation.equations.map(e=>e.id),[['poisson-laplace'],['linear-advection']][i]);
 }
 assert.equal(json('catalog/atlas-test-problems.json').problems.length,problemCount);
 const gallery=json('numerical-methods-atlas/gallery/index.json').items;
 for(let i=0;i<2;i++){
  const p=gallery.find(p=>p.id===['poisson-2d-sine','advection-sine'][i]);const e=p.supplemental_execution_entries.find(e=>e.id===ids[i]);
  assert.ok(e.preview.url.endsWith('/'+ids[i]+'-preview.png'));
 }
});

test('bilingual theory, software context and both searches expose the appropriate methods and executions',()=>{
 for(const lang of ['ja','en'])for(let i=0;i<2;i++){
  const c=json(`numerical-methods-atlas/${lang}/read/${methods[i]}/index.json`);
  assert.ok(c.html.includes('katex-mathml')&&!c.html.includes('math-placeholder'));
  assert.ok(c.html.includes('id="'+['fem-comparison','dg-comparison'][i]+'"'));
  assert.deepEqual(c.scoped_supplements.map(c=>c.id),[ids[i]]);
  assert.ok(text(`numerical-methods-atlas/${lang}/read/${methods[i]}/index.md`).includes('| --- |'));
  assert.ok(c.html.includes(['https://github.com/Nek5000/nekRS','https://www.pyfr.org/'][i]));
 }
 const global=makeSearch(json('search/index.json').documents),inline=json('numerical-methods-atlas/home-search-index.json');
 for(const [q,lang,id]of [['SEM Poisson 実行','ja',ids[0]],['FR periodic advection run','en',ids[1]]])for(const rows of [global(q,lang,'atlas'),searchChapters(inline,q,lang)])assert.ok(rows.some(r=>r.kind==='execution-example'&&r.url.includes('/validation/'+id+'/')),q);
 for(const [q,id]of [['SEM',methods[0]],['FR',methods[1]]])for(const rows of [global(q,'ja','atlas'),searchChapters(inline,q,'ja')])assert.ok(rows.some(r=>r.kind==='method'&&r.id===id),q);
 for(const [q,id]of [['Nek5000',methods[0]],['nekRS',methods[0]],['PyFR',methods[1]]])assert.ok(global(q,'en','atlas').some(r=>r.url.includes('/read/'+id+'/')),q);
});
