#!/usr/bin/env node
/** Render the same area map for static fallback without a DOM or browser state. */
import {readFileSync} from 'node:fs';
import {configureLocale} from '../numerical-methods-atlas/i18n.js';
import {renderHomeMap} from '../numerical-methods-atlas/home-overview.js';

const messages=JSON.parse(readFileSync(new URL('../numerical-methods-atlas/locales/messages.json',import.meta.url),'utf8'));
const selected=process.argv[2]||'foundations';
const maps={};
for(const lang of ['ja','en']){
 configureLocale(messages,lang);
 maps[lang]=renderHomeMap(selected,lang,{staticMode:true});
}
process.stdout.write(JSON.stringify(maps)+'\n');
