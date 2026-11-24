# Current R4 scientific outcome: lbm-curved-boundary

Primarylocalattempt passed28pytest(no skip),2fixedphysicalruns and33/33originalcasegates; compileincludedsharedtime37.777063s. Thisprimaryoutcomebindstheexactpre-rasterizationcontractpreservedin`presentation-history/pre-rasterization-contract.json`. Onlypcolormeshartist rasterizationforSVG/PDF andthisoutcomeprosechangedafterward; allphysics/test/input/criteria remainbyteidentical. CanonicalZIPverificationmustbeassessedfromitsactualverification.json; noindependentZIPpassispredictedhere.

日本語: 固定主計算は28テスト・2計算・33判定すべて合格しました。コンパイルを含む共有実測時間は37.777063秒です。合格時の元plot/契約を正確に保持し、以後の変更は図のメッシュartistのラスター化と結果説明だけです。元の失敗と同じ科学公差を保持しています。公開ZIPの独立再実行は実際のverification.jsonで確認してください。

# R4 fixed organization: lbm-curved-boundary

Currentcase: `lbm-cylinder-re20`. ThepreviousTWO-caseR3mainfinished112/113andremainsFAILED. Itsactualcylinder33/33passdoesnotupgradeannularpressure. RootfixedN80/160/240forBOTHannularvariantsatunchangedUi.02/tau.7/nu.01/T4/fullpointwisepcriterion.08. New160/240geometry/one-stepqualificationpassed29/29in3.692724s,all12bindingsunchanged. Rawcombinedplanningprojection90.2825s exceedstheprefixedapproximately85sorganizationthreshold,sothisR4SPLITSannulus/cylinderintotwoseparatelyrunnablegroupswithidenticalcaseIDs/solver/criteria. Eachhas28pytestandownshared120s,compilerincluded. THISR4mainisunexecutedatfreeze.

日本語: 格子以外の物理条件・誤差条件を変えず、円環と円柱の配布単位だけを分離します。旧主計算の失敗・全点圧力未達を保持し、新計算の実行前に契約を凍結します。旧全配列は私用永続領域へ保持し、公開履歴は正確な全文テキストの重複排除と明示的SHA対応表です。公開ZIPに旧NPZまで含むとは主張しません。現行ケースの新NPZ/CSVは全保存します。

## Retained R3 design chronology (historical, not current group inventory)

# Curved D2Q9 BGK: fixed annulus and actual Re20 cylinder

日本語: `lbm-annular-couette-control`と`lbm-cylinder-re20`の固定した実2D計算です。R2旧主計算は、環状の全点圧力誤差.617757>.08と円柱step265の出口近傍での非正密度により不合格でした。全旧ソース・入力・公差・配列・CSV・ログ・JUnitを`history/attempt-01-linear-outlet-pressure-failure/`へ保持します。現在のR3は独立レビュー済みの2次曲面補間と全9成分NEE出口への再設計です。固定物理入力と113判定の公差は変更しません。R3主計算はこの契約時点で未実行です。

English: two actual2D cases, not a boundary-only algebra demonstration. The oldR2 main failed annular fullpointwise pressure(.617757>.08) andcylinder outlet-adjacent density atstep265. Fullold source/results/logs are retained under`history/attempt-01-linear-outlet-pressure-failure/`. R3 adopts separately qualified quadraticcurved links andanall-nine poststream NEEoutlet; fixedphysicalinputs andall113criteria remainunchanged. R3main is unexecuted atthis freeze. Actual result and independentZIP rerun receipts, not this prose, determine success.

## Execution / 実行

Python3.12; exactly numpy2.0.2,scipy1.14.1,pytest8.3.5; systemC++17 compiler(`c++` orCXX). No binary/compiler installer is shipped. `native.py` compiles a disposable sharedlibrary underTMPDIR using`-O2 -std=c++17 -ffp-contract=off -fPIC -Wall -Wextra -Werror`, nofastmath. Compiler timeout15s; bothpytest compilation andmain compilation count toward anexternal shared120s. Compilerstdout/stderr/command andfailures survive. Plotting separately usesmatplotlib3.9.4 andonlysavedarrays.

```sh
python -B -W error -m pytest -q -p no:cacheprovider --junitxml=FRESH_RECEIPT/tests.xml
python -B -W error run.py --input inputs.json --output FRESH_RESULTS
python plot.py --results FRESH_RESULTS/result.json --output FRESH_RESULTS
```

Plot accepts either result.json or itsdirectory. Nativeobjects/libraries aretemporary andnever enter generated science. Original22pytest bodies remain byteidentical;6additive tests qualify quadratic/NEE paths, giving28pytest total.8main evolutions(6annulus+2cylinder),80+33=113casegates are fixedbefore rerun.

## Fixed physical problem / 固定物理問題

Annulus: Rin.2,Rout.4,center(.5,.5),Ui.02,outerwall0,nu.01;N80/160/240,tau.7,dt=(20/3)/N²,T4,3840/15360/34560integersteps. Quadraticcircle versus stair-halfway produces6runs. Analytic utheta=Ar+B/r and radialNSpressure/traction are independently qualified by7Cartesian/radial identities. Pressure is compared atEVERYfluidnode after aconstantgauge removal; no radialaverage,fit,rescaling orsample selection. Finest velocity.03,pointwisepressure.08,torque relative.05; alsofixedstationarity,refinement andledger gates.

Cylinder: originalSchäfer–Turek2D-1fullchannel[0,2.2]x[0,.41],circle(.2,.2),R.05,nu.001,rho1,meanU.2,peak.3,Re20. dx.01/.005,xwet221/441,yhalfway41/82,dt=dx/6,T30,18000/36000steps; late26/28/30. ParabolicZou–Heinlet,stationaryhalfwaychannelwalls,truecirclequadraticlinks; outletall9poststreamNEEwithdensity1andadjacentpoststreamvelocity. Initial straightPoiseuille pressuregradient is astartupguess,never aninteriorreset orcylinderreference. Normalizeforce by2/(rho*meanU²D). CD/CL/dp/La distance fromoriginalTable3estimatedranges has separatefrozen coarseLBMtolerances5%/.01/10%/.025; notrigorousenclosures. Ma,stationarity andtwogrid differences remainrequired.

Originalchapterprinted3/7allows choosingoutflow; adoptedfinite NEEreservoir differs fromlaterFEATflowdo-nothing. No borrowed exactNabhtruth or exactauthorNEEimplementation claim. Theannulus doesnot complete thecylindercase.

## Boundary derivation and honest source scope / 境界式・閲読範囲

`boundary-repair-DERIVATION.md` derivesbothqbranches onthereflectedcharacteristic. Shortq usesoutgoingatx,x−c,x−2c; longq usesoutgoingatx andincomingpostcollisionatx,x−c;exactq=.5reduceshalfway. Movingwall signs/coefficients satisfyuniformtangentialequilibrium. NegativeLagrangecoefficients preclude generalpositivity/unconditionalstability. Actualfixed5geometries passed neighborenumeration; missingneighbors explicitlyfail,withnofallback/floor.

Atoutletafterstream/walls/inlet, usefeq(1,ua)+fa−feq(rhoa,ua) forall9directions. Openledger accountsdelta versus already-streamed populations,includingtheknown6; lostoutgoing3alreadyenteredstreamledger. Fulloutletnodesowncornerclosure; adjacentinteriorretainswallclosure. Interpolationmaychangenetmass; actualwallmass isreportedseparately fromledgerclosure.

Lallemand/Luo2003selectedoriginaltext sec3printed410–414 Eq12–15 wasreadvia disclosedmirror; no localPDF/rendered-symbol audit. OfficialGuo/Zheng/Shi2002abstract wasread;fullprimaryequationsunavailable,soourpoststreamNEEvariantisindependentlyderived.2001BFLfulltext andNabh1998originalremainunread. Noauthorcodecopied. See`cases.json`,`references/source-review.json`,and`qualification/curved-repair-87/reference-scope.json`.

## Qualification, failures and saved science / 資格・失敗・保存

Originalnativecomponent58/58passed4.183360s,distinct fromthispacketpytest/main. Newcurvedcomponent87/87passed once,2.273437sincludingcompile; all16boundfilesunchanged. IndependentgenericLagrangeoracle,degree0/1/2,qnear0/.5/1,movingwall/halfway,NEEmoments/all9ledger,cornerownership,original-linearnegativecontrols andmissingneighborguards werefixedbeforeexecution. Itsresetone-step timing isonlyaplanningprojection,notmeasuredmainorLinuxruntime. Completeprotocol/source/review/authorization/outputs areunder`qualification/curved-repair-87/`. Thesaved-onlydiagnosisunder`qualification/curved-saved-only-audit/`isnotanewtrajectoryorarepairedpressurefield.

Eachmainrun savesfullpopulations,density,velocity,linkgeometry,allstepmass/momentum/bodyforce/torqueledgers,exactstep/timeCSV anddeclaredcheckpoints. NumericCSVhasheaders,finiteuniformrows. ActivecandidateNPZ/stage/streamedCSVsurviveeach1000stepchunk; exceptionsretaincandidate,traceback andpartialcaseJSON. Allfixedcases/gates mustpass; noautomaticretry,clip,floor,endpoint extension,pressureaveraging,warning suppression orcriterionrelaxation. ActualsavedfieldssupplyPNG/SVG/PDF andpreviews onlyaftersuccess. Archivedtestsarenamed.txtwithpathmaps,sotheold22arenotcollectedagain.
