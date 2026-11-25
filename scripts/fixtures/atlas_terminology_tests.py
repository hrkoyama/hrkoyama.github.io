"""Editorial metadata tests only: no solver, ZIP loader or generator execution."""
import ast
from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts'))
import atlas_terminology as t


def read(path):
    return json.loads(path.read_text())


def source_function(path, name, namespace):
    tree = ast.parse((ROOT/path).read_text())
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), 'exec'), namespace)
    return namespace[name]


class TerminologyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=os.environ['ATLAS_TERMINOLOGY_TEST_SCRATCH'])
        self.root = Path(self.temp.name)
        self.mapping = read(ROOT/t.MAPPING)
        for relative in [t.MAPPING, t.HELPER]+[v['source']['path'] for v in self.mapping['cases'].values()]:
            target = self.root/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/relative, target)
        self.raw = {}
        for ident, row in self.mapping['cases'].items():
            value = read(self.root/row['source']['path'])
            self.raw[ident] = next(x for x in (value['cases'] if isinstance(value, dict) else value) if x['id'] == ident)

    def tearDown(self):
        self.temp.cleanup()

    def write_mapping(self, value):
        (self.root/t.MAPPING).write_text(json.dumps(value, ensure_ascii=False))

    def test_01_exact_ten_text_leaves_copy_and_provenance(self):
        original = deepcopy(self.raw)
        count = 0
        for ident, raw in self.raw.items():
            value = t.project_case(self.root, raw)
            marker = value.pop('editorial_terminology')
            restored = deepcopy(value)
            for field, replacement in self.mapping['cases'][ident]['fields'].items():
                self.assertEqual(value[field]['ja'], replacement['after'])
                self.assertEqual(value[field]['en'], raw[field]['en'])
                restored[field]['ja'] = replacement['before']
                count += 1
            self.assertEqual(restored, raw)
            self.assertEqual(marker['editorial_source_sha256'], {name: sha256((self.root/name).read_bytes()).hexdigest() for name in [t.MAPPING,t.HELPER]})
            binding = marker['raw_source']
            self.assertEqual(binding['sha256'], sha256((self.root/binding['path']).read_bytes()).hexdigest())
            self.assertEqual(marker['raw_case_canonical_sha256'], sha256(t._canonical(raw)).hexdigest())
            pointed = read(self.root/binding['path'])
            for part in binding['case_pointer'].strip('/').split('/'):
                pointed = pointed[int(part)] if isinstance(pointed,list) else pointed[part]
            self.assertEqual(pointed,raw)
        self.assertEqual(count,10)
        self.assertEqual(self.raw,original)

    def test_02_strict_idempotency_and_public_extra_fields(self):
        for raw in self.raw.values():
            first = t.project_case(self.root, {**raw,'measured':{'passed':True,'error':0.0003}})
            second = t.project_case(self.root,first)
            self.assertEqual(first,second)
            self.assertIsNot(first,second)
            second['measured']['error']=9
            self.assertEqual(first['measured']['error'],0.0003)
            unproven=deepcopy(first);del unproven['editorial_terminology']
            with self.assertRaises(ValueError):t.project_case(self.root,unproven)
            stale=deepcopy(first);stale['editorial_terminology']['schema_version']=True
            with self.assertRaises(ValueError):t.project_case(self.root,stale)

    def test_03_reject_unrelated_input_language_reference_and_numeric_changes(self):
        raw=self.raw['radiation-transport']
        for key,value in [('title',{**raw['title'],'en':'changed'}),('method_ids',['unrelated']),('references',[]),('formulas',['new formula'])]:
            changed=deepcopy(raw);changed[key]=value
            if key not in raw:
                # Extra public decorations are preserved; an existing field is required for this negative.
                continue
            with self.subTest(key=key),self.assertRaises(ValueError):t.project_case(self.root,changed)
        altered=deepcopy(self.mapping)
        altered['cases']['radiation-transport']['fields']['title']['after']=17
        self.write_mapping(altered)
        with self.assertRaises(ValueError):t.project_case(self.root,raw)

    def test_04_reject_off_allowlist_and_changed_prose(self):
        mutations=[]
        for kind in ['language','field','wording','source']:
            value=deepcopy(self.mapping)
            row=value['cases']['radiation-transport']
            if kind=='language':value['language']='en'
            if kind=='field':row['fields']['validation']={'before':'x','after':'y'}
            if kind=='wording':row['fields']['title']['after']+=' extra claim'
            if kind=='source':row['source']['sha256']='0'*64
            mutations.append(value)
        for value in mutations:
            self.write_mapping(value)
            with self.assertRaises(ValueError):t.project_case(self.root,self.raw['radiation-transport'])

    def test_05_missing_or_tampered_sources_fail_closed(self):
        file=self.root/self.mapping['cases']['kepler-eccentricity']['source']['path']
        file.write_bytes(file.read_bytes()+b' ')
        with self.assertRaises(ValueError):t.project_case(self.root,self.raw['radiation-transport'])
        (self.root/t.MAPPING).unlink()
        with self.assertRaises(ValueError):t.project_case(self.root,self.raw['radiation-transport'])

    def test_06_unmapped_copy_needs_no_mapping_and_rejects_forged_marker(self):
        (self.root/t.MAPPING).unlink()
        raw={'id':'unrelated','value':{'number':3.5,'en':'unchanged'}}
        value=t.project_case(self.root,raw)
        self.assertEqual(value,raw);self.assertIsNot(value['value'],raw['value'])
        with self.assertRaises(ValueError):t.project_case(self.root,{**raw,'editorial_terminology':{}})

    def fixture_data(self,ident):
        row=self.mapping['cases'][ident];relative=row['source']['path'];parts=Path(relative).parts
        return {'group':parts[-2],'edition':parts[-3],'metadata':[deepcopy(self.raw[ident])],
                'results':{'cases':[{'id':ident,'passed':True}]},'base':'/'+str(Path(relative).parent)+'/',
                'test_urls':['https://hrkoyama.github.io/test.py'],'source_sha256':{relative:row['source']['sha256']},
                'directory':self.root/Path(relative).parent,'manifest':{},
                'verification':{'passed_tests':1,'archive':{'archive_directory':'fixture','file':'fixture.zip','sha256':'a'*64}}}

    def test_07_method_and_supplement_public_seams_close_without_raw_mutation(self):
        data={ident:self.fixture_data(ident) for ident in self.raw};original=deepcopy(data)
        lookup=lambda root,group,edition:next(x for x in data.values() if x['group']==group and x['edition']==edition)
        ns={'load_depth_group':lookup,'depth_code_urls':lambda data,ids:[],'ORIGIN':'https://hrkoyama.github.io'}
        method=source_function('scripts/atlas_depth_release.py','_depth_release_record',ns)
        config={'edition':'unused','groups':[{'id':v['group'],'edition':v['edition']} for v in data.values()]}
        path=self.root/'catalog/atlas-depth-expansion.json';path.write_text(json.dumps(config))
        ns={'json':json,'load_depth_group':lookup,'depth_code_urls':lambda data,ids:[], 'depth_gallery_figure':lambda *args:None}
        supplemental=source_function('scripts/atlas_goal_availability.py','load_supplemental_examples',ns)
        selected=supplemental(self.root,list(self.raw))
        self.assertEqual([x['id'] for x in selected],list(self.raw))
        for public in selected:
            ident=public['id'];fixture=data[ident]
            record=method(self.root,{'id':self.raw[ident]['method_ids'][0],'status':'educational-example'},
                          {'group':fixture['group'],'edition':fixture['edition'],'case_ids':[ident]})
            self.assertEqual(record['examples'][0]['title'],public['title'])
            self.assertEqual(record['examples'][0]['editorial_terminology'],public['editorial_terminology'])
            self.assertEqual(record['editorial_source_sha256'],t.editorial_sources(public))
            self.assertEqual(t.project_case(self.root,public),public)
            for name,checksum in fixture['source_sha256'].items():self.assertEqual(public['source_sha256'][name],checksum)
        self.assertEqual(data,original)

    def test_08_exact_builder_projection_expression_preserves_raw_cases(self):
        tree=ast.parse((ROOT/'scripts/build-atlas-depth-examples.py').read_text())
        build=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='build')
        loop=next(n for n in build.body if isinstance(n,ast.For) and ast.unparse(n.target)=='current')
        values=[{'metadata':list(self.raw.values())}]
        before=deepcopy(values)
        namespace={'data':{'fixture':values[0]},'ROOT':self.root,'project_cases':t.project_cases,
                   'with_formula_supplement':lambda case,supplement:deepcopy(case),'formula_supplements':{}}
        exec(compile(ast.Module(body=[loop],type_ignores=[]),'exact-builder-metadata-loop','exec'),namespace)
        self.assertEqual(values[0]['metadata'],t.project_cases(self.root,before[0]['metadata']))
        self.assertEqual(self.raw,{case['id']:case for case in before[0]['metadata']})
        self.assertEqual([c['id'] for c in values[0]['metadata']],list(self.raw))


if __name__=='__main__':
    unittest.main(verbosity=2)
