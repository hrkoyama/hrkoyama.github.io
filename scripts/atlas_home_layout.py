"""Build the concise front door and the separate bilingual reading directory."""
import hashlib
import html
import json
import re
import subprocess


def build_home_layout(root, copy, sections, metrics, featured, maps, context):
    atlas = root / 'numerical-methods-atlas'
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    overview = atlas / 'home-overview.js'
    source = overview.read_text()
    for name in ['home-search.js', 'home-overview-data.js', 'atlas-home-data.js']:
        source = re.sub(r"from './"+re.escape(name)+r"(?:[?]v=[a-f0-9]+)?'",
                        "from './"+name+'?v='+digest(atlas/name)+"'", source)
    overview.write_text(source)
    navigation = atlas / 'home-navigation.mjs'
    source = navigation.read_text()
    for name in ['home-overview-data.js', 'atlas-home-data.js']:
        source = re.sub(r"from './"+re.escape(name)+r"(?:[?]v=[a-f0-9]+)?'",
                        "from './"+name+'?v='+digest(atlas/name)+"'", source)
    navigation.write_text(source)
    rendered = json.loads(subprocess.check_output(['node', 'scripts/render-atlas-landing.mjs'], cwd=root, text=True))
    page = atlas / 'index.html'
    text = page.read_text()
    fallback = '<!-- atlas-intro-fallback -->'+''.join(
        '<div data-site-language="'+lang+'" lang="'+lang+'">'+rendered[lang]+'</div>' for lang in ['ja','en'])+'<!-- /atlas-intro-fallback -->'
    text = re.sub(r'(<main\b[^>]*>).*?</main>', lambda m:m[1]+fallback+'</main>', text, count=1, flags=re.S)
    text = re.sub(r'<body(?:\s[^>]*)?>', '<body class="atlas-home">', text, count=1)
    text = re.sub(r'<link rel="stylesheet" href="/styles/atlas-home-shell[.]css[^"]*">\s*', '', text)
    text = text.replace('</head>', '<link rel="stylesheet" href="/styles/atlas-home-shell.css?v='+digest(root/'styles/atlas-home-shell.css')+'">\n</head>')
    page.write_text(text)

    blocks = []
    for lang in ['ja','en']:
        ja = lang == 'ja'
        title = '体系的に読む' if ja else 'Read systematically'
        description = '分野の地図、読む順番、章の目次から、学びたい内容を選んでください。' if ja else 'Choose a field, follow a reading path, or open the chapter index.'
        links = [(f'/numerical-methods-atlas/{lang}/read/', '解説章の目次' if ja else 'Chapter index'),
                 (f'/numerical-methods-atlas/methods/?lang={lang}', '全手法の一覧' if ja else 'All method records'),
                 (f'/numerical-methods-atlas/connections/?lang={lang}', '分野をつなぐ' if ja else 'Connections across fields')]
        intro = '<section class="page-width"><p><a href="/numerical-methods-atlas/?lang='+lang+'">'+('アトラストップ' if ja else 'Atlas home')+'</a></p><h1>'+title+'</h1><p class="intro-description">'+description+'</p><nav class="study-shortcuts">'+''.join('<a href="'+u+'">'+label+'</a>' for u,label in links)+'</nav></section>'
        catalogue = '<details class="page-width explore-catalogue"><summary>'+('数式・図・収録範囲から探す' if ja else 'Browse equations, figures and coverage')+'</summary>'+metrics[lang]+sections[lang]+'</details>'
        tail = '<section class="page-width"><h2>'+('資料と機械可読データ' if ja else 'Resources and machine-readable data')+'</h2><p><a href="/numerical-methods-atlas/methods/index.json">'+('手法台帳 / JSON' if ja else 'Method registry / JSON')+'</a> · <a href="/guide/packs/numerical.md">Markdown</a> · <a href="/llms.txt">AI index</a> · <a href="index.json">'+('この案内 / JSON' if ja else 'This directory / JSON')+'</a></p></section>'
        body = intro+rendered['guides'][lang]+maps[lang]+catalogue+context[lang]+tail
        # Standalone directories must open interactive exhibits on the SPA root.
        body = body.replace('href="#/', 'href="/numerical-methods-atlas/?lang='+lang+'#/')
        blocks.append('<div class="home-overview" data-site-language="'+lang+'" lang="'+lang+'">'+body+'</div>')
    directory = atlas / 'explore'
    directory.mkdir(exist_ok=True)
    assets = ['/numerical-methods-atlas/style.css','/numerical-methods-atlas/home-overview.css',
              '/styles/atlas-purpose.css','/styles/atlas-depth.css','/styles/atlas-crossovers.css','/styles/atlas-home-shell.css']
    head = ''.join('<link rel="stylesheet" href="'+name+'?v='+digest(root/name.lstrip('/'))+'">\n' for name in assets)
    document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="体系的に読む | 数値計算法アトラス" data-page-title-en="Read systematically | Numerical Methods Atlas">体系的に読む | 数値計算法アトラス</title><meta name="description" content="分野地図・読む順番・解説章の目次。Field map, reading paths and chapter index."><link rel="canonical" href="https://hrkoyama.github.io/numerical-methods-atlas/explore/">'+head+'<script defer src="/numerical-methods-atlas/explore.js?v='+digest(atlas/'explore.js')+'"></script></head><body class="atlas-explore"><main>'+''.join(blocks)+'</main></body></html>\n'
    (directory/'index.html').write_text(document)
    record = dict(schema_version=1, source='/catalog/atlas-home.json',
                  title={'ja':'体系的に読む','en':'Read systematically'},
                  home={l:'/numerical-methods-atlas/?lang='+l for l in ['ja','en']},
                  chapters={l:f'/numerical-methods-atlas/{l}/read/' for l in ['ja','en']},
                  methods='/numerical-methods-atlas/methods/index.json',
                  field_map={l:'/numerical-methods-atlas/explore/?lang='+l+'#atlas-map-'+l for l in ['ja','en']})
    (directory/'index.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    (directory/'index.md').write_text('# 体系的に読む / Read systematically\n\n'+
        '\n'.join('- '+l+': https://hrkoyama.github.io'+record['chapters'][l] for l in ['ja','en'])+
        '\n- Field map: https://hrkoyama.github.io/numerical-methods-atlas/explore/\n- Method registry: https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json\n- Source-linked reading pack: https://hrkoyama.github.io/guide/packs/numerical.md\n')
    app = atlas/'app.js'
    text = app.read_text()
    for name in ['home-overview.js','home-navigation.mjs']:
        text = re.sub(r"from './"+re.escape(name)+r"(?:[?]v=[a-f0-9]+)?'", "from './"+name+'?v='+digest(atlas/name)+"'", text)
    app.write_text(text)
