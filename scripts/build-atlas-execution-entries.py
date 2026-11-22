#!/usr/bin/env python3
"""Publish stable human/AI entry pages without modifying scientific recipes."""
from pathlib import Path
import hashlib
import html
import importlib.util
import json
import re
import xml.etree.ElementTree as ET
from atlas_execution_discovery import (ROOT,ORIGIN,ENTRY_BASE,REGISTRY_URL,
    load_discovery,public_discovery,entry_path,entry_url)

spec=importlib.util.spec_from_file_location('execution_guide',ROOT/'scripts/build-atlas-execution-guide.py')
guide=importlib.util.module_from_spec(spec);spec.loader.exec_module(guide)
ESC=html.escape

def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value)

def json_text(data):return json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
def link(url,label):return '<a href="'+ESC(url,quote=True)+'">'+ESC(label)+'</a>'

def document(url,title,description,sections):
    head='<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    head+='<title data-page-title-ja="'+ESC(title['ja'],quote=True)+'" data-page-title-en="'+ESC(title['en'],quote=True)+'">'+ESC(title['ja'])+'</title>'
    head+='<meta name="description" data-description-ja="'+ESC(description['ja'],quote=True)+'" data-description-en="'+ESC(description['en'],quote=True)+'" content="'+ESC(description['ja'],quote=True)+'"><link rel="canonical" href="'+ORIGIN+url+'">'
    for name in ['atlas-resources','atlas-execution','atlas-discovery']:
        digest=hashlib.sha256((ROOT/'styles'/f'{name}.css').read_bytes()).hexdigest()[:12]
        head+='<link rel="stylesheet" href="/styles/'+name+'.css?v='+digest+'">'
    return head+'</head><body class="profile-page" data-site-language-anchors="suffix"><main id="main" class="profile-main atlas-resource-main atlas-execution-main atlas-entry-main">'+''.join(sections)+'</main></body></html>\n'

def read_result(record):
    asset=next(x for x in record['outputs'] if x['id']=='results')
    path=ROOT/asset['url'].removeprefix(ORIGIN+'/')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=asset['sha256']:raise ValueError('Changed reference result')
    return json.loads(raw)

def markdown(item,receipt_url,case):
    x=item['execution'];out='# '+x['name']['en']+' / '+x['name']['ja']+'\n\n'
    out+='Entry: '+entry_url(x['id'])+'\nRegistry: '+REGISTRY_URL+'\nSource record: '+x['id']+'\n\n'
    out+='Public-file rerun: '+('passed' if case['passed'] else 'failed')+'\nReceipt: '+receipt_url+'\n\n'
    for lang in ['ja','en']:
        out+='## '+lang+'\n\n'+item['outcome'][lang]+'\n\n'
        for field in ['scope','assumptions','units','boundaries']:
            out+='### '+field+'\n\n'+x[field][lang]+'\n\n'
        out+='### Input and run\n\nInput: '+x['inputs']['url']+'\nInput SHA-256: '+x['inputs']['sha256']+'\nZIP: '+x['release']['download']+'\nRun from: '+x['release']['archive_directory']+'\n\n```sh\n'+x['commands']['install']+'\n'+x['commands']['run']+'\n```\n\n'
        out+='### Outputs\n\n'+'\n'.join('- '+a['generated_path']+' ('+a['format']+'): '+a['url'] for a in x['outputs'])+'\n\n'
        if x.get('reference_notes'):out+=x['reference_notes'][lang]+'\n\n'
        out+='### Numerical acceptance\n\n'
        for c in [*x['checks'],*x.get('expected_failures',[])]:
            selector=c['pointer']
            if c.get('where'):selector+='; where='+json.dumps(c['where'],ensure_ascii=False,sort_keys=True)
            if c.get('field'):selector+='; field='+c['field']
            out+='- '+c['id']+' / '+c['description'][lang]+': '+selector+'; '+guide.check_condition(c)+'\n'
        if x.get('failure_scope'):out+='\n### Failure and scope\n\n'+x['failure_scope'][lang]+'\n'
        out+='\nReading: '+x['reading'][lang]+'\n\n### References\n\n'+'\n'.join('- '+r['description'][lang]+': '+r['url'] for r in x['references'])+'\n\n'
        out+='Code license: '+x['terms']['code_license']+'\nContent/data terms: '+x['terms']['content_and_data']+'\n'+x['terms']['scope'][lang]+'\n\n'
    return out.rstrip()+'\n'

def build():
    data=load_discovery(ROOT);public=public_discovery(data)
    execution=json.loads((ROOT/'catalog/atlas-execution-examples.json').read_text())
    receipt_url=execution['verification_receipt'].removesuffix('.json')+'-public.json'
    receipt=json.loads((ROOT/receipt_url.removeprefix(ORIGIN+'/')).read_text())
    guide.validate_receipt(receipt,execution,ROOT)
    if receipt['registry_source_mode']!='public-registry' or not receipt['passed']:raise ValueError('Require a successful public-registry rerun')
    case_records={x['id']:x for x in receipt['examples']}
    for item in data['examples']:
        x=item['execution'];ident=x['id'];case=case_records[ident];sections=[]
        for lang in ['ja','en']:
            ja=lang=='ja'
            body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">'+('固定入力から実行・検証' if ja else 'FIXED INPUT · EXECUTION · VALIDATION')+'</p>'
            body+='<nav class="resource-nav">'+link(ENTRY_BASE+'?lang='+lang,'19問題から選ぶ' if ja else 'Choose among 19 problems')+link('/numerical-methods-atlas/?lang='+lang,'アトラスの冒頭' if ja else 'Atlas home')+'</nav>'
            example=guide.render_example(x,read_result(x),lang,heading_level=1)
            intro='<p class="intro execution-outcome">'+ESC(item['outcome'][lang])+'</p><nav class="resource-nav entry-actions">'+link(x['inputs']['url'],'固定入力 / JSON' if ja else 'Fixed input / JSON')+link(x['release']['download'],'対応するコード / ZIP' if ja else 'Code edition / ZIP')+link('/numerical-methods-atlas/code-and-data/?lang='+lang+'#execution-steps-'+lang,'環境準備と共通手順' if ja else 'Setup and common steps')+'</nav>'
            example=example.replace('</h1>','</h1>'+intro,1)
            example=example.replace('<details class="execution-validation">','<details class="execution-validation" open>',1)
            body+=example
            state='合格' if case['passed'] else '未達'
            body+='<aside class="entry-verification"><h2>'+('公開ファイルからの確認' if ja else 'Checked using the public files')+'</h2><p>'+('この例の再実行：'+state if ja else 'This example rerun: '+('passed' if case['passed'] else 'failed'))+'</p><p>'+link(receipt_url,'入力・環境・時間・合否の記録 / JSON' if ja else 'Inputs, environment, timing and decisions / JSON')+'</p><p>'+('数値判定はこの固定条件を対象とします。原子2例は同じ1回の実行を共有します。' if ja else 'Numerical acceptance applies to these fixed conditions. The two atomic examples share one execution.')+'</p></aside>'
            body+='<nav class="resource-nav">'+link('index.json','この例の台帳 / JSON' if ja else 'This example record / JSON')+link('index.md','Markdown')+link('/numerical-methods-atlas/equations/?lang='+lang,'数式から探す' if ja else 'Browse formulas')+link('/numerical-methods-atlas/gallery/?lang='+lang+'#'+x['problem_id']+'-'+lang,'保存図を探す' if ja else 'Find its saved illustration')+link('/numerical-methods-atlas/code-and-data/ci/?lang='+lang,'Linuxの継続検証' if ja else 'Linux verification CI')+'</nav></section>'
            sections.append(body)
        title={lang:x['name'][lang]+(' | 実行・検証例' if lang=='ja' else ' | Runnable example') for lang in ['ja','en']}
        description={lang:item['outcome'][lang] for lang in ['ja','en']}
        dest=ROOT/entry_path(ident).lstrip('/')
        write(dest/'index.html',document(entry_path(ident),title,description,sections))
        record={**x,'url':entry_url(ident),'entry':{lang:entry_url(ident,lang) for lang in ['ja','en']},'registry_url':REGISTRY_URL,
                'registry_sha256':data['registry_sha256'],'discovery':{k:v for k,v in item.items() if k!='execution'},
                'public_rerun':{'passed':case['passed'],'receipt':receipt_url,'execution_group':x['execution_group']}}
        write(dest/'index.json',json_text(record));write(dest/'index.md',markdown(item,receipt_url,case))
    parent=ROOT/ENTRY_BASE.lstrip('/');sections=[]
    for lang in ['ja','en']:
        ja=lang=='ja'
        body='<section data-site-language="'+lang+'" lang="'+lang+'"><p class="eyebrow">19 FIXED-INPUT EXAMPLES</p><h1>'+('何を確かめるか、問題から選ぶ' if ja else 'Choose the result you want to check')+'</h1><p class="intro">'+('入力を取得し、計算し、結果を判定する15の入口です。各例で使える条件と確かめられる量を確認できます。' if ja else 'Fifteen paths from fixed input to computation and numerical decisions. Each example states its conditions and what you can check.')+'</p><nav class="resource-nav">'+link('/numerical-methods-atlas/?lang='+lang,'文字で探す' if ja else 'Search by words')+link('/numerical-methods-atlas/equations/?lang='+lang,'数式から探す' if ja else 'Browse by formula')+link('/numerical-methods-atlas/gallery/?lang='+lang,'絵から探す' if ja else 'Browse by picture')+link('/numerical-methods-atlas/code-and-data/?lang='+lang,'共通手順と全実行記録' if ja else 'Common steps and execution records')+link('/numerical-methods-atlas/code-and-data/ci/?lang='+lang,'Linuxの継続検証' if ja else 'Linux verification CI')+'</nav><ul class="execution-entry-index">'
        for item in data['examples']:
            x=item['execution'];body+='<li data-entry-id="'+x['id']+'"><h2>'+link(entry_url(x['id'],lang),x['name'][lang])+'</h2><p>'+ESC(item['outcome'][lang])+'</p>'+link(entry_url(x['id'],lang),'入力・実行・判定へ →' if ja else 'Input, execution and checks →')+'</li>'
        body+='</ul><p>'+link('index.json','19例の入口台帳 / JSON' if ja else 'Discovery records for 19 examples / JSON')+' · '+link(REGISTRY_URL,'実行条件の正本 / JSON' if ja else 'Authoritative execution conditions / JSON')+'</p></section>'
        sections.append(body)
    title={'ja':'代表19問題の実行・検証例 | 数値計算法アトラス','en':'19 runnable verification examples | Numerical Methods Atlas'}
    write(parent/'index.html',document(ENTRY_BASE,title,data['scope'],sections));write(parent/'index.json',json_text(public))
    path=ROOT/'numerical-methods-atlas/sitemap.xml';xml=ET.parse(path);node=xml.getroot();ns='{http://www.sitemaps.org/schemas/sitemap/0.9}';known={x.text for x in node.findall('.//{*}loc')}
    for url in [ORIGIN+ENTRY_BASE,*[entry_url(x['id']) for x in data['examples']]]:
        if url not in known:ET.SubElement(ET.SubElement(node,ns+'url'),ns+'loc').text=url
    ET.register_namespace('',ns[1:-1]);xml.write(path,encoding='utf-8',xml_declaration=True)
    path=ROOT/'llms.txt';text=re.sub(r'^- \[Execution example entry pages\].*\n?','',path.read_text(),flags=re.M)
    path.write_text(text.rstrip()+'\n- [Execution example entry pages]('+ORIGIN+ENTRY_BASE+'): 19 stable bilingual pages, each with fixed input, versioned code, acceptance criteria, failure scope and a public-file rerun receipt. Each has index.json and index.md; the discovery index is '+ORIGIN+ENTRY_BASE+'index.json. Navigation metadata preserves the original execution registry and its receipt hash.\n')
    print('Built19 stable execution pages, their HTML/JSON/Markdown and discovery index.')

if __name__=='__main__':build()
