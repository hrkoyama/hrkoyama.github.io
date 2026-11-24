"""Extract PDF body while auditing, rather than silently dropping, the fixed footer.

The ReportLab document reserves y<62pt for its footer at y=30pt. pypdf's
documented visitor/mult API locates fragments in page coordinates. Every
nonblank fragment below50pt must be exactly our footer and the page number.
https://github.com/py-pdf/pypdf/blob/main/docs/user/extract-text.md
"""
import re,unicodedata
from pypdf import mult

def normalize(text):
    return re.sub(r'\s+','',unicodedata.normalize('NFKC',text)).replace('−','-')

def extract_body(reader):
    pages=[]
    for number,page in enumerate(reader.pages,1):
        body=[];footer=[]
        def visitor(text,cm,tm,font,size):
            if not text.strip():
                body.append(text)
                return
            y=mult(tm,cm)[5]
            (footer if y<50 else body).append(text)
        page.extract_text(visitor_text=visitor)
        expected=normalize('Numerical Foundations /2026-11-24')+str(number)
        assert normalize(''.join(footer))==expected,('Unexpected footer-region text',number,footer)
        pages.append(''.join(body))
    return '\n'.join(pages)
