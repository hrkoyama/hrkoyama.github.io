"""Author English PDF on GitHub, sharing the frozen Japanese edition's SVGs."""
import argparse
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from foundations_en_contract import ROOT,load
from build_book import Vector
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Preformatted,KeepTogether,CondPageBreak

def build(font,mono):
    d=load(); assets=ROOT/d['assets_base'].lstrip('/')
    dest=ROOT/d['base'].lstrip('/')/d['edition']/'numerical-foundations-en.pdf'
    dest.parent.mkdir(parents=True,exist_ok=True)
    pdfmetrics.registerFont(TTFont('BookEN',font))
    pdfmetrics.registerFont(TTFont('CodeEN',mono))
    base=dict(fontName='BookEN',textColor=colors.HexColor('#19343b'),allowWidows=0,allowOrphans=0)
    styles={
      'body':ParagraphStyle('body',**base,fontSize=9.5,leading=14.5,spaceAfter=6),
      'h1':ParagraphStyle('h1',**base,fontSize=20,leading=26,spaceAfter=16,keepWithNext=True),
      'h2':ParagraphStyle('h2',**base,fontSize=12,leading=17,spaceBefore=10,spaceAfter=6,keepWithNext=True),
      'small':ParagraphStyle('small',**base,fontSize=8,leading=11.5,spaceAfter=5),
      'code':ParagraphStyle('code',fontName='CodeEN',fontSize=8,leading=11,backColor=colors.HexColor('#f0f5f5'),borderPadding=7,spaceBefore=8,spaceAfter=12),
    }
    story=[]
    def paragraph(text,kind='body'):return Paragraph(escape(text),styles[kind])
    def p(text,kind='body'):story.append(paragraph(text,kind))
    def h(text):p(text,'h2')
    p('NUMERICAL METHODS ATLAS / FOUNDATIONS','small')
    p(d['title'],'h1');p(d['subtitle']);p('A 19-chapter course for beginners / 24 November 2026')
    for t in d['preface']:p(t)
    p('Audience: '+d['audience'])
    p('The Web and PDF use the same manuscript, equation SVGs, and figures. All expandable Web answers are displayed in full here.')
    p('Web: https://hrkoyama.github.io'+d['base'],'small')
    story.append(PageBreak());p('Contents','h1')
    for part in d['parts']:
        h(part['title'])
        for c in d['chapters']:
            if c['part']==part['id']:p(str(c['n'])+'. '+c['title'])
    story.append(PageBreak());p('Frequently used notation','h1')
    for term,meaning in d['glossary']:p(term+': '+meaning)
    h('Using the examples')
    p('Run code snippets from the extracted ZIP directory. Enter the Chapter 19 commands in a shell rather than Python.')
    for t in d['lab_guide']:p(t)
    for c in d['chapters']:
        story.append(Spacer(1,18));story.append(CondPageBreak(420));p('Chapter '+str(c['n'])+': '+c['title'],'h1')
        for t in c['goals']:p('Learning goal: '+t,'small')
        for t in c['lead']:p(t)
        eq=0
        for s in c['sections']:
            h(s['title'])
            for t in s['paragraphs']:p(t)
            for formula in s['equations']:
                eq+=1;story.append(Vector(assets/'equations'/f'equation-{c["id"]}-{eq}.svg',475,75));story.append(Spacer(1,8))
        h('A small worked example')
        for t in c['worked']['paragraphs']:p(t)
        story.append(KeepTogether([Preformatted(c['worked']['code'],styles['code'],maxLineLength=95,splitChars=' ,',newLineChars='    ')]))
        p(c['worked']['result'])
        story.append(KeepTogether([Vector(assets/'figures'/(c['figure']['id']+'.svg'),475,205),paragraph(c['figure']['caption'],'small')]))
        p('Saved data: '+c['experiment']['data'],'small');p(c['experiment']['instructions'],'small')
        h('Review questions and answers')
        for i,q in enumerate(c['questions'],1):
            p('Question '+str(i)+': '+q['question']);p('Answer: '+q['answer'])
        h('Common pitfalls')
        for t in c['pitfalls']:p('- '+t)
        h('Key points')
        for t in c['summary']:p('- '+t)
        h('Continue in the atlas')
        for key in c['readings']:
            r=d['readings'][key];p(r['title']);p(r['url'],'small')
    story.append(PageBreak());p('References and reproduction','h1')
    for r in d['references']:h(r['title']);p(r['scope']);p(r['url'],'small')
    h('Scope of the computations and production');p(d['execution_scope']);p(d['rights'])
    p('Code ZIP: https://hrkoyama.github.io/code/numerical-foundations/2026-11-24/numerical-foundations-lab-2026-11-24.zip','small')
    p('Manuscript: https://hrkoyama.github.io/catalog/atlas-foundations-course.en.json','small')
    def footer(canvas,doc):
        canvas.saveState();canvas.setStrokeColor(colors.HexColor('#bfd0d3'));canvas.line(58,44,537,44)
        canvas.setFont('BookEN',8);canvas.setFillColor(colors.HexColor('#48636a'))
        canvas.drawString(58,30,'Numerical Foundations /2026-11-24');canvas.drawRightString(537,30,str(doc.page));canvas.restoreState()
    SimpleDocTemplate(str(dest),pagesize=(595.28,841.89),leftMargin=58,rightMargin=58,topMargin=48,bottomMargin=62,title=d['title'],author='hrkoyama',pageCompression=1).build(story,onFirstPage=footer,onLaterPages=footer)
    print(dest)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--font',required=True);p.add_argument('--mono',required=True);a=p.parse_args();build(a.font,a.mono)
