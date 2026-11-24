// Synthetic browser measurement. No scientific solver, reference or ZIP is run.
import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import os from 'node:os';
const query='Sod test';
const conditions={download_bits_per_second:1_600_000,upload_bits_per_second:750_000,latency_ms:150,cpu_slowdown_multiplier:4,viewport:{width:390,height:844},cache:'fresh context, HTTP cache disabled, service workers blocked',scope:'All page requests shaped before navigation. Synthetic Chromium on a shared Linux runner; not a physical smartphone.'};
const expectedHash=createHash('sha256').update(readFileSync(new URL('../search/atlas-query-index.json',import.meta.url))).digest('hex');

test('cold navigation and first actionable atlas search result',async({page,browser},info)=>{
 const {language,entry}=info.project.metadata;
 const client=await page.context().newCDPSession(page),errors=[],resourcesFailed=[],requestURLs=[],requestNames=new Map(),applied=new Map();
 await client.send('Network.enable');await client.send('Network.setCacheDisabled',{cacheDisabled:true});
 const {ruleIds}=await client.send('Network.emulateNetworkConditionsByRule',{matchedNetworkConditions:[{urlPattern:'',latency:conditions.latency_ms,downloadThroughput:conditions.download_bits_per_second/8,uploadThroughput:conditions.upload_bits_per_second/8,connectionType:'cellular3g'}]});
 await client.send('Emulation.setCPUThrottlingRate',{rate:conditions.cpu_slowdown_multiplier});
 client.on('Network.requestWillBeSent',e=>requestNames.set(e.requestId,e.request.url));
 client.on('Network.requestWillBeSentExtraInfo',e=>applied.set(e.requestId,e.appliedNetworkConditionsId));
 page.on('pageerror',e=>errors.push(e.message));
 page.on('requestfailed',r=>resourcesFailed.push(r.url()+': '+r.failure()?.errorText));
 page.on('request',r=>requestURLs.push(r.url()));
 page.on('response',r=>{if(r.status()>=400)resourcesFailed.push(r.status()+' '+r.url());});
 await page.addInitScript(()=>{
  const state={input:null,submit:null,json:[],longTasks:[]};window.__atlasSearchPerformance=state;
  document.addEventListener('input',()=>{state.input??=performance.now();},true);
  document.addEventListener('submit',()=>{state.submit??=performance.now();},true);
  if(PerformanceObserver.supportedEntryTypes.includes('longtask'))new PerformanceObserver(list=>{for(const x of list.getEntries())state.longTasks.push({start:x.startTime,duration:x.duration});}).observe({type:'longtask',buffered:true});
  const original=window.fetch.bind(window);
  window.fetch=(...args)=>original(...args).then(response=>{
   const path=new URL(response.url,location.href).pathname;
   if(path==='/search/atlas-query-index.json'){
    const json=response.json.bind(response);response.json=async()=>{
     const mark={path,start:performance.now(),end:null};state.json.push(mark);
     try{return await json();}finally{mark.end=performance.now();}
    };
   }
   return response;
  });
 });
 const indexPromise=page.waitForResponse(r=>new URL(r.url()).pathname==='/search/atlas-query-index.json');
 const start=entry==='home'?`/numerical-methods-atlas/?lang=${language}`:`/search/?scope=atlas&lang=${language}`;
 await page.goto(start,{waitUntil:'domcontentloaded'});
 const input=page.locator(entry==='home'?'#home-search-input':'#search-query');
 await expect(input).toBeVisible();
 if(entry==='global')await expect(page.locator('#search-status')).toHaveText(language==='ja'?/公開ページ・資料/:/Search .*public pages/);
 const ready=await page.evaluate(()=>performance.now());
 expect(requestURLs.some(u=>new URL(u).pathname==='/search/atlas-query-index.json')).toBe(false);
 await input.fill(query);await input.press('Enter');
 const first=page.locator(entry==='home'?'#home-search-results > li':'#search-results > li').first().locator(entry==='home'?'a':'h2 a').first();
 await expect(first).toHaveAttribute('href','/numerical-methods-atlas/code-and-data/examples/sod/?lang='+language);
 await first.click({trial:true});
 await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
 const metric=await page.evaluate(()=>({end:performance.now(),state:window.__atlasSearchPerformance,navigation:performance.getEntriesByType('navigation')[0].toJSON(),resources:performance.getEntriesByType('resource').map(x=>x.toJSON())}));
 const indexResponse=await indexPromise,body=await indexResponse.body();
 const actualHash=createHash('sha256').update(body).digest('hex');expect(actualHash).toBe(expectedHash);
 const transfer=metric.resources.find(r=>new URL(r.name).pathname==='/search/atlas-query-index.json');
 expect(transfer.encodedBodySize).toBeGreaterThan(0);expect(transfer.decodedBodySize).toBe(body.length);
 const indexRequest=[...requestNames].find(([,u])=>new URL(u).pathname==='/search/atlas-query-index.json');
 expect(ruleIds).toContain(applied.get(indexRequest?.[0]));
 expect(['gzip','br','zstd']).toContain(indexResponse.headers()['content-encoding']);
 expect(errors).toEqual([]);expect(resourcesFailed).toEqual([]);
 expect(requestURLs.some(u=>[...new URL(u).searchParams.values()].some(value=>value.includes(query)))).toBe(false);
 expect(metric.state.input).not.toBeNull();expect(metric.state.submit).not.toBeNull();
 const jsonEnd=metric.state.json.at(-1)?.end;expect(jsonEnd).toBeGreaterThan(0);
 const source=execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim();
 const row={passed:true,source_commit:source,tested_tree:process.env.ATLAS_PERF_TREE||execFileSync('git',['write-tree'],{encoding:'utf8'}).trim(),target:process.env.ATLAS_PERF_TARGET||'candidate',language,entry,repetition:info.repeatEachIndex,query,conditions,
  measurements:{navigation_to_search_ready_ms:ready,input_to_actionable_result_ms:metric.end-metric.state.input,submit_to_actionable_result_ms:metric.end-metric.state.submit,navigation_to_actionable_result_ms:metric.end,index_transfer_ms:transfer.duration,index_encoded_bytes:transfer.encodedBodySize,index_decoded_bytes:body.length,index_response_to_json_ready_ms:Math.max(0,jsonEnd-transfer.responseEnd),json_ready_to_actionable_result_ms:metric.end-jsonEnd,search_long_task_ms:metric.state.longTasks.filter(t=>t.start>=metric.state.input).reduce((n,t)=>n+t.duration,0)},
  index_sha256:actualHash,index_content_encoding:indexResponse.headers()['content-encoding'],first_result:await first.getAttribute('href'),network_rule_ids:ruleIds,index_rule_applied:applied.get(indexRequest[0]),
  browser:browser.version(),host:{platform:os.platform(),arch:os.arch(),release:os.release(),cpus:os.cpus().length,cpu_model:os.cpus()[0]?.model,node:process.version,runner_image:process.env.ImageOS||'',runner_image_version:process.env.ImageVersion||''},
  diagnostics:metric,request_paths:requestURLs.map(u=>new URL(u).pathname),
  caveats:['Three repetitions per language/entry; report min/median/max, not a stable tail percentile.','Test-only fetch timing and long-task observers add instrumentation overhead. Response-to-JSON and JSON-to-actionable are combined phases, not an independent solver or exact CPU/decompression profile.','Candidate uses a loopback gzip fixture; published target uses the actual HR CDN. HTTP-cache cold does not mean a cold operating-system disk cache.']};
 await writeFile(info.outputPath('sample.json'),JSON.stringify(row,null,2)+'\n');
 await client.detach();
});
