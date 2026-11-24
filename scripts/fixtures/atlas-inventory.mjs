// Current registration expectations come from canonical inputs. Immutable
// release counts, hashes and numerical golden values stay in their own tests.
import {readFileSync} from 'node:fs';
const root=new URL('../../',import.meta.url),read=path=>JSON.parse(readFileSync(new URL(path,root)));
const registration=read('catalog/atlas-registration.json');
const methods=read(registration.methods_catalog).methods;
const supplements=read(registration.supplements_catalog);
export const methodIds=methods.map(row=>row.id);
export const methodCount=methodIds.length;
export const methodStatusCounts=Object.fromEntries(['educational-example','reading-only','planned'].map(status=>[status,methods.filter(row=>row.status===status).length]));
export const supplementGroupIds=supplements.groups.map(row=>row.id);
export const supplementCaseIds=supplements.groups.flatMap(row=>{
 const value=read('code/validated-examples/'+(row.edition||supplements.edition)+'/'+row.id+'/cases.json');return (Array.isArray(value)?value:value.cases).map(x=>x.id);
});

// General inventory sizes are canonical. Historical preservation tests below
// exclude later additions while retaining every original hash/golden value.
export const supplementCaseCount=supplementCaseIds.length;
export const supplementGroupCount=supplementGroupIds.length;
const problemRows=read('catalog/atlas-test-problems.json').problems;
export const problemCount=problemRows.length;
export const equationCount=read('catalog/atlas-equations.json').equations.length;
const mapped=Object.values(supplements.case_problem_ids).filter(x=>x!==null);
export const supplementalMappedCaseCount=mapped.length;
export const supplementalProblemCount=new Set(mapped).size;
export const runnableProblemCount=new Set([...read('catalog/atlas-execution-examples.json').examples.map(x=>x.problem_id),...mapped]).size;
const batch37=read('scripts/fixtures/atlas-batch38-47-baseline.json');
const oldGroups=new Set(batch37.release_registry.releases.map(x=>x.group));
const oldProblems=new Set(batch37.gallery_items.map(x=>x.id));
export const groupsAddedAfterBatch37=supplementGroupIds.filter(x=>!oldGroups.has(x));
const oldCases=new Set(batch37.release_registry.releases.flatMap(x=>x.case_ids));
export const examplesAddedAfterBatch37=[...new Set([...problemRows.map(x=>x.id).filter(x=>!oldProblems.has(x)),...supplementCaseIds.filter(x=>!oldCases.has(x))])];

export const equationsAddedAfterBatch37=read('catalog/atlas-equations.json').equations.map(x=>x.id).filter(x=>!Object.hasOwn(batch37.equation_formulas,x));

// Explicit metadata projection only for historical goldens. Current science
// fields remain in each golden and the batch38 preservation test below.
export function projectMethodBeforeBatch38(row){
 const previous=batch37.method_append_fields_before_batch38[row.id];
 if(!previous)return row;
 const copy={...row};
 for(const key of ['summary','limitations','depth_release','depth_additional_releases','supplemental_scope_profiles','metadata_review','depth_scope']){
  if(Object.hasOwn(previous,key))copy[key]=previous[key];else delete copy[key];
 }
 return copy;
}

export const problemGroupCounts=Object.fromEntries([...new Set(problemRows.map(x=>x.group))].map(g=>[g,problemRows.filter(x=>x.group===g).length]));
