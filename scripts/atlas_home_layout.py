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
    descriptions = {}
    for lang in ['ja','en']:
        ja = lang == 'ja'
        title = '学習ガイド：おすすめの順番' if ja else 'Learning guide: suggested order'
        description = '基礎から学ぶための案内です。おすすめの順番と分野の地図から、学びたい経路を選べます。' if ja else 'A guide to learning from the foundations. Choose a path using the suggested study order and field map.'
        descriptions[lang] = description
        links = [(f'/numerical-methods-atlas/methods/?lang={lang}',
                  '全手法一覧' if ja else 'All methods',
                  '手法名から、適用条件・対応するコードとテスト・公開状況を調べます。' if ja else 'Look up a method to check its conditions, related code and tests, and publication status.'),
                 (f'/numerical-methods-atlas/connections/?lang={lang}',
                  '分野をつなぐ' if ja else 'Connections across fields',
                  '複数の分野で共通する数学と、追加で必要な検証をたどります。' if ja else 'Follow mathematics shared across fields and the additional verification each connection needs.')]
        shortcuts = '<section class="page-width"><h2>'+('調べる・関連資料へ進む' if ja else 'Look up methods and related resources')+'</h2><nav class="study-shortcuts" aria-label="'+('関連する調べもの' if ja else 'Related lookups')+'"><ul>'+''.join('<li><a href="'+u+'">'+label+'</a><p>'+note+'</p></li>' for u,label,note in links)+'</ul></nav></section>'
        role = 'ここはおすすめの経路を選ぶガイドです。すべての章・資料を探すときは、全章目次を利用してください。' if ja else 'This guide suggests learning paths. Use the complete chapter index to look up every chapter and resource.'
        toc = '<p><a data-learning-guide-toc href="/numerical-methods-atlas/'+lang+'/read/">'+('分野別の全章目次' if ja else 'Complete chapter index')+'</a> — '+('既知の章や学習資料を探す索引' if ja else 'Look up a known chapter or learning resource')+'</p>'
        intro = '<section class="page-width"><p><a href="/numerical-methods-atlas/?lang='+lang+'">'+('アトラストップ' if ja else 'Atlas home')+'</a></p><h1>'+title+'</h1><p class="intro-description">'+description+'</p><p data-learning-guide-role>'+role+'</p>'+toc+'</section>'
        references = '<section class="page-width study-references" aria-labelledby="study-references-title-'+lang+'"><h2 id="study-references-title-'+lang+'">'+('教科書・参考文献' if ja else 'Textbooks and references')+'</h2><div class="study-reference-grid"><article><h3><a href="/numerical-methods-atlas/'+lang+'/read/textbooks/">'+('教科書案内' if ja else 'Textbook guide')+'</a></h3><p>'+('学びたい分野や学習段階に合う教科書を探します。' if ja else 'Find textbooks for your field and stage of study.')+'</p></article><article><h3><a href="/numerical-methods-atlas/'+lang+'/read/references/">'+('論文・参考文献一覧' if ja else 'Papers and reference list')+'</a></h3><p>'+('手法の原著論文と関連資料の出典を確認できます。' if ja else 'Find original publications and supporting sources for numerical methods.')+'</p></article></div></section>'
        catalogue = '<details class="page-width explore-catalogue"><summary>'+('数式・図・収録範囲から探す' if ja else 'Browse equations, figures and coverage')+'</summary>'+metrics[lang]+sections[lang]+'</details>'
        tail = '<section class="page-width"><h2>'+('資料と機械可読データ' if ja else 'Resources and machine-readable data')+'</h2><p><a href="/numerical-methods-atlas/methods/index.json">'+('手法台帳 / JSON' if ja else 'Method registry / JSON')+'</a> · <a href="/guide/packs/numerical.md">Markdown</a> · <a href="/llms.txt">AI index</a> · <a href="index.json">'+('この案内 / JSON' if ja else 'This directory / JSON')+'</a></p></section>'
        body = intro+'<div data-learning-guide-paths="'+lang+'">'+rendered['guides'][lang]+'</div>'+maps[lang]+shortcuts+references+rendered['browse'][lang]+catalogue+context[lang]+tail
        # Standalone directories must open interactive exhibits on the SPA root.
        body = body.replace('href="#/', 'href="/numerical-methods-atlas/?lang='+lang+'#/')
        blocks.append('<div class="home-overview" data-site-language="'+lang+'" lang="'+lang+'">'+body+'</div>')
    directory = atlas / 'explore'
    directory.mkdir(exist_ok=True)
    assets = ['/numerical-methods-atlas/style.css','/numerical-methods-atlas/home-overview.css',
              '/styles/atlas-purpose.css','/styles/atlas-depth.css','/styles/atlas-crossovers.css','/styles/atlas-home-shell.css']
    head = ''.join('<link rel="stylesheet" href="'+name+'?v='+digest(root/name.lstrip('/'))+'">\n' for name in assets)
    document = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title data-page-title-ja="学習ガイド：おすすめの順番 | 数値計算法アトラス" data-page-title-en="Learning guide: suggested order | Numerical Methods Atlas">学習ガイド：おすすめの順番 | 数値計算法アトラス</title><meta name="description" content="おすすめの学ぶ順番と分野の地図。Suggested learning order and field map, separate from the complete chapter index."><link rel="canonical" href="https://hrkoyama.github.io/numerical-methods-atlas/explore/">'+head+'<script defer src="/numerical-methods-atlas/explore.js?v='+digest(atlas/'explore.js')+'"></script></head><body class="atlas-explore"><main>'+''.join(blocks)+'</main></body></html>\n'
    (directory/'index.html').write_text(document)
    record = dict(schema_version=1, source='/catalog/atlas-home.json',
                  title={'ja':'学習ガイド：おすすめの順番','en':'Learning guide: suggested order'},
                  role='learning-guide', description=descriptions,
                  home={l:'/numerical-methods-atlas/?lang='+l for l in ['ja','en']},
                  chapters={l:f'/numerical-methods-atlas/{l}/read/' for l in ['ja','en']},
                  learning_resources={l:{name:f'/numerical-methods-atlas/{l}/read/{name}/' for name in ['textbooks','references']} for l in ['ja','en']},
                  browse={l:{name:f'/numerical-methods-atlas/{name}/?lang={l}' for name in ['solutions','gallery','equations']} for l in ['ja','en']},
                  methods='/numerical-methods-atlas/methods/index.json',
                  field_map={l:'/numerical-methods-atlas/explore/?lang='+l+'#atlas-map-'+l for l in ['ja','en']})
    (directory/'index.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    (directory/'index.md').write_text('# 学習ガイド：おすすめの順番 / Learning guide: suggested order\n\n'+
        'おすすめ経路と分野の地図から学ぶ順番を選びます。全章・学習資料を探す索引は、分野別の全章目次です。\n\nChoose a suggested learning path. The complete chapter index is a separate lookup of every chapter and resource.\n\n'+
        '\n'.join('- '+l+': https://hrkoyama.github.io'+record['chapters'][l] for l in ['ja','en'])+
        '\n\n## 教科書・参考文献 / Textbooks and references\n\n'+
        '\n'.join('- '+l+' '+name+': https://hrkoyama.github.io'+url for l,resources in record['learning_resources'].items() for name,url in resources.items())+
        '\n\n## 式や図から探す / Browse by equations and figures\n\n'+
        '\n'.join('- '+l+' '+name+': https://hrkoyama.github.io'+url for l,resources in record['browse'].items() for name,url in resources.items())+
        '\n- Field map: https://hrkoyama.github.io/numerical-methods-atlas/explore/\n- Method registry: https://hrkoyama.github.io/numerical-methods-atlas/methods/index.json\n- Source-linked reading pack: https://hrkoyama.github.io/guide/packs/numerical.md\n')
    app = atlas/'app.js'
    text = app.read_text()
    for name in ['home-overview.js','home-navigation.mjs']:
        text = re.sub(r"from './"+re.escape(name)+r"(?:[?]v=[a-f0-9]+)?'", "from './"+name+'?v='+digest(atlas/name)+"'", text)
    app.write_text(text)
