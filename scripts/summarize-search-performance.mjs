import {readdir,readFile,writeFile,mkdir} from 'node:fs/promises';
import path from 'node:path';
const root='test-results/search-performance';
async function samples(dir){let entries=[];try{entries=await readdir(dir,{withFileTypes:true});}catch{return [];}const rows=[];for(const x of entries){const p=path.join(dir,x.name);if(x.isDirectory())rows.push(...await samples(p));else if(x.name==='sample.json')rows.push(JSON.parse(await readFile(p,'utf8')));}return rows;}
const rows=await samples(path.join(root,'samples')),groups=[];
for(const language of ['ja','en'])for(const entry of ['home','global']){
 const values=rows.filter(r=>r.language===language&&r.entry===entry).sort((a,b)=>a.repetition-b.repetition),metrics={};
 for(const key of ['navigation_to_search_ready_ms','input_to_actionable_result_ms','submit_to_actionable_result_ms','navigation_to_actionable_result_ms','index_transfer_ms','json_ready_to_actionable_result_ms']){
  const a=values.map(v=>v.measurements[key]).sort((a,b)=>a-b);if(a.length)metrics[key]={min:a[0],median:a[Math.floor(a.length/2)],max:a.at(-1)};
 }
 groups.push({language,entry,samples:values.length,repetitions:values.map(v=>v.repetition),measurements:metrics});
}
let runner;try{runner=JSON.parse(await readFile(path.join(root,'playwright-report.json'),'utf8'));}catch{}
const passed=rows.length===12&&groups.every(g=>JSON.stringify(g.repetitions)==='[0,1,2]')&&rows.every(r=>r.passed)&&new Set(rows.map(r=>r.source_commit)).size===1&&new Set(rows.map(r=>r.tested_tree)).size===1&&runner?.stats.expected===12&&runner?.stats.unexpected===0&&runner?.stats.flaky===0&&runner?.stats.skipped===0;
const report={passed,measured_at_utc:new Date().toISOString(),source_commit:rows[0]?.source_commit,tested_tree:rows[0]?.tested_tree,target:rows[0]?.target,conditions:rows[0]?.conditions,expected_samples:12,sample_count:rows.length,groups,samples:rows,scope:'Synthetic fixed-condition first-search timing; no numerical solvers or references rerun. Three samples do not establish a reliable p95. No arbitrary latency pass threshold.'};
await mkdir(root,{recursive:true});await writeFile(path.join(root,'summary.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({passed,sample_count:rows.length,source_commit:report.source_commit,target:report.target,groups},null,2));
if(!passed)process.exitCode=1;
