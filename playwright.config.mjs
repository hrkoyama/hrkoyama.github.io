import {defineConfig} from '@playwright/test';
const port=4196;
export default defineConfig({
 testDir:'./browser',
 timeout:60_000,
 globalTimeout:180_000,
 expect:{timeout:15_000},
 workers:2,
 retries:0,
 forbidOnly:!!process.env.CI,
 outputDir:'test-results/browser',
 reporter:[['list'],['json',{outputFile:'test-results/browser-report.json'}],['html',{outputFolder:'playwright-report',open:'never'}]],
 use:{baseURL:`http://127.0.0.1:${port}`,browserName:'chromium',trace:'retain-on-failure',screenshot:'only-on-failure'},
 webServer:{command:`python3 -m http.server ${port} --bind 127.0.0.1`,url:`http://127.0.0.1:${port}/`,reuseExistingServer:false,gracefulShutdown:{signal:'SIGTERM',timeout:1000}},
 projects:['ja','en'].flatMap(language=>[390,1280].map(width=>({name:`${language}-${width}`,metadata:{language},use:{viewport:{width,height:844},locale:language==='ja'?'ja-JP':'en-US'}})))
});
