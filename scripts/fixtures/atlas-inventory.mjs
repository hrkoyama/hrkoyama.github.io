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
