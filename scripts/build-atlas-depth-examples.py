#!/usr/bin/env python3
"""Build bilingual lightweight-validation readings from verified frozen results.

This program validates hashes and renders saved measurements. It executes no
scientific solver, reference generator, statistical sampler or plotter.
"""
from html import escape
from pathlib import Path
import json
import re
import struct
import subprocess
import xml.etree.ElementTree as ET

from atlas_depth_release import GROUPS, ORIGIN, depth_code_urls, digest, load_depth_group, read_json

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT/'numerical-methods-atlas'
CATALOG = '/catalog/atlas-depth-expansion.json'
INDEX = '/numerical-methods-atlas/validation/'
LANGUAGES = ('ja', 'en')


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def link(url, text):
    assert not url.lower().startswith(('javascript:', 'data:'))
    return '<a href="'+escape(url, quote=True)+'">'+escape(str(text))+'</a>'


def paragraph(text):
    return '<p>'+escape(text)+'</p>'


def localized(value, language):
    if isinstance(value, dict):
        return value[language]
    return str(value)


def scope_text(language, common_count):
    return (f'共通{common_count}実行例の台帳とは別に管理する追加検証集です。配布ZIPを独立展開し、各グループの全固定入力と検査を実行した記録を示します。設定・手法・刻み幅の違いを独立した物理問題の数には加算しません。'
            if language == 'ja' else
            f'These additional validation supplements are managed separately from the common {common_count}-example registry. Receipts cover independent ZIP extraction, tests and every fixed input within each group. Changes of settings, methods or step sizes do not add independent physical problems.')


def terms(language):
    text = ('オリジナルコードはMIT。本文・図・固定入力・数値データと第三者資料は、それぞれの利用条件に従います。'
            if language == 'ja' else
            'Original code is MIT. Text, figures, fixed inputs, numerical data and third-party material retain their separate terms.')
    return '<aside class="validation-terms">'+paragraph(text)+'<p>'+link('/LICENSING.md', 'LICENSING.md')+' · '+link('/rights/?lang='+language, '利用条件・AI方針' if language == 'ja' else 'Rights & AI policy')+'</p></aside>'


def number(value):
    if value is None:
        return '—'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (int, float)):
        return format(value, '.12g')
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
    return str(value)


def table(headers, rows, label):
    return ('<div class="validation-table" tabindex="0" role="region" aria-label="'+escape(label, quote=True)+'">'
            '<table><thead><tr>'+''.join('<th scope="col">'+escape(str(h))+'</th>' for h in headers)+
            '</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(number(v))+'</td>' for v in row)+'</tr>' for row in rows)+
            '</tbody></table></div>')


def record_tables(records, language, label):
    if isinstance(records, dict):
        return ''.join('<h4>'+escape(str(name))+'</h4>'+record_tables(value, language, label+' '+str(name))
                       for name, value in records.items())
    if not records:
        return ''
    if not isinstance(records, list):
        return table(['value'], [[records]], label)
    if not all(isinstance(row, dict) for row in records):
        return table(['index', 'value'], list(enumerate(records)), label)
    headers = list(dict.fromkeys(key for row in records for key in row))
    return table(headers, [[row.get(key) for key in headers] for row in records], label)


def chapter_route(group, language):
    return '/numerical-methods-atlas/'+language+'/read/validation-'+group+'/'


def case_route(identifier, language=None):
    return INDEX+identifier+'/'+('?lang='+language if language else '')


def document(url, title, description, body, language=None, alternates=None):
    active = language or 'ja'
    if isinstance(title, dict):
        title_html = '<title data-page-title-ja="'+escape(title['ja'], quote=True)+'" data-page-title-en="'+escape(title['en'], quote=True)+'">'+escape(title['ja'])+'</title>'
        descriptions = ' data-description-ja="'+escape(description['ja'], quote=True)+'" data-description-en="'+escape(description['en'], quote=True)+'"'
        description_text = description['ja']
    else:
        title_html = '<title>'+escape(title)+'</title>'; descriptions = ''; description_text = description
    head = ('<!doctype html><html lang="'+active+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+title_html+
            '<meta name="description"'+descriptions+' content="'+escape(description_text, quote=True)+'"><link rel="canonical" href="'+ORIGIN+url+'">')
    if alternates:
        head += ''.join('<link rel="alternate" hreflang="'+key+'" href="'+ORIGIN+value+'">' for key, value in alternates.items())
    for name in ['atlas-resources', 'atlas-validation']:
        head += '<link rel="stylesheet" href="/styles/'+name+'.css?v='+digest(ROOT/'styles'/(name+'.css'))[:12]+'">'
    head += '<link rel="stylesheet" href="/numerical-methods-atlas/vendor/katex.min.css">'
    attribute = ' data-content-language="'+language+'"' if language else ' data-site-language-anchors="suffix"'
    return head+'</head><body class="profile-page"'+attribute+'><main id="main" class="validation-main">'+body+'</main></body></html>\n'


def group_commands(data, language):
    ja = language == 'ja'
    commands = 'python -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output'
    return (paragraph(('ZIPの '+data['verification']['archive']['archive_directory']+' フォルダで実行します。このコマンドは配布版の全'+str(len(data['metadata']))+'例を実行します。新規または空の出力先を指定してください。'
                       if ja else 'Run inside '+data['verification']['archive']['archive_directory']+' from the ZIP. This command executes all '+str(len(data['metadata']))+' fixed cases in the supplement. Choose a new or empty output directory.'))+
            '<pre><code>'+escape(commands)+'</code></pre>'+paragraph('Matplotlibは保存図の任意の再描画にだけ使い、通常の科学計算には不要です。' if ja else 'Matplotlib is optional for redrawing saved figures; ordinary scientific execution does not require it.'))


def reference_html(case, language, anchor):
    ja = language == 'ja'
    result = paragraph('原著・公式資料の書誌、抄録、原文の一部、実行した公式コードなどの確認範囲を区別します。論文全文や第三者コードの一括転載・全文監査を主張しません。'
                       if ja else 'Bibliography, abstracts, selected original sections and executed official code have distinct review scopes. Full papers and third-party code are not reproduced wholesale, and no blanket full-text audit is claimed.')+'<ol class="validation-references">'
    for reference in case['references']:
        url = reference.get('url') or reference.get('source') or 'https://doi.org/'+reference['doi']
        assert url.startswith(('https://', 'http://'))
        result += '<li id="'+anchor+'-source-'+escape(reference['id'], quote=True)+'">'+link(url, reference['author']+' ('+str(reference.get('year', 'n.d.'))+'). '+reference['title'])
        if reference.get('doi'):
            result += ' · '+link('https://doi.org/'+reference['doi'], 'DOI: '+reference['doi'])
        result += paragraph(('確認範囲 / review_level: ' if ja else 'Review scope / review_level: ')+reference['review_level'])
        note = reference.get('review') or reference.get('review_note')
        if note:
            result += paragraph(localized(note, language))
        result += '</li>'
    result += '</ol>'
    if case.get('reference_implementations'):
        result += '<p>'+('独立参照の公式資料：' if ja else 'Official reference-implementation documentation: ')+' · '.join(link(url, url.rsplit('/', 1)[-1]) for url in case['reference_implementations'])+'</p>'
    return result


def render_case(case, measured, data, language, rendered, heading_level=2, commands=False, editorial_note=None):
    ja = language == 'ja'; ident = case['id']; anchor = ident if heading_level == 2 else ident+'-'+language
    level = heading_level+1
    body = '<article class="validation-case" data-validation-case="'+ident+'" id="'+anchor+'"><h'+str(heading_level)+'>'+escape(case['title'][language])+'</h'+str(heading_level)+'>'+paragraph(case['summary'][language])
    base = data['base']
    body += '<nav class="validation-actions" aria-label="'+('コード・入力・検証' if ja else 'Code, inputs and verification')+'">'+link(case_route(ident, language), '固定入力・実行入口' if ja else 'Fixed-input execution entry')+link(base+data['verification']['archive']['file'], 'コード / ZIP' if ja else 'Code / ZIP')+link(base+'inputs.json', '固定入力 / JSON' if ja else 'Fixed input / JSON')+link(base+'results/result.json', '全結果 / JSON' if ja else 'All results / JSON')+link(base+'verification.json', '独立展開の検証記録' if ja else 'Independent-extraction receipt')+'</nav>'
    fields = [('assumptions', '前提・単位・境界', 'Assumptions, units and boundaries'),
              ('algorithm', '採用した計算法', 'Adopted numerical method'),
              ('validation', '何と比較し、何を測るか', 'References and measured quantities'),
              ('limits', '確認の限界と失敗条件', 'Verification limits and failures')]
    for key, japanese, english in fields:
        body += '<h'+str(level)+' id="'+anchor+'-'+key+'">'+(japanese if ja else english)+'</h'+str(level)+'>'+paragraph(case[key][language])
        if key == 'assumptions' and editorial_note:
            body += '<aside class="validation-scope validation-editorial-note"><strong>'+('編集上の補足' if ja else 'Editorial clarification')+'</strong>'+paragraph(editorial_note[language])+'</aside>'
        if key == 'algorithm':
            formulas = case.get('formulas', case.get('equations', []))
            body += ''.join('<div class="validation-math">'+rendered['depth-'+ident+'-'+str(i)][0]+'</div>' for i in range(len(formulas)))
    body += '<h'+str(level)+' id="'+anchor+'-measurements">'+('保存した実測値と判定' if ja else 'Stored measurements and decisions')+'</h'+str(level)+'>'
    body += paragraph('表示は丸めています。合否は固定入力の元の公差と丸め前の数値で判定し、全判定が合格した保存結果だけを表示します。'
                      if ja else 'Display values are rounded. Acceptance uses original fixed-input tolerances and unrounded numbers; only stored results passing every check are presented.')
    body += table(['量 / metric', '実測値' if ja else 'Measured value'], list(measured['metrics'].items()), case['title'][language]+('：実測値' if ja else ': measurements'))
    body += table(['判定 / check', '合格' if ja else 'Passed'], list(measured['checks'].items()), case['title'][language]+('：判定' if ja else ': decisions'))
    png = (data['directory']/'results'/(ident+'.png')).read_bytes(); assert png[:8] == b'\x89PNG\r\n\x1a\n'
    width, height = struct.unpack('>II', png[16:24])
    body += '<figure><img loading="lazy" src="'+base+'results/'+ident+'.png" width="'+str(width)+'" height="'+str(height)+'" alt="'+escape(case['title'][language]+('の保存済み検証図' if ja else ': stored validation figure'), quote=True)+'"><figcaption>'+('保存結果の図です。入力・参照・判定の範囲は本文とJSONを参照してください。' if ja else 'Figure from saved results. See the text and JSON for input, reference and acceptance scope.')+'</figcaption></figure>'
    body += '<details class="validation-records"><summary>'+('全記録を表で読む' if ja else 'Read every stored record')+'</summary>'+record_tables(measured['records'], language, ident+' records')+'</details>'
    if measured.get('reference_records'):
        body += '<details class="validation-records"><summary>'+('独立参照の記録を表で読む' if ja else 'Read independent-reference records')+'</summary>'+record_tables(measured['reference_records'], language, ident+' reference records')+'</details>'
    body += '<p>'+link(case_route(ident)+'index.json', 'この例の実測値・全記録 / JSON' if ja else 'Measurements and complete records / JSON')+'</p>'
    if commands:
        body += '<h'+str(level)+'>'+('取得して再実行する' if ja else 'Download and rerun')+'</h'+str(level)+'>'+group_commands(data, language)
        body += '<details><summary>'+('コード・テストの個別ファイル' if ja else 'Individual code and test files')+'</summary><ul>'+''.join('<li>'+link(url, url.split(data['base'], 1)[-1])+'</li>' for url in depth_code_urls(data, [ident])+data['test_urls'])+'</ul></details>'
    body += '<h'+str(level)+' id="'+anchor+'-references">'+('一次文献・関連資料と確認範囲' if ja else 'Primary sources and review scope')+'</h'+str(level)+'>'+reference_html(case, language, anchor)+'</article>'
    return body


def markdown_case(case, measured, data, language, heading_level=1, editorial_note=None):
    title = case['title'][language]
    heading = '#'*heading_level
    subheading = heading+'#'
    out = heading+' '+title+'\n\n'+case['summary'][language]+'\n\n'
    for field, labels in [('assumptions', ('前提・単位・境界', 'Assumptions, units and boundaries')),
                          ('algorithm', ('採用した計算法', 'Adopted numerical method')),
                          ('validation', ('比較・検証', 'References and validation')),
                          ('limits', ('確認の限界', 'Limits'))]:
        out += subheading+' '+labels[language == 'en']+'\n\n'+case[field][language]+'\n\n'
        if field == 'assumptions' and editorial_note:
            out += '**'+('編集上の補足' if language == 'ja' else 'Editorial clarification')+'**\n\n'+editorial_note[language]+'\n\n'
        if field == 'algorithm':
            out += ''.join('$$\n'+formula+'\n$$\n\n' for formula in case.get('formulas', case.get('equations', [])))
    out += subheading+' '+('保存実測値と判定' if language == 'ja' else 'Stored measurements and decisions')+'\n\n```json\n'+json.dumps({'metrics': measured['metrics'], 'checks': measured['checks']}, ensure_ascii=False, indent=2, allow_nan=False)+'\n```\n\n'
    out += ('全recordsとreference_records：' if language == 'ja' else 'Complete records and reference_records: ')+ORIGIN+case_route(case['id'])+'index.json\n\n'
    out += subheading+' '+('取得・実行' if language == 'ja' else 'Download and run')+'\n\nZIP: '+ORIGIN+data['base']+data['verification']['archive']['file']+'\nInput: '+ORIGIN+data['base']+'inputs.json\nResults: '+ORIGIN+data['base']+'results/result.json\nReceipt: '+ORIGIN+data['base']+'verification.json\n\n```sh\npython -m pip install -r requirements.txt\npython -m pytest -q\npython run.py --input inputs.json --output output\n```\n\n'
    out += ('このコマンドは配布グループの全例を実行します。\n\n' if language == 'ja' else 'This command executes every fixed case in the distribution group.\n\n')
    out += subheading+' '+('出典と確認範囲' if language == 'ja' else 'Sources and review scope')+'\n\n'
    for reference in case['references']:
        url = reference.get('url') or reference.get('source') or 'https://doi.org/'+reference['doi']
        out += '- '+reference['author']+' ('+str(reference.get('year', 'n.d.'))+'). '+reference['title']+'. '+url+'; review_level='+reference['review_level']+'\n'
        note = reference.get('review') or reference.get('review_note')
        if note:
            out += '  '+localized(note, language)+'\n'
    return out+'\nOriginal code: MIT. Text/figures/inputs/data/third-party material: separate terms at https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.\n'


def build():
    catalog = read_json(ROOT/CATALOG.lstrip('/'))
    assert {group['id'] for group in catalog['groups']} == set(GROUPS)
    assert len(catalog['groups']) == len(GROUPS)
    for group in catalog['groups']:
        assert all(group['title'].get(language) for language in LANGUAGES)
    data = {group['id']: load_depth_group(ROOT, group['id'], catalog['edition']) for group in catalog['groups']}
    identifiers = [case['id'] for group in data.values() for case in group['metadata']]
    assert len(identifiers) == len(set(identifiers))
    registry_path = ATLAS/'code-and-data/examples.json'
    registry_hash = digest(registry_path)
    common_count = len(read_json(registry_path)['examples'])
    source_hashes = {CATALOG.lstrip('/'): digest(ROOT/CATALOG.lstrip('/'))}
    for group in data.values():
        source_hashes.update(group['source_sha256'])
    formulas = [{'id': 'depth-'+case['id']+'-'+str(i), 'formula': [formula]}
                for group in data.values() for case in group['metadata']
                for i, formula in enumerate(case.get('formulas', case.get('equations', [])))]
    rendered = json.loads(subprocess.check_output(['node', 'scripts/render-atlas-math.cjs'], cwd=ROOT,
        input=json.dumps(formulas, ensure_ascii=False).encode()))['rendered']
    documents = {language: read_json(ATLAS/('content.'+language+'.json')) for language in LANGUAGES}
    translations = read_json(ATLAS/'translation-status.json')
    public_cases, public_groups, chapter_entries = [], [], {}
    for group in catalog['groups']:
        group_id = group['id']; current = data[group_id]
        measured = {row['id']: row for row in current['results']['cases']}
        public_groups.append({**group, 'case_ids': [case['id'] for case in current['metadata']],
            'release_base': ORIGIN+current['base'], 'verification': ORIGIN+current['base']+'verification.json',
            'passed_tests': current['verification']['passed_tests'], 'independent_rerun_seconds': current['verification']['independent_rerun_seconds']})
        for case in current['metadata']:
            ident = case['id']; page_title = {language: case['title'][language]+(' | 実行・検証例' if language == 'ja' else ' | Runnable validation') for language in LANGUAGES}
            editorial_note = catalog.get('case_notes', {}).get(ident)
            public_case = {**case, 'group': group_id, 'edition': catalog['edition'], 'measured': measured[ident],
                'problem_id': catalog.get('case_problem_ids', {}).get(ident),
                'editorial_note': editorial_note,
                'url': ORIGIN+case_route(ident), 'entry': {language: ORIGIN+case_route(ident, language) for language in LANGUAGES},
                'reading': {language: ORIGIN+chapter_route(group_id, language)+'#'+ident for language in LANGUAGES},
                'release': {'base': ORIGIN+current['base'], 'archive': current['verification']['archive'],
                    'download': ORIGIN+current['base']+current['verification']['archive']['file'],
                    'manifest': ORIGIN+current['base']+'source-manifest.json', 'verification': ORIGIN+current['base']+'verification.json',
                    'results': ORIGIN+current['base']+'results/result.json', 'input': ORIGIN+current['base']+'inputs.json',
                    'code_urls': depth_code_urls(current, [ident]), 'test_urls': current['test_urls'], 'passed_tests': current['verification']['passed_tests']},
                'source_sha256': source_hashes, 'scope': {language: scope_text(language, common_count) for language in LANGUAGES}}
            public_cases.append(public_case)
            sections, markdown = [], ''
            for language in LANGUAGES:
                nav = '<nav class="validation-actions">'+link(INDEX+'?lang='+language, '追加検証の一覧' if language == 'ja' else 'Additional validation index')+link(chapter_route(group_id, language)+'#'+ident, '詳しい解説' if language == 'ja' else 'Detailed reading')+link('index.json', 'JSON')+link('index.md', 'Markdown')+'</nav>'
                sections.append('<section data-site-language="'+language+'" lang="'+language+'">'+nav+'<aside class="validation-scope">'+paragraph(scope_text(language, common_count))+'</aside>'+render_case(case, measured[ident], current, language, rendered, 1, True, editorial_note)+terms(language)+'</section>')
                markdown += markdown_case(case, measured[ident], current, language, editorial_note=editorial_note)+'\n'
            destination = ROOT/case_route(ident).lstrip('/'); destination.mkdir(parents=True, exist_ok=True)
            (destination/'index.html').write_text(document(case_route(ident), page_title, case['summary'], ''.join(sections)))
            dump(destination/'index.json', public_case); (destination/'index.md').write_text(markdown.rstrip()+'\n')
        chapter_entries[group_id] = {}
        chapter_id = 'validation-'+group_id
        for language in LANGUAGES:
            ja = language == 'ja'; title = group['title'][language]
            intro = '小規模な固定入力で、計算法・参照・誤差・収束・失敗条件を確かめます。' if ja else 'Small fixed inputs connect numerical methods, references, errors, refinement and explicit failure conditions.'
            body = '<h1>'+escape(title)+'</h1>'+paragraph(intro)+'<aside class="validation-scope">'+paragraph(scope_text(language, common_count))
            if catalog.get('routine_policy'):
                body += paragraph(catalog['routine_policy'][language])
            body += '</aside>'
            body += '<nav class="validation-actions">'+link(INDEX+'?lang='+language, '追加検証の一覧' if ja else 'Additional validation index')+link(current['base']+current['verification']['archive']['file'], 'コード・テスト / ZIP' if ja else 'Code and tests / ZIP')+link(current['base']+'verification.json', '独立展開の検証記録' if ja else 'Independent-extraction receipt')+'</nav>'
            body += '<nav class="validation-toc" aria-label="'+('この章の例' if ja else 'Cases in this chapter')+'">'+''.join(link('#'+case['id'], case['title'][language]) for case in current['metadata'])+'</nav>'
            body += '<section><h2 id="run-all">'+('配布版を取得して実行する' if ja else 'Download and execute the supplement')+'</h2>'+group_commands(current, language)+'</section>'
            markdown = '# '+title+'\n\n'+intro+'\n\n'+scope_text(language, common_count)+'\n\n'
            for case in current['metadata']:
                note = catalog.get('case_notes', {}).get(case['id'])
                body += render_case(case, measured[case['id']], current, language, rendered, editorial_note=note)
                markdown += markdown_case(case, measured[case['id']], current, language, 2, note)+'\n'
            body += terms(language)
            headings = [{'level': int(level), 'id': ident, 'title': re.sub('<[^>]+>', '', text)}
                        for level, ident, text in re.findall(r'<h([23]) id="([a-z0-9-]+)">(.*?)</h[23]>', body, re.S)]
            # Case section IDs live on their article; expose them as TOC/search headings.
            headings += [{'level': 2, 'id': case['id'], 'title': case['title'][language]} for case in current['metadata']]
            entry = {'title': title, 'html': body, 'headings': headings, 'locale': language,
                     'source_url': current['base']+'cases.json', 'updated_on': catalog['edition'][:10]}
            if ja:
                entry['translation_status'] = 'draft'
            documents[language][chapter_id] = entry; chapter_entries[group_id][language] = entry
            destination = ROOT/chapter_route(group_id, language).lstrip('/'); destination.mkdir(parents=True, exist_ok=True)
            nav = '<nav class="validation-actions">'+link('/numerical-methods-atlas/'+language+'/read/', '解説章の目次' if ja else 'Reading contents')+link('index.json', 'JSON')+link('index.md', 'Markdown')+'</nav>'
            (destination/'index.html').write_text(document(chapter_route(group_id, language), title+' | Numerical Methods Atlas', intro, nav+'<div class="validation-prose">'+body+'</div>', language, {lang: chapter_route(group_id, lang) for lang in LANGUAGES}))
            dump(destination/'index.json', {**entry, 'url': ORIGIN+chapter_route(group_id, language), 'group': group_id,
                 'case_ids': [case['id'] for case in current['metadata']], 'measurements': current['results']['cases'],
                 'source_sha256': source_hashes}); (destination/'index.md').write_text(markdown.rstrip()+'\n')
            translations['chapters'][chapter_id] = {'status': 'draft', 'source_url': current['base']+'cases.json',
                'source_sha256': digest(current['directory']/'cases.json'), 'checked_on': catalog['edition'][:10]}
    for language in LANGUAGES:
        dump(ATLAS/('content.'+language+'.json'), documents[language])
        if language == 'en':
            dump(ATLAS/'content.json', documents[language])
        toc_path = ATLAS/language/'read/index.html'
        text = re.sub(r'<!-- depth-examples -->.*?<!-- /depth-examples -->', '', toc_path.read_text(), flags=re.S)
        block = '<!-- depth-examples --><section class="page-width"><h2>'+('小規模な追加検証：手法から実測値へ' if language == 'ja' else 'Lightweight additional validation: methods to measurements')+'</h2><ul>'+''.join('<li>'+link(chapter_route(group['id'], language), group['title'][language])+'</li>' for group in catalog['groups'])+'</ul><p>'+link(INDEX+'?lang='+language, '全追加例の固定入力・コード・テスト' if language == 'ja' else 'Fixed inputs, code and tests for all additional cases')+'</p></section><!-- /depth-examples -->'
        assert '</main>' in text; toc_path.write_text(text.replace('</main>', block+'</main>'))
    translations.update(total=len(documents['en']), translated=sum(key in documents['ja'] for key in documents['en']),
        reviewed=sum(value['status'] == 'reviewed' for key, value in translations['chapters'].items() if key in documents['en']))
    dump(ATLAS/'translation-status.json', translations)
    search_path = ATLAS/'home-search-index.json'; search = read_json(search_path)
    search['entries'] = [entry for entry in search['entries'] if entry.get('origin') != 'depth-examples']
    for group in catalog['groups']:
        current = data[group['id']]
        keywords = list(group.get('fields', []))
        for case in current['metadata']:
            keywords.extend([case['id'], *case['method_ids'], case['title']['ja'], case['title']['en']])
        search['entries'].append({'id': 'reading-validation-'+group['id'], 'title': group['title'],
            'headings': {language: chapter_entries[group['id']][language]['headings'] for language in LANGUAGES},
            'keywords': list(dict.fromkeys(keywords)),
            'routes': {language: chapter_route(group['id'], language) for language in LANGUAGES}, 'origin': 'depth-examples', 'kind': 'chapter'})
    dump(search_path, search)
    sections, markdown = [], ''
    for language in LANGUAGES:
        ja = language == 'ja'; body = '<section data-site-language="'+language+'" lang="'+language+'"><h1>'+escape(catalog['title'][language])+'</h1>'+paragraph(scope_text(language, common_count))
        for field in ['policy', 'routine_policy']:
            if catalog.get(field):
                body += paragraph(catalog[field][language])
        body += paragraph((str(len(identifiers))+'の固定検証例を、'+str(len(data))+'つの配布版から実行できます。' if ja else str(len(identifiers))+' fixed validation cases are runnable through '+str(len(data))+' supplements.'))
        body += '<nav class="validation-actions">'+link('/numerical-methods-atlas/?lang='+language, 'アトラス' if ja else 'Atlas')+link('/numerical-methods-atlas/depth/?lang='+language, '分野ごとの検証範囲' if ja else 'Field validation scope')+link('index.json', 'JSON')+link('index.md', 'Markdown')+'</nav><div class="validation-group-grid">'
        markdown += '# '+catalog['title'][language]+'\n\n'+scope_text(language, common_count)+'\n\n'
        for group in catalog['groups']:
            current = data[group['id']]
            body += '<section class="validation-group"><h2 id="'+group['id']+'-'+language+'">'+link(chapter_route(group['id'], language), group['title'][language])+'</h2><p>'+str(current['verification']['passed_tests'])+('検査に合格。ZIP独立展開から全入力を再実行。' if ja else ' tests passed; every input rerun from an independent ZIP extraction.')+'</p><ul>'
            markdown += '## '+group['title'][language]+'\n\n'
            for case in current['metadata']:
                body += '<li data-validation-entry="'+case['id']+'"><h3>'+link(case_route(case['id'], language), case['title'][language])+'</h3>'+paragraph(case['summary'][language])+'</li>'
                markdown += '- ['+case['title'][language]+']('+ORIGIN+case_route(case['id'], language)+'): '+case['summary'][language]+'\n'
            body += '</ul></section>'; markdown += '\n'
        sections.append(body+'</div>'+terms(language)+'</section>')
    destination = ROOT/INDEX.lstrip('/'); destination.mkdir(parents=True, exist_ok=True)
    (destination/'index.html').write_text(document(INDEX, catalog['title'], {language: scope_text(language, common_count) for language in LANGUAGES}, ''.join(sections)))
    dump(destination/'index.json', {'schema_version': 1, 'edition': catalog['edition'], 'title': catalog['title'],
         'policy': catalog.get('policy'), 'routine_policy': catalog.get('routine_policy'),
         'case_problem_ids': catalog.get('case_problem_ids', {}),
         'common_registry': {'url': ORIGIN+'/numerical-methods-atlas/code-and-data/examples.json', 'example_count': common_count, 'sha256': registry_hash, 'modified_by_this_builder': False},
         'case_count': len(identifiers), 'groups': public_groups, 'cases': public_cases, 'source_sha256': source_hashes})
    (destination/'index.md').write_text(markdown+'\nOriginal code: MIT. Other materials: https://hrkoyama.github.io/LICENSING.md and https://hrkoyama.github.io/rights/.\n')
    sitemap = ATLAS/'sitemap.xml'; tree = ET.parse(sitemap); xml = tree.getroot(); namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    known = {element.text for element in xml.findall('.//{*}loc')}
    urls = [INDEX, *[case_route(ident) for ident in identifiers], *[chapter_route(group, language) for group in data for language in LANGUAGES]]
    for route in urls:
        if ORIGIN+route not in known:
            ET.SubElement(ET.SubElement(xml, namespace+'url'), namespace+'loc').text = ORIGIN+route
    ET.register_namespace('', namespace[1:-1]); tree.write(sitemap, encoding='utf-8', xml_declaration=True)
    assert digest(registry_path) == registry_hash, 'Common execution registry must remain unchanged'
    print('Built', len(identifiers), 'additional validation entries and', len(catalog['groups']), 'bilingual readings from verified frozen measurements.')


if __name__ == '__main__':
    build()
