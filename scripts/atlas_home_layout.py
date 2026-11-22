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
        description = '考え方から学ぶときは解説へ。使う手法やコードを調べるときは対応表へ進んでください。' if ja else 'Read the explanations to learn the ideas. Use the reference to look up a method and its code.'
        links = [(f'/numerical-methods-atlas/{lang}/read/',
                  '分野別に解説を読む' if ja else 'Learn by field',
                  '理論や式の導き方、具体例を、分野ごとの流れに沿って読み進めます。' if ja else 'Learn the theory, derivations and examples in a sequence organized by field.'),
                 (f'/numerical-methods-atlas/methods/?lang={lang}',
                  '手法・コードの対応表' if ja else 'Methods and code reference',
                  '手法名から、適用条件・対応するコードとテスト・公開状況を調べます。' if ja else 'Look up a method to check its conditions, related code and tests, and publication status.'),
                 (f'/numerical-methods-atlas/connections/?lang={lang}',
                  '分野をつなぐ' if ja else 'Connections across fields',
                  '複数の分野で共通する数学と、追加で必要な検証をたどります。' if ja else 'Follow mathematics shared across fields and the additional verification each connection needs.')]
        shortcuts = '<nav class="study-shortcuts" aria-label="'+('読む目的に合わせて選ぶ' if ja else 'Choose how to read')+'"><ul>'+''.join('<li'+(' class="study-shortcut-primary"' if i==0 else '')+'><a href="'+u+'">'+label+'</a><p>'+note+'</p></li>' for i,(u,label,note) in enumerate(links))+'</ul></nav>'
        intro = '<section class="page-width"><p><a href="/numerical-methods-atlas/?lang='+lang+'">'+('アトラストップ' if ja else 'Atlas home')+'</a></p><h1>'+title+'</h1><p class="intro-description">'+description+'</p>'+shortcuts+'</section>'
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
