import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const read=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(read(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const cases=['csvr-kinetic-kernel','csvr-langevin-harmonic','csvr-langevin-quartic'];
const methods=json('numerical-methods-atlas/methods/index.json').methods;

test('only CSVR and Langevin are implemented thermostats and old evidence remains the primary Langevin edition',()=>{
 const thermal=methods.filter(x=>x.group.id==='thermostats');
 assert.equal(thermal.length,12);
 assert.deepEqual(thermal.filter(x=>x.status==='educational-example').map(x=>x.id).sort(),['langevin-thermostat','stochastic-velocity-rescaling']);
 assert.equal(thermal.filter(x=>x.status==='planned').length,10);
 const langevin=thermal.find(x=>x.id==='langevin-thermostat');
 assert.equal(langevin.depth_release.group,'models');
 assert.deepEqual(langevin.depth_release.case_ids,['langevin-harmonic']);
 assert.equal(langevin.code_edition,'2026-11-22');
 assert.equal(langevin.depth_additional_releases.length,1);
 assert.deepEqual(langevin.depth_additional_releases[0].case_ids,cases.slice(1));
 assert.ok(langevin.execution_examples.some(x=>x.id==='langevin-harmonic'));
 for(const id of cases.slice(1))assert.ok(langevin.execution_examples.some(x=>x.id===id));
 assert.ok(!langevin.execution_examples.some(x=>x.id==='csvr-kinetic-kernel'),'CSVR bath diagnostic cannot be borrowed by the Langevin method');
 const csvr=thermal.find(x=>x.id==='stochastic-velocity-rescaling');
 assert.deepEqual(csvr.depth_release.case_ids,cases);
 assert.ok(csvr.code_urls.some(x=>x.endsWith('/thermostats/thermostats.py')));
 for(const row of thermal.filter(x=>x.status==='planned')){assert.deepEqual(row.code_urls,[]);assert.deepEqual(row.execution_examples,[]);}
});

test('old four immutable archives and the common 22-example registry remain byte-identical',()=>{
 const expected={foundations:'1d130f886c31647aa5ba565fb10703a64d8af249c5715b4b2301401a3cfe22e2',models:'18619b7f1223dbe33b58534d4e1248205decf9e706fa31c9e9517542530d379c',particles:'8d2c39d6166a6b8715329574ed699515b0aa5b1f4c08fbec46b97400c50025b6',mhd:'2e7eeaaacaeb918671228cc56ab333d0c4ca5a9879241846f5772594552d0b16'};
 for(const [group,hash] of Object.entries(expected))assert.equal(sha(`code/validated-examples/2026-11-22/${group}/atlas-${group}-2026-11-22.zip`),hash);
 assert.equal(sha('numerical-methods-atlas/code-and-data/examples.json'),'3fd85a15483d2a8abcd06fc9523da0f4cc7e45d4a835f06355ac424fd5af8cb7');
 const policy=read('.github/workflows/atlas-public-linux.yml');assert.ok(!policy.includes('workflow_run:')&&!policy.includes('cron:'));
 assert.ok(!read('.github/workflows/atlas-depth-linux.yml').match(/pyscf|matplotlib|quantum-periodic/i));
});

test('multiple-release resolution refuses wrong-case borrowing, duplicate releases and lost primary evidence',()=>{
 const source=String.raw`
import copy,json,sys
from pathlib import Path
sys.path.insert(0,'scripts')
from atlas_depth_release import depth_release_records
m=next(x for x in json.load(open('catalog/atlas-methods.json'))['methods'] if x['id']=='langevin-thermostat')
r=depth_release_records(Path.cwd(),m)
assert [x['group'] for x in r]==['models','thermostats']
for extra in [dict(m['depth_additional_releases'][0],case_ids=['csvr-kinetic-kernel']),m['depth_release']]:
 bad=copy.deepcopy(m);bad['depth_additional_releases']=[extra]
 try:depth_release_records(Path.cwd(),bad)
 except AssertionError:pass
 else:raise AssertionError('Borrowed or repeated evidence accepted')
`;
 execFileSync('python3',['-B','-c',source],{cwd:root,encoding:'utf8',timeout:30000});
});

test('new diagnostic and additional method do not inflate the physical-problem inventory',()=>{
 const index=json('numerical-methods-atlas/validation/index.json');
 assert.equal(index.case_count,58);assert.equal(index.groups.length,25);
 assert.equal(sha('code/validated-examples/2026-11-22/thermostats/inputs.json'),'8097b48107f42800ce6883aeaf73f22cf37f01e2269884f2f965d85a315f2a38');
 assert.equal(json('code/validated-examples/2026-11-22/thermostats/verification.json').passed_tests,42);
 assert.equal(index.case_problem_ids['csvr-kinetic-kernel'],null);
 assert.equal(index.case_problem_ids['csvr-langevin-harmonic'],'langevin-harmonic');
 assert.equal(index.case_problem_ids['csvr-langevin-quartic'],'thermostatted-quartic');
 const inventory=json('numerical-methods-atlas/test-cases/index.json');
 assert.equal(inventory.problems.length,92);
 assert.ok(!inventory.problems.some(x=>x.id==='csvr-kinetic-kernel'));
 const harmonic=inventory.problems.find(x=>x.id==='langevin-harmonic');
 assert.ok(harmonic.supplemental_examples.some(x=>x.id==='langevin-harmonic'));
 assert.ok(harmonic.supplemental_examples.some(x=>x.id==='csvr-langevin-harmonic'));
 for(const id of cases){
  const page=json(`numerical-methods-atlas/validation/${id}/index.json`);
  assert.ok(page.measured.passed);
  assert.ok(page.references.some(r=>r.doi==='10.1063/1.2408420'));
  assert.ok(page.references.some(r=>r.doi==='10.1016/j.cpc.2008.01.006'));
  for(const lang of ['ja','en'])assert.ok(page.limits[lang]&&page.validation[lang]);
 }
});
