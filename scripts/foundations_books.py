"""Resolve separately verified print editions; never rebuild PDFs or science."""
import hashlib,json,re
from pathlib import Path,PurePosixPath

REGISTRY='catalog/atlas-foundations-books.json'
EDITION='2026-11-25'
BASE='numerical-methods-atlas/learn/numerical-foundations/'
BOOKS=BASE+'books/'+EDITION+'/'
CONTACT='hrkoyamacontact@gmail.com'
SOURCE={'ja':'catalog/atlas-foundations-course.json','en':'catalog/atlas-foundations-course.en.json'}
SOURCE_SHA={'ja':'231338afd44d8126863eba326dbc98ff9a2a9efd85cc5a228a503835f51cf9d9','en':'1b1dceef84892e3c113ca080b1fea1217af0c335b3a0c616e1e3610dc38807f2'}
PREVIOUS={'ja':{'path':BASE+'2026-11-24/numerical-foundations-ja.pdf','sha256':'99fd73f16f8af17ef0d6addb35b6ef3034879854b1919fe11b030a6a6e2ea74d'},'en':{'path':BASE+'en/2026-11-24/numerical-foundations-en.pdf','sha256':'d0c61b494711e9abce178425f6c2e3f7268a060f322593d70a0f133427847c5d'}}
PAPER={'ja':{'name':'A4','width_pt':595.2755905511812,'height_pt':841.8897637795277},'en':{'name':'USLetter','width_pt':612,'height_pt':792}}
PDF={'ja':BOOKS+'numerical-foundations-ja-a4.pdf','en':BOOKS+'numerical-foundations-en-letter.pdf'}
CHECKS={'all_manuscript_fragments','chapter_fragments_in_order','all_19_chapters_38_answers_36_equations_19_figures','paper_all_pages','fonts_and_glyphs','exact_contact_text_and_mailto','actual_19_chapter_outline_map','print_request_and_console_checks','full_page_visual_review'}

def need(value,message):
    if not value:raise ValueError(message)
def digest(raw):return hashlib.sha256(raw).hexdigest()
def relative(name):
    need(isinstance(name,str) and name and '\\' not in name,'Noncanonical book path')
    part=PurePosixPath(name);need(not part.is_absolute() and '..' not in part.parts and part.as_posix()==name,'Noncanonical book path');return name
def parse(raw):
    need(len(raw)<=2*1024*1024,'Oversized book metadata')
    def pairs(items):
        value={}
        for key,item in items:need(key not in value,'Repeated book JSON key');value[key]=item
        return value
    value=json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda _:(_ for _ in ()).throw(ValueError('Nonfinite book metadata')))
    text=json.dumps(value,ensure_ascii=False,allow_nan=False)
    need(not any(marker in text for marker in ['/Users/','/private/','LOCAL-WORK-QUEUE','atlas-private-work-queue','codex-scratch']),'Private path in public book metadata')
    return value

def load_book_chain(read_bytes):
    """read_bytes supplies actual local or HR bytes; proof checks never execute."""
    registry=parse(read_bytes(REGISTRY))
    need(registry.get('state')=='FROZEN_VERIFIED' and registry.get('schema_version')==1,'Unbound book registry')
    need(registry['origin']=='https://hrkoyama.github.io' and registry['current_layout_edition']==EDITION,'Wrong book origin/edition')
    def bound(binding):
        name=relative(binding['path']);need(re.fullmatch('[0-9a-f]{64}',binding['sha256'] or ''),'Unbound book SHA')
        raw=read_bytes(name);need(digest(raw)==binding['sha256'],'Book evidence SHA differs: '+name);return raw
    need(registry['edition_manifest']['path']==BOOKS+'manifest.json' and registry['book_verification']['path']==BOOKS+'book-verification.json','Wrong versioned book evidence paths')
    manifest=parse(bound(registry['edition_manifest']));proof=parse(bound(registry['book_verification']))
    need(manifest.get('schema_version')==proof.get('schema_version')==1,'Unknown book evidence schema')
    need(manifest['state']==proof['state']=='FROZEN_VERIFIED' and proof['passed'] is True,'Actual book QA PASS required')
    need(manifest['layout_edition']==proof['layout_edition']==EDITION and manifest['manuscript_edition']=='2026-11-24','Book editions differ')
    need(proof['edition_manifest']==registry['edition_manifest'],'Book proof/manifest binding differs')
    need(manifest['contact']=={'email':CONTACT,'href':'mailto:'+CONTACT},'Wrong authorized book contact')
    need(proof['immutable_assets_and_manuscripts_unchanged'] is True and proof['science_rerun'] is False,'Old assets/source preservation not verified')
    need(set(registry['primary'])==set(manifest['books'])==set(proof['books'])=={'ja','en'},'Both language books required')
    for language in ['ja','en']:
        row=registry['primary'][language];book=manifest['books'][language];qa=proof['books'][language];pdf=row['pdf']
        need(row['web']=='/'+BASE+('en/' if language=='en' else ''),'Wrong language Web index')
        need(row['paper']==book['expected_paper']==PAPER[language] and book['measured_paper']=={'all_pages_checked':pdf['pages'],'maximum_allowed_deviation_pt':1,'rotation_degrees':0},'Wrong language paper evidence')
        need(row['previous_pdf']==PREVIOUS[language],'Original book alternate changed')
        need(row['manuscript']==book['manuscript']=={'path':SOURCE[language],'sha256':SOURCE_SHA[language]},'Original manuscript binding changed')
        need(digest(read_bytes(SOURCE[language]))==SOURCE_SHA[language],'Original manuscript bytes changed')
        need(pdf==book['pdf'] and pdf['path']==PDF[language] and type(pdf['bytes']) is int and 0<pdf['bytes']<=5*1024*1024 and type(pdf['pages']) is int and 19<=pdf['pages']<=120,'Unbound/invalid new PDF properties')
        payload=bound(pdf);need(payload.startswith(b'%PDF-') and len(payload)==pdf['bytes'],'Actual new PDF length/type differs')
        need(qa['pdf_sha256']==pdf['sha256'] and qa['pages']==pdf['pages'],'QA covers different PDF bytes/pages')
        need(set(qa['checks'])==CHECKS and all(value is True for value in qa['checks'].values()),'Incomplete actual book QA checks')
        count=602 if language=='ja' else 605
        need(book['expected_content']=={'chapters':19,'answered_questions':38,'equations':36,'figures':19,'prose_and_code_fragments':count} and qa['actual_fragments_checked']==count,'Incomplete manuscript/figure/question coverage')
        visual=qa['visual_review'];need(visual['completed'] is True and visual['all_page_count']==pdf['pages'] and re.fullmatch('[0-9a-f]{64}',visual['receipt_sha256'] or ''),'Actual full-page visual review required')
    return registry

def current_books(root):
    root=Path(root).resolve(strict=True)
    def read(name):
        path=root/relative(name);need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),'Missing/unsafe current book file')
        limit=5*1024*1024 if name.endswith('.pdf') else 2*1024*1024
        need(path.stat().st_size<=limit,'Oversized book input');return path.read_bytes()
    return load_book_chain(read)
