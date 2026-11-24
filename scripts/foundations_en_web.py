"""Render English course HTML from its PDF manuscript; never generate PDF or science."""
import json
from html import escape as e
from foundations_en_contract import ROOT,SOURCE,sha,verify_frozen

ORIGIN='https://hrkoyama.github.io'
JA='/numerical-methods-atlas/learn/numerical-foundations/'

def build(root=ROOT):
    d,receipt=verify_frozen(root)
    base=d['base'];assets=d['assets_base'];out=root/base.lstrip('/')
    pdf=base+d['edition']+'/numerical-foundations-en.pdf'
    release=json.loads((root/'code/numerical-foundations/2026-11-24/release.json').read_text())
    assert sha(root/release['zip'].lstrip('/'))==release['zip_sha256']
    for path,digest in release['source_files'].items():assert sha(root/path)==digest,path
    def paragraphs(values):return ''.join('<p>'+e(v)+'</p>' for v in values)
    def bullets(values):return '<ul>'+''.join('<li>'+e(v)+'</li>' for v in values)+'</ul>'
    def layout(title,body,route):
        counterpart=JA+route[len(base):]
        head='<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+e(title)+' | Numerical Foundations</title><meta name="description" content="A 19-chapter beginner course on numerical error, stability, dissipation, dispersion, boundaries, splitting and symplectic integration. Matching Web/PDF with verified examples and answers.">'
        head+='<link rel="canonical" href="'+ORIGIN+route+'"><link rel="alternate" hreflang="en" href="'+ORIGIN+route+'"><link rel="alternate" hreflang="ja" href="'+ORIGIN+counterpart+'"><link rel="stylesheet" href="/styles/atlas-foundations-course.css?v='+sha(root/'styles/atlas-foundations-course.css')[:12]+'">'
        nav='<nav aria-label="Breadcrumb"><a href="/numerical-methods-atlas/en/read/">Atlas reading</a> / <a href="'+base+'">Numerical foundations</a></nav><nav class="course-language" aria-label="Course language"><a href="'+counterpart+'" hreflang="ja" lang="ja">日本語</a> · <a href="'+route+'" hreflang="en" aria-current="page">English</a></nav>'
        footer='<footer><a href="'+base+'">Contents: all 19 chapters</a> · <a href="'+pdf+'">Same-content PDF</a> · <a href="'+release['zip']+'">Worked-example code ZIP</a><p>24 November 2026 edition · '+e(d['rights'])+'</p></footer>'
        return '<!doctype html><html lang="en"><head>'+head+'</head><body data-content-language="en"><main>'+nav+body+footer+'</main></body></html>\n'
    body='<p class="eyebrow">NUMERICAL METHODS ATLAS / FOUNDATIONS</p><h1>'+e(d['title'])+'</h1><p class="subtitle">'+e(d['subtitle'])+'</p><p>19 chapters · 19 figures · 38 review questions with answers · 24 November 2026</p>'
    body+='<div class="downloads"><a href="'+pdf+'">Download the PDF</a><a href="'+release['zip']+'">Small-example code ZIP</a><a href="/'+SOURCE+'">Shared manuscript JSON</a></div><section><h2 id="start">Introduction</h2>'+paragraphs(d['preface'])+'<p>Audience: '+e(d['audience'])+'</p><p>Run code snippets from the extracted ZIP directory. Enter the Chapter 19 commands in a shell rather than Python.</p></section>'
    for part in d['parts']:
        body+='<section><h2 id="'+part['id']+'">'+e(part['title'])+'</h2><ol start="'+part['range'].split('-')[0]+'">'+''.join('<li><a href="'+base+c['id']+'/">'+e(c['title'])+'</a><p>'+e(c['goals'][0])+'</p></li>' for c in d['chapters'] if c['part']==part['id'])+'</ol></section>'
    body+='<section><h2 id="symbols">Frequently used notation</h2><dl>'+''.join('<dt>'+e(t)+'</dt><dd>'+e(v)+'</dd>' for t,v in d['glossary'])+'</dl></section><section><h2 id="lab">Using the examples</h2>'+paragraphs(d['lab_guide'])+'</section><section><h2 id="references">References and reproduction</h2>'
    for r in d['references']:body+='<h3><a href="'+r['url']+'">'+e(r['title'])+'</a></h3><p>'+e(r['scope'])+'</p>'
    body+='<h3>Scope of the computations and production</h3><p>'+e(d['execution_scope'])+'</p></section>'
    out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(layout(d['title'],body,base))
    for c in d['chapters']:
        body='<p class="eyebrow">Chapter '+str(c['n'])+' / 19</p><h1>'+e(c['title'])+'</h1>'+''.join('<p class="goal">Learning goal: '+e(t)+'</p>' for t in c['goals'])+paragraphs(c['lead']);eq=0
        for i,s in enumerate(c['sections'],1):
            body+='<section><h2 id="section-'+str(i)+'">'+e(s['title'])+'</h2>'+paragraphs(s['paragraphs'])
            for formula in s['equations']:
                eq+=1;body+='<div class="equation"><img src="'+assets+'equations/equation-'+c['id']+'-'+str(eq)+'.svg" alt="'+e(formula['plain'],quote=True)+'"></div>'
            body+='</section>'
        fig=assets+'figures/'+c['figure']['id']
        body+='<section><h2 id="example">A small worked example</h2>'+paragraphs(c['worked']['paragraphs'])+'<pre><code>'+e(c['worked']['code'])+'</code></pre><p>'+e(c['worked']['result'])+'</p><figure><a href="'+fig+'.svg"><img src="'+fig+'.svg" alt="'+e(c['figure']['alt'],quote=True)+'" width="760" height="350" loading="lazy"></a><figcaption>'+e(c['figure']['caption'])+'</figcaption></figure><p class="data">Saved data: '+e(c['experiment']['data'])+'</p><p>'+e(c['experiment']['instructions'])+'</p><p><a href="'+release['zip']+'">Get code, inputs, saved CSVs, and tests</a> / <a href="'+fig+'.png">Figure PNG</a> / <a href="'+fig+'.pdf">Figure PDF</a></p></section><section><h2 id="questions">Review questions and answers</h2>'
        for i,q in enumerate(c['questions'],1):body+='<p>Question '+str(i)+': '+e(q['question'])+'</p><details><summary>Show answer</summary><p>'+e(q['answer'])+'</p></details>'
        body+='</section><section><h2 id="pitfalls">Common pitfalls</h2>'+bullets(c['pitfalls'])+'</section><section><h2 id="summary">Key points</h2>'+bullets(c['summary'])+'</section><section><h2 id="reading">Continue in the atlas</h2><ul>'+''.join('<li><a href="'+d['readings'][k]['url']+'">'+e(d['readings'][k]['title'])+'</a></li>' for k in c['readings'])+'</ul></section>'
        body+='<nav class="chapter-nav" aria-label="Chapter navigation">'+('<a rel="prev" href="'+base+f'{c["n"]-1:02d}/">Previous chapter</a>' if c['n']>1 else '<a href="'+base+'">Introduction</a>')+'<a href="'+base+'">Contents</a>'+('<a rel="next" href="'+base+f'{c["n"]+1:02d}/">Next chapter</a>' if c['n']<19 else '<a href="'+base+'#references">References</a>')+'</nav>'
        target=out/c['id'];target.mkdir(exist_ok=True);(target/'index.html').write_text(layout(c['title'],body,base+c['id']+'/'))
    print('Built English index +19 chapters; exact PDF manuscript and shared science verified.')
