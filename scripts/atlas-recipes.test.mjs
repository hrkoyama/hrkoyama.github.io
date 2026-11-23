import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
const root=new URL('../',import.meta.url);
const text=p=>readFileSync(new URL(p,root),'utf8');
const json=p=>JSON.parse(text(p));
const sha=p=>createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex');
const registry=json('catalog/atlas-execution-examples.json');
const targets=['advection-sine','sod','shu-osher','poisson-1d-dirichlet','poisson-2d-sine','bratu','harmonic-oscillator','stiff-cosine','smooth-function-projection','isolated-particles','periodic-particles','taylor-green','brio-wu','hydrogenic-atoms','helium-ground-state','logistic-growth','sir-epidemic','mc-integral','gbm-sde','h2-rhf','periodic-he-dft','periodic-he-forces'];
const prefix='code/numerical-methods-atlas/2026-11-22/';
const path=url=>new URL(url).pathname.slice(1);
const supplementalProblemIds=['matrix-factorization','krylov-spectrum','quadrature-moments','gaussian-mcmc','langevin-harmonic','reaction-diffusion-fourier','turing-schnakenberg','fitzhugh-nagumo','neutral-periodic-charges','logarithmic-particles','cold-plasma-pic','maxwell-collisions','absorbing-slab','thermostatted-quartic','mcmc-bimodal-mixture','advected-magnetostatic-equilibrium'];

test('all 22 runnable representative problems have one reproduction record within the 83-problem inventory',()=>{
  assert.equal(registry.examples.length,22);
  assert.deepEqual(registry.examples.map(x=>x.problem_id).sort(),[...targets].sort());
  assert.equal(json('catalog/atlas-test-problems.json').problems.length,87);
  assert.equal(json('numerical-methods-atlas/coverage.json').counts.test_problems,87);
  assert.equal(registry.examples.filter(x=>x.release.family==='numerical-methods-atlas'&&x.release.version==='2026-11-22').length,12);
  for(const id of ['barnes-hut','hydrogenic-atoms','helium-ground-state'])assert.equal(registry.examples.find(x=>x.id===id).release.version,'2026-11-21');
});

test('sixteen additional physical problems bind to successful immutable supplements without multiplying shared cases',()=>{
  const inventory=json('catalog/atlas-test-problems.json').problems;
  const mapping=json('catalog/atlas-depth-expansion.json').case_problem_ids;
  const selected=inventory.filter(x=>supplementalProblemIds.includes(x.id));
  assert.equal(selected.length,16);
  const earlier=inventory.filter(x=>!['noh','sedov','guderley','zalesak'].includes(x.id));
  assert.equal(earlier.length-selected.length,67,'the historical representative/supplemental distinction remains intact');
  assert.equal(inventory.filter(x=>x.id!=='zalesak').length-selected.length,70);
  assert.equal(inventory.filter(x=>x.id==='noh').length,1);
  assert.equal(mapping['noh-shock'],'noh');
  assert.equal(mapping.ewald,mapping.spme);assert.equal(mapping['glm-fourier-mode'],null);
  assert.equal(inventory.filter(x=>x.id==='neutral-periodic-charges').length,1);
  for(const problem of selected){
    assert.equal(problem.availability,'saved-output');
    assert.ok(problem.supplemental_examples.length);
    for(const item of problem.supplemental_examples){
      assert.equal(mapping[item.id],problem.id);
      const entry=json(item.url.slice(1)+'index.json');
      assert.equal(entry.problem_id,problem.id);
      const base=path(entry.release.base);
      const results=json(base+'results/result.json'),receipt=json(base+'verification.json');
      assert.equal(results.passed,true);assert.equal(receipt.all_cases_rerun,true);assert.equal(receipt.passed,true);
      assert.equal(results.input_sha256,sha(base+'inputs.json'));
      assert.equal(entry.source_sha256[base+'results/result.json'],sha(base+'results/result.json'));
      const row=results.cases.find(x=>x.id===item.id);assert.ok(row);
      assert.equal(row.passed,true);assert.ok(Object.keys(row.checks).length>0&&Object.values(row.checks).every(x=>x===true));
      assert.ok(receipt.case_ids.includes(item.id));
      if(base===problem.code_base.slice(1))assert.ok(problem.evidence.some(x=>x.path===base+'results/result.json'&&x.json_pointer==='/cases'&&x.where?.id===item.id));
      assert.ok(existsSync(new URL(base+'results/'+item.id+'.png',root)));
      assert.ok(existsSync(new URL(item.url.slice(1)+'index.html',root)));
    }
  }
  assert.deepEqual(selected.find(x=>x.id==='neutral-periodic-charges').supplemental_examples.map(x=>x.id),['ewald','spme','ewald-convergence','spme-convergence']);
});

test('new recipes expose the exact fixed input, measured acceptance criteria and populated numerical output',()=>{
  for(const example of registry.examples.filter(x=>x.release.family==='numerical-methods-atlas'&&x.release.version==='2026-11-22')){
    const input=json(path(example.inputs.url));
    assert.equal(input.problem_id,example.problem_id);
    assert.ok(input.acceptance.length>=3,example.id+' meaningful criteria');
    const result=json(path(example.outputs.find(x=>x.id==='results').url));
    assert.equal(result.input_sha256,sha(path(example.inputs.url)));
    assert.equal(result.status,'passed');assert.equal(result.passed,true);
    assert.deepEqual(result.parameters,input.parameters);
    for(const check of input.acceptance){
      const published=example.checks.find(c=>c.id===check.id);
      assert.ok(published,example.id+'/'+check.id);
      assert.equal(published.pointer,'/metrics/'+check.metric);
      assert.equal(published.comparison,check.comparison);
      assert.equal(published.tolerance,check.tolerance);
      assert.equal(published.expected,check.expected);
      assert.equal(result.checks[check.id],true);
    }
    assert.ok(example.failure_scope.ja&&example.failure_scope.en);
    const csv=text(path(example.outputs.find(x=>x.format==='csv').url)).trim().split(/\r?\n/);
    assert.equal(csv.length-1,result.table.rows);
    const columns=csv.shift().split(',');assert.deepEqual(columns,result.table.columns);
    for(const row of csv){const values=row.split(',');assert.equal(values.length,columns.length);assert.ok(values.every(v=>v.trim()&&Number.isFinite(Number(v))));}
    assert.ok(example.commands.run.includes('run_recipe.py --input recipes/'+example.id+'.json'));
  }
});

test('recipe adapters preserve the verified numerical solver source and distinguish references from exact solutions',()=>{
  const original=json('code/numerical-methods-atlas/2026-11-21/source-manifest.json');
  for(const file of Object.keys(original.files).filter(x=>x.startsWith('numart/')))assert.equal(sha(prefix+file),original.files[file],file);
  for(const id of ['shu-osher','brio-wu']){
    const example=registry.examples.find(x=>x.id===id);
    assert.ok(example.references.some(x=>x.type==='numerical-refinement'),id+' numerical reference');
    assert.match(example.scope.en+' '+example.failure_scope.en+' '+example.reference_notes.en,/not exact|not an exact|no exact|neither exact/i,id+' limited claim');
  }
  const verification=json(prefix+'verification.json');
  assert.equal(verification.failures,0);assert.equal(verification.errors,0);
  assert.ok(verification.passed>411);
  assert.equal(verification.skipped,6);
});

test('convergence lower bounds reject weak, missing, boolean and non-finite observations',()=>{
  const script=`import importlib.util\ns=importlib.util.spec_from_file_location('b','scripts/build-atlas-execution-examples.py');b=importlib.util.module_from_spec(s);s.loader.exec_module(b)\nc={'id':'order','pointer':'/order','comparison':'minimum','tolerance':1.8}\nassert b.evaluate_check({'order':1.99},c)['passed']\nfor v in [1.2,True,float('nan'),float('inf')]:assert not b.evaluate_check({'order':v},c)['passed']\nassert not b.evaluate_check({},c)['passed']\nprint('ok')`;
  assert.match(execFileSync('python3',['-c',script],{cwd:root,encoding:'utf8'}),/ok/);
});

test('all twenty-two are rerun from the exact public registry and the guide displays that receipt',()=>{
  const preferred=registry.verification_receipt.replace(/\.json$/,'-public.json');
  const url=existsSync(new URL(path(preferred),root))?preferred:registry.verification_receipt;
  const receipt=json(path(url));
  assert.equal(receipt.registry_source_mode,'public-registry');
  assert.equal(receipt.registry_url,'https://hrkoyama.github.io/numerical-methods-atlas/code-and-data/examples.json');
  assert.equal(receipt.registry_sha256,sha('numerical-methods-atlas/code-and-data/examples.json'));
  assert.equal(receipt.passed,true);
  assert.equal(receipt.unique_runner_executions,21);
  assert.deepEqual(receipt.examples.map(x=>x.id).sort(),registry.examples.map(x=>x.id).sort());
  for(const row of receipt.examples){assert.equal(row.execution.completed,true);assert.equal(row.validation.passed,true);assert.equal(row.passed,true);}
  assert.ok(text('numerical-methods-atlas/code-and-data/index.html').includes('href="'+url+'"'));
});
