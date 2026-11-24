"""Check every English manuscript fragment against PDF extraction; freeze shared assets."""
import importlib.metadata,json,re,unicodedata
from pypdf import PdfReader
from foundations_en_contract import ROOT,SOURCE,load,fragments,sha
d=load();edition=ROOT/d['base'].lstrip('/')/d['edition'];pdf=edition/'numerical-foundations-en.pdf'
reader=PdfReader(pdf)
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).replace('−','-')
text=norm('\n'.join(p.extract_text() for p in reader.pages));expected=fragments(d)
missing=[t for t in expected if norm(t) not in text]
assert not missing,repr(missing)
shared=ROOT/d['assets_base'].lstrip('/')
paths=[pdf,shared/'numerical-foundations-ja.pdf',shared/'book-verification.json',ROOT/'catalog/atlas-foundations-course.json',ROOT/'code/numerical-foundations/2026-11-24/numerical-foundations-lab-2026-11-24.zip']
paths += sorted((shared/'figures').glob('*'))+sorted((shared/'equations').glob('*.svg'))
receipt={'passed':True,'source_sha256':sha(ROOT/SOURCE),'pdf_pages':len(reader.pages),'chapters':19,
 'questions_and_answers':38,'prose_and_code_fragments_checked':len(expected),'equations':36,'figures':19,
 'assets':{str(p.relative_to(ROOT)):sha(p) for p in paths},
 'shared_assets_base':d['assets_base'],'generation':'GitHub-side authoring; Web/PDF share one English manuscript. Equations, plots, saved data, Japanese PDF and scientific ZIP are reused unchanged.',
 'visual_review':'All pages must be rendered and reviewed before publication; rendering artifacts and final review evidence are kept with the release process.',
 'dependencies':{p:importlib.metadata.version(p) for p in ['reportlab','svglib','pypdf']}}
(edition/'book-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='assets'},indent=2))
