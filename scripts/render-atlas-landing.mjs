#!/usr/bin/env node
/** Render the same front door without browser state, plus the relocated guides. */
import {readFileSync} from 'node:fs';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {homeOverviewPage,renderHomeGuides} from '../numerical-methods-atlas/home-overview.js';

const root=new URL('../',import.meta.url);
const messages=JSON.parse(readFileSync(new URL('numerical-methods-atlas/locales/messages.json',root),'utf8'));
const coverage=JSON.parse(readFileSync(new URL('numerical-methods-atlas/coverage.json',root),'utf8'));
const rendered={guides:{}};
for(const lang of ['ja','en']){
 configureLocale(messages,lang);
 rendered[lang]=homeOverviewPage(coverage,'foundations',{staticMode:true});
 rendered.guides[lang]=renderHomeGuides(lang);
}
process.stdout.write(JSON.stringify(rendered)+'\n');
