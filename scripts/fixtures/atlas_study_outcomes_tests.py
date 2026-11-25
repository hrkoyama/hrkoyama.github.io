# -*- coding: utf-8 -*-
"""Pure display fixtures: no solver, numerical library or full builder run."""
import ast
import base64
import copy
from html import escape
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import re
import struct
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT/'scripts/atlas_study_outcomes.py'
LEGACY_FIXTURE = Path(__file__).with_name('atlas-study-outcomes-legacy.json')
spec = importlib.util.spec_from_file_location('proposed_study_outcomes', MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class StudyDisplayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get('ATLAS_STUDY_TEST_SCRATCH'))
        self.counter = itertools.count()

    def tearDown(self):
        self.tmp.cleanup()

    def fixture(self, goals, header=None):
        directory = Path(self.tmp.name)/str(next(self.counter))
        (directory/'results').mkdir(parents=True)
        acceptance = b'{"fixture":"synthetic display criteria"}\n'
        acceptance_sha = hashlib.sha256(acceptance).hexdigest()
        result = {'cases':[{'id':'fixture-case'}], 'study_goals':goals,
                  'acceptance_sha256':acceptance_sha if header is None else header}
        raw = (json.dumps(result, ensure_ascii=False)+'\n').encode()
        (directory/'acceptance.json').write_bytes(acceptance)
        (directory/'results/result.json').write_bytes(raw)
        return {'directory':directory, 'base':'/code/display-fixture/',
                'manifest':{'files':{'results/result.json':hashlib.sha256(raw).hexdigest(),
                                     'acceptance.json':acceptance_sha}}}

    def test_true_false_null_and_missing_scalar_measurements_are_distinct(self):
        original = {'P/met':{'observed':True,'actual':.2,'target':.3},
                    'P/unmet':False, 'P/null-record':{'observed':None,'actual':None,'target':1.7},
                    'P/raw-null':None, 'P/raw-true':True,
                    'P/uncertain':{'observed':True,'simultaneous_classification':'unresolved'}}
        data = self.fixture(original)
        projected = m.project_study_outcomes(data, 'fixture-case', 'P/', 'https://example.invalid')
        self.assertEqual(projected['counts'], {'met':3,'unmet':1,'unresolved':2,'total':6})
        rows = {row['name']:row for row in projected['goals']}
        self.assertIsNone(rows['P/null-record']['observed'])
        self.assertIsNone(rows['P/null-record']['stored']['actual'])
        self.assertIs(rows['P/unmet']['observed'], False)
        self.assertEqual(rows['P/uncertain']['stored']['simultaneous_classification'], 'unresolved')
        self.assertEqual(original, {row['name']:row['stored'] for row in projected['goals']})
        html = m.study_outcomes_html(projected, 'en')
        self.assertIn('3 met, 1 unmet, 2 unresolved', html)
        self.assertIn('&quot;actual&quot;:null', html)
        self.assertIn('<details>', html)
        self.assertIn('not statistical certification', html)
        self.assertIn('未確定2', m.study_outcomes_html(projected, 'ja'))
        markdown = m.study_outcomes_markdown(projected, 'en')
        self.assertIn('"actual": null', markdown)
        self.assertEqual(json.loads(json.dumps(projected))['goals'], projected['goals'])

    def test_absent_selector_is_no_io_legacy_path(self):
        self.assertIsNone(m.project_study_outcomes({}, 'old-case', None, ''))
        self.assertEqual(m.study_outcomes_html(None,'ja'), '')
        self.assertEqual(m.study_outcomes_markdown(None,'en'), '')

    def test_result_byte_mutation_rejected_even_if_json_semantics_same(self):
        data = self.fixture({'P/a':True})
        path = data['directory']/'results/result.json'
        path.write_bytes(path.read_bytes()+b'\n')
        with self.assertRaises(ValueError):
            m.project_study_outcomes(data,'fixture-case','P/','')

    def test_acceptance_bytes_and_result_header_are_both_bound(self):
        data = self.fixture({'P/a':True})
        (data['directory']/'acceptance.json').write_bytes(b'{}\n')
        with self.assertRaises(ValueError):m.project_study_outcomes(data,'fixture-case','P/','')
        data = self.fixture({'P/a':True},header='b'*64)
        with self.assertRaises(ValueError):m.project_study_outcomes(data,'fixture-case','P/','')

    def test_unknown_case_empty_prefix_and_missing_prefix_fail_closed(self):
        data = self.fixture({'P/a':True})
        for ident,prefix in [('unknown','P/'),('fixture-case',''),('fixture-case','Q/')]:
            with self.subTest(ident=ident,prefix=prefix):
                with self.assertRaises(ValueError):m.project_study_outcomes(data,ident,prefix,'')

    def test_integer_string_and_missing_observed_are_not_coerced(self):
        for value in [0,1,'false',{'actual':1.}]:
            with self.subTest(value=value):
                data = self.fixture({'P/a':value})
                with self.assertRaises(ValueError):m.project_study_outcomes(data,'fixture-case','P/','')

    def test_html_escapes_names_and_records(self):
        projected=m.project_study_outcomes(self.fixture({'P/<script>':{'observed':False,'note':'<unsafe>'}}),
                                            'fixture-case','P/','https://example.invalid')
        html=m.study_outcomes_html(projected,'en')
        self.assertNotIn('<script>',html)
        self.assertNotIn('<unsafe>',html)
        self.assertIn('&lt;script&gt;',html)

    def namespaces(self,path):
        # Execute function definitions only, never imports or build().
        tree=ast.parse(path.read_text())
        ns={'escape':escape,'Path':Path,'json':json,'re':re,'struct':struct,
            'ORIGIN':'https://example.invalid','INDEX':'/validation/',
            'depth_additional_figures':lambda *args:[],
            'depth_code_urls':lambda *args:[],
            'render_execution_navigation':lambda *args:'',
            'execution_navigation_markdown':lambda *args:''}
        ns.update({name:getattr(m,name) for name in ['project_study_outcomes','study_outcome_headline',
                                                  'study_outcomes_html','study_outcomes_markdown']})
        nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)]
        exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),ns)
        return ns,tree

    def test_legacy_bool_helper_and_full_render_outputs_unchanged_without_optin(self):
        baseline=json.loads(LEGACY_FIXTURE.read_text())
        ot=ast.parse(baseline['original_study_targets_source'])
        new,nt=self.namespaces(ROOT/'scripts/build-atlas-depth-examples.py')
        node=lambda tree:next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='original_study_targets')
        self.assertEqual(ast.dump(node(ot),include_attributes=False),ast.dump(node(nt),include_attributes=False))
        directory=Path(self.tmp.name)/'legacy'
        (directory/'results').mkdir(parents=True)
        png=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jJQsAAAAASUVORK5CYII=')
        (directory/'results/fixture-case.png').write_bytes(png)
        labels={'ja':'Fixture JA','en':'Fixture EN'}
        case={'id':'fixture-case',**{k:copy.deepcopy(labels) for k in ['title','summary','assumptions','algorithm','validation','limits']},
              'references':[{'id':'fixture','title':'Fixture reference','url':'https://example.invalid/ref',
                             'review_level':'synthetic-fixture-only','review':labels}]}
        data={'directory':directory,'base':'/code/fixture/','manifest':{'files':{}},
              'verification':{'archive':{'file':'fixture.zip','archive_directory':'fixture'}}}
        for legacy in [False,True]:
            measured={'metrics':{'fixture':1},'checks':{'fixture':True},'records':{'fixture':[1,2]}}
            if legacy:
                measured.update(original_target_results={'met':True,'unmet':False},
                    original_target_summary={'met':1,'total':2,'all_met':False,'acceptance_sha256':'a'*64})
            for lang in ['ja','en']:
                self.assertEqual(baseline['outputs'][str(legacy).lower()+'/'+lang+'/html'].encode('utf-8'),
                                 new['render_case'](case,measured,data,lang,{}).encode('utf-8'))
                self.assertEqual(baseline['outputs'][str(legacy).lower()+'/'+lang+'/markdown'].encode('utf-8'),
                                 new['markdown_case'](case,measured,data,lang).encode('utf-8'))


if __name__=='__main__':
    unittest.main(verbosity=2)
