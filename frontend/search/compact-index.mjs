/** Decode a fixed public vocabulary; fetch only fixed same-site detail assets. */
const decoded=new WeakMap(),pending=new Map();
const MAX_TERMS=500000,MAX_VOCABULARY_UNITS=8200000;
function vocabulary(data){
 const packed=data.terms;
 if(!Array.isArray(packed))throw Error('Invalid search vocabulary');
 if(data.vocabulary_encoding===undefined){
  if(packed.length>MAX_TERMS||packed.some(word=>typeof word!=='string'))throw Error('Invalid search vocabulary');
  return packed;
 }
 if(data.vocabulary_encoding!=='unicode-prefix-flat-v1'||packed.length%2||packed.length>2*MAX_TERMS)throw Error('Invalid search vocabulary');
 const words=[];let previous=[],units=0;
 for(let i=0;i<packed.length;i+=2){
  const prefix=packed[i],suffix=packed[i+1];
  if(!Number.isInteger(prefix)||prefix<0||prefix>previous.length||typeof suffix!=='string'||/[\uD800-\uDFFF]/u.test(suffix))throw Error('Invalid search vocabulary');
  if(suffix.length>MAX_VOCABULARY_UNITS-units)throw Error('Invalid search vocabulary');
  // Python len/slicing count Unicode code points, unlike JS string offsets.
  const points=previous.slice(0,prefix).concat(Array.from(suffix)),word=points.join('');
  units+=word.length;if(units>MAX_VOCABULARY_UNITS)throw Error('Invalid search vocabulary');
  words.push(word);previous=points;
 }
 return words;
}
function varints(value,limit){
 if(typeof value!=='string'||value.length>4*MAX_TERMS||! /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(value))throw Error('Invalid search terms');
 const raw=atob(value);
 if(btoa(raw)!==value)throw Error('Invalid search terms');
 const values=[];let number=0,factor=1,bytes=0;
 for(let i=0;i<raw.length;i++){
  const byte=raw.charCodeAt(i);number+=(byte%128)*factor;bytes++;
  if(number>=limit||bytes>3)throw Error('Invalid search terms');
  if(byte<128){
   if(bytes>1&&byte===0)throw Error('Invalid search terms');
   values.push(number);if(values.length>MAX_TERMS)throw Error('Invalid search terms');
   number=0;factor=1;bytes=0;
  }else factor*=128;
 }
 if(bytes)throw Error('Invalid search terms');
 return values;
}
export function unpackSearchIndex(data){
 if(data?.format!=='compact-search-v1')return data;
 if(decoded.has(data))return decoded.get(data);
 const words=vocabulary(data),binary=data.term_encoding==='sorted-delta-varint-base64';
 if(data.term_encoding!==undefined&&!['sorted-delta','sorted-delta-varint-base64'].includes(data.term_encoding))throw Error('Invalid search terms');
 const expand=indices=>{
  if(binary)indices=varints(indices,words.length);
  if(!Array.isArray(indices))throw Error('Invalid search terms');
  let previous=0;
  return indices.map((delta,position)=>{
   if(!Number.isInteger(delta)||delta<0)throw Error('Invalid search terms');
   if(binary&&position>0&&delta===0)throw Error('Invalid search terms');
   const index=binary||data.term_encoding==='sorted-delta'?previous+delta:delta;previous=index;
   if(index>=words.length)throw Error('Invalid search terms');
   return words[index];
  }).join(' ');
 };
 const field=data.kind==='atlas'?'entries':'documents';
 if(!Array.isArray(data[field])||data[field].length>2000)throw Error('Invalid search records');
 const rows=data[field].map(row=>{
  const terms=row.search_terms;
  const searchText=Array.isArray(terms)||typeof terms==='string'?expand(terms):Object.fromEntries(Object.entries(terms||{}).map(([language,ids])=>[language,expand(ids)]));
  const {search_terms,...record}=row;return {...record,search_text:searchText};
 });
 const {terms,vocabulary_encoding,...rest}=data;
 // Preserve the legacy unpacked record/header API; storage codecs are private
 // to this loader. Both old numeric arrays and the new byte strings decode here.
 if(binary)rest.term_encoding='sorted-delta';
 const result={...rest,format:'unpacked-search-v1',[field]:rows};decoded.set(data,result);return result;
}
export function searchDetailURL(key){
 if(typeof key!=='string'||! /^[a-f0-9]{64}$/.test(key))throw Error('Invalid search detail key');
 return new URL('./details/'+key+'.json',import.meta.url);
}
export function loadSearchDetail(key){
 const url=searchDetailURL(key);
 if(!pending.has(key))pending.set(key,fetch(url,{credentials:'omit'}).then(response=>{
  if(!response.ok)throw Error('Search detail unavailable');return response.json();
 }).then(data=>{if(!data||typeof data!=='object'||Array.isArray(data))throw Error('Invalid search detail');return data;}).catch(error=>{pending.delete(key);throw error;}));
 return pending.get(key);
}
