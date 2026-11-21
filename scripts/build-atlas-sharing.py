#!/usr/bin/env python3
"""Generate the atlas introduction, copyable text and 1200x630 sharing assets.

HTML, SVG and metadata use only the standard library. New PNG rendering needs
Pillow and a Japanese-capable font; unchanged, hash-checked PNGs are reused.
See numerical-methods-atlas/share/BUILD.md for reproducible rendering commands.
"""
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import struct
import sys

ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://hrkoyama.github.io'
BASE='/numerical-methods-atlas/share/'
DEST=ROOT/BASE.lstrip('/')
SOURCE='catalog/atlas-sharing.json'
SOURCES=[SOURCE,'catalog/atlas-methods.json','numerical-methods-atlas/coverage.json',
         'catalog/atlas-execution-examples.json','catalog/atlas-execution-discovery.json']


def sha(value):return hashlib.sha256(value).hexdigest()
def encode(value):return json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
def esc(value):return html.escape(str(value),quote=True)
def write(name,value):
    path=DEST/name
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value)


def load():
    raw={path:(ROOT/path).read_bytes() for path in SOURCES}
    data={path:json.loads(value) for path,value in raw.items()}
    copy=data[SOURCE]
    if copy['schema_version']!=1 or copy['route']!=BASE:raise ValueError('Unsupported sharing catalog')
    methods=data['catalog/atlas-methods.json']['methods']
    statuses=Counter(row['status'] for row in methods)
    if set(statuses)!={'educational-example','reading-only','planned'}:raise ValueError('Unknown method status')
    counts=data['numerical-methods-atlas/coverage.json']['counts'].copy()
    counts.update(method_records=len(methods),educational_examples=statuses['educational-example'],
                  reading_only=statuses['reading-only'],planned=statuses['planned'])
    examples=data['catalog/atlas-execution-examples.json']['examples']
    counts['execution_examples']=len(examples)
    if counts['methods']!=counts['educational_examples']+counts['reading_only']:
        raise ValueError('Reconcile existing coverage with canonical method statuses')
    discoveries={row['id']:row for row in data['catalog/atlas-execution-discovery.json']['examples']}
    if set(discoveries)!={row['id'] for row in examples}:raise ValueError('Discovery/example mismatch')
    for row in examples:
        if not (ROOT/f"numerical-methods-atlas/code-and-data/examples/{row['id']}/index.html").is_file():
            raise ValueError('Build dedicated execution pages before the sharing page')
    return copy,counts,examples,discoveries,{path:sha(value) for path,value in raw.items()}


def formatted(copy,counts,lang,key):return copy['copy'][lang][key].format(**counts)
def link(url,label,download=False):return '<a href="'+esc(url)+'"'+(' download' if download else '')+'>'+esc(label)+'</a>'


def routes(lang):
    return [('/search/?lang='+lang,'文字で検索' if lang=='ja' else 'Search by words'),
            ('/numerical-methods-atlas/equations/?lang='+lang,'数式から探す' if lang=='ja' else 'Browse by equation'),
            ('/numerical-methods-atlas/gallery/?lang='+lang,'絵から探す' if lang=='ja' else 'Browse by picture')]


def intro_text(copy,counts,lang,kind=None):
    if kind:return formatted(copy,counts,lang,kind)+'\n'+copy['atlas_url']+'?lang='+lang+'\n'
    c=copy['copy'][lang]
    values=[c['title'],formatted(copy,counts,lang,'short'),formatted(copy,counts,lang,'paragraph'),
            copy['atlas_url']+'?lang='+lang]
    values += [label+': '+ORIGIN+url for url,label in routes(lang)]
    values += [('固定入力の実行例' if lang=='ja' else 'Fixed-input execution examples')+': '+ORIGIN+'/numerical-methods-atlas/code-and-data/?lang='+lang,
               ('この言語の共有プレビュー' if lang=='ja' else 'Sharing preview in this language')+': '+ORIGIN+BASE+lang+'/',
               copy['sharing_terms'][lang],('利用条件' if lang=='ja' else 'Rights and terms')+': '+ORIGIN+'/rights/?lang='+lang]
    return '\n\n'.join(values)+'\n'


def scene(copy,counts,lang):
    c=copy['copy'][lang]['image'];colors=copy['image']['colors'];items=[]
    def rect(x,y,w,h,fill):items.append(dict(kind='rect',x=x,y=y,w=w,h=h,fill=fill))
    def text(x,y,value,size,color=None,max_width=1080):items.append(dict(kind='text',x=x,y=y,text=value.format(**counts),size=size,fill=color or colors['green'],max_width=max_width))
    rect(0,0,1200,630,colors['paper'])
    rect(60,28,54,5,colors['orange'])
    text(60,64,c['eyebrow'],19,max_width=1080)
    text(60,151,c['title'],60 if lang=='ja' else 68,max_width=840)
    text(60,207,c['subtitle'],28,max_width=1080)
    rect(926,101,214,59,colors['orange'])
    text(1033,140,c['badge'],22,colors['paper'],max_width=190)
    items[-1]['anchor']='middle'
    for i in range(3):
        x=60+380*i
        rect(x,258,320,116,colors['green'])
        text(x+22,304,c['steps'][i],23,colors['paper'],max_width=276)
        text(x+22,344,c['step_notes'][i],19,colors['paper'],max_width=276)
        if i<2:items.append(dict(kind='line',points=[(x+339,315),(x+362,315),(x+355,308),(x+362,315),(x+355,322)],fill=colors['orange'],width=3))
    for i,key in enumerate(['methods','papers','equations','test_problems']):
        x=60+280*i
        text(x,465,str(counts[key]),46,max_width=240)
        text(x,504,c['metric_labels'][i],17,max_width=240)
    rect(60,533,1080,1,colors['line'])
    text(60,569,c['footer'],17,max_width=1080)
    text(60,607,'hrkoyama.github.io/numerical-methods-atlas/',22,max_width=1080)
    return items


def svg(copy,counts,lang,items):
    title=copy['copy'][lang]['image']['title']
    description=formatted(copy,counts,lang,'description')
    family=esc(copy['image']['font_family'])
    output=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-labelledby="title description" lang="'+lang+'">',
            '<title id="title">'+esc(title)+'</title><desc id="description">'+esc(description)+'</desc>',
            '<metadata>'+esc(json.dumps({'source':ORIGIN+BASE,'rights':ORIGIN+'/rights/','scope':'Introduction graphic; not new simulation output','counts':{k:counts[k] for k in ['methods','papers','equations','test_problems','execution_examples']}},ensure_ascii=False))+'</metadata>']
    for item in items:
        if item['kind']=='rect':output.append(f'<rect x="{item["x"]}" y="{item["y"]}" width="{item["w"]}" height="{item["h"]}" fill="{item["fill"]}"/>')
        elif item['kind']=='line':output.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in item['points'])+'" fill="none" stroke="'+item['fill']+'" stroke-width="'+str(item['width'])+'"/>')
        else:output.append(f'<text x="{item["x"]}" y="{item["y"]}" font-family="{family}" font-size="{item["size"]}" font-weight="600" text-anchor="{item.get("anchor","start")}" fill="{item["fill"]}">{esc(item["text"])}</text>')
    return '\n'.join(output+['</svg>'])+'\n'


def find_font(explicit):
    if explicit:
        path=Path(explicit).expanduser()
        if not path.is_file():raise ValueError('The requested --font file does not exist')
        return path
    candidates=list(Path('/System/Library/Fonts').glob('*W6.ttc'))
    candidates += [Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'),
                   Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'),
                   Path('/usr/share/fonts/truetype/noto/NotoSansJP-Regular.ttf')]
    for path in candidates:
        if path.is_file():return path
    raise ValueError('A Japanese-capable font is required; pass --font /path/to/font.ttf (Hiragino or Noto Sans CJK). Font binaries are not bundled.')


def png(path,items,font_path):
    try:
        import PIL
        from PIL import Image,ImageDraw,ImageFont,features
    except ImportError as exc:
        raise RuntimeError('New PNG rendering needs Pillow. Install render-requirements.txt from the share directory in your build environment, then rerun this script. Unchanged verified PNGs do not need Pillow.') from exc
    canvas=Image.new('RGB',(1200,630))
    draw=ImageDraw.Draw(canvas);fonts={}
    for item in items:
        if item['kind']=='rect':draw.rectangle((item['x'],item['y'],item['x']+item['w'],item['y']+item['h']),fill=item['fill'])
        elif item['kind']=='line':draw.line(item['points'],fill=item['fill'],width=item['width'],joint='curve')
        else:
            font=fonts.setdefault(item['size'],ImageFont.truetype(str(font_path),item['size']))
            if font.getlength(item['text'])>item['max_width']:
                raise ValueError('Sharing graphic text exceeds its layout width: '+item['text'])
            draw.text((item['x'],item['y']),item['text'],font=font,fill=item['fill'],anchor='ms' if item.get('anchor')=='middle' else 'ls')
    canvas.save(path,format='PNG',compress_level=9)
    return {'name':'Pillow','version':PIL.__version__,'freetype':features.version_module('freetype2')}


def valid_png(path,expected):
    if not path.is_file() or sha(path.read_bytes())!=expected:return False
    raw=path.read_bytes()
    return raw[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',raw[16:24])==(1200,630)


def body(copy,counts,examples,discoveries,lang,bilingual):
    ja=lang=='ja';c=copy['copy'][lang]
    examples_id='examples-'+lang if bilingual else 'examples'
    materials_id='materials-'+lang if bilingual else 'materials'
    attr=' data-site-language="'+lang+'"' if bilingual else ''
    output='<section'+attr+' lang="'+lang+'"><p class="eyebrow">NUMERICAL METHODS ATLAS · INTRODUCTION &amp; SHARING</p>'
    output+='<h1>'+esc(c['headline'])+'</h1><p class="share-lead">'+esc(c['lead'])+'</p>'
    output+='<nav class="share-primary" aria-label="'+('まず見る資料' if ja else 'Start here')+'">'+link(copy['atlas_url']+'?lang='+lang,'アトラスを開く' if ja else 'Open the atlas')+link('#'+examples_id,f'固定入力の{counts["execution_examples"]}例' if ja else f'{counts["execution_examples"]} fixed-input examples')+link('#'+materials_id,'紹介文と画像を使う' if ja else 'Get sharing text and images')+'</nav>'
    output+='<ol class="share-workflow">'+''.join('<li><strong>'+esc(x['title'])+'</strong><p>'+esc(x['body'])+'</p></li>' for x in c['workflow'])+'</ol>'
    output+='<div class="share-metrics">'+''.join('<div><strong>'+str(counts[key])+'</strong><span>'+esc(label)+'</span></div>' for key,label in zip(['methods','papers','equations','test_problems'],c['image']['metric_labels']))+'</div>'
    output+='<p class="share-scope">'+esc((f'{counts["methods"]}は収録手法・構成要素の数です。手法の見取り図は{counts["method_records"]}レコード（教育用例・関連コード{counts["educational_examples"]}、解説のみ{counts["reading_only"]}、予定{counts["planned"]}）。完成した汎用ソルバーの数ではありません。{counts["execution_examples"]}実行例は全{counts["test_problems"]}問題の一部で、別に加算しません。' if ja else f'{counts["methods"]} counts existing methods and building blocks. The method map has {counts["method_records"]} records: {counts["educational_examples"]} educational/related-code, {counts["reading_only"]} reading-only and {counts["planned"]} planned. These are not counts of complete production solvers. The {counts["execution_examples"]} runnable examples are a subset of the {counts["test_problems"]} problems, not an addition.'))+'</p>'
    output+='<h2>'+('文字・数式・絵から探す' if ja else 'Find a starting point')+'</h2><nav class="share-routes" aria-label="'+('3つの入口' if ja else 'Three discovery routes')+'">'+''.join(link(url,label) for url,label in routes(lang))+'</nav>'
    output+='<details class="share-examples" id="'+examples_id+'"><summary>'+esc(f'固定入力から実行できる{counts["execution_examples"]}例を選ぶ' if ja else f'Choose from {counts["execution_examples"]} fixed-input examples')+'</summary><p>'+('各リンクで条件、版、入力、実行手順、JSON/CSVと許容誤差を確認できます。' if ja else 'Each entry provides conditions, edition, input, commands, JSON/CSV and numerical tolerances.')+'</p><ul>'
    for row in examples:
        output+='<li>'+link('/numerical-methods-atlas/code-and-data/examples/'+row['id']+'/?lang='+lang,row['name'][lang])+'<span>'+esc(discoveries[row['id']]['outcome'][lang])+'</span></li>'
    output+='</ul></details>'
    output+='<section id="'+materials_id+'" class="share-materials"><h2>'+('紹介文と画像を使う' if ja else 'Text and images for an introduction')+'</h2><p>'+('紹介文はそのまま選択・コピーできます。アトラスのURLと組み合わせ、出典が分かる形で紹介してください。' if ja else 'Select and copy the text below. Include the atlas URL and keep the source identifiable.')+'</p>'
    for key,rows,label in [('short',4,'短い紹介' if ja else 'Short introduction'),('paragraph',7,'1段落の説明' if ja else 'One-paragraph description')]:
        output+='<label for="share-'+key+'-'+lang+'">'+label+'</label><textarea id="share-'+key+'-'+lang+'" readonly spellcheck="false" rows="'+str(rows)+'">'+esc(formatted(copy,counts,lang,key))+'</textarea><p class="share-download">'+link(BASE+'atlas-intro-'+key+'-'+lang+'.txt','TXTをダウンロード' if ja else 'Download TXT',True)+'</p>'
    output+='<label for="share-atlas-url-'+lang+'">'+('アトラスのURL' if ja else 'Atlas URL')+'</label><input id="share-atlas-url-'+lang+'" class="share-url" type="url" readonly value="'+esc(copy['atlas_url']+'?lang='+lang)+'">'
    output+='<label for="share-preview-url-'+lang+'">'+('日本語の共有プレビューを使うURL' if ja else 'URL for an English sharing preview')+'</label><input id="share-preview-url-'+lang+'" class="share-url" type="url" readonly value="'+ORIGIN+BASE+lang+'/">'
    output+='<p class="share-scope">'+('SNS等のプレビュー言語を選ぶ場合は、この言語別URLを共有します。' if ja else 'Share this language-specific URL when you want an English link-preview image.')+'</p>'
    output+='<figure class="share-image"><img src="'+BASE+'atlas-intro-'+lang+'.png" width="1200" height="630" loading="lazy" alt="'+esc(c['image']['title']+' '+c['image']['subtitle'])+'"><figcaption>'+('手法選び・実行・結果照合の流れを示す紹介画像（1200×630）。' if ja else 'An introduction graphic showing method choice, execution and result checks (1200×630).')+'</figcaption></figure>'
    output+='<nav class="share-downloads" aria-label="'+('共有素材のダウンロード' if ja else 'Download sharing materials')+'">'+link(BASE+'atlas-intro-'+lang+'.png','PNG / 1200×630',True)+link(BASE+'atlas-intro-'+lang+'.svg','SVG / 1200×630',True)+link(BASE+'atlas-intro-'+lang+'.txt','紹介文とリンク一式 / TXT' if ja else 'Text and links / TXT',True)+'</nav></section>'
    output+='<section class="share-ai"><h2>'+('AIも、出典と条件を保ってたどれる' if ja else 'AI can follow the evidence and conditions too')+'</h2><p>'+('公開ページと機械可読な台帳から、手法の条件、コード版、入力、参照値と許容誤差へ進めます。AIの回答には出典を添え、元の資料と推論を区別してください。' if ja else 'Public pages and machine-readable registries connect method conditions, code editions, inputs, references and tolerances. Cite sources in AI answers and distinguish the source material from inference.')+'</p><nav>'+link('/llms.txt','AI向け案内' if ja else 'AI site guide')+link('/numerical-methods-atlas/code-and-data/examples.json','実行例の台帳 / JSON' if ja else 'Execution registry / JSON')+link('/using/?lang='+lang,'使い方と引用' if ja else 'Use and citation')+'</nav></section>'
    output+='<section class="share-terms"><h2>'+('利用条件と更新' if ja else 'Terms and updates')+'</h2><p>'+esc(copy['sharing_terms'][lang])+'</p><p>'+link('/rights/?lang='+lang,'利用条件・AI方針' if ja else 'Rights and AI policy')+' · '+link(BASE+'sharing.json','紹介素材の台帳 / JSON' if ja else 'Sharing metadata / JSON')+'</p><p class="share-scope">'+('台帳確認日：' if ja else 'Registry review: ')+esc(copy['reviewed_on'])+' · Hiroshi Koyama</p></section></section>'
    return output


def document(copy,counts,examples,discoveries,lang,fixed=False):
    c=copy['copy'][lang];url=ORIGIN+BASE+(lang+'/' if fixed else '')
    title=c['title'];description=formatted(copy,counts,lang,'description')
    image=ORIGIN+BASE+'atlas-intro-'+lang+'.png'
    css=sha((ROOT/'styles/atlas-sharing.css').read_bytes())[:12]
    head='<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    if fixed:head+='<title>'+esc(title)+'</title><meta name="description" content="'+esc(description)+'">'
    else:
        head+='<title data-page-title-ja="'+esc(copy['copy']['ja']['title'])+'" data-page-title-en="'+esc(copy['copy']['en']['title'])+'">'+esc(title)+'</title>'
        head+='<meta name="description" content="'+esc(description)+'" data-description-ja="'+esc(formatted(copy,counts,'ja','description'))+'" data-description-en="'+esc(formatted(copy,counts,'en','description'))+'">'
    head+='<link rel="canonical" href="'+url+'">'
    head+=''.join('<link rel="alternate" hreflang="'+l+'" href="'+ORIGIN+BASE+l+'/">' for l in ['ja','en'])+'<link rel="alternate" hreflang="x-default" href="'+ORIGIN+BASE+'">'
    head+='<meta property="og:type" content="website"><meta property="og:locale" content="'+('ja_JP' if lang=='ja' else 'en_US')+'"><meta property="og:url" content="'+url+'"><meta property="og:title" content="'+esc(title)+'"><meta property="og:description" content="'+esc(description)+'"><meta property="og:image" content="'+image+'"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="'+esc(c['image']['title']+' '+c['image']['subtitle'])+'">'
    head+='<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="'+esc(title)+'"><meta name="twitter:description" content="'+esc(description)+'"><meta name="twitter:image" content="'+image+'"><meta name="twitter:image:alt" content="'+esc(c['image']['title']+' '+c['image']['subtitle'])+'">'
    # The common chrome refresh replaces only this marked shared-assets block.
    head+='<!-- site-head --><link rel="stylesheet" href="/site.css"><script src="/site.js" defer></script><!-- /site-head -->'
    head+='<link rel="stylesheet" href="/styles/atlas-sharing.css?v='+css+'"></head>'
    attrs=' data-content-language="'+lang+'"' if fixed else ' data-site-language-anchors="suffix"'
    languages=[lang] if fixed else ['ja','en']
    return head+'<body class="profile-page"'+attrs+'><main id="main" class="profile-main atlas-sharing-main">'+''.join(body(copy,counts,examples,discoveries,l,not fixed) for l in languages)+'</main></body></html>\n'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font',help='Japanese-capable TrueType/OpenType font; no font is redistributed')
    args=parser.parse_args()
    copy,counts,examples,discoveries,source_hashes=load()
    DEST.mkdir(parents=True,exist_ok=True)
    previous=json.loads((DEST/'build.json').read_text()) if (DEST/'build.json').is_file() else {}
    renderer=previous.get('renderer',{})
    images={}
    script_hash=sha(Path(__file__).read_bytes())
    rendered={lang:{'items':scene(copy,counts,lang)} for lang in ['ja','en']}
    for lang in ['ja','en']:
        items=rendered[lang]['items'];svg_text=svg(copy,counts,lang,items)
        write('atlas-intro-'+lang+'.svg',svg_text)
        # Text/layout/code identity is independent of locally installed fonts.
        content_key=sha((svg_text+script_hash).encode())
        path=DEST/('atlas-intro-'+lang+'.png');prior=previous.get('images',{}).get(lang,{})
        rendered[lang].update(svg=svg_text,content_key=content_key,path=path,
                             redraw=content_key!=prior.get('content_input_sha256') or not valid_png(path,prior.get('png_sha256')))
    font_record=previous.get('font',{})
    font=find_font(args.font) if args.font else None
    if font is not None and sha(font.read_bytes())!=font_record.get('sha256'):
        for record in rendered.values():record['redraw']=True
    if any(record['redraw'] for record in rendered.values()):
        font=font or find_font(None)
        font_hash=sha(font.read_bytes())
        if font_hash!=font_record.get('sha256'):
            for record in rendered.values():record['redraw']=True
        font_record={'filename':font.name,'sha256':font_hash}
    for lang,record in rendered.items():
        if record['redraw']:renderer=png(record['path'],record['items'],font)
        key=sha((record['svg']+font_record['sha256']+script_hash).encode())
        images[lang]={'svg_sha256':sha(record['svg'].encode()),'png_sha256':sha(record['path'].read_bytes()),
                      'content_input_sha256':record['content_key'],'render_input_sha256':key,'width':1200,'height':630}
        for kind in ['short','paragraph']:write('atlas-intro-'+kind+'-'+lang+'.txt',intro_text(copy,counts,lang,kind))
        write('atlas-intro-'+lang+'.txt',intro_text(copy,counts,lang))
        write(lang+'/index.html',document(copy,counts,examples,discoveries,lang,True))
    write('index.html',document(copy,counts,examples,discoveries,'ja'))
    public={**copy,'url':ORIGIN+BASE,'counts':counts,'sources':source_hashes,
            'introductions':{lang:{key:formatted(copy,counts,lang,key) for key in ['short','paragraph','description']} for lang in ['ja','en']},
            'assets':{lang:{'svg':ORIGIN+BASE+'atlas-intro-'+lang+'.svg','png':ORIGIN+BASE+'atlas-intro-'+lang+'.png','text':ORIGIN+BASE+'atlas-intro-'+lang+'.txt','preview_url':ORIGIN+BASE+lang+'/'} for lang in ['ja','en']}}
    write('sharing.json',encode(public))
    write('build.json',encode({'schema_version':1,'sources':source_hashes,'builder_sha256':script_hash,
                              'renderer':renderer,'font':font_record,'images':images}))
    write('render-requirements.txt',copy['renderer']['dependency']+'\n')
    write('BUILD.md','# Rebuilding the atlas introduction assets\n\n'
          'From the site repository root, use a Python environment with Pillow:\n\n'
          '```sh\npython -m pip install -r numerical-methods-atlas/share/render-requirements.txt\n'
          'python scripts/build-atlas-sharing.py\n```\n\n'
          'Use `--font /path/to/Japanese-capable-font.ttf` when automatic Hiragino/Noto CJK detection does not apply. '
          'Font binaries are not redistributed. The recorded font hash, Pillow/FreeType versions and source hashes are in build.json. '
          'SVG and PNG use the same text and flat drawing instructions; PNG text widths are checked before output. '
          'Unchanged PNGs are reused only after their render-input hash, file hash and 1200×630 dimensions match, '
          'so an ordinary unchanged refresh needs only the Python standard library and no locally installed Japanese font. '
          'Changed graphics require Pillow; failures are explicit and stale images are not silently accepted.\n\n'
          'These are introduction graphics, not new scientific results. Counts come from the shared catalogs and coverage inventory. '
          'Existing rights apply: https://hrkoyama.github.io/rights/\n')
    print('Built bilingual atlas sharing materials:',counts['execution_examples'],'examples;',counts['methods'],'existing methods;',counts['method_records'],'status records.')


if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError,RuntimeError) as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(1)
