#!/usr/bin/env python 3
"""Rebuild local search from published readings and current public registries."""
from pathlib import Path
from compact_search import write_compact
from atlas_search_methods import version_search_engine
from html.parser import HTMLParser
from urllib.parse import urlsplit
import hashlib
import json
import re
from atlas_execution_discovery import load_discovery, entry_path
from atlas_search_methods import search_methods, version_method_search, version_navigation_imports
from atlas_goal_availability import load_supplemental_examples

ROOT=Path(__file__).resolve().parents[1]


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.is_file() else default


def plain(text):
    return re.sub(r'\s+', ' ', text).strip()


class PublishedText(HTMLParser):
    """Read visible main content, excluding site chrome and reading sidebars."""
    voids = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    blocked_tags = {'script', 'style', 'noscript', 'nav', 'footer', 'button', 'input', 'textarea', 'select', 'option', 'svg', 'canvas', 'template', 'annotation', 'annotation-xml'}
    boundaries = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'section', 'article', 'br', 'div'}

    def __init__(self, language):
        super().__init__(convert_charrefs=True)
        self.language = language
        self.stack = []
        self.parts = []
        self.title = ''
        self.headings = []
        self.heading = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        parent = self.stack[-1] if self.stack else ('', False, False)
        inside = parent[1] or tag == 'main'
        classes = set(attrs.get('class', '').split())
        blocked = (parent[2] or tag in self.blocked_tags or
                   bool(classes & {'site-chrome', 'reading-nav', 'chapter-toc', 'search-navigation',
                                   'execution-resource-navigation', 'method-route-navigation', 'problem-routes'}) or
                   'hidden' in attrs or attrs.get('aria-hidden') == 'true' or
                   attrs.get('data-site-language', self.language) != self.language)
        if tag not in self.voids:
            self.stack.append((tag, inside, blocked))
        if inside and not blocked:
            if tag in self.boundaries:
                self.parts.append(' ')
            if re.fullmatch(r'h[1-6]', tag):
                self.heading = {'level': int(tag[1]), 'id': attrs.get('id', ''), 'parts': []}

    def handle_endtag(self, tag):
        if self.heading and tag == 'h' + str(self.heading['level']):
            title = plain(''.join(self.heading['parts']))
            if self.heading['level'] == 1 and not self.title:
                self.title = title
            elif title and self.heading['id']:
                self.headings.append({'level': self.heading['level'], 'id': self.heading['id'], 'title': title})
            self.heading = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag in self.boundaries:
            self.parts.append(' ')

    def handle_data(self, text):
        if self.stack and self.stack[-1][1] and not self.stack[-1][2]:
            self.parts.append(text)
            if self.heading:
                self.heading['parts'].append(text)


def published_page(path, language):
    parser = PublishedText(language)
    parser.feed(re.sub(r'(<\/?h)\s+([1-6])', r'\1\2', path.read_text()))
    if not parser.title:
        raise ValueError('Missing published main H1: ' + str(path))
    return {'title': parser.title, 'headings': parser.headings, 'text': plain(''.join(parser.parts))}


def chapter_metadata(root):
    """Preserve public record identities and aliases, never stored prose/titles."""
    methods = {item['id']: item for item in read_json(root/'catalog/atlas-methods.json', {'methods': []})['methods']}
    metadata = {}
    detailed = read_json(root/'catalog/atlas-detailed-reading.json', {'chapters': []})
    for chapter in detailed['chapters']:
        aliases = [alias for ident in chapter.get('methods', []) for alias in methods.get(ident, {}).get('aliases', [])]
        metadata[chapter['id']] = ('reading-'+chapter['id'], 'detailed-reading', chapter.get('keywords', [])+aliases)
    depth = read_json(root/'catalog/atlas-depth-expansion.json', {'groups': []})
    for group in depth['groups']:
        ident = 'validation-'+group['id']
        metadata[ident] = ('reading-'+ident, 'depth-examples', group.get('fields', []))
    for ident, source, origin in [
        ('h2-hf', 'atlas-h2-reading.json', 'h2-reading'),
        ('periodic-dft', 'atlas-periodic-reading.json', 'periodic-reading'),
        ('periodic-forces', 'atlas-forces-reading.json', 'forces-reading'),
    ]:
        data = read_json(root/'catalog'/source, {})
        metadata[ident] = ('reading-'+ident, origin, data.get('keywords', []))
    return metadata


def build_chapter_entries(root):
    """One record per physically published reading, independent of the old index."""
    atlas = root/'numerical-methods-atlas'
    pages = {}
    for language in ['ja', 'en']:
        for path in sorted((atlas/language/'read').glob('*/index.html')):
            ident = path.parent.name
            if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', ident):
                raise ValueError('Unsafe reading directory: ' + ident)
            pages.setdefault(ident, {})[language] = published_page(path, language)
    metadata = chapter_metadata(root)
    coverage = read_json(atlas/'coverage.json', {'items': []})['items']
    glossary = read_json(atlas/'glossary.json', {'terms': []})['terms']
    entries = []
    for ident, editions in sorted(pages.items()):
        entry_id, origin, aliases = metadata.get(ident, (ident, 'published-reading', []))
        keywords = [ident, ident.replace('-', ' '), *aliases]
        for item in coverage:
            if item.get('chapter') == ident:
                keywords += [item.get('label', ''), item.get('group', '')]
        for term in glossary:
            if term.get('chapter') == ident:
                keywords += [term.get('en', ''), term.get('ja', ''), *term.get('aliases', [])]
        if ident == 'stability':
            keywords += ['散逸', '数値散逸', '分散', '分散誤差', '位相誤差', 'ノイマン解析', 'von Neumann', 'numerical dissipation', 'numerical dispersion', 'amplitude', 'phase error']
        entries.append({
            'id': entry_id, 'chapter': ident, 'kind': 'chapter', 'origin': origin,
            'title': {language: editions.get(language, {}).get('title') for language in ['ja', 'en']},
            'headings': {language: editions.get(language, {}).get('headings', []) for language in ['ja', 'en']},
            'text': {language: edition['text'] for language, edition in editions.items()},
            'keywords': list(dict.fromkeys(value for value in keywords if value)),
            'routes': {language: f'/numerical-methods-atlas/{language}/read/{ident}/' for language in editions},
        })
    return entries


def attach_navigation(index, navigation):
    """Use explicit entity identities, never infer scientific links from prose."""
    for entry in index['entries']:
        kind = entry.get('kind')
        if kind == 'method':
            key = 'method:' + entry['method']['id']
        elif kind == 'chapter':
            key = 'chapter:' + entry['chapter']
            if key not in navigation['nodes']:
                continue
        elif kind == 'problem':
            key = 'problem:' + entry['id'].removeprefix('problem-')
        elif kind == 'execution-example':
            ident = entry['id'].removeprefix('execution-').removeprefix('supplement-')
            key = 'execution:' + ident
        elif kind in {'equation', 'reference'}:
            key = kind + ':' + entry['id'].removeprefix(kind + '-')
        else:
            continue
        entry['search_navigation'] = navigation['nodes'][key]
    index['navigation_source_sha256'] = navigation['source_sha256']


def update_goal_resource_navigation(root, navigation):
    """Enrich generated scoped resources without changing the source goal catalog."""
    path = root / 'search/goals-data.mjs'
    first, newline, rest = path.read_text().partition('\n')
    prefix = 'export const goals='
    if not first.startswith(prefix) or not first.endswith(';') or not newline:
        raise ValueError('Review generated goal module format: ' + str(path))
    goals = json.loads(first[len(prefix):-1])
    for goal in goals:
        for resource in goal.get('resources', []):
            resource['search_navigation_by_goal'] = navigation['method_goals'].get(resource['id'], {})
    path.write_text(prefix + json.dumps(goals, ensure_ascii=False, separators=(',', ':')) + ';\n' + rest)


def main(root=ROOT, navigation=None):
    global ROOT, ATLAS
    ROOT = Path(root)
    ATLAS = ROOT/'numerical-methods-atlas'
    if navigation is None:
        from atlas_search_routes import load_search_routes
        navigation = load_search_routes(ROOT)
    catalog=json.loads((ROOT/'catalog/atlas-methods.json').read_text())
    method_records={method['id']:method for method in search_methods(ROOT, navigation)}
    path=ATLAS/'home-search-index.json'
    index={'version':1,'entries':build_chapter_entries(ROOT)}
    page_cache={}
    def add(ident,title,keywords,routes,kind='resource'):
        entry={'id':ident,'title':title,'headings':{'ja':[],'en':[]},'keywords':keywords,'routes':routes,'origin':'public-problem-registry' if kind=='problem' else 'public-method-registry','kind':kind}
        if kind in {'resource','problem'}:
            # Resource names and prose also follow their current public pages.
            entry['keywords']=list(dict.fromkeys([*keywords,*title.values()]))
            editions={}
            for language,route in routes.items():
                pathname=urlsplit(route).path
                local=ROOT/pathname.lstrip('/')/'index.html'
                if not local.is_file():continue
                key=(local,language)
                if key not in page_cache:page_cache[key]=published_page(local,language)
                editions[language]=page_cache[key]
            if not editions:return
            entry['title']={language:editions.get(language,{}).get('title') for language in ['ja','en']}
            entry['headings']={language:editions.get(language,{}).get('headings',[]) for language in ['ja','en']}
            entry['text']={language:edition['text'] for language,edition in editions.items()}
            entry['routes']={language:routes[language] for language in editions}
        index['entries'].append(entry)
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
    add('shared-execution-guide',{'ja':'代表22問題を固定入力から実行・検証する','en':'Run and validate 22 fixed-input representative problems'},['共通手順','実行方法','検証','固定入力','コード データ','再現','Barnes Hut','水素型原子','ヘリウム','reproduce','validation','execution guide','代表22問題','線形移流','Sod','Shu Osher','Poisson','Bratu','調和振動子','硬いODE','周期PM','Taylor Green','Brio Wu'],{lang:'/numerical-methods-atlas/code-and-data/?lang='+lang for lang in ['ja','en']})
    add('equation-index',{'ja':'数式から探す','en':'Browse by equation'},['数式検索','方程式の一覧','equation index','formula'],{lang:'/numerical-methods-atlas/equations/?lang='+lang for lang in ['ja','en']})
    add('test-inventory',{'ja':'テスト計算の全体一覧','en':'Atlas-wide test-problem inventory'},['テスト計算','検証問題','benchmark','test problems'],{lang:'/numerical-methods-atlas/test-cases/?lang='+lang for lang in ['ja','en']})
    total=len(json.loads((ROOT/'catalog/atlas-test-problems.json').read_text())['problems'])
    add('visual-test-index',{'ja':f'絵から探す：全{total}のテスト計算','en':f'Browse all {total} test problems by picture'},['絵から探す','画像','ギャラリー','テスト計算','visual index','gallery'],{lang:'/numerical-methods-atlas/gallery/?lang='+lang for lang in ['ja','en']})
    # Problem identities and evidence come from the generated reviewed registry;
    # searchable titles, headings and prose come from the actual hub pages.
    for problem in read_json(ATLAS/'problems/index.json', {'problems': []})['problems']:
        keywords=[problem['id'],problem['id'].replace('-',' '),*problem['name'].values(),
                  'テスト問題','方程式','厳密解','参照解','計算法','コード',
                  'test problem','equation','reference solution','code']
        keywords += [name for method in problem['methods'] for name in method['name'].values()]
        add('problem-'+problem['id'],problem['name'],keywords,
            {lang:urlsplit(problem['hub'][lang]).path+'?lang='+lang for lang in ['ja','en']},'problem')
    # Pick up newly published top-level guides without another hand-maintained list.
    indexed_paths={urlsplit(route).path for entry in index['entries'] for route in entry.get('routes',{}).values()}
    for resource in sorted(ATLAS.glob('*/index.html')):
        route='/'+resource.parent.relative_to(ROOT).as_posix()+'/'
        if route not in indexed_paths and resource.parent.name!='connections':
            add('public-resource-'+resource.parent.name,{},[resource.parent.name.replace('-',' ')],{lang:route+'?lang='+lang for lang in ['ja','en']})
    for language in ['ja','en']:
        resource=ATLAS/language/'read/index.html'
        if resource.is_file():
            route=f'/numerical-methods-atlas/{language}/read/'
            add('reading-index-'+language,{},[],{language:route})
    connections=json.loads((ROOT/'catalog/atlas-crossovers.json').read_text())
    math_families={x['id']:x for x in connections['math_families']}
    crossover_terms=['分野間','分野横断','クロスオーバー','共通数理','共通の数理','検証の違い','crossover','cross field','shared mathematics','validation differences']
    add('crossovers-overview',connections['title'],crossover_terms+list(connections['intro'].values()),{lang:'/numerical-methods-atlas/connections/?lang='+lang for lang in ['ja','en']},'connection')
    index['entries'][-1]['snippet']=connections['intro']
    for route in connections['routes']:
        keywords=[*crossover_terms,*route.get('keywords',[]),*route['summary'].values()]
        for ident in route['math_ids']:keywords+=list(math_families[ident]['name'].values())+list(math_families[ident]['summary'].values())
        for stage in route['stages']:keywords+=list(stage['title'].values())
        add('crossover-'+route['id'],route['title'],list(dict.fromkeys(keywords)),{lang:'/numerical-methods-atlas/connections/?lang='+lang+'#'+route['id']+'-'+lang for lang in ['ja','en']},'connection')
        index['entries'][-1]['snippet']=route['summary']
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
    expansion=json.loads((ROOT/'catalog/atlas-depth-expansion.json').read_text())
    supplements=load_supplemental_examples(ROOT,list(expansion['case_problem_ids']))
    case_aliases={
        'sem-poisson-2d':['SEM','spectral element','spectral-element','スペクトル要素','スペクトル要素法','Poisson','ポアソン','FEM','h refinement','p refinement'],
        'fr-periodic-advection':['FR','flux reconstruction','流束再構成','FR法','DG','周期移流','periodic advection','Radau'],
        'level-set-translation':['level set','level-set','levelset','レベルセット','界面','circle','円の移流','平行移動','translation','signed distance'],
        'level-set-rotation':['level set','level-set','levelset','レベルセット','界面','circle','円の回転','剛体回転','rigid rotation','signed distance'],

        'reaction-diffusion-splitting':['Lie Trotter','Lie-Trotter','Lie–Trotter','Strang','作用素分割','反応拡散','Schnakenberg','ストラング','リー・トロッター'],
        'gaussian-mcmc':['Metropolis Hastings','マルコフ連鎖','有効標本数','ESS','自己相関'],
        'langevin-harmonic':['BAOAB','NVT','正準分布','温度制御'],
        'reaction-diffusion-fourier':['反応拡散','diffusion reaction'],
        'turing-schnakenberg':['Turing','チューリング','Schnakenberg','パターン形成'],
        'fitzhugh-nagumo':['FHN','FitzHugh Nagumo','膜興奮','励起回復'],
    }
    for item in supplements:
        identity=[item['id'],item['id'].replace('-',' '),*item['title'].values(),*item['method_ids'],*case_aliases.get(item['id'],[])]
        index['entries'].append({
            'id':'supplement-'+item['id'],'title':item['title'],
            'headings':{'ja':[],'en':[]},
            'keywords':list(dict.fromkeys([*identity,*item['summary'].values(),*execution_intents])),
            'focus_keywords':list(dict.fromkeys(identity)),
            'snippet':item['summary'],
            'routes':{lang:item['url']+'?lang='+lang for lang in ['ja','en']},
            'kind':'execution-example','origin':'public-depth-validation',
        })
    index['entries'].extend(dict(entity) for entity in navigation['entities'])
    attach_navigation(index, navigation)
    index['scope']='Current published chapter, guide and problem-hub titles, section headings and main text; individual equation/reference identities and their own definitions; model/method identities, glossary aliases, reviewed applicability, 22 common runnable examples, '+str(len(supplements))+' separately verified supplements and cross-field routes. Navigation follows reviewed source associations, not prose mentions. Supplements do not add entries to the common execution registry.'
    (ROOT/'search/atlas-navigation.json').write_text(json.dumps(navigation,ensure_ascii=False,separators=(',',':'))+'\n')
    llms = ROOT/'llms.txt'
    marker = '- [Atlas search resource connections]('
    lines = [line for line in llms.read_text().splitlines() if not line.startswith(marker)]
    lines.append(marker+'https://hrkoyama.github.io/search/atlas-navigation.json): explicit method, equation, problem-picture, reference and execution routes for search results; purpose restrictions and original verification scopes are retained.')
    llms.write_text('\n'.join(lines)+'\n')
    path.write_text(json.dumps(index,ensure_ascii=False,separators=(',',':'))+'\n')
    compact_path = write_compact(ROOT, index, 'atlas')
    update_goal_resource_navigation(ROOT, navigation)
    module=ATLAS/'home-search.js';text=module.read_text()
    text=text.replace("[...titles,...headings.map(h=>h.title),...keys].join(' ')","[...titles,...headings.map(h=>h.title),...keys,...Object.values(entry.text||{})].join(' ')")
    text=text.replace("const locale=language==='ja'&&entry.title.ja?'ja':'en';","const locale=language==='ja'&&entry.title.ja?'ja':entry.title.en?'en':'ja';")
    text=re.sub(r"from '../search/method-search[.]mjs(?:[?]v=[a-f0-9]+)?'", "from '../search/method-search.mjs?v="+version_method_search(ROOT)+"'", text)
    text=version_navigation_imports(ROOT, text)
    text=re.sub(r"from '../search/engine[.]mjs(?:[?]v=[a-f0-9]+)?'", "from '../search/engine.mjs?v="+version_search_engine(ROOT)+"'", text)
    marker=' // Public word-search entry\n'
    if marker not in text:
        target=" const schedule=()=>"
        assert target in text
        text=text.replace(target,marker+" document.querySelectorAll('[data-atlas-word-search]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();input.focus({preventScroll:true});form.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});}));\n"+target,1)
    text=re.sub(r"new URL\('(?:home-search-index[.]json|[.][.]/search/atlas-query-index[.]json)(?:[?]v=[a-f0-9]+)?',import.meta.url\)","new URL('../search/atlas-query-index.json?v="+hashlib.sha256(compact_path.read_bytes()).hexdigest()[:12]+"',import.meta.url)",text)
    old='score}];'
    new="score,url:(/^\\/numerical-methods-atlas\\/[a-z0-9/?=.-]+$/.test(entry.routes?.[locale]||'')||entry.kind==='connection'&&/^\\/numerical-methods-atlas\\/connections\\/\\?lang=(ja|en)#(?:dft-md|reaction-transport|poisson-fields)-\\1$/.test(entry.routes?.[locale]||'')&&entry.routes[locale].startsWith('/numerical-methods-atlas/connections/?lang='+locale+'#'))&&!entry.routes[locale].includes('..')?entry.routes[locale]:null}];"
    if old in text:text=text.replace(old,new)
    assert new in text or 'findMethods(' in text or 'atlasSearch(index)' in text,'Review upstream search result shape'
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


if __name__ == '__main__':
    main()
