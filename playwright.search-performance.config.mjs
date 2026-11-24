import {defineConfig} from '@playwright/test';
const target=process.env.ATLAS_PERF_TARGET||'candidate';
if(!['candidate','published'].includes(target))throw Error('Unknown performance target');
export default defineConfig({
 testDir:'./performance',timeout:180_000,globalTimeout:1_500_000,expect:{timeout:120_000},
 workers:1,retries:0,repeatEach:3,forbidOnly:!!process.env.CI,
 outputDir:'test-results/search-performance/samples',
 reporter:[['list'],['json',{outputFile:'test-results/search-performance/playwright-report.json'}]],
 use:{baseURL:target==='published'?'https://hrkoyama.github.io':'http://127.0.0.1:4198',browserName:'chromium',serviceWorkers:'block',viewport:{width:390,height:844},trace:'retain-on-failure',screenshot:'only-on-failure'},
 ...(target==='candidate'?{webServer:{command:'python3 -B scripts/serve-atlas-gzip.py --port 4198',url:'http://127.0.0.1:4198/',timeout:120_000,reuseExistingServer:false,gracefulShutdown:{signal:'SIGTERM',timeout:1000}}}:{}),
 projects:['ja','en'].flatMap(language=>['home','global'].map(entry=>({name:`${language}-${entry}`,metadata:{language,entry},use:{locale:language==='ja'?'ja-JP':'en-US'}})))
});
