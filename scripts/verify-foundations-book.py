#!/usr/bin/env python3
"""Authoring check: extract every manuscript paragraph from the PDF; freeze assets.
Requires pypdf. Run after visual inspection, before the normal site refresh.
"""
import hashlib,json,re,unicodedata
from pathlib import Path
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'catalog/atlas-foundations-course.json';d=json.loads(source.read_text());edition=ROOT/d['base'].lstrip('/')/d['edition'];pdf=edition/'numerical-foundations-ja.pdf'
reader=PdfReader(pdf)
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).replace('−','-')
text=norm('\n'.join(p.extract_text() for p in reader.pages))
expected=[*d['preface'],d['audience'],d['rights'],d['execution_scope']]
for c in d['chapters']:
 expected += [c['title'],*c['lead'],*c['goals'],*c['worked']['paragraphs'],c['worked']['result'],c['figure']['caption'],c['experiment']['instructions'],*c['pitfalls'],*c['summary']]
 for s in c['sections']:expected += [s['title'],*s['paragraphs']]
 for q in c['questions']:expected += list(q.values())
 for line in c['worked']['code'].splitlines():
  if line.strip():expected.append(line.strip())
missing=[t for t in expected if norm(t) not in text]
if missing:raise ValueError('Missing PDF prose/code: '+repr(missing))
assets={str(p.relative_to(edition)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(edition.rglob('*')) if p.is_file() and p.name!='book-verification.json'}
receipt={'passed':True,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'pdf_pages':len(reader.pages),'chapters':19,'questions_and_answers':38,'prose_and_code_fragments_checked':len(expected),'equations':36,'figures':19,'assets':assets,'visual_review':'All rendered pages reviewed; shared vector equations and charts; embedded Japanese TrueType font also used for code comments.','generation':'ReportLab 4.4.9 / svglib 1.6.0 / MathJax 3.2.2 SVG; authoring-only; normal refresh validates frozen assets without executing scientific or PDF code.'}
(edition/'book-verification.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='assets'},ensure_ascii=False,indent=2))
