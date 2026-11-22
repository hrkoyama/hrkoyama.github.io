#!/usr/bin/env python3
"""Include the public method registry in the atlas's own search, preserving chapters."""
from pathlib import Path
import hashlib
import json
import re
from atlas_execution_discovery import load_discovery, entry_path
from atlas_search_methods import search_methods, version_method_search

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'numerical-methods-atlas'
catalog=json.loads((ROOT/'catalog/atlas-methods.json').read_text())
method_records={method['id']:method for method in search_methods(ROOT)}
path=ATLAS/'home-search-index.json';index=json.loads(path.read_text())
index['entries']=[x for x in index['entries'] if x.get('origin') not in {'public-method-registry','public-execution-discovery'}]
for entry in index['entries']:
    if entry['id'] in {'roadmap','keep'}:
        for lang in ['ja','en']:
            entry['headings'][lang]=json.loads((ATLAS/('content.'+lang+'.json')).read_text())[entry['id']]['headings']
def add(ident,title,keywords,routes,kind='resource'):
    index['entries'].append({'id':ident,'title':title,'headings':{'ja':[],'en':[]},'keywords':keywords,'routes':routes,'origin':'public-method-registry','kind':kind})
for x in catalog['methods']:
    review=x.get('method_review',{})
    extra=[]
    if review:
        extra=['適用条件','制約','一次文献','primary sources','applicability','assumptions',x['units'],x['units_ja'],x['boundary_conditions'],x['boundary_conditions_ja']]
        for name in ['problem','variant']:
            extra+=list(review[name].values())
        for name in ['use_when','avoid_when']:
            for values in review[name].values():extra+=values
    add('registry-'+x['id'],x['name'],list(x['name'].values())+x.get('aliases',[])+list(x['group'].values())+extra,{lang:'/numerical-methods-atlas/methods/'+x['id']+'/?lang='+lang for lang in ['ja','en']},'method')
    index['entries'][-1]['method']=method_records[x['id']]
add('public-method-map',{'ja':'手法の見取り図','en':'A map of numerical methods'},['手法 見取り図','method map','主要24手法','適用条件','条件と制約','一次文献','primary references','priority methods'],{lang:'/numerical-methods-atlas/methods/?lang='+lang for lang in ['ja','en']})
add('public-code-guide',{'ja':'コード・入力・検証を取得する','en':'Get code, inputs and verification'},['公開コード','データ','download','code edition'],{lang:'/numerical-methods-atlas/code-and-data/?lang='+lang for lang in ['ja','en']})
add('shared-execution-guide',{'ja':'代表15問題を固定入力から実行・検証する','en':'Run and validate 15 fixed-input representative problems'},['共通手順','実行方法','検証','固定入力','コード データ','再現','Barnes Hut','水素型原子','ヘリウム','reproduce','validation','execution guide','代表15問題','線形移流','Sod','Shu Osher','Poisson','Bratu','調和振動子','硬いODE','周期PM','Taylor Green','Brio Wu'],{lang:'/numerical-methods-atlas/code-and-data/?lang='+lang for lang in ['ja','en']})
add('thermostats',{'ja':'サーモスタット：温度制御と分布の比較','en':'Thermostats: temperature control and distributions'},['サーモスタット','温度制御','thermostat','NVT'],{lang:f'/numerical-methods-atlas/{lang}/read/thermostats/' for lang in ['ja','en']})
add('equation-index',{'ja':'数式から探す','en':'Browse by equation'},['数式検索','方程式の一覧','equation index','formula'],{lang:'/numerical-methods-atlas/equations/?lang='+lang for lang in ['ja','en']})
add('test-inventory',{'ja':'テスト計算の全体一覧','en':'Atlas-wide test-problem inventory'},['テスト計算','検証問題','benchmark','test problems'],{lang:'/numerical-methods-atlas/test-cases/?lang='+lang for lang in ['ja','en']})
total=len(json.loads((ROOT/'catalog/atlas-test-problems.json').read_text())['problems'])
add('visual-test-index',{'ja':f'絵から探す：全{total}のテスト計算','en':f'Browse all {total} test problems by picture'},['絵から探す','画像','ギャラリー','テスト計算','visual index','gallery'],{lang:'/numerical-methods-atlas/gallery/?lang='+lang for lang in ['ja','en']})
add('quantum-chemistry-overview',{'ja':'量子化学・DFT：何を近似し、何を解くか','en':'Quantum chemistry and DFT: approximations and equations'},['量子化学','密度汎関数','電子状態','HF','DFT','Kohn–Sham','Hartree–Fock','quantum chemistry','対称群','小群','既約表現','band symmetry'],{lang:f'/numerical-methods-atlas/{lang}/read/quantum-chemistry/' for lang in ['ja','en']})
add('quantum-atoms-examples',{'ja':'水素型原子とHe：実行・検証例','en':'Hydrogenic atoms and helium: runnable validation examples'},['水素型原子','ヘリウム','He','hydrogenic','helium','LDA_X','SCF','原子 計算 コード 検証'],{lang:f'/numerical-methods-atlas/{lang}/read/quantum-atoms/' for lang in ['ja','en']})
execution_intents=['実行','コード','入力','検証','再現','ダウンロード','run','code','execute','execution','runnable','reproduce','validation','input','download','example']
for item in load_discovery(ROOT)['examples']:
    execution=item['execution']
    identity=[item['id'],item['id'].replace('-',' '),item['problem_id'],*execution['name'].values(),*item['keywords']]
    index['entries'].append({
        'id':'execution-'+item['id'],'title':execution['name'],
        'headings':{'ja':[],'en':[]},
        'keywords':list(dict.fromkeys([*identity,*item['outcome'].values(),*execution_intents])),
        'focus_keywords':list(dict.fromkeys(identity)),
        'snippet':item['outcome'],
        'routes':{lang:entry_path(item['id'])+'?lang='+lang for lang in ['ja','en']},
        'kind':'execution-example','origin':'public-execution-discovery',
    })
index['scope']='chapter titles, section headings, model and method labels, glossary aliases, reviewed applicability conditions, and 15 individually scoped runnable execution examples'
path.write_text(json.dumps(index,ensure_ascii=False,separators=(',',':'))+'\n')
module=ATLAS/'home-search.js';text=module.read_text()
text=re.sub(r"from '../search/method-search[.]mjs(?:[?]v=[a-f0-9]+)?'", "from '../search/method-search.mjs?v="+version_method_search(ROOT)+"'", text)
marker=' // Public word-search entry\n'
if marker not in text:
    target=" const schedule=()=>"
    assert target in text
    text=text.replace(target,marker+" document.querySelectorAll('[data-atlas-word-search]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();input.focus({preventScroll:true});form.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});}));\n"+target,1)
text=re.sub(r"new URL\('home-search-index[.]json(?:[?]v=[a-f0-9]+)?',import.meta.url\)","new URL('home-search-index.json?v="+hashlib.sha256(path.read_bytes()).hexdigest()[:12]+"',import.meta.url)",text)
old='score}];'
new="score,url:/^\\/numerical-methods-atlas\\/[a-z0-9/?=.-]+$/.test(entry.routes?.[locale]||'')&&!entry.routes[locale].includes('..')?entry.routes[locale]:null}];"
if old in text:text=text.replace(old,new)
assert new in text or 'findMethods(' in text,'Review upstream search result shape'
text=text.replace("a.href=readingURL(new URL('.',import.meta.url),result.id,result.locale,result.section)","a.href=result.url||readingURL(new URL('.',import.meta.url),result.id,result.locale,result.section)")
text=text.replace('該当する章がありません。','該当する項目がありません。').replace('No chapters match.','No entries match.')
text=text.replace('`${n}章が該当${n>m?`（上位${m}章を表示）`', '`${n}件が該当${n>m?`（上位${m}件を表示）`')
text=text.replace("`${n} matching chapter${n===1?'':'s'}", "`${n} matching entr${n===1?'y':'ies'}")
module.write_text(text)
# Version the changed module dependency; the purpose builder versions its parent.
overview=ATLAS/'home-overview.js';text=overview.read_text()
text=re.sub(r"from './home-search[.]js(?:[?]v=[a-f0-9]+)?'","from './home-search.js?v="+hashlib.sha256(module.read_bytes()).hexdigest()[:12]+"'",text)
overview.write_text(text)
print('Built atlas-local search:',len(index['entries']),'chapter/resource entries.')
