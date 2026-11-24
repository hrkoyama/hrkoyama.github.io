"""Build the PDF from the same catalog and frozen SVGs as the Web edition.
Authoring-only: requires ReportLab 4.4.9, svglib 1.6.0, and an embedded CJK TTF.
Normal site/index refresh never invokes this script.
"""
import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, KeepTogether, Flowable
from svglib.svglib import svg2rlg

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'numerical-methods-atlas/learn/numerical-foundations'
EDITION = BASE / '2026-11-24'


class Vector(Flowable):
    def __init__(self, path, maximum_width=475, maximum_height=230):
        super().__init__()
        self.drawing = svg2rlg(str(path))
        scale = min(maximum_width / self.drawing.width, maximum_height / self.drawing.height, 1.0)
        self.drawing.scale(scale, scale)
        self.width = self.drawing.width * scale
        self.height = self.drawing.height * scale
        self.hAlign = 'LEFT'
    def draw(self):
        from reportlab.graphics import renderPDF
        renderPDF.draw(self.drawing, self.canv, 0, 0)


def build(font):
    source = ROOT / 'catalog/atlas-foundations-course.json'
    d = json.loads(source.read_text())
    pdfmetrics.registerFont(TTFont('JP', font))
    styles = {
        'body': ParagraphStyle('body', fontName='JP', fontSize=9.6, leading=15, spaceAfter=6, wordWrap='CJK', textColor=colors.HexColor('#19343b')),
        'h1': ParagraphStyle('h1', fontName='JP', fontSize=21, leading=29, spaceAfter=18, wordWrap='CJK', keepWithNext=True, textColor=colors.HexColor('#006d77')),
        'h2': ParagraphStyle('h2', fontName='JP', fontSize=12.3, leading=18, spaceBefore=9, spaceAfter=6, wordWrap='CJK', keepWithNext=True, textColor=colors.HexColor('#006d77')),
        'small': ParagraphStyle('small', fontName='JP', fontSize=8.2, leading=11.8, spaceAfter=5, wordWrap='CJK', textColor=colors.HexColor('#48636a')),
        'code': ParagraphStyle('code', fontName='JP', fontSize=8, leading=11, backColor=colors.HexColor('#f0f5f5'), borderPadding=8, spaceBefore=8, spaceAfter=12),
    }
    story=[]
    def p(text, kind='body'):
        story.append(Paragraph(escape(text), styles[kind]))
    def heading(t):p(t,'h2')
    p('NUMERICAL METHODS ATLAS / FOUNDATIONS','small')
    p(d['title'],'h1');p(d['subtitle']);p('初学者のための19章 / 2026年11月24日版')
    for t in d['preface']:p(t)
    p('想定読者：'+d['audience'])
    p('WebとPDFは、共通の章原稿・数式SVG・図から作成しています。Webの折りたたみ解答はPDFではすべて表示します。')
    p('Web: https://hrkoyama.github.io'+d['base'],'small')
    story.append(PageBreak());p('目次と記号','h1')
    for part in d['parts']:
        heading(part['title'])
        for c in d['chapters']:
            if c['part']==part['id']:p(str(c['n'])+'　'+c['title'])
    story.append(PageBreak());p('よく使う記号','h1')
    for term,meaning in d['glossary']:p(term+'：'+meaning)
    p('計算例の読み方','h2');p('コード断片を実行する際は、配布ZIPを展開したディレクトリで実行します。第19章のコマンドだけはPythonではなくシェルに入力します。図・保存結果・入力の照合は verify_release.py が行います。')
    for c in d['chapters']:
        story.append(PageBreak());p(f'第{c["n"]}章　{c["title"]}','h1')
        for t in c['goals']:p('到達目標：'+t,'small')
        for t in c['lead']:p(t)
        equation=0
        for s in c['sections']:
            heading(s['title'])
            for t in s['paragraphs']:p(t)
            for e in s['equations']:
                equation+=1;story.append(Vector(EDITION/'equations'/f'equation-{c["id"]}-{equation}.svg',475,75));story.append(Spacer(1,9))
        heading('小さな計算例')
        for t in c['worked']['paragraphs']:p(t)
        story.append(KeepTogether([Preformatted(c['worked']['code'],styles['code'],maxLineLength=100,splitChars=' ,',newLineChars='    ')]))
        p(c['worked']['result'])
        story.append(Vector(EDITION/'figures'/(c['figure']['id']+'.svg'),475,205))
        p(c['figure']['caption'],'small')
        p('保存データ：'+c['experiment']['data'],'small');p(c['experiment']['instructions'],'small')
        heading('確認問題と解答')
        for i,q in enumerate(c['questions'],1):
            p(f'問{i}　'+q['question']);p('解答　'+q['answer'])
        heading('つまずきやすい点')
        for t in c['pitfalls']:p('・'+t)
        heading('この章の要点')
        for t in c['summary']:p('・'+t)
        heading('アトラスで先を読む')
        for key in c['readings']:
            r=d['readings'][key];p(r['title']);p(r['url'],'small')
    story.append(PageBreak());p('参考資料と再現手順','h1')
    for ref in d['references']:
        heading(ref['title']);p(ref['scope']);p(ref['url'],'small')
    heading('教材の実行・制作範囲');p(d['execution_scope']);p(d['rights'])
    p('コード配布： https://hrkoyama.github.io/code/numerical-foundations/2026-11-24/numerical-foundations-lab-2026-11-24.zip','small')
    p('原稿： https://hrkoyama.github.io/catalog/atlas-foundations-course.json','small')
    def footer(canvas, doc):
        canvas.saveState();canvas.setStrokeColor(colors.HexColor('#bfd0d3'));canvas.line(58,44,537,44)
        canvas.setFont('JP',8);canvas.setFillColor(colors.HexColor('#48636a'));canvas.drawString(58,30,'数値計算の基礎 / 2026-11-24');canvas.drawRightString(537,30,str(doc.page));canvas.restoreState()
    dest=EDITION/'numerical-foundations-ja.pdf'
    SimpleDocTemplate(str(dest),pagesize=(595.28,841.89),leftMargin=58,rightMargin=58,topMargin=48,bottomMargin=62,title=d['title'],author='hrkoyama',pageCompression=1).build(story,onFirstPage=footer,onLaterPages=footer)
    print(dest)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--font',required=True);build(parser.parse_args().font)
