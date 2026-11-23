#!/usr/bin/env python3
"""Merge explicitly reviewed benchmark bibliography and preserve other records."""
from pathlib import Path
import json
import re
ROOT=Path(__file__).resolve().parents[1]
def build(root=ROOT):
    refs=json.loads((root/'catalog/atlas-benchmark-references.json').read_text())['references']
    path=root/'numerical-methods-atlas/references.json'
    library=[x for x in json.loads(path.read_text()) if x.get('origin')!='atlas-benchmark-references']
    for row in refs:
        matches=[x for x in library if x['id']==row['id'] or (row.get('doi') and x.get('doi','').lower()==row['doi'].lower())]
        if matches:raise ValueError('Benchmark bibliography would duplicate an existing record: '+row['id'])
        library.append(row)
    path.write_text(json.dumps(library,ensure_ascii=False,indent=2)+'\n')
    path=root/'numerical-methods-atlas/assets/references.bib'
    text=re.sub(r'\n% BEGIN BENCHMARK REFERENCES\n.*?% END BENCHMARK REFERENCES\n?','',path.read_text(),flags=re.S).rstrip()+'\n'
    entries=[]
    for row in refs:
        fields={key:row[key] for key in ['author','title','year','journal','volume','number','pages','doi','version'] if key in row}
        fields['url']=row['source']
        entries.append('@'+('article' if row['type']=='article' else 'misc')+'{'+row['id']+',\n'+',\n'.join('  '+key+' = {'+str(value)+'}' for key,value in fields.items())+'\n}')
    path.write_text(text+'\n% BEGIN BENCHMARK REFERENCES\n'+'\n\n'.join(entries)+'\n% END BENCHMARK REFERENCES\n')
    print('Merged benchmark bibliography:',len(refs),'records, with original-problem/software roles.')
if __name__=='__main__':build()
